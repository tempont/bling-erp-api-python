# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``notas_servicos``. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.models.fields import BlingDate
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import Contato, Data21, Data22


class NotasServicosCancelamentoDTO(BlingModel):
    """OpenAPI schema ``NotasServicosCancelamentoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        codigo_motivo: Bling ``codigoMotivo``; type ``int | None``; opcional. `1` Erro na Emissão<br> `2` Serviço não Prestado<br>`9` Outros
        justificativa: Bling ``justificativa``; type ``str | None``; opcional. Justificativa do cancelamento."""

    codigo_motivo: int | None = Field(
        default=None,
        validation_alias=AliasChoices("codigo_motivo", "codigoMotivo"),
        examples=[1],
        serialization_alias="codigoMotivo",
    )
    justificativa: str | None = Field(default=None, examples=["Cancelamento de NFS-e"])


class NotasServicosContatoEnderecoDTO(BlingModel):
    """OpenAPI schema ``NotasServicosContatoEnderecoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        endereco: Bling ``endereco``; type ``str | None``; opcional.
        numero: Bling ``numero``; type ``str | None``; opcional.
        complemento: Bling ``complemento``; type ``str | None``; opcional.
        bairro: Bling ``bairro``; type ``str``; obrigatório.
        cep: Bling ``cep``; type ``str | None``; opcional.
        municipio: Bling ``municipio``; type ``str``; obrigatório.
        uf: Bling ``uf``; type ``str | None``; opcional."""

    endereco: str | None = Field(default=None, examples=["Olavo Bilac"])
    numero: str | None = Field(default=None, examples=["914"])
    complemento: str | None = Field(default=None, examples=["Sala 101"])
    bairro: str = Field(..., examples=["Imigrante"])
    cep: str | None = Field(default=None, examples=["95702-000"])
    municipio: str = Field(..., examples=["Bento Gonçalves"])
    uf: str | None = Field(default=None, examples=["RS"])


class NotasServicosDadosBase(BlingModel):
    """OpenAPI schema ``NotasServicosDadosBase``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        numero: Bling ``numero``; type ``str | None``; opcional.
        numero_rps: Bling ``numeroRPS``; type ``str``; obrigatório.
        serie: Bling ``serie``; type ``str``; obrigatório.
        situacao: Bling ``situacao``; type ``int | None``; opcional. `0` Pendente <br> `1` Emitida <br> `2` Disponível para consulta <br> `3` Cancelada
        data_emissao: Bling ``dataEmissao``; type ``BlingDate | None``; opcional.
        valor: Bling ``valor``; type ``float | None``; opcional."""

    id: int = Field(..., examples=[12345678])
    numero: str | None = Field(default=None, examples=["123"])
    numero_rps: str = Field(
        ...,
        validation_alias=AliasChoices("numero_rps", "numeroRPS"),
        examples=["32"],
        serialization_alias="numeroRPS",
    )
    serie: str = Field(..., examples=["1"])
    situacao: int | None = Field(default=None, examples=[0])
    data_emissao: BlingDate | None = Field(
        default=None,
        validation_alias=AliasChoices("data_emissao", "dataEmissao"),
        examples=["2023-01-12"],
        serialization_alias="dataEmissao",
    )
    valor: float | None = Field(default=None, examples=[100])


class NotasServicosDados(BlingModel):
    """OpenAPI schema ``NotasServicosDados``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        link: Bling ``link``; type ``str | None``; opcional. Link para acesso e impressão da NFS-e.
        codigo_verificacao: Bling ``codigoVerificacao``; type ``str | None``; opcional."""

    link: str | None = Field(default=None, examples=["https://linkexemplo.com.br/nfse"])
    codigo_verificacao: str | None = Field(
        default=None,
        validation_alias=AliasChoices("codigo_verificacao", "codigoVerificacao"),
        serialization_alias="codigoVerificacao",
    )


class NotasServicosDadosDTO(NotasServicosDados):
    """OpenAPI schema ``NotasServicosDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: NotasServicosDados.

    Fields:
        link: Bling ``link``; type ``str | None``; opcional. Link para acesso e impressão da NFS-e.
        codigo_verificacao: Bling ``codigoVerificacao``; type ``str | None``; opcional."""

    pass


