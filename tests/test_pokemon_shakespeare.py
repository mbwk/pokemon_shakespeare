from unittest import mock

from starlette.testclient import TestClient

mock.patch("pokemon_shakespeare.caching.cache_translation", lambda x: x).start()

from pokemon_shakespeare import __version__
from pokemon_shakespeare.exceptions import (
    PokemonNotFoundError,
    RatelimitedError,
)
from pokemon_shakespeare.main import app
from tests.resources import (
    DUMMY_CHARIZARD_JSON,
    DUMMY_SHAKESPEARE_JSON,
)


client = TestClient(app)


def test_version():
    assert __version__ == "0.1.0"


@mock.patch("pokemon_shakespeare.service._get_funtranslations_shakespearean")
@mock.patch("pokemon_shakespeare.service._get_pokeapi_pokemon")
def test_read_pokemon_normal(mock_pokemon, mock_funtranslate):
    mock_pokemon.return_value = DUMMY_CHARIZARD_JSON
    mock_funtranslate.return_value = DUMMY_SHAKESPEARE_JSON
    response = client.get("/pokemon/charizard")

    assert response.ok


@mock.patch("pokemon_shakespeare.service._get_pokeapi_pokemon")
def test_read_pokemon_invalid(mock_pokemon):
    mock_pokemon.side_effect = PokemonNotFoundError
    response = client.get("/pokemon/sonic")

    assert response.status_code == 404


@mock.patch("pokemon_shakespeare.service._get_funtranslations_shakespearean")
@mock.patch("pokemon_shakespeare.service._get_pokeapi_pokemon")
def test_read_pokemon_ratelimited_by_upstream(mock_pokemon, mock_funtranslate):
    mock_pokemon.return_value = DUMMY_CHARIZARD_JSON
    mock_funtranslate.side_effect = RatelimitedError

    response = client.get("/pokemon/charizard")
    assert response.status_code == 429
