"""Tests for transport rate-limit behavior."""

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from bling_erp_api.transport.sync import SyncTransport

if TYPE_CHECKING:
    import pytest


def test_sync_transport_retries_rate_limit_response(monkeypatch: pytest.MonkeyPatch) -> None:
    """Transport should retry 429 responses before surfacing rate-limit errors."""
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

    def fake_sleep(_delay: float) -> None:
        return None

    monkeypatch.setattr("bling_erp_api.transport.sync.time.sleep", fake_sleep)
    client = httpx.Client(
        base_url="https://api.bling.test/Api/v3",
        transport=httpx.MockTransport(handler),
    )
    transport = SyncTransport(
        auth=httpx.BasicAuth("client", "secret"),
        client=client,
        rate_limit_max_requests=None,
        rate_limit_max_retries=1,
    )

    response = transport.request("GET", "/pedidos/vendas")

    assert response == {"data": [{"id": 1}]}
    assert calls == ["/Api/v3/pedidos/vendas", "/Api/v3/pedidos/vendas"]
