class PokemonNotFoundError(Exception):
    pass


class RatelimitedError(Exception):
    pass


class CacheError(Exception):
    pass
