"""Pydantic models for Bling Categorias - Produtos endpoints."""

from __future__ import annotations

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class CategoriasProdutosDadosDTO(BlingModel):
    """Product category data (GET/POST/PUT /categorias/produtos).

    The Bling spec uses allOf composition with CategoriasProdutosCategoriPaiDTO.
    We model as a single combined DTO with optional parent field.
    """

    id: int = Field(..., description="ID da categoria de produto")
    descricao: str = Field(..., description="Descrição da categoria")
    categoria_pai: CategoriasProdutosCategoriPaiDTO | None = Field(
        default=None, alias="categoriaPai"
    )


class CategoriasProdutosCategoriPaiDTO(BlingModel):
    """Parent product category reference."""

    id: int = Field(..., description="ID da categoria de produto pai")
