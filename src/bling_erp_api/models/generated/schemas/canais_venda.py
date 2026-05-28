# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``canais_venda``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel


class CanalVendaDadosBaseDTO(BlingModel):
    """OpenAPI schema ``CanalVendaDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. ID do canal de venda.
        descricao: Bling ``descricao``; type ``str | None``; opcional. Descrição do canal de venda.
        tipo: Bling ``tipo``; type ``str | None``; opcional. Tipo do canal de venda.
        situacao: Bling ``situacao``; type ``int | None``; opcional. Situação do canal de venda<br> `1` Habilitado<br> `2` Desabilitado"""

    id: int | None = Field(default=None, examples=[12345678])
    descricao: str | None = Field(default=None, examples=["Loja de teste"])
    tipo: str | None = Field(default=None, examples=["Shopee"])
    situacao: int | None = Field(default=None, examples=[1])


class CanalVendaDepositoDTO(BlingModel):
    """OpenAPI schema ``CanalVendaDepositoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])


class CanalVendaFilialDTO(BlingModel):
    """OpenAPI schema ``CanalVendaFilialDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        cnpj: Bling ``cnpj``; type ``str | None``; opcional. CNPJ da filial.
        id_unidade_negocio: Bling ``idUnidadeNegocio``; type ``int | None``; opcional. ID da unidade de negócio.
        unidade_negocio: Bling ``unidadeNegocio``; type ``str | None``; opcional. Nome da unidade de negócio.
        deposito: Bling ``deposito``; type ``CanalVendaDepositoDTO | None``; opcional.
        padrao: Bling ``padrao``; type ``bool | None``; opcional."""

    cnpj: str | None = Field(default=None, examples=["12.345.678/9012-34"])
    id_unidade_negocio: int | None = Field(
        default=None,
        validation_alias=AliasChoices("id_unidade_negocio", "idUnidadeNegocio"),
        examples=[12345678],
        serialization_alias="idUnidadeNegocio",
    )
    unidade_negocio: str | None = Field(
        default=None,
        validation_alias=AliasChoices("unidade_negocio", "unidadeNegocio"),
        examples=["Empresa Teste"],
        serialization_alias="unidadeNegocio",
    )
    deposito: CanalVendaDepositoDTO | None = None
    padrao: bool | None = Field(default=None, examples=[True])


class CanalVendaTipoIntegracaoDTO(BlingModel):
    """OpenAPI schema ``CanalVendaTipoIntegracaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        nome: Bling ``nome``; type ``str | None``; opcional.
        tipo: Bling ``tipo``; type ``str | None``; opcional.
        agrupador: Bling ``agrupador``; type ``int | None``; opcional. Agrupador do canal de venda"""

    nome: str | None = Field(default=None, examples=["Loja Integrada"])
    tipo: str | None = Field(default=None, examples=["LojaIntegrada"])
    agrupador: int | None = Field(default=None, examples=[1])


class CanaisVendaGetResponse200(BlingModel):
    """OpenAPI schema ``CanaisVendaGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[CanalVendaDadosBaseDTO] | None``; opcional."""

    data: list[CanalVendaDadosBaseDTO] | None = None


class CanaisVendaTiposGetResponse200(BlingModel):
    """OpenAPI schema ``CanaisVendaTiposGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[CanalVendaTipoIntegracaoDTO] | None``; opcional."""

    data: list[CanalVendaTipoIntegracaoDTO] | None = None


class CanalVendaCanalVendaDTO(CanalVendaDadosBaseDTO):
    """OpenAPI schema ``CanalVendaCanalVendaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: CanalVendaDadosBaseDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. ID do canal de venda.
        descricao: Bling ``descricao``; type ``str | None``; opcional. Descrição do canal de venda.
        tipo: Bling ``tipo``; type ``str | None``; opcional. Tipo do canal de venda.
        situacao: Bling ``situacao``; type ``int | None``; opcional. Situação do canal de venda<br> `1` Habilitado<br> `2` Desabilitado
        filiais: Bling ``filiais``; type ``list[CanalVendaFilialDTO] | None``; opcional."""

    filiais: list[CanalVendaFilialDTO] | None = None


class CanaisVendaIdCanalVendaGetResponse200(BlingModel):
    """OpenAPI schema ``CanaisVendaIdCanalVendaGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``CanalVendaCanalVendaDTO | None``; opcional."""

    data: CanalVendaCanalVendaDTO | None = None


__all__ = [
    "CanaisVendaGetResponse200",
    "CanaisVendaIdCanalVendaGetResponse200",
    "CanaisVendaTiposGetResponse200",
    "CanalVendaCanalVendaDTO",
    "CanalVendaDadosBaseDTO",
    "CanalVendaDepositoDTO",
    "CanalVendaFilialDTO",
    "CanalVendaTipoIntegracaoDTO",
]
