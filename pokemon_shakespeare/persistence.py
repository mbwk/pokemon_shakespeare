import redis

from pokemon_shakespeare.exceptions import CacheError
from pokemon_shakespeare.settings import getconfig


def get_storage() -> redis.Redis:
    try:
        client = redis.Redis(
            host=str(getconfig("REDIS_HOST")),
            port=int(getconfig("REDIS_PORT")),
            db=int(getconfig("REDIS_DB")),
        )
        return client
    except redis.ConnectionError:
        raise CacheError
    finally:
        pass
