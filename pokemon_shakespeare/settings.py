import os
from typing import Any


DEFAULTS = {
    "REDIS_HOST": "localhost",
    "REDIS_PORT": 6379,
    "REDIS_DB": 0,
}


def getconfig(config_key: str) -> Any:
    config_value = os.getenv(config_key)
    return config_value if config_value is not None else DEFAULTS.get(config_key)
