"""Configuration defaults for the SDK."""

from __future__ import annotations

from dataclasses import dataclass

DEFAULT_API_BASE_URL = "https://api.bling.com.br/Api/v3"
DEFAULT_TIMEOUT_SECONDS = 30.0


@dataclass(frozen=True, slots=True)
class BlingClientConfig:
    """Runtime configuration used to create SDK transports."""

    base_url: str = DEFAULT_API_BASE_URL
    timeout: float = DEFAULT_TIMEOUT_SECONDS
