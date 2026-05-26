"""Semi-generated NFS-e invoice models."""

from __future__ import annotations

from pydantic import Field

from bling_erp_api.models.base import BlingModel

# --- Sub-DTOs ---


class NotasServicosContatoEnderecoDTO(BlingModel):
    endereco: str | None = Field(default=None, alias="endereco")
    numero: str | None = Field(default=None, alias="numero")
    complemento: str | None = Field(default=None, alias="complemento")
    bairro: str | None = Field(default=None, alias="bairro")
    cep: str | None = Field(default=None, alias="cep")
    municipio: str | None = Field(default=None, alias="municipio")
    uf: str | None = Field(default=None, alias="uf")
    pais: str | None = Field(default=None, alias="pais")


class NotasServicosContatoBaseDTO(BlingModel):
    id: int | None = Field(default=None, alias="id")
    nome: str | None = Field(default=None, alias="nome")
    numero_documento: str | None = Field(default=None, alias="numeroDocumento")
    email: str | None = Field(default=None, alias="email")


class NotasServicosContatoDTO(NotasServicosContatoBaseDTO):
    """Extended contact for NFS-e POST (inherits base fields)."""

    ie: str | None = Field(default=None, alias="ie")
    telefone: str | None = Field(default=None, alias="telefone")
    im: str | None = Field(default=None, alias="im")  # municipal registration
    endereco: NotasServicosContatoEnderecoDTO | None = Field(default=None, alias="endereco")


class NotasServicosVendedorDTO(BlingModel):
    id: int | None = Field(default=None, alias="id")


class NotasServicosServicoDTO(BlingModel):
    codigo: str | None = Field(default=None, alias="codigo")
    descricao: str | None = Field(default=None, alias="descricao")
    valor: float | None = Field(default=None, alias="valor")


class NotasServicosParcelaFormaPagamentoDTO(BlingModel):
    id: int | None = Field(default=None, alias="id")


class NotasServicosParcelaDTO(BlingModel):
    data: str | None = Field(default=None, alias="data")
    valor: float | None = Field(default=None, alias="valor")
    observacoes: str | None = Field(default=None, alias="observacoes")
    forma_pagamento: NotasServicosParcelaFormaPagamentoDTO | None = Field(
        default=None, alias="formaPagamento"
    )


class NotasServicosTributacaoIbsCbsValoresDTO(BlingModel):
    codigo_situacao_tributaria: str | None = Field(default=None, alias="codigoSituacaoTributaria")
    classificacao_tributaria: str | None = Field(default=None, alias="classificacaoTributaria")
    codigo_credito_presumido: str | None = Field(default=None, alias="codigoCreditoPresumido")
    cst_regime_regular: str | None = Field(default=None, alias="cstRegimeRegular")
    classificacao_tributaria_regular: str | None = Field(
        default=None, alias="classificacaoTributariaRegular"
    )
    percentual_diferimento_estadual: float | None = Field(
        default=None, alias="percentualDiferimentoEstadual"
    )
    percentual_diferimento_municipal: float | None = Field(
        default=None, alias="percentualDiferimentoMunicipal"
    )
    percentual_diferimento_cbs: float | None = Field(default=None, alias="percentualDiferimentoCBS")


class NotasServicosTributacaoIbsCbsDTO(BlingModel):
    indicador_operacao: str | None = Field(default=None, alias="indicadorOperacao")
    tipo_operacao: str | None = Field(default=None, alias="tipoOperacao")
    tipo_ente_governamental: str | None = Field(default=None, alias="tipoEnteGovernamental")
    tributacao: NotasServicosTributacaoIbsCbsValoresDTO | None = Field(
        default=None, alias="tributacao"
    )


# --- Main DTOs for NFS-e ---


class NotasServicosDadosBaseDTO(BlingModel):
    """Base DTO for NFS-e GET list/single."""

    id: int | None = Field(default=None, alias="id")
    numero: str | None = Field(default=None, alias="numero")
    numero_rps: str | None = Field(default=None, alias="numeroRPS")
    serie: str | None = Field(default=None, alias="serie")
    situacao: int | None = Field(default=None, alias="situacao")
    data_emissao: str | None = Field(default=None, alias="dataEmissao")
    valor: float | None = Field(default=None, alias="valor")
    contato: NotasServicosContatoBaseDTO | None = Field(default=None, alias="contato")


class NotasServicosDadosBaseDTO_POST(BlingModel):  # noqa: N801
    """Base DTO for NFS-e POST requests (extends with full contact)."""

    numero: str | None = Field(default=None, alias="numero")
    numero_rps: str | None = Field(default=None, alias="numeroRPS")
    serie: str | None = Field(default=None, alias="serie")
    contato: NotasServicosContatoDTO | None = Field(default=None, alias="contato")


class NotasServicosDadosDTO(BlingModel):
    """Additional GET response fields for NFS-e."""

    link: str | None = Field(default=None, alias="link")
    codigo_verificacao: str | None = Field(default=None, alias="codigoVerificacao")


