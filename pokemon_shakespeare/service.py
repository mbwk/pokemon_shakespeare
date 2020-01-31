from urllib.parse import urljoin


from pokemon_shakespeare.caching import cache_translation
from pokemon_shakespeare.exceptions import (
    PokemonNotFoundError,
    RatelimitedError,
)


import requests


POKEAPI_BASE = "https://pokeapi.co/api/v2/"

FUNTRANSLATIONS_BASE = "https://api.funtranslations.com/translate/"


POKEMON_ENDPOINT = urljoin(POKEAPI_BASE, "pokemon-species/")


def _get_pokeapi_pokemon(name: str) -> dict:
    response = requests.get(urljoin(POKEMON_ENDPOINT, name))
    if response.status_code == 404:
        raise PokemonNotFoundError
    return dict(response.json())


def get_pokemon(name: str) -> dict:
    pokeapi_dict = _get_pokeapi_pokemon(name)
    flavor_texts = pokeapi_dict["flavor_text_entries"]
    selected_flavor_text = flavor_texts[1]
    return {
        "name": name,
        "description": selected_flavor_text["flavor_text"],
    }


SHAKESPEARE_ENDPOINT = urljoin(FUNTRANSLATIONS_BASE, "shakespeare.json")


def _get_funtranslations_shakespearean(text: str) -> dict:
    response = requests.post(SHAKESPEARE_ENDPOINT, data={"text": text})
    if response.status_code == 429:
        raise RatelimitedError
    return dict(response.json())


def translate_text(text: str) -> str:
    no_newlines = text.replace("\n", " ")
    resjson = _get_funtranslations_shakespearean(no_newlines)
    return str(resjson["contents"]["translated"])


@cache_translation
def shakespearean_pokemon(name: str) -> dict:
    pokemon = get_pokemon(name)
    pokemon["description"] = translate_text(pokemon["description"])
    return pokemon
