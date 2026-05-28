# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``situacoes``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import BasePostResponse, Data33, Datum6, Datum7


class SituacoesAcaoDTO(BlingModel):
    """OpenAPI schema ``SituacoesAcaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        nome: Bling ``nome``; type ``str``; obrigatório. Nome da ação.
        descricao: Bling ``descricao``; type ``str``; obrigatório. Descrição da ação."""

    id: int = Field(..., examples=[6])
    nome: str = Field(..., examples=["estornarEstoque"])
    descricao: str = Field(..., examples=["Estornar estoque"])


class SituacoesModuloBaseDTO(BlingModel):
    """OpenAPI schema ``SituacoesModuloBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class SituacoesModuloDTO(BlingModel):
    """OpenAPI schema ``SituacoesModuloDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        nome: Bling ``nome``; type ``str``; obrigatório. Nome do módulo.
        descricao: Bling ``descricao``; type ``str``; obrigatório. Descrição do módulo.
        criar_situacoes: Bling ``criarSituacoes``; type ``bool``; obrigatório. Identifica a possibilidade de criar situações."""

    nome: str = Field(..., examples=["Vendas"])
    descricao: str = Field(..., examples=["Pedidos de Venda"])
    criar_situacoes: bool = Field(..., alias="criarSituacoes", examples=[False])


class SituacoesDTO(BlingModel):
    """OpenAPI schema ``SituacoesDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        nome: Bling ``nome``; type ``str``; obrigatório. Utilizado no GET."""

    id: int = Field(..., examples=[9])
    nome: str = Field(..., examples=["Em aberto"])


class SituacoesDadosDTO(BlingModel):
    """OpenAPI schema ``SituacoesDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id_herdado: Bling ``idHerdado``; type ``int | None``; opcional. ID da situação de referência.
        cor: Bling ``cor``; type ``str | None``; opcional. Código hexadecimal."""

    id_herdado: int | None = Field(default=None, alias="idHerdado", examples=[0])
    cor: str | None = Field(default=None, examples=["#E9DC40"])


class SituacoesTransicaoDTO(BlingModel):
    """OpenAPI schema ``SituacoesTransicaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        ativo: Bling ``ativo``; type ``bool | None``; opcional. Identifica se a transição está ativa.
        acoes: Bling ``acoes``; type ``list[int] | None``; opcional.
        modulo: Bling ``modulo``; type ``SituacoesModuloBaseDTO | None``; opcional.
        situacao_origem: Bling ``situacaoOrigem``; type ``SituacoesDTO``; obrigatório.
        situacao_destino: Bling ``situacaoDestino``; type ``SituacoesDTO``; obrigatório."""

    id: int = Field(..., examples=[9])
    ativo: bool | None = Field(default=None, examples=[True])
    acoes: list[int] | None = Field(default=None, examples=[[12, 15]])
    modulo: SituacoesModuloBaseDTO | None = None
    situacao_origem: SituacoesDTO = Field(..., alias="situacaoOrigem")
    situacao_destino: SituacoesDTO = Field(..., alias="situacaoDestino")


class SituacoesModulosGetResponse200(BlingModel):
    """OpenAPI schema ``SituacoesModulosGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[Datum6] | None``; opcional."""

    data: list[Datum6] | None = None


class SituacoesModulosIdModuloSistemaGetResponse200(BlingModel):
    """OpenAPI schema ``SituacoesModulosIdModuloSistemaGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[Datum7] | None``; opcional."""

    data: list[Datum7] | None = None


class SituacoesModulosIdModuloSistemaAcoesGetResponse200(BlingModel):
    """OpenAPI schema ``SituacoesModulosIdModuloSistemaAcoesGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[SituacoesAcaoDTO] | None``; opcional."""

    data: list[SituacoesAcaoDTO] | None = None


class SituacoesModulosIdModuloSistemaTransicoesGetResponse200(BlingModel):
    """OpenAPI schema ``SituacoesModulosIdModuloSistemaTransicoesGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[SituacoesTransicaoDTO] | None``; opcional."""

    data: list[SituacoesTransicaoDTO] | None = None


class SituacoesIdSituacaoGetResponse200(BlingModel):
    """OpenAPI schema ``SituacoesIdSituacaoGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data33 | None``; opcional."""

    data: Data33 | None = None


class SituacoesIdSituacaoPutRequest(SituacoesDadosDTO):
    """OpenAPI schema ``SituacoesIdSituacaoPutRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: SituacoesDadosDTO.

    Fields:
        id_herdado: Bling ``idHerdado``; type ``int | None``; opcional. ID da situação de referência.
        cor: Bling ``cor``; type ``str | None``; opcional. Código hexadecimal.
        id_modulo_sistema: Bling ``idModuloSistema``; type ``int | None``; opcional.
        nome: Bling ``nome``; type ``str | None``; opcional."""

    id_modulo_sistema: int | None = Field(
        default=None, alias="idModuloSistema", examples=[6423808065]
    )
    nome: str | None = Field(default=None, examples=["Finalizado"])


class SituacoesIdSituacaoPutResponse200(BlingModel):
    """OpenAPI schema ``SituacoesIdSituacaoPutResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``BasePostResponse | None``; opcional."""

    data: BasePostResponse | None = None


class SituacoesPostRequest(SituacoesDadosDTO):
    """OpenAPI schema ``SituacoesPostRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: SituacoesDadosDTO.

    Fields:
        id_herdado: Bling ``idHerdado``; type ``int | None``; opcional. ID da situação de referência.
        cor: Bling ``cor``; type ``str | None``; opcional. Código hexadecimal.
        id_modulo_sistema: Bling ``idModuloSistema``; type ``int | None``; opcional.
        nome: Bling ``nome``; type ``str | None``; opcional."""

    id_modulo_sistema: int | None = Field(
        default=None, alias="idModuloSistema", examples=[6423808065]
    )
    nome: str | None = Field(default=None, examples=["Finalizado"])


class SituacoesPostResponse201(BlingModel):
    """OpenAPI schema ``SituacoesPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``BasePostResponse | None``; opcional."""

    data: BasePostResponse | None = None


class SituacoesTransicoesIdTransicaoGetResponse200(BlingModel):
    """OpenAPI schema ``SituacoesTransicoesIdTransicaoGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``SituacoesTransicaoDTO | None``; opcional."""

    data: SituacoesTransicaoDTO | None = None


class SituacoesTransicoesIdTransicaoPutRequest(SituacoesTransicaoDTO):
    """OpenAPI schema ``SituacoesTransicoesIdTransicaoPutRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: SituacoesTransicaoDTO.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        ativo: Bling ``ativo``; type ``bool | None``; opcional. Identifica se a transição está ativa.
        acoes: Bling ``acoes``; type ``list[int] | None``; opcional.
        modulo: Bling ``modulo``; type ``SituacoesModuloBaseDTO | None``; opcional.
        situacao_origem: Bling ``situacaoOrigem``; type ``SituacoesDTO``; obrigatório.
        situacao_destino: Bling ``situacaoDestino``; type ``SituacoesDTO``; obrigatório."""

    pass


class SituacoesTransicoesIdTransicaoPutResponse200(BlingModel):
    """OpenAPI schema ``SituacoesTransicoesIdTransicaoPutResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``BasePostResponse | None``; opcional."""

    data: BasePostResponse | None = None


class SituacoesTransicoesPostRequest(SituacoesTransicaoDTO):
    """OpenAPI schema ``SituacoesTransicoesPostRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: SituacoesTransicaoDTO.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        ativo: Bling ``ativo``; type ``bool | None``; opcional. Identifica se a transição está ativa.
        acoes: Bling ``acoes``; type ``list[int] | None``; opcional.
        modulo: Bling ``modulo``; type ``SituacoesModuloBaseDTO | None``; opcional.
        situacao_origem: Bling ``situacaoOrigem``; type ``SituacoesDTO``; obrigatório.
        situacao_destino: Bling ``situacaoDestino``; type ``SituacoesDTO``; obrigatório."""

    pass


class SituacoesTransicoesPostResponse201(BlingModel):
    """OpenAPI schema ``SituacoesTransicoesPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``BasePostResponse | None``; opcional."""

    data: BasePostResponse | None = None


__all__ = [
    "SituacoesAcaoDTO",
    "SituacoesDTO",
    "SituacoesDadosDTO",
    "SituacoesIdSituacaoGetResponse200",
    "SituacoesIdSituacaoPutRequest",
    "SituacoesIdSituacaoPutResponse200",
    "SituacoesModuloBaseDTO",
    "SituacoesModuloDTO",
    "SituacoesModulosGetResponse200",
    "SituacoesModulosIdModuloSistemaAcoesGetResponse200",
    "SituacoesModulosIdModuloSistemaGetResponse200",
    "SituacoesModulosIdModuloSistemaTransicoesGetResponse200",
    "SituacoesPostRequest",
    "SituacoesPostResponse201",
    "SituacoesTransicaoDTO",
    "SituacoesTransicoesIdTransicaoGetResponse200",
    "SituacoesTransicoesIdTransicaoPutRequest",
    "SituacoesTransicoesIdTransicaoPutResponse200",
    "SituacoesTransicoesPostRequest",
    "SituacoesTransicoesPostResponse201",
]
