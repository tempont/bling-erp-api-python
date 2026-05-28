# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``logisticas_servicos``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel


class LogisticasServicosDadosSaveDTO(BlingModel):
    """OpenAPI schema ``LogisticasServicosDadosSaveDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. Id do serviço"""

    id: int | None = Field(default=None, examples=["123445"])


class LogisticasServicosDadosSituationDTO(BlingModel):
    """OpenAPI schema ``LogisticasServicosDadosSituationDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        ativo: Bling ``ativo``; type ``bool``; obrigatório. Define se está ativo ou não"""

    ativo: bool = Field(..., examples=[True])


class LogisticasServicosLogisticaDTO(BlingModel):
    """OpenAPI schema ``LogisticasServicosLogisticaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class LogisticasServicosTransportadorDTO(BlingModel):
    """OpenAPI schema ``LogisticasServicosTransportadorDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class LogisticasServicosPostResponse201(BlingModel):
    """OpenAPI schema ``LogisticasServicosPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[LogisticasServicosDadosSaveDTO] | None``; opcional."""

    data: list[LogisticasServicosDadosSaveDTO] | None = None


class LogisticasServicosIdLogisticaServicoPutResponse200(BlingModel):
    """OpenAPI schema ``LogisticasServicosIdLogisticaServicoPutResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``LogisticasServicosDadosSaveDTO | None``; opcional."""

    data: LogisticasServicosDadosSaveDTO | None = None


class LogisticasServicosDadosDTO(BlingModel):
    """OpenAPI schema ``LogisticasServicosDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. Id do serviço
        descricao: Bling ``descricao``; type ``str``; obrigatório. Descrição do serviço da logística
        codigo: Bling ``codigo``; type ``str``; obrigatório. Código do serviço
        aliases: Bling ``aliases``; type ``list[str]``; obrigatório. Aliases do serviço
        ativo: Bling ``ativo``; type ``bool | None``; opcional. Define se está ativo ou não
        frete_item: Bling ``freteItem``; type ``float``; obrigatório. Valor do frete que será calculado para cada item do pedido
        estimativa_entrega: Bling ``estimativaEntrega``; type ``int``; obrigatório. Será o prazo, em dias úteis, de entrega da mercadoria para esse serviço.
        id_codigo_servico: Bling ``idCodigoServico``; type ``str | None``; opcional. Id do código do servico
        logistica: Bling ``logistica``; type ``LogisticasServicosLogisticaDTO``; obrigatório.
        transportador: Bling ``transportador``; type ``LogisticasServicosTransportadorDTO``; obrigatório."""

    id: int | None = Field(default=None, examples=["123445"])
    descricao: str = Field(..., examples=["CARTA REG AR CONV B1 MFD"])
    codigo: str = Field(..., examples=["ABC1234"])
    aliases: list[str]
    ativo: bool | None = Field(default=None, examples=[True])
    frete_item: float = Field(
        ...,
        validation_alias=AliasChoices("frete_item", "freteItem"),
        examples=[12.45],
        serialization_alias="freteItem",
    )
    estimativa_entrega: int = Field(
        ...,
        validation_alias=AliasChoices("estimativa_entrega", "estimativaEntrega"),
        examples=[2],
        serialization_alias="estimativaEntrega",
    )
    id_codigo_servico: str | None = Field(
        default=None,
        validation_alias=AliasChoices("id_codigo_servico", "idCodigoServico"),
        examples=[13112],
        serialization_alias="idCodigoServico",
    )
    logistica: LogisticasServicosLogisticaDTO
    transportador: LogisticasServicosTransportadorDTO


class LogisticasServicosDadosSaveRequestDTO(BlingModel):
    """OpenAPI schema ``LogisticasServicosDadosSaveRequestDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        descricao: Bling ``descricao``; type ``str``; obrigatório. Descrição do serviço da logística
        codigo: Bling ``codigo``; type ``str``; obrigatório. Código do serviço
        aliases: Bling ``aliases``; type ``list[str]``; obrigatório. Aliases do serviço
        ativo: Bling ``ativo``; type ``bool | None``; opcional. Define se está ativo ou não
        frete_item: Bling ``freteItem``; type ``float``; obrigatório. Valor do frete que será calculado para cada item do pedido
        estimativa_entrega: Bling ``estimativaEntrega``; type ``int``; obrigatório. Será o prazo, em dias úteis, de entrega da mercadoria para esse serviço.
        id_codigo_servico: Bling ``idCodigoServico``; type ``str | None``; opcional. Id do código do servico
        transportador: Bling ``transportador``; type ``LogisticasServicosTransportadorDTO | None``; opcional."""

    descricao: str = Field(..., examples=["CARTA REG AR CONV B1 MFD"])
    codigo: str = Field(..., examples=["ABC1234"])
    aliases: list[str]
    ativo: bool | None = Field(default=None, examples=[True])
    frete_item: float = Field(
        ...,
        validation_alias=AliasChoices("frete_item", "freteItem"),
        examples=[12.45],
        serialization_alias="freteItem",
    )
    estimativa_entrega: int = Field(
        ...,
        validation_alias=AliasChoices("estimativa_entrega", "estimativaEntrega"),
        examples=[2],
        serialization_alias="estimativaEntrega",
    )
    id_codigo_servico: str | None = Field(
        default=None,
        validation_alias=AliasChoices("id_codigo_servico", "idCodigoServico"),
        examples=[13112],
        serialization_alias="idCodigoServico",
    )
    transportador: LogisticasServicosTransportadorDTO | None = None


class LogisticasServicosGetResponse200(BlingModel):
    """OpenAPI schema ``LogisticasServicosGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[LogisticasServicosDadosDTO] | None``; opcional."""

    data: list[LogisticasServicosDadosDTO] | None = None


class LogisticasServicosIdLogisticaServicoGetResponse200(BlingModel):
    """OpenAPI schema ``LogisticasServicosIdLogisticaServicoGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``LogisticasServicosDadosDTO | None``; opcional."""

    data: LogisticasServicosDadosDTO | None = None


class LogisticasServicosDadosCreateRequestDTO(BlingModel):
    """OpenAPI schema ``LogisticasServicosDadosCreateRequestDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        logistica: Bling ``logistica``; type ``LogisticasServicosLogisticaDTO``; obrigatório.
        servicos: Bling ``servicos``; type ``list[LogisticasServicosDadosSaveRequestDTO]``; obrigatório. Serviços da logística"""

    logistica: LogisticasServicosLogisticaDTO
    servicos: list[LogisticasServicosDadosSaveRequestDTO]


__all__ = [
    "LogisticasServicosDadosCreateRequestDTO",
    "LogisticasServicosDadosDTO",
    "LogisticasServicosDadosSaveDTO",
    "LogisticasServicosDadosSaveRequestDTO",
    "LogisticasServicosDadosSituationDTO",
    "LogisticasServicosGetResponse200",
    "LogisticasServicosIdLogisticaServicoGetResponse200",
    "LogisticasServicosIdLogisticaServicoPutResponse200",
    "LogisticasServicosLogisticaDTO",
    "LogisticasServicosPostResponse201",
    "LogisticasServicosTransportadorDTO",
]
