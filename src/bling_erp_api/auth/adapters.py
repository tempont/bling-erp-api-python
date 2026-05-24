"""Authentication adapters for SDK transports."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, Self

import httpx
from bling_jwt_auth import BlingAuth
from bling_jwt_auth.headers import bling_api_headers

if TYPE_CHECKING:
    from collections.abc import Callable, Generator


class AccessTokenProvider(Protocol):
    """Protocol implemented by objects that can return a valid access token."""

    def get_access_token(self) -> str:
        """Return a valid OAuth access token."""
        ...


class BlingAuthAdapter(httpx.Auth):
    """httpx auth adapter backed by a token provider from ``bling-jwt-auth``."""

    def __init__(
        self,
        token_provider: AccessTokenProvider,
        *,
        close_callback: Callable[[], None] | None = None,
    ) -> None:
        """Create an adapter around a token provider."""
        self._token_provider = token_provider
        self._close_callback = close_callback

    @classmethod
    def from_env(cls) -> Self:
        """Create an adapter from ``BLING_*`` environment settings."""
        auth = BlingAuth.from_env()
        return cls(auth.manager, close_callback=auth.close)

    def auth_flow(self, request: httpx.Request) -> Generator[httpx.Request, httpx.Response]:
        """Attach Bling authentication headers to an outgoing request."""
        request.headers.update(bling_api_headers(self._token_provider.get_access_token()))
        yield request

    def close(self) -> None:
        """Close owned authentication resources, when any exist."""
        if self._close_callback is not None:
            self._close_callback()
