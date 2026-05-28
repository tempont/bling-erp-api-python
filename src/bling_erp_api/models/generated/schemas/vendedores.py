# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``vendedores``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import Data38


class VendedoresComissaoDTO(BlingModel):
    """OpenAPI schema ``VendedoresComissaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        desconto_maximo: Bling ``descontoMaximo``; type ``float``; obrigatório.
        aliquota: Bling ``aliquota``; type ``float``; obrigatório."""

    desconto_maximo: float = Field(
        ...,
        validation_alias=AliasChoices("desconto_maximo", "descontoMaximo"),
        examples=[10],
        serialization_alias="descontoMaximo",
    )
    aliquota: float = Field(..., examples=[2])


class VendedoresContatoDTO(BlingModel):
    """OpenAPI schema ``VendedoresContatoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        nome: Bling ``nome``; type ``str``; obrigatório.
        situacao: Bling ``situacao``; type ``str``; obrigatório. `A` Ativo<br>`I` Inativo<br>`S` Sem movimento<br>`E` Excluído"""

    id: int = Field(..., examples=[12345678])
    nome: str = Field(..., examples=["Vendedor"])
    situacao: str = Field(..., examples=["A"])


class VendedoresDadosDTO(BlingModel):
    """OpenAPI schema ``VendedoresDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        comissoes: Bling ``comissoes``; type ``list[VendedoresComissaoDTO]``; obrigatório."""

    comissoes: list[VendedoresComissaoDTO]


class VendedoresLojaDTO(BlingModel):
    """OpenAPI schema ``VendedoresLojaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class VendedoresDadosBaseDTO(BlingModel):
    """OpenAPI schema ``VendedoresDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        desconto_limite: Bling ``descontoLimite``; type ``float | None``; opcional. Percentagem máxima para ceder como desconto, 0 para sem limite.
        loja: Bling ``loja``; type ``VendedoresLojaDTO | None``; opcional.
        contato: Bling ``contato``; type ``VendedoresContatoDTO``; obrigatório."""

    id: int | None = Field(default=None, examples=[12345678])
    desconto_limite: float | None = Field(
        default=None,
        validation_alias=AliasChoices("desconto_limite", "descontoLimite"),
        examples=[10.12],
        serialization_alias="descontoLimite",
    )
    loja: VendedoresLojaDTO | None = None
    contato: VendedoresContatoDTO


class VendedoresGetResponse200(BlingModel):
    """OpenAPI schema ``VendedoresGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``VendedoresDadosBaseDTO | None``; opcional."""

    data: VendedoresDadosBaseDTO | None = None


class VendedoresIdVendedorGetResponse200(BlingModel):
    """OpenAPI schema ``VendedoresIdVendedorGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data38 | None``; opcional."""

    data: Data38 | None = None


__all__ = [
    "VendedoresComissaoDTO",
    "VendedoresContatoDTO",
    "VendedoresDadosBaseDTO",
    "VendedoresDadosDTO",
    "VendedoresGetResponse200",
    "VendedoresIdVendedorGetResponse200",
    "VendedoresLojaDTO",
]
