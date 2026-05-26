"""Pydantic models for Bling Formas de Pagamentos endpoints."""

from __future__ import annotations

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class FormasPagamentosTaxaDTO(BlingModel):
    """Tax/fee configuration for a payment method."""

    aliquota: float | None = Field(default=None, description="% sobre valor da parcela")
    valor: float | None = Field(default=None, description="Valor fixo")
    prazo: int | None = Field(default=None, description="Dias de retenção")


class FormasPagamentosDadosCartaoDTO(BlingModel):
    """Card data for credit/debit payment methods."""

    bandeira: int = Field(..., description="Bandeira: 1=Visa")
    tipo: int = Field(..., description="1=TEF, 2=POS")
    cnpj_credenciadora: str | None = Field(default=None, alias="cnpjCredenciadora")
    auto_liquidacao: int | None = Field(default=None, alias="autoLiquidacao")


class FormasPagamentosDadosBaseDTO(BlingModel):
    """Base payment method data (list/create)."""

    id: int | None = Field(default=None, description="ID (readOnly)")
    descricao: str = Field(..., description="Nome da forma de pagamento")
    tipo_pagamento: int = Field(..., alias="tipoPagamento", description="1=Dinheiro...99=Outros")
    situacao: int | None = Field(default=None, description="0=Inativa, 1=Ativa")
    fixa: bool | None = Field(default=None, description="Fixa (readOnly)")
    padrao: int | None = Field(default=None, description="0=Não, 1=Padrão, 2=Padrão devolução")
    finalidade: int = Field(..., description="1=Pagamentos, 2=Recebimentos, 3=Ambos")
    juros: float | None = Field(default=None)
    multa: float | None = Field(default=None)


class FormasPagamentosDadosDTO(BlingModel):
    """Extended payment method data."""

    condicao: str | None = Field(default=None, description="Condição de pagamento padrão")
    destino: int = Field(..., description="1=Conta, 2=Ficha financeira, 3=Caixa e bancos")
    utiliza_dias_uteis: bool | None = Field(default=None, alias="utilizaDiasUteis")
    taxas: FormasPagamentosTaxaDTO | None = Field(default=None)
    dados_cartao: FormasPagamentosDadosCartaoDTO | None = Field(default=None, alias="dadosCartao")


class FormasPagamentosSalvarDTO(BlingModel):
    """Create/update payment method payload (allOf composition)."""

    descricao: str = Field(...)
    tipo_pagamento: int = Field(..., alias="tipoPagamento")
    finalidade: int = Field(...)
    situacao: int | None = Field(default=None)
    padrao: int | None = Field(default=None)
    juros: float | None = Field(default=None)
    multa: float | None = Field(default=None)
    condicao: str | None = Field(default=None)
    destino: int | None = Field(default=None)
    utiliza_dias_uteis: bool | None = Field(default=None, alias="utilizaDiasUteis")
    taxas: FormasPagamentosTaxaDTO | None = Field(default=None)
    dados_cartao: FormasPagamentosDadosCartaoDTO | None = Field(default=None, alias="dadosCartao")


class FormasPagamentosAlterarSituacaoDTO(BlingModel):
    """Payload for changing payment method status."""

    situacao: int = Field(..., description="1=Ativa, 0=Inativa")


class FormasPagamentosDefinirPadraoDTO(BlingModel):
    """Payload for setting payment method default."""

    padrao: int = Field(..., description="1=Pagamento, 2=Devolução, 3=Fiado")
