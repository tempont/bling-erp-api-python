# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``contas_financeiras``. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.models.fields import BlingDate
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel


class ContasFinanceirasDadosBasicosDTO(BlingModel):
    """OpenAPI schema ``ContasFinanceirasDadosBasicosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        descricao: Bling ``descricao``; type ``str | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    descricao: str | None = Field(default=None, examples=["Conta Contábil"])


__all__ = [
    "ContasFinanceirasDadosBasicosDTO",
]
