# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``ordens_producao``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import BasePostResponse


class OrdensProducaoContatoDTO(BlingModel):
    """OpenAPI schema ``OrdensProducaoContatoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        nome: Bling ``nome``; type ``str | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    nome: str | None = Field(default=None, examples=["João da Silva"])


class OrdensProducaoDepositoDTO(BlingModel):
    """OpenAPI schema ``OrdensProducaoDepositoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id_destino: Bling ``idDestino``; type ``int | None``; opcional.
        id_origem: Bling ``idOrigem``; type ``int | None``; opcional."""

    id_destino: int | None = Field(default=None, alias="idDestino", examples=[12345678])
    id_origem: int | None = Field(default=None, alias="idOrigem", examples=[12345678])


class OrdensProducaoProdutoDTO(BlingModel):
    """OpenAPI schema ``OrdensProducaoProdutoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        nome: Bling ``nome``; type ``str | None``; opcional.
        codigo: Bling ``codigo``; type ``str | None``; opcional."""

    id: int = Field(..., examples=[12345678])
    nome: str | None = Field(default=None, examples=["Nome do produto"])
    codigo: str | None = Field(default=None, examples=["Código do produto"])


class OrdensProducaoSituacaoDTO(BlingModel):
    """OpenAPI schema ``OrdensProducaoSituacaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        valor: Bling ``valor``; type ``int``; obrigatório.
        nome: Bling ``nome``; type ``str``; obrigatório."""

    id: int = Field(..., examples=[12345678])
    valor: int = Field(..., examples=[1])
    nome: str = Field(..., examples=["Em aberto"])


class OrdensProducaoSituacaoDadosDTO(BlingModel):
    """OpenAPI schema ``OrdensProducaoSituacaoDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id_situacao: Bling ``idSituacao``; type ``int``; obrigatório.
        quantidade: Bling ``quantidade``; type ``float | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        considerar_perdas: Bling ``considerarPerdas``; type ``bool | None``; opcional. Se deve considerar perdas na finalização da ordem de produção. (Válido apenas para finalização"""

    id_situacao: int = Field(..., alias="idSituacao", examples=[12345678])
    quantidade: float | None = Field(default=None, examples=[1])
    observacoes: str | None = Field(default=None, examples=["Observação"])
    considerar_perdas: bool | None = Field(default=None, alias="considerarPerdas", examples=[True])


class OrdensProducaoVendaDTO(BlingModel):
    """OpenAPI schema ``OrdensProducaoVendaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        numero: Bling ``numero``; type ``int | None``; opcional.
        contato: Bling ``contato``; type ``OrdensProducaoContatoDTO | None``; opcional."""

    numero: int | None = Field(default=None, examples=[12345678])
    contato: OrdensProducaoContatoDTO | None = None


class OrdensProducaoPostResponse201(BlingModel):
    """OpenAPI schema ``OrdensProducaoPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``BasePostResponse | None``; opcional."""

    data: BasePostResponse | None = None


class OrdensProducaoDadosBaseDTO(BlingModel):
    """OpenAPI schema ``OrdensProducaoDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        data_previsao_inicio: Bling ``dataPrevisaoInicio``; type ``date | None``; opcional.
        data_previsao_final: Bling ``dataPrevisaoFinal``; type ``date | None``; opcional.
        data_inicio: Bling ``dataInicio``; type ``date | None``; opcional.
        data_fim: Bling ``dataFim``; type ``date | None``; opcional.
        numero: Bling ``numero``; type ``int``; obrigatório.
        responsavel: Bling ``responsavel``; type ``str | None``; opcional.
        deposito: Bling ``deposito``; type ``OrdensProducaoDepositoDTO``; obrigatório.
        situacao: Bling ``situacao``; type ``OrdensProducaoSituacaoDTO``; obrigatório."""

    id: int = Field(..., examples=[12345678])
    data_previsao_inicio: date | None = Field(
        default=None, alias="dataPrevisaoInicio", examples=["2021-01-01"]
    )
    data_previsao_final: date | None = Field(
        default=None, alias="dataPrevisaoFinal", examples=["2021-01-01"]
    )
    data_inicio: date | None = Field(default=None, alias="dataInicio", examples=["2021-01-01"])
    data_fim: date | None = Field(default=None, alias="dataFim", examples=["2021-01-01"])
    numero: int = Field(..., examples=[12345678])
    responsavel: str | None = Field(default=None, examples=["Responsável pela ordem de produção"])
    deposito: OrdensProducaoDepositoDTO
    situacao: OrdensProducaoSituacaoDTO


class OrdensProducaoItemDTO(BlingModel):
    """OpenAPI schema ``OrdensProducaoItemDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        produto: Bling ``produto``; type ``OrdensProducaoProdutoDTO | None``; opcional.
        quantidade: Bling ``quantidade``; type ``float | None``; opcional."""

    produto: OrdensProducaoProdutoDTO | None = None
    quantidade: float | None = Field(default=None, examples=[1])


class OrdensProducaoGetResponse200(BlingModel):
    """OpenAPI schema ``OrdensProducaoGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[OrdensProducaoDadosBaseDTO] | None``; opcional."""

    data: list[OrdensProducaoDadosBaseDTO] | None = None


class OrdensProducaoDadosDTO(BlingModel):
    """OpenAPI schema ``OrdensProducaoDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        vendas: Bling ``vendas``; type ``list[OrdensProducaoVendaDTO] | None``; opcional.
        itens: Bling ``itens``; type ``list[OrdensProducaoItemDTO] | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional."""

    vendas: list[OrdensProducaoVendaDTO] | None = None
    itens: list[OrdensProducaoItemDTO] | None = None
    observacoes: str | None = Field(default=None, examples=["Observações"])


class OrdensProducaoDadosGeradosPorDemandaDTO(BlingModel):
    """OpenAPI schema ``OrdensProducaoDadosGeradosPorDemandaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        itens: Bling ``itens``; type ``list[OrdensProducaoItemDTO] | None``; opcional.
        deposito: Bling ``deposito``; type ``OrdensProducaoDepositoDTO | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    itens: list[OrdensProducaoItemDTO] | None = None
    deposito: OrdensProducaoDepositoDTO | None = None


class OrdensProducaoDadosPostDTO(BlingModel):
    """OpenAPI schema ``OrdensProducaoDadosPostDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        itens: Bling ``itens``; type ``list[OrdensProducaoItemDTO] | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional."""

    itens: list[OrdensProducaoItemDTO] | None = None
    observacoes: str | None = Field(default=None, examples=["Observações"])


class OrdensProducaoPostRequest(OrdensProducaoDadosBaseDTO, OrdensProducaoDadosPostDTO):
    """OpenAPI schema ``OrdensProducaoPostRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: OrdensProducaoDadosBaseDTO, OrdensProducaoDadosPostDTO.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        data_previsao_inicio: Bling ``dataPrevisaoInicio``; type ``date | None``; opcional.
        data_previsao_final: Bling ``dataPrevisaoFinal``; type ``date | None``; opcional.
        data_inicio: Bling ``dataInicio``; type ``date | None``; opcional.
        data_fim: Bling ``dataFim``; type ``date | None``; opcional.
        numero: Bling ``numero``; type ``int``; obrigatório.
        responsavel: Bling ``responsavel``; type ``str | None``; opcional.
        deposito: Bling ``deposito``; type ``OrdensProducaoDepositoDTO``; obrigatório.
        situacao: Bling ``situacao``; type ``OrdensProducaoSituacaoDTO``; obrigatório.
        itens: Bling ``itens``; type ``list[OrdensProducaoItemDTO] | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional."""

    pass


class OrdensProducaoIdOrdemProducaoGetResponse200(
    OrdensProducaoDadosBaseDTO, OrdensProducaoDadosDTO
):
    """OpenAPI schema ``OrdensProducaoIdOrdemProducaoGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: OrdensProducaoDadosBaseDTO, OrdensProducaoDadosDTO.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        data_previsao_inicio: Bling ``dataPrevisaoInicio``; type ``date | None``; opcional.
        data_previsao_final: Bling ``dataPrevisaoFinal``; type ``date | None``; opcional.
        data_inicio: Bling ``dataInicio``; type ``date | None``; opcional.
        data_fim: Bling ``dataFim``; type ``date | None``; opcional.
        numero: Bling ``numero``; type ``int``; obrigatório.
        responsavel: Bling ``responsavel``; type ``str | None``; opcional.
        deposito: Bling ``deposito``; type ``OrdensProducaoDepositoDTO``; obrigatório.
        situacao: Bling ``situacao``; type ``OrdensProducaoSituacaoDTO``; obrigatório.
        vendas: Bling ``vendas``; type ``list[OrdensProducaoVendaDTO] | None``; opcional.
        itens: Bling ``itens``; type ``list[OrdensProducaoItemDTO] | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional."""

    pass


class OrdensProducaoIdOrdemProducaoPutRequest(
    OrdensProducaoDadosBaseDTO, OrdensProducaoDadosPostDTO
):
    """OpenAPI schema ``OrdensProducaoIdOrdemProducaoPutRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: OrdensProducaoDadosBaseDTO, OrdensProducaoDadosPostDTO.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        data_previsao_inicio: Bling ``dataPrevisaoInicio``; type ``date | None``; opcional.
        data_previsao_final: Bling ``dataPrevisaoFinal``; type ``date | None``; opcional.
        data_inicio: Bling ``dataInicio``; type ``date | None``; opcional.
        data_fim: Bling ``dataFim``; type ``date | None``; opcional.
        numero: Bling ``numero``; type ``int``; obrigatório.
        responsavel: Bling ``responsavel``; type ``str | None``; opcional.
        deposito: Bling ``deposito``; type ``OrdensProducaoDepositoDTO``; obrigatório.
        situacao: Bling ``situacao``; type ``OrdensProducaoSituacaoDTO``; obrigatório.
        itens: Bling ``itens``; type ``list[OrdensProducaoItemDTO] | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional."""

    pass


class OrdensProducaoGerarSobDemandaPostResponse201(BlingModel):
    """OpenAPI schema ``OrdensProducaoGerarSobDemandaPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[OrdensProducaoDadosGeradosPorDemandaDTO] | None``; opcional."""

    data: list[OrdensProducaoDadosGeradosPorDemandaDTO] | None = None


__all__ = [
    "OrdensProducaoContatoDTO",
    "OrdensProducaoDadosBaseDTO",
    "OrdensProducaoDadosDTO",
    "OrdensProducaoDadosGeradosPorDemandaDTO",
    "OrdensProducaoDadosPostDTO",
    "OrdensProducaoDepositoDTO",
    "OrdensProducaoGerarSobDemandaPostResponse201",
    "OrdensProducaoGetResponse200",
    "OrdensProducaoIdOrdemProducaoGetResponse200",
    "OrdensProducaoIdOrdemProducaoPutRequest",
    "OrdensProducaoItemDTO",
    "OrdensProducaoPostRequest",
    "OrdensProducaoPostResponse201",
    "OrdensProducaoProdutoDTO",
    "OrdensProducaoSituacaoDTO",
    "OrdensProducaoSituacaoDadosDTO",
    "OrdensProducaoVendaDTO",
]
