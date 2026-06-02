# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``configuracoes``. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.models.fields import BlingDate
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel


class ConfiguracaoAproximadoNotaServicoDTO(BlingModel):
    """OpenAPI schema ``ConfiguracaoAproximadoNotaServicoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        utilizar_aliq_ibpt: Bling ``utilizarAliqIBPT``; type ``bool | None``; opcional. Utilizar alíquotas da tabela do IBPT para cálculo de tributos aproximados
        percentual_aliq: Bling ``percentualAliq``; type ``float | None``; opcional. Alíquota para cálculo de impostos aproximados"""

    utilizar_aliq_ibpt: bool | None = Field(
        default=None,
        validation_alias=AliasChoices("utilizar_aliq_ibpt", "utilizarAliqIBPT"),
        examples=["true"],
        serialization_alias="utilizarAliqIBPT",
    )
    percentual_aliq: float | None = Field(
        default=None,
        validation_alias=AliasChoices("percentual_aliq", "percentualAliq"),
        examples=[0],
        serialization_alias="percentualAliq",
    )


class ConfiguracaoBasicaNotaServicoDTO(BlingModel):
    """OpenAPI schema ``ConfiguracaoBasicaNotaServicoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        emissor_padrao: Bling ``emissorPadrao``; type ``int | None``; opcional.
        natureza_operacao: Bling ``naturezaOperacao``; type ``int | None``; opcional."""

    emissor_padrao: int | None = Field(
        default=None,
        validation_alias=AliasChoices("emissor_padrao", "emissorPadrao"),
        examples=[3],
        serialization_alias="emissorPadrao",
    )
    natureza_operacao: int | None = Field(
        default=None,
        validation_alias=AliasChoices("natureza_operacao", "naturezaOperacao"),
        examples=[1],
        serialization_alias="naturezaOperacao",
    )


class ConfiguracaoCSLLPISCOFINSNotaServicoDTO(BlingModel):
    """OpenAPI schema ``ConfiguracaoCSLLPISCOFINSNotaServicoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        calcular: Bling ``calcular``; type ``bool | None``; opcional. Reter CSLL, PIS e COFINS para notas acima de R$ 5.000,00 (Descontinuado pela Lei 13.137)
        reter: Bling ``reter``; type ``bool | None``; opcional. Reter CSLL, PIS e COFINS quando a soma desses impostos for maior que R$ 10,00(Lei 10.833)"""

    calcular: bool | None = Field(default=None, examples=["true"])
    reter: bool | None = Field(default=None, examples=["false"])


class ConfiguracaoCadastroPrefeituraNotaServicoDTO(BlingModel):
    """OpenAPI schema ``ConfiguracaoCadastroPrefeituraNotaServicoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        login: Bling ``login``; type ``str | None``; opcional.
        senha: Bling ``senha``; type ``str | None``; opcional."""

    login: str | None = Field(default=None, examples=["Login prefeitura"])
    senha: str | None = Field(default=None, examples=["Senha prefeitura"])


class ConfiguracaoCodigoTributoNotaServicoDTO(BlingModel):
    """OpenAPI schema ``ConfiguracaoCodigoTributoNotaServicoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        lista_servico: Bling ``listaServico``; type ``str``; obrigatório.
        tributacao: Bling ``tributacao``; type ``str | None``; opcional."""

    lista_servico: str = Field(
        ...,
        validation_alias=AliasChoices("lista_servico", "listaServico"),
        examples=["0107"],
        serialization_alias="listaServico",
    )
    tributacao: str | None = Field(default=None, examples=["0107"])


class ConfiguracaoEmailPadraoNotaFiscalServicoDTO(BlingModel):
    """OpenAPI schema ``ConfiguracaoEmailPadraoNotaFiscalServicoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        copia: Bling ``copia``; type ``str | None``; opcional.
        resposta: Bling ``resposta``; type ``str | None``; opcional."""

    copia: str | None = Field(default=None, examples=["E-mail padrão de cópia"])
    resposta: str | None = Field(default=None, examples=["E-mail padrão de resposta"])


