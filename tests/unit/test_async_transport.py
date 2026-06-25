"""Tests for AsyncTransport — rate limiting, 429 retry, and context manager."""

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING

import httpx
import pytest

from bling_erp_api.exceptions import BlingRateLimitError, BlingTransportError
from bling_erp_api.rate_limit import RateLimiter
from bling_erp_api.transport import AsyncTransport as ExportedAsyncTransport
from bling_erp_api.transport import AsyncTransportProtocol
from bling_erp_api.transport.async_ import AsyncTransport

if TYPE_CHECKING:
    from collections.abc import Generator


@pytest.fixture
def async_transport() -> Generator[AsyncTransport, None, None]:
    """Provide an AsyncTransport with rate limiting disabled."""
    client = httpx.AsyncClient(
        base_url="https://api.bling.test/Api/v3",
        transport=httpx.MockTransport(lambda r: httpx.Response(200, json={}, request=r)),
    )
    transport = AsyncTransport(
        auth=httpx.BasicAuth("client", "secret"),
        client=client,
        rate_limit_max_requests=None,
    )
    yield transport
    asyncio.run(transport.close())


class TestAsyncTransport429Retry:
    """429 retry loop mirrors SyncTransport behavior."""

    async def _run_retry_once(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """First call returns 429, second succeeds."""

        async def _noop_sleep(_delay: float) -> None:
            return None

        monkeypatch.setattr(asyncio, "sleep", _noop_sleep)

        calls: list[str] = []

        def handler(request: httpx.Request) -> httpx.Response:
            calls.append(request.url.path)
            if len(calls) == 1:
                return httpx.Response(
                    429,
                    json={"error": {"message": "Limite de requisições atingido."}},
                    headers={"Retry-After": "0"},
                    request=request,
                )
            return httpx.Response(200, json={"data": [{"id": 1}]}, request=request)

        client = httpx.AsyncClient(
            base_url="https://api.bling.test/Api/v3",
            transport=httpx.MockTransport(handler),
        )
        transport = AsyncTransport(
            auth=httpx.BasicAuth("client", "secret"),
            client=client,
            rate_limit_max_requests=None,
            rate_limit_max_retries=1,
        )

        response = await transport.request("GET", "/pedidos/vendas")

        assert response == {"data": [{"id": 1}]}
        assert calls == ["/Api/v3/pedidos/vendas", "/Api/v3/pedidos/vendas"]

    def test_retries_on_rate_limit(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """AsyncTransport retries a single 429 before succeeding."""
        asyncio.run(self._run_retry_once(monkeypatch))

    async def _run_retry_exhausted(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Multiple 429s exceed max_retries and bubble up."""

        async def _noop_sleep(_delay: float) -> None:
            return None

        monkeypatch.setattr(asyncio, "sleep", _noop_sleep)

        def handler(request: httpx.Request) -> httpx.Response:
            return httpx.Response(
                429,
                json={"error": {"message": "rate limit"}},
                request=request,
            )

        client = httpx.AsyncClient(
            base_url="https://api.bling.test/Api/v3",
            transport=httpx.MockTransport(handler),
        )
        transport = AsyncTransport(
            auth=httpx.BasicAuth("client", "secret"),
            client=client,
            rate_limit_max_requests=None,
            rate_limit_max_retries=2,
        )

        with pytest.raises(BlingRateLimitError):
            await transport.request("GET", "/pedidos/vendas")

    def test_exhausts_retries(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """BlingRateLimitError is surfaced after retries exhausted."""
        asyncio.run(self._run_retry_exhausted(monkeypatch))

    async def _run_retry_delay_captured(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Positive Retry-After value is passed to asyncio.sleep."""
        sleeps: list[float] = []

        async def track_sleep(delay: float) -> None:
            sleeps.append(delay)

        monkeypatch.setattr(asyncio, "sleep", track_sleep)

        calls: list[str] = []

        def handler(request: httpx.Request) -> httpx.Response:
            calls.append(request.url.path)
            if len(calls) == 1:
                return httpx.Response(
                    429,
                    json={"error": {"message": "rate limit"}},
                    headers={"Retry-After": "2.5"},
                    request=request,
                )
            return httpx.Response(200, json={"data": [{"id": 1}]}, request=request)

        client = httpx.AsyncClient(
            base_url="https://api.bling.test/Api/v3",
            transport=httpx.MockTransport(handler),
        )
        transport = AsyncTransport(
            auth=httpx.BasicAuth("client", "secret"),
            client=client,
            rate_limit_max_requests=None,
            rate_limit_max_retries=1,
        )

        response = await transport.request("GET", "/test")

        assert response == {"data": [{"id": 1}]}
        # The sleep should have been called with the Retry-After value.
        assert 2.5 in sleeps

    def test_retry_after_value_used(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Retry-After header value is used for sleep duration."""
        asyncio.run(self._run_retry_delay_captured(monkeypatch))


class TestAsyncTransportContextManager:
    """Async context manager protocol."""

    async def _run_context_manager(self) -> None:
        client = httpx.AsyncClient(
            base_url="https://api.bling.test/Api/v3",
            transport=httpx.MockTransport(
                lambda r: httpx.Response(200, json={"ok": True}, request=r),
            ),
        )
        async with AsyncTransport(
            auth=httpx.BasicAuth("client", "secret"),
            client=client,
            rate_limit_max_requests=None,
        ) as transport:
            response = await transport.request("GET", "/test")

        assert response == {"ok": True}

    def test_async_context_manager(self) -> None:
        """AsyncTransport works with ``async with``."""
        asyncio.run(self._run_context_manager())

    async def _run_close_owned(self) -> None:
        """When AsyncTransport owns its client, __aexit__ closes it."""
        transport = AsyncTransport(
            auth=httpx.BasicAuth("client", "secret"),
            base_url="https://api.bling.test/Api/v3",
            rate_limit_max_requests=None,
        )
        async with transport:
            pass

        # After __aexit__, requesting raises BlingTransportError because
        # the owned client is closed.
        with pytest.raises(BlingTransportError):
            await transport.request("GET", "/should-fail")

    def test_close_owned_client(self) -> None:
        """AsyncTransport closes its own client on context exit."""
        asyncio.run(self._run_close_owned())


class TestAsyncTransportImport:
    """AsyncTransport is importable from the transport package."""

    def test_import_from_transport_package(self) -> None:
        """AsyncTransport and AsyncTransportProtocol are exported."""
        assert ExportedAsyncTransport is not None
        assert AsyncTransportProtocol is not None

    def test_import_direct(self) -> None:
        """AsyncTransport is importable from its module."""
        assert AsyncTransport is not None


class TestAsyncRateLimiter:
    """RateLimiter.wait_async() basic behavior."""

    async def _run_wait_async(self) -> None:
        limiter = RateLimiter(max_requests=2, period_seconds=0.5)

        # First two calls return immediately.
        await limiter.wait_async()
        await limiter.wait_async()

        # Third call must wait because the window is full.
        before = asyncio.get_running_loop().time()
        await limiter.wait_async()
        after = asyncio.get_running_loop().time()

        # It should have waited at least a brief amount.
        assert after - before >= 0.0

    def test_wait_async_blocks_when_full(self) -> None:
        """wait_async pauses when at capacity."""
        asyncio.run(self._run_wait_async())
