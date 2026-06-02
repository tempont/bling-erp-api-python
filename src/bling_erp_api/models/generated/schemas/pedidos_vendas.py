# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``pedidos_vendas``. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.models.fields import BlingDate
from typing import TYPE_CHECKING, Any

from pydantic import AliasChoices, AwareDatetime, Field, RootModel

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

    id_nota_fiscal: int = Field(
        ...,
        validation_alias=AliasChoices("id_nota_fiscal", "idNotaFiscal"),
        examples=[12345678],
        serialization_alias="idNotaFiscal",
    )


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
    nome_usuario: str | None = Field(
        default=None,
        validation_alias=AliasChoices("nome_usuario", "nomeUsuario"),
        examples=["usuario"],
        serialization_alias="nomeUsuario",
    )


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
    unidade_negocio: LojaUnidadeNegocioDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("unidade_negocio", "unidadeNegocio"),
        serialization_alias="unidadeNegocio",
    )


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

    taxa_comissao: float | None = Field(
        default=None,
        validation_alias=AliasChoices("taxa_comissao", "taxaComissao"),
        examples=[1],
        serialization_alias="taxaComissao",
    )
    custo_frete: float | None = Field(
        default=None,
        validation_alias=AliasChoices("custo_frete", "custoFrete"),
        examples=[9.99],
        serialization_alias="custoFrete",
    )
    valor_base: float | None = Field(
        default=None,
        validation_alias=AliasChoices("valor_base", "valorBase"),
        examples=[129.9],
        serialization_alias="valorBase",
    )


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
    nome_pais: str | None = Field(
        default=None,
        validation_alias=AliasChoices("nome_pais", "nomePais"),
        examples=["BRASIL"],
        serialization_alias="nomePais",
    )


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
        default=None,
        validation_alias=AliasChoices("codigo_rastreamento", "codigoRastreamento"),
        examples=["COD123BR"],
        serialization_alias="codigoRastreamento",
    )


class VendasTributacaoDTO(BlingModel):
    """OpenAPI schema ``VendasTributacaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        total_icms: Bling ``totalICMS``; type ``float | None``; opcional.
        total_ipi: Bling ``totalIPI``; type ``float | None``; opcional."""

    total_icms: float | None = Field(
        default=None,
        validation_alias=AliasChoices("total_icms", "totalICMS"),
        examples=[5.55],
        serialization_alias="totalICMS",
    )
    total_ipi: float | None = Field(
        default=None,
        validation_alias=AliasChoices("total_ipi", "totalIPI"),
        examples=[5.55],
        serialization_alias="totalIPI",
    )


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
    tipo_pessoa: str | None = Field(
        default=None,
        validation_alias=AliasChoices("tipo_pessoa", "tipoPessoa"),
        examples=["J"],
        serialization_alias="tipoPessoa",
    )
    numero_documento: str | None = Field(
        default=None,
        validation_alias=AliasChoices("numero_documento", "numeroDocumento"),
        examples=["30188025000121"],
        serialization_alias="numeroDocumento",
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
        data: Bling ``data``; type ``BlingDate``; obrigatório. Valor obrigatório caso parâmetro de geração de parcelas seja este
        data_saida: Bling ``dataSaida``; type ``BlingDate``; obrigatório. Valor obrigatório caso parâmetro de geração de parcelas seja este
        data_prevista: Bling ``dataPrevista``; type ``BlingDate``; obrigatório. Valor obrigatório caso parâmetro de geração de parcelas seja este
        total_produtos: Bling ``totalProdutos``; type ``float | None``; opcional.
        total: Bling ``total``; type ``float | None``; opcional.
        contato: Bling ``contato``; type ``VendasContatoDTO``; obrigatório.
        situacao: Bling ``situacao``; type ``VendasSituacaoDTO | None``; opcional.
        loja: Bling ``loja``; type ``VendasLojaDTO | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    numero: int | None = Field(default=None, examples=[123])
    numero_loja: str | None = Field(
        default=None,
        validation_alias=AliasChoices("numero_loja", "numeroLoja"),
        examples=["Loja_123"],
        serialization_alias="numeroLoja",
    )
    data: BlingDate = Field(..., examples=["2023-01-12"])
    data_saida: BlingDate = Field(
        ...,
        validation_alias=AliasChoices("data_saida", "dataSaida"),
        examples=["2023-01-12"],
        serialization_alias="dataSaida",
    )
    data_prevista: BlingDate = Field(
        ...,
        validation_alias=AliasChoices("data_prevista", "dataPrevista"),
        examples=["2023-01-12"],
        serialization_alias="dataPrevista",
    )
    total_produtos: float | None = Field(
        default=None,
        validation_alias=AliasChoices("total_produtos", "totalProdutos"),
        examples=[10],
        serialization_alias="totalProdutos",
    )
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
        data: Bling ``data``; type ``BlingDate``; obrigatório. Valor obrigatório caso parâmetro de geração de parcelas seja este
        data_saida: Bling ``dataSaida``; type ``BlingDate``; obrigatório. Valor obrigatório caso parâmetro de geração de parcelas seja este
        data_prevista: Bling ``dataPrevista``; type ``BlingDate``; obrigatório. Valor obrigatório caso parâmetro de geração de parcelas seja este
        total_produtos: Bling ``totalProdutos``; type ``float | None``; opcional.
        total: Bling ``total``; type ``float | None``; opcional.
        contato: Bling ``contato``; type ``VendasContatoDTO``; obrigatório.
        situacao: Bling ``situacao``; type ``VendasSituacaoDTOPUT | None``; opcional.
        loja: Bling ``loja``; type ``VendasLojaDTO | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    numero: int | None = Field(default=None, examples=[123])
    numero_loja: str | None = Field(
        default=None,
        validation_alias=AliasChoices("numero_loja", "numeroLoja"),
        examples=["Loja_123"],
        serialization_alias="numeroLoja",
    )
    data: BlingDate = Field(..., examples=["2023-01-12"])
    data_saida: BlingDate = Field(
        ...,
        validation_alias=AliasChoices("data_saida", "dataSaida"),
        examples=["2023-01-12"],
        serialization_alias="dataSaida",
    )
    data_prevista: BlingDate = Field(
        ...,
        validation_alias=AliasChoices("data_prevista", "dataPrevista"),
        examples=["2023-01-12"],
        serialization_alias="dataPrevista",
    )
    total_produtos: float | None = Field(
        default=None,
        validation_alias=AliasChoices("total_produtos", "totalProdutos"),
        examples=[10],
        serialization_alias="totalProdutos",
    )
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
    aliquota_ipi: float | None = Field(
        default=None,
        validation_alias=AliasChoices("aliquota_ipi", "aliquotaIPI"),
        examples=[0],
        serialization_alias="aliquotaIPI",
    )
    descricao: str = Field(..., examples=["Produto do Bling"])
    descricao_detalhada: str | None = Field(
        default=None,
        validation_alias=AliasChoices("descricao_detalhada", "descricaoDetalhada"),
        examples=["Brinde"],
        serialization_alias="descricaoDetalhada",
    )
    produto: VendasItemProdutoDTO | None = None
    comissao: VendasItemComissaoDTO | None = None
    natureza_operacao: VendasItemNaturezaOperacaoDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("natureza_operacao", "naturezaOperacao"),
        serialization_alias="naturezaOperacao",
    )


