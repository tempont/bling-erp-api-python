"""Async transport for ``AsyncBlingClient``."""

from __future__ import annotations

import asyncio
import email.utils
import math
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Self

import httpx

from bling_erp_api.config import (
    DEFAULT_API_BASE_URL,
    DEFAULT_RATE_LIMIT_MAX_REQUESTS,
    DEFAULT_RATE_LIMIT_MAX_RETRIES,
    DEFAULT_RATE_LIMIT_PERIOD_SECONDS,
    DEFAULT_RETRY_AFTER_RATE_LIMIT_SECONDS,
    DEFAULT_TIMEOUT_SECONDS,
)
from bling_erp_api.exceptions import (
    BlingRateLimitError,
    BlingTransportError,
    raise_for_error_response,
)
from bling_erp_api.rate_limit import RateLimiter
from bling_erp_api.response import response_json_object

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject, JsonPayload, QueryParams


class AsyncTransport:
    """Asynchronous transport with the same resource-facing contract.

    Wraps an ``httpx.AsyncClient`` with local rate limiting, 429 retry, and
    async context manager support.
    """

    def __init__(  # noqa: PLR0913
        self,
        *,
        auth: httpx.Auth,
        base_url: str = DEFAULT_API_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
        client: httpx.AsyncClient | None = None,
        rate_limiter: RateLimiter | None = None,
        rate_limit_max_requests: int | None = DEFAULT_RATE_LIMIT_MAX_REQUESTS,
        rate_limit_period_seconds: float = DEFAULT_RATE_LIMIT_PERIOD_SECONDS,
        rate_limit_max_retries: int = DEFAULT_RATE_LIMIT_MAX_RETRIES,
    ) -> None:
        """Create an async transport around an ``httpx.AsyncClient``."""
        self._auth = auth
        self._owns_client = client is None
        self._client = client or httpx.AsyncClient(base_url=base_url, timeout=timeout, auth=auth)
        self._rate_limiter = rate_limiter or _build_rate_limiter(
            max_requests=rate_limit_max_requests,
            period_seconds=rate_limit_period_seconds,
        )
        self._rate_limit_max_retries = rate_limit_max_retries

    async def request(
        self,
        method: str,
        path: str,
        *,
        params: QueryParams | None = None,
        json: JsonPayload | None = None,
        headers: dict[str, str] | None = None,
    ) -> JsonObject:
        """Send an async request and return a decoded JSON object."""
        attempts = 0
        while True:
            if self._rate_limiter is not None:
                await self._rate_limiter.wait_async()

            response = await self._send_request(
                method,
                path,
                params=params,
                json=json,
                headers=headers,
            )
            try:
                raise_for_error_response(response)
            except BlingRateLimitError:
                if attempts >= self._rate_limit_max_retries:
                    raise
                attempts += 1
                await _async_sleep_retry_after(response)
                continue

            return response_json_object(response)

    async def _send_request(
        self,
        method: str,
        path: str,
        *,
        params: QueryParams | None = None,
        json: JsonPayload | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Send one HTTP request."""
        try:
            return await self._client.request(
                method,
                path,
                params=params,
                json=json,
                headers=headers,
            )
        except httpx.HTTPError as exc:
            msg = f"Unable to complete Bling API request: {exc}"
            raise BlingTransportError(msg) from exc
        except RuntimeError as exc:
            msg = f"Unable to complete Bling API request: {exc}"
            raise BlingTransportError(msg) from exc

    async def close(self) -> None:
        """Close owned HTTP and auth resources."""
        if self._owns_client:
            await self._client.aclose()

        close = getattr(self._auth, "close", None)
        if callable(close):
            result = close()
            if asyncio.iscoroutine(result):
                await result

    async def __aenter__(self) -> Self:
        """Return this transport for async context manager usage."""
        return self

    async def __aexit__(self, *_exc: object) -> None:
        """Close resources when leaving an async context manager."""
        await self.close()


def _build_rate_limiter(*, max_requests: int | None, period_seconds: float) -> RateLimiter | None:
    if max_requests is None:
        return None
    return RateLimiter(max_requests=max_requests, period_seconds=period_seconds)


_MAX_RETRY_AFTER_SECONDS = 300.0


async def _async_sleep_retry_after(response: httpx.Response) -> None:
    """Sleep for the duration indicated by the ``Retry-After`` header.

    Async counterpart of ``_sleep_retry_after`` in ``sync.py``.
    """
    retry_after = response.headers.get("Retry-After")
    if retry_after is None:
        delay = DEFAULT_RETRY_AFTER_RATE_LIMIT_SECONDS
    else:
        try:
            delay = float(retry_after)
            if not math.isfinite(delay):
                delay = DEFAULT_RETRY_AFTER_RATE_LIMIT_SECONDS
        except ValueError:
            try:
                parsed = email.utils.parsedate_to_datetime(retry_after)
                delay = (parsed - datetime.now(UTC)).total_seconds()
            except (TypeError, ValueError, AttributeError):
                delay = DEFAULT_RETRY_AFTER_RATE_LIMIT_SECONDS
    delay = max(0.0, min(delay, _MAX_RETRY_AFTER_SECONDS))
    if delay > 0:
        await asyncio.sleep(delay)
