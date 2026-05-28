# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``contas_receber``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

from .contas import ContasDadosBaseDTO

if TYPE_CHECKING:
    from .common import BasePostResponse, Bordero, Data7, Error1, FieldModel
    from .contas import ContasCategoriaDTO, ContasPortadorDTO


class ContasReceberAutenticacaoDTO(BlingModel):
    """OpenAPI schema ``ContasReceberAutenticacaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        tipo: Bling ``tipo``; type ``int``; obrigatório. Tipo de autenticação:<br>`1` Código de autenticação por dois fatores<br>`4` Senha de 6 dígitos do app Bling Conta
        codigo: Bling ``codigo``; type ``str``; obrigatório."""

    tipo: int = Field(..., examples=[1])
    codigo: str = Field(..., examples=["111111"])


class ContasReceberBoletosDadosDTO(BlingModel):
    """OpenAPI schema ``ContasReceberBoletosDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        numero_externo: Bling ``numeroExterno``; type ``str | None``; opcional. Código de identificação do boleto
        vencimento: Bling ``vencimento``; type ``str | None``; opcional.
        valor: Bling ``valor``; type ``float | None``; opcional.
        situacao: Bling ``situacao``; type ``int | None``; opcional. `1` Em aberto <br>`2` Recebido <br>`3` Parcialmente recebido <br>`4` Devolvido <br>`5` Parcialmente devolvido <br>`6` Cancelado"""

    id: int | None = Field(default=None, examples=[1328793273])
    numero_externo: str | None = Field(default=None, alias="numeroExterno", examples=["BWbXB"])
    vencimento: str | None = Field(default=None, examples=["2023-09-12"])
    valor: float | None = Field(default=None, examples=[111.2])
    situacao: int | None = Field(default=None, examples=[1])


class ContasReceberContaContabilDTO(BlingModel):
    """OpenAPI schema ``ContasReceberContaContabilDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        descricao: Bling ``descricao``; type ``str | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    descricao: str | None = Field(default=None, examples=["Contas a pagar"])


class ContasReceberContaDTO(BlingModel):
    """OpenAPI schema ``ContasReceberContaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. Para cancelar apenas uma conta, deve-se informar o ID da conta."""

    id: int = Field(..., examples=[6423836115])


class ContasReceberContatoDTO(BlingModel):
    """OpenAPI schema ``ContasReceberContatoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        nome: Bling ``nome``; type ``str | None``; opcional.
        numero_documento: Bling ``numeroDocumento``; type ``str | None``; opcional.
        tipo: Bling ``tipo``; type ``str | None``; opcional."""

    id: int = Field(..., examples=[12345678])
    nome: str | None = Field(default=None, examples=["Contato Teste"])
    numero_documento: str | None = Field(
        default=None, alias="numeroDocumento", examples=["12345678910"]
    )
    tipo: str | None = Field(default=None, examples=["F"])


class ContasReceberDadosOrigemDTO(BlingModel):
    """OpenAPI schema ``ContasReceberDadosOrigemDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        tipo_origem: Bling ``tipoOrigem``; type ``str | None``; opcional.
        numero: Bling ``numero``; type ``str | None``; opcional.
        data_emissao: Bling ``dataEmissao``; type ``str | None``; opcional.
        valor: Bling ``valor``; type ``float | None``; opcional.
        situacao: Bling ``situacao``; type ``int | None``; opcional. Situações da nota fiscal: <br> `1` Pendente: Situação inicial. <br> `3` Cancelada: Nota foi emitida e posteriormente cancelada. <br> `4` Aguardando recibo: Quando há uma tentativa...
        url: Bling ``url``; type ``str | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    tipo_origem: str | None = Field(default=None, alias="tipoOrigem", examples=["venda"])
    numero: str | None = Field(default=None, examples=["0921132"])
    data_emissao: str | None = Field(default=None, alias="dataEmissao", examples=["2023-07-05"])
    valor: float | None = Field(default=None, examples=[45.76])
    situacao: int | None = Field(default=None, examples=[1])
    url: str | None = Field(
        default=None, examples=["doc.view.php?id=9ab1671b3f05765cb49fee83ee0f2496"]
    )


