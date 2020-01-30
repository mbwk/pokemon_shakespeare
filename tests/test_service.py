import json
from unittest import mock

from pokemon_shakespeare.service import (
    get_pokemon,
    shakespearean_pokemon,
)


with open("samples/charizard.json") as f:
    DUMMY_CHARIZARD_JSON = json.loads(str(f.read()))

DUMMY_SHAKESPEARE_DESC = (
    "Charizard flies 'round the sky in search of powerful opponents. 't "
    "breathes fire of such most wondrous heat yond 't melts aught. However, "
    "'t nev'r turns its fiery breath on any opponent weaker than itself."
)


@mock.patch("pokemon_shakespeare.service._get_pokeapi_pokemon")
def test_get_pokemon(mock_get):
    mock_get.return_value = DUMMY_CHARIZARD_JSON
    pokemon = get_pokemon("charizard")
    assert pokemon["name"] == "charizard"
    assert pokemon["description"] == (
        "Charizard flies around the sky in search of powerful opponents."
        "\nIt breathes fire of such great heat that it melts anything.\n"
        "However, it never turns its fiery breath on any opponent\nweaker"
        " than itself."
    )


@mock.patch("pokemon_shakespeare.service._get_funtranslations_shakespearean")
@mock.patch("pokemon_shakespeare.service._get_pokeapi_pokemon")
def test_shakespearean_pokemon(mock_pokemon, mock_funtranslate):
    mock_pokemon.return_value = DUMMY_CHARIZARD_JSON
    mock_funtranslate.return_value = DUMMY_SHAKESPEARE_DESC

    translated_pokemon = shakespearean_pokemon("charizard")
    assert translated_pokemon["name"] == "charizard"
    assert translated_pokemon["description"] == DUMMY_SHAKESPEARE_DESC
