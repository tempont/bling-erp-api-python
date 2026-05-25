"""Tests for product models."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.products import (
    ProductListResponse,
    ProductMutationResponse,
    ProductResponse,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def test_product_list_response_parses_bling_aliases_and_extra_fields() -> None:
    """List response should parse Bling aliases and tolerate new fields."""
    payload = json.loads((FIXTURES_DIR / "product_list.json").read_text(encoding="utf-8"))

    response = ProductListResponse.model_validate(payload)

    product = response.data[0]
    assert product.id == 12345678
    assert product.parent_product_id == 87654321
    assert product.name == "Produto Teste"
    assert product.code == "SKU-1"
    assert product.price == 19.9
    assert product.cost_price == 12.5
    assert product.product_type == "P"
    assert product.status == "A"
    assert product.format == "S"
    assert product.short_description == "Descricao curta"
    assert product.image_url == "https://example.test/produto.jpg"
    assert product.model_extra == {"campoNovoBling": "mantido"}


def test_product_response_allows_optional_fields() -> None:
    """Single product response should allow sparse payloads."""
    response = ProductResponse.model_validate({"data": {"id": 123, "nome": "Produto"}})

    assert response.data.id == 123
    assert response.data.name == "Produto"
    assert response.data.variations == []


def test_product_mutation_response_parses_id_and_warnings() -> None:
    """Create and update responses should parse returned id metadata."""
    response = ProductMutationResponse.model_validate(
        {"data": {"id": 123, "warnings": ["Mensagem de aviso."]}}
    )

    assert response.data.id == 123
    assert response.data.warnings == ["Mensagem de aviso."]
