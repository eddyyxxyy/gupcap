import datetime

import computa


def main() -> None:
    inicio = datetime.datetime.now()
    computa.computar(fim=50_000_000)
    fim = datetime.datetime.now() - inicio

    print(f'Terminou em "{fim.total_seconds():.2f}" segundos.')


if __name__ == '__main__':
    main()