class ContasReceberFormaPagamentoDTO(BlingModel):
    """OpenAPI schema ``ContasReceberFormaPagamentoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        codigo_fiscal: Bling ``codigoFiscal``; type ``int | None``; opcional. `1` Dinheiro <br> `2` Cheque <br> `3` Cartão de crédito <br> `4` Cartão de débito <br> `5` Crédito loja <br> `10` Vale alimentação <br> `11` Vale refeição <br> `12` Vale presente..."""

    id: int = Field(..., examples=[12345678])
    codigo_fiscal: int | None = Field(default=None, alias="codigoFiscal", examples=[15])


class ContasReceberNotaFiscalDTO(BlingModel):
    """OpenAPI schema ``ContasReceberNotaFiscalDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        numero: Bling ``numero``; type ``str``; obrigatório."""

    numero: str = Field(..., examples=["000001"])


class ContasReceberOcorrenciaUnicaDTO(BlingModel):
    """OpenAPI schema ``ContasReceberOcorrenciaUnicaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        tipo: Bling ``tipo``; type ``int``; obrigatório. `1` Única<br> Ignorado no método PUT"""

    tipo: int = Field(..., examples=[1])


class ContasReceberOcorrenciaParceladaDTO(BlingModel):
    """OpenAPI schema ``ContasReceberOcorrenciaParceladaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        tipo: Bling ``tipo``; type ``int``; obrigatório. `2` Parcelada<br> Ignorado no método PUT
        considerar_dias_uteis: Bling ``considerarDiasUteis``; type ``bool | None``; opcional. Ignorado no método PUT
        dia_vencimento: Bling ``diaVencimento``; type ``int``; obrigatório.
        numero_parcelas: Bling ``numeroParcelas``; type ``int | None``; opcional. Ignorado no método PUT"""

    tipo: int = Field(..., examples=[2])
    considerar_dias_uteis: bool | None = Field(
        default=None, alias="considerarDiasUteis", examples=[True]
    )
    dia_vencimento: int = Field(..., alias="diaVencimento", examples=["25"])
    numero_parcelas: int | None = Field(default=None, alias="numeroParcelas", examples=[1])


class ContasReceberOcorrenciaDTO(BlingModel):
    """OpenAPI schema ``ContasReceberOcorrenciaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        tipo: Bling ``tipo``; type ``int``; obrigatório. `3` Mensal<br> `4` Bimestral<br> `5` Trimestral<br> `6` Semestral<br> `7` Anual<br> `8` Quinzenal<br> Ignorado no método PUT
        considerar_dias_uteis: Bling ``considerarDiasUteis``; type ``bool | None``; opcional. Ignorado no método PUT
        dia_vencimento: Bling ``diaVencimento``; type ``int``; obrigatório.
        data_limite: Bling ``dataLimite``; type ``date | None``; opcional."""

    tipo: int = Field(..., examples=[3])
    considerar_dias_uteis: bool | None = Field(
        default=None, alias="considerarDiasUteis", examples=[True]
    )
    dia_vencimento: int = Field(..., alias="diaVencimento", examples=["25"])
    data_limite: date | None = Field(default=None, alias="dataLimite", examples=["2023-01-12"])


