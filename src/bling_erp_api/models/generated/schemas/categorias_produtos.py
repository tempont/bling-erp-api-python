# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``categorias_produtos``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import BasePostResponse, Data4, Datum2


class CategoriasProdutosCategoriPaiDTO(BlingModel):
    """OpenAPI schema ``CategoriasProdutosCategoriPaiDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. Id da categoria do produto pai."""

    id: int = Field(..., examples=[12345678])


class CategoriasProdutosDadosDTO(BlingModel):
    """OpenAPI schema ``CategoriasProdutosDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        descricao: Bling ``descricao``; type ``str``; obrigatório. Descrição da categoria"""

    id: int = Field(..., examples=[12345678])
    descricao: str = Field(..., examples=["Eletrônicos"])


class CategoriasProdutos(BlingModel):
    """OpenAPI schema ``CategoriasProdutos``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. ID da categoria de produto"""

    id: int = Field(..., examples=[12345678])


class CategoriasProdutosGetResponse200(BlingModel):
    """OpenAPI schema ``CategoriasProdutosGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[Datum2] | None``; opcional."""

    data: list[Datum2] | None = None


class CategoriasProdutosPostRequest(CategoriasProdutosDadosDTO):
    """OpenAPI schema ``CategoriasProdutosPostRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: CategoriasProdutosDadosDTO.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        descricao: Bling ``descricao``; type ``str``; obrigatório. Descrição da categoria
        categoria_pai: Bling ``categoriaPai``; type ``CategoriasProdutosCategoriPaiDTO | None``; opcional."""

    categoria_pai: CategoriasProdutosCategoriPaiDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("categoria_pai", "categoriaPai"),
        serialization_alias="categoriaPai",
    )


class CategoriasProdutosPostResponse201(BlingModel):
    """OpenAPI schema ``CategoriasProdutosPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``BasePostResponse | None``; opcional."""

    data: BasePostResponse | None = None


class CategoriasProdutosIdCategoriaProdutoGetResponse200(BlingModel):
    """OpenAPI schema ``CategoriasProdutosIdCategoriaProdutoGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data4 | None``; opcional."""

    data: Data4 | None = None


__all__ = [
    "CategoriasProdutos",
    "CategoriasProdutosCategoriPaiDTO",
    "CategoriasProdutosDadosDTO",
    "CategoriasProdutosGetResponse200",
    "CategoriasProdutosIdCategoriaProdutoGetResponse200",
    "CategoriasProdutosPostRequest",
    "CategoriasProdutosPostResponse201",
]
