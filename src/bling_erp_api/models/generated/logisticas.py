"""Pydantic models for Bling Logísticas endpoints."""

from __future__ import annotations

from pydantic import Field

from bling_erp_api.models.base import BlingModel


# --- Shared ---
class LogisticasLogisticaDTO(BlingModel):
    id: int = Field(...)


class LogisticasTransportadorDTO(BlingModel):
    id: int = Field(...)


class LogisticasIntegracaoDTO(BlingModel):
    id: int = Field(...)


class LogisticasServicoBaseDTO(BlingModel):
    id: int = Field(...)


# --- Main ---
class LogisticasServicoPostDTO(BlingModel):
    descricao: str = Field(...)
    frete_item: float | None = Field(default=None, alias="freteItem")
    estimativa_entrega: int | None = Field(default=None, alias="estimativaEntrega")
    codigo: str | None = Field(default=None)
    transportador: LogisticasTransportadorDTO | None = Field(default=None)
    aliases: list[str] | None = Field(default=None)
    ativo: bool | None = Field(default=None)


class LogisticasServicoDTO(BlingModel):
    id: int = Field(...)
    descricao: str = Field(...)
    frete_item: float = Field(..., alias="freteItem")
    estimativa_entrega: int = Field(..., alias="estimativaEntrega")
    codigo: str = Field(...)
    logistica: LogisticasLogisticaDTO = Field(...)
    transportador: LogisticasTransportadorDTO = Field(...)
    aliases: list[str] = Field(...)
    ativo: bool = Field(...)


class LogisticasDadosBaseDTO(BlingModel):
    id: int = Field(...)
    descricao: str = Field(...)
    tipo_integracao: str = Field(..., alias="tipoIntegracao")
    integracao_nativa: bool = Field(..., alias="integracaoNativa")
    situacao: str = Field(...)
    integracao: LogisticasIntegracaoDTO = Field(...)
    servicos: list[LogisticasServicoBaseDTO] = Field(...)


class LogisticasDadosDTO(BlingModel):
    """Full logistics data (allOf)."""

    id: int | None = Field(default=None)
    descricao: str | None = Field(default=None)
    tipo_integracao: str | None = Field(default=None, alias="tipoIntegracao")
    integracao_nativa: bool | None = Field(default=None, alias="integracaoNativa")
    situacao: str | None = Field(default=None)
    integracao: LogisticasIntegracaoDTO | None = Field(default=None)
    servicos: list[LogisticasServicoDTO] | None = Field(default=None)


class LogisticasDadosPostDTO(BlingModel):
    descricao: str = Field(...)
    situacao: str = Field(...)
    servicos: list[LogisticasServicoPostDTO] | None = Field(default=None)


class LogisticasDadosPutDTO(BlingModel):
    descricao: str = Field(...)
    situacao: str = Field(...)


# --- Serviços ---
class LogisticasServicosLogisticaDTO(BlingModel):
    id: int = Field(...)


class LogisticasServicosTransportadorDTO(BlingModel):
    id: int = Field(...)


class LogisticasServicosDadosSaveRequestDTO(BlingModel):
    descricao: str = Field(...)
    codigo: str = Field(...)
    aliases: list[str] = Field(...)
    ativo: bool | None = Field(default=None)
    frete_item: float = Field(..., alias="freteItem")
    estimativa_entrega: int = Field(..., alias="estimativaEntrega")
    id_codigo_servico: str | None = Field(default=None, alias="idCodigoServico")
    transportador: LogisticasServicosTransportadorDTO | None = Field(default=None)


class LogisticasServicosDadosCreateRequestDTO(BlingModel):
    logistica: LogisticasServicosLogisticaDTO = Field(...)
    servicos: list[LogisticasServicosDadosSaveRequestDTO] = Field(...)


class LogisticasServicosDadosDTO(BlingModel):
    id: int | None = Field(default=None)
    descricao: str = Field(...)
    codigo: str = Field(...)
    aliases: list[str] = Field(...)
    ativo: bool | None = Field(default=None)
    frete_item: float = Field(..., alias="freteItem")
    estimativa_entrega: int = Field(..., alias="estimativaEntrega")
    id_codigo_servico: str | None = Field(default=None, alias="idCodigoServico")
    logistica: LogisticasServicosLogisticaDTO = Field(...)
    transportador: LogisticasServicosTransportadorDTO = Field(...)


class LogisticasServicosDadosSaveDTO(BlingModel):
    id: int | None = Field(default=None)


class LogisticasServicosDadosSituationDTO(BlingModel):
    ativo: bool = Field(...)


