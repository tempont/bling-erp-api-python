"""Tests for sales order models."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

from bling_erp_api.models.generated.sales_orders import (
    SalesOrderInvoiceResponse,
    SalesOrderListResponse,
    SalesOrderMutationResponse,
    SalesOrderResponse,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def test_sales_order_list_response_parses_bling_aliases_and_extra_fields() -> None:
    """List response should parse Bling field names and tolerate new fields."""
    payload = json.loads((FIXTURES_DIR / "sales_order_list.json").read_text(encoding="utf-8"))

    response = SalesOrderListResponse.model_validate(payload)

    order = response.data[0]
    assert order.id == 12345678
    assert order.number == 42
    assert order.store_number == "WEB-42"
    assert order.date == date(2024, 1, 10)
    assert order.output_date == date(2024, 1, 10)
    assert order.expected_date == date(2024, 1, 12)
    assert order.products_total == 21
    assert order.contact is not None
    assert order.contact.name == "Cliente Teste"
    assert order.contact.person_type == "J"
    assert order.items[0].product is not None
    assert order.items[0].product.id == 444
    assert order.installments[0].payment_method is not None
    assert order.installments[0].payment_method.id == 666
    assert order.model_extra == {"campoNovoBling": "mantido"}


def test_sales_order_response_allows_optional_fields() -> None:
    """Single order response should allow sparse Bling payloads."""
    response = SalesOrderResponse.model_validate(
        {"data": {"id": 123, "contato": {"id": 456, "nome": "Cliente"}}}
    )

    assert response.data.id == 123
    assert response.data.contact is not None
    assert response.data.contact.name == "Cliente"
    assert response.data.items == []
    assert response.data.installments == []


def test_sales_order_mutation_response_parses_warnings() -> None:
    """Create and update responses should parse post/put metadata."""
    response = SalesOrderMutationResponse.model_validate(
        {"data": {"id": 123, "alertas": [{"code": 49, "msg": "Aviso"}]}}
    )

    assert response.data.id == 123
    assert response.data.warnings == [{"code": 49, "msg": "Aviso"}]


def test_sales_order_invoice_response_parses_invoice_alias() -> None:
    """Invoice generation response should expose idNotaFiscal as invoice_id."""
    response = SalesOrderInvoiceResponse.model_validate({"idNotaFiscal": 987654})

    assert response.invoice_id == 987654
