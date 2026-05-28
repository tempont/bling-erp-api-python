# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``pedidos_vendas``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import Data34, Data35, Data36, Data37, ErrorField, LojaUnidadeNegocioDTO


class VendasCategoriaDTO(BlingModel):
    """OpenAPI schema ``VendasCategoriaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class VendasCreateInvoiceResponseDTO(BlingModel):
    """OpenAPI schema ``VendasCreateInvoiceResponseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id_nota_fiscal: Bling ``idNotaFiscal``; type ``int``; obrigatório."""

    id_nota_fiscal: int = Field(..., alias="idNotaFiscal", examples=[12345678])


class VendasDescontoDTO(BlingModel):
    """OpenAPI schema ``VendasDescontoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        valor: Bling ``valor``; type ``float``; obrigatório.
        unidade: Bling ``unidade``; type ``str | None``; opcional."""

    valor: float = Field(..., examples=[15.45])
    unidade: str | None = "REAL"


class VendasIntermediadorDTO(BlingModel):
    """OpenAPI schema ``VendasIntermediadorDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        cnpj: Bling ``cnpj``; type ``str | None``; opcional.
        nome_usuario: Bling ``nomeUsuario``; type ``str | None``; opcional."""

    cnpj: str | None = Field(default=None, examples=["13921649000197"])
    nome_usuario: str | None = Field(default=None, alias="nomeUsuario", examples=["usuario"])


class VendasItemComissaoDTO(BlingModel):
    """OpenAPI schema ``VendasItemComissaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        base: Bling ``base``; type ``float | None``; opcional.
        aliquota: Bling ``aliquota``; type ``float | None``; opcional.
        valor: Bling ``valor``; type ``float | None``; opcional."""

    base: float | None = Field(default=None, examples=[10])
    aliquota: float | None = Field(default=None, examples=[2])
    valor: float | None = Field(default=None, examples=[0.2])


class VendasItemNaturezaOperacaoDTO(BlingModel):
    """OpenAPI schema ``VendasItemNaturezaOperacaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. ID da natureza de operação"""

    id: int | None = Field(default=None, examples=[12345678])


class VendasItemProdutoDTO(BlingModel):
    """OpenAPI schema ``VendasItemProdutoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class VendasLojaDTO(BlingModel):
    """OpenAPI schema ``VendasLojaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        unidade_negocio: Bling ``unidadeNegocio``; type ``LojaUnidadeNegocioDTO | None``; opcional."""

    id: int = Field(..., examples=[12345678])
    unidade_negocio: LojaUnidadeNegocioDTO | None = Field(default=None, alias="unidadeNegocio")


class VendasNotaFiscalDTO(BlingModel):
    """OpenAPI schema ``VendasNotaFiscalDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class VendasParcelaFormaPagamentoDTO(BlingModel):
    """OpenAPI schema ``VendasParcelaFormaPagamentoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class VendasSituacaoDTO(BlingModel):
    """OpenAPI schema ``VendasSituacaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        valor: Bling ``valor``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])
    valor: int = Field(..., examples=[1])


class VendasSituacaoDTOPUT(BlingModel):
    """OpenAPI schema ``VendasSituacaoDTOPUT``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        valor: Bling ``valor``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])
    valor: int = Field(..., examples=[1])


class VendasTaxaDTO(BlingModel):
    """OpenAPI schema ``VendasTaxaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        taxa_comissao: Bling ``taxaComissao``; type ``float | None``; opcional. Taxa de comissão perante ao total da venda.
        custo_frete: Bling ``custoFrete``; type ``float | None``; opcional. Valor de custo do frete.
        valor_base: Bling ``valorBase``; type ``float | None``; opcional. Valor base da venda para demonstrativo de cálculo das taxas via interface (Se não informado considera o total da venda)."""

    taxa_comissao: float | None = Field(default=None, alias="taxaComissao", examples=[1])
    custo_frete: float | None = Field(default=None, alias="custoFrete", examples=[9.99])
    valor_base: float | None = Field(default=None, alias="valorBase", examples=[129.9])


class VendasTransporteContatoDTO(BlingModel):
    """OpenAPI schema ``VendasTransporteContatoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        nome: Bling ``nome``; type ``str``; obrigatório."""

    id: int | None = Field(default=None, examples=[12345678])
    nome: str = Field(..., examples=["Transportador"])