class ContasReceberOcorrenciaSemanalDTO(BlingModel):
    """OpenAPI schema ``ContasReceberOcorrenciaSemanalDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        tipo: Bling ``tipo``; type ``int``; obrigatório. `9` Semanal<br> Ignorado no método PUT
        considerar_dias_uteis: Bling ``considerarDiasUteis``; type ``bool | None``; opcional. Ignorado no método PUT
        dia_semana_vencimento: Bling ``diaSemanaVencimento``; type ``int``; obrigatório.
        data_limite: Bling ``dataLimite``; type ``date | None``; opcional."""

    tipo: int = Field(..., examples=[9])
    considerar_dias_uteis: bool | None = Field(
        default=None, alias="considerarDiasUteis", examples=[True]
    )
    dia_semana_vencimento: int = Field(..., alias="diaSemanaVencimento", examples=["25"])
    data_limite: date | None = Field(default=None, alias="dataLimite", examples=["2023-01-12"])


class ContasReceberOrigemDTO(BlingModel):
    """OpenAPI schema ``ContasReceberOrigemDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. ID da venda ou nota fiscal que originou a conta."""

    id: int = Field(..., examples=[5436875653])


class ContasReceberVendaDTO(BlingModel):
    """OpenAPI schema ``ContasReceberVendaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        numero: Bling ``numero``; type ``str``; obrigatório."""

    numero: str = Field(..., examples=["123"])


