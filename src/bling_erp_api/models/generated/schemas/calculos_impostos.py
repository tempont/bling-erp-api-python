# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``calculos_impostos``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel


class CalculosImpostosIbsCbsRegDTO(BlingModel):
    """OpenAPI schema ``CalculosImpostosIbsCbsRegDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        cst_regular: Bling ``cstRegular``; type ``str | None``; opcional. CST da Tributação Regular
        classificacao_tributaria_regular: Bling ``classificacaoTributariaRegular``; type ``str | None``; opcional. Classificação Tributária Regular
        aliquota_efetiva_regular_ibs_uf: Bling ``aliquotaEfetivaRegularIbsUf``; type ``float | None``; opcional. Alíquota Efetiva Regular IBS UF
        aliquota_efetiva_regular_ibs_municipio: Bling ``aliquotaEfetivaRegularIbsMunicipio``; type ``float | None``; opcional. Alíquota Efetiva Regular IBS Município
        aliquota_efetiva_regular_cbs: Bling ``aliquotaEfetivaRegularCbs``; type ``float | None``; opcional. Alíquota Efetiva Regular CBS
        valor_tributacao_regular_ibs_uf: Bling ``valorTributacaoRegularIbsUf``; type ``float | None``; opcional. Valor Tributação Regular IBS UF
        valor_tributacao_regular_ibs_municipio: Bling ``valorTributacaoRegularIbsMunicipio``; type ``float | None``; opcional. Valor Tributação Regular IBS Município
        valor_tributacao_regular_cbs: Bling ``valorTributacaoRegularCbs``; type ``float | None``; opcional. Valor Tributação Regular CBS"""

    cst_regular: str | None = Field(default=None, alias="cstRegular", examples=["000"])
    classificacao_tributaria_regular: str | None = Field(
        default=None, alias="classificacaoTributariaRegular", examples=["000001"]
    )
    aliquota_efetiva_regular_ibs_uf: float | None = Field(
        default=None, alias="aliquotaEfetivaRegularIbsUf", examples=[0]
    )
    aliquota_efetiva_regular_ibs_municipio: float | None = Field(
        default=None, alias="aliquotaEfetivaRegularIbsMunicipio", examples=[0]
    )
    aliquota_efetiva_regular_cbs: float | None = Field(
        default=None, alias="aliquotaEfetivaRegularCbs", examples=[0]
    )
    valor_tributacao_regular_ibs_uf: float | None = Field(
        default=None, alias="valorTributacaoRegularIbsUf", examples=[0]
    )
    valor_tributacao_regular_ibs_municipio: float | None = Field(
        default=None, alias="valorTributacaoRegularIbsMunicipio", examples=[0]
    )
    valor_tributacao_regular_cbs: float | None = Field(
        default=None, alias="valorTributacaoRegularCbs", examples=[0]
    )


class CalculosImpostosMunicipioDTO(BlingModel):
    """OpenAPI schema ``CalculosImpostosMunicipioDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. ID do município segundo a Tabela de Código de Município do IBGE"""

    id: int = Field(..., examples=[4302105])


class CalculosImpostosProdutoDTO(BlingModel):
    """OpenAPI schema ``CalculosImpostosProdutoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        valor_unitario: Bling ``valorUnitario``; type ``float``; obrigatório.
        cupom_fiscal: Bling ``cupomFiscal``; type ``int``; obrigatório.
        origem: Bling ``origem``; type ``int``; obrigatório. `0` Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8 <br>`1` Estrangeira - Importação direta, exceto a indicada no código 6 <br>`2` Estrangeira - Adquirida no mercado interno...
        quantidade: Bling ``quantidade``; type ``float``; obrigatório."""

    id: int = Field(..., examples=[12345678])
    valor_unitario: float = Field(..., alias="valorUnitario", examples=[0])
    cupom_fiscal: int = Field(..., alias="cupomFiscal", examples=[0])
    origem: int = Field(..., examples=[0])
    quantidade: float = Field(..., examples=[0])