class VendasTransporteEtiquetaDTO(BlingModel):
    """OpenAPI schema ``VendasTransporteEtiquetaDTO``.

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
        bairro: Bling ``bairro``; type ``str | None``; opcional.
        nome_pais: Bling ``nomePais``; type ``str | None``; opcional. Utilizado quando a UF for 'EX' (estrangeiro)."""

    nome: str | None = Field(default=None, examples=["Transportador"])
    endereco: str | None = Field(default=None, examples=["Olavo Bilac"])
    numero: str | None = Field(default=None, examples=["914"])
    complemento: str | None = Field(default=None, examples=["Sala 101"])
    municipio: str | None = Field(default=None, examples=["Bento Gonçalves"])
    uf: str | None = Field(default=None, examples=["RS"])
    cep: str | None = Field(default=None, examples=["95702-000"])
    bairro: str | None = Field(default=None, examples=["Imigrante"])
    nome_pais: str | None = Field(default=None, alias="nomePais", examples=["BRASIL"])


class VendasTransporteVolumeDTO(BlingModel):
    """OpenAPI schema ``VendasTransporteVolumeDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. Ignorado no método POST.
        servico: Bling ``servico``; type ``str``; obrigatório.
        codigo_rastreamento: Bling ``codigoRastreamento``; type ``str | None``; opcional."""

    id: int = Field(..., examples=[12345678])
    servico: str = Field(..., examples=["ALIAS_123"])
    codigo_rastreamento: str | None = Field(
        default=None, alias="codigoRastreamento", examples=["COD123BR"]
    )


class VendasTributacaoDTO(BlingModel):
    """OpenAPI schema ``VendasTributacaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        total_icms: Bling ``totalICMS``; type ``float | None``; opcional.
        total_ipi: Bling ``totalIPI``; type ``float | None``; opcional."""

    total_icms: float | None = Field(default=None, alias="totalICMS", examples=[5.55])
    total_ipi: float | None = Field(default=None, alias="totalIPI", examples=[5.55])


class VendasContatoDTO(BlingModel):
    """OpenAPI schema ``VendasContatoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        nome: Bling ``nome``; type ``str``; obrigatório.
        tipo_pessoa: Bling ``tipoPessoa``; type ``str | None``; opcional. `F` Física<br> `J` Jurídica<br> `E` Estrangeira
        numero_documento: Bling ``numeroDocumento``; type ``str | None``; opcional. CNPJ ou CPF."""

    id: int = Field(..., examples=[12345678])
    nome: str = Field(..., examples=["Contato do Bling"])
    tipo_pessoa: str | None = Field(default=None, alias="tipoPessoa", examples=["J"])
    numero_documento: str | None = Field(
        default=None, alias="numeroDocumento", examples=["30188025000121"]
    )


class VendasVendedorDTO(BlingModel):
    """OpenAPI schema ``VendasVendedorDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class PedidosVendasDeleteResponse200(BlingModel):
    """OpenAPI schema ``PedidosVendasDeleteResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data35 | None``; opcional."""

    data: Data35 | None = None


class VendasDadosBaseDTO(BlingModel):
    """OpenAPI schema ``VendasDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        numero: Bling ``numero``; type ``int | None``; opcional.
        numero_loja: Bling ``numeroLoja``; type ``str | None``; opcional.
        data: Bling ``data``; type ``date``; obrigatório. Valor obrigatório caso parâmetro de geração de parcelas seja este
        data_saida: Bling ``dataSaida``; type ``date``; obrigatório. Valor obrigatório caso parâmetro de geração de parcelas seja este
        data_prevista: Bling ``dataPrevista``; type ``date``; obrigatório. Valor obrigatório caso parâmetro de geração de parcelas seja este
        total_produtos: Bling ``totalProdutos``; type ``float | None``; opcional.
        total: Bling ``total``; type ``float | None``; opcional.
        contato: Bling ``contato``; type ``VendasContatoDTO``; obrigatório.
        situacao: Bling ``situacao``; type ``VendasSituacaoDTO | None``; opcional.
        loja: Bling ``loja``; type ``VendasLojaDTO | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    numero: int | None = Field(default=None, examples=[123])
    numero_loja: str | None = Field(default=None, alias="numeroLoja", examples=["Loja_123"])
    data: date = Field(..., examples=["2023-01-12"])
    data_saida: date = Field(..., alias="dataSaida", examples=["2023-01-12"])
    data_prevista: date = Field(..., alias="dataPrevista", examples=["2023-01-12"])
    total_produtos: float | None = Field(default=None, alias="totalProdutos", examples=[10])
    total: float | None = Field(default=None, examples=[12])
    contato: VendasContatoDTO
    situacao: VendasSituacaoDTO | None = None
    loja: VendasLojaDTO | None = None


