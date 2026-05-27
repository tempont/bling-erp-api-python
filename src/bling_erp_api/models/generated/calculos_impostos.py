"""Modelos para cálculos de impostos (Naturezas de Operações)."""

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class CalculosImpostosRegraOperacaoDTO(BlingModel):
    """Regra de operação de imposto."""

    id: int = Field(..., alias="id")


class CalculosImpostosDadosBaseDTO(BlingModel):
    """DTO base para dados de cálculos de impostos."""

    regra_operacao: CalculosImpostosRegraOperacaoDTO | None = Field(
        default=None, alias="regraOperacao"
    )
    tributacao: int | None = Field(default=None, alias="tributacao")
    cst: str | None = Field(default=None, alias="cst")
    aliquota: float | None = Field(default=None, alias="aliquota")
    base: float | None = Field(default=None, alias="base")
    valor_base_calculo: float | None = Field(default=None, alias="valorBaseCalculo")
    valor_imposto: float | None = Field(default=None, alias="valorImposto")
    observacoes: str | None = Field(default=None, alias="observacoes")
    informacoes_adicionais_fisco: str | None = Field(
        default=None, alias="informacoesAdicionaisFisco"
    )


class CalculosImpostosIcmsDTO(BlingModel):
    """Dados de cálculo do ICMS."""

    regra_operacao: CalculosImpostosRegraOperacaoDTO | None = Field(
        default=None, alias="regraOperacao"
    )
    tributacao: int | None = Field(default=None, alias="tributacao")
    cst: str | None = Field(default=None, alias="cst")
    aliquota: float | None = Field(default=None, alias="aliquota")
    base: float | None = Field(default=None, alias="base")
    valor_base_calculo: float | None = Field(default=None, alias="valorBaseCalculo")
    valor_imposto: float | None = Field(default=None, alias="valorImposto")
    observacoes: str | None = Field(default=None, alias="observacoes")
    informacoes_adicionais_fisco: str | None = Field(
        default=None, alias="informacoesAdicionaisFisco"
    )
    porcentagem_fcp_difal: float | None = Field(default=None, alias="porcentagemFcpDifal")
    valor_fcp_difal: float | None = Field(default=None, alias="valorFcpDifal")
    valor_fcp_efetivo: float | None = Field(default=None, alias="valorFcpEfetivo")
    porcentagem_fcp: float | None = Field(default=None, alias="porcentagemFcp")
    porcentagem_fcp_uf_destino: float | None = Field(default=None, alias="porcentagemFcpUfDestino")
    modalidade_base_calculo: float | None = Field(default=None, alias="modalidadeBaseCalculo")
    valor_pauta: float | None = Field(default=None, alias="valorPauta")
    aliquota_presumido: float | None = Field(default=None, alias="aliquotaPresumido")
    porcentagem_base_calculo_uf_destino: float | None = Field(
        default=None, alias="porcentagemBaseCalculoUfDestino"
    )
    porcentagem_icms_uf_destino: float | None = Field(
        default=None, alias="porcentagemIcmsUfDestino"
    )
    tipo_partilha: int | None = Field(default=None, alias="tipoPartilha")
    valor_icms_desonerado: float | None = Field(default=None, alias="valorIcmsDesonerado")
    motivo_desoneracao_icms: int | None = Field(default=None, alias="motivoDesoneracaoIcms")
    base_diferimento: float | None = Field(default=None, alias="baseDiferimento")
    valor_base_diferimento: float | None = Field(default=None, alias="valorBaseDiferimento")
    valor_presumido: float | None = Field(default=None, alias="valorPresumido")
    aliquota_posicao: float | None = Field(default=None, alias="aliquotaPosicao")


