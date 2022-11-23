import asyncio


async def diz_oi(nome: str) -> None:
    print(f'Oi, {nome}.')


if __name__ == '__main__':
    el = asyncio.new_event_loop()
    asyncio.set_event_loop(el)
    asyncio.run(diz_oi('Edson'))