# --- Etiquetas ---
class LogisticasEtiquetasDadosResponseDTO(BlingModel):
    id: int = Field(...)
    link: str = Field(...)
    observacao: str = Field(...)


# --- Objetos ---
class LogisticasObjetosPedidoVendaDTO(BlingModel):
    id: int = Field(...)


class LogisticasObjetosNotaFiscalDTO(BlingModel):
    id: int = Field(...)


class LogisticasObjetosServicoDTO(BlingModel):
    id: int = Field(...)


class LogisticasObjetosDimensaoDTO(BlingModel):
    peso: float = Field(...)
    altura: float = Field(...)
    largura: float = Field(...)
    comprimento: float = Field(...)
    diametro: float = Field(...)


class LogisticasObjetosEmbalagemDTO(BlingModel):
    id: int = Field(...)


class LogisticasObjetosRastreamentoDTO(BlingModel):
    codigo: str = Field(...)
    descricao: str = Field(...)
    situacao: int = Field(...)
    origem: str = Field(...)
    destino: str = Field(...)
    ultima_alteracao: str = Field(..., alias="ultimaAlteracao")
    url: str = Field(...)


class LogisticasObjetosUpdateRequestDTO(BlingModel):
    rastreamento: LogisticasObjetosRastreamentoDTO | None = Field(default=None)
    dimensoes: LogisticasObjetosDimensaoDTO = Field(...)
    embalagem: LogisticasObjetosEmbalagemDTO = Field(...)
    data_saida: str = Field(..., alias="dataSaida")
    prazo_entrega_previsto: int = Field(..., alias="prazoEntregaPrevisto")
    frete_previsto: float = Field(..., alias="fretePrevisto")
    valor_declarado: float = Field(..., alias="valorDeclarado")
    aviso_recebimento: bool = Field(..., alias="avisoRecebimento")
    mao_propria: bool = Field(..., alias="maoPropria")


class LogisticasObjetosDadosCreateRequestDTO(BlingModel):
    pedido_venda: LogisticasObjetosPedidoVendaDTO = Field(..., alias="pedidoVenda")
    nota_fiscal: LogisticasObjetosNotaFiscalDTO = Field(..., alias="notaFiscal")
    servico: LogisticasObjetosServicoDTO = Field(...)
    rastreamento: LogisticasObjetosRastreamentoDTO | None = Field(default=None)
    dimensoes: LogisticasObjetosDimensaoDTO = Field(...)
    embalagem: LogisticasObjetosEmbalagemDTO = Field(...)
    data_saida: str = Field(..., alias="dataSaida")
    prazo_entrega_previsto: int = Field(..., alias="prazoEntregaPrevisto")
    frete_previsto: float = Field(..., alias="fretePrevisto")
    valor_declarado: float = Field(..., alias="valorDeclarado")
    aviso_recebimento: bool = Field(..., alias="avisoRecebimento")
    mao_propria: bool = Field(..., alias="maoPropria")


class LogisticasObjetosDadosDTO(BlingModel):
    pedido_venda: LogisticasObjetosPedidoVendaDTO | None = Field(default=None, alias="pedidoVenda")
    nota_fiscal: LogisticasObjetosNotaFiscalDTO | None = Field(default=None, alias="notaFiscal")
    servico: LogisticasObjetosServicoDTO | None = Field(default=None)
    rastreamento: LogisticasObjetosRastreamentoDTO | None = Field(default=None)
    dimensao: LogisticasObjetosDimensaoDTO | None = Field(default=None)
    embalagem: LogisticasObjetosEmbalagemDTO | None = Field(default=None)
    data_saida: str | None = Field(default=None, alias="dataSaida")
    prazo_entrega_previsto: int | None = Field(default=None, alias="prazoEntregaPrevisto")
    frete_previsto: float | None = Field(default=None, alias="fretePrevisto")
    valor_declarado: float | None = Field(default=None, alias="valorDeclarado")
    aviso_recebimento: bool | None = Field(default=None, alias="avisoRecebimento")
    mao_propria: bool | None = Field(default=None, alias="maoPropria")


class LogisticasObjetosObjetoDTO(BlingModel):
    id: int = Field(...)


# --- Remessas ---
class LogisticasRemessasDadosBaseDTO(BlingModel):
    id: int = Field(...)


class LogisticasRemessasDadosDTO(BlingModel):
    id: int | None = Field(default=None)


class LogisticasRemessasDadosPostDTO(BlingModel):
    id: int = Field(...)


class LogisticasRemessasDadosBaseDTOCommon(BlingModel):
    id: int = Field(...)


class LogisticasRemessaRemessaDTO(BlingModel):
    id: int = Field(...)
