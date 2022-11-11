import time
from queue import Queue
from threading import Thread

import colorama


def gerador_de_dados(queue: Queue) -> None:
    for i in range(1, 11):
        print(colorama.Fore.GREEN + f'Dado {i} gerado.', flush=True)
        time.sleep(2)
        queue.put(i)


def consumidor_de_dados(queue: Queue) -> None:
    while queue.qsize() > 0:
        valor = queue.get()
        print(colorama.Fore.RED + f'Dado {valor ** 2} processado.', flush=True)
        time.sleep(1)


def main() -> None:
    print(colorama.Fore.WHITE + 'Sistema iniciado.', flush=True)
    queue = Queue()
    th1 = Thread(target=gerador_de_dados, args=(queue,))
    th2 = Thread(target=consumidor_de_dados, args=(queue,))

    # Geramos os dados que são a dependência da Thread 2
    th1.start()
    th1.join()

    # Utilizamos os dados gerados
    th2.start()
    th2.join()


if __name__ == '__main__':
    main()
