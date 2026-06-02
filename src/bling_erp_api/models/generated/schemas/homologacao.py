# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``homologacao``. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.models.fields import BlingDate
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import Data12


class HomologacaoDadosBaseDTO(BlingModel):
    """OpenAPI schema ``HomologacaoDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        nome: Bling ``nome``; type ``str | None``; opcional.
        preco: Bling ``preco``; type ``float | None``; opcional.
        codigo: Bling ``codigo``; type ``str | None``; opcional."""

    nome: str | None = Field(default=None, examples=["Copo do Bling"])
    preco: float | None = Field(default=None, examples=[32.56])
    codigo: str | None = Field(default=None, examples=["COD-4587"])


class HomologacaoDadosDTO(BlingModel):
    """OpenAPI schema ``HomologacaoDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])


class HomologacaoSituacaoDTO(BlingModel):
    """OpenAPI schema ``HomologacaoSituacaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        situacao: Bling ``situacao``; type ``str | None``; opcional."""

    situacao: str | None = Field(default=None, examples=["I"])


class HomologacaoProdutosGetResponse200(BlingModel):
    """OpenAPI schema ``HomologacaoProdutosGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``HomologacaoDadosBaseDTO | None``; opcional."""

    data: HomologacaoDadosBaseDTO | None = None


class HomologacaoProdutosPostResponse201(BlingModel):
    """OpenAPI schema ``HomologacaoProdutosPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data12 | None``; opcional."""

    data: Data12 | None = None


__all__ = [
    "HomologacaoDadosBaseDTO",
    "HomologacaoDadosDTO",
    "HomologacaoProdutosGetResponse200",
    "HomologacaoProdutosPostResponse201",
    "HomologacaoSituacaoDTO",
]
