# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``contas_contabeis``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel


class ContasContabeisDadosDTO(BlingModel):
    """OpenAPI schema ``ContasContabeisDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. Id da conta financeira
        descricao: Bling ``descricao``; type ``str | None``; opcional. Descrição personalizada da conta financeira
        tipo: Bling ``tipo``; type ``str | None``; opcional. `banco` Para configuração de boleto CNAB <br> `caixa` Portador caixa sem integração <br> `conta-bancaria` Contas configuradas para cashout (TED ou pix) <br>`integracao-pagamento`...
        alias_integracao: Bling ``aliasIntegracao``; type ``str | None``; opcional. Alias identificador da integração de pagamento"""

    id: int | None = Field(default=None, examples=[12345678])
    descricao: str | None = Field(default=None, examples=["Contas a pagar"])
    tipo: str | None = Field(default=None, examples=["integracao-pagamento"])
    alias_integracao: str | None = Field(
        default=None,
        validation_alias=AliasChoices("alias_integracao", "aliasIntegracao"),
        examples=["BlingPagamentos"],
        serialization_alias="aliasIntegracao",
    )


class ContasContabeisGetResponse200(BlingModel):
    """OpenAPI schema ``ContasContabeisGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[ContasContabeisDadosDTO] | None``; opcional."""

    data: list[ContasContabeisDadosDTO] | None = None


class ContasContabeisIdContaContabilGetResponse200(BlingModel):
    """OpenAPI schema ``ContasContabeisIdContaContabilGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``ContasContabeisDadosDTO | None``; opcional."""

    data: ContasContabeisDadosDTO | None = None


__all__ = [
    "ContasContabeisDadosDTO",
    "ContasContabeisGetResponse200",
    "ContasContabeisIdContaContabilGetResponse200",
]
