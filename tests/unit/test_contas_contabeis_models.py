"""Model tests for Contas Financeiras Pydantic models."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.contas_contabeis import ContasContabeisDadosDTO

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def test_contas_contabeis_dados_dto_from_fixture() -> None:
    """Deserialize ContasContabeisDadosDTO from fixture JSON."""
    payload = json.loads((FIXTURES_DIR / "contas_contabeis_get.json").read_text(encoding="utf-8"))
    model = ContasContabeisDadosDTO.model_validate(payload["data"])
    assert model.id == 10
    assert model.descricao == "Conta Corrente Principal"
    assert model.tipo == "conta-bancaria"
    assert model.alias_integracao == "bank_account"
