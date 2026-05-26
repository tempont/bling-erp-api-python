"""Model tests for FormasPagamentos Pydantic models."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.payment_methods import (
    FormasPagamentosDadosBaseDTO,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def test_formas_pagamentos_dados_base_dto_from_fixture() -> None:
    """Deserialize FormasPagamentosDadosBaseDTO from fixture JSON."""
    payload = json.loads((FIXTURES_DIR / "payment_methods_get.json").read_text(encoding="utf-8"))
    model = FormasPagamentosDadosBaseDTO.model_validate(payload["data"])
    assert model.descricao == "Boleto"
    assert model.tipo_pagamento == 2
    assert model.finalidade == 3
