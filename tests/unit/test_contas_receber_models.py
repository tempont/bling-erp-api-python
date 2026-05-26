"""Model tests for Contas a Receber Pydantic models."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.contas_receber import ContasReceberDadosListDTO

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def test_contas_receber_dados_list_dto_from_fixture() -> None:
    """Deserialize ContasReceberDadosListDTO from fixture JSON."""
    payload = json.loads((FIXTURES_DIR / "contas_receber_get.json").read_text(encoding="utf-8"))
    model = ContasReceberDadosListDTO.model_validate(payload["data"])
    assert model.id == 2001
    assert model.situacao == 1
    assert model.vencimento == "2025-04-10"
    assert model.valor == 2500.00
    assert model.id_transacao == "TRX001"
    assert model.link_qrcode_pix == "https://pix.example.com/qr"
    assert model.link_boleto == "https://boleto.example.com/123"
    assert model.data_emissao == "2025-04-01"
