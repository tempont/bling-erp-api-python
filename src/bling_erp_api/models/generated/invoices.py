"""Semi-generated NF-e/NFC-e invoice models."""

from __future__ import annotations

from typing import Any

from pydantic import Field

from bling_erp_api.models.base import BlingModel

# --- Sub-DTOs (simplified but functional) ---


class NotasFiscaisContatoEnderecoDTO(BlingModel):
    endereco: str | None = Field(default=None, alias="endereco")
    numero: str | None = Field(default=None, alias="numero")
    complemento: str | None = Field(default=None, alias="complemento")
    bairro: str | None = Field(default=None, alias="bairro")
    cep: str | None = Field(default=None, alias="cep")
    municipio: str | None = Field(default=None, alias="municipio")
    uf: str | None = Field(default=None, alias="uf")
    pais: str | None = Field(default=None, alias="pais")


class NotasFiscaisContatoDTO(BlingModel):
    id: int | None = Field(default=None, alias="id")
    nome: str | None = Field(default=None, alias="nome")
    tipo_pessoa: str | None = Field(default=None, alias="tipoPessoa")
    numero_documento: str | None = Field(default=None, alias="numeroDocumento")
    ie: str | None = Field(default=None, alias="ie")
    rg: str | None = Field(default=None, alias="rg")
    contribuinte: int | None = Field(default=None, alias="contribuinte")
    telefone: str | None = Field(default=None, alias="telefone")
    email: str | None = Field(default=None, alias="email")
    endereco: NotasFiscaisContatoEnderecoDTO | None = Field(default=None, alias="endereco")


class NotasFiscaisNaturezaOperacaoDTO(BlingModel):
    id: int | None = Field(default=None, alias="id")


class NotasFiscaisLojaDTO(BlingModel):
    id: int | None = Field(default=None, alias="id")
    numero: str | None = Field(default=None, alias="numero")


class NotasFiscaisVendedorDTO(BlingModel):
    id: int | None = Field(default=None, alias="id")


class NotasFiscaisIcmsDTO(BlingModel):
    st: int | None = Field(default=None, alias="st")
    origem: int | None = Field(default=None, alias="origem")
    modalidade: int | None = Field(default=None, alias="modalidade")
    aliquota: float | None = Field(default=None, alias="aliquota")
    valor: float | None = Field(default=None, alias="valor")


class NotasFiscaisImpostoDTO(BlingModel):
    valor_aproximado_total_tributos: float | None = Field(
        default=None, alias="valorAproximadoTotalTributos"
    )
    icms: NotasFiscaisIcmsDTO | None = Field(default=None, alias="icms")


class NotasFiscaisDocumentoReferenciadoItemDTO(BlingModel):
    """Referenced document for an item (WriteOnly)."""


class NotasFiscaisItemDTO(BlingModel):
    codigo: str | None = Field(default=None, alias="codigo")
    descricao: str | None = Field(default=None, alias="descricao")
    unidade: str | None = Field(default=None, alias="unidade")
    quantidade: float | None = Field(default=None, alias="quantidade")
    valor: float | None = Field(default=None, alias="valor")
    valor_total: float | None = Field(default=None, alias="valorTotal")
    tipo: str | None = Field(default=None, alias="tipo")
    peso_bruto: float | None = Field(default=None, alias="pesoBruto")
    peso_liquido: float | None = Field(default=None, alias="pesoLiquido")
    numero_pedido_compra: str | None = Field(default=None, alias="numeroPedidoCompra")
    classificacao_fiscal: str | None = Field(default=None, alias="classificacaoFiscal")
    cest: str | None = Field(default=None, alias="cest")
    codigo_servico: str | None = Field(default=None, alias="codigoServico")
    origem: int | None = Field(default=None, alias="origem")
    informacoes_adicionais: str | None = Field(default=None, alias="informacoesAdicionais")
    gtin: str | None = Field(default=None, alias="gtin")
    cfop: str | None = Field(default=None, alias="cfop")
    impostos: NotasFiscaisImpostoDTO | None = Field(default=None, alias="impostos")
    documento_referenciado: NotasFiscaisDocumentoReferenciadoItemDTO | None = Field(
        default=None, alias="documentoReferenciado"
    )


class NotasFiscaisParcelaFormaPagamentoDTO(BlingModel):
    id: int | None = Field(default=None, alias="id")


class NotasFiscaisParcelaDTO(BlingModel):
    data: str | None = Field(default=None, alias="data")
    valor: float | None = Field(default=None, alias="valor")
    observacoes: str | None = Field(default=None, alias="observacoes")
    caut: str | None = Field(default=None, alias="caut")
    forma_pagamento: NotasFiscaisParcelaFormaPagamentoDTO | None = Field(
        default=None, alias="formaPagamento"
    )


