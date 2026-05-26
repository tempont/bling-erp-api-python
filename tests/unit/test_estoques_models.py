"""Model tests for Estoques Pydantic models."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.estoques import EstoquesSaldosBaseDTO

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def test_estoques_saldos_base_dto_from_fixture() -> None:
    """Deserialize EstoquesSaldosBaseDTO from fixture JSON."""
    payload = json.loads((FIXTURES_DIR / "estoques_saldos_get.json").read_text(encoding="utf-8"))
    model = EstoquesSaldosBaseDTO.model_validate(payload["data"][0])
    assert model.produto is not None
    assert model.produto.id == 100
    assert model.saldo_fisico_total == 50.0
