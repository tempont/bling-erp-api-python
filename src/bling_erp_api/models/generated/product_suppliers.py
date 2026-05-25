"""Semi-generated models for Produtos — Fornecedores."""

from __future__ import annotations

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class ProductSupplierProductRef(BlingModel):
    id: int


class ProductSupplierVendorRef(BlingModel):
    id: int


class ProductSupplierVendorUpdateRef(BlingModel):
    id: int | None = None


class ProductSupplier(BlingModel):
    """Linha ou detalhe entre produto e fornecedor."""

    record_id: int | None = Field(default=None, alias="id")
    description: str | None = Field(default=None, alias="descricao")
    codigo_fornecedor: str | None = Field(default=None, alias="codigo")
    preco_custo: float | None = Field(default=None, alias="precoCusto")
    preco_compra: float | None = Field(default=None, alias="precoCompra")
    padrao: bool | None = None
    produto: ProductSupplierProductRef | None = None
    fornecedor: ProductSupplierVendorRef | None = None
    garantia_months: int | None = Field(default=None, alias="garantia")


class ProductSupplierCreateRequest(ProductSupplier):
    """``POST`` / ``PUT`` payloads que incluem garantia obrigatória no create."""


class ProductSupplierUpdateRequest(BlingModel):
    """Payload ``PUT`` de alteração."""

    record_id: int | None = Field(default=None, alias="id")
    description: str | None = Field(default=None, alias="descricao")
    codigo_fornecedor: str | None = Field(default=None, alias="codigo")
    preco_custo: float | None = Field(default=None, alias="precoCusto")
    preco_compra: float | None = Field(default=None, alias="precoCompra")
    padrao: bool | None = None
    produto: ProductSupplierProductRef | None = None
    fornecedor: ProductSupplierVendorUpdateRef | None = None
    garantia_months: int | None = Field(default=None, alias="garantia")


class ProductSupplierListResponse(BlingModel):
    data: list[ProductSupplier] = Field(default_factory=list)
