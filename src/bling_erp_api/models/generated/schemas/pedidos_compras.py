# ruff: noqa
# pyright: reportIncompatibleVariableOverride=false, reportUnusedImport=false
"""Generated OpenAPI schemas for ``pedidos_compras``. Do not edit manually."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, Any

from pydantic import AwareDatetime, Field, RootModel

from bling_erp_api.models.base import BlingModel

if TYPE_CHECKING:
    from .common import Data25, Data26


class PedidosComprasCategoriaDTO(BlingModel):
    """OpenAPI schema ``PedidosComprasCategoriaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class PedidosComprasDescontoDTO(BlingModel):
    """OpenAPI schema ``PedidosComprasDescontoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        valor: Bling ``valor``; type ``float``; obrigatório.
        unidade: Bling ``unidade``; type ``str | None``; opcional."""

    valor: float = Field(..., examples=[15.45])
    unidade: str | None = "REAL"


class PedidosComprasFormaPagamentoDTO(BlingModel):
    """OpenAPI schema ``PedidosComprasFormaPagamentoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class PedidosComprasFornecedorDTO(BlingModel):
    """OpenAPI schema ``PedidosComprasFornecedorDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório."""

    id: int = Field(..., examples=[12345678])


class PedidosComprasItemNotaFiscalDTO(BlingModel):
    """OpenAPI schema ``PedidosComprasItemNotaFiscalDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional. ID da nota fiscal vinculada ao pedido de compra.
        quantidade: Bling ``quantidade``; type ``float | None``; opcional. Quantidade do item no pedido que foi vinculada a uma nota de entrada."""

    id: int | None = Field(default=None, examples=[12345678])
    quantidade: float | None = Field(default=None, examples=[5])


class PedidosComprasParcelaDTO(BlingModel):
    """OpenAPI schema ``PedidosComprasParcelaDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        valor: Bling ``valor``; type ``float``; obrigatório.
        data_vencimento: Bling ``dataVencimento``; type ``date``; obrigatório.
        observacao: Bling ``observacao``; type ``str | None``; opcional.
        forma_pagamento: Bling ``formaPagamento``; type ``PedidosComprasFormaPagamentoDTO | None``; opcional."""

    valor: float = Field(..., examples=[2090.66])
    data_vencimento: date = Field(..., alias="dataVencimento", examples=["2020-09-23"])
    observacao: str | None = Field(default=None, examples=["Observação da parcela."])
    forma_pagamento: PedidosComprasFormaPagamentoDTO | None = Field(
        default=None, alias="formaPagamento"
    )


class PedidosComprasProdutoDTO(BlingModel):
    """OpenAPI schema ``PedidosComprasProdutoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        codigo: Bling ``codigo``; type ``str | None``; opcional."""

    id: int = Field(..., examples=[12345678])
    codigo: str | None = Field(default=None, examples=["CODE123"])


class PedidosComprasSituacaoDTO(BlingModel):
    """OpenAPI schema ``PedidosComprasSituacaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        valor: Bling ``valor``; type ``int``; obrigatório. `0` Em aberto <br> `1` Atendido <br> `2` Cancelado <br> `3` Em andamento <br> Ignorado no método POST."""

    id: int = Field(..., examples=[12345678])
    valor: int = Field(..., examples=[0])


class PedidosComprasTransporteDTO(BlingModel):
    """OpenAPI schema ``PedidosComprasTransporteDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        frete: Bling ``frete``; type ``float | None``; opcional.
        transportador: Bling ``transportador``; type ``str | None``; opcional.
        frete_por_conta: Bling ``fretePorConta``; type ``int | None``; opcional. `0` Contratação do Frete por conta do Remetente (CIF) <br> `1` Contratação do Frete por conta do Destinatário (FOB) <br> `2` Contratação do Frete por conta de Terceiros <br> `3` T...
        peso_bruto: Bling ``pesoBruto``; type ``float | None``; opcional.
        volumes: Bling ``volumes``; type ``int | None``; opcional."""

    frete: float | None = Field(default=None, examples=[15.78])
    transportador: str | None = Field(default=None, examples=["Zé Transportes"])
    frete_por_conta: int | None = Field(default=1, alias="fretePorConta", examples=[0])
    peso_bruto: float | None = Field(default=None, alias="pesoBruto", examples=[15.78])
    volumes: int | None = Field(default=None, examples=[11])


class PedidosComprasTributacaoDTO(BlingModel):
    """OpenAPI schema ``PedidosComprasTributacaoDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        total_icms: Bling ``totalICMS``; type ``float | None``; opcional.
        total_ipi: Bling ``totalIPI``; type ``float | None``; opcional. Calculado automaticamente com base no IPI dos itens."""

    total_icms: float | None = Field(default=None, alias="totalICMS", examples=[5.55])
    total_ipi: float | None = Field(default=None, alias="totalIPI", examples=[5.55])


class PedidosCompraResponsePOSTPUT(BlingModel):
    """OpenAPI schema ``PedidosCompraResponsePOSTPUT``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int``; obrigatório.
        numero: Bling ``numero``; type ``int``; obrigatório.
        alertas: Bling ``alertas``; type ``list[str] | None``; opcional.
        erros_anexo: Bling ``errosAnexo``; type ``list[str] | None``; opcional."""

    id: int = Field(..., examples=[12345678])
    numero: int = Field(..., examples=[123])
    alertas: list[str] | None = None
    erros_anexo: list[str] | None = Field(default=None, alias="errosAnexo")


class PedidosComprasPostResponse201(BlingModel):
    """OpenAPI schema ``PedidosComprasPostResponse201``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data25 | None``; opcional."""

    data: Data25 | None = None


class PedidosComprasIdPedidoCompraPutResponse200(BlingModel):
    """OpenAPI schema ``PedidosComprasIdPedidoCompraPutResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data25 | None``; opcional."""

    data: Data25 | None = None


class PedidosComprasDadosBaseDTO(BlingModel):
    """OpenAPI schema ``PedidosComprasDadosBaseDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        numero: Bling ``numero``; type ``int | None``; opcional.
        data: Bling ``data``; type ``date | None``; opcional.
        data_prevista: Bling ``dataPrevista``; type ``date | None``; opcional.
        total_produtos: Bling ``totalProdutos``; type ``float | None``; opcional.
        total: Bling ``total``; type ``float | None``; opcional.
        fornecedor: Bling ``fornecedor``; type ``PedidosComprasFornecedorDTO``; obrigatório.
        situacao: Bling ``situacao``; type ``PedidosComprasSituacaoDTO | None``; opcional."""

    id: int | None = Field(default=None, examples=[12345678])
    numero: int | None = Field(default=None, examples=[12])
    data: date | None = Field(default=None, examples=["2020-08-24"])
    data_prevista: date | None = Field(default=None, alias="dataPrevista", examples=["2020-08-30"])
    total_produtos: float | None = Field(default=None, alias="totalProdutos", examples=[2090.66])
    total: float | None = Field(default=None, examples=[2090.66])
    fornecedor: PedidosComprasFornecedorDTO
    situacao: PedidosComprasSituacaoDTO | None = None


class PedidosComprasItemDTO(BlingModel):
    """OpenAPI schema ``PedidosComprasItemDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        descricao: Bling ``descricao``; type ``str``; obrigatório.
        codigo_fornecedor: Bling ``codigoFornecedor``; type ``str | None``; opcional.
        unidade: Bling ``unidade``; type ``str | None``; opcional.
        valor: Bling ``valor``; type ``float``; obrigatório.
        quantidade: Bling ``quantidade``; type ``float | None``; opcional.
        aliquota_ipi: Bling ``aliquotaIPI``; type ``float | None``; opcional.
        descricao_detalhada: Bling ``descricaoDetalhada``; type ``str | None``; opcional.
        nota_fiscal: Bling ``notaFiscal``; type ``PedidosComprasItemNotaFiscalDTO | None``; opcional.
        produto: Bling ``produto``; type ``PedidosComprasProdutoDTO | None``; opcional."""

    descricao: str = Field(..., examples=["Copo do Bling"])
    codigo_fornecedor: str | None = Field(
        default=None, alias="codigoFornecedor", examples=["46546546"]
    )
    unidade: str | None = Field(default=None, examples=["Un"])
    valor: float = Field(..., examples=[149.99])
    quantidade: float | None = Field(default=None, examples=[12])
    aliquota_ipi: float | None = Field(default=None, alias="aliquotaIPI", examples=[15.85])
    descricao_detalhada: str | None = Field(
        default=None, alias="descricaoDetalhada", examples=["Descrição do item do pedido."]
    )
    nota_fiscal: PedidosComprasItemNotaFiscalDTO | None = Field(default=None, alias="notaFiscal")
    produto: PedidosComprasProdutoDTO | None = None


class PedidosComprasGetResponse200(BlingModel):
    """OpenAPI schema ``PedidosComprasGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``list[PedidosComprasDadosBaseDTO] | None``; opcional."""

    data: list[PedidosComprasDadosBaseDTO] | None = None


class PedidosComprasDadosDTO(BlingModel):
    """OpenAPI schema ``PedidosComprasDadosDTO``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        ordem_compra: Bling ``ordemCompra``; type ``str | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        observacoes_internas: Bling ``observacoesInternas``; type ``str | None``; opcional.
        desconto: Bling ``desconto``; type ``PedidosComprasDescontoDTO | None``; opcional.
        categoria: Bling ``categoria``; type ``PedidosComprasCategoriaDTO | None``; opcional.
        tributacao: Bling ``tributacao``; type ``PedidosComprasTributacaoDTO | None``; opcional.
        transporte: Bling ``transporte``; type ``PedidosComprasTransporteDTO | None``; opcional.
        itens: Bling ``itens``; type ``list[PedidosComprasItemDTO]``; obrigatório.
        parcelas: Bling ``parcelas``; type ``list[PedidosComprasParcelaDTO] | None``; opcional."""

    ordem_compra: str | None = Field(default=None, alias="ordemCompra", examples=["351635"])
    observacoes: str | None = Field(default=None, examples=["Observação sobre o pedido."])
    observacoes_internas: str | None = Field(
        default=None, alias="observacoesInternas", examples=["Observação interna sobre o pedido."]
    )
    desconto: PedidosComprasDescontoDTO | None = None
    categoria: PedidosComprasCategoriaDTO | None = None
    tributacao: PedidosComprasTributacaoDTO | None = None
    transporte: PedidosComprasTransporteDTO | None = None
    itens: list[PedidosComprasItemDTO]
    parcelas: list[PedidosComprasParcelaDTO] | None = None


class PedidosComprasPostRequest(PedidosComprasDadosBaseDTO, PedidosComprasDadosDTO):
    """OpenAPI schema ``PedidosComprasPostRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: PedidosComprasDadosBaseDTO, PedidosComprasDadosDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        numero: Bling ``numero``; type ``int | None``; opcional.
        data: Bling ``data``; type ``date | None``; opcional.
        data_prevista: Bling ``dataPrevista``; type ``date | None``; opcional.
        total_produtos: Bling ``totalProdutos``; type ``float | None``; opcional.
        total: Bling ``total``; type ``float | None``; opcional.
        fornecedor: Bling ``fornecedor``; type ``PedidosComprasFornecedorDTO``; obrigatório.
        situacao: Bling ``situacao``; type ``PedidosComprasSituacaoDTO | None``; opcional.
        ordem_compra: Bling ``ordemCompra``; type ``str | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        observacoes_internas: Bling ``observacoesInternas``; type ``str | None``; opcional.
        desconto: Bling ``desconto``; type ``PedidosComprasDescontoDTO | None``; opcional.
        categoria: Bling ``categoria``; type ``PedidosComprasCategoriaDTO | None``; opcional.
        tributacao: Bling ``tributacao``; type ``PedidosComprasTributacaoDTO | None``; opcional.
        transporte: Bling ``transporte``; type ``PedidosComprasTransporteDTO | None``; opcional.
        itens: Bling ``itens``; type ``list[PedidosComprasItemDTO]``; obrigatório.
        parcelas: Bling ``parcelas``; type ``list[PedidosComprasParcelaDTO] | None``; opcional."""

    pass


class PedidosComprasIdPedidoCompraGetResponse200(BlingModel):
    """OpenAPI schema ``PedidosComprasIdPedidoCompraGetResponse200``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Fields:
        data: Bling ``data``; type ``Data26 | None``; opcional."""

    data: Data26 | None = None


class PedidosComprasIdPedidoCompraPutRequest(PedidosComprasDadosBaseDTO, PedidosComprasDadosDTO):
    """OpenAPI schema ``PedidosComprasIdPedidoCompraPutRequest``.

    Modelo Pydantic gerado a partir do contrato OpenAPI do Bling. Use este schema
    quando ele aparecer como request body ou response schema nos métodos do SDK.

    Herda campos de: PedidosComprasDadosBaseDTO, PedidosComprasDadosDTO.

    Fields:
        id: Bling ``id``; type ``int | None``; opcional.
        numero: Bling ``numero``; type ``int | None``; opcional.
        data: Bling ``data``; type ``date | None``; opcional.
        data_prevista: Bling ``dataPrevista``; type ``date | None``; opcional.
        total_produtos: Bling ``totalProdutos``; type ``float | None``; opcional.
        total: Bling ``total``; type ``float | None``; opcional.
        fornecedor: Bling ``fornecedor``; type ``PedidosComprasFornecedorDTO``; obrigatório.
        situacao: Bling ``situacao``; type ``PedidosComprasSituacaoDTO | None``; opcional.
        ordem_compra: Bling ``ordemCompra``; type ``str | None``; opcional.
        observacoes: Bling ``observacoes``; type ``str | None``; opcional.
        observacoes_internas: Bling ``observacoesInternas``; type ``str | None``; opcional.
        desconto: Bling ``desconto``; type ``PedidosComprasDescontoDTO | None``; opcional.
        categoria: Bling ``categoria``; type ``PedidosComprasCategoriaDTO | None``; opcional.
        tributacao: Bling ``tributacao``; type ``PedidosComprasTributacaoDTO | None``; opcional.
        transporte: Bling ``transporte``; type ``PedidosComprasTransporteDTO | None``; opcional.
        itens: Bling ``itens``; type ``list[PedidosComprasItemDTO]``; obrigatório.
        parcelas: Bling ``parcelas``; type ``list[PedidosComprasParcelaDTO] | None``; opcional."""

    pass


__all__ = [
    "PedidosCompraResponsePOSTPUT",
    "PedidosComprasCategoriaDTO",
    "PedidosComprasDadosBaseDTO",
    "PedidosComprasDadosDTO",
    "PedidosComprasDescontoDTO",
    "PedidosComprasFormaPagamentoDTO",
    "PedidosComprasFornecedorDTO",
    "PedidosComprasGetResponse200",
    "PedidosComprasIdPedidoCompraGetResponse200",
    "PedidosComprasIdPedidoCompraPutRequest",
    "PedidosComprasIdPedidoCompraPutResponse200",
    "PedidosComprasItemDTO",
    "PedidosComprasItemNotaFiscalDTO",
    "PedidosComprasParcelaDTO",
    "PedidosComprasPostRequest",
    "PedidosComprasPostResponse201",
    "PedidosComprasProdutoDTO",
    "PedidosComprasSituacaoDTO",
    "PedidosComprasTransporteDTO",
    "PedidosComprasTributacaoDTO",
]
