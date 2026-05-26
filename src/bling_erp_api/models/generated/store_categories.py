"""Pydantic models for Bling Categorias - Lojas endpoints."""

from __future__ import annotations

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class CategoriasLojasLojaDTO(BlingModel):
    """Store reference in a store category binding."""

    id: int = Field(..., description="ID da loja")


class CategoriasLojasCategoriaProdutoDTO(BlingModel):
    """Product category reference in a store category binding."""

    id: int = Field(..., description="ID da categoria de produto")


class CategoriasLojasDadosDTO(BlingModel):
    """Store category binding data (GET/POST/PUT /categorias/lojas)."""

    id: int | None = Field(default=None, description="ID do vínculo (readOnly)")
    loja: CategoriasLojasLojaDTO | None = Field(default=None)
    descricao: str = Field(..., description="Descrição da categoria na loja")
    codigo: str = Field(..., description="Código da categoria na loja")
    categoria_produto: CategoriasLojasCategoriaProdutoDTO | None = Field(
        default=None, alias="categoriaProduto"
    )
