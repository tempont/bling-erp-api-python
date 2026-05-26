"""Pydantic models for Bling Grupos de Produtos endpoints."""

from __future__ import annotations

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class GruposProdutosGrupoProdutoPaiDTO(BlingModel):
    """Parent product group reference."""

    id: int = Field(..., description="ID do grupo pai")
    nome: str | None = Field(default=None, description="Nome do grupo pai (readOnly)")


class GruposProdutosDadosDTO(BlingModel):
    """Product group data (GET/POST/PUT)."""

    id: int | None = Field(default=None, description="ID interno (readOnly)")
    nome: str = Field(..., description="Nome do grupo")
    grupo_produto_pai: GruposProdutosGrupoProdutoPaiDTO | None = Field(
        default=None, alias="grupoProdutoPai"
    )