class CalculosImpostosRegraOperacaoDTO(BlingModel):
    """OpenAPI schema ``CalculosImpostosRegraOperacaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class CalculosImpostosUnidadeNegocioDTO(BlingModel):
    """OpenAPI schema ``CalculosImpostosUnidadeNegocioDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class CalculosImpostosCbsDTO(BlingModel):
    """OpenAPI schema ``CalculosImpostosCbsDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        regra_operacao: Bling ``regraOperacao``; type ``CalculosImpostosRegraOperacaoDTO | None``; opcional.
        percentual_cbs: Bling ``percentualCbs``; type ``float | None``; opcional. Percentual CBS
        percentual_reducao_aliquota: Bling ``percentualReducaoAliquota``; type ``float | None``; opcional. % Redução Alíquota
        aliquota_efetiva: Bling ``aliquotaEfetiva``; type ``float | None``; opcional. Alíquota Efetiva
        percentual_diferimento: Bling ``percentualDiferimento``; type ``float | None``; opcional. % Diferimento
        codigo_credito_presumido: Bling ``codigoCreditoPresumido``; type ``str | None``; opcional. Código Crédito Presumido
        percentual_credito_presumido: Bling ``percentualCreditoPresumido``; type ``float | None``; opcional. % Crédito Presumido CBS"""

    regra_operacao: CalculosImpostosRegraOperacaoDTO | None = Field(
        default=None, alias="regraOperacao"
    )
    percentual_cbs: float | None = Field(default=None, alias="percentualCbs", examples=[0.9])
    percentual_reducao_aliquota: float | None = Field(
        default=None, alias="percentualReducaoAliquota", examples=[0]
    )
    aliquota_efetiva: float | None = Field(default=None, alias="aliquotaEfetiva", examples=[0])
    percentual_diferimento: float | None = Field(
        default=None, alias="percentualDiferimento", examples=[0]
    )
    codigo_credito_presumido: str | None = Field(
        default=None, alias="codigoCreditoPresumido", examples=[""]
    )
    percentual_credito_presumido: float | None = Field(
        default=None, alias="percentualCreditoPresumido", examples=[0]
    )


class CalculosImpostosIbsCbsDTO(BlingModel):
    """OpenAPI schema ``CalculosImpostosIbsCbsDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        regra_operacao: Bling ``regraOperacao``; type ``CalculosImpostosRegraOperacaoDTO | None``; opcional.
        cst: Bling ``cst``; type ``str | None``; opcional. Código de Situação Tributária
        classificacao_tributaria: Bling ``classificacaoTributaria``; type ``str | None``; opcional. Código de Classificação Tributária
        valor_base_calculo: Bling ``valorBaseCalculo``; type ``float | None``; opcional. Valor Base de Cálculo IBS/CBS"""

    regra_operacao: CalculosImpostosRegraOperacaoDTO | None = Field(
        default=None, alias="regraOperacao"
    )
    cst: str | None = Field(default=None, examples=["000"])
    classificacao_tributaria: str | None = Field(
        default=None, alias="classificacaoTributaria", examples=["000001"]
    )
    valor_base_calculo: float | None = Field(default=None, alias="valorBaseCalculo", examples=[0])


class CalculosImpostosIbsDTO(BlingModel):
    """OpenAPI schema ``CalculosImpostosIbsDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        regra_operacao: Bling ``regraOperacao``; type ``CalculosImpostosRegraOperacaoDTO | None``; opcional.
        percentual_ibs_uf: Bling ``percentualIbsUf``; type ``float | None``; opcional. Percentual IBS UF
        percentual_ibs_municipio: Bling ``percentualIbsMunicipio``; type ``float | None``; opcional. Percentual IBS Município
        percentual_reducao_aliquota_uf: Bling ``percentualReducaoAliquotaUf``; type ``float | None``; opcional. % Redução Alíquota UF
        percentual_reducao_aliquota_municipio: Bling ``percentualReducaoAliquotaMunicipio``; type ``float | None``; opcional. % Redução Alíquota Município
        aliquota_efetiva_uf: Bling ``aliquotaEfetivaUf``; type ``float | None``; opcional. Alíquota Efetiva UF
        aliquota_efetiva_municipio: Bling ``aliquotaEfetivaMunicipio``; type ``float | None``; opcional. Alíquota Efetiva Município
        percentual_diferimento_uf: Bling ``percentualDiferimentoUf``; type ``float | None``; opcional. % Diferimento UF
        percentual_diferimento_municipio: Bling ``percentualDiferimentoMunicipio``; type ``float | None``; opcional. % Diferimento Município
        codigo_credito_presumido: Bling ``codigoCreditoPresumido``; type ``str | None``; opcional. Código Crédito Presumido
        percentual_credito_presumido: Bling ``percentualCreditoPresumido``; type ``float | None``; opcional. % Crédito Presumido IBS"""

    regra_operacao: CalculosImpostosRegraOperacaoDTO | None = Field(
        default=None, alias="regraOperacao"
    )
    percentual_ibs_uf: float | None = Field(default=None, alias="percentualIbsUf", examples=[0.1])
    percentual_ibs_municipio: float | None = Field(
        default=None, alias="percentualIbsMunicipio", examples=[0]
    )
    percentual_reducao_aliquota_uf: float | None = Field(
        default=None, alias="percentualReducaoAliquotaUf", examples=[0]
    )
    percentual_reducao_aliquota_municipio: float | None = Field(
        default=None, alias="percentualReducaoAliquotaMunicipio", examples=[0]
    )
    aliquota_efetiva_uf: float | None = Field(default=None, alias="aliquotaEfetivaUf", examples=[0])
    aliquota_efetiva_municipio: float | None = Field(
        default=None, alias="aliquotaEfetivaMunicipio", examples=[0]
    )
    percentual_diferimento_uf: float | None = Field(
        default=None, alias="percentualDiferimentoUf", examples=[0]
    )
    percentual_diferimento_municipio: float | None = Field(
        default=None, alias="percentualDiferimentoMunicipio", examples=[0]
    )
    codigo_credito_presumido: str | None = Field(
        default=None, alias="codigoCreditoPresumido", examples=[""]
    )
    percentual_credito_presumido: float | None = Field(
        default=None, alias="percentualCreditoPresumido", examples=[0]
    )


