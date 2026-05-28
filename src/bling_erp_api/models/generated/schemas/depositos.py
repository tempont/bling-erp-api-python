# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``depositos``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

from .common import BasePostResponse
from .estoques import EstoquesDepositoBaseDTO, EstoquesDepositoDTO

if TYPE_CHECKING:
    from .common import BasePostResponse, ErrorField


class DepositosDadosDTO(BlingModel):
    """OpenAPI schema ``DepositosDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        descricao: Bling ``descricao``; type ``str``; obrigatório.
        situacao: Bling ``situacao``; type ``int``; obrigatório. `0` Inativo <br> `1` Ativo
        padrao: Bling ``padrao``; type ``bool``; obrigatório.
        desconsiderar_saldo: Bling ``desconsiderarSaldo``; type ``bool``; obrigatório."""

    id: int | None = Field(default=None, examples=[12345678])
    descricao: str = Field(..., examples=["Depósito Geral"])
    situacao: int = Field(..., examples=[1])
    padrao: bool = Field(..., examples=[False])
    desconsiderar_saldo: bool = Field(..., alias="desconsiderarSaldo", examples=[False])


class Deposito(EstoquesDepositoBaseDTO, EstoquesDepositoDTO):
    """OpenAPI schema ``Deposito``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: EstoquesDepositoBaseDTO, EstoquesDepositoDTO.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        saldo_fisico: Bling ``saldoFisico``; type ``float | None``; opcional. Saldo físico do produto
        saldo_virtual: Bling ``saldoVirtual``; type ``float | None``; opcional. Saldo do produto desconsiderando produtos reservados"""

    pass


class DepositosGetResponse200(BlingModel):
    """OpenAPI schema ``DepositosGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[DepositosDadosDTO] | None``; opcional."""

    data: list[DepositosDadosDTO] | None = None


class DepositosPostResponse201(BlingModel):
    """OpenAPI schema ``DepositosPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``BasePostResponse | None``; opcional."""

    data: BasePostResponse | None = None


class DepositosIdDepositoGetResponse200(BlingModel):
    """OpenAPI schema ``DepositosIdDepositoGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``DepositosDadosDTO | None``; opcional."""

    data: DepositosDadosDTO | None = None


class DepositosIdDepositoPutResponse200(BasePostResponse):
    """OpenAPI schema ``DepositosIdDepositoPutResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: BasePostResponse.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        alertas: Bling ``alertas``; type ``list[ErrorField] | None``; opcional."""

    alertas: list[ErrorField] | None = None


__all__ = [
    "Deposito",
    "DepositosDadosDTO",
    "DepositosGetResponse200",
    "DepositosIdDepositoGetResponse200",
    "DepositosIdDepositoPutResponse200",
    "DepositosPostResponse201",
]
