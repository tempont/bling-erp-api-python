"""Model tests for Logísticas Pydantic models."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.logisticas import LogisticasDadosBaseDTO

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def test_logisticas_dados_base_dto_from_fixture() -> None:
    """Deserialize LogisticasDadosBaseDTO from fixture JSON."""
    payload = json.loads((FIXTURES_DIR / "logisticas_get.json").read_text(encoding="utf-8"))
    model = LogisticasDadosBaseDTO.model_validate(payload["data"])
    assert model.id == 101
    assert model.descricao == "Correios PAC"
    assert model.tipo_integracao == "Correios"
    assert model.integracao_nativa is True
    assert model.situacao == "H"
    assert len(model.servicos) == 1
    assert model.servicos[0].id == 201
