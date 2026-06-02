# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``estoques``. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.models.fields import BlingDate
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import BasePostResponse, Datum3
    from .depositos import Deposito


class Estoques(BlingModel):
    """OpenAPI schema ``Estoques``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        itens: Bling ``itens``; type ``list[int] | None``; opcional."""

    itens: list[int] | None = Field(default=None, examples=[[1234567, 7654321]])


class EstoquesDadosBaseDTO(BlingModel):
    """OpenAPI schema ``EstoquesDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        operacao: Bling ``operacao``; type ``str``; obrigatório. `B` Balanço <br> `E` Entrada <br> `S` Saída
        preco: Bling ``preco``; type ``float | None``; opcional. Preço unitário
        custo: Bling ``custo``; type ``float | None``; opcional. Custo unitário
        quantidade: Bling ``quantidade``; type ``float``; obrigatório.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional."""

    operacao: str = Field(..., examples=["B"])
    preco: float | None = Field(default=None, examples=[1500.75])
    custo: float | None = Field(default=None, examples=[1500.75])
    quantidade: float = Field(..., examples=[50.75])
    observacoes: str | None = Field(default=None, examples=["Observações de estoque"])


class EstoquesDepositoBaseDTO(BlingModel):
    """OpenAPI schema ``EstoquesDepositoBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class EstoquesDepositoDTO(BlingModel):
    """OpenAPI schema ``EstoquesDepositoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        saldo_fisico: Bling ``saldoFisico``; type ``float | None``; opcional. Saldo físico do produto
        saldo_virtual: Bling ``saldoVirtual``; type ``float | None``; opcional. Saldo do produto desconsiderando produtos reservados"""

    saldo_fisico: float | None = Field(
        default=None,
        validation_alias=AliasChoices("saldo_fisico", "saldoFisico"),
        examples=[1250.75],
        serialization_alias="saldoFisico",
    )
    saldo_virtual: float | None = Field(
        default=None,
        validation_alias=AliasChoices("saldo_virtual", "saldoVirtual"),
        examples=[1250.75],
        serialization_alias="saldoVirtual",
    )


class EstoquesProdutoDTO(BlingModel):
    """OpenAPI schema ``EstoquesProdutoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        codigo: Bling ``codigo``; type ``str | None``; opcional."""

    id: int = Field(..., examples=[12345678])
    codigo: str | None = Field(default=None, examples=["12345678"])


class EstoquesSaldosBaseDTO(BlingModel):
    """OpenAPI schema ``EstoquesSaldosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        produto: Bling ``produto``; type ``EstoquesProdutoDTO | None``; opcional.
        saldo_fisico_total: Bling ``saldoFisicoTotal``; type ``float | None``; opcional. Saldo físico total do produto
        saldo_virtual_total: Bling ``saldoVirtualTotal``; type ``float | None``; opcional. Saldo total do produto desconsiderando produtos reservados"""

    produto: EstoquesProdutoDTO | None = None
    saldo_fisico_total: float | None = Field(
        default=None,
        validation_alias=AliasChoices("saldo_fisico_total", "saldoFisicoTotal"),
        examples=[1500.75],
        serialization_alias="saldoFisicoTotal",
    )
    saldo_virtual_total: float | None = Field(
        default=None,
        validation_alias=AliasChoices("saldo_virtual_total", "saldoVirtualTotal"),
        examples=[1500.75],
        serialization_alias="saldoVirtualTotal",
    )


class EstoquesSaldosDTO(BlingModel):
    """OpenAPI schema ``EstoquesSaldosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        depositos: Bling ``depositos``; type ``list[Deposito] | None``; opcional."""

    depositos: list[Deposito] | None = None


class EstoqueGetAllResponseDTO(BlingModel):
    """OpenAPI schema ``EstoqueGetAllResponseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        saldo_virtual_total: Bling ``saldoVirtualTotal``; type ``float | None``; opcional. Saldo em estoque atual, considerando a reserva de estoque."""

    saldo_virtual_total: float | None = Field(
        default=None,
        validation_alias=AliasChoices("saldo_virtual_total", "saldoVirtualTotal"),
        examples=["1.0"],
        serialization_alias="saldoVirtualTotal",
    )


class EstoquesSaldosIdDepositoGetResponse200(BlingModel):
    """OpenAPI schema ``EstoquesSaldosIdDepositoGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[EstoquesSaldosBaseDTO] | None``; opcional."""

    data: list[EstoquesSaldosBaseDTO] | None = None


class EstoquesSaldosGetResponse200(BlingModel):
    """OpenAPI schema ``EstoquesSaldosGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[Datum3] | None``; opcional."""

    data: list[Datum3] | None = None


class EstoquesPostResponse201(BlingModel):
    """OpenAPI schema ``EstoquesPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``BasePostResponse | None``; opcional."""

    data: BasePostResponse | None = None


class EstoquesDadosDTO(BlingModel):
    """OpenAPI schema ``EstoquesDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        produto: Bling ``produto``; type ``EstoquesProdutoDTO``; obrigatório.
        deposito: Bling ``deposito``; type ``EstoquesDepositoBaseDTO``; obrigatório."""

    produto: EstoquesProdutoDTO
    deposito: EstoquesDepositoBaseDTO


class EstoquesPostRequest(EstoquesDadosDTO, EstoquesDadosBaseDTO):
    """OpenAPI schema ``EstoquesPostRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: EstoquesDadosDTO, EstoquesDadosBaseDTO.

    Fields:
        produto: Bling ``produto``; type ``EstoquesProdutoDTO``; obrigatório.
        deposito: Bling ``deposito``; type ``EstoquesDepositoBaseDTO``; obrigatório.
        operacao: Bling ``operacao``; type ``str``; obrigatório. `B` Balanço <br> `E` Entrada <br> `S` Saída
        preco: Bling ``preco``; type ``float | None``; opcional. Preço unitário
        custo: Bling ``custo``; type ``float | None``; opcional. Custo unitário
        quantidade: Bling ``quantidade``; type ``float``; obrigatório.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional."""

    pass


__all__ = [
    "EstoqueGetAllResponseDTO",
    "Estoques",
    "EstoquesDadosBaseDTO",
    "EstoquesDadosDTO",
    "EstoquesDepositoBaseDTO",
    "EstoquesDepositoDTO",
    "EstoquesPostRequest",
    "EstoquesPostResponse201",
    "EstoquesProdutoDTO",
    "EstoquesSaldosBaseDTO",
    "EstoquesSaldosDTO",
    "EstoquesSaldosGetResponse200",
    "EstoquesSaldosIdDepositoGetResponse200",
]
