"""Model tests for Contas a Pagar Pydantic models."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.contas_pagar import ContasPagarDadosDTO
from bling_erp_api.models.generated.contas_shared import (
    ContasBaixarContaDTO,
    ContasCategoriaDTO,
    ContasPortadorDTO,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def test_contas_pagar_dados_dto_from_fixture() -> None:
    """Deserialize ContasPagarDadosDTO from fixture JSON."""
    payload = json.loads((FIXTURES_DIR / "contas_pagar_get.json").read_text(encoding="utf-8"))
    model = ContasPagarDadosDTO.model_validate(payload["data"])
    assert model.id == 1001
    assert model.situacao == 1
    assert model.vencimento == "2025-03-15"
    assert model.valor == 1500.00
    assert model.saldo == 1500.00
    assert model.data_emissao == "2025-03-01"
    assert model.numero_documento == "NF-001"
    assert model.portador is not None
    assert model.portador.id == 5


def test_contas_baixar_conta_dto_serialization() -> None:
    """Serialize ContasBaixarContaDTO with camelCase aliases."""
    baixa = ContasBaixarContaDTO(
        data="2025-03-16",
        usarDataVencimento=False,
        portador=ContasPortadorDTO(id=5),
        categoria=ContasCategoriaDTO(id=10),
        historico="Pagamento realizado",
        valorRecebido=1500.00,
    )
    result = baixa.model_dump(by_alias=True, exclude_none=True)
    assert result["data"] == "2025-03-16"
    assert result["usarDataVencimento"] is False
    assert result["portador"]["id"] == 5
    assert result["historico"] == "Pagamento realizado"
    assert result["valorRecebido"] == 1500.00
