"""Core API."""

import os
import json

from typing import Any, Dict
from functools import lru_cache


DEFAULT_PATH_SECRETS_FILE = "~/.glosm.json"


@lru_cache(maxsize=128)
def _secrets(path_secrets_file: str = None) -> Dict:

    with open(os.path.expanduser(path_secrets_file or DEFAULT_PATH_SECRETS_FILE), "r") as f:
        return json.load(f)


def get(*keys) -> Any:
    """Get a secret, specified by one or more keys. Without any keys, return all secrets.

    The keys are traversed recursively. If `get()` returns `{1: {2: {3: 4}}}` then `get(1, 2, 3)` will return `4`.
    """

    secrets = _secrets()

    if not keys:
        return secrets

    result = secrets
    for key in keys:
        result = result[key]

    return result
