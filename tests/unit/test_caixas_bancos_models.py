"""Model tests for Caixas e Bancos Pydantic models."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.caixas_bancos import (
    CaixasBancosDadosBasicoContatoDTO,
    CaixasBancosDadosBasicosCategoriaDTO,
    CaixasBancosDadosBasicosOrigemDTO,
    CaixasBancosItemLancamentoDTO,
    CaixasBancosLancamentoDTO,
    CaixasBancosSalvarLancamentoDTO,
    CaixasBancosSalvarLancamentoResponseDTO,
    ContasFinanceirasDadosBasicosDTO,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def test_caixas_bancos_item_lancamento_dto_from_fixture() -> None:
    """Deserialize CaixasBancosItemLancamentoDTO from list fixture."""
    payload = json.loads((FIXTURES_DIR / "caixas_bancos_list.json").read_text(encoding="utf-8"))
    model = CaixasBancosItemLancamentoDTO.model_validate(payload["data"][0])
    assert model.id == "1"
    assert model.deb_cred == "D"
    assert model.situacao == "R"
    assert model.valor == 500.00
    assert model.data == "2025-01-10"
    assert model.observacoes == "Pagamento de fornecedor"
    assert model.descricao == "Fornecedor ABC"
    assert model.origem is not None
    assert model.origem.id == 10
    assert model.origem.tipo == "duplicata"
    assert model.contato is not None
    assert model.contato.nome == "Fornecedor ABC Ltda"
    assert model.conta_financeira is not None
    assert model.conta_financeira.descricao == "Conta Corrente"


def test_caixas_bancos_lancamento_dto_from_fixture() -> None:
    """Deserialize CaixasBancosLancamentoDTO from fixture JSON."""
    payload = json.loads((FIXTURES_DIR / "caixas_bancos_get.json").read_text(encoding="utf-8"))
    model = CaixasBancosLancamentoDTO.model_validate(payload["data"])
    assert model.id == 12345678
    assert model.deb_cred == "D"
    assert model.saldo == "N"
    assert model.situacao == "R"
    assert model.transferencia == "0"
    assert model.tipo_lancamento == "1"
    assert model.data == "2025-01-10"
    assert model.competencia == "2025-01-01"
    assert model.valor == 500.00
    assert model.observacoes == "Pagamento de fornecedor"
    assert model.parcela is not None
    assert model.parcela.id == 555
    assert model.categoria is not None
    assert model.categoria.descricao == "Despesas Operacionais"
    assert model.conciliacao_movimentacao is not None
    assert model.conciliacao_movimentacao.id == 777
    assert model.contato is not None
    assert model.contato.cnpj == "12345678000199"
    assert model.origem is not None
    assert model.origem.tipo == "duplicata"
    assert model.conta_financeira is not None
    assert model.conta_financeira.descricao == "Conta Corrente"


def test_caixas_bancos_salvar_lancamento_dto_serialization() -> None:
    """Serialize CaixasBancosSalvarLancamentoDTO with camelCase aliases."""
    lancamento = CaixasBancosSalvarLancamentoDTO(
        data="2025-02-01",
        valor=350.00,
        debCred="C",
        competencia="2025-02-01",
        observacoes="Venda balcão",
        transferencia="0",
        idContaContabil=42,
        contaFinanceira=ContasFinanceirasDadosBasicosDTO(id=1),
        categoria=CaixasBancosDadosBasicosCategoriaDTO(id=10),
        origem=CaixasBancosDadosBasicosOrigemDTO(id=10),
        contato=CaixasBancosDadosBasicoContatoDTO(id=100),
    )
    result = lancamento.model_dump(by_alias=True, exclude_none=True)
    assert result["data"] == "2025-02-01"
    assert result["valor"] == 350.00
    assert result["debCred"] == "C"
    assert result["competencia"] == "2025-02-01"
    assert result["observacoes"] == "Venda balcão"
    assert result["transferencia"] == "0"
    assert result["idContaContabil"] == 42
    assert result["contaFinanceira"]["id"] == 1
    assert result["categoria"]["id"] == 10
    assert result["origem"]["id"] == 10
    assert result["contato"]["id"] == 100


def test_caixas_bancos_salvar_lancamento_response_dto_from_fixture() -> None:
    """Deserialize CaixasBancosSalvarLancamentoResponseDTO from fixture JSON."""
    payload = json.loads((FIXTURES_DIR / "caixas_bancos_create.json").read_text(encoding="utf-8"))
    model = CaixasBancosSalvarLancamentoResponseDTO.model_validate(payload["data"])
    assert model.id == 99999
