# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``anuncios_categorias``. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.models.fields import BlingDate
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .anuncios import AnunciosCategoriaDTO, AnunciosGetAttributesFromCategoryResponseDTO


class AnunciosCategoriasGetResponse200(BlingModel):
    """OpenAPI schema ``AnunciosCategoriasGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[AnunciosCategoriaDTO] | None``; opcional."""

    data: list[AnunciosCategoriaDTO] | None = None


class AnunciosCategoriasIdCategoriaGetResponse200(BlingModel):
    """OpenAPI schema ``AnunciosCategoriasIdCategoriaGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``AnunciosGetAttributesFromCategoryResponseDTO | None``; opcional."""

    data: AnunciosGetAttributesFromCategoryResponseDTO | None = None


__all__ = [
    "AnunciosCategoriasGetResponse200",
    "AnunciosCategoriasIdCategoriaGetResponse200",
]
