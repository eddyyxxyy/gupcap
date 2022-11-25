import asyncio

import aiofiles


async def exemplo_arq1():
    async with aiofiles.open('texto.txt') as arquivo:
        conteudo = await arquivo.read()
    print(conteudo)


async def exemplo_arq2():
    async with aiofiles.open('texto.txt') as arquivo:
        async for linha in arquivo:
            print(linha)


def main():
    el = asyncio.new_event_loop()

    el.run_until_complete(exemplo_arq2())

    el.close()


if __name__ == '__main__':
    main()
