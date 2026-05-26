"""Pydantic models for Bling Borderôs endpoints."""

from __future__ import annotations

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class BorderosContatoDTO(BlingModel):
    """Contact reference in a bordero payment."""

    id: int = Field(..., description="ID do contato")


class BorderosPortadorDTO(BlingModel):
    """Holder reference for a bordero."""

    id: int = Field(..., description="ID do portador")


class BorderosCategoriaDTO(BlingModel):
    """Category reference for a bordero."""

    id: int = Field(..., description="ID da categoria")


class BorderosPagamentoDTO(BlingModel):
    """Payment entry in a bordero."""

    contato: BorderosContatoDTO = Field(...)
    numero_documento: str = Field(..., alias="numeroDocumento")
    valor_pago: float = Field(..., alias="valorPago")
    juros: float = Field(...)
    desconto: float = Field(...)
    acrescimo: float = Field(...)
    tarifa: float = Field(...)


class BorderosDadosDTO(BlingModel):
    """Full bordero data (GET /borderos/{idBordero})."""

    id: int = Field(...)
    data: str = Field(...)
    historico: str = Field(...)
    portador: BorderosPortadorDTO = Field(...)
    categoria: BorderosCategoriaDTO = Field(...)
    pagamentos: list[BorderosPagamentoDTO] = Field(...)
