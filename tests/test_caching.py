import unittest
from unittest import mock

from pokemon_shakespeare.caching import cache_translation
from pokemon_shakespeare.exceptions import PokemonNotFoundError
from tests.resources import DUMMY_SHAKESPEARE_DESC


def _make_mock_external_call():
    mock_external_call = mock.Mock(
        return_value={"name": "charizard", "description": DUMMY_SHAKESPEARE_DESC}
    )
    assert mock_external_call.call_count == 0
    return mock_external_call


def test_decorator_intercepts_duplicate_calls():
    mock_external_call = _make_mock_external_call()
    wrapped_external_call = cache_translation(mock_external_call)

    mock_cache = dict()

    def mock_set(name: str, desc: str):
        mock_cache[name] = desc

    with mock.patch(
        "pokemon_shakespeare.caching._get_from_cache", wraps=mock_cache.get
    ):
        with mock.patch("pokemon_shakespeare.caching._set_in_cache", wraps=mock_set):
            wrapped_external_call("charizard")
            assert mock_external_call.called
            assert mock_external_call.call_count == 1
            for _ in range(3):
                wrapped_external_call("charizard")
            assert mock_external_call.call_count == 1


def test_decorator_allows_unique_calls():
    mock_external_call = _make_mock_external_call()
    wrapped_external_call = cache_translation(mock_external_call)

    mock_cache = dict()

    def mock_set(name: str, desc: str):
        mock_cache[name] = desc

    with mock.patch(
        "pokemon_shakespeare.caching._get_from_cache", wraps=mock_cache.get
    ):
        with mock.patch("pokemon_shakespeare.caching._set_in_cache", wraps=mock_set):
            wrapped_external_call("charizard")
            assert mock_external_call.called
            assert mock_external_call.call_count == 1
            wrapped_external_call("groudon")
            assert mock_external_call.call_count == 2


class UpstreamErrorHandlingTestCase(unittest.TestCase):
    def test_leave_cache_unchanged_on_upstream_error(self):
        mock_external_call = _make_mock_external_call()
        mock_external_call.side_effect = PokemonNotFoundError
        wrapped_external_call = cache_translation(mock_external_call)

        mock_cache = dict()

        def mock_set(name: str, desc: str):
            mock_cache[name] = desc

        with mock.patch(
            "pokemon_shakespeare.caching._get_from_cache", wraps=mock_cache.get
        ):
            with mock.patch(
                "pokemon_shakespeare.caching._set_in_cache", wraps=mock_set
            ):
                with self.assertRaises(PokemonNotFoundError):
                    wrapped_external_call("sonic")
                assert mock_cache.get("sonic") is None
