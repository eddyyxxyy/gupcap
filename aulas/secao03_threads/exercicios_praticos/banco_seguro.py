import random
import threading
import time

lock = threading.RLock()


class Conta:
    def __init__(self, saldo: int = 0) -> None:
        self.saldo = saldo


def criar_contas() -> list[Conta]:
    return [
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000)),
    ]


def pega_duas_contas(contas: list[Conta]) -> tuple[Conta, Conta]:
    c1 = random.choice(contas)
    c2 = random.choice(contas)
    while c1 == c2:
        c2 = random.choice(contas)
    return c1, c2


def servicos(contas: list[Conta], total: int) -> None:
    for _ in range(1, 10000):
        c1, c2 = pega_duas_contas(contas)
        valor = random.randint(1, 100)
        transferir(c1, c2, valor)
        valida_banco(contas, total)


def transferir(origem: Conta, destino: Conta, valor: int) -> None:
    if origem.saldo < valor:
        return
    with lock:
        origem.saldo -= valor
        time.sleep(0.001)
        destino.saldo += valor


def valida_banco(contas: list[Conta], total: int) -> None:
    with lock:
        atual = sum(conta.saldo for conta in contas)
    if atual != total:
        print(
            f'ERRO! Balanço bancário inconsistente. '
            + f'BRL$ {atual:.2f} vs BRL$ {total:.2f}',
            flush=True,
        )
    else:
        print(
            f'Tudo certo, Balanço bancário consistente. '
            + f'BRL$ {atual:.2f} vs BRL$ {total:.2f}',
            flush=True,
        )


def main() -> None:
    contas = criar_contas()
    with lock:
        total = sum(conta.saldo for conta in contas)
    print('Iniciando transferências...')

    # Se colocarmos várias threads, teremos o problema Race Conditions
    tarefas = [
        threading.Thread(target=servicos, args=(contas, total)),
        threading.Thread(target=servicos, args=(contas, total)),
        threading.Thread(target=servicos, args=(contas, total)),
    ]
    # Gerando diversos erros no programa

    [tarefa.start() for tarefa in tarefas]
    [tarefa.join() for tarefa in tarefas]

    print('Transferências concluídas.')
    valida_banco(contas, total)


if __name__ == '__main__':
    main()
