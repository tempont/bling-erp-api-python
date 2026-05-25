"""Configuration defaults for the SDK."""

from __future__ import annotations

from dataclasses import dataclass

DEFAULT_API_BASE_URL = "https://api.bling.com.br/Api/v3"
DEFAULT_TIMEOUT_SECONDS = 30.0
DEFAULT_RATE_LIMIT_MAX_REQUESTS = 3
DEFAULT_RATE_LIMIT_PERIOD_SECONDS = 1.0
DEFAULT_RETRY_AFTER_RATE_LIMIT_SECONDS = 1.0
DEFAULT_RATE_LIMIT_MAX_RETRIES = 3


@dataclass(frozen=True, slots=True)
class BlingClientConfig:
    """Runtime configuration used to create SDK transports."""

    base_url: str = DEFAULT_API_BASE_URL
    timeout: float = DEFAULT_TIMEOUT_SECONDS
    rate_limit_max_requests: int = DEFAULT_RATE_LIMIT_MAX_REQUESTS
    rate_limit_period_seconds: float = DEFAULT_RATE_LIMIT_PERIOD_SECONDS
    rate_limit_max_retries: int = DEFAULT_RATE_LIMIT_MAX_RETRIES
