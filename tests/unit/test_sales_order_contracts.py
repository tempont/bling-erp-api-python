"""Tests for OpenAPI-derived sales order contracts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import cast

from bling_erp_api.contracts.generated.sales_orders import SALES_ORDER_OPERATIONS

SPEC_PATH = Path("specs/bling-openapi-reference.json")


def test_sales_order_contract_covers_openapi_operations() -> None:
    """Generated contracts should cover every PedidosVenda operation in OpenAPI."""
    payload = cast("dict[str, object]", json.loads(SPEC_PATH.read_text(encoding="utf-8")))
    paths = cast("dict[str, object]", payload["paths"])
    official_operations = {
        (
            str(method).upper(),
            path,
            str(cast("dict[str, object]", operation)["x-api-action"]),
        )
        for path, methods in paths.items()
        for method, operation in cast("dict[str, object]", methods).items()
        if cast("dict[str, object]", operation).get("x-api-resource") == "PedidosVenda"
    }

    contracted_operations = {
        (operation.method, operation.path, operation.action)
        for operation in SALES_ORDER_OPERATIONS.values()
    }

    assert contracted_operations == official_operations


def test_sales_order_list_contract_exposes_portuguese_sdk_parameters() -> None:
    """List contract should bind official query names to Portuguese SDK names."""
    operation = SALES_ORDER_OPERATIONS["listar"]

    assert operation.method == "GET"
    assert operation.path == "/pedidos/vendas"
    assert {parameter.name: parameter.sdk_name for parameter in operation.parameters} == {
        "pagina": "pagina",
        "limite": "limite",
        "idContato": "id_contato",
        "idsSituacoes[]": "ids_situacoes",
        "dataInicial": "data_inicial",
        "dataFinal": "data_final",
        "dataAlteracaoInicial": "data_alteracao_inicial",
        "dataAlteracaoFinal": "data_alteracao_final",
        "dataPrevistaInicial": "data_prevista_inicial",
        "dataPrevistaFinal": "data_prevista_final",
        "numero": "numero",
        "idLoja": "id_loja",
        "idVendedor": "id_vendedor",
        "idControleCaixa": "id_controle_caixa",
        "numerosLojas[]": "numeros_lojas",
        "idUnidadeNegocio": "id_unidade_negocio",
    }