class VendasParcelaDTO(BlingModel):
    """OpenAPI schema ``VendasParcelaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório. Ignorado no método POST.
        data_vencimento: Bling ``dataVencimento``; type ``BlingDate``; obrigatório.
        valor: Bling ``valor``; type ``float``; obrigatório.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        caut: Bling ``caut``; type ``str | None``; opcional. cAut (ou NSU): código de autorização da operação financeira
        forma_pagamento: Bling ``formaPagamento``; type ``VendasParcelaFormaPagamentoDTO``; obrigatório."""

    id: int = Field(..., examples=[12345678])
    data_vencimento: BlingDate = Field(
        ...,
        validation_alias=AliasChoices("data_vencimento", "dataVencimento"),
        examples=["2023-01-12"],
        serialization_alias="dataVencimento",
    )
    valor: float = Field(..., examples=[123.45])
    observacoes: str | None = Field(default=None, examples=["Observação da parcela"])
    caut: str | None = Field(default=None, examples=["123456789"])
    forma_pagamento: VendasParcelaFormaPagamentoDTO = Field(
        ...,
        validation_alias=AliasChoices("forma_pagamento", "formaPagamento"),
        serialization_alias="formaPagamento",
    )


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

    frete_por_conta: int | None = Field(
        default=None,
        validation_alias=AliasChoices("frete_por_conta", "fretePorConta"),
        examples=[0],
        serialization_alias="fretePorConta",
    )
    frete: float | None = Field(default=None, examples=[20])
    quantidade_volumes: int | None = Field(
        default=None,
        validation_alias=AliasChoices("quantidade_volumes", "quantidadeVolumes"),
        examples=[1],
        serialization_alias="quantidadeVolumes",
    )
    peso_bruto: float | None = Field(
        default=None,
        validation_alias=AliasChoices("peso_bruto", "pesoBruto"),
        examples=[0.5],
        serialization_alias="pesoBruto",
    )
    prazo_entrega: int | None = Field(
        default=None,
        validation_alias=AliasChoices("prazo_entrega", "prazoEntrega"),
        examples=[10],
        serialization_alias="prazoEntrega",
    )
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
        default=None,
        validation_alias=AliasChoices("numero_pedido_compra", "numeroPedidoCompra"),
        examples=["123"],
        serialization_alias="numeroPedidoCompra",
    )
    outras_despesas: float | None = Field(
        default=None,
        validation_alias=AliasChoices("outras_despesas", "outrasDespesas"),
        examples=[2],
        serialization_alias="outrasDespesas",
    )
    observacoes: str | None = Field(default=None, examples=["Observações do pedido."])
    observacoes_internas: str | None = Field(
        default=None,
        validation_alias=AliasChoices("observacoes_internas", "observacoesInternas"),
        examples=["Observações internas do pedido."],
        serialization_alias="observacoesInternas",
    )
    desconto: VendasDescontoDTO | None = None
    categoria: VendasCategoriaDTO | None = None
    nota_fiscal: VendasNotaFiscalDTO | None = Field(
        default=None,
        validation_alias=AliasChoices("nota_fiscal", "notaFiscal"),
        serialization_alias="notaFiscal",
    )
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
