POKEAPI_BASE = "https://pokeapi.co/api/v2/"

FUNTRANSLATIONS_BASE = "https://api.funtranslations.com/translate/"


def _get_pokeapi_pokemon(name: str) -> dict:
    raise NotImplementedError


def get_pokemon(name: str) -> dict:
    pokeapi_dict = _get_pokeapi_pokemon(name)
    flavor_texts = pokeapi_dict["flavor_text_entries"]
    selected_flavor_text = flavor_texts[1]
    return {
        "name": name,
        "description": selected_flavor_text["flavor_text"],
    }


def _get_funtranslations_shakespearean(text: str) -> str:
    raise NotImplementedError


def translate_text(text: str) -> str:
    no_newlines = text.replace("\n", " ")
    return _get_funtranslations_shakespearean(no_newlines)


def shakespearean_pokemon(name: str) -> dict:
    pokemon = get_pokemon(name)
    pokemon["description"] = translate_text(pokemon["description"])
    return pokemon
