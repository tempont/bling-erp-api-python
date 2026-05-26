"""Model tests for Borderôs Pydantic models."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.borderos import (
    BorderosDadosDTO,
    BorderosPagamentoDTO,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def test_borderos_dados_dto_from_fixture() -> None:
    """Deserialize BorderosDadosDTO from fixture JSON."""
    payload = json.loads((FIXTURES_DIR / "borderos_get.json").read_text(encoding="utf-8"))
    model = BorderosDadosDTO.model_validate(payload["data"])
    assert model.id == 123456
    assert model.data == "2025-01-15"
    assert model.historico == "Borderô referente às vendas de janeiro"
    assert model.portador is not None
    assert model.portador.id == 100
    assert model.categoria is not None
    assert model.categoria.id == 200
    assert model.pagamentos is not None
    assert len(model.pagamentos) == 2


def test_borderos_pagamento_dto_from_fixture() -> None:
    """Deserialize BorderosPagamentoDTO from nested fixture data."""
    payload = json.loads((FIXTURES_DIR / "borderos_get.json").read_text(encoding="utf-8"))
    first_payment = payload["data"]["pagamentos"][0]
    model = BorderosPagamentoDTO.model_validate(first_payment)
    assert model.contato.id == 300
    assert model.numero_documento == "DOC-001"
    assert model.valor_pago == 1500.75
    assert model.juros == 5.50
    assert model.desconto == 10.00
    assert model.acrescimo == 0.00
    assert model.tarifa == 2.50
