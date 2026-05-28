# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``grupos_produtos``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import BasePostResponse, Data24


class GruposProdutosGrupoProdutoPaiDTO(BlingModel):
    """OpenAPI schema ``GruposProdutosGrupoProdutoPaiDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        nome: Bling ``nome``; type ``str | None``; opcional."""

    id: int = Field(..., examples=[123456])
    nome: str | None = Field(default=None, examples=["Grupo 1"])


class GruposProdutosPostResponse201(BlingModel):
    """OpenAPI schema ``GruposProdutosPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``BasePostResponse | None``; opcional."""

    data: BasePostResponse | None = None


class GruposProdutosDadosDTO(BlingModel):
    """OpenAPI schema ``GruposProdutosDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        nome: Bling ``nome``; type ``str``; obrigatório.
        grupo_produto_pai: Bling ``grupoProdutoPai``; type ``GruposProdutosGrupoProdutoPaiDTO | None``; opcional."""

    id: int | None = Field(default=None, examples=[123456])
    nome: str = Field(..., examples=["Grupo 1"])
    grupo_produto_pai: GruposProdutosGrupoProdutoPaiDTO | None = Field(
        default=None, alias="grupoProdutoPai"
    )


class GruposProdutosGetResponse200(BlingModel):
    """OpenAPI schema ``GruposProdutosGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[GruposProdutosDadosDTO] | None``; opcional."""

    data: list[GruposProdutosDadosDTO] | None = None


class GruposProdutosPostRequest(
    RootModel[GruposProdutosDadosDTO | GruposProdutosGrupoProdutoPaiDTO]
):
    """OpenAPI schema ``GruposProdutosPostRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        root: Bling ``root``; type ``GruposProdutosDadosDTO | GruposProdutosGrupoProdutoPaiDTO``; obrigatório."""

    root: GruposProdutosDadosDTO | GruposProdutosGrupoProdutoPaiDTO


class GruposProdutosIdGrupoProdutoGetResponse200(BlingModel):
    """OpenAPI schema ``GruposProdutosIdGrupoProdutoGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``GruposProdutosDadosDTO | GruposProdutosGrupoProdutoPaiDTO | None``; opcional."""

    data: GruposProdutosDadosDTO | GruposProdutosGrupoProdutoPaiDTO | None = None


class GruposProdutosIdGrupoProdutoPutRequest(
    RootModel[GruposProdutosDadosDTO | GruposProdutosGrupoProdutoPaiDTO]
):
    """OpenAPI schema ``GruposProdutosIdGrupoProdutoPutRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        root: Bling ``root``; type ``GruposProdutosDadosDTO | GruposProdutosGrupoProdutoPaiDTO``; obrigatório."""

    root: GruposProdutosDadosDTO | GruposProdutosGrupoProdutoPaiDTO


class GruposProdutosDeleteResponse200(BlingModel):
    """OpenAPI schema ``GruposProdutosDeleteResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data24 | None``; opcional."""

    data: Data24 | None = None


__all__ = [
    "GruposProdutosDadosDTO",
    "GruposProdutosDeleteResponse200",
    "GruposProdutosGetResponse200",
    "GruposProdutosGrupoProdutoPaiDTO",
    "GruposProdutosIdGrupoProdutoGetResponse200",
    "GruposProdutosIdGrupoProdutoPutRequest",
    "GruposProdutosPostRequest",
    "GruposProdutosPostResponse201",
]