class ContasReceberVendedorDTO(BlingModel):
    """OpenAPI schema ``ContasReceberVendedorDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class ContasReceberPostResponse201(BlingModel):
    """OpenAPI schema ``ContasReceberPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``BasePostResponse | None``; opcional."""

    data: BasePostResponse | None = None


class ContasReceberIdContaReceberBaixarPostResponse200(BlingModel):
    """OpenAPI schema ``ContasReceberIdContaReceberBaixarPostResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        bordero: Bling ``bordero``; type ``Bordero | None``; opcional."""

    bordero: Bordero | None = None


class ContasReceberBoletosGetResponse404(BlingModel):
    """OpenAPI schema ``ContasReceberBoletosGetResponse404``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        error: Bling ``error``; type ``Error1 | None``; opcional."""

    error: Error1 | None = None


class ContasReceberBoletosCancelarPostResponse400(BlingModel):
    """OpenAPI schema ``ContasReceberBoletosCancelarPostResponse400``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        type: Bling ``type``; type ``str``; obrigatório.
        message: Bling ``message``; type ``str``; obrigatório.
        description: Bling ``description``; type ``str``; obrigatório.
        fields: Bling ``fields``; type ``list[FieldModel] | None``; opcional."""

    type: str = Field(..., examples=["VALIDATION_ERROR"])
    message: str = Field(..., examples=["Não foi possível realizar o cancelamento"])
    description: str = Field(
        ...,
        examples=[
            "Não foi possível realizar cancelamento da(s) conta(s) a receber, pois houveram erros de validação."
        ],
    )
    fields: list[FieldModel] | None = None


class ContasReceberBoletosCancelarDTO(BlingModel):
    """OpenAPI schema ``ContasReceberBoletosCancelarDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        autenticacao: Bling ``autenticacao``; type ``ContasReceberAutenticacaoDTO | None``; opcional.
        origem: Bling ``origem``; type ``ContasReceberOrigemDTO | None``; opcional.
        conta: Bling ``conta``; type ``ContasReceberContaDTO | None``; opcional.
        motivo: Bling ``motivo``; type ``str``; obrigatório."""

    autenticacao: ContasReceberAutenticacaoDTO | None = None
    origem: ContasReceberOrigemDTO | None = None
    conta: ContasReceberContaDTO | None = None
    motivo: str = Field(..., examples=["Cancelado por força maior"])


class ContasReceberBoletosDadosBaseDTO(BlingModel):
    """OpenAPI schema ``ContasReceberBoletosDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        venda: Bling ``venda``; type ``ContasReceberVendaDTO | None``; opcional.
        nota_fiscal: Bling ``notaFiscal``; type ``ContasReceberNotaFiscalDTO | None``; opcional.
        valor_total: Bling ``valorTotal``; type ``float | None``; opcional.
        contas: Bling ``contas``; type ``list[ContasReceberBoletosDadosDTO] | None``; opcional."""

    venda: ContasReceberVendaDTO | None = None
    nota_fiscal: ContasReceberNotaFiscalDTO | None = Field(default=None, alias="notaFiscal")
    valor_total: float | None = Field(default=None, alias="valorTotal", examples=[111.2])
    contas: list[ContasReceberBoletosDadosDTO] | None = None


class ContasReceberDadosBaseDTO(BlingModel):
    """OpenAPI schema ``ContasReceberDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        saldo: Bling ``saldo``; type ``float``; obrigatório. É calculado subtraindo os valores dos recebimentos do valor da conta
        data_emissao: Bling ``dataEmissao``; type ``date | None``; opcional.
        vencimento_original: Bling ``vencimentoOriginal``; type ``date``; obrigatório.
        numero_documento: Bling ``numeroDocumento``; type ``str | None``; opcional. Número para controle interno da empresa
        competencia: Bling ``competencia``; type ``date | None``; opcional.
        historico: Bling ``historico``; type ``str | None``; opcional. Descriçao da conta para controle interno da empresa
        numero_banco: Bling ``numeroBanco``; type ``str``; obrigatório. Adicionado automaticamente com o número preenchido no cadastro do banco
        portador: Bling ``portador``; type ``ContasPortadorDTO | None``; opcional.
        categoria: Bling ``categoria``; type ``ContasCategoriaDTO | None``; opcional.
        vendedor: Bling ``vendedor``; type ``ContasReceberVendedorDTO | None``; opcional.
        borderos: Bling ``borderos``; type ``list[int]``; obrigatório. IDs de borderos relacionados à conta caso ela possua pagamentos"""

    saldo: float = Field(..., examples=[100.75])
    data_emissao: date | None = Field(default=None, alias="dataEmissao", examples=["2023-01-12"])
    vencimento_original: date = Field(..., alias="vencimentoOriginal", examples=["2023-01-12"])
    numero_documento: str | None = Field(default=None, alias="numeroDocumento", examples=[""])
    competencia: date | None = Field(default=None, examples=["2023-01-12"])
    historico: str | None = Field(default=None, examples=[""])
    numero_banco: str = Field(..., alias="numeroBanco", examples=[""])
    portador: ContasPortadorDTO | None = None
    categoria: ContasCategoriaDTO | None = None
    vendedor: ContasReceberVendedorDTO | None = None
    borderos: list[int]


class ContasReceberDadosDTO(BlingModel):
    """OpenAPI schema ``ContasReceberDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        ocorrencia: Bling ``ocorrencia``; type ``ContasReceberOcorrenciaUnicaDTO | ContasReceberOcorrenciaParceladaDTO | ContasReceberOcorrenciaDTO | ContasReceberOcorrenciaSemanalDTO | None``; opcional."""

    ocorrencia: (
        ContasReceberOcorrenciaUnicaDTO
        | ContasReceberOcorrenciaParceladaDTO
        | ContasReceberOcorrenciaDTO
        | ContasReceberOcorrenciaSemanalDTO
        | None
    ) = None


class ContasReceberDadosListDTO(BlingModel):
    """OpenAPI schema ``ContasReceberDadosListDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        situacao: Bling ``situacao``; type ``int``; obrigatório. `1` Aberto <br>`2` Pago<br>`3` Parcial<br>`4` Devolvido<br>`5` Cancelado<br>`6` Devolvido parcial<br>`7` Confirmado
        vencimento: Bling ``vencimento``; type ``date``; obrigatório.
        valor: Bling ``valor``; type ``float``; obrigatório.
        id_transacao: Bling ``idTransacao``; type ``str | None``; opcional.
        link_qr_code_pix: Bling ``linkQRCodePix``; type ``str | None``; opcional.
        link_boleto: Bling ``linkBoleto``; type ``str | None``; opcional.
        data_emissao: Bling ``dataEmissao``; type ``date | None``; opcional.
        contato: Bling ``contato``; type ``ContasReceberContatoDTO``; obrigatório.
        forma_pagamento: Bling ``formaPagamento``; type ``ContasReceberFormaPagamentoDTO | None``; opcional.
        conta_contabil: Bling ``contaContabil``; type ``ContasReceberContaContabilDTO | None``; opcional.
        origem: Bling ``origem``; type ``ContasReceberDadosOrigemDTO | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    situacao: int = Field(..., examples=[1])
    vencimento: date = Field(..., examples=["2023-01-12"])
    valor: float = Field(..., examples=[1500.75])
    id_transacao: str | None = Field(default=None, alias="idTransacao", examples=["vX98D"])
    link_qr_code_pix: str | None = Field(
        default=None,
        alias="linkQRCodePix",
        examples=["doc.view.php?id=9ab1671b3f05765cb49fee83ee0f2496"],
    )
    link_boleto: str | None = Field(
        default=None,
        alias="linkBoleto",
        examples=["doc.view.php?id=9ab1671b3f05765cb49fee83ee0f2496"],
    )
    data_emissao: date | None = Field(default=None, alias="dataEmissao", examples=["2023-01-12"])
    contato: ContasReceberContatoDTO
    forma_pagamento: ContasReceberFormaPagamentoDTO | None = Field(
        default=None, alias="formaPagamento"
    )
    conta_contabil: ContasReceberContaContabilDTO | None = Field(
        default=None, alias="contaContabil"
    )
    origem: ContasReceberDadosOrigemDTO | None = None


