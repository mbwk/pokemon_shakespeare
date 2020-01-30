POKEAPI_BASE = "https://pokeapi.co/api/v2/"

FUNTRANSLATIONS_BASE = "https://api.funtranslations.com/translate/"


def _get_pokeapi_pokemon(name: str) -> dict:
    raise NotImplementedError


def get_pokemon(name: str) -> dict:
    raise NotImplementedError


def _get_funtranslations_shakespearean(text: str) -> str:
    raise NotImplementedError


def translate_text(text: str) -> str:
    raise NotImplementedError


def shakespearean_pokemon(name: str) -> dict:
    raise NotImplementedError
