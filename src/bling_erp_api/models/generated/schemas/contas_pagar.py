# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``contas_pagar``. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.models.fields import BlingDate
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

from .contas import ContasDadosBaseDTO

if TYPE_CHECKING:
    from .common import Bordero, Data39
    from .contas import ContasCategoriaDTO, ContasDadosBaseDTO, ContasPortadorDTO
    from .contas_receber import (
        ContasReceberOcorrenciaDTO,
        ContasReceberOcorrenciaParceladaDTO,
        ContasReceberOcorrenciaSemanalDTO,
        ContasReceberOcorrenciaUnicaDTO,
    )


class ContasPagarIdContaPagarBaixarPostResponse200(BlingModel):
    """OpenAPI schema ``ContasPagarIdContaPagarBaixarPostResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        bordero: Bling ``bordero``; type ``Bordero | None``; opcional."""

    bordero: Bordero | None = None


class ContasPagarDadosDTO(BlingModel):
    """OpenAPI schema ``ContasPagarDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        saldo: Bling ``saldo``; type ``float | None``; opcional. Valor total subtraído dos valores dos recebimentos
        data_emissao: Bling ``dataEmissao``; type ``BlingDate | None``; opcional.
        vencimento_original: Bling ``vencimentoOriginal``; type ``BlingDate``; obrigatório.
        numero_documento: Bling ``numeroDocumento``; type ``str | None``; opcional. Número para controle interno da empresa
        competencia: Bling ``competencia``; type ``BlingDate | None``; opcional.
        historico: Bling ``historico``; type ``str | None``; opcional. Descriçao da conta para controle interno da empresa
        numero_banco: Bling ``numeroBanco``; type ``str``; obrigatório. Adicionado automaticamente com o número preenchido no cadastro do banco
        portador: Bling ``portador``; type ``ContasPortadorDTO | None``; opcional.
        categoria: Bling ``categoria``; type ``ContasCategoriaDTO | None``; opcional.
        borderos: Bling ``borderos``; type ``list[int]``; obrigatório.
        ocorrencia: Bling ``ocorrencia``; type ``ContasReceberOcorrenciaUnicaDTO | ContasReceberOcorrenciaParceladaDTO | ContasReceberOcorrenciaDTO | ContasReceberOcorrenciaSemanalDTO | None``; opcional."""

    saldo: float | None = Field(default=None, examples=[100.75])
    data_emissao: BlingDate | None = Field(
        default=None,
        validation_alias=AliasChoices("data_emissao", "dataEmissao"),
        examples=["2023-01-12"],
        serialization_alias="dataEmissao",
    )
    vencimento_original: BlingDate = Field(
        ...,
        validation_alias=AliasChoices("vencimento_original", "vencimentoOriginal"),
        examples=["2023-01-12"],
        serialization_alias="vencimentoOriginal",
    )
    numero_documento: str | None = Field(
        default=None,
        validation_alias=AliasChoices("numero_documento", "numeroDocumento"),
        examples=[""],
        serialization_alias="numeroDocumento",
    )
    competencia: BlingDate | None = Field(default=None, examples=["2023-01-12"])
    historico: str | None = Field(default=None, examples=[""])
    numero_banco: str = Field(
        ...,
        validation_alias=AliasChoices("numero_banco", "numeroBanco"),
        examples=[""],
        serialization_alias="numeroBanco",
    )
    portador: ContasPortadorDTO | None = None
    categoria: ContasCategoriaDTO | None = None
    borderos: list[int]
    ocorrencia: (
        ContasReceberOcorrenciaUnicaDTO
        | ContasReceberOcorrenciaParceladaDTO
        | ContasReceberOcorrenciaDTO
        | ContasReceberOcorrenciaSemanalDTO
        | None
    ) = None


class ContasPagarDadosPostDTO(BlingModel):
    """OpenAPI schema ``ContasPagarDadosPostDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        ocorrencia: Bling ``ocorrencia``; type ``ContasReceberOcorrenciaUnicaDTO | ContasReceberOcorrenciaParceladaDTO | ContasReceberOcorrenciaDTO | ContasReceberOcorrenciaSemanalDTO | None``; opcional."""

    ocorrencia: (
        ContasReceberOcorrenciaUnicaDTO
        | ContasReceberOcorrenciaParceladaDTO
        | ContasReceberOcorrenciaDTO
        | ContasReceberOcorrenciaSemanalDTO
        | None
    ) = None


class ContasPagarGetResponse200(BlingModel):
    """OpenAPI schema ``ContasPagarGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[ContasDadosBaseDTO] | None``; opcional."""

    data: list[ContasDadosBaseDTO] | None = None


