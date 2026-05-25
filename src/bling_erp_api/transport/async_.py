"""Async transport placeholder for a future ``AsyncBlingClient``."""

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from bling_erp_api.config import DEFAULT_API_BASE_URL, DEFAULT_TIMEOUT_SECONDS
from bling_erp_api.exceptions import BlingTransportError, raise_for_error_response
from bling_erp_api.response import response_json_object

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject, JsonPayload, QueryParams


class AsyncTransport:
    """Asynchronous transport with the same resource-facing contract."""

    def __init__(
        self,
        *,
        auth: httpx.Auth,
        base_url: str = DEFAULT_API_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
        client: httpx.AsyncClient | None = None,
    ) -> None:
        """Create an async transport around an ``httpx.AsyncClient``."""
        self._auth = auth
        self._owns_client = client is None
        self._client = client or httpx.AsyncClient(base_url=base_url, timeout=timeout, auth=auth)

    async def request(
        self,
        method: str,
        path: str,
        *,
        params: QueryParams | None = None,
        json: JsonPayload | None = None,
    ) -> JsonObject:
        """Send an async request and return a decoded JSON object."""
        try:
            response = await self._client.request(
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

    async def close(self) -> None:
        """Close owned HTTP resources."""
        if self._owns_client:
            await self._client.aclose()
