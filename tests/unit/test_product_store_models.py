"""Model mapping tests para produtos em lojas."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.product_stores import ProductStoreLink

FIXTURE_PATH = Path("tests/fixtures/responses/product_store_list.json")


def test_product_store_list_row_fixture() -> None:
    """Deserializa vínculo produto-loja conforme dados do endpoint."""
    payload = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    row = ProductStoreLink.model_validate(payload["data"][0])
    assert row.record_id == 555667788
    assert row.codigo_loja == "LOJA-X"
    assert row.produto.id == 111
    assert row.loja.id == 9
