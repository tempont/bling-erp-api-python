"""Model mapping tests for estruturas de produto."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.product_structures import ProductStructureResponse

FIXTURE_PATH = Path("tests/fixtures/responses/product_structure_obter.json")


def test_product_structure_obter_fixture_round_trip() -> None:
    """Produtos estrutura GET envelopes should hydrate via Pydantic."""
    payload = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    model = ProductStructureResponse.model_validate(payload)
    component = model.data.componentes[0]
    assert model.data.stock_kind == "F"
    assert component.produto.id == 987654321
    assert component.quantity == 3.25
    dumped = model.model_dump(by_alias=True, mode="json")
    assert dumped["data"]["componentes"][0]["quantidade"] == 3.25
