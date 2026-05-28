# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``logisticas``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .logisticas_remessas import LogisticasRemessasDadosDTO


class LogisticasDadosPutDTO(BlingModel):
    """OpenAPI schema ``LogisticasDadosPutDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        descricao: Bling ``descricao``; type ``str``; obrigatório. Descrição da logística
        situacao: Bling ``situacao``; type ``str``; obrigatório. Situação da logística<br> `H` Habilitado<br> `D` Desabilitado"""

    descricao: str = Field(..., examples=["Correios Cliente"])
    situacao: str = Field(..., examples=["H"])


class LogisticasIntegracaoDTO(BlingModel):
    """OpenAPI schema ``LogisticasIntegracaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class LogisticasLogisticaDTO(BlingModel):
    """OpenAPI schema ``LogisticasLogisticaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class LogisticasServicoBaseDTO(BlingModel):
    """OpenAPI schema ``LogisticasServicoBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. ID do serviço da logística"""

    id: int = Field(..., examples=[6423813145])


class LogisticasTransportadorDTO(BlingModel):
    """OpenAPI schema ``LogisticasTransportadorDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class LogisticasLogisticaRemessaDTO(BlingModel):
    """OpenAPI schema ``LogisticasLogisticaRemessaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class LogisticasRemessaRemessaDTO(BlingModel):
    """OpenAPI schema ``LogisticasRemessaRemessaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class LogisticasPostResponse201(BlingModel):
    """OpenAPI schema ``LogisticasPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``LogisticasLogisticaDTO | None``; opcional."""

    data: LogisticasLogisticaDTO | None = None


class LogisticasIdLogisticaRemessasGetResponse200(BlingModel):
    """OpenAPI schema ``LogisticasIdLogisticaRemessasGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[LogisticasRemessasDadosDTO] | None``; opcional."""

    data: list[LogisticasRemessasDadosDTO] | None = None


class LogisticasDadosBaseDTO(BlingModel):
    """OpenAPI schema ``LogisticasDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. ID da logística
        descricao: Bling ``descricao``; type ``str``; obrigatório. Descrição da logística
        tipo_integracao: Bling ``tipoIntegracao``; type ``str``; obrigatório. Tipo da logística
        integracao_nativa: Bling ``integracaoNativa``; type ``bool``; obrigatório.
        situacao: Bling ``situacao``; type ``str``; obrigatório. Situação da logística<br> `H` Habilitado<br> `D` Desabilitado
        integracao: Bling ``integracao``; type ``LogisticasIntegracaoDTO``; obrigatório.
        servicos: Bling ``servicos``; type ``list[LogisticasServicoBaseDTO]``; obrigatório. ID dos serviços vinculados a logística"""

    id: int = Field(..., examples=[6423813145])
    descricao: str = Field(..., examples=["Correios Cliente"])
    tipo_integracao: str = Field(
        ...,
        validation_alias=AliasChoices("tipo_integracao", "tipoIntegracao"),
        examples=["Correios"],
        serialization_alias="tipoIntegracao",
    )
    integracao_nativa: bool = Field(
        ...,
        validation_alias=AliasChoices("integracao_nativa", "integracaoNativa"),
        examples=[False],
        serialization_alias="integracaoNativa",
    )
    situacao: str = Field(..., examples=["H"])
    integracao: LogisticasIntegracaoDTO
    servicos: list[LogisticasServicoBaseDTO]


class LogisticasServicoDTO(LogisticasServicoBaseDTO):
    """OpenAPI schema ``LogisticasServicoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: LogisticasServicoBaseDTO.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. ID do serviço da logística
        descricao: Bling ``descricao``; type ``str``; obrigatório. Descrição do serviço da logística
        frete_item: Bling ``freteItem``; type ``float``; obrigatório. Valor do frete que será calculado para cada item do pedido
        estimativa_entrega: Bling ``estimativaEntrega``; type ``int``; obrigatório. Será o prazo, em dias úteis, de entrega da mercadoria para esse serviço.
        codigo: Bling ``codigo``; type ``str``; obrigatório. Código do serviço
        logistica: Bling ``logistica``; type ``LogisticasLogisticaDTO``; obrigatório.
        transportador: Bling ``transportador``; type ``LogisticasTransportadorDTO``; obrigatório.
        aliases: Bling ``aliases``; type ``list[str]``; obrigatório. Aliases do serviço
        ativo: Bling ``ativo``; type ``bool``; obrigatório. Indica se o serviço está ativo"""

    descricao: str = Field(..., examples=["CARTA REG AR CONV B1 MFD"])
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
    codigo: str = Field(..., examples=["ABC1234"])
    logistica: LogisticasLogisticaDTO
    transportador: LogisticasTransportadorDTO
    aliases: list[str]
    ativo: bool = Field(..., examples=[True])


class LogisticaServicoPostDTO(BlingModel):
    """OpenAPI schema ``LogisticaServicoPostDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        descricao: Bling ``descricao``; type ``str``; obrigatório. Descrição do serviço da logística
        frete_item: Bling ``freteItem``; type ``float | None``; opcional. Valor do frete que será calculado para cada item do pedido
        estimativa_entrega: Bling ``estimativaEntrega``; type ``int | None``; opcional. Será o prazo, em dias úteis, de entrega da mercadoria para esse serviço.
        codigo: Bling ``codigo``; type ``str | None``; opcional. Código do serviço
        transportador: Bling ``transportador``; type ``LogisticasTransportadorDTO | None``; opcional.
        aliases: Bling ``aliases``; type ``list[str] | None``; opcional. Aliases do serviço
        ativo: Bling ``ativo``; type ``bool | None``; opcional. Indica se o serviço está ativo"""

    descricao: str = Field(..., examples=["CARTA REG AR CONV B1 MFD"])
    frete_item: float | None = Field(
        default=None,
        validation_alias=AliasChoices("frete_item", "freteItem"),
        examples=[12.45],
        serialization_alias="freteItem",
    )
    estimativa_entrega: int | None = Field(
        default=None,
        validation_alias=AliasChoices("estimativa_entrega", "estimativaEntrega"),
        examples=[2],
        serialization_alias="estimativaEntrega",
    )
    codigo: str | None = Field(default=None, examples=["ABC1234"])
    transportador: LogisticasTransportadorDTO | None = None
    aliases: list[str] | None = None
    ativo: bool | None = Field(default=None, examples=[True])


class LogisticasGetResponse200(BlingModel):
    """OpenAPI schema ``LogisticasGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[LogisticasDadosBaseDTO] | None``; opcional."""

    data: list[LogisticasDadosBaseDTO] | None = None


class LogisticasDadosPostDTO(BlingModel):
    """OpenAPI schema ``LogisticasDadosPostDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        descricao: Bling ``descricao``; type ``str``; obrigatório. Descrição da logística
        situacao: Bling ``situacao``; type ``str``; obrigatório. Situação da logística<br> `H` Habilitado<br> `D` Desabilitado
        servicos: Bling ``servicos``; type ``list[LogisticaServicoPostDTO] | None``; opcional. Serviços vinculados à logística"""

    descricao: str = Field(..., examples=["Correios Cliente"])
    situacao: str = Field(..., examples=["H"])
    servicos: list[LogisticaServicoPostDTO] | None = None


class LogisticasDadosDTO(LogisticasDadosBaseDTO):
    """OpenAPI schema ``LogisticasDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: LogisticasDadosBaseDTO.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. ID da logística
        descricao: Bling ``descricao``; type ``str``; obrigatório. Descrição da logística
        tipo_integracao: Bling ``tipoIntegracao``; type ``str``; obrigatório. Tipo da logística
        integracao_nativa: Bling ``integracaoNativa``; type ``bool``; obrigatório.
        situacao: Bling ``situacao``; type ``str``; obrigatório. Situação da logística<br> `H` Habilitado<br> `D` Desabilitado
        integracao: Bling ``integracao``; type ``LogisticasIntegracaoDTO``; obrigatório.
        servicos: Bling ``servicos``; type ``list[LogisticasServicoDTO] | None``; opcional. Serviços vinculados à logística"""

    servicos: list[LogisticasServicoDTO] | None = None


class LogisticasIdLogisticaGetResponse200(BlingModel):
    """OpenAPI schema ``LogisticasIdLogisticaGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``LogisticasDadosDTO | None``; opcional."""

    data: LogisticasDadosDTO | None = None


__all__ = [
    "LogisticaServicoPostDTO",
    "LogisticasDadosBaseDTO",
    "LogisticasDadosDTO",
    "LogisticasDadosPostDTO",
    "LogisticasDadosPutDTO",
    "LogisticasGetResponse200",
    "LogisticasIdLogisticaGetResponse200",
    "LogisticasIdLogisticaRemessasGetResponse200",
    "LogisticasIntegracaoDTO",
    "LogisticasLogisticaDTO",
    "LogisticasLogisticaRemessaDTO",
    "LogisticasPostResponse201",
    "LogisticasRemessaRemessaDTO",
    "LogisticasServicoBaseDTO",
    "LogisticasServicoDTO",
    "LogisticasTransportadorDTO",
]
