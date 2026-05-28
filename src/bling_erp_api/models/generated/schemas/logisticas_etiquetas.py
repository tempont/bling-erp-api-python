# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``logisticas_etiquetas``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel


class LogisticasEtiquetasDadosResponseDTO(BlingModel):
    """OpenAPI schema ``LogisticasEtiquetasDadosResponseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. ID da venda
        link: Bling ``link``; type ``str``; obrigatório. Link para obter a etiqueta
        observacao: Bling ``observacao``; type ``str``; obrigatório. Mensagem de observação"""

    id: int = Field(..., examples=[6423813145])
    link: str = Field(..., examples=["https://bling-storage-dev.s3.sa-east-1.amazonaws.com"])
    observacao: str = Field(
        ...,
        examples=[
            "O formato de impressão selecionado difere do retornado pelo integrador ou pela configuração da logística."
        ],
    )


class LogisticasEtiquetasGetResponse200(BlingModel):
    """OpenAPI schema ``LogisticasEtiquetasGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[LogisticasEtiquetasDadosResponseDTO] | None``; opcional."""

    data: list[LogisticasEtiquetasDadosResponseDTO] | None = None


__all__ = [
    "LogisticasEtiquetasDadosResponseDTO",
    "LogisticasEtiquetasGetResponse200",
]