class ConfiguracaoEnvioEmailNotaServicoDTO(BlingModel):
    """OpenAPI schema ``ConfiguracaoEnvioEmailNotaServicoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        enviar_boleto_rps: Bling ``enviarBoletoRPS``; type ``bool | None``; opcional. Enviar junto com o RPS o boleto das contas lançadas através do RPS ou do contrato
        remetente: Bling ``remetente``; type ``str | None``; opcional.
        assunto: Bling ``assunto``; type ``str | None``; opcional.
        mensagem: Bling ``mensagem``; type ``str | None``; opcional.
        padrao: Bling ``padrao``; type ``ConfiguracaoEmailPadraoNotaFiscalServicoDTO | None``; opcional."""

    enviar_boleto_rps: bool | None = Field(
        default=None,
        validation_alias=AliasChoices("enviar_boleto_rps", "enviarBoletoRPS"),
        examples=["true"],
        serialization_alias="enviarBoletoRPS",
    )
    remetente: str | None = Field(default=None, examples=["Nome remetente padrão"])
    assunto: str | None = Field(default=None, examples=["Assunto padrão"])
    mensagem: str | None = Field(default=None, examples=["Mensagem padrão e-mail"])
    padrao: ConfiguracaoEmailPadraoNotaFiscalServicoDTO | None = None


class ConfiguracaoINSSNotaServicoDTO(BlingModel):
    """OpenAPI schema ``ConfiguracaoINSSNotaServicoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        reter: Bling ``reter``; type ``bool | None``; opcional. Determina se o INSS deve ser retido"""

    reter: bool | None = Field(default=None, examples=["true"])


class ConfiguracaoNumeracaoRPSNotaServicoDTO(BlingModel):
    """OpenAPI schema ``ConfiguracaoNumeracaoRPSNotaServicoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        cnpj_emitente: Bling ``cnpjEmitente``; type ``str | None``; opcional.
        id: Bling ``id``; type ``int | None``; opcional.
        numero: Bling ``numero``; type ``int | None``; opcional.
        serie: Bling ``serie``; type ``int | None``; opcional."""

    cnpj_emitente: str | None = Field(
        default=None,
        validation_alias=AliasChoices("cnpj_emitente", "cnpjEmitente"),
        examples=["48.426.683/0001-70"],
        serialization_alias="cnpjEmitente",
    )
    id: int | None = Field(default=None, examples=[1])
    numero: int | None = Field(default=None, examples=[1])
    serie: int | None = Field(default=None, examples=[1])


class ConfiguracaoOutrosNotaServicoDTO(BlingModel):
    """OpenAPI schema ``ConfiguracaoOutrosNotaServicoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        csllpiscofinsdto: Bling ``CSLLPISCOFINSDTO``; type ``ConfiguracaoCSLLPISCOFINSNotaServicoDTO | None``; opcional.
        inss: Bling ``INSS``; type ``ConfiguracaoINSSNotaServicoDTO | None``; opcional.
        aproximados: Bling ``aproximados``; type ``ConfiguracaoAproximadoNotaServicoDTO | None``; opcional."""

    csllpiscofinsdto: ConfiguracaoCSLLPISCOFINSNotaServicoDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("csllpiscofinsdto", "CSLLPISCOFINSDTO"),
        serialization_alias="CSLLPISCOFINSDTO",
    )
    inss: ConfiguracaoINSSNotaServicoDTO | None = Field(
        default=None, validation_alias=AliasChoices("inss", "INSS"), serialization_alias="INSS"
    )
    aproximados: ConfiguracaoAproximadoNotaServicoDTO | None = None


class ConfiguracaoTextoIRNotaServicoDTO(BlingModel):
    """OpenAPI schema ``ConfiguracaoTextoIRNotaServicoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        padrao: Bling ``padrao``; type ``str | None``; opcional.
        isento: Bling ``isento``; type ``str | None``; opcional."""

    padrao: str | None = Field(default=None, examples=["( - ) IRenda Fonte 1,5%"])
    isento: str | None = Field(default=None, examples=["IR Isento Cfe. Lei nro. 9430/96 Art.64"])


