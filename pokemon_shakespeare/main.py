from fastapi import FastAPI, HTTPException

from pokemon_shakespeare.exceptions import (
    PokemonNotFoundError,
    RatelimitedError,
)
from pokemon_shakespeare.service import shakespearean_pokemon


app = FastAPI()


@app.get("/")
def read_root() -> str:
    return "Hello, world!"


@app.get("/pokemon/{pokemon}")
def read_pokemon(pokemon: str) -> dict:
    try:
        return shakespearean_pokemon(pokemon)
    except PokemonNotFoundError:
        raise HTTPException(404, detail="Pokemon not found.")
    except RatelimitedError:
        raise HTTPException(
            429, detail="Too many new translation requests within one hour."
        )