class CalculosImpostosDadosBaseDTO(BlingModel):
    """OpenAPI schema ``CalculosImpostosDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        regra_operacao: Bling ``regraOperacao``; type ``CalculosImpostosRegraOperacaoDTO | None``; opcional.
        tributacao: Bling ``tributacao``; type ``int | None``; opcional. `1` Tributado <br> `2` Isento <br> `3` Outra situação
        cst: Bling ``cst``; type ``str | None``; opcional.
        aliquota: Bling ``aliquota``; type ``float | None``; opcional.
        base: Bling ``base``; type ``float | None``; opcional.
        valor_base_calculo: Bling ``valorBaseCalculo``; type ``float | None``; opcional.
        valor_imposto: Bling ``valorImposto``; type ``float | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        informacoes_adicionais_fisco: Bling ``informacoesAdicionaisFisco``; type ``str | None``; opcional."""

    regra_operacao: CalculosImpostosRegraOperacaoDTO | None = Field(
        default=None, alias="regraOperacao"
    )
    tributacao: int | None = Field(default=None, examples=[1])
    cst: str | None = Field(default=None, examples=["49"])
    aliquota: float | None = Field(default=None, examples=[0])
    base: float | None = Field(default=None, examples=[0])
    valor_base_calculo: float | None = Field(default=None, alias="valorBaseCalculo", examples=[0])
    valor_imposto: float | None = Field(default=None, alias="valorImposto", examples=[0])
    observacoes: str | None = Field(default=None, examples=[""])
    informacoes_adicionais_fisco: str | None = Field(
        default=None, alias="informacoesAdicionaisFisco", examples=[""]
    )


class CalculosImpostosIpiDTO(CalculosImpostosDadosBaseDTO):
    """OpenAPI schema ``CalculosImpostosIpiDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: CalculosImpostosDadosBaseDTO.

    Fields:
        regra_operacao: Bling ``regraOperacao``; type ``CalculosImpostosRegraOperacaoDTO | None``; opcional.
        tributacao: Bling ``tributacao``; type ``int | None``; opcional. `1` Tributado <br> `2` Isento <br> `3` Outra situação
        cst: Bling ``cst``; type ``str | None``; opcional.
        aliquota: Bling ``aliquota``; type ``float | None``; opcional.
        base: Bling ``base``; type ``float | None``; opcional.
        valor_base_calculo: Bling ``valorBaseCalculo``; type ``float | None``; opcional.
        valor_imposto: Bling ``valorImposto``; type ``float | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        informacoes_adicionais_fisco: Bling ``informacoesAdicionaisFisco``; type ``str | None``; opcional.
        valor_ipi_fixo_unitario: Bling ``valorIpiFixoUnitario``; type ``float | None``; opcional.
        classe_enquadramento_ipi: Bling ``classeEnquadramentoIpi``; type ``str | None``; opcional.
        codigo_enquadramento_ipi: Bling ``codigoEnquadramentoIpi``; type ``int | None``; opcional.
        codigo_selo: Bling ``codigoSelo``; type ``str | None``; opcional.
        codigo_ex_tipi: Bling ``codigoExTipi``; type ``int | None``; opcional."""

    valor_ipi_fixo_unitario: float | None = Field(
        default=None, alias="valorIpiFixoUnitario", examples=[0]
    )
    classe_enquadramento_ipi: str | None = Field(
        default=None, alias="classeEnquadramentoIpi", examples=[""]
    )
    codigo_enquadramento_ipi: int | None = Field(
        default=None, alias="codigoEnquadramentoIpi", examples=[0]
    )
    codigo_selo: str | None = Field(default=None, alias="codigoSelo", examples=[""])
    codigo_ex_tipi: int | None = Field(default=None, alias="codigoExTipi", examples=[0])