class NotasServicosContatoBaseDTO(BlingModel):
    """OpenAPI schema ``NotasServicosContatoBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        nome: Bling ``nome``; type ``str``; obrigatório.
        numero_documento: Bling ``numeroDocumento``; type ``str``; obrigatório. CNPJ ou CPF.
        email: Bling ``email``; type ``str``; obrigatório."""

    id: int = Field(..., examples=[12345678])
    nome: str = Field(..., examples=["Pedro Silva"])
    numero_documento: str = Field(
        ...,
        validation_alias=AliasChoices("numero_documento", "numeroDocumento"),
        examples=["30188025000121"],
        serialization_alias="numeroDocumento",
    )
    email: str = Field(..., examples=["pedrosilva@bling.com.br"])


class NotasServicosParcelaFormaPagamentoDTO(BlingModel):
    """OpenAPI schema ``NotasServicosParcelaFormaPagamentoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class NotasServicosServicoDTO(BlingModel):
    """OpenAPI schema ``NotasServicosServicoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        codigo: Bling ``codigo``; type ``str``; obrigatório.
        descricao: Bling ``descricao``; type ``str``; obrigatório.
        valor: Bling ``valor``; type ``float``; obrigatório."""

    codigo: str = Field(..., examples=["10301"])
    descricao: str = Field(..., examples=["Pintura"])
    valor: float = Field(..., examples=[100.25])


class NotasServicosTributacaoIbsCbsValoresDTO(BlingModel):
    """OpenAPI schema ``NotasServicosTributacaoIbsCbsValoresDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        codigo_situacao_tributaria: Bling ``codigoSituacaoTributaria``; type ``str``; obrigatório. Código de Situação Tributária (CST) com 3 dígitos. Define o regime de tributação da operação. Exemplos: '000' = Tributação integral, '200' = Alíquota reduzida, '410' = Imunidade,...
        classificacao_tributaria: Bling ``classificacaoTributaria``; type ``str``; obrigatório. Código da Classificação Tributária com 6 dígitos. Define a situação específica dentro do CST informado. Cada CST possui suas próprias classificações tributárias válidas. Exemplos:...
        codigo_credito_presumido: Bling ``codigoCreditoPresumido``; type ``str | None``; opcional. Código do crédito presumido (2 dígitos). Informe APENAS quando a classificação tributária conceder direito a crédito presumido. Consulte sua contabilidade para verificar se sua op...
        cst_regime_regular: Bling ``cstRegimeRegular``; type ``str | None``; opcional. CST aplicável ao regime regular de tributação (3 dígitos). Utilize quando a operação estiver em regime especial mas precisa informar a situação no regime regular. Consulte sua con...
        classificacao_tributaria_regular: Bling ``classificacaoTributariaRegular``; type ``str | None``; opcional. Classificação tributária para o regime regular (6 dígitos). Deve ser compatível com o 'cstRegimeRegular' informado. Consulte sua contabilidade para o código correto.
        percentual_diferimento_estadual: Bling ``percentualDiferimentoEstadual``; type ``float | None``; opcional. Percentual de diferimento do IBS estadual (parcela UF), de 0.00 a 100.00. O diferimento posterga o pagamento do imposto para etapa posterior da cadeia. Consulte sua contabilidade...
        percentual_diferimento_municipal: Bling ``percentualDiferimentoMunicipal``; type ``float | None``; opcional. Percentual de diferimento do IBS municipal, de 0.00 a 100.00. Aplica-se à parcela municipal do imposto sobre bens e serviços. Consulte sua contabilidade para verificar se há difer...
        percentual_diferimento_cbs: Bling ``percentualDiferimentoCBS``; type ``float | None``; opcional. Percentual de diferimento da Contribuição sobre Bens e Serviços (CBS), de 0.00 a 100.00. A CBS é o tributo federal da Reforma Tributária. Consulte sua contabilidade para verificar..."""

    codigo_situacao_tributaria: str = Field(
        ...,
        validation_alias=AliasChoices("codigo_situacao_tributaria", "codigoSituacaoTributaria"),
        examples=["000"],
        serialization_alias="codigoSituacaoTributaria",
    )
    classificacao_tributaria: str = Field(
        ...,
        validation_alias=AliasChoices("classificacao_tributaria", "classificacaoTributaria"),
        examples=["000001"],
        serialization_alias="classificacaoTributaria",
    )
    codigo_credito_presumido: str | None = Field(
        default=None,
        validation_alias=AliasChoices("codigo_credito_presumido", "codigoCreditoPresumido"),
        examples=["01"],
        serialization_alias="codigoCreditoPresumido",
    )
    cst_regime_regular: str | None = Field(
        default=None,
        validation_alias=AliasChoices("cst_regime_regular", "cstRegimeRegular"),
        examples=["550"],
        serialization_alias="cstRegimeRegular",
    )
    classificacao_tributaria_regular: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "classificacao_tributaria_regular", "classificacaoTributariaRegular"
        ),
        examples=["550016"],
        serialization_alias="classificacaoTributariaRegular",
    )
    percentual_diferimento_estadual: float | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "percentual_diferimento_estadual", "percentualDiferimentoEstadual"
        ),
        examples=[10],
        serialization_alias="percentualDiferimentoEstadual",
    )
    percentual_diferimento_municipal: float | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "percentual_diferimento_municipal", "percentualDiferimentoMunicipal"
        ),
        examples=[5],
        serialization_alias="percentualDiferimentoMunicipal",
    )
    percentual_diferimento_cbs: float | None = Field(
        default=None,
        validation_alias=AliasChoices("percentual_diferimento_cbs", "percentualDiferimentoCBS"),
        examples=[8],
        serialization_alias="percentualDiferimentoCBS",
    )


class NotasServicosVendedorDTO(BlingModel):
    """OpenAPI schema ``NotasServicosVendedorDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class NotasServicosResponsePOSTPUT(BlingModel):
    """OpenAPI schema ``NotasServicosResponsePOSTPUT``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        numero_rps: Bling ``numeroRPS``; type ``str``; obrigatório.
        serie: Bling ``serie``; type ``str``; obrigatório."""

    id: int = Field(..., examples=[12345678])
    numero_rps: str = Field(
        ...,
        validation_alias=AliasChoices("numero_rps", "numeroRPS"),
        examples=["123"],
        serialization_alias="numeroRPS",
    )
    serie: str = Field(..., examples=["1"])