class NotasFiscaisDocumentoReferenciadoDTO(BlingModel):
    data: str | None = Field(default=None, alias="data")
    numero: str | None = Field(default=None, alias="numero")
    serie: str | None = Field(default=None, alias="serie")
    contador_ordem_operacao: str | None = Field(default=None, alias="contadorOrdemOperacao")
    chave_acesso: str | None = Field(default=None, alias="chaveAcesso")
    modelo: str | None = Field(default=None, alias="modelo")


class NotasFiscaisNotaFiscalProdutorRuralReferenciadaDTO(BlingModel):
    """Referenced rural producer invoice (WriteOnly)."""

    numero: str | None = Field(default=None, alias="numero")
    serie: str | None = Field(default=None, alias="serie")
    data: str | None = Field(default=None, alias="data")


class NotasFiscaisIntermediadorDTO(BlingModel):
    """Intermediary/marketplace (WriteOnly)."""

    cnpj: str | None = Field(default=None, alias="cnpj")
    nome_usuario: str | None = Field(default=None, alias="nomeUsuario")


# --- Transport sub-DTOs ---


class NotasFiscaisTransportadorEnderecoDTO(BlingModel):
    endereco: str | None = Field(default=None, alias="endereco")
    municipio: str | None = Field(default=None, alias="municipio")
    uf: str | None = Field(default=None, alias="uf")


class NotasFiscaisTransportadorGetDTO(BlingModel):
    nome: str | None = Field(default=None, alias="nome")
    numero_documento: str | None = Field(default=None, alias="numeroDocumento")


class NotasFiscaisTransportadorPostDTO(BlingModel):
    nome: str | None = Field(default=None, alias="nome")
    numero_documento: str | None = Field(default=None, alias="numeroDocumento")
    ie: str | None = Field(default=None, alias="ie")
    endereco: NotasFiscaisTransportadorEnderecoDTO | None = Field(default=None, alias="endereco")


class NotasFiscaisTransporteVeiculoDTO(BlingModel):
    placa: str | None = Field(default=None, alias="placa")
    uf: str | None = Field(default=None, alias="uf")
    marca: str | None = Field(default=None, alias="marca")


class NotasFiscaisTransporteVolumeGetDTO(BlingModel):
    id: int | None = Field(default=None, alias="id")


class NotasFiscaisTransporteDadosVolumeDTO(BlingModel):
    quantidade: float | None = Field(default=None, alias="quantidade")
    especie: str | None = Field(default=None, alias="especie")
    numero: str | None = Field(default=None, alias="numero")
    peso_bruto: float | None = Field(default=None, alias="pesoBruto")
    peso_liquido: float | None = Field(default=None, alias="pesoLiquido")


class NotasFiscaisTransporteVolumePostDTO(BlingModel):
    id: int | None = Field(default=None, alias="id")
    servico: str | None = Field(default=None, alias="servico")
    codigo_rastreamento: str | None = Field(default=None, alias="codigoRastreamento")
    dados_volume: NotasFiscaisTransporteDadosVolumeDTO | None = Field(
        default=None, alias="dadosVolume"
    )


class NotasFiscaisTransporteEtiquetaDTO(BlingModel):
    nome: str | None = Field(default=None, alias="nome")
    endereco: str | None = Field(default=None, alias="endereco")
    numero: str | None = Field(default=None, alias="numero")
    complemento: str | None = Field(default=None, alias="complemento")
    municipio: str | None = Field(default=None, alias="municipio")
    uf: str | None = Field(default=None, alias="uf")
    cep: str | None = Field(default=None, alias="cep")
    bairro: str | None = Field(default=None, alias="bairro")


class NotasFiscaisTransporteGetDTO(BlingModel):
    frete_por_conta: int | None = Field(default=None, alias="fretePorConta")
    transportador: NotasFiscaisTransportadorGetDTO | None = Field(
        default=None, alias="transportador"
    )
    volumes: list[NotasFiscaisTransporteVolumeGetDTO] = Field(default_factory=list, alias="volumes")
    etiqueta: NotasFiscaisTransporteEtiquetaDTO | None = Field(default=None, alias="etiqueta")


class NotasFiscaisTransportePostDTO(BlingModel):
    frete_por_conta: int | None = Field(default=None, alias="fretePorConta")
    frete: float | None = Field(default=None, alias="frete")
    transportador: NotasFiscaisTransportadorPostDTO | None = Field(
        default=None, alias="transportador"
    )
    veiculo: NotasFiscaisTransporteVeiculoDTO | None = Field(default=None, alias="veiculo")
    volume: NotasFiscaisTransporteVolumePostDTO | None = Field(default=None, alias="volume")
    volumes: list[NotasFiscaisTransporteVolumePostDTO] = Field(
        default_factory=list, alias="volumes"
    )
    etiqueta: NotasFiscaisTransporteEtiquetaDTO | None = Field(default=None, alias="etiqueta")


# --- Main DTOs ---


