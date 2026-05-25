"""Model mapping tests for lançamentos de lote."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.product_batch_entries import ProductBatchEntry

FIXTURE_PATH = Path("tests/fixtures/responses/product_batch_entry_list.json")


def test_batch_entry_fixture() -> None:
    """Deserializa um lançamento de lote retornado pela API."""
    payload = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    row = ProductBatchEntry.model_validate(payload["data"][0])
    assert row.entry_id == 444333222
    assert row.id_lote == 876543210
    assert row.observacao == "Entrada inicial"
