"""Tests for SDK exception formatting."""

from __future__ import annotations

import httpx
import pytest

from bling_erp_api.exceptions import (
    BlingNotFoundError,
    BlingValidationError,
    raise_for_error_response,
)


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


def test_validation_error_message_includes_description_and_fields() -> None:
    """Bling validation errors should expose the useful API guidance."""
    request = httpx.Request("POST", "https://api.bling.com.br/Api/v3/situacoes")
    response = httpx.Response(
        400,
        json={
            "error": {
                "type": "VALIDATION_ERROR",
                "message": "Não foi possível criar o registro",
                "description": "O módulo informado não permite criar situações.",
                "fields": [
                    {
                        "code": 49,
                        "msg": "ID do módulo do sistema inválido.",
                        "element": "idModuloSistema",
                    }
                ],
            }
        },
        request=request,
    )

    with pytest.raises(BlingValidationError) as exc_info:
        raise_for_error_response(response)

    assert str(exc_info.value) == (
        "POST /Api/v3/situacoes returned 400: VALIDATION_ERROR; "
        "Não foi possível criar o registro; "
        "O módulo informado não permite criar situações.; "
        "fields: idModuloSistema (49): ID do módulo do sistema inválido."
    )


def test_validation_error_message_includes_nested_collection_fields() -> None:
    """Bling validation errors should expose nested collection item details."""
    request = httpx.Request("POST", "https://api.bling.com.br/Api/v3/propostas-comerciais")
    response = httpx.Response(
        400,
        json={
            "error": {
                "type": "VALIDATION_ERROR",
                "message": "Não foi possível salvar a proposta comercial",
                "description": (
                    "A proposta comercial não pode ser salva, pois ocorreram problemas "
                    "em sua validação."
                ),
                "fields": [
                    {
                        "code": 21,
                        "msg": "Uma ou mais parcelas da proposta possuem erros de validação",
                        "element": "parcelas",
                        "collection": [
                            {
                                "index": 0,
                                "code": 12,
                                "msg": "Id da forma de pagamento inválido.",
                                "element": "formaPagamento",
                            }
                        ],
                    }
                ],
            }
        },
        request=request,
    )

    with pytest.raises(BlingValidationError) as exc_info:
        raise_for_error_response(response)

    assert str(exc_info.value) == (
        "POST /Api/v3/propostas-comerciais returned 400: VALIDATION_ERROR; "
        "Não foi possível salvar a proposta comercial; "
        "A proposta comercial não pode ser salva, pois ocorreram problemas em sua validação.; "
        "fields: parcelas (21): Uma ou mais parcelas da proposta possuem erros de validação; "
        "formaPagamento[0] (12): Id da forma de pagamento inválido."
    )
