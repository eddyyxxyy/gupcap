import asyncio


async def diz_oi_demorado(nome: str) -> None:
    print('Oi...')
    await asyncio.sleep(2)
    print(f'{nome}...')


if __name__ == '__main__':
    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)
    asyncio.run(diz_oi_demorado('Edson'))