class ContasReceberGetResponse200(BlingModel):
    """OpenAPI schema ``ContasReceberGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[ContasReceberDadosListDTO] | None``; opcional."""

    data: list[ContasReceberDadosListDTO] | None = None


class ContasReceberPostRequest(
    ContasDadosBaseDTO, ContasReceberDadosBaseDTO, ContasReceberDadosDTO
):
    """OpenAPI schema ``ContasReceberPostRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: ContasDadosBaseDTO, ContasReceberDadosBaseDTO, ContasReceberDadosDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        situacao: Bling ``situacao``; type ``int``; obrigatório. `1` Aberto <br>`2` Pago<br>`3` Parcial<br>`4` Devolvido<br>`5` Cancelado<br>`6` Devolvido parcial<br>`7` Confirmado
        vencimento: Bling ``vencimento``; type ``date``; obrigatório.
        valor: Bling ``valor``; type ``float``; obrigatório.
        contato: Bling ``contato``; type ``ContasContatoDTO``; obrigatório.
        forma_pagamento: Bling ``formaPagamento``; type ``ContasFormaPagamentoDTO | None``; opcional.
        saldo: Bling ``saldo``; type ``float``; obrigatório. É calculado subtraindo os valores dos recebimentos do valor da conta
        data_emissao: Bling ``dataEmissao``; type ``date | None``; opcional.
        vencimento_original: Bling ``vencimentoOriginal``; type ``date``; obrigatório.
        numero_documento: Bling ``numeroDocumento``; type ``str | None``; opcional. Número para controle interno da empresa
        competencia: Bling ``competencia``; type ``date | None``; opcional.
        historico: Bling ``historico``; type ``str | None``; opcional. Descriçao da conta para controle interno da empresa
        numero_banco: Bling ``numeroBanco``; type ``str``; obrigatório. Adicionado automaticamente com o número preenchido no cadastro do banco
        portador: Bling ``portador``; type ``ContasPortadorDTO | None``; opcional.
        categoria: Bling ``categoria``; type ``ContasCategoriaDTO | None``; opcional.
        vendedor: Bling ``vendedor``; type ``ContasReceberVendedorDTO | None``; opcional.
        borderos: Bling ``borderos``; type ``list[int]``; obrigatório. IDs de borderos relacionados à conta caso ela possua pagamentos
        ocorrencia: Bling ``ocorrencia``; type ``ContasReceberOcorrenciaUnicaDTO | ContasReceberOcorrenciaParceladaDTO | ContasReceberOcorrenciaDTO | ContasReceberOcorrenciaSemanalDTO | None``; opcional."""

    pass


