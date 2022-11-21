import datetime
import math
import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor as Executer


def computar(inicio: int = 1, *, fim) -> None:
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.prod([pos - fator, pos * fator])


def main() -> None:
    quantidade_cores = multiprocessing.cpu_count()
    print(
        f'Realizando o processamento matemático com {quantidade_cores} cores(s).'
    )

    inicio = datetime.datetime.now()

    with Executer(max_workers=quantidade_cores) as executer:
        for core in range(1, quantidade_cores + 1):
            ini = 50_000_000 * (core - 1) / quantidade_cores
            fim = 50_000_000 * core / quantidade_cores
            print(f'Core {core}: processando de {ini} até {fim}.')
            executer.submit(computar, inicio=ini, fim=fim)

    fim = datetime.datetime.now() - inicio

    print(f'Terminou em "{fim.total_seconds():.2f}" segundos.')


if __name__ == '__main__':
    main()


"""
Teste do arquivo performance_padrao_python da seção 2: Terminou em "13.06" segundos.
Teste do arquivo performance_python_threads da seção 3: Terminou em "9.06" segundos.
Teste do arquivo performance_python_multiprocessos da seção 3: Terminou em "3" segundos.
"""
