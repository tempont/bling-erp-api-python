# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``usuarios``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import Datum8, Datum9


class UsuariosRecuperarSenhaPostResponse200(BlingModel):
    """OpenAPI schema ``UsuariosRecuperarSenhaPostResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[Datum8] | None``; opcional."""

    data: list[Datum8] | None = None


class UsuariosVerificarHashGetResponse200(BlingModel):
    """OpenAPI schema ``UsuariosVerificarHashGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[Datum9] | None``; opcional."""

    data: list[Datum9] | None = None


__all__ = [
    "UsuariosRecuperarSenhaPostResponse200",
    "UsuariosVerificarHashGetResponse200",
]
