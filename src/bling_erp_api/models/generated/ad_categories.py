"""Pydantic models for Bling Ad Categories (Anúncios - Categorias) endpoints."""

from __future__ import annotations

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class AnunciosCategoriaListDTO(BlingModel):
    """Category item for listing (GET /anuncios/categorias)."""

    id: int | None = Field(default=None, description="ID da categoria")
    nome: str | None = Field(default=None, description="Nome da categoria")


class AnunciosGetAttributesFromCategoryResponseDTO(BlingModel):
    """Response for getting category attributes (GET /anuncios/categorias/{idCategoria})."""

    id: int | None = Field(default=None, description="ID do atributo")
    nome: str | None = Field(default=None, description="Nome do atributo")
    obrigatorio: bool | None = Field(default=None, description="Se o atributo é obrigatório")
    tipo: str | None = Field(default=None, description="Tipo do atributo")
    unidade_padrao: str | None = Field(
        default=None,
        alias="unidadePadrao",
        description="Unidade padrão do atributo",
    )
    minimo: int | None = Field(default=None, description="Valor mínimo")
    maximo: int | None = Field(default=None, description="Valor máximo")
