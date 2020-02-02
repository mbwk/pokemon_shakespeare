from fastapi import FastAPI, HTTPException

import pokemon_shakespeare
from pokemon_shakespeare.exceptions import (
    PokemonNotFoundError,
    RatelimitedError,
)
from pokemon_shakespeare.service import (
    shakespearean_pokemon,
    normalize_pokemon_name,
)


app = FastAPI()


@app.get("/")
def read_root() -> str:
    return "Pokemon Shakespeare API v{}".format(pokemon_shakespeare.__version__)


@app.get("/pokemon/{pokemon}")
def read_pokemon(pokemon: str) -> dict:
    try:
        return shakespearean_pokemon(normalize_pokemon_name(pokemon))
    except PokemonNotFoundError:
        raise HTTPException(404, detail="Pokemon not found.")
    except RatelimitedError:
        raise HTTPException(
            429, detail="Too many new translation requests within one hour."
        )