class CalculosImpostosIcmsStDTO(BlingModel):
    """Dados de cálculo do ICMS ST."""

    regra_operacao: CalculosImpostosRegraOperacaoDTO | None = Field(
        default=None, alias="regraOperacao"
    )
    tributacao: int | None = Field(default=None, alias="tributacao")
    cst: str | None = Field(default=None, alias="cst")
    aliquota: float | None = Field(default=None, alias="aliquota")
    base: float | None = Field(default=None, alias="base")
    valor_base_calculo: float | None = Field(default=None, alias="valorBaseCalculo")
    valor_imposto: float | None = Field(default=None, alias="valorImposto")
    observacoes: str | None = Field(default=None, alias="observacoes")
    informacoes_adicionais_fisco: str | None = Field(
        default=None, alias="informacoesAdicionaisFisco"
    )
    percentual_adicionado: float | None = Field(default=None, alias="percentualAdicionado")
    modalidade_base_calculo: int | None = Field(default=None, alias="modalidadeBaseCalculo")
    valor_pauta: float | None = Field(default=None, alias="valorPauta")


class CalculosImpostosIpiDTO(BlingModel):
    """Dados de cálculo do IPI."""

    regra_operacao: CalculosImpostosRegraOperacaoDTO | None = Field(
        default=None, alias="regraOperacao"
    )
    tributacao: int | None = Field(default=None, alias="tributacao")
    cst: str | None = Field(default=None, alias="cst")
    aliquota: float | None = Field(default=None, alias="aliquota")
    base: float | None = Field(default=None, alias="base")
    valor_base_calculo: float | None = Field(default=None, alias="valorBaseCalculo")
    valor_imposto: float | None = Field(default=None, alias="valorImposto")
    observacoes: str | None = Field(default=None, alias="observacoes")
    informacoes_adicionais_fisco: str | None = Field(
        default=None, alias="informacoesAdicionaisFisco"
    )
    valor_ipi_fixo_unitario: float | None = Field(default=None, alias="valorIpiFixoUnitario")
    classe_enquadramento_ipi: str | None = Field(default=None, alias="classeEnquadramentoIpi")
    codigo_enquadramento_ipi: int | None = Field(default=None, alias="codigoEnquadramentoIpi")
    codigo_selo: str | None = Field(default=None, alias="codigoSelo")
    codigo_ex_tipi: int | None = Field(default=None, alias="codigoExTipi")


class CalculosImpostosIssqnDTO(BlingModel):
    """Dados de cálculo do ISS-QN."""

    regra_operacao: CalculosImpostosRegraOperacaoDTO | None = Field(
        default=None, alias="regraOperacao"
    )
    tributacao: int | None = Field(default=None, alias="tributacao")
    cst: str | None = Field(default=None, alias="cst")
    aliquota: float | None = Field(default=None, alias="aliquota")
    base: float | None = Field(default=None, alias="base")
    valor_base_calculo: float | None = Field(default=None, alias="valorBaseCalculo")
    valor_imposto: float | None = Field(default=None, alias="valorImposto")
    observacoes: str | None = Field(default=None, alias="observacoes")
    informacoes_adicionais_fisco: str | None = Field(
        default=None, alias="informacoesAdicionaisFisco"
    )
    codigo_lista_servicos: str | None = Field(default=None, alias="codigoListaServicos")
    descontar_iss_total_nota: bool | None = Field(default=None, alias="descontarIssTotalNota")
    reter_iss: bool | None = Field(default=None, alias="reterIss")


class CalculosImpostosPisDTO(BlingModel):
    """Dados de cálculo do PIS."""

    regra_operacao: CalculosImpostosRegraOperacaoDTO | None = Field(
        default=None, alias="regraOperacao"
    )
    tributacao: int | None = Field(default=None, alias="tributacao")
    cst: str | None = Field(default=None, alias="cst")
    aliquota: float | None = Field(default=None, alias="aliquota")
    base: float | None = Field(default=None, alias="base")
    valor_base_calculo: float | None = Field(default=None, alias="valorBaseCalculo")
    valor_imposto: float | None = Field(default=None, alias="valorImposto")
    observacoes: str | None = Field(default=None, alias="observacoes")
    informacoes_adicionais_fisco: str | None = Field(
        default=None, alias="informacoesAdicionaisFisco"
    )
    valor_pis_fixo: float | None = Field(default=None, alias="valorPisFixo")