class ContasReceberIdContaReceberGetResponse200(BlingModel):
    """OpenAPI schema ``ContasReceberIdContaReceberGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data7 | None``; opcional."""

    data: Data7 | None = None


class ContasReceberIdContaReceberPutRequest(ContasDadosBaseDTO, ContasReceberDadosBaseDTO):
    """OpenAPI schema ``ContasReceberIdContaReceberPutRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: ContasDadosBaseDTO, ContasReceberDadosBaseDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        situacao: Bling ``situacao``; type ``int``; obrigatório. `1` Aberto <br>`2` Pago<br>`3` Parcial<br>`4` Devolvido<br>`5` Cancelado<br>`6` Devolvido parcial<br>`7` Confirmado
        vencimento: Bling ``vencimento``; type ``date``; obrigatório.
        valor: Bling ``valor``; type ``float``; obrigatório.
        contato: Bling ``contato``; type ``ContasContatoDTO``; obrigatório.
        forma_pagamento: Bling ``formaPagamento``; type ``ContasFormaPagamentoDTO | None``; opcional.
        saldo: Bling ``saldo``; type ``float``; obrigatório. É calculado subtraindo os valores dos recebimentos do valor da conta
        data_emissao: Bling ``dataEmissao``; type ``date | None``; opcional.
        vencimento_original: Bling ``vencimentoOriginal``; type ``date``; obrigatório.
        numero_documento: Bling ``numeroDocumento``; type ``str | None``; opcional. Número para controle interno da empresa
        competencia: Bling ``competencia``; type ``date | None``; opcional.
        historico: Bling ``historico``; type ``str | None``; opcional. Descriçao da conta para controle interno da empresa
        numero_banco: Bling ``numeroBanco``; type ``str``; obrigatório. Adicionado automaticamente com o número preenchido no cadastro do banco
        portador: Bling ``portador``; type ``ContasPortadorDTO | None``; opcional.
        categoria: Bling ``categoria``; type ``ContasCategoriaDTO | None``; opcional.
        vendedor: Bling ``vendedor``; type ``ContasReceberVendedorDTO | None``; opcional.
        borderos: Bling ``borderos``; type ``list[int]``; obrigatório. IDs de borderos relacionados à conta caso ela possua pagamentos"""

    pass


__all__ = [
    "ContasReceberAutenticacaoDTO",
    "ContasReceberBoletosCancelarDTO",
    "ContasReceberBoletosCancelarPostResponse400",
    "ContasReceberBoletosDadosBaseDTO",
    "ContasReceberBoletosDadosDTO",
    "ContasReceberBoletosGetResponse404",
    "ContasReceberContaContabilDTO",
    "ContasReceberContaDTO",
    "ContasReceberContatoDTO",
    "ContasReceberDadosBaseDTO",
    "ContasReceberDadosDTO",
    "ContasReceberDadosListDTO",
    "ContasReceberDadosOrigemDTO",
    "ContasReceberFormaPagamentoDTO",
    "ContasReceberGetResponse200",
    "ContasReceberIdContaReceberBaixarPostResponse200",
    "ContasReceberIdContaReceberGetResponse200",
    "ContasReceberIdContaReceberPutRequest",
    "ContasReceberNotaFiscalDTO",
    "ContasReceberOcorrenciaDTO",
    "ContasReceberOcorrenciaParceladaDTO",
    "ContasReceberOcorrenciaSemanalDTO",
    "ContasReceberOcorrenciaUnicaDTO",
    "ContasReceberOrigemDTO",
    "ContasReceberPostRequest",
    "ContasReceberPostResponse201",
    "ContasReceberVendaDTO",
    "ContasReceberVendedorDTO",
]
