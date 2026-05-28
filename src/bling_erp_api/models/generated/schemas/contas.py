# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``contas``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel


class ContasCategoriaDTO(BlingModel):
    """OpenAPI schema ``ContasCategoriaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class ContasContatoDTO(BlingModel):
    """OpenAPI schema ``ContasContatoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class ContasFormaPagamentoDTO(BlingModel):
    """OpenAPI schema ``ContasFormaPagamentoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class ContasPortadorDTO(BlingModel):
    """OpenAPI schema ``ContasPortadorDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class ContasBaixarContaDTO(BlingModel):
    """OpenAPI schema ``ContasBaixarContaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``date``; obrigatório.
        usar_data_vencimento: Bling ``usarDataVencimento``; type ``bool``; obrigatório.
        portador: Bling ``portador``; type ``ContasPortadorDTO``; obrigatório.
        categoria: Bling ``categoria``; type ``ContasCategoriaDTO``; obrigatório.
        historico: Bling ``historico``; type ``str``; obrigatório. Descriçao da conta para controle interno da empresa
        juros: Bling ``juros``; type ``float | None``; opcional. Valor em reais dos juros.
        desconto: Bling ``desconto``; type ``float | None``; opcional. Valor em reais do desconto.
        acrescimo: Bling ``acrescimo``; type ``float | None``; opcional. Valor em reais do acréscimo.
        valor_recebido: Bling ``valorRecebido``; type ``float | None``; opcional. Valor bruto da conta, incluindo a taxa do marketplace se aplicável. Se não for especificado, o valor total da conta será usado
        tarifa: Bling ``tarifa``; type ``float | None``; opcional. O valor da tarifa deve ser preenchido caso a forma de pagamento possua taxas de alíquota ou de valor fixo."""

    data: date = Field(..., examples=["2023-01-12"])
    usar_data_vencimento: bool = Field(..., alias="usarDataVencimento", examples=[False])
    portador: ContasPortadorDTO
    categoria: ContasCategoriaDTO
    historico: str = Field(..., examples=[""])
    juros: float | None = Field(default=0, examples=[10.5])
    desconto: float | None = Field(default=0, examples=[10.5])
    acrescimo: float | None = Field(default=0, examples=[10.5])
    valor_recebido: float | None = Field(default=None, alias="valorRecebido", examples=[100.5])
    tarifa: float | None = Field(default=0, examples=[5])


class ContasDadosBaseDTO(BlingModel):
    """OpenAPI schema ``ContasDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        situacao: Bling ``situacao``; type ``int``; obrigatório. `1` Aberto <br>`2` Pago<br>`3` Parcial<br>`4` Devolvido<br>`5` Cancelado<br>`6` Devolvido parcial<br>`7` Confirmado
        vencimento: Bling ``vencimento``; type ``date``; obrigatório.
        valor: Bling ``valor``; type ``float``; obrigatório.
        contato: Bling ``contato``; type ``ContasContatoDTO``; obrigatório.
        forma_pagamento: Bling ``formaPagamento``; type ``ContasFormaPagamentoDTO | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    situacao: int = Field(..., examples=[1])
    vencimento: date = Field(..., examples=["2023-01-12"])
    valor: float = Field(..., examples=[1500.75])
    contato: ContasContatoDTO
    forma_pagamento: ContasFormaPagamentoDTO | None = Field(default=None, alias="formaPagamento")


__all__ = [
    "ContasBaixarContaDTO",
    "ContasCategoriaDTO",
    "ContasContatoDTO",
    "ContasDadosBaseDTO",
    "ContasFormaPagamentoDTO",
    "ContasPortadorDTO",
]
