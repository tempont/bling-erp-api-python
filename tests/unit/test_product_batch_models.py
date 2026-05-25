"""Model mapping tests for produtos e lotes."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.product_batches import ProductBatch

FIXTURE_PATH = Path("tests/fixtures/responses/product_batch_list.json")


def test_product_batch_list_row_fixture() -> None:
    """Deserializa entrada de lista de lotes."""
    payload = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    row = ProductBatch.model_validate(payload["data"][0])
    assert row.id_lote == 876543210
    assert row.codigo_lote == "LOTE-DEMO"
    assert row.produto.id == 111
    assert row.deposito.id == 3
