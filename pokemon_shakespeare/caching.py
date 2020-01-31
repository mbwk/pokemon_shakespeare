from typing import (
    Callable,
    Dict,
)


def _get_from_cache(name: str) -> str:
    raise NotImplementedError


def _set_in_cache(name: str, description: str):
    raise NotImplementedError


def cache_translation(
    external_call: Callable[[str], Dict[str, str]]
) -> Callable[[str], Dict[str, str]]:
    def inner(name: str) -> Dict[str, str]:
        existing = _get_from_cache(name)
        if existing:
            return {
                "name": name,
                "description": existing,
            }
        new = external_call(name)
        _set_in_cache(name, new["description"])
        return new

    return inner