class ConfiguracaoTributoNotaServicoDTO(BlingModel):
    """OpenAPI schema ``ConfiguracaoTributoNotaServicoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. ID é passado apenas para tributos existentes para fins de atualização
        percentual_iss: Bling ``percentualISS``; type ``float | None``; opcional.
        cnae: Bling ``CNAE``; type ``str``; obrigatório.
        descricao_servico: Bling ``descricaoServico``; type ``str``; obrigatório.
        padrao: Bling ``padrao``; type ``bool | None``; opcional. Determina se o tributo em questão será o padrão para criação de notas
        indicador_operacao: Bling ``indicadorOperacao``; type ``str | None``; opcional. Indicador de operação da reforma tributária
        codigo: Bling ``codigo``; type ``ConfiguracaoCodigoTributoNotaServicoDTO``; obrigatório."""

    id: int | None = Field(default=None, examples=[1])
    percentual_iss: float | None = Field(
        default=None,
        validation_alias=AliasChoices("percentual_iss", "percentualISS"),
        examples=[5],
        serialization_alias="percentualISS",
    )
    cnae: str = Field(
        ...,
        validation_alias=AliasChoices("cnae", "CNAE"),
        examples=["82.99"],
        serialization_alias="CNAE",
    )
    descricao_servico: str = Field(
        ...,
        validation_alias=AliasChoices("descricao_servico", "descricaoServico"),
        examples=["Laudo de Vistoria Veicular"],
        serialization_alias="descricaoServico",
    )
    padrao: bool | None = Field(default=None, examples=["false"])
    indicador_operacao: str | None = Field(
        default=None,
        validation_alias=AliasChoices("indicador_operacao", "indicadorOperacao"),
        examples=["010101"],
        serialization_alias="indicadorOperacao",
    )
    codigo: ConfiguracaoCodigoTributoNotaServicoDTO


class ConfiguracaoAdicionalNotaServicoDTO(BlingModel):
    """OpenAPI schema ``ConfiguracaoAdicionalNotaServicoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        cfps: Bling ``CFPS``; type ``str | None``; opcional. Código Fiscal de Prestação de Serviço
        cfop: Bling ``CFOP``; type ``str | None``; opcional. Código Fiscal de Operações e Prestações
        aedf: Bling ``AEDF``; type ``str | None``; opcional. Autorização de Emissão de Documento Fiscal Eletrônico
        proximo_numero_lote: Bling ``proximoNumeroLote``; type ``int | None``; opcional.
        observacao_impressa_nota: Bling ``observacaoImpressaNota``; type ``str | None``; opcional. Observação utilizada apenas para impressão
        descricao_complementar: Bling ``descricaoComplementar``; type ``str | None``; opcional. Será adicionada abaixa da descrição do serviço em todas as notas
        tipo_emissao: Bling ``tipoEmissao``; type ``str | None``; opcional. `T` Todos <br>`R` RPS e NFS-e <br>`N` Apenas NFS-e
        campo_numero_doc_contas: Bling ``campoNumeroDocContas``; type ``bool | None``; opcional. Escolha qual informação será utilizada como nº do documento ao lançar contas. Utilize o campo RPS caso o lançamento de contas ocorra antes do envio da nota
        incentivador_fiscal: Bling ``incentivadorFiscal``; type ``bool | None``; opcional.
        alterar_situacao: Bling ``alterarSituacao``; type ``bool | None``; opcional. Permitir alteração de situação por usuários
        incluir_parcelas: Bling ``incluirParcelas``; type ``bool | None``; opcional. Incluir informação das parcelas na descrição dos serviços na emissão da NFS-e
        considerar_data_parcela: Bling ``considerarDataParcela``; type ``bool | None``; opcional. Permite utilizar a data de vencimento da parcela da venda na geração automática de parcelas da nota de serviço
        considerar_data_ordem_servico: Bling ``considerarDataOrdemServico``; type ``bool | None``; opcional. Permite utilizar a data de vencimento da parcela da ordem de serviço na geração automática de parcelas da nota de serviço
        cadastro_prefeitura: Bling ``cadastroPrefeitura``; type ``ConfiguracaoCadastroPrefeituraNotaServicoDTO | None``; opcional."""

    cfps: str | None = Field(
        default=None,
        validation_alias=AliasChoices("cfps", "CFPS"),
        examples=["9.001"],
        serialization_alias="CFPS",
    )
    cfop: str | None = Field(
        default=None,
        validation_alias=AliasChoices("cfop", "CFOP"),
        examples=["1.250"],
        serialization_alias="CFOP",
    )
    aedf: str | None = Field(
        default=None,
        validation_alias=AliasChoices("aedf", "AEDF"),
        examples=[""],
        serialization_alias="AEDF",
    )
    proximo_numero_lote: int | None = Field(
        default=None,
        validation_alias=AliasChoices("proximo_numero_lote", "proximoNumeroLote"),
        examples=[78],
        serialization_alias="proximoNumeroLote",
    )
    observacao_impressa_nota: str | None = Field(
        default=None,
        validation_alias=AliasChoices("observacao_impressa_nota", "observacaoImpressaNota"),
        examples=["OBS"],
        serialization_alias="observacaoImpressaNota",
    )
    descricao_complementar: str | None = Field(
        default=None,
        validation_alias=AliasChoices("descricao_complementar", "descricaoComplementar"),
        examples=["OBS"],
        serialization_alias="descricaoComplementar",
    )
    tipo_emissao: str | None = Field(
        default=None,
        validation_alias=AliasChoices("tipo_emissao", "tipoEmissao"),
        examples=["R"],
        serialization_alias="tipoEmissao",
    )
    campo_numero_doc_contas: bool | None = Field(
        default=None,
        validation_alias=AliasChoices("campo_numero_doc_contas", "campoNumeroDocContas"),
        examples=["true"],
        serialization_alias="campoNumeroDocContas",
    )
    incentivador_fiscal: bool | None = Field(
        default=None,
        validation_alias=AliasChoices("incentivador_fiscal", "incentivadorFiscal"),
        examples=["true"],
        serialization_alias="incentivadorFiscal",
    )
    alterar_situacao: bool | None = Field(
        default=None,
        validation_alias=AliasChoices("alterar_situacao", "alterarSituacao"),
        examples=["true"],
        serialization_alias="alterarSituacao",
    )
    incluir_parcelas: bool | None = Field(
        default=None,
        validation_alias=AliasChoices("incluir_parcelas", "incluirParcelas"),
        examples=["false"],
        serialization_alias="incluirParcelas",
    )
    considerar_data_parcela: bool | None = Field(
        default=None,
        validation_alias=AliasChoices("considerar_data_parcela", "considerarDataParcela"),
        examples=["true"],
        serialization_alias="considerarDataParcela",
    )
    considerar_data_ordem_servico: bool | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "considerar_data_ordem_servico", "considerarDataOrdemServico"
        ),
        examples=["true"],
        serialization_alias="considerarDataOrdemServico",
    )
    cadastro_prefeitura: ConfiguracaoCadastroPrefeituraNotaServicoDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("cadastro_prefeitura", "cadastroPrefeitura"),
        serialization_alias="cadastroPrefeitura",
    )


