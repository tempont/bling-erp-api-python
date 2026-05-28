# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``logisticas_objetos``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel


class LogisticasObjetosDimensaoDTO(BlingModel):
    """OpenAPI schema ``LogisticasObjetosDimensaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        peso: Bling ``peso``; type ``float``; obrigatório.
        altura: Bling ``altura``; type ``float``; obrigatório.
        largura: Bling ``largura``; type ``float``; obrigatório.
        comprimento: Bling ``comprimento``; type ``float``; obrigatório.
        diametro: Bling ``diametro``; type ``float``; obrigatório."""

    peso: float = Field(..., examples=[1.5])
    altura: float = Field(..., examples=[1.5])
    largura: float = Field(..., examples=[1.5])
    comprimento: float = Field(..., examples=[1.5])
    diametro: float = Field(..., examples=[1.5])


class LogisticasObjetosEmbalagemDTO(BlingModel):
    """OpenAPI schema ``LogisticasObjetosEmbalagemDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. ID do produto utilizado como embalagem"""

    id: int = Field(..., examples=[12345678])


class LogisticasObjetosNotaFiscalDTO(BlingModel):
    """OpenAPI schema ``LogisticasObjetosNotaFiscalDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class LogisticasObjetosObjetoDTO(BlingModel):
    """OpenAPI schema ``LogisticasObjetosObjetoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class LogisticasObjetosPedidoVendaDTO(BlingModel):
    """OpenAPI schema ``LogisticasObjetosPedidoVendaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class LogisticasObjetosRastreamentoDTO(BlingModel):
    """OpenAPI schema ``LogisticasObjetosRastreamentoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        codigo: Bling ``codigo``; type ``str``; obrigatório.
        descricao: Bling ``descricao``; type ``str``; obrigatório.
        situacao: Bling ``situacao``; type ``int``; obrigatório. `0` Postado <br> `1` Em andamento <br> `2` Não entregue <br> `3` Entregue <br> `4` Aguardando retirada <br> `5` Etiqueta comprada <br> `6` Vinculado <br> `7` Atrasado <br> `8` Não...
        origem: Bling ``origem``; type ``str``; obrigatório. Cidade e estado de origem
        destino: Bling ``destino``; type ``str``; obrigatório. Cidade e estado de destino
        ultima_alteracao: Bling ``ultimaAlteracao``; type ``AwareDatetime``; obrigatório. Data e hora em que ocorreu a atualização de rastreio.
        url: Bling ``url``; type ``str``; obrigatório. URL de rastreamento"""

    codigo: str = Field(..., examples=["EC272330554BR"])
    descricao: str = Field(..., examples=["Criado"])
    situacao: int = Field(..., examples=["8"])
    origem: str = Field(..., examples=["São Paulo, SP"])
    destino: str = Field(..., examples=["São Paulo, SP"])
    ultima_alteracao: AwareDatetime = Field(
        ...,
        validation_alias=AliasChoices("ultima_alteracao", "ultimaAlteracao"),
        examples=["2020-11-11 16:40:33"],
        serialization_alias="ultimaAlteracao",
    )
    url: str = Field(..., examples=["https://www.rastreamento.exemplo.com.br/EC272330554BR"])


class LogisticasObjetosServicoDTO(BlingModel):
    """OpenAPI schema ``LogisticasObjetosServicoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class LogisticasObjetosIdObjetoPutResponse200(BlingModel):
    """OpenAPI schema ``LogisticasObjetosIdObjetoPutResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``LogisticasObjetosObjetoDTO | None``; opcional."""

    data: LogisticasObjetosObjetoDTO | None = None


class LogisticasObjetosPostResponse201(BlingModel):
    """OpenAPI schema ``LogisticasObjetosPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``LogisticasObjetosObjetoDTO | None``; opcional."""

    data: LogisticasObjetosObjetoDTO | None = None