class CalculosImpostosIssqnDTO(CalculosImpostosDadosBaseDTO):
    """OpenAPI schema ``CalculosImpostosIssqnDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: CalculosImpostosDadosBaseDTO.

    Fields:
        regra_operacao: Bling ``regraOperacao``; type ``CalculosImpostosRegraOperacaoDTO | None``; opcional.
        tributacao: Bling ``tributacao``; type ``int | None``; opcional. `1` Tributado <br> `2` Isento <br> `3` Outra situação
        cst: Bling ``cst``; type ``str | None``; opcional.
        aliquota: Bling ``aliquota``; type ``float | None``; opcional.
        base: Bling ``base``; type ``float | None``; opcional.
        valor_base_calculo: Bling ``valorBaseCalculo``; type ``float | None``; opcional.
        valor_imposto: Bling ``valorImposto``; type ``float | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        informacoes_adicionais_fisco: Bling ``informacoesAdicionaisFisco``; type ``str | None``; opcional.
        codigo_lista_servicos: Bling ``codigoListaServicos``; type ``str | None``; opcional.
        descontar_iss_total_nota: Bling ``descontarIssTotalNota``; type ``bool | None``; opcional.
        reter_iss: Bling ``reterIss``; type ``bool | None``; opcional."""

    codigo_lista_servicos: str | None = Field(
        default=None, alias="codigoListaServicos", examples=["01.04"]
    )
    descontar_iss_total_nota: bool | None = Field(
        default=None, alias="descontarIssTotalNota", examples=[False]
    )
    reter_iss: bool | None = Field(default=None, alias="reterIss", examples=[False])


class CalculosImpostosLojaDTO(BlingModel):
    """OpenAPI schema ``CalculosImpostosLojaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        unidade_negocio: Bling ``unidadeNegocio``; type ``CalculosImpostosUnidadeNegocioDTO | None``; opcional."""

    id: int = Field(..., examples=[12345678])
    unidade_negocio: CalculosImpostosUnidadeNegocioDTO | None = Field(
        default=None, alias="unidadeNegocio"
    )


class CalculosImpostosPisDTO(CalculosImpostosDadosBaseDTO):
    """OpenAPI schema ``CalculosImpostosPisDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: CalculosImpostosDadosBaseDTO.

    Fields:
        regra_operacao: Bling ``regraOperacao``; type ``CalculosImpostosRegraOperacaoDTO | None``; opcional.
        tributacao: Bling ``tributacao``; type ``int | None``; opcional. `1` Tributado <br> `2` Isento <br> `3` Outra situação
        cst: Bling ``cst``; type ``str | None``; opcional.
        aliquota: Bling ``aliquota``; type ``float | None``; opcional.
        base: Bling ``base``; type ``float | None``; opcional.
        valor_base_calculo: Bling ``valorBaseCalculo``; type ``float | None``; opcional.
        valor_imposto: Bling ``valorImposto``; type ``float | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        informacoes_adicionais_fisco: Bling ``informacoesAdicionaisFisco``; type ``str | None``; opcional.
        valor_pis_fixo: Bling ``valorPisFixo``; type ``float | None``; opcional."""

    valor_pis_fixo: float | None = Field(default=None, alias="valorPisFixo", examples=[0])


class CalculosImpostosSimplesDTO(CalculosImpostosDadosBaseDTO):
    """OpenAPI schema ``CalculosImpostosSimplesDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: CalculosImpostosDadosBaseDTO.

    Fields:
        regra_operacao: Bling ``regraOperacao``; type ``CalculosImpostosRegraOperacaoDTO | None``; opcional.
        tributacao: Bling ``tributacao``; type ``int | None``; opcional. `1` Tributado <br> `2` Isento <br> `3` Outra situação
        cst: Bling ``cst``; type ``str | None``; opcional.
        aliquota: Bling ``aliquota``; type ``float | None``; opcional.
        base: Bling ``base``; type ``float | None``; opcional.
        valor_base_calculo: Bling ``valorBaseCalculo``; type ``float | None``; opcional.
        valor_imposto: Bling ``valorImposto``; type ``float | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        informacoes_adicionais_fisco: Bling ``informacoesAdicionaisFisco``; type ``str | None``; opcional.
        base_diferimento: Bling ``baseDiferimento``; type ``float | None``; opcional.
        modalidade_base_calculo: Bling ``modalidadeBaseCalculo``; type ``int | None``; opcional.
        valor_pauta: Bling ``valorPauta``; type ``float | None``; opcional.
        valor_imposto_st: Bling ``valorImpostoSt``; type ``float | None``; opcional.
        valor_base_calculo_st: Bling ``valorBaseCalculoSt``; type ``float | None``; opcional.
        base_calculo_st: Bling ``baseCalculoSt``; type ``float | None``; opcional.
        percentual_adicionado_st: Bling ``percentualAdicionadoSt``; type ``float | None``; opcional.
        modalidade_base_calculo_st: Bling ``modalidadeBaseCalculoSt``; type ``float | None``; opcional.
        valor_pauta_st: Bling ``valorPautaSt``; type ``float | None``; opcional.
        aliquota_st: Bling ``aliquotaSt``; type ``float | None``; opcional.
        aliquota_st_retido: Bling ``aliquotaStRetido``; type ``float | None``; opcional.
        base_st_retido: Bling ``baseStRetido``; type ``float | None``; opcional.
        valor_unitario_base_cst_retencao: Bling ``valorUnitarioBaseCstRetencao``; type ``float | None``; opcional.
        valor_unitario_icms_st_retencao: Bling ``valorUnitarioIcmsStRetencao``; type ``float | None``; opcional.
        valor_unitario_icms_substituto: Bling ``valorUnitarioIcmsSubstituto``; type ``float | None``; opcional."""

    base_diferimento: float | None = Field(default=None, alias="baseDiferimento", examples=[0])
    modalidade_base_calculo: int | None = Field(
        default=None, alias="modalidadeBaseCalculo", examples=[0]
    )
    valor_pauta: float | None = Field(default=None, alias="valorPauta", examples=[0])
    valor_imposto_st: float | None = Field(default=None, alias="valorImpostoSt", examples=[0])
    valor_base_calculo_st: float | None = Field(
        default=None, alias="valorBaseCalculoSt", examples=[0]
    )
    base_calculo_st: float | None = Field(default=None, alias="baseCalculoSt", examples=[0])
    percentual_adicionado_st: float | None = Field(
        default=None, alias="percentualAdicionadoSt", examples=[0]
    )
    modalidade_base_calculo_st: float | None = Field(
        default=None, alias="modalidadeBaseCalculoSt", examples=[0]
    )
    valor_pauta_st: float | None = Field(default=None, alias="valorPautaSt", examples=[0])
    aliquota_st: float | None = Field(default=None, alias="aliquotaSt", examples=[0])
    aliquota_st_retido: float | None = Field(default=None, alias="aliquotaStRetido", examples=[0])
    base_st_retido: float | None = Field(default=None, alias="baseStRetido", examples=[0])
    valor_unitario_base_cst_retencao: float | None = Field(
        default=None, alias="valorUnitarioBaseCstRetencao", examples=[0]
    )
    valor_unitario_icms_st_retencao: float | None = Field(
        default=None, alias="valorUnitarioIcmsStRetencao", examples=[0]
    )
    valor_unitario_icms_substituto: float | None = Field(
        default=None, alias="valorUnitarioIcmsSubstituto", examples=[0]
    )