class ConfiguracaoControleNotaServicoDTO(BlingModel):
    """OpenAPI schema ``ConfiguracaoControleNotaServicoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        numeracao_rps: Bling ``numeracaoRPS``; type ``ConfiguracaoNumeracaoRPSNotaServicoDTO | None``; opcional."""

    numeracao_rps: ConfiguracaoNumeracaoRPSNotaServicoDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("numeracao_rps", "numeracaoRPS"),
        serialization_alias="numeracaoRPS",
    )


class ConfiguracaoIRNotaServicoDTO(BlingModel):
    """OpenAPI schema ``ConfiguracaoIRNotaServicoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        percentual: Bling ``percentual``; type ``float | None``; opcional.
        valor_minimo_alternativo_descontol: Bling ``valorMinimoAlternativoDescontol``; type ``float | None``; opcional.
        descontar: Bling ``descontar``; type ``bool | None``; opcional. Determina se o valor mínimo alternativo de desconto será aplicado
        texto: Bling ``texto``; type ``ConfiguracaoTextoIRNotaServicoDTO | None``; opcional."""

    percentual: float | None = Field(default=None, examples=[0])
    valor_minimo_alternativo_descontol: float | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "valor_minimo_alternativo_descontol", "valorMinimoAlternativoDescontol"
        ),
        examples=[0],
        serialization_alias="valorMinimoAlternativoDescontol",
    )
    descontar: bool | None = Field(default=None, examples=["false"])
    texto: ConfiguracaoTextoIRNotaServicoDTO | None = None