class LogisticasObjetosDadosDTO(BlingModel):
    """OpenAPI schema ``LogisticasObjetosDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        pedido_venda: Bling ``pedidoVenda``; type ``LogisticasObjetosPedidoVendaDTO``; obrigatório.
        nota_fiscal: Bling ``notaFiscal``; type ``LogisticasObjetosNotaFiscalDTO``; obrigatório.
        servico: Bling ``servico``; type ``LogisticasObjetosServicoDTO``; obrigatório.
        rastreamento: Bling ``rastreamento``; type ``LogisticasObjetosRastreamentoDTO | None``; opcional.
        dimensao: Bling ``dimensao``; type ``LogisticasObjetosDimensaoDTO``; obrigatório.
        embalagem: Bling ``embalagem``; type ``LogisticasObjetosEmbalagemDTO``; obrigatório.
        data_saida: Bling ``dataSaida``; type ``date``; obrigatório.
        prazo_entrega_previsto: Bling ``prazoEntregaPrevisto``; type ``int``; obrigatório.
        frete_previsto: Bling ``fretePrevisto``; type ``float``; obrigatório.
        valor_declarado: Bling ``valorDeclarado``; type ``float``; obrigatório.
        aviso_recebimento: Bling ``avisoRecebimento``; type ``bool``; obrigatório.
        mao_propria: Bling ``maoPropria``; type ``bool``; obrigatório."""

    pedido_venda: LogisticasObjetosPedidoVendaDTO = Field(
        ...,
        validation_alias=AliasChoices("pedido_venda", "pedidoVenda"),
        serialization_alias="pedidoVenda",
    )
    nota_fiscal: LogisticasObjetosNotaFiscalDTO = Field(
        ...,
        validation_alias=AliasChoices("nota_fiscal", "notaFiscal"),
        serialization_alias="notaFiscal",
    )
    servico: LogisticasObjetosServicoDTO
    rastreamento: LogisticasObjetosRastreamentoDTO | None = None
    dimensao: LogisticasObjetosDimensaoDTO
    embalagem: LogisticasObjetosEmbalagemDTO
    data_saida: date = Field(
        ...,
        validation_alias=AliasChoices("data_saida", "dataSaida"),
        examples=["2022-12-01"],
        serialization_alias="dataSaida",
    )
    prazo_entrega_previsto: int = Field(
        ...,
        validation_alias=AliasChoices("prazo_entrega_previsto", "prazoEntregaPrevisto"),
        examples=[15],
        serialization_alias="prazoEntregaPrevisto",
    )
    frete_previsto: float = Field(
        ...,
        validation_alias=AliasChoices("frete_previsto", "fretePrevisto"),
        examples=[59.9],
        serialization_alias="fretePrevisto",
    )
    valor_declarado: float = Field(
        ...,
        validation_alias=AliasChoices("valor_declarado", "valorDeclarado"),
        examples=[55.9],
        serialization_alias="valorDeclarado",
    )
    aviso_recebimento: bool = Field(
        ...,
        validation_alias=AliasChoices("aviso_recebimento", "avisoRecebimento"),
        examples=[False],
        serialization_alias="avisoRecebimento",
    )
    mao_propria: bool = Field(
        ...,
        validation_alias=AliasChoices("mao_propria", "maoPropria"),
        examples=[False],
        serialization_alias="maoPropria",
    )


class LogisticasObjetosUpdateRequestDTO(BlingModel):
    """OpenAPI schema ``LogisticasObjetosUpdateRequestDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        rastreamento: Bling ``rastreamento``; type ``LogisticasObjetosRastreamentoDTO | None``; opcional.
        dimensoes: Bling ``dimensoes``; type ``LogisticasObjetosDimensaoDTO | None``; opcional.
        embalagem: Bling ``embalagem``; type ``LogisticasObjetosEmbalagemDTO``; obrigatório.
        data_saida: Bling ``dataSaida``; type ``date``; obrigatório.
        prazo_entrega_previsto: Bling ``prazoEntregaPrevisto``; type ``int``; obrigatório.
        frete_previsto: Bling ``fretePrevisto``; type ``float``; obrigatório.
        valor_declarado: Bling ``valorDeclarado``; type ``float``; obrigatório.
        aviso_recebimento: Bling ``avisoRecebimento``; type ``bool``; obrigatório.
        mao_propria: Bling ``maoPropria``; type ``bool``; obrigatório."""

    rastreamento: LogisticasObjetosRastreamentoDTO | None = None
    dimensoes: LogisticasObjetosDimensaoDTO | None = None
    embalagem: LogisticasObjetosEmbalagemDTO
    data_saida: date = Field(
        ...,
        validation_alias=AliasChoices("data_saida", "dataSaida"),
        examples=["2022-12-01"],
        serialization_alias="dataSaida",
    )
    prazo_entrega_previsto: int = Field(
        ...,
        validation_alias=AliasChoices("prazo_entrega_previsto", "prazoEntregaPrevisto"),
        examples=[15],
        serialization_alias="prazoEntregaPrevisto",
    )
    frete_previsto: float = Field(
        ...,
        validation_alias=AliasChoices("frete_previsto", "fretePrevisto"),
        examples=[59.9],
        serialization_alias="fretePrevisto",
    )
    valor_declarado: float = Field(
        ...,
        validation_alias=AliasChoices("valor_declarado", "valorDeclarado"),
        examples=[55.9],
        serialization_alias="valorDeclarado",
    )
    aviso_recebimento: bool = Field(
        ...,
        validation_alias=AliasChoices("aviso_recebimento", "avisoRecebimento"),
        examples=[False],
        serialization_alias="avisoRecebimento",
    )
    mao_propria: bool = Field(
        ...,
        validation_alias=AliasChoices("mao_propria", "maoPropria"),
        examples=[False],
        serialization_alias="maoPropria",
    )