class NotasFiscaisDadosBaseDTO(BlingModel):
    """Base DTO for NF-e and NFC-e invoices."""

    id: int | None = Field(default=None, alias="id")
    tipo: int | None = Field(default=None, alias="tipo")
    situacao: int | None = Field(default=None, alias="situacao")
    numero: str | None = Field(default=None, alias="numero")
    data_emissao: str | None = Field(default=None, alias="dataEmissao")
    data_operacao: str | None = Field(default=None, alias="dataOperacao")
    chave_acesso: str | None = Field(default=None, alias="chaveAcesso")
    contato: NotasFiscaisContatoDTO | None = Field(default=None, alias="contato")
    natureza_operacao: NotasFiscaisNaturezaOperacaoDTO | None = Field(
        default=None, alias="naturezaOperacao"
    )
    loja: NotasFiscaisLojaDTO | None = Field(default=None, alias="loja")


class NotasFiscaisDadosPostDTO(BlingModel):
    """Additional data for NF-e/NFC-e POST and PUT requests."""

    finalidade: int | None = Field(default=None, alias="finalidade")
    tipo_nota: str | None = Field(default=None, alias="tipoNota")
    seguro: float | None = Field(default=None, alias="seguro")
    despesas: float | None = Field(default=None, alias="despesas")
    desconto: float | None = Field(default=None, alias="desconto")
    observacoes: str | None = Field(default=None, alias="observacoes")
    xml: str | None = Field(default=None, alias="xml")
    link_danfe: str | None = Field(default=None, alias="linkDanfe")
    link_pdf: str | None = Field(default=None, alias="linkPDF")
    documento_referenciado: NotasFiscaisDocumentoReferenciadoDTO | None = Field(
        default=None, alias="documentoReferenciado"
    )
    documentos_referenciados: list[NotasFiscaisDocumentoReferenciadoDTO] = Field(
        default_factory=list, alias="documentosReferenciados"
    )
    itens: list[NotasFiscaisItemDTO] = Field(default_factory=list, alias="itens")
    parcelas: list[NotasFiscaisParcelaDTO] = Field(default_factory=list, alias="parcelas")
    transporte: NotasFiscaisTransportePostDTO | None = Field(default=None, alias="transporte")
    nota_fiscal_produtor_rural_referenciada: (
        NotasFiscaisNotaFiscalProdutorRuralReferenciadaDTO | None
    ) = Field(default=None, alias="notaFiscalProdutorRuralReferenciada")
    intermediador: NotasFiscaisIntermediadorDTO | None = Field(default=None, alias="intermediador")


class NotasFiscaisDadosGetDTO(BlingModel):
    """Additional response fields for NF-e/NFC-e GET."""

    serie: int | None = Field(default=None, alias="serie")
    valor_nota: float | None = Field(default=None, alias="valorNota")
    valor_frete: float | None = Field(default=None, alias="valorFrete")
    finalidade: int | None = Field(default=None, alias="finalidade")
    tipo_nota: str | None = Field(default=None, alias="tipoNota")
    xml: str | None = Field(default=None, alias="xml")
    link_danfe: str | None = Field(default=None, alias="linkDanfe")
    link_pdf: str | None = Field(default=None, alias="linkPDF")
    optante_simples_nacional: bool | None = Field(default=None, alias="optanteSimplesNacional")
    numero_pedido_loja: str | None = Field(default=None, alias="numeroPedidoLoja")
    transporte: NotasFiscaisTransporteGetDTO | None = Field(default=None, alias="transporte")
    vendedor: NotasFiscaisVendedorDTO | None = Field(default=None, alias="vendedor")
    itens: list[NotasFiscaisItemDTO] = Field(default_factory=list, alias="itens")
    parcelas: list[NotasFiscaisParcelaDTO] = Field(default_factory=list, alias="parcelas")


class NotaFiscalResponseData(BlingModel):
    """Combined POST/PUT response data."""

    id: int | None = Field(default=None, alias="id")
    numero: str | None = Field(default=None, alias="numero")
    serie: str | None = Field(default=None, alias="serie")
    contato: dict[str, Any] | None = Field(default=None, alias="contato")


class NotaFiscalResponsePOST(BlingModel):
    """POST/PUT response data for NF-e/NFC-e."""

    data: NotaFiscalResponseData | dict[str, Any] | None = Field(default=None, alias="data")


class NotasFiscaisDocumentoDTO(BlingModel):
    """Document download response."""

    nome: str | None = Field(default=None, alias="nome")
    conteudo: str | None = Field(default=None, alias="conteudo")


class NotasFiscaisExclusaoDTO(BlingModel):
    """Mass deletion response."""

    alertas: list[str] = Field(default_factory=list, alias="alertas")
    ids_excluidos: list[int] = Field(default_factory=list, alias="idsExcluidos")


# --- List response wrapper for NF-e/NFC-e ---


class NotasFiscaisListResponse(BlingModel):
    data: list[NotasFiscaisDadosBaseDTO] = Field(default_factory=list, alias="data")


class NotaFiscalGetResponse(BlingModel):
    """Single NF-e/NFC-e get response."""

    data: dict[str, Any] | None = Field(default=None, alias="data")
