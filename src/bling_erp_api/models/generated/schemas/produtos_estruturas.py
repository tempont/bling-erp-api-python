# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``produtos_estruturas``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

from .produtos import ProdutosComponenteDTO

if TYPE_CHECKING:
    from .common import Data28
    from .produtos import ProdutosEstruturaDTO


class ProdutosEstruturasIdProdutoEstruturaGetResponse200(BlingModel):
    """OpenAPI schema ``ProdutosEstruturasIdProdutoEstruturaGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``ProdutosEstruturaDTO | None``; opcional."""

    data: ProdutosEstruturaDTO | None = None


class ProdutosEstruturasIdProdutoEstruturaComponentesPostRequest(
    RootModel[list[ProdutosComponenteDTO]]
):
    """OpenAPI schema ``ProdutosEstruturasIdProdutoEstruturaComponentesPostRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        root: Bling ``root``; type ``list[ProdutosComponenteDTO]``; obrigatório."""

    root: list[ProdutosComponenteDTO]


class ProdutosEstruturasDeleteResponse200(BlingModel):
    """OpenAPI schema ``ProdutosEstruturasDeleteResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data28 | None``; opcional."""

    data: Data28 | None = None


__all__ = [
    "ProdutosEstruturasDeleteResponse200",
    "ProdutosEstruturasIdProdutoEstruturaComponentesPostRequest",
    "ProdutosEstruturasIdProdutoEstruturaGetResponse200",
]
