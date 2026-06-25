"""Configuration defaults for the SDK."""

from __future__ import annotations

import os

from dotenv import load_dotenv as _load_dotenv

_loaded = False


def load_env() -> None:
    """Lazy-load ``.env`` file variables. Idempotent — safe to call multiple times."""
    global _loaded  # noqa: PLW0603
    if _loaded:
        return
    _load_dotenv(override=False)
    _loaded = True


is_dev: str | None = os.environ.get("BLING_ENV")

if is_dev and is_dev == "dev":
    base_url = "https://api.bling.com.br/Api/v3/homologacao"
else:
    base_url = "https://api.bling.com.br/Api/v3"

DEFAULT_API_BASE_URL = base_url
DEFAULT_TIMEOUT_SECONDS = 30.0
DEFAULT_RATE_LIMIT_MAX_REQUESTS = 3
DEFAULT_RATE_LIMIT_PERIOD_SECONDS = 1.0
DEFAULT_RETRY_AFTER_RATE_LIMIT_SECONDS = 1.0
DEFAULT_RATE_LIMIT_MAX_RETRIES = 3
