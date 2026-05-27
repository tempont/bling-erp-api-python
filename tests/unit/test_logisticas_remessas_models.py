"""Model tests for Logísticas - Remessas Pydantic models."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.logisticas import LogisticasRemessasDadosBaseDTO

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def test_logisticas_remessas_dados_base_dto_from_fixture() -> None:
    """Deserialize LogisticasRemessasDadosBaseDTO from fixture JSON."""
    payload = json.loads(
        (FIXTURES_DIR / "logisticas_remessas_get.json").read_text(encoding="utf-8")
    )
    model = LogisticasRemessasDadosBaseDTO.model_validate(payload["data"])
    assert model.id == 501
