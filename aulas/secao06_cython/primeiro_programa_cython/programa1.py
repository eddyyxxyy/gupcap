import cumprimenta


def main() -> None:
    nome: str = input('Qual o seu nome?\n-> ')
    cumprimenta.cumprimentar(nome)


if __name__ == '__main__':
    main()