class NfsePostResponse201(BlingModel):
    """OpenAPI schema ``NfsePostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data21 | None``; opcional."""

    data: Data21 | None = None


class NotasServicosContatoDTO(BlingModel):
    """OpenAPI schema ``NotasServicosContatoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        ie: Bling ``ie``; type ``str | None``; opcional. Inscrição estadual.
        telefone: Bling ``telefone``; type ``str | None``; opcional.
        im: Bling ``im``; type ``str | None``; opcional. Inscrição municipal.
        endereco: Bling ``endereco``; type ``NotasServicosContatoEnderecoDTO | None``; opcional."""

    ie: str | None = Field(default=None, examples=["949895756023"])
    telefone: str | None = Field(default=None, examples=["54 3771-7278"])
    im: str | None = Field(default=None, examples=["145780150"])
    endereco: NotasServicosContatoEnderecoDTO | None = None


class NotasServicosDadosBaseDTO(NotasServicosDadosBase):
    """OpenAPI schema ``NotasServicosDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: NotasServicosDadosBase.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        numero: Bling ``numero``; type ``str | None``; opcional.
        numero_rps: Bling ``numeroRPS``; type ``str``; obrigatório.
        serie: Bling ``serie``; type ``str``; obrigatório.
        situacao: Bling ``situacao``; type ``int | None``; opcional. `0` Pendente <br> `1` Emitida <br> `2` Disponível para consulta <br> `3` Cancelada
        data_emissao: Bling ``dataEmissao``; type ``date | None``; opcional.
        valor: Bling ``valor``; type ``float | None``; opcional.
        contato: Bling ``contato``; type ``NotasServicosContatoBaseDTO | None``; opcional."""

    contato: NotasServicosContatoBaseDTO | None = None


class NotasServicosDadosBaseDTOPOST(NotasServicosDadosBase):
    """OpenAPI schema ``NotasServicosDadosBaseDTOPOST``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: NotasServicosDadosBase.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        numero: Bling ``numero``; type ``str | None``; opcional.
        numero_rps: Bling ``numeroRPS``; type ``str``; obrigatório.
        serie: Bling ``serie``; type ``str``; obrigatório.
        situacao: Bling ``situacao``; type ``int | None``; opcional. `0` Pendente <br> `1` Emitida <br> `2` Disponível para consulta <br> `3` Cancelada
        data_emissao: Bling ``dataEmissao``; type ``date | None``; opcional.
        valor: Bling ``valor``; type ``float | None``; opcional.
        contato: Bling ``contato``; type ``Contato | None``; opcional."""

    contato: Contato | None = None


