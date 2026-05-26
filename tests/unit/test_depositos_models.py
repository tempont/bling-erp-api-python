"""Model tests for Depósitos Pydantic models."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.depositos import DepositosDadosDTO

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def test_depositos_dados_dto_from_fixture() -> None:
    """Deserialize DepositosDadosDTO from fixture JSON."""
    payload = json.loads((FIXTURES_DIR / "depositos_get.json").read_text(encoding="utf-8"))
    model = DepositosDadosDTO.model_validate(payload["data"])
    assert model.id == 1
    assert model.descricao == "Depósito Principal"
    assert model.padrao is True
