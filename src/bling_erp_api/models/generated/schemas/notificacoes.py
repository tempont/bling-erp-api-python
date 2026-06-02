# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``notificacoes``. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.models.fields import BlingDate
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import Datum4


class NotificacoesEnquadramentosFiscaisDTO(BlingModel):
    """OpenAPI schema ``NotificacoesEnquadramentosFiscaisDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        tamanho_empresa: Bling ``tamanhoEmpresa``; type ``list[str] | None``; opcional. Perfil no qual a empresa se encaixa.
        id_municipio: Bling ``idMunicipio``; type ``list[int] | None``; opcional. Código do município da empresa.
        uf: Bling ``uf``; type ``list[str] | None``; opcional.
        crt: Bling ``crt``; type ``list[int] | None``; opcional. Código de Regime Tributário"""

    tamanho_empresa: list[str] | None = Field(
        default=None,
        validation_alias=AliasChoices("tamanho_empresa", "tamanhoEmpresa"),
        examples=[["micro", "pequena"]],
        serialization_alias="tamanhoEmpresa",
    )
    id_municipio: list[int] | None = Field(
        default=None,
        validation_alias=AliasChoices("id_municipio", "idMunicipio"),
        examples=[["2704104", "2704203"]],
        serialization_alias="idMunicipio",
    )
    uf: list[str] | None = Field(default=None, examples=[["SP", "RS"]])
    crt: list[int] | None = Field(default=None, examples=[[1]])


class NotificacoesQuantidadeDTO(BlingModel):
    """OpenAPI schema ``NotificacoesQuantidadeDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        quantidade: Bling ``quantidade``; type ``int | None``; opcional. Quantidade de notificações."""

    quantidade: int | None = Field(default=None, examples=["10"])


class NotificacoesUlidsDTO(BlingModel):
    """OpenAPI schema ``NotificacoesUlidsDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``str | None``; opcional. ULID da notificação."""

    id: str | None = Field(default=None, examples=["01ARZ3NDEKTSV4RRFFQ69G5FAV"])


class NotificacoesQuantidadeGetResponse200(BlingModel):
    """OpenAPI schema ``NotificacoesQuantidadeGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``NotificacoesQuantidadeDTO | None``; opcional."""

    data: NotificacoesQuantidadeDTO | None = None


class NotificacoesDadosBaseDTO(BlingModel):
    """OpenAPI schema ``NotificacoesDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        emitente: Bling ``emitente``; type ``str``; obrigatório. Nome do usuário que criou a notificação.
        modulo: Bling ``modulo``; type ``str``; obrigatório.
        descricao: Bling ``descricao``; type ``str``; obrigatório. Mensagem do corpo da notificação.
        titulo: Bling ``titulo``; type ``str``; obrigatório. Título no cabeçalho da notificação.
        fonte: Bling ``fonte``; type ``str | None``; opcional. Nome do orgão ou entidade em que se baseia a informação.
        link_ajuda: Bling ``linkAjuda``; type ``str | None``; opcional. Link para direcionar o cliente à mais informações.
        acao: Bling ``acao``; type ``str | None``; opcional. Ação executada na notificação.
        data_criacao: Bling ``dataCriacao``; type ``BlingDate | None``; opcional. Data de criação da notificação.
        data_envio: Bling ``dataEnvio``; type ``str``; obrigatório. Data de publicação da notificação.
        data_vigencia: Bling ``dataVigencia``; type ``BlingDate | None``; opcional. Data em que uma possível alteração informada entrará em vigor.
        data_acao: Bling ``dataAcao``; type ``BlingDate | None``; opcional. Data em que a ação foi realizada pelo usuário.
        data_leitura: Bling ``dataLeitura``; type ``str | None``; opcional. Data em que o usuário leu a notificação.
        data_alerta: Bling ``dataAlerta``; type ``BlingDate | None``; opcional. Data em que a notificação ficará com a cor amarela para alertar usuário.
        data_perigo: Bling ``dataPerigo``; type ``BlingDate | None``; opcional. Data em que a notificação ficará com a cor vermelha para alertar usuário.
        enquadramentos: Bling ``enquadramentos``; type ``list[NotificacoesEnquadramentosFiscaisDTO] | None``; opcional."""

    emitente: str
    modulo: str = Field(..., examples=["FISCAL"])
    descricao: str
    titulo: str
    fonte: str | None = Field(default=None, examples=["SEFAZ"])
    link_ajuda: str | None = Field(
        default=None,
        validation_alias=AliasChoices("link_ajuda", "linkAjuda"),
        serialization_alias="linkAjuda",
    )
    acao: str | None = None
    data_criacao: BlingDate | None = Field(
        default=None,
        validation_alias=AliasChoices("data_criacao", "dataCriacao"),
        examples=["2023-01-12"],
        serialization_alias="dataCriacao",
    )
    data_envio: str = Field(
        ...,
        validation_alias=AliasChoices("data_envio", "dataEnvio"),
        examples=["2023-01-12 00:00:00"],
        serialization_alias="dataEnvio",
    )
    data_vigencia: BlingDate | None = Field(
        default=None,
        validation_alias=AliasChoices("data_vigencia", "dataVigencia"),
        examples=["2023-01-12"],
        serialization_alias="dataVigencia",
    )
    data_acao: BlingDate | None = Field(
        default=None,
        validation_alias=AliasChoices("data_acao", "dataAcao"),
        examples=["2023-01-12"],
        serialization_alias="dataAcao",
    )
    data_leitura: str | None = Field(
        default=None,
        validation_alias=AliasChoices("data_leitura", "dataLeitura"),
        examples=["2023-01-12 11:50:00"],
        serialization_alias="dataLeitura",
    )
    data_alerta: BlingDate | None = Field(
        default=None,
        validation_alias=AliasChoices("data_alerta", "dataAlerta"),
        examples=["2023-01-12"],
        serialization_alias="dataAlerta",
    )
    data_perigo: BlingDate | None = Field(
        default=None,
        validation_alias=AliasChoices("data_perigo", "dataPerigo"),
        examples=["2023-01-12"],
        serialization_alias="dataPerigo",
    )
    enquadramentos: list[NotificacoesEnquadramentosFiscaisDTO] | None = None


class NotificacoesGetResponse200(BlingModel):
    """OpenAPI schema ``NotificacoesGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[Datum4] | None``; opcional."""

    data: list[Datum4] | None = None


class NotificacoesIdNotificacaoConfirmarLeituraPostResponse200(BlingModel):
    """OpenAPI schema ``NotificacoesIdNotificacaoConfirmarLeituraPostResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[Datum4] | None``; opcional."""

    data: list[Datum4] | None = None


__all__ = [
    "NotificacoesDadosBaseDTO",
    "NotificacoesEnquadramentosFiscaisDTO",
    "NotificacoesGetResponse200",
    "NotificacoesIdNotificacaoConfirmarLeituraPostResponse200",
    "NotificacoesQuantidadeDTO",
    "NotificacoesQuantidadeGetResponse200",
    "NotificacoesUlidsDTO",
]
