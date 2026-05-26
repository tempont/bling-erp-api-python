"""Pydantic models for Bling Contas a Pagar endpoints."""

from __future__ import annotations

from pydantic import Field

from bling_erp_api.models.base import BlingModel
from bling_erp_api.models.generated.contas_shared import (
    ContasCategoriaDTO,
    ContasOcorrenciaParceladaDTO,
    ContasOcorrenciaRecorrenteDTO,
    ContasOcorrenciaSemanalDTO,
    ContasOcorrenciaUnicaDTO,
    ContasPortadorDTO,
)


class ContasPagarDadosDTO(BlingModel):
    """Contas a Pagar extended data (response/update). Combines allOf from spec."""

    # From ContasDadosBaseDTO
    id: int | None = Field(default=None, description="ID da conta (readOnly)")
    situacao: int | None = Field(default=None, description="Situação (readOnly)")
    vencimento: str | None = Field(default=None, description="Data de vencimento")
    valor: float | None = Field(default=None, description="Valor da conta")
    # From ContasPagarDadosDTO
    saldo: float | None = Field(default=None)
    data_emissao: str | None = Field(default=None, alias="dataEmissao")
    vencimento_original: str | None = Field(default=None, alias="vencimentoOriginal")
    numero_documento: str | None = Field(default=None, alias="numeroDocumento")
    competencia: str | None = Field(default=None)
    historico: str | None = Field(default=None)
    numero_banco: str | None = Field(default=None, alias="numeroBanco")
    portador: ContasPortadorDTO | None = Field(default=None)
    categoria: ContasCategoriaDTO | None = Field(default=None)
    borderos: list[int] | None = Field(default=None)


class ContasPagarSalvarDTO(BlingModel):
    """Create payload for contas a pagar. Combines ContasDadosBaseDTO + ContasPagarDadosDTO + ContasPagarDadosPostDTO."""

    vencimento: str = Field(..., description="Data de vencimento")
    valor: float = Field(..., description="Valor da conta")
    contato: object = Field(..., description="Dados do contato")
    forma_pagamento: object | None = Field(default=None, alias="formaPagamento")
    data_emissao: str | None = Field(default=None, alias="dataEmissao")
    vencimento_original: str | None = Field(default=None, alias="vencimentoOriginal")
    numero_documento: str | None = Field(default=None, alias="numeroDocumento")
    competencia: str | None = Field(default=None)
    historico: str | None = Field(default=None)
    portador: ContasPortadorDTO | None = Field(default=None)
    categoria: ContasCategoriaDTO | None = Field(default=None)
    ocorrencia: (
        ContasOcorrenciaUnicaDTO
        | ContasOcorrenciaParceladaDTO
        | ContasOcorrenciaRecorrenteDTO
        | ContasOcorrenciaSemanalDTO
        | None
    ) = Field(default=None)
