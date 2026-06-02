# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``categorias_lojas``. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.models.fields import BlingDate
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import BasePostResponse


class CategoriasLojasCategoriaProdutoDTO(BlingModel):
    """OpenAPI schema ``CategoriasLojasCategoriaProdutoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class CategoriasLojasLojaDTO(BlingModel):
    """OpenAPI schema ``CategoriasLojasLojaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class CategoriasLojasPostResponse201(BlingModel):
    """OpenAPI schema ``CategoriasLojasPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``BasePostResponse | None``; opcional."""

    data: BasePostResponse | None = None


class CategoriasLojasDadosDTO(BlingModel):
    """OpenAPI schema ``CategoriasLojasDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        loja: Bling ``loja``; type ``CategoriasLojasLojaDTO``; obrigatório.
        descricao: Bling ``descricao``; type ``str``; obrigatório.
        codigo: Bling ``codigo``; type ``str``; obrigatório. Código da categoria na loja.
        categoria_produto: Bling ``categoriaProduto``; type ``CategoriasLojasCategoriaProdutoDTO``; obrigatório."""

    id: int | None = Field(default=None, examples=[12345678])
    loja: CategoriasLojasLojaDTO
    descricao: str = Field(..., examples=["Categoria de produto vinculado à loja"])
    codigo: str = Field(..., examples=["12345678"])
    categoria_produto: CategoriasLojasCategoriaProdutoDTO = Field(
        ...,
        validation_alias=AliasChoices("categoria_produto", "categoriaProduto"),
        serialization_alias="categoriaProduto",
    )


class CategoriasLojasGetResponse200(BlingModel):
    """OpenAPI schema ``CategoriasLojasGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[CategoriasLojasDadosDTO] | None``; opcional."""

    data: list[CategoriasLojasDadosDTO] | None = None


class CategoriasLojasIdCategoriaLojaGetResponse200(BlingModel):
    """OpenAPI schema ``CategoriasLojasIdCategoriaLojaGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``CategoriasLojasDadosDTO | None``; opcional."""

    data: CategoriasLojasDadosDTO | None = None


__all__ = [
    "CategoriasLojasCategoriaProdutoDTO",
    "CategoriasLojasDadosDTO",
    "CategoriasLojasGetResponse200",
    "CategoriasLojasIdCategoriaLojaGetResponse200",
    "CategoriasLojasLojaDTO",
    "CategoriasLojasPostResponse201",
]
