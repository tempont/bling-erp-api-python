# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``naturezas_operacoes``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .calculos_impostos import CalculosImpostosDadosDTO


class NaturezasOperacoesDadosDTO(BlingModel):
    """OpenAPI schema ``NaturezasOperacoesDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        situacao: Bling ``situacao``; type ``int | None``; opcional. `0` Inativo <br> `1` Ativo
        padrao: Bling ``padrao``; type ``int | None``; opcional. `0` Sem padrão <br>`1` Padrão venda <br> `2` Padrão compra <br> `3` Padrão venda física <br> `4` Padrão venda jurídica <br> `5` Padrão compra física <br> `6` Padrão compra jurídic...
        descricao: Bling ``descricao``; type ``str | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    situacao: int | None = Field(default=None, examples=[1])
    padrao: int | None = Field(default=None, examples=[1])
    descricao: str | None = Field(default=None, examples=["Compra de Mercadoria"])


class NaturezasOperacoesGetResponse200(BlingModel):
    """OpenAPI schema ``NaturezasOperacoesGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[NaturezasOperacoesDadosDTO] | None``; opcional."""

    data: list[NaturezasOperacoesDadosDTO] | None = None


class NaturezasOperacoesIdNaturezaOperacaoObterTributacaoPostResponse200(BlingModel):
    """OpenAPI schema ``NaturezasOperacoesIdNaturezaOperacaoObterTributacaoPostResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``CalculosImpostosDadosDTO | None``; opcional."""

    data: CalculosImpostosDadosDTO | None = None


__all__ = [
    "NaturezasOperacoesDadosDTO",
    "NaturezasOperacoesGetResponse200",
    "NaturezasOperacoesIdNaturezaOperacaoObterTributacaoPostResponse200",
]