class CalculosImpostosCalculoDTO(BlingModel):
    """OpenAPI schema ``CalculosImpostosCalculoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        tipo_nota: Bling ``tipoNota``; type ``int``; obrigatório. `0` Entrada <br> `1` Saída
        uf: Bling ``uf``; type ``str``; obrigatório. UF do destinatário
        municipio: Bling ``municipio``; type ``CalculosImpostosMunicipioDTO``; obrigatório.
        obter_regras: Bling ``obterRegras``; type ``bool | None``; opcional. Se false, os valores das regras de tributação de cada imposto serão zerados (cst, alíquota, base, etc.)
        crt: Bling ``crt``; type ``int | None``; opcional. CRT da empresa <br> `1` Simples Nacional <br> `2` Simples Nacional - excesso de sublimite de receita bruta <br> `3` Regime Normal <br> `4` MEI
        loja: Bling ``loja``; type ``CalculosImpostosLojaDTO``; obrigatório.
        produto: Bling ``produto``; type ``CalculosImpostosProdutoDTO``; obrigatório."""

    tipo_nota: int = Field(..., alias="tipoNota", examples=[1])
    uf: str = Field(..., examples=["RS"])
    municipio: CalculosImpostosMunicipioDTO
    obter_regras: bool | None = Field(default=True, alias="obterRegras", examples=[True])
    crt: int | None = Field(default=None, examples=[1])
    loja: CalculosImpostosLojaDTO
    produto: CalculosImpostosProdutoDTO


class CalculosImpostosCofinsDTO(CalculosImpostosDadosBaseDTO):
    """OpenAPI schema ``CalculosImpostosCofinsDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: CalculosImpostosDadosBaseDTO.

    Fields:
        regra_operacao: Bling ``regraOperacao``; type ``CalculosImpostosRegraOperacaoDTO | None``; opcional.
        tributacao: Bling ``tributacao``; type ``int | None``; opcional. `1` Tributado <br> `2` Isento <br> `3` Outra situação
        cst: Bling ``cst``; type ``str | None``; opcional.
        aliquota: Bling ``aliquota``; type ``float | None``; opcional.
        base: Bling ``base``; type ``float | None``; opcional.
        valor_base_calculo: Bling ``valorBaseCalculo``; type ``float | None``; opcional.
        valor_imposto: Bling ``valorImposto``; type ``float | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        informacoes_adicionais_fisco: Bling ``informacoesAdicionaisFisco``; type ``str | None``; opcional.
        valor_cofins_fixo: Bling ``valorCofinsFixo``; type ``float | None``; opcional."""

    valor_cofins_fixo: float | None = Field(default=None, alias="valorCofinsFixo", examples=[0])


