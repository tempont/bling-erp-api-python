"""Tests for OpenAPI-generated Pydantic models."""

from __future__ import annotations

from inspect import signature
from pathlib import Path

import pytest
from pydantic import ValidationError

from bling_erp_api.models.generated.product_stores import ProdutosLojasPostRequest
from bling_erp_api.models.generated.products import (
    ProdutosDadosBaseDTO,
    ProdutosDadosDTO,
    ProdutosGetResponse200,
    ProdutosIdProdutoGetResponse200,
)
from bling_erp_api.models.generated.sales_orders import (
    PedidosVendasPostRequest,
)
from bling_erp_api.utils.serialization import to_json_object

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def test_generated_model_accepts_bling_aliases_and_preserves_extra_fields() -> None:
    """Generated models should accept Bling fields and tolerate new API fields."""
    model = ProdutosDadosBaseDTO.model_validate(
        {
            "id": 123,
            "idProdutoPai": 456,
            "nome": "Produto",
            "tipo": "P",
            "situacao": "A",
            "formato": "S",
            "campoNovoBling": "mantido",
        }
    )

    assert model.id_produto_pai == 456
    assert model.model_extra == {"campoNovoBling": "mantido"}


def test_generated_model_accepts_pythonic_field_names_and_serializes_bling_aliases() -> None:
    """Generated models should expose snake_case while serializing Bling aliases."""
    model = ProdutosDadosBaseDTO.model_validate(
        {
            "id_produto_pai": 456,
            "nome": "Produto",
            "tipo": "P",
            "situacao": "A",
            "formato": "S",
        }
    )

    assert to_json_object(model) == {
        "idProdutoPai": 456,
        "nome": "Produto",
        "tipo": "P",
        "situacao": "A",
        "formato": "S",
    }


def test_generated_model_constructor_signature_prefers_pythonic_names() -> None:
    """Generated models should guide SDK users toward Python field names."""
    model_signature = str(signature(ProdutosDadosDTO))

    assert "descricao_curta" in model_signature
    assert "data_validade" in model_signature
    assert "descricaoCurta" not in model_signature
    assert "dataValidade" not in model_signature


def test_generated_model_normalizes_bling_aliases_without_preserving_them_as_extra() -> None:
    """Known Bling aliases should hydrate fields, not survive as extra payload keys."""
    model = ProdutosDadosDTO.model_validate(
        {
            "nome": "Produto",
            "tipo": "P",
            "situacao": "A",
            "formato": "S",
            "descricaoCurta": "Descrição curta",
        }
    )

    payload = to_json_object(model)

    assert model.descricao_curta == "Descrição curta"
    assert "descricaoCurta" not in (model.model_extra or {})
    assert payload["descricaoCurta"] == "Descrição curta"
    assert "descricao_curta" not in payload


def test_generated_model_rejects_conflicting_python_and_bling_field_names() -> None:
    """Users should not be able to serialize both snake_case and Bling names."""
    with pytest.raises(ValidationError, match="Conflicting values"):
        ProdutosDadosDTO.model_validate(
            {
                "nome": "Produto",
                "tipo": "P",
                "situacao": "A",
                "formato": "S",
                "descricao_curta": "snake",
                "descricaoCurta": "camel",
            }
        )


def test_generated_list_response_wraps_data_items() -> None:
    """OpenAPI path responses should wrap list payloads as Pydantic models."""
    response = ProdutosGetResponse200.model_validate(
        {
            "data": [
                {
                    "id": 123,
                    "nome": "Produto",
                    "tipo": "P",
                    "situacao": "A",
                    "formato": "S",
                }
            ]
        }
    )

    assert response.data
    assert response.data[0].nome == "Produto"


def test_generated_detail_response_wraps_data_item() -> None:
    """OpenAPI detail responses should expose the documented data schema."""
    response = ProdutosIdProdutoGetResponse200.model_validate(
        {
            "data": {
                "id": 123,
                "nome": "Produto",
                "tipo": "P",
                "situacao": "A",
                "formato": "S",
            }
        }
    )

    assert isinstance(response.data, ProdutosDadosDTO)
    assert response.data.nome == "Produto"


def test_generated_composed_request_serializes_aliases() -> None:
    """Generated allOf request models should serialize nested Bling field names."""
    request = PedidosVendasPostRequest.model_validate(
        {
            "data": "2024-01-01",
            "dataSaida": "2024-01-02",
            "dataPrevista": "2024-01-03",
            "contato": {"id": 1, "nome": "Cliente"},
            "itens": [
                {
                    "id": 1,
                    "quantidade": 1,
                    "valor": 10,
                    "descricao": "Produto",
                    "produto": {"id": 123},
                }
            ],
            "parcelas": [
                {
                    "id": 1,
                    "dataVencimento": "2024-02-01",
                    "valor": 10,
                    "formaPagamento": {"id": 1},
                }
            ],
        }
    )

    payload = to_json_object(request)

    assert payload["dataSaida"] == "2024-01-02"
    assert payload["itens"] == [
        {
            "id": 1,
            "quantidade": 1,
            "valor": 10,
            "descricao": "Produto",
            "produto": {"id": 123},
        }
    ]


def test_generated_model_docstrings_document_payload_fields() -> None:
    """Public payload models should describe their available fields in IDE hovers."""
    product_doc = ProdutosDadosDTO.__doc__ or ""
    store_doc = ProdutosLojasPostRequest.__doc__ or ""

    assert "categoria: Bling ``categoria``" in product_doc
    assert "codigo: Bling ``codigo``" in store_doc
    assert "categorias_produtos: Bling ``categoriasProdutos``" in store_doc


def test_generated_schemas_are_split_into_schema_modules() -> None:
    """Generated schemas should live in a package instead of a single monolithic file."""
    generated_dir = PROJECT_ROOT / "src" / "bling_erp_api" / "models" / "generated"

    assert not (generated_dir / "schemas.py").exists()
    assert (generated_dir / "schemas" / "produtos.py").exists()
    assert (generated_dir / "schemas" / "produtos_lojas.py").exists()
