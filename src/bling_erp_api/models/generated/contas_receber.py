"""Pydantic models for Bling Contas a Receber endpoints."""

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


class ContasReceberVendedorDTO(BlingModel):
    """Salesperson reference for contas a receber."""

    id: int = Field(..., description="ID do vendedor")


class ContasReceberDadosListDTO(BlingModel):
    """List item for contas a receber (GET /contas/receber)."""

    id: int | None = Field(default=None, description="ID da conta (readOnly)")
    situacao: int | None = Field(default=None, description="Situação (readOnly)")
    vencimento: str | None = Field(default=None, description="Data de vencimento")
    valor: float | None = Field(default=None, description="Valor da conta")
    id_transacao: str | None = Field(default=None, alias="idTransacao")
    link_qrcode_pix: str | None = Field(default=None, alias="linkQRCodePix")
    link_boleto: str | None = Field(default=None, alias="linkBoleto")
    data_emissao: str | None = Field(default=None, alias="dataEmissao")
    contato: object | None = Field(default=None)
    forma_pagamento: object | None = Field(default=None, alias="formaPagamento")
    conta_contabil: object | None = Field(default=None, alias="contaContabil")
    origem: object | None = Field(default=None)


class ContasReceberSalvarDTO(BlingModel):
    """Create/update payload for contas a receber. Combines allOf from spec."""

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
    vendedor: ContasReceberVendedorDTO | None = Field(default=None)
    borderos: list[int] | None = Field(default=None)
    ocorrencia: (
        ContasOcorrenciaUnicaDTO
        | ContasOcorrenciaParceladaDTO
        | ContasOcorrenciaRecorrenteDTO
        | ContasOcorrenciaSemanalDTO
        | None
    ) = Field(default=None)


class ContasReceberBoletosDadosDTO(BlingModel):
    """Individual boleto data."""

    id: int | None = Field(default=None)
    numero_externo: str | None = Field(default=None, alias="numeroExterno")
    vencimento: str | None = Field(default=None)
    valor: float | None = Field(default=None)
    situacao: int | None = Field(default=None)


class ContasReceberBoletosDadosBaseDTO(BlingModel):
    """Response for GET /contas/receber/boletos."""

    venda: object | None = Field(default=None)
    nota_fiscal: object | None = Field(default=None, alias="notaFiscal")
    valor_total: float | None = Field(default=None, alias="valorTotal")
    contas: list[ContasReceberBoletosDadosDTO] | None = Field(default=None)


class ContasReceberBoletosCancelarDTO(BlingModel):
    """Payload for POST /contas/receber/boletos/cancelar."""

    autenticacao: object | None = Field(default=None)
    origem: object | None = Field(default=None)
    conta: object | None = Field(default=None)
    motivo: str = Field(..., description="Motivo do cancelamento")