class CalculosImpostosIcmsDTO(CalculosImpostosDadosBaseDTO):
    """OpenAPI schema ``CalculosImpostosIcmsDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: CalculosImpostosDadosBaseDTO.

    Fields:
        regra_operacao: Bling ``regraOperacao``; type ``CalculosImpostosRegraOperacaoDTO | None``; opcional.
        tributacao: Bling ``tributacao``; type ``int | None``; opcional. `1` Tributado <br> `2` Isento <br> `3` Outra situação
        cst: Bling ``cst``; type ``str | None``; opcional.
        aliquota: Bling ``aliquota``; type ``float | None``; opcional.
        base: Bling ``base``; type ``float | None``; opcional.
        valor_base_calculo: Bling ``valorBaseCalculo``; type ``float | None``; opcional.
        valor_imposto: Bling ``valorImposto``; type ``float | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        informacoes_adicionais_fisco: Bling ``informacoesAdicionaisFisco``; type ``str | None``; opcional.
        porcentagem_fcp_difal: Bling ``porcentagemFcpDifal``; type ``float | None``; opcional.
        valor_fcp_difal: Bling ``valorFcpDifal``; type ``float | None``; opcional.
        valor_fcp_efetivo: Bling ``valorFcpEfetivo``; type ``float | None``; opcional.
        porcentagem_fcp: Bling ``porcentagemFcp``; type ``float | None``; opcional.
        porcentagem_fcp_uf_destino: Bling ``porcentagemFcpUfDestino``; type ``float | None``; opcional.
        modalidade_base_calculo: Bling ``modalidadeBaseCalculo``; type ``float | None``; opcional.
        valor_pauta: Bling ``valorPauta``; type ``float | None``; opcional.
        aliquota_presumido: Bling ``aliquotaPresumido``; type ``float | None``; opcional.
        porcentagem_base_calculo_uf_destino: Bling ``porcentagemBaseCalculoUfDestino``; type ``float | None``; opcional.
        porcentagem_icms_uf_destino: Bling ``porcentagemIcmsUfDestino``; type ``float | None``; opcional.
        tipo_partilha: Bling ``tipoPartilha``; type ``int | None``; opcional. `0` Isento <br> `1` Normal
        valor_icms_desonerado: Bling ``valorIcmsDesonerado``; type ``float | None``; opcional.
        motivo_desoneracao_icms: Bling ``motivoDesoneracaoIcms``; type ``int | None``; opcional. `0` Nenhum <br> `1` Táxi <br> `3` Produtor Agropecuário <br> `4` Frotista/Locadora <br> `5` Diplomático/Consular <br> `6` Utilitários e Motocicletas da Amazônia Ocidental e Áreas...
        base_diferimento: Bling ``baseDiferimento``; type ``float | None``; opcional.
        valor_base_diferimento: Bling ``valorBaseDiferimento``; type ``float | None``; opcional.
        valor_presumido: Bling ``valorPresumido``; type ``float | None``; opcional.
        aliquota_posicao: Bling ``aliquotaPosicao``; type ``float | None``; opcional."""

    porcentagem_fcp_difal: float | None = Field(
        default=None, alias="porcentagemFcpDifal", examples=[0]
    )
    valor_fcp_difal: float | None = Field(default=None, alias="valorFcpDifal", examples=[0])
    valor_fcp_efetivo: float | None = Field(default=None, alias="valorFcpEfetivo", examples=[0])
    porcentagem_fcp: float | None = Field(default=None, alias="porcentagemFcp", examples=[0])
    porcentagem_fcp_uf_destino: float | None = Field(
        default=None, alias="porcentagemFcpUfDestino", examples=[0]
    )
    modalidade_base_calculo: float | None = Field(
        default=None, alias="modalidadeBaseCalculo", examples=[0]
    )
    valor_pauta: float | None = Field(default=None, alias="valorPauta", examples=[0])
    aliquota_presumido: float | None = Field(default=None, alias="aliquotaPresumido", examples=[0])
    porcentagem_base_calculo_uf_destino: float | None = Field(
        default=None, alias="porcentagemBaseCalculoUfDestino", examples=[0]
    )
    porcentagem_icms_uf_destino: float | None = Field(
        default=None, alias="porcentagemIcmsUfDestino", examples=[0]
    )
    tipo_partilha: int | None = Field(default=None, alias="tipoPartilha", examples=[0])
    valor_icms_desonerado: float | None = Field(
        default=None, alias="valorIcmsDesonerado", examples=[0]
    )
    motivo_desoneracao_icms: int | None = Field(
        default=None, alias="motivoDesoneracaoIcms", examples=[0]
    )
    base_diferimento: float | None = Field(default=None, alias="baseDiferimento", examples=[0])
    valor_base_diferimento: float | None = Field(
        default=None, alias="valorBaseDiferimento", examples=[0]
    )
    valor_presumido: float | None = Field(default=None, alias="valorPresumido", examples=[0])
    aliquota_posicao: float | None = Field(default=None, alias="aliquotaPosicao", examples=[0])


