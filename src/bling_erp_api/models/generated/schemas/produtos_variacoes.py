# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``produtos_variacoes``. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.models.fields import BlingDate
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import BasePostResponse
    from .produtos import ProdutosDadosDTO


class ProdutosVariacoesAtributoDTO(BlingModel):
    """OpenAPI schema ``ProdutosVariacoesAtributoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        nome: Bling ``nome``; type ``str``; obrigatório.
        opcoes: Bling ``opcoes``; type ``list[str] | None``; opcional."""

    nome: str = Field(..., examples=["Cor"])
    opcoes: list[str] | None = Field(default=None, examples=[["Azul", "Vermelho"]])


class ProdutosVariacoesDadosAtributoDTO(BlingModel):
    """OpenAPI schema ``ProdutosVariacoesDadosAtributoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        atributo_antigo: Bling ``atributoAntigo``; type ``str``; obrigatório.
        atributo_novo: Bling ``atributoNovo``; type ``str``; obrigatório."""

    atributo_antigo: str = Field(
        ...,
        validation_alias=AliasChoices("atributo_antigo", "atributoAntigo"),
        examples=["Cor"],
        serialization_alias="atributoAntigo",
    )
    atributo_novo: str = Field(
        ...,
        validation_alias=AliasChoices("atributo_novo", "atributoNovo"),
        examples=["Coloração"],
        serialization_alias="atributoNovo",
    )


class ProdutosVariacoesProdutoPaiDTO(BlingModel):
    """OpenAPI schema ``ProdutosVariacoesProdutoPaiDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional."""

    id: int | None = Field(default=None, examples=[123456789])


class ProdutosVariacoesIdProdutoPaiAtributosPatchResponse200(BlingModel):
    """OpenAPI schema ``ProdutosVariacoesIdProdutoPaiAtributosPatchResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[BasePostResponse] | None``; opcional."""

    data: list[BasePostResponse] | None = None


class ProdutosVariacoesCombinacaoDadosDTO(BlingModel):
    """OpenAPI schema ``ProdutosVariacoesCombinacaoDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        produto_pai: Bling ``produtoPai``; type ``ProdutosVariacoesProdutoPaiDTO``; obrigatório.
        atributos: Bling ``atributos``; type ``list[ProdutosVariacoesAtributoDTO]``; obrigatório."""

    produto_pai: ProdutosVariacoesProdutoPaiDTO = Field(
        ...,
        validation_alias=AliasChoices("produto_pai", "produtoPai"),
        serialization_alias="produtoPai",
    )
    atributos: list[ProdutosVariacoesAtributoDTO]


class ProdutosVariacoesIdProdutoPaiGetResponse200(BlingModel):
    """OpenAPI schema ``ProdutosVariacoesIdProdutoPaiGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``ProdutosDadosDTO | None``; opcional."""

    data: ProdutosDadosDTO | None = None


class ProdutosVariacoesAtributosGerarCombinacoesPostResponse200(BlingModel):
    """OpenAPI schema ``ProdutosVariacoesAtributosGerarCombinacoesPostResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``ProdutosDadosDTO | None``; opcional."""

    data: ProdutosDadosDTO | None = None


__all__ = [
    "ProdutosVariacoesAtributoDTO",
    "ProdutosVariacoesAtributosGerarCombinacoesPostResponse200",
    "ProdutosVariacoesCombinacaoDadosDTO",
    "ProdutosVariacoesDadosAtributoDTO",
    "ProdutosVariacoesIdProdutoPaiAtributosPatchResponse200",
    "ProdutosVariacoesIdProdutoPaiGetResponse200",
    "ProdutosVariacoesProdutoPaiDTO",
]
