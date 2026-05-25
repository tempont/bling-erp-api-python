"""Model mapping tests for produtos e fornecedores."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.product_suppliers import ProductSupplier

FIXTURE_PATH = Path("tests/fixtures/responses/product_supplier_list.json")


def test_product_supplier_list_row_fixture() -> None:
    """Deserializa uma linha retornada em ``GET /produtos/fornecedores``."""
    payload = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    row = ProductSupplier.model_validate(payload["data"][0])
    assert row.record_id == 123456789
    assert row.codigo_fornecedor == "SKU-FORN"
    assert row.fornecedor is not None
    assert row.fornecedor.id == 222