class NotasServicosParcelaDTO(BlingModel):
    """OpenAPI schema ``NotasServicosParcelaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``BlingDate``; obrigatório.
        valor: Bling ``valor``; type ``float``; obrigatório.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        forma_pagamento: Bling ``formaPagamento``; type ``NotasServicosParcelaFormaPagamentoDTO | None``; opcional."""

    data: BlingDate = Field(..., examples=["2023-01-12"])
    valor: float = Field(..., examples=[123.45])
    observacoes: str | None = Field(default=None, examples=["Observação da parcela"])
    forma_pagamento: NotasServicosParcelaFormaPagamentoDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("forma_pagamento", "formaPagamento"),
        serialization_alias="formaPagamento",
    )


class NotasServicosTributacaoIbsCbsDTO(BlingModel):
    """OpenAPI schema ``NotasServicosTributacaoIbsCbsDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        indicador_operacao: Bling ``indicadorOperacao``; type ``str``; obrigatório. Código que indica onde a operação será realizada (6 dígitos). Valores comuns: '100301' = Domicílio do adquirente, '100302' = Local da prestação do serviço, '100303' = Outro local...
        tipo_operacao: Bling ``tipoOperacao``; type ``str``; obrigatório. Tipo da operação tributável. Valores aceitos: '1' = Fornecimento de serviço (operação padrão onde o emitente é o prestador), '2' = Recebimento do pagamento (quando há intermediaçã...
        tipo_ente_governamental: Bling ``tipoEnteGovernamental``; type ``str | None``; opcional. Tipo de ente governamental tomador do serviço. Informe APENAS quando o cliente for órgão público. Valores aceitos: '1' = União (órgão federal), '2' = Estado (órgão estadual), '3'...
        tributacao: Bling ``tributacao``; type ``NotasServicosTributacaoIbsCbsValoresDTO``; obrigatório."""

    indicador_operacao: str = Field(
        ...,
        validation_alias=AliasChoices("indicador_operacao", "indicadorOperacao"),
        examples=["100301"],
        serialization_alias="indicadorOperacao",
    )
    tipo_operacao: str = Field(
        ...,
        validation_alias=AliasChoices("tipo_operacao", "tipoOperacao"),
        examples=["1"],
        serialization_alias="tipoOperacao",
    )
    tipo_ente_governamental: str | None = Field(
        default=None,
        validation_alias=AliasChoices("tipo_ente_governamental", "tipoEnteGovernamental"),
        examples=["4"],
        serialization_alias="tipoEnteGovernamental",
    )
    tributacao: NotasServicosTributacaoIbsCbsValoresDTO


class NfseGetResponse200(BlingModel):
    """OpenAPI schema ``NfseGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[NotasServicosDadosBaseDTO] | None``; opcional."""

    data: list[NotasServicosDadosBaseDTO] | None = None


class NfseIdNotaServicoGetResponse200(BlingModel):
    """OpenAPI schema ``NfseIdNotaServicoGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data22 | None``; opcional."""

    data: Data22 | None = None


class NfseIdNotaServicoEnviarPostResponse200(BlingModel):
    """OpenAPI schema ``NfseIdNotaServicoEnviarPostResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data22 | None``; opcional."""

    data: Data22 | None = None


