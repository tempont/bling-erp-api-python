"""Tests for OpenAPI-generated Pydantic models."""

from __future__ import annotations

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
