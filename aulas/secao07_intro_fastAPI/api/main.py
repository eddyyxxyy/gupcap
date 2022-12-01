from fastapi import FastAPI
from pydantic import BaseModel


class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    em_oferta: bool = False


app = FastAPI()

produtos = [
    Produto(id=1, nome='Playstation 5', preco=5745.55, em_oferta=True),
    Produto(id=2, nome='Nintendo Wii', preco=2654.12),
    Produto(id=3, nome='Xbox 360', preco=1765.34, em_oferta=True),
    Produto(id=4, nome='Super Nintendo', preco=234.67),
    Produto(id=5, nome='Atari 2600', preco=199.90, em_oferta=True),
]


@app.get('/')
async def index() -> dict:
    return {'Geek': 'University'}


@app.get('/produtos/{id}')
async def buscar_produto(id: int) -> Produto | None:
    for produto in produtos:
        if produto.id == id:
            return produto
    return None


@app.put('/produtos/{id}')
async def atualizar_produto(id: int, produto: Produto) -> Produto | None:
    for prod in produtos:
        if prod.id == id:
            prod = produto

            return prod
    return None