class CalculosImpostosCofinsDTO(BlingModel):
    """Dados de cálculo do COFINS."""

    regra_operacao: CalculosImpostosRegraOperacaoDTO | None = Field(
        default=None, alias="regraOperacao"
    )
    tributacao: int | None = Field(default=None, alias="tributacao")
    cst: str | None = Field(default=None, alias="cst")
    aliquota: float | None = Field(default=None, alias="aliquota")
    base: float | None = Field(default=None, alias="base")
    valor_base_calculo: float | None = Field(default=None, alias="valorBaseCalculo")
    valor_imposto: float | None = Field(default=None, alias="valorImposto")
    observacoes: str | None = Field(default=None, alias="observacoes")
    informacoes_adicionais_fisco: str | None = Field(
        default=None, alias="informacoesAdicionaisFisco"
    )
    valor_cofins_fixo: float | None = Field(default=None, alias="valorCofinsFixo")


class CalculosImpostosSimplesDTO(BlingModel):
    """Dados de cálculo do Simples."""

    regra_operacao: CalculosImpostosRegraOperacaoDTO | None = Field(
        default=None, alias="regraOperacao"
    )
    tributacao: int | None = Field(default=None, alias="tributacao")
    cst: str | None = Field(default=None, alias="cst")
    aliquota: float | None = Field(default=None, alias="aliquota")
    base: float | None = Field(default=None, alias="base")
    valor_base_calculo: float | None = Field(default=None, alias="valorBaseCalculo")
    valor_imposto: float | None = Field(default=None, alias="valorImposto")
    observacoes: str | None = Field(default=None, alias="observacoes")
    informacoes_adicionais_fisco: str | None = Field(
        default=None, alias="informacoesAdicionaisFisco"
    )
    base_diferimento: float | None = Field(default=None, alias="baseDiferimento")
    modalidade_base_calculo: int | None = Field(default=None, alias="modalidadeBaseCalculo")
    valor_pauta: float | None = Field(default=None, alias="valorPauta")
    valor_imposto_st: float | None = Field(default=None, alias="valorImpostoSt")
    valor_base_calculo_st: float | None = Field(default=None, alias="valorBaseCalculoSt")
    base_calculo_st: float | None = Field(default=None, alias="baseCalculoSt")
    percentual_adicionado_st: float | None = Field(default=None, alias="percentualAdicionadoSt")
    modalidade_base_calculo_st: float | None = Field(default=None, alias="modalidadeBaseCalculoSt")
    valor_pauta_st: float | None = Field(default=None, alias="valorPautaSt")
    aliquota_st: float | None = Field(default=None, alias="aliquotaSt")
    aliquota_st_retido: float | None = Field(default=None, alias="aliquotaStRetido")
    base_st_retido: float | None = Field(default=None, alias="baseStRetido")
    valor_unitario_base_cst_retencao: float | None = Field(
        default=None, alias="valorUnitarioBaseCstRetencao"
    )
    valor_unitario_icms_st_retencao: float | None = Field(
        default=None, alias="valorUnitarioIcmsStRetencao"
    )
    valor_unitario_icms_substituto: float | None = Field(
        default=None, alias="valorUnitarioIcmsSubstituto"
    )


class CalculosImpostosIbsDTO(BlingModel):
    """Dados de cálculo do IBS."""

    regra_operacao: CalculosImpostosRegraOperacaoDTO | None = Field(
        default=None, alias="regraOperacao"
    )
    percentual_ibs_uf: float | None = Field(default=None, alias="percentualIbsUf")
    percentual_ibs_municipio: float | None = Field(default=None, alias="percentualIbsMunicipio")
    percentual_reducao_aliquota_uf: float | None = Field(
        default=None, alias="percentualReducaoAliquotaUf"
    )
    percentual_reducao_aliquota_municipio: float | None = Field(
        default=None, alias="percentualReducaoAliquotaMunicipio"
    )
    aliquota_efetiva_uf: float | None = Field(default=None, alias="aliquotaEfetivaUf")
    aliquota_efetiva_municipio: float | None = Field(default=None, alias="aliquotaEfetivaMunicipio")
    percentual_diferimento_uf: float | None = Field(default=None, alias="percentualDiferimentoUf")
    percentual_diferimento_municipio: float | None = Field(
        default=None, alias="percentualDiferimentoMunicipio"
    )
    codigo_credito_presumido: str | None = Field(default=None, alias="codigoCreditoPresumido")
    percentual_credito_presumido: float | None = Field(
        default=None, alias="percentualCreditoPresumido"
    )