class CalculosImpostosIcmsStDTO(CalculosImpostosDadosBaseDTO):
    """OpenAPI schema ``CalculosImpostosIcmsStDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: CalculosImpostosDadosBaseDTO.

    Fields:
        regra_operacao: Bling ``regraOperacao``; type ``CalculosImpostosRegraOperacaoDTO | None``; opcional.
        tributacao: Bling ``tributacao``; type ``int | None``; opcional. `1` Tributado <br> `2` Isento <br> `3` Outra situação
        cst: Bling ``cst``; type ``str | None``; opcional.
        aliquota: Bling ``aliquota``; type ``float | None``; opcional.
        base: Bling ``base``; type ``float | None``; opcional.
        valor_base_calculo: Bling ``valorBaseCalculo``; type ``float | None``; opcional.
        valor_imposto: Bling ``valorImposto``; type ``float | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        informacoes_adicionais_fisco: Bling ``informacoesAdicionaisFisco``; type ``str | None``; opcional.
        percentual_adicionado: Bling ``percentualAdicionado``; type ``float | None``; opcional.
        modalidade_base_calculo: Bling ``modalidadeBaseCalculo``; type ``int | None``; opcional. `0` Margem Valor Agregado (%) <br> `1` Pauta (valor), <br> `2` Preço Tabelado Máximo (valor) <br> `3` Valor da operação
        valor_pauta: Bling ``valorPauta``; type ``float | None``; opcional."""

    percentual_adicionado: float | None = Field(
        default=None, alias="percentualAdicionado", examples=[0]
    )
    modalidade_base_calculo: int | None = Field(
        default=None, alias="modalidadeBaseCalculo", examples=[0]
    )
    valor_pauta: float | None = Field(default=None, alias="valorPauta", examples=[0])


