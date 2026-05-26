"""Model tests for Empresas Pydantic models."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.empresas import EmpresasDadosBasicosDTO

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def test_empresas_dados_basicos_dto_from_fixture() -> None:
    """Deserialize EmpresasDadosBasicosDTO from fixture JSON."""
    payload = json.loads((FIXTURES_DIR / "empresas_get.json").read_text(encoding="utf-8"))
    model = EmpresasDadosBasicosDTO.model_validate(payload["data"])
    assert model.cnpj == "12345678000199"
