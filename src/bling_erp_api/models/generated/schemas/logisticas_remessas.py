# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``logisticas_remessas``. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.models.fields import BlingDate
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .logisticas import LogisticasLogisticaRemessaDTO, LogisticasRemessaRemessaDTO


class LogisticasRemessasDadosBaseDTOCommon(BlingModel):
    """OpenAPI schema ``LogisticasRemessasDadosBaseDTOCommon``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        numero_plp: Bling ``numeroPlp``; type ``str``; obrigatório.
        situacao: Bling ``situacao``; type ``int``; obrigatório. `-3` A ser corrigida <br> `-2` Em processamento <br> `-1` Cancelado <br> `0` Em aberto <br> `1` Emitido <br> `2` Pronto para envio <br> `3` Despachado <br> `4` Pronto para envio <...
        descricao: Bling ``descricao``; type ``str``; obrigatório.
        data_criacao: Bling ``dataCriacao``; type ``str``; obrigatório."""

    id: int = Field(..., examples=[12345678])
    numero_plp: str = Field(
        ...,
        validation_alias=AliasChoices("numero_plp", "numeroPlp"),
        examples=["749fdc73"],
        serialization_alias="numeroPlp",
    )
    situacao: int
    descricao: str = Field(..., examples=["Remessa_18092023"])
    data_criacao: str = Field(
        ...,
        validation_alias=AliasChoices("data_criacao", "dataCriacao"),
        examples=["2023-09-18"],
        serialization_alias="dataCriacao",
    )


class LogisticasRemessasDadosDTO(LogisticasRemessasDadosBaseDTOCommon):
    """OpenAPI schema ``LogisticasRemessasDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: LogisticasRemessasDadosBaseDTOCommon.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        numero_plp: Bling ``numeroPlp``; type ``str``; obrigatório.
        situacao: Bling ``situacao``; type ``int``; obrigatório. `-3` A ser corrigida <br> `-2` Em processamento <br> `-1` Cancelado <br> `0` Em aberto <br> `1` Emitido <br> `2` Pronto para envio <br> `3` Despachado <br> `4` Pronto para envio <...
        descricao: Bling ``descricao``; type ``str``; obrigatório.
        data_criacao: Bling ``dataCriacao``; type ``str``; obrigatório.
        objetos: Bling ``objetos``; type ``list[int]``; obrigatório."""

    objetos: list[int]


