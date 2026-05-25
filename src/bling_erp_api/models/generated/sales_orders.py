"""Semi-generated sales order models."""

from __future__ import annotations

import datetime as dt  # noqa: TC003

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class SalesOrderContact(BlingModel):
    """Contact embedded in a sales order."""

    id: int
    name: str | None = Field(default=None, alias="nome")
    person_type: str | None = Field(default=None, alias="tipoPessoa")
    document_number: str | None = Field(default=None, alias="numeroDocumento")


class SalesOrderStatus(BlingModel):
    """Status embedded in a sales order."""

    id: int
    value: int | None = Field(default=None, alias="valor")


class SalesOrderStore(BlingModel):
    """Store embedded in a sales order."""

    id: int
    business_unit: dict[str, object] | None = Field(default=None, alias="unidadeNegocio")


class SalesOrderItemProduct(BlingModel):
    """Product reference embedded in a sales order item."""

    id: int


class SalesOrderItem(BlingModel):
    """Sales order item."""

    id: int | None = None
    code: str | None = Field(default=None, alias="codigo")
    unit: str | None = Field(default=None, alias="unidade")
    quantity: float | None = Field(default=None, alias="quantidade")
    discount: float | None = Field(default=None, alias="desconto")
    value: float | None = Field(default=None, alias="valor")
    ipi_rate: float | None = Field(default=None, alias="aliquotaIPI")
    description: str | None = Field(default=None, alias="descricao")
    detailed_description: str | None = Field(default=None, alias="descricaoDetalhada")
    product: SalesOrderItemProduct | None = Field(default=None, alias="produto")
    commission: dict[str, object] | None = Field(default=None, alias="comissao")
    operation_nature: dict[str, object] | None = Field(default=None, alias="naturezaOperacao")


class SalesOrderPaymentMethod(BlingModel):
    """Payment method reference embedded in an installment."""

    id: int


class SalesOrderInstallment(BlingModel):
    """Sales order installment."""

    id: int | None = None
    due_date: dt.date | None = Field(default=None, alias="dataVencimento")
    value: float | None = Field(default=None, alias="valor")
    notes: str | None = Field(default=None, alias="observacoes")
    authorization_code: str | None = Field(default=None, alias="caut")
    payment_method: SalesOrderPaymentMethod | None = Field(default=None, alias="formaPagamento")


class SalesOrder(BlingModel):
    """Sales order returned by Bling."""

    id: int | None = None
    number: int | None = Field(default=None, alias="numero")
    store_number: str | None = Field(default=None, alias="numeroLoja")
    date: dt.date | None = Field(default=None, alias="data")
    output_date: dt.date | None = Field(default=None, alias="dataSaida")
    expected_date: dt.date | None = Field(default=None, alias="dataPrevista")
    products_total: float | None = Field(default=None, alias="totalProdutos")
    total: float | None = None
    contact: SalesOrderContact | None = Field(default=None, alias="contato")
    status: SalesOrderStatus | None = Field(default=None, alias="situacao")
    store: SalesOrderStore | None = Field(default=None, alias="loja")
    purchase_order_number: str | None = Field(default=None, alias="numeroPedidoCompra")
    other_expenses: float | None = Field(default=None, alias="outrasDespesas")
    notes: str | None = Field(default=None, alias="observacoes")
    internal_notes: str | None = Field(default=None, alias="observacoesInternas")
    discount: dict[str, object] | None = Field(default=None, alias="desconto")
    category: dict[str, object] | None = Field(default=None, alias="categoria")
    invoice: dict[str, object] | None = Field(default=None, alias="notaFiscal")
    taxation: dict[str, object] | None = Field(default=None, alias="tributacao")
    items: list[SalesOrderItem] = Field(default_factory=list, alias="itens")
    installments: list[SalesOrderInstallment] = Field(default_factory=list, alias="parcelas")
    shipping: dict[str, object] | None = Field(default=None, alias="transporte")
    seller: dict[str, object] | None = Field(default=None, alias="vendedor")
    intermediary: dict[str, object] | None = Field(default=None, alias="intermediador")
    fees: dict[str, object] | None = Field(default=None, alias="taxas")


class SalesOrderCreateRequest(SalesOrder):
    """Payload accepted by ``POST /pedidos/vendas``."""


class SalesOrderUpdateRequest(SalesOrder):
    """Payload accepted by ``PUT /pedidos/vendas/{idPedidoVenda}``."""


class SalesOrderListResponse(BlingModel):
    """Response returned by ``GET /pedidos/vendas``."""

    data: list[SalesOrder] = Field(default_factory=list)


class SalesOrderResponse(BlingModel):
    """Response returned by ``GET /pedidos/vendas/{idPedidoVenda}``."""

    data: SalesOrder


class SalesOrderMutationResult(BlingModel):
    """Result returned by create and update operations."""

    id: int | None = None
    warnings: list[dict[str, object]] = Field(default_factory=list, alias="alertas")
    tracking: dict[str, object] | None = Field(default=None, alias="rastreamento")


class SalesOrderMutationResponse(BlingModel):
    """Response returned by create and update operations."""

    data: SalesOrderMutationResult


class SalesOrderDeleteManyResult(BlingModel):
    """Result returned when deleting multiple sales orders."""

    warnings: list[str] = Field(default_factory=list, alias="alertas")


class SalesOrderDeleteManyResponse(BlingModel):
    """Response returned by ``DELETE /pedidos/vendas`` when Bling sends a body."""

    data: SalesOrderDeleteManyResult | None = None


class SalesOrderInvoiceResponse(BlingModel):
    """Response returned when generating an invoice from a sales order."""

    invoice_id: int = Field(alias="idNotaFiscal")
