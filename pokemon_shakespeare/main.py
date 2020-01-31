from pokemon_shakespeare.exceptions import PokemonNotFoundError
from pokemon_shakespeare.service import shakespearean_pokemon

from fastapi import FastAPI
from starlette.exceptions import HTTPException


app = FastAPI()


@app.get("/")
def read_root() -> str:
    return "Hello, world!"


@app.get("/pokemon/{pokemon}")
def read_pokemon(pokemon: str) -> dict:
    try:
        return shakespearean_pokemon(pokemon)
    except PokemonNotFoundError:
        raise HTTPException(404)