class CalculosImpostosDadosDTO(BlingModel):
    """OpenAPI schema ``CalculosImpostosDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        faturada: Bling ``faturada``; type ``bool | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        pis_cofins_presumido: Bling ``pisCofinsPresumido``; type ``bool | None``; opcional.
        soma_impostos_total: Bling ``somaImpostosTotal``; type ``bool | None``; opcional.
        soma_icms_total: Bling ``somaIcmsTotal``; type ``bool | None``; opcional.
        aliquota_funrural: Bling ``aliquotaFunrural``; type ``float | None``; opcional.
        desconta_funrural: Bling ``descontaFunrural``; type ``bool | None``; opcional.
        consumidor_final: Bling ``consumidorFinal``; type ``bool | None``; opcional.
        ret_imposto_retido: Bling ``retImpostoRetido``; type ``bool | None``; opcional.
        ret_aliquota_ir: Bling ``retAliquotaIr``; type ``float | None``; opcional.
        ret_valor_ir: Bling ``retValorIr``; type ``float | None``; opcional.
        ret_aliquota_csll: Bling ``retAliquotaCsll``; type ``float | None``; opcional.
        ret_valor_csll: Bling ``retValorCsll``; type ``float | None``; opcional.
        desconto_condicional: Bling ``descontoCondicional``; type ``bool | None``; opcional.
        base_comissao: Bling ``baseComissao``; type ``float | None``; opcional.
        icms: Bling ``icms``; type ``CalculosImpostosIcmsDTO | None``; opcional.
        valor_pmc: Bling ``valorPmc``; type ``float | None``; opcional.
        aliquota_valor_aprox_impostos: Bling ``aliquotaValorAproxImpostos``; type ``float | None``; opcional.
        informacoes_adicionais_fisco: Bling ``informacoesAdicionaisFisco``; type ``str | None``; opcional.
        incluir_frete_ipi: Bling ``incluirFreteIpi``; type ``bool | None``; opcional.
        simples: Bling ``simples``; type ``CalculosImpostosSimplesDTO | None``; opcional.
        ipi: Bling ``ipi``; type ``CalculosImpostosIpiDTO | None``; opcional.
        issqn: Bling ``issqn``; type ``CalculosImpostosIssqnDTO | None``; opcional.
        pis: Bling ``pis``; type ``CalculosImpostosPisDTO | None``; opcional.
        cofins: Bling ``cofins``; type ``CalculosImpostosCofinsDTO | None``; opcional.
        icms_st: Bling ``icmsSt``; type ``CalculosImpostosIcmsStDTO | None``; opcional.
        pis_st: Bling ``pisSt``; type ``CalculosImpostosDadosBaseDTO | None``; opcional.
        cofins_st: Bling ``cofinsSt``; type ``CalculosImpostosDadosBaseDTO | None``; opcional.
        ii: Bling ``ii``; type ``CalculosImpostosDadosBaseDTO | None``; opcional.
        codigo_beneficio_fiscal: Bling ``codigoBeneficioFiscal``; type ``str | None``; opcional.
        porcentagem_fcp: Bling ``porcentagemFcp``; type ``float | None``; opcional.
        cfop: Bling ``cfop``; type ``int | None``; opcional.
        simples_st: Bling ``simplesSt``; type ``CalculosImpostosDadosBaseDTO | None``; opcional.
        ibs_cbs: Bling ``ibsCbs``; type ``CalculosImpostosIbsCbsDTO | None``; opcional.
        ibs: Bling ``ibs``; type ``CalculosImpostosIbsDTO | None``; opcional.
        cbs: Bling ``cbs``; type ``CalculosImpostosCbsDTO | None``; opcional.
        ibs_cbs_reg: Bling ``ibsCbsReg``; type ``CalculosImpostosIbsCbsRegDTO | None``; opcional."""

    faturada: bool | None = Field(default=None, examples=[False])
    observacoes: str | None = Field(
        default=None, examples=["Total aproximado de tributos: R$ [APROX_TRIB]. Fonte IBPT."]
    )
    pis_cofins_presumido: bool | None = Field(
        default=None, alias="pisCofinsPresumido", examples=[False]
    )
    soma_impostos_total: bool | None = Field(
        default=None, alias="somaImpostosTotal", examples=[False]
    )
    soma_icms_total: bool | None = Field(default=None, alias="somaIcmsTotal", examples=[False])
    aliquota_funrural: float | None = Field(default=None, alias="aliquotaFunrural", examples=[0])
    desconta_funrural: bool | None = Field(default=None, alias="descontaFunrural", examples=[False])
    consumidor_final: bool | None = Field(default=None, alias="consumidorFinal", examples=[False])
    ret_imposto_retido: bool | None = Field(
        default=None, alias="retImpostoRetido", examples=[False]
    )
    ret_aliquota_ir: float | None = Field(default=None, alias="retAliquotaIr", examples=[0])
    ret_valor_ir: float | None = Field(default=None, alias="retValorIr", examples=[0])
    ret_aliquota_csll: float | None = Field(default=None, alias="retAliquotaCsll", examples=[0])
    ret_valor_csll: float | None = Field(default=None, alias="retValorCsll", examples=[0])
    desconto_condicional: bool | None = Field(
        default=None, alias="descontoCondicional", examples=[False]
    )
    base_comissao: float | None = Field(default=None, alias="baseComissao", examples=[0])
    icms: CalculosImpostosIcmsDTO | None = None
    valor_pmc: float | None = Field(default=None, alias="valorPmc", examples=[0])
    aliquota_valor_aprox_impostos: float | None = Field(
        default=None, alias="aliquotaValorAproxImpostos", examples=[0]
    )
    informacoes_adicionais_fisco: str | None = Field(
        default=None, alias="informacoesAdicionaisFisco", examples=[""]
    )
    incluir_frete_ipi: bool | None = Field(default=None, alias="incluirFreteIpi", examples=[False])
    simples: CalculosImpostosSimplesDTO | None = None
    ipi: CalculosImpostosIpiDTO | None = None
    issqn: CalculosImpostosIssqnDTO | None = None
    pis: CalculosImpostosPisDTO | None = None
    cofins: CalculosImpostosCofinsDTO | None = None
    icms_st: CalculosImpostosIcmsStDTO | None = Field(default=None, alias="icmsSt")
    pis_st: CalculosImpostosDadosBaseDTO | None = Field(default=None, alias="pisSt")
    cofins_st: CalculosImpostosDadosBaseDTO | None = Field(default=None, alias="cofinsSt")
    ii: CalculosImpostosDadosBaseDTO | None = None
    codigo_beneficio_fiscal: str | None = Field(
        default=None, alias="codigoBeneficioFiscal", examples=[""]
    )
    porcentagem_fcp: float | None = Field(default=None, alias="porcentagemFcp", examples=[0])
    cfop: int | None = Field(default=None, examples=[0])
    simples_st: CalculosImpostosDadosBaseDTO | None = Field(default=None, alias="simplesSt")
    ibs_cbs: CalculosImpostosIbsCbsDTO | None = Field(default=None, alias="ibsCbs")
    ibs: CalculosImpostosIbsDTO | None = None
    cbs: CalculosImpostosCbsDTO | None = None
    ibs_cbs_reg: CalculosImpostosIbsCbsRegDTO | None = Field(default=None, alias="ibsCbsReg")


__all__ = [
    "CalculosImpostosCalculoDTO",
    "CalculosImpostosCbsDTO",
    "CalculosImpostosCofinsDTO",
    "CalculosImpostosDadosBaseDTO",
    "CalculosImpostosDadosDTO",
    "CalculosImpostosIbsCbsDTO",
    "CalculosImpostosIbsCbsRegDTO",
    "CalculosImpostosIbsDTO",
    "CalculosImpostosIcmsDTO",
    "CalculosImpostosIcmsStDTO",
    "CalculosImpostosIpiDTO",
    "CalculosImpostosIssqnDTO",
    "CalculosImpostosLojaDTO",
    "CalculosImpostosMunicipioDTO",
    "CalculosImpostosPisDTO",
    "CalculosImpostosProdutoDTO",
    "CalculosImpostosRegraOperacaoDTO",
    "CalculosImpostosSimplesDTO",
    "CalculosImpostosUnidadeNegocioDTO",
]
