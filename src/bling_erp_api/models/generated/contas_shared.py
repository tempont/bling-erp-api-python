"""Shared Pydantic models for Bling Contas (Pagar e Receber) endpoints."""

from __future__ import annotations

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class ContasContatoDTO(BlingModel):
    """Contact reference in a conta."""

    id: int = Field(..., description="ID do contato")


class ContasFormaPagamentoDTO(BlingModel):
    """Payment method reference."""

    id: int = Field(..., description="ID da forma de pagamento")


class ContasPortadorDTO(BlingModel):
    """Portador (financial account) reference."""

    id: int = Field(..., description="ID do portador")


class ContasCategoriaDTO(BlingModel):
    """Category reference."""

    id: int = Field(..., description="ID da categoria")


class ContasDadosBaseDTO(BlingModel):
    """Base conta data shared by ContasPagar and ContasReceber."""

    id: int | None = Field(default=None, description="ID da conta (readOnly)")
    situacao: int | None = Field(
        default=None,
        description="Situação: 1=Aberto, 2=Pago, 3=Parcial, 4=Devolvido, 5=Cancelado (readOnly)",
    )
    vencimento: str = Field(..., description="Data de vencimento")
    valor: float = Field(..., description="Valor da conta")
    contato: ContasContatoDTO = Field(...)
    forma_pagamento: ContasFormaPagamentoDTO | None = Field(default=None, alias="formaPagamento")


class ContasBaixarContaDTO(BlingModel):
    """Payload for baixar (settle) a conta."""

    data: str = Field(..., description="Data do pagamento/recebimento")
    usar_data_vencimento: bool = Field(..., alias="usarDataVencimento")
    portador: ContasPortadorDTO = Field(...)
    categoria: ContasCategoriaDTO = Field(...)
    historico: str = Field(...)
    juros: float | None = Field(default=None)
    desconto: float | None = Field(default=None)
    acrescimo: float | None = Field(default=None)
    valor_recebido: float | None = Field(default=None, alias="valorRecebido")
    tarifa: float | None = Field(default=None)


class ContasOcorrenciaUnicaDTO(BlingModel):
    """Single occurrence (tipo=1)."""

    tipo: int = Field(1, description="Tipo de ocorrência: 1=Única")


class ContasOcorrenciaParceladaDTO(BlingModel):
    """Installment occurrence (tipo=2)."""

    tipo: int = Field(2, description="Tipo de ocorrência: 2=Parcelada")
    considerar_dias_uteis: bool = Field(..., alias="considerarDiasUteis")
    dia_vencimento: int = Field(..., alias="diaVencimento")
    numero_parcelas: int = Field(..., alias="numeroParcelas")


class ContasOcorrenciaRecorrenteDTO(BlingModel):
    """Recurring occurrence (tipo=3..8). Tipos: 3=Mensal, 4=Bimestral, 5=Trimestral, 6=Semestral, 7=Anual, 8=Quinzenal."""

    tipo: int = Field(..., description="Tipo de recorrência: 3=Mensal a 8=Quinzenal")
    considerar_dias_uteis: bool = Field(..., alias="considerarDiasUteis")
    dia_vencimento: int = Field(..., alias="diaVencimento")
    data_limite: str | None = Field(default=None, alias="dataLimite")


class ContasOcorrenciaSemanalDTO(BlingModel):
    """Weekly occurrence (tipo=9)."""

    tipo: int = Field(9, description="Tipo de ocorrência: 9=Semanal")
    considerar_dias_uteis: bool = Field(..., alias="considerarDiasUteis")
    dia_semana_vencimento: int = Field(..., alias="diaSemanaVencimento")
    data_limite: str | None = Field(default=None, alias="dataLimite")