class CalculosImpostosCbsDTO(BlingModel):
    """Dados de cálculo do CBS."""

    regra_operacao: CalculosImpostosRegraOperacaoDTO | None = Field(
        default=None, alias="regraOperacao"
    )
    percentual_cbs: float | None = Field(default=None, alias="percentualCbs")
    percentual_reducao_aliquota: float | None = Field(
        default=None, alias="percentualReducaoAliquota"
    )
    aliquota_efetiva: float | None = Field(default=None, alias="aliquotaEfetiva")
    percentual_diferimento: float | None = Field(default=None, alias="percentualDiferimento")
    codigo_credito_presumido: str | None = Field(default=None, alias="codigoCreditoPresumido")
    percentual_credito_presumido: float | None = Field(
        default=None, alias="percentualCreditoPresumido"
    )


class CalculosImpostosIbsCbsDTO(BlingModel):
    """Dados de cálculo do IBS/CBS."""

    regra_operacao: CalculosImpostosRegraOperacaoDTO | None = Field(
        default=None, alias="regraOperacao"
    )
    cst: str | None = Field(default=None, alias="cst")
    classificacao_tributaria: str | None = Field(default=None, alias="classificacaoTributaria")
    valor_base_calculo: float | None = Field(default=None, alias="valorBaseCalculo")


class CalculosImpostosIbsCbsRegDTO(BlingModel):
    """Dados de cálculo do IBS/CBS Regime Regular."""

    cst_regular: str | None = Field(default=None, alias="cstRegular")
    classificacao_tributaria_regular: str | None = Field(
        default=None, alias="classificacaoTributariaRegular"
    )
    aliquota_efetiva_regular_ibs_uf: float | None = Field(
        default=None, alias="aliquotaEfetivaRegularIbsUf"
    )
    aliquota_efetiva_regular_ibs_municipio: float | None = Field(
        default=None, alias="aliquotaEfetivaRegularIbsMunicipio"
    )
    aliquota_efetiva_regular_cbs: float | None = Field(
        default=None, alias="aliquotaEfetivaRegularCbs"
    )
    valor_tributacao_regular_ibs_uf: float | None = Field(
        default=None, alias="valorTributacaoRegularIbsUf"
    )
    valor_tributacao_regular_ibs_municipio: float | None = Field(
        default=None, alias="valorTributacaoRegularIbsMunicipio"
    )
    valor_tributacao_regular_cbs: float | None = Field(
        default=None, alias="valorTributacaoRegularCbs"
    )


class CalculosImpostosMunicipioDTO(BlingModel):
    """Município para cálculo de impostos."""

    id: int = Field(..., alias="id")


class CalculosImpostosUnidadeNegocioDTO(BlingModel):
    """Unidade de negócio para cálculo de impostos."""

    id: int = Field(..., alias="id")


class CalculosImpostosLojaDTO(BlingModel):
    """Loja para cálculo de impostos."""

    id: int = Field(..., alias="id")
    unidade_negocio: CalculosImpostosUnidadeNegocioDTO | None = Field(
        default=None, alias="unidadeNegocio"
    )


class CalculosImpostosProdutoDTO(BlingModel):
    """Produto para cálculo de impostos."""

    id: int = Field(..., alias="id")
    valor_unitario: float = Field(..., alias="valorUnitario")
    cupom_fiscal: int = Field(..., alias="cupomFiscal")
    origem: int = Field(..., alias="origem")
    quantidade: float = Field(..., alias="quantidade")


