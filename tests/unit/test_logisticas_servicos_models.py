"""Model tests for Logísticas - Serviços Pydantic models."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.logisticas import LogisticasServicosDadosDTO

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def test_logisticas_servicos_dados_dto_from_fixture() -> None:
    """Deserialize LogisticasServicosDadosDTO from fixture JSON."""
    payload = json.loads(
        (FIXTURES_DIR / "logisticas_servicos_get.json").read_text(encoding="utf-8")
    )
    model = LogisticasServicosDadosDTO.model_validate(payload["data"])
    assert model.id == 201
    assert model.descricao == "PAC"
    assert model.codigo == "04510"
    assert model.aliases == ["PAC", "Encomenda"]
    assert model.ativo is True
    assert model.frete_item == 15.50
    assert model.estimativa_entrega == 7
    assert model.logistica.id == 101
    assert model.transportador.id == 301
