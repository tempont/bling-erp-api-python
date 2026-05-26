"""Pydantic models for Bling Homologação endpoints."""

from __future__ import annotations

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class HomologacaoDadosBaseDTO(BlingModel):
    """Homologation product data (create/update payload)."""

    nome: str | None = Field(default=None, description="Nome do produto")
    preco: float | None = Field(default=None, description="Preço")
    codigo: str | None = Field(default=None, description="Código")


class HomologacaoDadosDTO(BlingModel):
    """Homologation product ID (response)."""

    id: int | None = Field(default=None, description="ID do produto da homologação")


class HomologacaoSituacaoDTO(BlingModel):
    """Status change payload for homologation."""

    situacao: str = Field(..., description="Nova situação (ex: 'I')")