class VendasDadosBaseDTOPUT(BlingModel):
    """OpenAPI schema ``VendasDadosBaseDTOPUT``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        numero: Bling ``numero``; type ``int | None``; opcional.
        numero_loja: Bling ``numeroLoja``; type ``str | None``; opcional.
        data: Bling ``data``; type ``date``; obrigatório. Valor obrigatório caso parâmetro de geração de parcelas seja este
        data_saida: Bling ``dataSaida``; type ``date``; obrigatório. Valor obrigatório caso parâmetro de geração de parcelas seja este
        data_prevista: Bling ``dataPrevista``; type ``date``; obrigatório. Valor obrigatório caso parâmetro de geração de parcelas seja este
        total_produtos: Bling ``totalProdutos``; type ``float | None``; opcional.
        total: Bling ``total``; type ``float | None``; opcional.
        contato: Bling ``contato``; type ``VendasContatoDTO``; obrigatório.
        situacao: Bling ``situacao``; type ``VendasSituacaoDTOPUT | None``; opcional.
        loja: Bling ``loja``; type ``VendasLojaDTO | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    numero: int | None = Field(default=None, examples=[123])
    numero_loja: str | None = Field(default=None, alias="numeroLoja", examples=["Loja_123"])
    data: date = Field(..., examples=["2023-01-12"])
    data_saida: date = Field(..., alias="dataSaida", examples=["2023-01-12"])
    data_prevista: date = Field(..., alias="dataPrevista", examples=["2023-01-12"])
    total_produtos: float | None = Field(default=None, alias="totalProdutos", examples=[10])
    total: float | None = Field(default=None, examples=[12])
    contato: VendasContatoDTO
    situacao: VendasSituacaoDTOPUT | None = None
    loja: VendasLojaDTO | None = None


class VendasItemDTO(BlingModel):
    """OpenAPI schema ``VendasItemDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. Ignorado no método POST.
        codigo: Bling ``codigo``; type ``str | None``; opcional.
        unidade: Bling ``unidade``; type ``str | None``; opcional.
        quantidade: Bling ``quantidade``; type ``float``; obrigatório.
        desconto: Bling ``desconto``; type ``float | None``; opcional. Valor percentual.
        valor: Bling ``valor``; type ``float``; obrigatório. Valor unitário do item. Preço de lista = 4.9 (valor) + 2% (desconto)
        aliquota_ipi: Bling ``aliquotaIPI``; type ``float | None``; opcional.
        descricao: Bling ``descricao``; type ``str``; obrigatório.
        descricao_detalhada: Bling ``descricaoDetalhada``; type ``str | None``; opcional.
        produto: Bling ``produto``; type ``VendasItemProdutoDTO | None``; opcional.
        comissao: Bling ``comissao``; type ``VendasItemComissaoDTO | None``; opcional.
        natureza_operacao: Bling ``naturezaOperacao``; type ``VendasItemNaturezaOperacaoDTO | None``; opcional."""

    id: int = Field(..., examples=[12345678])
    codigo: str | None = Field(default=None, examples=["BLG-5"])
    unidade: str | None = Field(default=None, examples=["UN"])
    quantidade: float = Field(..., examples=[1])
    desconto: float | None = Field(default=None, examples=[2])
    valor: float = Field(..., examples=[4.9])
    aliquota_ipi: float | None = Field(default=None, alias="aliquotaIPI", examples=[0])
    descricao: str = Field(..., examples=["Produto do Bling"])
    descricao_detalhada: str | None = Field(
        default=None, alias="descricaoDetalhada", examples=["Brinde"]
    )
    produto: VendasItemProdutoDTO | None = None
    comissao: VendasItemComissaoDTO | None = None
    natureza_operacao: VendasItemNaturezaOperacaoDTO | None = Field(
        default=None, alias="naturezaOperacao"
    )


class VendasParcelaDTO(BlingModel):
    """OpenAPI schema ``VendasParcelaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. Ignorado no método POST.
        data_vencimento: Bling ``dataVencimento``; type ``date``; obrigatório.
        valor: Bling ``valor``; type ``float``; obrigatório.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        caut: Bling ``caut``; type ``str | None``; opcional. cAut (ou NSU): código de autorização da operação financeira
        forma_pagamento: Bling ``formaPagamento``; type ``VendasParcelaFormaPagamentoDTO``; obrigatório."""

    id: int = Field(..., examples=[12345678])
    data_vencimento: date = Field(..., alias="dataVencimento", examples=["2023-01-12"])
    valor: float = Field(..., examples=[123.45])
    observacoes: str | None = Field(default=None, examples=["Observação da parcela"])
    caut: str | None = Field(default=None, examples=["123456789"])
    forma_pagamento: VendasParcelaFormaPagamentoDTO = Field(..., alias="formaPagamento")


class VendasTransporteDTO(BlingModel):
    """OpenAPI schema ``VendasTransporteDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        frete_por_conta: Bling ``fretePorConta``; type ``int | None``; opcional. `0` Contratação do Frete por conta do Remetente (CIF)<br> `1` Contratação do Frete por conta do Destinatário (FOB)<br> `2` Contratação do Frete por conta de Terceiros<br> `3` Tran...
        frete: Bling ``frete``; type ``float | None``; opcional.
        quantidade_volumes: Bling ``quantidadeVolumes``; type ``int | None``; opcional.
        peso_bruto: Bling ``pesoBruto``; type ``float | None``; opcional.
        prazo_entrega: Bling ``prazoEntrega``; type ``int | None``; opcional.
        contato: Bling ``contato``; type ``VendasTransporteContatoDTO | None``; opcional.
        etiqueta: Bling ``etiqueta``; type ``VendasTransporteEtiquetaDTO | None``; opcional.
        volumes: Bling ``volumes``; type ``list[VendasTransporteVolumeDTO] | None``; opcional."""

    frete_por_conta: int | None = Field(default=None, alias="fretePorConta", examples=[0])
    frete: float | None = Field(default=None, examples=[20])
    quantidade_volumes: int | None = Field(default=None, alias="quantidadeVolumes", examples=[1])
    peso_bruto: float | None = Field(default=None, alias="pesoBruto", examples=[0.5])
    prazo_entrega: int | None = Field(default=None, alias="prazoEntrega", examples=[10])
    contato: VendasTransporteContatoDTO | None = None
    etiqueta: VendasTransporteEtiquetaDTO | None = None
    volumes: list[VendasTransporteVolumeDTO] | None = None


class PedidosVendasGetResponse200(BlingModel):
    """OpenAPI schema ``PedidosVendasGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[VendasDadosBaseDTO] | None``; opcional."""

    data: list[VendasDadosBaseDTO] | None = None


class VendasDadosDTO(BlingModel):
    """OpenAPI schema ``VendasDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        numero_pedido_compra: Bling ``numeroPedidoCompra``; type ``str | None``; opcional. Número da ordem de compra do pedido.
        outras_despesas: Bling ``outrasDespesas``; type ``float | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        observacoes_internas: Bling ``observacoesInternas``; type ``str | None``; opcional.
        desconto: Bling ``desconto``; type ``VendasDescontoDTO | None``; opcional.
        categoria: Bling ``categoria``; type ``VendasCategoriaDTO | None``; opcional.
        nota_fiscal: Bling ``notaFiscal``; type ``VendasNotaFiscalDTO | None``; opcional.
        tributacao: Bling ``tributacao``; type ``VendasTributacaoDTO | None``; opcional.
        itens: Bling ``itens``; type ``list[VendasItemDTO]``; obrigatório.
        parcelas: Bling ``parcelas``; type ``list[VendasParcelaDTO]``; obrigatório.
        transporte: Bling ``transporte``; type ``VendasTransporteDTO | None``; opcional.
        vendedor: Bling ``vendedor``; type ``VendasVendedorDTO | None``; opcional.
        intermediador: Bling ``intermediador``; type ``VendasIntermediadorDTO | None``; opcional.
        taxas: Bling ``taxas``; type ``VendasTaxaDTO | None``; opcional."""

    numero_pedido_compra: str | None = Field(
        default=None, alias="numeroPedidoCompra", examples=["123"]
    )
    outras_despesas: float | None = Field(default=None, alias="outrasDespesas", examples=[2])
    observacoes: str | None = Field(default=None, examples=["Observações do pedido."])
    observacoes_internas: str | None = Field(
        default=None, alias="observacoesInternas", examples=["Observações internas do pedido."]
    )
    desconto: VendasDescontoDTO | None = None
    categoria: VendasCategoriaDTO | None = None
    nota_fiscal: VendasNotaFiscalDTO | None = Field(default=None, alias="notaFiscal")
    tributacao: VendasTributacaoDTO | None = None
    itens: list[VendasItemDTO]
    parcelas: list[VendasParcelaDTO]
    transporte: VendasTransporteDTO | None = None
    vendedor: VendasVendedorDTO | None = None
    intermediador: VendasIntermediadorDTO | None = None
    taxas: VendasTaxaDTO | None = None


class VendasResponsePOSTPUT(BlingModel):
    """OpenAPI schema ``VendasResponsePOSTPUT``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        alertas: Bling ``alertas``; type ``list[ErrorField] | None``; opcional.
        rastreamento: Bling ``rastreamento``; type ``dict[str, Any] | None``; opcional. Dados de rastreamento."""

    alertas: list[ErrorField] | None = None
    rastreamento: dict[str, Any] | None = None


class PedidosVendasPostRequest(VendasDadosBaseDTO, VendasDadosDTO):
    """OpenAPI schema ``PedidosVendasPostRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: VendasDadosBaseDTO, VendasDadosDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        numero: Bling ``numero``; type ``int | None``; opcional.
        numero_loja: Bling ``numeroLoja``; type ``str | None``; opcional.
        data: Bling ``data``; type ``date``; obrigatório. Valor obrigatório caso parâmetro de geração de parcelas seja este
        data_saida: Bling ``dataSaida``; type ``date``; obrigatório. Valor obrigatório caso parâmetro de geração de parcelas seja este
        data_prevista: Bling ``dataPrevista``; type ``date``; obrigatório. Valor obrigatório caso parâmetro de geração de parcelas seja este
        total_produtos: Bling ``totalProdutos``; type ``float | None``; opcional.
        total: Bling ``total``; type ``float | None``; opcional.
        contato: Bling ``contato``; type ``VendasContatoDTO``; obrigatório.
        situacao: Bling ``situacao``; type ``VendasSituacaoDTO | None``; opcional.
        loja: Bling ``loja``; type ``VendasLojaDTO | None``; opcional.
        numero_pedido_compra: Bling ``numeroPedidoCompra``; type ``str | None``; opcional. Número da ordem de compra do pedido.
        outras_despesas: Bling ``outrasDespesas``; type ``float | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        observacoes_internas: Bling ``observacoesInternas``; type ``str | None``; opcional.
        desconto: Bling ``desconto``; type ``VendasDescontoDTO | None``; opcional.
        categoria: Bling ``categoria``; type ``VendasCategoriaDTO | None``; opcional.
        nota_fiscal: Bling ``notaFiscal``; type ``VendasNotaFiscalDTO | None``; opcional.
        tributacao: Bling ``tributacao``; type ``VendasTributacaoDTO | None``; opcional.
        itens: Bling ``itens``; type ``list[VendasItemDTO]``; obrigatório.
        parcelas: Bling ``parcelas``; type ``list[VendasParcelaDTO]``; obrigatório.
        transporte: Bling ``transporte``; type ``VendasTransporteDTO | None``; opcional.
        vendedor: Bling ``vendedor``; type ``VendasVendedorDTO | None``; opcional.
        intermediador: Bling ``intermediador``; type ``VendasIntermediadorDTO | None``; opcional.
        taxas: Bling ``taxas``; type ``VendasTaxaDTO | None``; opcional."""

    pass


class PedidosVendasPostResponse201(BlingModel):
    """OpenAPI schema ``PedidosVendasPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data34 | None``; opcional."""

    data: Data34 | None = None


class PedidosVendasIdPedidoVendaGetResponse200(BlingModel):
    """OpenAPI schema ``PedidosVendasIdPedidoVendaGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data36 | None``; opcional."""

    data: Data36 | None = None


class PedidosVendasIdPedidoVendaPutRequest(VendasDadosBaseDTOPUT, VendasDadosDTO):
    """OpenAPI schema ``PedidosVendasIdPedidoVendaPutRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: VendasDadosBaseDTOPUT, VendasDadosDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        numero: Bling ``numero``; type ``int | None``; opcional.
        numero_loja: Bling ``numeroLoja``; type ``str | None``; opcional.
        data: Bling ``data``; type ``date``; obrigatório. Valor obrigatório caso parâmetro de geração de parcelas seja este
        data_saida: Bling ``dataSaida``; type ``date``; obrigatório. Valor obrigatório caso parâmetro de geração de parcelas seja este
        data_prevista: Bling ``dataPrevista``; type ``date``; obrigatório. Valor obrigatório caso parâmetro de geração de parcelas seja este
        total_produtos: Bling ``totalProdutos``; type ``float | None``; opcional.
        total: Bling ``total``; type ``float | None``; opcional.
        contato: Bling ``contato``; type ``VendasContatoDTO``; obrigatório.
        situacao: Bling ``situacao``; type ``VendasSituacaoDTOPUT | None``; opcional.
        loja: Bling ``loja``; type ``VendasLojaDTO | None``; opcional.
        numero_pedido_compra: Bling ``numeroPedidoCompra``; type ``str | None``; opcional. Número da ordem de compra do pedido.
        outras_despesas: Bling ``outrasDespesas``; type ``float | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        observacoes_internas: Bling ``observacoesInternas``; type ``str | None``; opcional.
        desconto: Bling ``desconto``; type ``VendasDescontoDTO | None``; opcional.
        categoria: Bling ``categoria``; type ``VendasCategoriaDTO | None``; opcional.
        nota_fiscal: Bling ``notaFiscal``; type ``VendasNotaFiscalDTO | None``; opcional.
        tributacao: Bling ``tributacao``; type ``VendasTributacaoDTO | None``; opcional.
        itens: Bling ``itens``; type ``list[VendasItemDTO]``; obrigatório.
        parcelas: Bling ``parcelas``; type ``list[VendasParcelaDTO]``; obrigatório.
        transporte: Bling ``transporte``; type ``VendasTransporteDTO | None``; opcional.
        vendedor: Bling ``vendedor``; type ``VendasVendedorDTO | None``; opcional.
        intermediador: Bling ``intermediador``; type ``VendasIntermediadorDTO | None``; opcional.
        taxas: Bling ``taxas``; type ``VendasTaxaDTO | None``; opcional."""

    pass


class PedidosVendasIdPedidoVendaPutResponse200(BlingModel):
    """OpenAPI schema ``PedidosVendasIdPedidoVendaPutResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data37 | None``; opcional."""

    data: Data37 | None = None


__all__ = [
    "PedidosVendasDeleteResponse200",
    "PedidosVendasGetResponse200",
    "PedidosVendasIdPedidoVendaGetResponse200",
    "PedidosVendasIdPedidoVendaPutRequest",
    "PedidosVendasIdPedidoVendaPutResponse200",
    "PedidosVendasPostRequest",
    "PedidosVendasPostResponse201",
    "VendasCategoriaDTO",
    "VendasContatoDTO",
    "VendasCreateInvoiceResponseDTO",
    "VendasDadosBaseDTO",
    "VendasDadosBaseDTOPUT",
    "VendasDadosDTO",
    "VendasDescontoDTO",
    "VendasIntermediadorDTO",
    "VendasItemComissaoDTO",
    "VendasItemDTO",
    "VendasItemNaturezaOperacaoDTO",
    "VendasItemProdutoDTO",
    "VendasLojaDTO",
    "VendasNotaFiscalDTO",
    "VendasParcelaDTO",
    "VendasParcelaFormaPagamentoDTO",
    "VendasResponsePOSTPUT",
    "VendasSituacaoDTO",
    "VendasSituacaoDTOPUT",
    "VendasTaxaDTO",
    "VendasTransporteContatoDTO",
    "VendasTransporteDTO",
    "VendasTransporteEtiquetaDTO",
    "VendasTransporteVolumeDTO",
    "VendasTributacaoDTO",
    "VendasVendedorDTO",
]