class NotasServicosDadosDTO_POST(BlingModel):  # noqa: N801
    """Additional POST data for NFS-e creation."""

    data: str | None = Field(default=None, alias="data")
    base_calculo: float | None = Field(default=None, alias="baseCalculo")
    reter_iss: bool | None = Field(default=None, alias="reterISS")
    desconto: float | None = Field(default=None, alias="desconto")
    vendedor: NotasServicosVendedorDTO | None = Field(default=None, alias="vendedor")
    servicos: list[NotasServicosServicoDTO] = Field(default_factory=list, alias="servicos")
    parcelas: list[NotasServicosParcelaDTO] = Field(default_factory=list, alias="parcelas")
    tributacao_ibs_cbs: NotasServicosTributacaoIbsCbsDTO | None = Field(
        default=None, alias="tributacaoIbsCbs"
    )


class NotasServicosResponsePOSTPUT(BlingModel):
    """POST/PUT response data for NFS-e."""

    id: int | None = Field(default=None, alias="id")
    numero_rps: str | None = Field(default=None, alias="numeroRPS")
    serie: str | None = Field(default=None, alias="serie")


class NotasServicosCancelamentoDTO(BlingModel):
    """NFS-e cancellation request body."""

    codigo_motivo: int | None = Field(default=None, alias="codigoMotivo")
    justificativa: str | None = Field(default=None, alias="justificativa")


class NotasServicosListResponse(BlingModel):
    """NFS-e list response wrapper."""

    data: list[NotasServicosDadosBaseDTO] = Field(default_factory=list, alias="data")


# --- Configurações NFS-e (simplified but covering key fields) ---


class ConfiguracaoBasicaNotaServicoDTO(BlingModel):
    emissor_padrao: int | None = Field(default=None, alias="emissorPadrao")
    natureza_operacao: int | None = Field(default=None, alias="naturezaOperacao")


class ConfiguracaoTributoNotaServicoDTO(BlingModel):
    """A single tax configuration item."""


class ConfiguracaoISSNotaServicoDTO(BlingModel):
    zerar: bool | None = Field(default=None, alias="zerar")
    reter: bool | None = Field(default=None, alias="reter")
    descontar: bool | None = Field(default=None, alias="descontar")
    tributos: list[ConfiguracaoTributoNotaServicoDTO] = Field(
        default_factory=list, alias="tributos"
    )


class ConfiguracaoNumeracaoRPSNotaServicoDTO(BlingModel):
    cnpj_emitente: str | None = Field(default=None, alias="cnpjEmitente")
    id: int | None = Field(default=None, alias="id")
    numero: str | None = Field(default=None, alias="numero")
    serie: str | None = Field(default=None, alias="serie")


class ConfiguracaoControleNotaServicoDTO(BlingModel):
    numeracao_rps: ConfiguracaoNumeracaoRPSNotaServicoDTO | None = Field(
        default=None, alias="numeracaoRPS"
    )


class ConfiguracaoImpostoNotaServicoDTO(BlingModel):
    bloquear_retencao_pessoa_fisica: bool | None = Field(
        default=None, alias="bloquearRetencaoPessoaFisica"
    )


class ConfiguracaoEnvioEmailNotaServicoDTO(BlingModel):
    enviar_boleto_rps: bool | None = Field(default=None, alias="enviarBoletoRPS")
    remetente: str | None = Field(default=None, alias="remetente")
    assunto: str | None = Field(default=None, alias="assunto")
    mensagem: str | None = Field(default=None, alias="mensagem")
    padrao: str | None = Field(default=None, alias="padrao")


class ConfiguracaoAdicionalNotaServicoDTO(BlingModel):
    cfps: str | None = Field(default=None, alias="CFPS")
    cfop: str | None = Field(default=None, alias="CFOP")
    aedf: str | None = Field(default=None, alias="AEDF")
    proximo_numero_lote: int | None = Field(default=None, alias="proximoNumeroLote")
    observacao_impressa_nota: str | None = Field(default=None, alias="observacaoImpressaNota")
    descricao_complementar: str | None = Field(default=None, alias="descricaoComplementar")
    tipo_emissao: str | None = Field(default=None, alias="tipoEmissao")
    campo_numero_doc_contas: str | None = Field(default=None, alias="campoNumeroDocContas")
    incentivador_fiscal: str | None = Field(default=None, alias="incentivadorFiscal")
    alterar_situacao: str | None = Field(default=None, alias="alterarSituacao")
    incluir_parcelas: bool | None = Field(default=None, alias="incluirParcelas")
    considerar_data_parcela: bool | None = Field(default=None, alias="considerarDataParcela")
    considerar_data_ordem_servico: bool | None = Field(
        default=None, alias="considerarDataOrdemServico"
    )
    cadastro_prefeitura: str | None = Field(default=None, alias="cadastroPrefeitura")


class ConfiguracaoNotaServicoDadosBaseDTO(BlingModel):
    """NFS-e configuration settings request/response."""

    basicas: ConfiguracaoBasicaNotaServicoDTO | None = Field(default=None, alias="basicas")
    iss: ConfiguracaoISSNotaServicoDTO | None = Field(default=None, alias="ISS")
    controle: ConfiguracaoControleNotaServicoDTO | None = Field(default=None, alias="controle")
    impostos: ConfiguracaoImpostoNotaServicoDTO | None = Field(default=None, alias="impostos")
    envio_email: ConfiguracaoEnvioEmailNotaServicoDTO | None = Field(
        default=None, alias="envioEmail"
    )
    adicionais: ConfiguracaoAdicionalNotaServicoDTO | None = Field(default=None, alias="adicionais")