class ConfiguracaoISSNotaServicoDTO(BlingModel):
    """OpenAPI schema ``ConfiguracaoISSNotaServicoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        zerar: Bling ``zerar``; type ``bool | None``; opcional.
        reter: Bling ``reter``; type ``bool | None``; opcional.
        descontar: Bling ``descontar``; type ``bool | None``; opcional.
        tributos: Bling ``tributos``; type ``list[ConfiguracaoTributoNotaServicoDTO]``; obrigatório."""

    zerar: bool | None = Field(default=None, examples=["false"])
    reter: bool | None = Field(default=None, examples=["true"])
    descontar: bool | None = Field(default=None, examples=["true"])
    tributos: list[ConfiguracaoTributoNotaServicoDTO]


class ConfiguracaoImpostoNotaServicoDTO(BlingModel):
    """OpenAPI schema ``ConfiguracaoImpostoNotaServicoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        bloquear_retencao_pessoa_fisica: Bling ``bloquearRetencaoPessoaFisica``; type ``bool | None``; opcional.
        ir: Bling ``IR``; type ``ConfiguracaoIRNotaServicoDTO | None``; opcional.
        outros: Bling ``outros``; type ``ConfiguracaoOutrosNotaServicoDTO | None``; opcional."""

    bloquear_retencao_pessoa_fisica: bool | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "bloquear_retencao_pessoa_fisica", "bloquearRetencaoPessoaFisica"
        ),
        examples=["true"],
        serialization_alias="bloquearRetencaoPessoaFisica",
    )
    ir: ConfiguracaoIRNotaServicoDTO | None = Field(
        default=None, validation_alias=AliasChoices("ir", "IR"), serialization_alias="IR"
    )
    outros: ConfiguracaoOutrosNotaServicoDTO | None = None


class ConfiguracaoNotaServicoDadosBaseDTO(BlingModel):
    """OpenAPI schema ``ConfiguracaoNotaServicoDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        basicas: Bling ``basicas``; type ``ConfiguracaoBasicaNotaServicoDTO | None``; opcional.
        iss: Bling ``ISS``; type ``ConfiguracaoISSNotaServicoDTO | None``; opcional.
        controle: Bling ``controle``; type ``ConfiguracaoControleNotaServicoDTO | None``; opcional.
        impostos: Bling ``impostos``; type ``ConfiguracaoImpostoNotaServicoDTO | None``; opcional.
        envio_email: Bling ``envioEmail``; type ``ConfiguracaoEnvioEmailNotaServicoDTO | None``; opcional.
        adicionais: Bling ``adicionais``; type ``ConfiguracaoAdicionalNotaServicoDTO | None``; opcional."""

    basicas: ConfiguracaoBasicaNotaServicoDTO | None = None
    iss: ConfiguracaoISSNotaServicoDTO | None = Field(
        default=None, validation_alias=AliasChoices("iss", "ISS"), serialization_alias="ISS"
    )
    controle: ConfiguracaoControleNotaServicoDTO | None = None
    impostos: ConfiguracaoImpostoNotaServicoDTO | None = None
    envio_email: ConfiguracaoEnvioEmailNotaServicoDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("envio_email", "envioEmail"),
        serialization_alias="envioEmail",
    )
    adicionais: ConfiguracaoAdicionalNotaServicoDTO | None = None


__all__ = [
    "ConfiguracaoAdicionalNotaServicoDTO",
    "ConfiguracaoAproximadoNotaServicoDTO",
    "ConfiguracaoBasicaNotaServicoDTO",
    "ConfiguracaoCSLLPISCOFINSNotaServicoDTO",
    "ConfiguracaoCadastroPrefeituraNotaServicoDTO",
    "ConfiguracaoCodigoTributoNotaServicoDTO",
    "ConfiguracaoControleNotaServicoDTO",
    "ConfiguracaoEmailPadraoNotaFiscalServicoDTO",
    "ConfiguracaoEnvioEmailNotaServicoDTO",
    "ConfiguracaoINSSNotaServicoDTO",
    "ConfiguracaoIRNotaServicoDTO",
    "ConfiguracaoISSNotaServicoDTO",
    "ConfiguracaoImpostoNotaServicoDTO",
    "ConfiguracaoNotaServicoDadosBaseDTO",
    "ConfiguracaoNumeracaoRPSNotaServicoDTO",
    "ConfiguracaoOutrosNotaServicoDTO",
    "ConfiguracaoTextoIRNotaServicoDTO",
    "ConfiguracaoTributoNotaServicoDTO",
]
