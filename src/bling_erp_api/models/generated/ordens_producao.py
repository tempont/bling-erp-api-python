"""Modelos para Ordens de Produção."""

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class OrdensProducaoDepositoDTO(BlingModel):
    """Depósito da ordem de produção."""

    id_destino: int | None = Field(default=None, alias="idDestino")
    id_origem: int | None = Field(default=None, alias="idOrigem")


class OrdensProducaoSituacaoDTO(BlingModel):
    """Situação da ordem de produção."""

    id: int = Field(..., alias="id")
    valor: int | None = Field(default=None, alias="valor")
    nome: str | None = Field(default=None, alias="nome")


class OrdensProducaoProdutoDTO(BlingModel):
    """Produto referenciado na ordem de produção."""

    id: int = Field(..., alias="id")
    nome: str | None = Field(default=None, alias="nome")
    codigo: str | None = Field(default=None, alias="codigo")


class OrdensProducaoItemDTO(BlingModel):
    """Item da ordem de produção."""

    produto: OrdensProducaoProdutoDTO | None = Field(default=None, alias="produto")
    quantidade: float | None = Field(default=None, alias="quantidade")


class OrdensProducaoContatoDTO(BlingModel):
    """Contato vinculado à venda."""

    id: int | None = Field(default=None, alias="id")
    nome: str | None = Field(default=None, alias="nome")


class OrdensProducaoVendaDTO(BlingModel):
    """Venda vinculada à ordem de produção."""

    numero: int | None = Field(default=None, alias="numero")
    contato: OrdensProducaoContatoDTO | None = Field(default=None, alias="contato")


class OrdensProducaoSituacaoDadosDTO(BlingModel):
    """Dados para alteração de situação."""

    id_situacao: int = Field(..., alias="idSituacao")
    quantidade: float | None = Field(default=None, alias="quantidade")
    observacoes: str | None = Field(default=None, alias="observacoes")
    considerar_perdas: bool | None = Field(default=None, alias="considerarPerdas")


class OrdensProducaoCreateRequestDTO(BlingModel):
    """Corpo para criar/alterar ordem de produção (allOf Base + Post)."""

    id: int | None = Field(default=None, alias="id")
    data_previsao_inicio: str | None = Field(default=None, alias="dataPrevisaoInicio")
    data_previsao_final: str | None = Field(default=None, alias="dataPrevisaoFinal")
    data_inicio: str | None = Field(default=None, alias="dataInicio")
    data_fim: str | None = Field(default=None, alias="dataFim")
    numero: int | None = Field(default=None, alias="numero")
    responsavel: str | None = Field(default=None, alias="responsavel")
    deposito: OrdensProducaoDepositoDTO | None = Field(default=None, alias="deposito")
    situacao: OrdensProducaoSituacaoDTO | None = Field(default=None, alias="situacao")
    itens: list[OrdensProducaoItemDTO] | None = Field(default=None, alias="itens")
    observacoes: str | None = Field(default=None, alias="observacoes")


class OrdensProducaoDetailResponseDTO(BlingModel):
    """Resposta detalhada de ordem de produção (allOf Base + Dados)."""

    id: int | None = Field(default=None, alias="id")
    data_previsao_inicio: str | None = Field(default=None, alias="dataPrevisaoInicio")
    data_previsao_final: str | None = Field(default=None, alias="dataPrevisaoFinal")
    data_inicio: str | None = Field(default=None, alias="dataInicio")
    data_fim: str | None = Field(default=None, alias="dataFim")
    numero: int | None = Field(default=None, alias="numero")
    responsavel: str | None = Field(default=None, alias="responsavel")
    deposito: OrdensProducaoDepositoDTO | None = Field(default=None, alias="deposito")
    situacao: OrdensProducaoSituacaoDTO | None = Field(default=None, alias="situacao")
    vendas: list[OrdensProducaoVendaDTO] | None = Field(default=None, alias="vendas")
    itens: list[OrdensProducaoItemDTO] | None = Field(default=None, alias="itens")
    observacoes: str | None = Field(default=None, alias="observacoes")


class OrdensProducaoDadosGeradosPorDemandaDTO(BlingModel):
    """Resposta do gerar-sob-demanda."""

    id: int | None = Field(default=None, alias="id")
    itens: list[OrdensProducaoItemDTO] | None = Field(default=None, alias="itens")
    deposito: OrdensProducaoDepositoDTO | None = Field(default=None, alias="deposito")


class BasePostResponse(BlingModel):
    """Resposta de criação de recurso."""

    id: int = Field(..., alias="id")


class OrdensProducaoDadosBaseDTO(BlingModel):
    """Dados base da ordem de produção (para listagem)."""

    id: int | None = Field(default=None, alias="id")
    data_previsao_inicio: str | None = Field(default=None, alias="dataPrevisaoInicio")
    data_previsao_final: str | None = Field(default=None, alias="dataPrevisaoFinal")
    data_inicio: str | None = Field(default=None, alias="dataInicio")
    data_fim: str | None = Field(default=None, alias="dataFim")
    numero: int | None = Field(default=None, alias="numero")
    responsavel: str | None = Field(default=None, alias="responsavel")
    deposito: OrdensProducaoDepositoDTO | None = Field(default=None, alias="deposito")
    situacao: OrdensProducaoSituacaoDTO | None = Field(default=None, alias="situacao")
