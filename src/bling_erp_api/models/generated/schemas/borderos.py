# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``borderos``. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.models.fields import BlingDate
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel


class BorderosCategoriaDTO(BlingModel):
    """OpenAPI schema ``BorderosCategoriaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class BorderosContatoDTO(BlingModel):
    """OpenAPI schema ``BorderosContatoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class BorderosPagamentoDTO(BlingModel):
    """OpenAPI schema ``BorderosPagamentoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        contato: Bling ``contato``; type ``BorderosContatoDTO``; obrigatório.
        numero_documento: Bling ``numeroDocumento``; type ``str``; obrigatório.
        valor_pago: Bling ``valorPago``; type ``float``; obrigatório.
        juros: Bling ``juros``; type ``float``; obrigatório.
        desconto: Bling ``desconto``; type ``float``; obrigatório.
        acrescimo: Bling ``acrescimo``; type ``float``; obrigatório.
        tarifa: Bling ``tarifa``; type ``float``; obrigatório. Tarifa da forma de pagamento"""

    contato: BorderosContatoDTO
    numero_documento: str = Field(
        ...,
        validation_alias=AliasChoices("numero_documento", "numeroDocumento"),
        examples=[""],
        serialization_alias="numeroDocumento",
    )
    valor_pago: float = Field(
        ...,
        validation_alias=AliasChoices("valor_pago", "valorPago"),
        examples=[1500.75],
        serialization_alias="valorPago",
    )
    juros: float = Field(..., examples=[10])
    desconto: float = Field(..., examples=[10])
    acrescimo: float = Field(..., examples=[10])
    tarifa: float = Field(..., examples=[10])


class BorderosPortadorDTO(BlingModel):
    """OpenAPI schema ``BorderosPortadorDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class BorderosDadosDTO(BlingModel):
    """OpenAPI schema ``BorderosDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        data: Bling ``data``; type ``BlingDate``; obrigatório.
        historico: Bling ``historico``; type ``str``; obrigatório.
        portador: Bling ``portador``; type ``BorderosPortadorDTO``; obrigatório.
        categoria: Bling ``categoria``; type ``BorderosCategoriaDTO``; obrigatório.
        pagamentos: Bling ``pagamentos``; type ``list[BorderosPagamentoDTO]``; obrigatório."""

    id: int = Field(..., examples=[12345678])
    data: BlingDate = Field(..., examples=["2023-01-12"])
    historico: str = Field(..., examples=["Referente ao pedido nº 12345678"])
    portador: BorderosPortadorDTO
    categoria: BorderosCategoriaDTO
    pagamentos: list[BorderosPagamentoDTO]


class BorderosIdBorderoGetResponse200(BlingModel):
    """OpenAPI schema ``BorderosIdBorderoGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``BorderosDadosDTO | None``; opcional."""

    data: BorderosDadosDTO | None = None


__all__ = [
    "BorderosCategoriaDTO",
    "BorderosContatoDTO",
    "BorderosDadosDTO",
    "BorderosIdBorderoGetResponse200",
    "BorderosPagamentoDTO",
    "BorderosPortadorDTO",
]
