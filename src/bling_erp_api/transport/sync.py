"""Synchronous HTTP transport based on httpx."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self

import httpx

from bling_erp_api.config import DEFAULT_API_BASE_URL, DEFAULT_TIMEOUT_SECONDS
from bling_erp_api.exceptions import BlingTransportError, raise_for_error_response
from bling_erp_api.response import response_json_object

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject, QueryParams


class SyncTransport:
    """Synchronous transport used by ``BlingClient`` resources."""

    def __init__(
        self,
        *,
        auth: httpx.Auth,
        base_url: str = DEFAULT_API_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
        client: httpx.Client | None = None,
    ) -> None:
        """Create a transport around an ``httpx.Client``."""
        self._auth = auth
        self._owns_client = client is None
        self._client = client or httpx.Client(base_url=base_url, timeout=timeout, auth=auth)

    def request(
        self,
        method: str,
        path: str,
        *,
        params: QueryParams | None = None,
        json: JsonObject | None = None,
    ) -> JsonObject:
        """Send a request and return a decoded JSON object."""
        try:
            response = self._client.request(
                method,
                path,
                params=params,
                json=json,
            )
        except httpx.HTTPError as exc:
            msg = f"Unable to complete Bling API request: {exc}"
            raise BlingTransportError(msg) from exc

        raise_for_error_response(response)
        return response_json_object(response)

    def close(self) -> None:
        """Close owned HTTP and auth resources."""
        if self._owns_client:
            self._client.close()

        close = getattr(self._auth, "close", None)
        if callable(close):
            close()

    def __enter__(self) -> Self:
        """Return this transport for context manager usage."""
        return self

    def __exit__(self, *_exc: object) -> None:
        """Close resources when leaving a context manager."""
        self.close()
