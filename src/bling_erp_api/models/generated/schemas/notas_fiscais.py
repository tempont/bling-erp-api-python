# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``notas_fiscais``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import Contato1, Data14, Data17, Data19, Data20


class NotasFiscaisContatoEnderecoDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisContatoEnderecoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        endereco: Bling ``endereco``; type ``str``; obrigatório.
        numero: Bling ``numero``; type ``str | None``; opcional.
        complemento: Bling ``complemento``; type ``str | None``; opcional.
        bairro: Bling ``bairro``; type ``str``; obrigatório.
        cep: Bling ``cep``; type ``str | None``; opcional.
        municipio: Bling ``municipio``; type ``str``; obrigatório.
        uf: Bling ``uf``; type ``str | None``; opcional.
        pais: Bling ``pais``; type ``str | None``; opcional. País do cliente, caso o cliente for estrangeiro (uf: UX)"""

    endereco: str = Field(..., examples=["Olavo Bilac"])
    numero: str | None = Field(default=None, examples=["914"])
    complemento: str | None = Field(default=None, examples=["Sala 101"])
    bairro: str = Field(..., examples=["Imigrante"])
    cep: str | None = Field(default=None, examples=["95702-000"])
    municipio: str = Field(..., examples=["Bento Gonçalves"])
    uf: str | None = Field(default=None, examples=["RS"])
    pais: str | None = Field(default=None, examples=[""])


class NotasFiscaisDocumentoDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisDocumentoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        nome: Bling ``nome``; type ``str | None``; opcional. Nome do documento.
        conteudo: Bling ``conteudo``; type ``str | None``; opcional. Conteúdo do documento comprimido com GZIP e codificado em base64. Para obter o documento original, decodifique o base64 e descomprima o resultado com GZIP."""

    nome: str | None = None
    conteudo: str | None = Field(
        default=None, examples=["H4sIAAAAAAACA8z9BVgcTdc2iiIJGjxAsDBBg..."]
    )


class NotasFiscaisDocumentoReferenciadoDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisDocumentoReferenciadoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        modelo: Bling ``modelo``; type ``str``; obrigatório. `1` Nota fiscal talão <br> `2` Nota fiscal de consumidor talão <br> `2D` Cupom fiscal <br> `4` Nota de produtor <br> `55` NF-e <br> `65` NFC-e
        data: Bling ``data``; type ``str | None``; opcional. Data da nota original no formato AAMM.
        numero: Bling ``numero``; type ``str | None``; opcional. Número da nota original.
        serie: Bling ``serie``; type ``str | None``; opcional. Série da nota original.
        contador_ordem_operacao: Bling ``contadorOrdemOperacao``; type ``str | None``; opcional. Contador de Ordem de Operação (COO) do cupom original.
        chave_acesso: Bling ``chaveAcesso``; type ``str | None``; opcional. Chave de acesso da nota original."""

    modelo: str = Field(..., examples=["55"])
    data: str | None = Field(default=None, examples=["2401"])
    numero: str | None = Field(default=None, examples=["123"])
    serie: str | None = Field(default=None, examples=["1"])
    contador_ordem_operacao: str | None = Field(
        default=None, alias="contadorOrdemOperacao", examples=["1"]
    )
    chave_acesso: str | None = Field(
        default=None, alias="chaveAcesso", examples=["62634519764512837946527549134679858182373412"]
    )


class NotasFiscaisDocumentoReferenciadoItemDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisDocumentoReferenciadoItemDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        chave_acesso: Bling ``chaveAcesso``; type ``str | None``; opcional. Chave de acesso da nota original.
        numero_item: Bling ``numeroItem``; type ``str | None``; opcional. Número do item na nota referenciada."""

    chave_acesso: str | None = Field(
        default=None, alias="chaveAcesso", examples=["62634519764512837946527549134679858182373412"]
    )
    numero_item: str | None = Field(default=None, alias="numeroItem", examples=["1"])


class NotasFiscaisExclusaoDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisExclusaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        alertas: Bling ``alertas``; type ``list[str] | None``; opcional.
        ids_excluidos: Bling ``idsExcluidos``; type ``list[int]``; obrigatório."""

    alertas: list[str] | None = None
    ids_excluidos: list[int] = Field(..., alias="idsExcluidos")


class NotasFiscaisIcmsDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisIcmsDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        st: Bling ``st``; type ``int | None``; opcional.
        origem: Bling ``origem``; type ``int | None``; opcional. `0` Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8 <br> `1` Estrangeira - Importação direta, exceto a indicada no código 6; 2: Estrangeira - Adquirida no mercado interno, e...
        modalidade: Bling ``modalidade``; type ``int | None``; opcional. `0` Margem Valor Agregado (%) <br> `1` Pauta (valor) <br> `2` Preço Tabelado Máx. (valor) <br> `3` Valor da operação
        aliquota: Bling ``aliquota``; type ``float | None``; opcional.
        valor: Bling ``valor``; type ``float | None``; opcional."""

    st: int | None = Field(default=None, examples=[60])
    origem: int | None = Field(default=None, examples=[0])
    modalidade: int | None = Field(default=None, examples=[0])
    aliquota: float | None = Field(default=None, examples=[5])
    valor: float | None = Field(default=None, examples=[10.5])


class NotasFiscaisImpostoDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisImpostoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        valor_aproximado_total_tributos: Bling ``valorAproximadoTotalTributos``; type ``float | None``; opcional.
        icms: Bling ``icms``; type ``NotasFiscaisIcmsDTO | None``; opcional."""

    valor_aproximado_total_tributos: float | None = Field(
        default=None, alias="valorAproximadoTotalTributos", examples=[1.2]
    )
    icms: NotasFiscaisIcmsDTO | None = None


class NotasFiscaisIntermediadorDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisIntermediadorDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        cnpj: Bling ``cnpj``; type ``str``; obrigatório.
        nome_usuario: Bling ``nomeUsuario``; type ``str``; obrigatório."""

    cnpj: str = Field(..., examples=["13921649000197"])
    nome_usuario: str = Field(..., alias="nomeUsuario", examples=["usuario"])


class NotasFiscaisItemDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisItemDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        codigo: Bling ``codigo``; type ``str``; obrigatório.
        descricao: Bling ``descricao``; type ``str | None``; opcional.
        unidade: Bling ``unidade``; type ``str | None``; opcional.
        quantidade: Bling ``quantidade``; type ``float | None``; opcional.
        valor: Bling ``valor``; type ``float | None``; opcional. Valor unitário do item.
        valor_total: Bling ``valorTotal``; type ``float | None``; opcional.
        tipo: Bling ``tipo``; type ``str | None``; opcional. `P` Produto <br> `S` Serviço
        peso_bruto: Bling ``pesoBruto``; type ``float | None``; opcional.
        peso_liquido: Bling ``pesoLiquido``; type ``float | None``; opcional.
        numero_pedido_compra: Bling ``numeroPedidoCompra``; type ``str | None``; opcional.
        classificacao_fiscal: Bling ``classificacaoFiscal``; type ``str | None``; opcional. NCM do item.
        cest: Bling ``cest``; type ``str | None``; opcional.
        codigo_servico: Bling ``codigoServico``; type ``str | None``; opcional.
        origem: Bling ``origem``; type ``int | None``; opcional. `0` Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8 <br> `1` Estrangeira - Importação direta, exceto a indicada no código 6; 2: Estrangeira - Adquirida no mercado interno, e...
        informacoes_adicionais: Bling ``informacoesAdicionais``; type ``str | None``; opcional.
        gtin: Bling ``gtin``; type ``str | None``; opcional.
        cfop: Bling ``cfop``; type ``str | None``; opcional.
        impostos: Bling ``impostos``; type ``NotasFiscaisImpostoDTO | None``; opcional.
        documento_referenciado: Bling ``documentoReferenciado``; type ``NotasFiscaisDocumentoReferenciadoItemDTO | None``; opcional. Documento fiscal referenciado pelo item."""

    codigo: str = Field(..., examples=["BLG-5"])
    descricao: str | None = Field(default=None, examples=["Produto do Bling"])
    unidade: str | None = Field(default=None, examples=["UN"])
    quantidade: float | None = Field(default=None, examples=[1])
    valor: float | None = Field(default=None, examples=[4.9])
    valor_total: float | None = Field(default=None, alias="valorTotal", examples=[5.9])
    tipo: str | None = Field(default=None, examples=["P"])
    peso_bruto: float | None = Field(default=None, alias="pesoBruto", examples=[0.5])
    peso_liquido: float | None = Field(default=None, alias="pesoLiquido", examples=[0.5])
    numero_pedido_compra: str | None = Field(
        default=None, alias="numeroPedidoCompra", examples=["235"]
    )
    classificacao_fiscal: str | None = Field(
        default=None, alias="classificacaoFiscal", examples=["9999.99.99"]
    )
    cest: str | None = Field(default=None, examples=["99.999.99"])
    codigo_servico: str | None = Field(default=None, alias="codigoServico", examples=["99.99"])
    origem: int | None = Field(default=None, examples=[0])
    informacoes_adicionais: str | None = Field(
        default=None, alias="informacoesAdicionais", examples=["Descrição do item"]
    )
    gtin: str | None = Field(default=None, examples=["7890403456855"])
    cfop: str | None = Field(default=None, examples=["6102"])
    impostos: NotasFiscaisImpostoDTO | None = None
    documento_referenciado: NotasFiscaisDocumentoReferenciadoItemDTO | None = Field(
        default=None, alias="documentoReferenciado"
    )


class NotasFiscaisLojaDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisLojaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        numero: Bling ``numero``; type ``str | None``; opcional."""

    id: int = Field(..., examples=[12345678])
    numero: str | None = Field(default=None, examples=["LOJA_8864"])


class NotasFiscaisNaturezaOperacaoDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisNaturezaOperacaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class NotasFiscaisNotaFiscalProdutorRuralReferenciadaDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisNotaFiscalProdutorRuralReferenciadaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        numero: Bling ``numero``; type ``str``; obrigatório. Número da NF referenciada.
        serie: Bling ``serie``; type ``str``; obrigatório. Série da NF referenciada.
        data: Bling ``data``; type ``date``; obrigatório."""

    numero: str = Field(..., examples=["125"])
    serie: str = Field(..., examples=["1"])
    data: date = Field(..., examples=["2023-01-12"])


class NotasFiscaisParcelaFormaPagamentoDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisParcelaFormaPagamentoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class NotasFiscaisTransporteDadosVolumeDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisTransporteDadosVolumeDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        quantidade: Bling ``quantidade``; type ``int | None``; opcional.
        especie: Bling ``especie``; type ``int | None``; opcional. <br>`1` Outro(s)<br> `2` Volume(s)<br> `3` Unidade(s)<br> `4` Caixa(s)<br> `5` Pacote(s)<br> `6` Envelope(s)<br> `7` Pallet(s)<br> `8` Saco(s)
        numero: Bling ``numero``; type ``str | None``; opcional.
        peso_bruto: Bling ``pesoBruto``; type ``float | None``; opcional.
        peso_liquido: Bling ``pesoLiquido``; type ``float | None``; opcional."""

    quantidade: int | None = Field(default=None, examples=[5])
    especie: int | None = Field(default=None, examples=[1])
    numero: str | None = Field(default=None, examples=["1"])
    peso_bruto: float | None = Field(default=None, alias="pesoBruto", examples=[0.5])
    peso_liquido: float | None = Field(default=None, alias="pesoLiquido", examples=[0.35])


class NotasFiscaisTransporteEtiquetaDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisTransporteEtiquetaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        nome: Bling ``nome``; type ``str | None``; opcional.
        endereco: Bling ``endereco``; type ``str | None``; opcional.
        numero: Bling ``numero``; type ``str | None``; opcional.
        complemento: Bling ``complemento``; type ``str | None``; opcional.
        municipio: Bling ``municipio``; type ``str | None``; opcional.
        uf: Bling ``uf``; type ``str | None``; opcional.
        cep: Bling ``cep``; type ``str | None``; opcional.
        bairro: Bling ``bairro``; type ``str | None``; opcional."""

    nome: str | None = Field(default=None, examples=["Transportador"])
    endereco: str | None = Field(default=None, examples=["Olavo Bilac"])
    numero: str | None = Field(default=None, examples=["914"])
    complemento: str | None = Field(default=None, examples=["Sala 101"])
    municipio: str | None = Field(default=None, examples=["Bento Gonçalves"])
    uf: str | None = Field(default=None, examples=["RS"])
    cep: str | None = Field(default=None, examples=["95702-000"])
    bairro: str | None = Field(default=None, examples=["Imigrante"])


class NotasFiscaisTransporteTransportadorEnderecoDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisTransporteTransportadorEnderecoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        endereco: Bling ``endereco``; type ``str | None``; opcional.
        municipio: Bling ``municipio``; type ``str | None``; opcional.
        uf: Bling ``uf``; type ``str | None``; opcional."""

    endereco: str | None = Field(default=None, examples=["Olavo Bilac"])
    municipio: str | None = Field(default=None, examples=["Bento Gonçalves"])
    uf: str | None = Field(default=None, examples=["RS"])


class NotasFiscaisTransporteTransportadorGetDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisTransporteTransportadorGetDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        nome: Bling ``nome``; type ``str``; obrigatório.
        numero_documento: Bling ``numeroDocumento``; type ``str | None``; opcional. CNPJ ou CPF."""

    nome: str = Field(..., examples=["Transportador"])
    numero_documento: str | None = Field(
        default=None, alias="numeroDocumento", examples=["30188025000121"]
    )


class NotasFiscaisTransporteTransportadorPostDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisTransporteTransportadorPostDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        nome: Bling ``nome``; type ``str``; obrigatório.
        numero_documento: Bling ``numeroDocumento``; type ``str | None``; opcional. CNPJ ou CPF.
        ie: Bling ``ie``; type ``str | None``; opcional. Inscrição estadual.
        endereco: Bling ``endereco``; type ``NotasFiscaisTransporteTransportadorEnderecoDTO | None``; opcional."""

    nome: str = Field(..., examples=["Transportador"])
    numero_documento: str | None = Field(
        default=None, alias="numeroDocumento", examples=["30188025000121"]
    )
    ie: str | None = Field(default=None, examples=["949895756023"])
    endereco: NotasFiscaisTransporteTransportadorEnderecoDTO | None = None


class NotasFiscaisTransporteVeiculoDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisTransporteVeiculoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        placa: Bling ``placa``; type ``str | None``; opcional.
        uf: Bling ``uf``; type ``str | None``; opcional.
        marca: Bling ``marca``; type ``str | None``; opcional."""

    placa: str | None = Field(default=None, examples=["LDO-2373"])
    uf: str | None = Field(default=None, examples=["RS"])
    marca: str | None = Field(default=None, examples=["Volvo"])


class NotasFiscaisTransporteVolumeGetDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisTransporteVolumeGetDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])


class NotasFiscaisTransporteVolumePostDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisTransporteVolumePostDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        servico: Bling ``servico``; type ``str``; obrigatório. Utilizado no método POST.
        codigo_rastreamento: Bling ``codigoRastreamento``; type ``str | None``; opcional. Utilizado no método POST."""

    id: int | None = Field(default=None, examples=[12345678])
    servico: str = Field(..., examples=["ALIAS_123"])
    codigo_rastreamento: str | None = Field(
        default=None, alias="codigoRastreamento", examples=["COD123BR"]
    )


class NotasFiscaisVendedorDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisVendedorDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345679])


class NotaFiscalResponsePOST(BlingModel):
    """OpenAPI schema ``NotaFiscalResponsePOST``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        numero: Bling ``numero``; type ``str``; obrigatório.
        serie: Bling ``serie``; type ``str``; obrigatório.
        contato: Bling ``contato``; type ``Contato1``; obrigatório."""

    numero: str = Field(..., examples=["6541"])
    serie: str = Field(..., examples=["1"])
    contato: Contato1


class NfePostResponse201(BlingModel):
    """OpenAPI schema ``NfePostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data17 | None``; opcional."""

    data: Data17 | None = None


class NfeDeleteResponse200(BlingModel):
    """OpenAPI schema ``NfeDeleteResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``NotasFiscaisExclusaoDTO | None``; opcional."""

    data: NotasFiscaisExclusaoDTO | None = None


class NfeIdNotaFiscalEnviarPostResponse200(BlingModel):
    """OpenAPI schema ``NfeIdNotaFiscalEnviarPostResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data20 | None``; opcional."""

    data: Data20 | None = None


class NfeDocumentoChaveAcessoGetResponse200(BlingModel):
    """OpenAPI schema ``NfeDocumentoChaveAcessoGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[NotasFiscaisDocumentoDTO] | None``; opcional."""

    data: list[NotasFiscaisDocumentoDTO] | None = None


class NotasFiscaisContatoDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisContatoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        nome: Bling ``nome``; type ``str``; obrigatório.
        tipo_pessoa: Bling ``tipoPessoa``; type ``str``; obrigatório. `F` Física <br> `J` Jurídica <br> `E` Estrangeira.
        numero_documento: Bling ``numeroDocumento``; type ``str``; obrigatório. CNPJ ou CPF.
        ie: Bling ``ie``; type ``str | None``; opcional.
        rg: Bling ``rg``; type ``str | None``; opcional.
        contribuinte: Bling ``contribuinte``; type ``int``; obrigatório. `1` Contribuinte do ICMS <br> `2` Contribuinte isento de ICMS <br> `9` Não contribuinte.
        telefone: Bling ``telefone``; type ``str | None``; opcional.
        email: Bling ``email``; type ``str | None``; opcional.
        endereco: Bling ``endereco``; type ``NotasFiscaisContatoEnderecoDTO | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    nome: str = Field(..., examples=["Contato do Bling"])
    tipo_pessoa: str = Field(..., alias="tipoPessoa", examples=["J"])
    numero_documento: str = Field(..., alias="numeroDocumento", examples=["30188025000121"])
    ie: str | None = Field(default=None, examples=["7364873393"])
    rg: str | None = Field(default=None, examples=["451838701"])
    contribuinte: int = Field(..., examples=[1])
    telefone: str | None = Field(default=None, examples=["54 3771-7278"])
    email: str | None = Field(default=None, examples=["pedrosilva@bling.com.br"])
    endereco: NotasFiscaisContatoEnderecoDTO | None = None


class NotasFiscaisDadosBaseDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        tipo: Bling ``tipo``; type ``int``; obrigatório. `0` Entrada <br> `1` Saída
        situacao: Bling ``situacao``; type ``int | None``; opcional. `1` Pendente<br>`2` Cancelada<br>`3` Aguardando recibo<br>`4` Rejeitada<br>`5` Autorizada<br>`6` Emitida DANFE<br>`7` Registrada<br>`8` Aguardando protocolo<br>`9` Denegada<br>`10...
        numero: Bling ``numero``; type ``str``; obrigatório.
        data_emissao: Bling ``dataEmissao``; type ``str | None``; opcional. Data e hora da emissão.
        data_operacao: Bling ``dataOperacao``; type ``str``; obrigatório. Data de saída/entrada de acordo com o tipo da nota.
        chave_acesso: Bling ``chaveAcesso``; type ``str | None``; opcional.
        contato: Bling ``contato``; type ``NotasFiscaisContatoDTO``; obrigatório.
        natureza_operacao: Bling ``naturezaOperacao``; type ``NotasFiscaisNaturezaOperacaoDTO``; obrigatório.
        loja: Bling ``loja``; type ``NotasFiscaisLojaDTO | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    tipo: int = Field(..., examples=[1])
    situacao: int | None = Field(default=None, examples=[1])
    numero: str = Field(..., examples=["6541"])
    data_emissao: str | None = Field(
        default=None, alias="dataEmissao", examples=["2023-01-12 09:52:12"]
    )
    data_operacao: str = Field(..., alias="dataOperacao", examples=["2023-01-12 09:52:12"])
    chave_acesso: str | None = Field(default=None, alias="chaveAcesso")
    contato: NotasFiscaisContatoDTO
    natureza_operacao: NotasFiscaisNaturezaOperacaoDTO = Field(..., alias="naturezaOperacao")
    loja: NotasFiscaisLojaDTO | None = None


class NotasFiscaisParcelaDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisParcelaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``date``; obrigatório.
        valor: Bling ``valor``; type ``float``; obrigatório.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        caut: Bling ``caut``; type ``str | None``; opcional. cAut (ou NSU): código de autorização da operação financeira.
        forma_pagamento: Bling ``formaPagamento``; type ``NotasFiscaisParcelaFormaPagamentoDTO | None``; opcional."""

    data: date = Field(..., examples=["2023-01-12"])
    valor: float = Field(..., examples=[123.45])
    observacoes: str | None = Field(default=None, examples=["Observação da parcela."])
    caut: str | None = Field(default=None, examples=["123456789"])
    forma_pagamento: NotasFiscaisParcelaFormaPagamentoDTO | None = Field(
        default=None, alias="formaPagamento"
    )


class NotasFiscaisTransporteGetDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisTransporteGetDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        frete_por_conta: Bling ``fretePorConta``; type ``int | None``; opcional. `0` Contratação do Frete por conta do Remetente (CIF) <br> `1` Contratação do Frete por conta do Destinatário (FOB) <br> `2` Contratação do Frete por conta de Terceiros <br> `3` T...
        transportador: Bling ``transportador``; type ``NotasFiscaisTransporteTransportadorGetDTO | None``; opcional.
        volumes: Bling ``volumes``; type ``list[NotasFiscaisTransporteVolumeGetDTO] | None``; opcional.
        etiqueta: Bling ``etiqueta``; type ``NotasFiscaisTransporteEtiquetaDTO | None``; opcional."""

    frete_por_conta: int | None = Field(default=1, alias="fretePorConta", examples=[0])
    transportador: NotasFiscaisTransporteTransportadorGetDTO | None = None
    volumes: list[NotasFiscaisTransporteVolumeGetDTO] | None = None
    etiqueta: NotasFiscaisTransporteEtiquetaDTO | None = None


class NotasFiscaisTransportePostDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisTransportePostDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        frete_por_conta: Bling ``fretePorConta``; type ``int | None``; opcional. `0` Contratação do Frete por conta do Remetente (CIF) <br> `1` Contratação do Frete por conta do Destinatário (FOB) <br> `2` Contratação do Frete por conta de Terceiros <br> `3` T...
        frete: Bling ``frete``; type ``float | None``; opcional. Utilizado no método POST.
        veiculo: Bling ``veiculo``; type ``NotasFiscaisTransporteVeiculoDTO | None``; opcional.
        transportador: Bling ``transportador``; type ``NotasFiscaisTransporteTransportadorPostDTO | None``; opcional.
        volume: Bling ``volume``; type ``NotasFiscaisTransporteDadosVolumeDTO | None``; opcional.
        volumes: Bling ``volumes``; type ``list[NotasFiscaisTransporteVolumePostDTO] | None``; opcional.
        etiqueta: Bling ``etiqueta``; type ``NotasFiscaisTransporteEtiquetaDTO | None``; opcional."""

    frete_por_conta: int | None = Field(default=None, alias="fretePorConta", examples=[0])
    frete: float | None = Field(default=None, examples=[20])
    veiculo: NotasFiscaisTransporteVeiculoDTO | None = None
    transportador: NotasFiscaisTransporteTransportadorPostDTO | None = None
    volume: NotasFiscaisTransporteDadosVolumeDTO | None = None
    volumes: list[NotasFiscaisTransporteVolumePostDTO] | None = None
    etiqueta: NotasFiscaisTransporteEtiquetaDTO | None = None


class NfeGetResponse200(BlingModel):
    """OpenAPI schema ``NfeGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[NotasFiscaisDadosBaseDTO] | None``; opcional."""

    data: list[NotasFiscaisDadosBaseDTO] | None = None


class NfeIdNotaFiscalPutResponse200(BlingModel):
    """OpenAPI schema ``NfeIdNotaFiscalPutResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data19 | None``; opcional."""

    data: Data19 | None = None


class NotasFiscaisDadosGetDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisDadosGetDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        serie: Bling ``serie``; type ``int | None``; opcional.
        valor_nota: Bling ``valorNota``; type ``float | None``; opcional.
        valor_frete: Bling ``valorFrete``; type ``float | None``; opcional.
        finalidade: Bling ``finalidade``; type ``int | None``; opcional. `1` Normal <br>`2` Complementar <br>`3` Ajuste <br>`4` Devolução <br>`5` Crédito <br>`6` Débito
        tipo_nota: Bling ``tipoNota``; type ``str | None``; opcional. Presente quando finalidade for 5 (Crédito) ou 6 (Débito). <br><br>**Crédito (finalidade 5):** <br>`01` Multa e juros <br>`02` Apropriação de crédito presumido de IBS sobre o saldo...
        xml: Bling ``xml``; type ``str | None``; opcional.
        link_danfe: Bling ``linkDanfe``; type ``str | None``; opcional.
        link_pdf: Bling ``linkPDF``; type ``str | None``; opcional.
        optante_simples_nacional: Bling ``optanteSimplesNacional``; type ``bool | None``; opcional.
        numero_pedido_loja: Bling ``numeroPedidoLoja``; type ``str | None``; opcional.
        transporte: Bling ``transporte``; type ``NotasFiscaisTransporteGetDTO | None``; opcional.
        vendedor: Bling ``vendedor``; type ``NotasFiscaisVendedorDTO | None``; opcional.
        itens: Bling ``itens``; type ``list[NotasFiscaisItemDTO] | None``; opcional.
        parcelas: Bling ``parcelas``; type ``list[NotasFiscaisParcelaDTO] | None``; opcional."""

    serie: int | None = Field(default=None, examples=["1"])
    valor_nota: float | None = Field(default=None, alias="valorNota", examples=[10.3])
    valor_frete: float | None = Field(default=None, alias="valorFrete", examples=[10.3])
    finalidade: int | None = Field(default=None, examples=[1])
    tipo_nota: str | None = Field(default=None, alias="tipoNota", examples=["01"])
    xml: str | None = None
    link_danfe: str | None = Field(default=None, alias="linkDanfe")
    link_pdf: str | None = Field(default=None, alias="linkPDF")
    optante_simples_nacional: bool | None = Field(default=None, alias="optanteSimplesNacional")
    numero_pedido_loja: str | None = Field(default=None, alias="numeroPedidoLoja")
    transporte: NotasFiscaisTransporteGetDTO | None = None
    vendedor: NotasFiscaisVendedorDTO | None = None
    itens: list[NotasFiscaisItemDTO] | None = None
    parcelas: list[NotasFiscaisParcelaDTO] | None = None


class NotasFiscaisDadosPostDTO(BlingModel):
    """OpenAPI schema ``NotasFiscaisDadosPostDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        finalidade: Bling ``finalidade``; type ``int | None``; opcional. `1` Normal <br>`2` Complementar <br>`3` Ajuste <br>`4` Devolução <br>`5` Crédito <br>`6` Débito
        tipo_nota: Bling ``tipoNota``; type ``str | None``; opcional. Obrigatório quando finalidade for 5 (Crédito) ou 6 (Débito). <br><br>**Crédito (finalidade 5):** <br>`01` Multa e juros <br>`02` Apropriação de crédito presumido de IBS sobre o sa...
        seguro: Bling ``seguro``; type ``float | None``; opcional.
        despesas: Bling ``despesas``; type ``float | None``; opcional.
        desconto: Bling ``desconto``; type ``float | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        xml: Bling ``xml``; type ``str | None``; opcional.
        link_danfe: Bling ``linkDanfe``; type ``str | None``; opcional.
        link_pdf: Bling ``linkPDF``; type ``str | None``; opcional.
        documento_referenciado: Bling ``documentoReferenciado``; type ``NotasFiscaisDocumentoReferenciadoDTO | None``; opcional.
        documentos_referenciados: Bling ``documentosReferenciados``; type ``list[NotasFiscaisDocumentoReferenciadoDTO] | None``; opcional.
        itens: Bling ``itens``; type ``list[NotasFiscaisItemDTO] | None``; opcional.
        parcelas: Bling ``parcelas``; type ``list[NotasFiscaisParcelaDTO] | None``; opcional.
        transporte: Bling ``transporte``; type ``NotasFiscaisTransportePostDTO | None``; opcional.
        nota_fiscal_produtor_rural_referenciada: Bling ``notaFiscalProdutorRuralReferenciada``; type ``NotasFiscaisNotaFiscalProdutorRuralReferenciadaDTO | None``; opcional.
        intermediador: Bling ``intermediador``; type ``NotasFiscaisIntermediadorDTO | None``; opcional."""

    finalidade: int | None = Field(default=None, examples=[1])
    tipo_nota: str | None = Field(default=None, alias="tipoNota", examples=["01"])
    seguro: float | None = Field(default=None, examples=[1.15])
    despesas: float | None = Field(default=None, examples=[5.08])
    desconto: float | None = Field(default=None, examples=[10.12])
    observacoes: str | None = Field(default=None, examples=["Observação da nota."])
    xml: str | None = None
    link_danfe: str | None = Field(default=None, alias="linkDanfe")
    link_pdf: str | None = Field(default=None, alias="linkPDF")
    documento_referenciado: NotasFiscaisDocumentoReferenciadoDTO | None = Field(
        default=None, alias="documentoReferenciado"
    )
    documentos_referenciados: list[NotasFiscaisDocumentoReferenciadoDTO] | None = Field(
        default=None, alias="documentosReferenciados"
    )
    itens: list[NotasFiscaisItemDTO] | None = Field(default=None, min_length=1)
    parcelas: list[NotasFiscaisParcelaDTO] | None = None
    transporte: NotasFiscaisTransportePostDTO | None = None
    nota_fiscal_produtor_rural_referenciada: (
        NotasFiscaisNotaFiscalProdutorRuralReferenciadaDTO | None
    ) = Field(default=None, alias="notaFiscalProdutorRuralReferenciada")
    intermediador: NotasFiscaisIntermediadorDTO | None = None


class NfePostRequest(NotasFiscaisDadosBaseDTO, NotasFiscaisDadosPostDTO):
    """OpenAPI schema ``NfePostRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: NotasFiscaisDadosBaseDTO, NotasFiscaisDadosPostDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        tipo: Bling ``tipo``; type ``int``; obrigatório. `0` Entrada <br> `1` Saída
        situacao: Bling ``situacao``; type ``int | None``; opcional. `1` Pendente<br>`2` Cancelada<br>`3` Aguardando recibo<br>`4` Rejeitada<br>`5` Autorizada<br>`6` Emitida DANFE<br>`7` Registrada<br>`8` Aguardando protocolo<br>`9` Denegada<br>`10...
        numero: Bling ``numero``; type ``str``; obrigatório.
        data_emissao: Bling ``dataEmissao``; type ``str | None``; opcional. Data e hora da emissão.
        data_operacao: Bling ``dataOperacao``; type ``str``; obrigatório. Data de saída/entrada de acordo com o tipo da nota.
        chave_acesso: Bling ``chaveAcesso``; type ``str | None``; opcional.
        contato: Bling ``contato``; type ``NotasFiscaisContatoDTO``; obrigatório.
        natureza_operacao: Bling ``naturezaOperacao``; type ``NotasFiscaisNaturezaOperacaoDTO``; obrigatório.
        loja: Bling ``loja``; type ``NotasFiscaisLojaDTO | None``; opcional.
        finalidade: Bling ``finalidade``; type ``int | None``; opcional. `1` Normal <br>`2` Complementar <br>`3` Ajuste <br>`4` Devolução <br>`5` Crédito <br>`6` Débito
        tipo_nota: Bling ``tipoNota``; type ``str | None``; opcional. Obrigatório quando finalidade for 5 (Crédito) ou 6 (Débito). <br><br>**Crédito (finalidade 5):** <br>`01` Multa e juros <br>`02` Apropriação de crédito presumido de IBS sobre o sa...
        seguro: Bling ``seguro``; type ``float | None``; opcional.
        despesas: Bling ``despesas``; type ``float | None``; opcional.
        desconto: Bling ``desconto``; type ``float | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        xml: Bling ``xml``; type ``str | None``; opcional.
        link_danfe: Bling ``linkDanfe``; type ``str | None``; opcional.
        link_pdf: Bling ``linkPDF``; type ``str | None``; opcional.
        documento_referenciado: Bling ``documentoReferenciado``; type ``NotasFiscaisDocumentoReferenciadoDTO | None``; opcional.
        documentos_referenciados: Bling ``documentosReferenciados``; type ``list[NotasFiscaisDocumentoReferenciadoDTO] | None``; opcional.
        itens: Bling ``itens``; type ``list[NotasFiscaisItemDTO] | None``; opcional.
        parcelas: Bling ``parcelas``; type ``list[NotasFiscaisParcelaDTO] | None``; opcional.
        transporte: Bling ``transporte``; type ``NotasFiscaisTransportePostDTO | None``; opcional.
        nota_fiscal_produtor_rural_referenciada: Bling ``notaFiscalProdutorRuralReferenciada``; type ``NotasFiscaisNotaFiscalProdutorRuralReferenciadaDTO | None``; opcional.
        intermediador: Bling ``intermediador``; type ``NotasFiscaisIntermediadorDTO | None``; opcional."""

    pass


class NfeIdNotaFiscalGetResponse200(BlingModel):
    """OpenAPI schema ``NfeIdNotaFiscalGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data14 | None``; opcional."""

    data: Data14 | None = None


class NfeIdNotaFiscalPutRequest(NotasFiscaisDadosBaseDTO, NotasFiscaisDadosPostDTO):
    """OpenAPI schema ``NfeIdNotaFiscalPutRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: NotasFiscaisDadosBaseDTO, NotasFiscaisDadosPostDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        tipo: Bling ``tipo``; type ``int``; obrigatório. `0` Entrada <br> `1` Saída
        situacao: Bling ``situacao``; type ``int | None``; opcional. `1` Pendente<br>`2` Cancelada<br>`3` Aguardando recibo<br>`4` Rejeitada<br>`5` Autorizada<br>`6` Emitida DANFE<br>`7` Registrada<br>`8` Aguardando protocolo<br>`9` Denegada<br>`10...
        numero: Bling ``numero``; type ``str``; obrigatório.
        data_emissao: Bling ``dataEmissao``; type ``str | None``; opcional. Data e hora da emissão.
        data_operacao: Bling ``dataOperacao``; type ``str``; obrigatório. Data de saída/entrada de acordo com o tipo da nota.
        chave_acesso: Bling ``chaveAcesso``; type ``str | None``; opcional.
        contato: Bling ``contato``; type ``NotasFiscaisContatoDTO``; obrigatório.
        natureza_operacao: Bling ``naturezaOperacao``; type ``NotasFiscaisNaturezaOperacaoDTO``; obrigatório.
        loja: Bling ``loja``; type ``NotasFiscaisLojaDTO | None``; opcional.
        finalidade: Bling ``finalidade``; type ``int | None``; opcional. `1` Normal <br>`2` Complementar <br>`3` Ajuste <br>`4` Devolução <br>`5` Crédito <br>`6` Débito
        tipo_nota: Bling ``tipoNota``; type ``str | None``; opcional. Obrigatório quando finalidade for 5 (Crédito) ou 6 (Débito). <br><br>**Crédito (finalidade 5):** <br>`01` Multa e juros <br>`02` Apropriação de crédito presumido de IBS sobre o sa...
        seguro: Bling ``seguro``; type ``float | None``; opcional.
        despesas: Bling ``despesas``; type ``float | None``; opcional.
        desconto: Bling ``desconto``; type ``float | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        xml: Bling ``xml``; type ``str | None``; opcional.
        link_danfe: Bling ``linkDanfe``; type ``str | None``; opcional.
        link_pdf: Bling ``linkPDF``; type ``str | None``; opcional.
        documento_referenciado: Bling ``documentoReferenciado``; type ``NotasFiscaisDocumentoReferenciadoDTO | None``; opcional.
        documentos_referenciados: Bling ``documentosReferenciados``; type ``list[NotasFiscaisDocumentoReferenciadoDTO] | None``; opcional.
        itens: Bling ``itens``; type ``list[NotasFiscaisItemDTO] | None``; opcional.
        parcelas: Bling ``parcelas``; type ``list[NotasFiscaisParcelaDTO] | None``; opcional.
        transporte: Bling ``transporte``; type ``NotasFiscaisTransportePostDTO | None``; opcional.
        nota_fiscal_produtor_rural_referenciada: Bling ``notaFiscalProdutorRuralReferenciada``; type ``NotasFiscaisNotaFiscalProdutorRuralReferenciadaDTO | None``; opcional.
        intermediador: Bling ``intermediador``; type ``NotasFiscaisIntermediadorDTO | None``; opcional."""

    pass


__all__ = [
    "NfeDeleteResponse200",
    "NfeDocumentoChaveAcessoGetResponse200",
    "NfeGetResponse200",
    "NfeIdNotaFiscalEnviarPostResponse200",
    "NfeIdNotaFiscalGetResponse200",
    "NfeIdNotaFiscalPutRequest",
    "NfeIdNotaFiscalPutResponse200",
    "NfePostRequest",
    "NfePostResponse201",
    "NotaFiscalResponsePOST",
    "NotasFiscaisContatoDTO",
    "NotasFiscaisContatoEnderecoDTO",
    "NotasFiscaisDadosBaseDTO",
    "NotasFiscaisDadosGetDTO",
    "NotasFiscaisDadosPostDTO",
    "NotasFiscaisDocumentoDTO",
    "NotasFiscaisDocumentoReferenciadoDTO",
    "NotasFiscaisDocumentoReferenciadoItemDTO",
    "NotasFiscaisExclusaoDTO",
    "NotasFiscaisIcmsDTO",
    "NotasFiscaisImpostoDTO",
    "NotasFiscaisIntermediadorDTO",
    "NotasFiscaisItemDTO",
    "NotasFiscaisLojaDTO",
    "NotasFiscaisNaturezaOperacaoDTO",
    "NotasFiscaisNotaFiscalProdutorRuralReferenciadaDTO",
    "NotasFiscaisParcelaDTO",
    "NotasFiscaisParcelaFormaPagamentoDTO",
    "NotasFiscaisTransporteDadosVolumeDTO",
    "NotasFiscaisTransporteEtiquetaDTO",
    "NotasFiscaisTransporteGetDTO",
    "NotasFiscaisTransportePostDTO",
    "NotasFiscaisTransporteTransportadorEnderecoDTO",
    "NotasFiscaisTransporteTransportadorGetDTO",
    "NotasFiscaisTransporteTransportadorPostDTO",
    "NotasFiscaisTransporteVeiculoDTO",
    "NotasFiscaisTransporteVolumeGetDTO",
    "NotasFiscaisTransporteVolumePostDTO",
    "NotasFiscaisVendedorDTO",
]
