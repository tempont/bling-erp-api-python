"""Pydantic models for Bling Caixas e Bancos endpoints."""

from __future__ import annotations

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class ContasFinanceirasDadosBasicosDTO(BlingModel):
    """Basic financial account reference."""

    id: int | None = Field(default=None, description="ID da conta financeira")
    descricao: str | None = Field(default=None, description="Descrição da conta financeira")


class CaixasBancosDadosBasicoContatoDTO(BlingModel):
    """Basic contact info for cash/bank entries."""

    id: int | None = Field(default=None, description="ID do contato")
    nome: str | None = Field(default=None, description="Nome do contato")
    cnpj: str | None = Field(default=None, description="CNPJ do contato")


class CaixasBancosDadosBasicosCategoriaDTO(BlingModel):
    """Basic category info for cash/bank entries."""

    id: int | None = Field(default=None, description="ID da categoria")
    descricao: str | None = Field(default=None, description="Descrição da categoria")


class CaixasBancosDadosBasicosOrigemDTO(BlingModel):
    """Basic origin info for cash/bank entries."""

    id: int | None = Field(default=None, description="ID da origem")
    tipo: str | None = Field(default=None, description="Tipo da origem")


class CaixasBancosLancamentoParcelaDTO(BlingModel):
    """Installment reference for a cash/bank entry."""

    id: int | None = Field(default=None, description="ID da parcela")


class CaixasBancosLancamentoConciliacaoMovimentacaoDTO(BlingModel):
    """Reconciliation movement reference."""

    id: int | None = Field(default=None, description="ID da conciliação")


class CaixasBancosItemLancamentoDTO(BlingModel):
    """List item representation (GET /caixas)."""

    id: str | None = Field(default=None, description="ID do lançamento")
    deb_cred: str | None = Field(default=None, alias="debCred", description="Débito/Crédito")
    situacao: str | None = Field(default=None, description="Situação")
    valor: float | None = Field(default=None, description="Valor")
    data: str | None = Field(default=None, description="Data")
    observacoes: str | None = Field(default=None, description="Observações")
    descricao: str | None = Field(default=None, description="Descrição")
    origem: CaixasBancosDadosBasicosOrigemDTO | None = Field(default=None)
    contato: CaixasBancosDadosBasicoContatoDTO | None = Field(default=None)
    conta_financeira: ContasFinanceirasDadosBasicosDTO | None = Field(
        default=None, alias="contaFinanceira"
    )


class CaixasBancosLancamentoDTO(BlingModel):
    """Full entry detail (GET /caixas/{idCaixa})."""

    id: int | None = Field(default=None, description="ID do lançamento")
    deb_cred: str | None = Field(default=None, alias="debCred", description="Débito/Crédito")
    saldo: str | None = Field(default=None, description="Saldo")
    situacao: str | None = Field(default=None, description="Situação")
    transferencia: str | None = Field(default=None, description="Transferência")
    tipo_lancamento: str | None = Field(default=None, alias="tipoLancamento")
    data: str | None = Field(default=None, description="Data")
    competencia: str | None = Field(default=None, description="Competência")
    valor: float | None = Field(default=None, description="Valor")
    observacoes: str | None = Field(default=None, description="Observações")
    parcela: CaixasBancosLancamentoParcelaDTO | None = Field(default=None)
    categoria: CaixasBancosDadosBasicosCategoriaDTO | None = Field(default=None)
    conciliacao_movimentacao: CaixasBancosLancamentoConciliacaoMovimentacaoDTO | None = Field(
        default=None, alias="conciliacaoMovimentacao"
    )
    contato: CaixasBancosDadosBasicoContatoDTO | None = Field(default=None)
    origem: CaixasBancosDadosBasicosOrigemDTO | None = Field(default=None)
    conta_financeira: ContasFinanceirasDadosBasicosDTO | None = Field(
        default=None, alias="contaFinanceira"
    )


class CaixasBancosSalvarLancamentoDTO(BlingModel):
    """Create/update payload (POST/PUT /caixas)."""

    id: int | None = Field(default=None, description="ID do lançamento")
    data: str = Field(..., description="Data do lançamento")
    valor: float = Field(..., description="Valor")
    deb_cred: str = Field(..., alias="debCred", description="Débito/Crédito")
    competencia: str = Field(..., description="Competência")
    observacoes: str = Field(..., description="Observações")
    transferencia: str | None = Field(default=None, description="Transferência")
    id_conta_contabil: int | None = Field(
        default=None,
        alias="idContaContabil",
        description="ID da conta contábil (especificado como obrigatório no OpenAPI mas ausente das propriedades)",
    )
    conta_financeira: ContasFinanceirasDadosBasicosDTO | None = Field(
        default=None, alias="contaFinanceira"
    )
    categoria: CaixasBancosDadosBasicosCategoriaDTO | None = Field(default=None)
    origem: CaixasBancosDadosBasicosOrigemDTO | None = Field(default=None)
    contato: CaixasBancosDadosBasicoContatoDTO | None = Field(default=None)


class CaixasBancosSalvarLancamentoResponseDTO(BlingModel):
    """Response after creating/updating an entry."""

    id: int | None = Field(default=None, description="ID do lançamento salvo")
