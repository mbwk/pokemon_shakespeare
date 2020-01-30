from starlette.testclient import TestClient

from pokemon_shakespeare import __version__
from pokemon_shakespeare.main import app


client = TestClient(app)


def test_version():
    assert __version__ == "0.1.0"


def test_read_pokemon_normal():
    response = client.get("/pokemon/charizard")

    assert response.ok


def test_read_pokemon_invalid():
    response = client.get("/pokemon/sonic")

    assert response.status_code == 404