class CalculosImpostosCalculoDTO(BlingModel):
    """Corpo da requisição para cálculo de tributação."""

    tipo_nota: int = Field(..., alias="tipoNota")
    uf: str = Field(..., alias="uf")
    municipio: CalculosImpostosMunicipioDTO = Field(..., alias="municipio")
    obter_regras: bool | None = Field(default=True, alias="obterRegras")
    crt: int | None = Field(default=None, alias="crt")
    loja: CalculosImpostosLojaDTO = Field(..., alias="loja")
    produto: CalculosImpostosProdutoDTO = Field(..., alias="produto")


class CalculosImpostosDadosDTO(BlingModel):
    """Resposta do cálculo de tributação."""

    faturada: bool | None = Field(default=None, alias="faturada")
    observacoes: str | None = Field(default=None, alias="observacoes")
    pis_cofins_presumido: bool | None = Field(default=None, alias="pisCofinsPresumido")
    soma_impostos_total: bool | None = Field(default=None, alias="somaImpostosTotal")
    soma_icms_total: bool | None = Field(default=None, alias="somaIcmsTotal")
    aliquota_funrural: float | None = Field(default=None, alias="aliquotaFunrural")
    desconta_funrural: bool | None = Field(default=None, alias="descontaFunrural")
    consumidor_final: bool | None = Field(default=None, alias="consumidorFinal")
    ret_imposto_retido: bool | None = Field(default=None, alias="retImpostoRetido")
    ret_aliquota_ir: float | None = Field(default=None, alias="retAliquotaIr")
    ret_valor_ir: float | None = Field(default=None, alias="retValorIr")
    ret_aliquota_csll: float | None = Field(default=None, alias="retAliquotaCsll")
    ret_valor_csll: float | None = Field(default=None, alias="retValorCsll")
    desconto_condicional: bool | None = Field(default=None, alias="descontoCondicional")
    base_comissao: float | None = Field(default=None, alias="baseComissao")
    icms: CalculosImpostosIcmsDTO | None = Field(default=None, alias="icms")
    valor_pmc: float | None = Field(default=None, alias="valorPmc")
    aliquota_valor_aprox_impostos: float | None = Field(
        default=None, alias="aliquotaValorAproxImpostos"
    )
    informacoes_adicionais_fisco: str | None = Field(
        default=None, alias="informacoesAdicionaisFisco"
    )
    incluir_frete_ipi: bool | None = Field(default=None, alias="incluirFreteIpi")
    simples: CalculosImpostosSimplesDTO | None = Field(default=None, alias="simples")
    ipi: CalculosImpostosIpiDTO | None = Field(default=None, alias="ipi")
    issqn: CalculosImpostosIssqnDTO | None = Field(default=None, alias="issqn")
    pis: CalculosImpostosPisDTO | None = Field(default=None, alias="pis")
    cofins: CalculosImpostosCofinsDTO | None = Field(default=None, alias="cofins")
    icms_st: CalculosImpostosIcmsStDTO | None = Field(default=None, alias="icmsSt")
    pis_st: CalculosImpostosDadosBaseDTO | None = Field(default=None, alias="pisSt")
    cofins_st: CalculosImpostosDadosBaseDTO | None = Field(default=None, alias="cofinsSt")
    ii: CalculosImpostosDadosBaseDTO | None = Field(default=None, alias="ii")
    codigo_beneficio_fiscal: str | None = Field(default=None, alias="codigoBeneficioFiscal")
    porcentagem_fcp: float | None = Field(default=None, alias="porcentagemFcp")
    cfop: int | None = Field(default=None, alias="cfop")
    simples_st: CalculosImpostosDadosBaseDTO | None = Field(default=None, alias="simplesSt")
    ibs_cbs: CalculosImpostosIbsCbsDTO | None = Field(default=None, alias="ibsCbs")
    ibs: CalculosImpostosIbsDTO | None = Field(default=None, alias="ibs")
    cbs: CalculosImpostosCbsDTO | None = Field(default=None, alias="cbs")
    ibs_cbs_reg: CalculosImpostosIbsCbsRegDTO | None = Field(default=None, alias="ibsCbsReg")
