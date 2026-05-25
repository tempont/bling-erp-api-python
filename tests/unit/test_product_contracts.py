"""Tests for OpenAPI-derived product contracts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import cast

from bling_erp_api.contracts.generated.products import PRODUCT_OPERATIONS

SPEC_PATH = Path("specs/bling-openapi-reference.json")


def test_product_contract_covers_openapi_operations() -> None:
    """Generated contracts should cover every Produtos operation in OpenAPI."""
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
        if cast("dict[str, object]", operation).get("x-api-resource") == "Produtos"
    }

    contracted_operations = {
        (operation.method, operation.path, operation.action)
        for operation in PRODUCT_OPERATIONS.values()
    }

    assert contracted_operations == official_operations


def test_product_list_contract_exposes_portuguese_sdk_parameters() -> None:
    """List contract should bind official product query names to SDK names."""
    operation = PRODUCT_OPERATIONS["listar"]

    assert operation.method == "GET"
    assert operation.path == "/produtos"
    assert {parameter.name: parameter.sdk_name for parameter in operation.parameters} == {
        "pagina": "pagina",
        "limite": "limite",
        "criterio": "criterio",
        "tipo": "tipo",
        "idComponente": "id_componente",
        "dataInclusaoInicial": "data_inclusao_inicial",
        "dataInclusaoFinal": "data_inclusao_final",
        "dataAlteracaoInicial": "data_alteracao_inicial",
        "dataAlteracaoFinal": "data_alteracao_final",
        "idCategoria": "id_categoria",
        "idLoja": "id_loja",
        "nome": "nome",
        "idsProdutos[]": "ids_produtos",
        "codigos[]": "codigos",
        "gtins[]": "gtins",
        "filtroSaldoEstoque": "filtro_saldo_estoque",
        "filtroSaldoEstoqueDeposito": "filtro_saldo_estoque_deposito",
    }