class ContasPagarPostRequest(ContasDadosBaseDTO, ContasPagarDadosDTO, ContasPagarDadosPostDTO):
    """OpenAPI schema ``ContasPagarPostRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: ContasDadosBaseDTO, ContasPagarDadosDTO, ContasPagarDadosPostDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        situacao: Bling ``situacao``; type ``int``; obrigatório. `1` Aberto <br>`2` Pago<br>`3` Parcial<br>`4` Devolvido<br>`5` Cancelado<br>`6` Devolvido parcial<br>`7` Confirmado
        vencimento: Bling ``vencimento``; type ``date``; obrigatório.
        valor: Bling ``valor``; type ``float``; obrigatório.
        contato: Bling ``contato``; type ``ContasContatoDTO``; obrigatório.
        forma_pagamento: Bling ``formaPagamento``; type ``ContasFormaPagamentoDTO | None``; opcional.
        saldo: Bling ``saldo``; type ``float | None``; opcional. Valor total subtraído dos valores dos recebimentos
        data_emissao: Bling ``dataEmissao``; type ``date | None``; opcional.
        vencimento_original: Bling ``vencimentoOriginal``; type ``date``; obrigatório.
        numero_documento: Bling ``numeroDocumento``; type ``str | None``; opcional. Número para controle interno da empresa
        competencia: Bling ``competencia``; type ``date | None``; opcional.
        historico: Bling ``historico``; type ``str | None``; opcional. Descriçao da conta para controle interno da empresa
        numero_banco: Bling ``numeroBanco``; type ``str``; obrigatório. Adicionado automaticamente com o número preenchido no cadastro do banco
        portador: Bling ``portador``; type ``ContasPortadorDTO | None``; opcional.
        categoria: Bling ``categoria``; type ``ContasCategoriaDTO | None``; opcional.
        borderos: Bling ``borderos``; type ``list[int]``; obrigatório.
        ocorrencia: Bling ``ocorrencia``; type ``ContasReceberOcorrenciaUnicaDTO | ContasReceberOcorrenciaParceladaDTO | ContasReceberOcorrenciaDTO | ContasReceberOcorrenciaSemanalDTO | None``; opcional."""

    pass


class ContasPagarIdContaPagarGetResponse200(BlingModel):
    """OpenAPI schema ``ContasPagarIdContaPagarGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data39 | None``; opcional."""

    data: Data39 | None = None


class ContasPagarIdContaPagarPutRequest(ContasDadosBaseDTO, ContasPagarDadosDTO):
    """OpenAPI schema ``ContasPagarIdContaPagarPutRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: ContasDadosBaseDTO, ContasPagarDadosDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        situacao: Bling ``situacao``; type ``int``; obrigatório. `1` Aberto <br>`2` Pago<br>`3` Parcial<br>`4` Devolvido<br>`5` Cancelado<br>`6` Devolvido parcial<br>`7` Confirmado
        vencimento: Bling ``vencimento``; type ``date``; obrigatório.
        valor: Bling ``valor``; type ``float``; obrigatório.
        contato: Bling ``contato``; type ``ContasContatoDTO``; obrigatório.
        forma_pagamento: Bling ``formaPagamento``; type ``ContasFormaPagamentoDTO | None``; opcional.
        saldo: Bling ``saldo``; type ``float | None``; opcional. Valor total subtraído dos valores dos recebimentos
        data_emissao: Bling ``dataEmissao``; type ``date | None``; opcional.
        vencimento_original: Bling ``vencimentoOriginal``; type ``date``; obrigatório.
        numero_documento: Bling ``numeroDocumento``; type ``str | None``; opcional. Número para controle interno da empresa
        competencia: Bling ``competencia``; type ``date | None``; opcional.
        historico: Bling ``historico``; type ``str | None``; opcional. Descriçao da conta para controle interno da empresa
        numero_banco: Bling ``numeroBanco``; type ``str``; obrigatório. Adicionado automaticamente com o número preenchido no cadastro do banco
        portador: Bling ``portador``; type ``ContasPortadorDTO | None``; opcional.
        categoria: Bling ``categoria``; type ``ContasCategoriaDTO | None``; opcional.
        borderos: Bling ``borderos``; type ``list[int]``; obrigatório.
        ocorrencia: Bling ``ocorrencia``; type ``ContasReceberOcorrenciaUnicaDTO | ContasReceberOcorrenciaParceladaDTO | ContasReceberOcorrenciaDTO | ContasReceberOcorrenciaSemanalDTO | None``; opcional."""

    pass


__all__ = [
    "ContasPagarDadosDTO",
    "ContasPagarDadosPostDTO",
    "ContasPagarGetResponse200",
    "ContasPagarIdContaPagarBaixarPostResponse200",
    "ContasPagarIdContaPagarGetResponse200",
    "ContasPagarIdContaPagarPutRequest",
    "ContasPagarPostRequest",
]
