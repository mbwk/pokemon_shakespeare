from typing import (
    Callable,
    Dict,
    Optional,
)


from pokemon_shakespeare.persistence import get_storage


def _get_from_cache(name: str) -> Optional[str]:
    r = get_storage()
    value = r.get(name)
    return value.decode("utf8") if value else None


def _set_in_cache(name: str, description: str):
    r = get_storage()
    r.set(name, description)


def get_available_translations():
    r = get_storage()
    return [name.decode("utf8") for name in r.keys()]


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
