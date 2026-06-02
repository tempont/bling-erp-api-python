# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``empresas``. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.models.fields import BlingDate
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel


class EmpresasDadosBasicosDTO(BlingModel):
    """OpenAPI schema ``EmpresasDadosBasicosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``str | None``; opcional. ID da empresa.
        nome: Bling ``nome``; type ``str | None``; opcional. Nome da empresa.
        cnpj: Bling ``cnpj``; type ``str | None``; opcional. CNPJ da empresa.
        email: Bling ``email``; type ``str | None``; opcional. Email da empresa.
        data_contrato: Bling ``dataContrato``; type ``BlingDate | None``; opcional. Data de início do contrato do plano."""

    id: str | None = Field(default=None, examples=["436c56a5679921f5f13a3d6433561773"])
    nome: str | None = Field(default=None, examples=["Empresa Teste LTDA"])
    cnpj: str | None = Field(default=None, examples=["12.345.657/8910-11"])
    email: str | None = Field(default=None, examples=["empresa@email.com"])
    data_contrato: BlingDate | None = Field(
        default=None,
        validation_alias=AliasChoices("data_contrato", "dataContrato"),
        examples=["2024-12-31"],
        serialization_alias="dataContrato",
    )


class EmpresasMeDadosBasicosGetResponse200(BlingModel):
    """OpenAPI schema ``EmpresasMeDadosBasicosGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``EmpresasDadosBasicosDTO | None``; opcional."""

    data: EmpresasDadosBasicosDTO | None = None


__all__ = [
    "EmpresasDadosBasicosDTO",
    "EmpresasMeDadosBasicosGetResponse200",
]