class LogisticasObjetosIdObjetoGetResponse200(BlingModel):
    """OpenAPI schema ``LogisticasObjetosIdObjetoGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``LogisticasObjetosDadosDTO | None``; opcional."""

    data: LogisticasObjetosDadosDTO | None = None


class LogisticasObjetosDadosCreateRequestDTO(LogisticasObjetosUpdateRequestDTO):
    """OpenAPI schema ``LogisticasObjetosDadosCreateRequestDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: LogisticasObjetosUpdateRequestDTO.

    Fields:
        rastreamento: Bling ``rastreamento``; type ``LogisticasObjetosRastreamentoDTO | None``; opcional.
        dimensoes: Bling ``dimensoes``; type ``LogisticasObjetosDimensaoDTO | None``; opcional.
        embalagem: Bling ``embalagem``; type ``LogisticasObjetosEmbalagemDTO``; obrigatório.
        data_saida: Bling ``dataSaida``; type ``date``; obrigatório.
        prazo_entrega_previsto: Bling ``prazoEntregaPrevisto``; type ``int``; obrigatório.
        frete_previsto: Bling ``fretePrevisto``; type ``float``; obrigatório.
        valor_declarado: Bling ``valorDeclarado``; type ``float``; obrigatório.
        aviso_recebimento: Bling ``avisoRecebimento``; type ``bool``; obrigatório.
        mao_propria: Bling ``maoPropria``; type ``bool``; obrigatório.
        pedido_venda: Bling ``pedidoVenda``; type ``LogisticasObjetosPedidoVendaDTO``; obrigatório.
        nota_fiscal: Bling ``notaFiscal``; type ``LogisticasObjetosNotaFiscalDTO``; obrigatório.
        servico: Bling ``servico``; type ``LogisticasObjetosServicoDTO``; obrigatório."""

    pedido_venda: LogisticasObjetosPedidoVendaDTO = Field(
        ...,
        validation_alias=AliasChoices("pedido_venda", "pedidoVenda"),
        serialization_alias="pedidoVenda",
    )
    nota_fiscal: LogisticasObjetosNotaFiscalDTO = Field(
        ...,
        validation_alias=AliasChoices("nota_fiscal", "notaFiscal"),
        serialization_alias="notaFiscal",
    )
    servico: LogisticasObjetosServicoDTO


__all__ = [
    "LogisticasObjetosDadosCreateRequestDTO",
    "LogisticasObjetosDadosDTO",
    "LogisticasObjetosDimensaoDTO",
    "LogisticasObjetosEmbalagemDTO",
    "LogisticasObjetosIdObjetoGetResponse200",
    "LogisticasObjetosIdObjetoPutResponse200",
    "LogisticasObjetosNotaFiscalDTO",
    "LogisticasObjetosObjetoDTO",
    "LogisticasObjetosPedidoVendaDTO",
    "LogisticasObjetosPostResponse201",
    "LogisticasObjetosRastreamentoDTO",
    "LogisticasObjetosServicoDTO",
    "LogisticasObjetosUpdateRequestDTO",
]
