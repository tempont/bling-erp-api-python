"""Modelos para Notificações."""

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class NotificacoesEnquadramentosFiscaisDTO(BlingModel):
    """Enquadramentos fiscais da notificação."""

    tamanho_empresa: list[str] | None = Field(default=None, alias="tamanhoEmpresa")
    id_municipio: list[int] | None = Field(default=None, alias="idMunicipio")
    uf: list[str] | None = Field(default=None, alias="uf")
    crt: list[int] | None = Field(default=None, alias="crt")


class NotificacoesDadosDTO(BlingModel):
    """Dados completos de uma notificação (Ulids + DadosBase combinados)."""

    id: str | None = Field(default=None, alias="id")
    emitente: str = Field(..., alias="emitente")
    modulo: str = Field(..., alias="modulo")
    titulo: str = Field(..., alias="titulo")
    descricao: str = Field(..., alias="descricao")
    fonte: str | None = Field(default=None, alias="fonte")
    link_ajuda: str | None = Field(default=None, alias="linkAjuda")
    acao: str | None = Field(default=None, alias="acao")
    data_criacao: str | None = Field(default=None, alias="dataCriacao")
    data_envio: str = Field(..., alias="dataEnvio")
    data_vigencia: str | None = Field(default=None, alias="dataVigencia")
    data_acao: str | None = Field(default=None, alias="dataAcao")
    data_leitura: str | None = Field(default=None, alias="dataLeitura")
    data_alerta: str | None = Field(default=None, alias="dataAlerta")
    data_perigo: str | None = Field(default=None, alias="dataPerigo")
    enquadramentos: list[NotificacoesEnquadramentosFiscaisDTO] | None = Field(
        default=None, alias="enquadramentos"
    )


class NotificacoesQuantidadeDTO(BlingModel):
    """Quantidade de notificações."""

    quantidade: int | None = Field(default=None, alias="quantidade")
