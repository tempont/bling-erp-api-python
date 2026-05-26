"""Model tests for Homologacao Pydantic models."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.homologation import (
    HomologacaoDadosBaseDTO,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def test_homologacao_dados_base_dto_from_fixture() -> None:
    """Deserialize HomologacaoDadosBaseDTO from fixture JSON."""
    payload = json.loads((FIXTURES_DIR / "homologation_get.json").read_text(encoding="utf-8"))
    model = HomologacaoDadosBaseDTO.model_validate(payload["data"])
    assert model.nome == "Produto Homologação"
    assert model.preco == 10.0
