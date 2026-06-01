"""Tests for SDK exception formatting."""

from __future__ import annotations

import httpx
import pytest

from bling_erp_api.exceptions import BlingNotFoundError, raise_for_error_response


def test_error_response_message_includes_request_context() -> None:
    """HTTP API errors should show endpoint and status in the default message."""
    request = httpx.Request("GET", "https://api.bling.com.br/vendedores/1")
    response = httpx.Response(
        404,
        json={"error": {"message": "Não encontrado."}},
        request=request,
    )

    with pytest.raises(BlingNotFoundError) as exc_info:
        raise_for_error_response(response)

    error = exc_info.value
    assert str(error) == "GET /vendedores/1 returned 404: Não encontrado."
    assert error.status_code == 404
    assert error.payload == {"error": {"message": "Não encontrado."}}


def test_error_response_message_without_request_context_still_includes_status() -> None:
    """HTTP API errors without attached request should still be actionable."""
    response = httpx.Response(404, json={"error": {"message": "Não encontrado."}})

    with pytest.raises(BlingNotFoundError, match=r"Bling API returned 404: Não encontrado\."):
        raise_for_error_response(response)