class LogisticasRemessasDimensaoDTO(BlingModel):
    """OpenAPI schema ``LogisticasRemessasDimensaoDTO``.

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


class LogisticasRemessasEmbalagemDTO(BlingModel):
    """OpenAPI schema ``LogisticasRemessasEmbalagemDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. ID do produto utilizado como embalagem"""

    id: int = Field(..., examples=[12345678])


class LogisticasRemessasNotaFiscalDTO(BlingModel):
    """OpenAPI schema ``LogisticasRemessasNotaFiscalDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class LogisticasRemessasPedidoVendaDTO(BlingModel):
    """OpenAPI schema ``LogisticasRemessasPedidoVendaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class LogisticasRemessasRastreamentoDTO(BlingModel):
    """OpenAPI schema ``LogisticasRemessasRastreamentoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        codigo: Bling ``codigo``; type ``str``; obrigatório.
        descricao: Bling ``descricao``; type ``str``; obrigatório.
        situacao: Bling ``situacao``; type ``int``; obrigatório. `0` Postado <br> `1` Em andamento <br> `2` Não entregue <br> `3` Entregue <br> `4` Aguardando retirada <br> `5` Em aberto <br> `6` Vinculado <br> `7` Atrasado <br> `8` Não postado...
        origem: Bling ``origem``; type ``str``; obrigatório. Cidade e estado de origem
        destino: Bling ``destino``; type ``str``; obrigatório. Cidade e estado de destino
        ultima_alteracao: Bling ``ultimaAlteracao``; type ``AwareDatetime``; obrigatório. Data e hora em que ocorreu a atualização de rastreio.
        url: Bling ``url``; type ``str``; obrigatório. URL de rastreamento"""

    codigo: str = Field(..., examples=["EC272330554BR"])
    descricao: str = Field(..., examples=["Criado"])
    situacao: int = Field(..., examples=[1])
    origem: str = Field(..., examples=["São Paulo, SP"])
    destino: str = Field(..., examples=["São Paulo, SP"])
    ultima_alteracao: AwareDatetime = Field(
        ...,
        validation_alias=AliasChoices("ultima_alteracao", "ultimaAlteracao"),
        examples=["2020-11-11 16:40:33"],
        serialization_alias="ultimaAlteracao",
    )
    url: str = Field(..., examples=["https://www.rastreamento.exemplo.com.br/EC272330554BR"])


class LogisticasRemessasServicoDTO(BlingModel):
    """OpenAPI schema ``LogisticasRemessasServicoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        nome: Bling ``nome``; type ``str``; obrigatório.
        codigo: Bling ``codigo``; type ``str``; obrigatório."""

    id: int = Field(..., examples=[12345678])
    nome: str = Field(..., examples=["SEDEX 10 A VISTA"])
    codigo: str = Field(..., examples=["04790"])


class LogisticasRemessasIdRemessaPutResponse200(BlingModel):
    """OpenAPI schema ``LogisticasRemessasIdRemessaPutResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``LogisticasRemessaRemessaDTO | None``; opcional."""

    data: LogisticasRemessaRemessaDTO | None = None


class LogisticasRemessasPostResponse201(BlingModel):
    """OpenAPI schema ``LogisticasRemessasPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``LogisticasRemessaRemessaDTO | None``; opcional."""

    data: LogisticasRemessaRemessaDTO | None = None


class LogisticasRemessasDadosPostDTO(LogisticasRemessasDadosBaseDTOCommon):
    """OpenAPI schema ``LogisticasRemessasDadosPostDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: LogisticasRemessasDadosBaseDTOCommon.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        numero_plp: Bling ``numeroPlp``; type ``str``; obrigatório.
        situacao: Bling ``situacao``; type ``int``; obrigatório. `-3` A ser corrigida <br> `-2` Em processamento <br> `-1` Cancelado <br> `0` Em aberto <br> `1` Emitido <br> `2` Pronto para envio <br> `3` Despachado <br> `4` Pronto para envio <...
        descricao: Bling ``descricao``; type ``str``; obrigatório.
        data_criacao: Bling ``dataCriacao``; type ``str``; obrigatório.
        logistica: Bling ``logistica``; type ``LogisticasLogisticaRemessaDTO | None``; opcional.
        objetos: Bling ``objetos``; type ``list[str]``; obrigatório."""

    logistica: LogisticasLogisticaRemessaDTO | None = None
    objetos: list[str]


class LogisticasRemessasObjetosDTO(BlingModel):
    """OpenAPI schema ``LogisticasRemessasObjetosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        remessa: Bling ``remessa``; type ``LogisticasRemessaRemessaDTO | None``; opcional.
        pedido_venda: Bling ``pedidoVenda``; type ``LogisticasRemessasPedidoVendaDTO``; obrigatório.
        nota_fiscal: Bling ``notaFiscal``; type ``LogisticasRemessasNotaFiscalDTO``; obrigatório.
        servico: Bling ``servico``; type ``LogisticasRemessasServicoDTO``; obrigatório.
        rastreamento: Bling ``rastreamento``; type ``LogisticasRemessasRastreamentoDTO``; obrigatório.
        dimensao: Bling ``dimensao``; type ``LogisticasRemessasDimensaoDTO``; obrigatório.
        embalagem: Bling ``embalagem``; type ``LogisticasRemessasEmbalagemDTO``; obrigatório.
        data_saida: Bling ``dataSaida``; type ``BlingDate``; obrigatório.
        prazo_entrega_previsto: Bling ``prazoEntregaPrevisto``; type ``int``; obrigatório.
        frete_previsto: Bling ``fretePrevisto``; type ``float``; obrigatório.
        valor_declarado: Bling ``valorDeclarado``; type ``float``; obrigatório.
        aviso_recebimento: Bling ``avisoRecebimento``; type ``bool``; obrigatório.
        mao_propria: Bling ``maoPropria``; type ``bool``; obrigatório."""

    id: int = Field(..., examples=["1235456"])
    remessa: LogisticasRemessaRemessaDTO | None = None
    pedido_venda: LogisticasRemessasPedidoVendaDTO = Field(
        ...,
        validation_alias=AliasChoices("pedido_venda", "pedidoVenda"),
        serialization_alias="pedidoVenda",
    )
    nota_fiscal: LogisticasRemessasNotaFiscalDTO = Field(
        ...,
        validation_alias=AliasChoices("nota_fiscal", "notaFiscal"),
        serialization_alias="notaFiscal",
    )
    servico: LogisticasRemessasServicoDTO
    rastreamento: LogisticasRemessasRastreamentoDTO
    dimensao: LogisticasRemessasDimensaoDTO
    embalagem: LogisticasRemessasEmbalagemDTO
    data_saida: BlingDate = Field(
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


class LogisticasRemessasDadosBaseDTO(LogisticasRemessasDadosBaseDTOCommon):
    """OpenAPI schema ``LogisticasRemessasDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: LogisticasRemessasDadosBaseDTOCommon.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        numero_plp: Bling ``numeroPlp``; type ``str``; obrigatório.
        situacao: Bling ``situacao``; type ``int``; obrigatório. `-3` A ser corrigida <br> `-2` Em processamento <br> `-1` Cancelado <br> `0` Em aberto <br> `1` Emitido <br> `2` Pronto para envio <br> `3` Despachado <br> `4` Pronto para envio <...
        descricao: Bling ``descricao``; type ``str``; obrigatório.
        data_criacao: Bling ``dataCriacao``; type ``str``; obrigatório.
        logistica: Bling ``logistica``; type ``LogisticasLogisticaRemessaDTO``; obrigatório.
        objetos: Bling ``objetos``; type ``list[LogisticasRemessasObjetosDTO]``; obrigatório."""

    logistica: LogisticasLogisticaRemessaDTO
    objetos: list[LogisticasRemessasObjetosDTO]


class LogisticasRemessasIdRemessaGetResponse200(BlingModel):
    """OpenAPI schema ``LogisticasRemessasIdRemessaGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``LogisticasRemessasDadosBaseDTO | None``; opcional."""

    data: LogisticasRemessasDadosBaseDTO | None = None


__all__ = [
    "LogisticasRemessasDadosBaseDTO",
    "LogisticasRemessasDadosBaseDTOCommon",
    "LogisticasRemessasDadosDTO",
    "LogisticasRemessasDadosPostDTO",
    "LogisticasRemessasDimensaoDTO",
    "LogisticasRemessasEmbalagemDTO",
    "LogisticasRemessasIdRemessaGetResponse200",
    "LogisticasRemessasIdRemessaPutResponse200",
    "LogisticasRemessasNotaFiscalDTO",
    "LogisticasRemessasObjetosDTO",
    "LogisticasRemessasPedidoVendaDTO",
    "LogisticasRemessasPostResponse201",
    "LogisticasRemessasRastreamentoDTO",
    "LogisticasRemessasServicoDTO",
]
