"""Synchronous HTTP transport based on httpx."""

from __future__ import annotations

import time
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


class SyncTransport:
    """Synchronous transport used by ``BlingClient`` resources."""

    def __init__(  # noqa: PLR0913
        self,
        *,
        auth: httpx.Auth,
        base_url: str = DEFAULT_API_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
        client: httpx.Client | None = None,
        rate_limiter: RateLimiter | None = None,
        rate_limit_max_requests: int | None = DEFAULT_RATE_LIMIT_MAX_REQUESTS,
        rate_limit_period_seconds: float = DEFAULT_RATE_LIMIT_PERIOD_SECONDS,
        rate_limit_max_retries: int = DEFAULT_RATE_LIMIT_MAX_RETRIES,
    ) -> None:
        """Create a transport around an ``httpx.Client``."""
        self._auth = auth
        self._owns_client = client is None
        self._client = client or httpx.Client(base_url=base_url, timeout=timeout, auth=auth)
        self._rate_limiter = rate_limiter or _build_rate_limiter(
            max_requests=rate_limit_max_requests,
            period_seconds=rate_limit_period_seconds,
        )
        self._rate_limit_max_retries = rate_limit_max_retries

    def request(
        self,
        method: str,
        path: str,
        *,
        params: QueryParams | None = None,
        json: JsonPayload | None = None,
    ) -> JsonObject:
        """Send a request and return a decoded JSON object."""
        attempts = 0
        while True:
            if self._rate_limiter is not None:
                self._rate_limiter.wait()

            response = self._send_request(method, path, params=params, json=json)
            try:
                raise_for_error_response(response)
            except BlingRateLimitError:
                if attempts >= self._rate_limit_max_retries:
                    raise
                attempts += 1
                _sleep_retry_after(response)
                continue

            return response_json_object(response)

    def _send_request(
        self,
        method: str,
        path: str,
        *,
        params: QueryParams | None = None,
        json: JsonPayload | None = None,
    ) -> httpx.Response:
        """Send one HTTP request."""
        try:
            return self._client.request(
                method,
                path,
                params=params,
                json=json,
            )
        except httpx.HTTPError as exc:
            msg = f"Unable to complete Bling API request: {exc}"
            raise BlingTransportError(msg) from exc

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


def _build_rate_limiter(*, max_requests: int | None, period_seconds: float) -> RateLimiter | None:
    if max_requests is None:
        return None
    return RateLimiter(max_requests=max_requests, period_seconds=period_seconds)


def _sleep_retry_after(response: httpx.Response) -> None:
    retry_after = response.headers.get("Retry-After")
    try:
        delay = (
            float(retry_after)
            if retry_after is not None
            else DEFAULT_RETRY_AFTER_RATE_LIMIT_SECONDS
        )
    except ValueError:
        delay = DEFAULT_RETRY_AFTER_RATE_LIMIT_SECONDS
    if delay > 0:
        time.sleep(delay)