class NotasServicosDadosDTOPOST(NotasServicosDados):
    """OpenAPI schema ``NotasServicosDadosDTOPOST``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: NotasServicosDados.

    Fields:
        link: Bling ``link``; type ``str | None``; opcional. Link para acesso e impressão da NFS-e.
        codigo_verificacao: Bling ``codigoVerificacao``; type ``str | None``; opcional.
        data: Bling ``data``; type ``BlingDate | None``; opcional. Utilizado no POST.
        base_calculo: Bling ``baseCalculo``; type ``float | None``; opcional.
        reter_iss: Bling ``reterISS``; type ``bool | None``; opcional. Utilizado no POST. Caso não seja informado, será levado em consideração o valor do parâmetro no sistema.
        desconto: Bling ``desconto``; type ``float | None``; opcional.
        vendedor: Bling ``vendedor``; type ``NotasServicosVendedorDTO | None``; opcional.
        servicos: Bling ``servicos``; type ``list[NotasServicosServicoDTO]``; obrigatório.
        parcelas: Bling ``parcelas``; type ``list[NotasServicosParcelaDTO] | None``; opcional.
        tributacao_ibs_cbs: Bling ``tributacaoIbsCbs``; type ``NotasServicosTributacaoIbsCbsDTO | None``; opcional."""

    data: BlingDate | None = Field(default=None, examples=["2023-01-12"])
    base_calculo: float | None = Field(
        default=None,
        validation_alias=AliasChoices("base_calculo", "baseCalculo"),
        examples=[100],
        serialization_alias="baseCalculo",
    )
    reter_iss: bool | None = Field(
        default=None,
        validation_alias=AliasChoices("reter_iss", "reterISS"),
        examples=[False],
        serialization_alias="reterISS",
    )
    desconto: float | None = Field(default=None, examples=[15.45])
    vendedor: NotasServicosVendedorDTO | None = None
    servicos: list[NotasServicosServicoDTO]
    parcelas: list[NotasServicosParcelaDTO] | None = None
    tributacao_ibs_cbs: NotasServicosTributacaoIbsCbsDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("tributacao_ibs_cbs", "tributacaoIbsCbs"),
        serialization_alias="tributacaoIbsCbs",
    )


class NfsePostRequest(NotasServicosDadosBaseDTOPOST, NotasServicosDadosDTOPOST):
    """OpenAPI schema ``NfsePostRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: NotasServicosDadosBaseDTOPOST, NotasServicosDadosDTOPOST.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        numero: Bling ``numero``; type ``str | None``; opcional.
        numero_rps: Bling ``numeroRPS``; type ``str``; obrigatório.
        serie: Bling ``serie``; type ``str``; obrigatório.
        situacao: Bling ``situacao``; type ``int | None``; opcional. `0` Pendente <br> `1` Emitida <br> `2` Disponível para consulta <br> `3` Cancelada
        data_emissao: Bling ``dataEmissao``; type ``date | None``; opcional.
        valor: Bling ``valor``; type ``float | None``; opcional.
        contato: Bling ``contato``; type ``Contato | None``; opcional.
        link: Bling ``link``; type ``str | None``; opcional. Link para acesso e impressão da NFS-e.
        codigo_verificacao: Bling ``codigoVerificacao``; type ``str | None``; opcional.
        data: Bling ``data``; type ``date | None``; opcional. Utilizado no POST.
        base_calculo: Bling ``baseCalculo``; type ``float | None``; opcional.
        reter_iss: Bling ``reterISS``; type ``bool | None``; opcional. Utilizado no POST. Caso não seja informado, será levado em consideração o valor do parâmetro no sistema.
        desconto: Bling ``desconto``; type ``float | None``; opcional.
        vendedor: Bling ``vendedor``; type ``NotasServicosVendedorDTO | None``; opcional.
        servicos: Bling ``servicos``; type ``list[NotasServicosServicoDTO]``; obrigatório.
        parcelas: Bling ``parcelas``; type ``list[NotasServicosParcelaDTO] | None``; opcional.
        tributacao_ibs_cbs: Bling ``tributacaoIbsCbs``; type ``NotasServicosTributacaoIbsCbsDTO | None``; opcional."""

    pass


__all__ = [
    "NfseGetResponse200",
    "NfseIdNotaServicoEnviarPostResponse200",
    "NfseIdNotaServicoGetResponse200",
    "NfsePostRequest",
    "NfsePostResponse201",
    "NotasServicosCancelamentoDTO",
    "NotasServicosContatoBaseDTO",
    "NotasServicosContatoDTO",
    "NotasServicosContatoEnderecoDTO",
    "NotasServicosDados",
    "NotasServicosDadosBase",
    "NotasServicosDadosBaseDTO",
    "NotasServicosDadosBaseDTOPOST",
    "NotasServicosDadosDTO",
    "NotasServicosDadosDTOPOST",
    "NotasServicosParcelaDTO",
    "NotasServicosParcelaFormaPagamentoDTO",
    "NotasServicosResponsePOSTPUT",
    "NotasServicosServicoDTO",
    "NotasServicosTributacaoIbsCbsDTO",
    "NotasServicosTributacaoIbsCbsValoresDTO",
    "NotasServicosVendedorDTO",
]
