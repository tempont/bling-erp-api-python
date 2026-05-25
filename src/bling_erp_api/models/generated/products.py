"""Semi-generated product models."""

from __future__ import annotations

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class Product(BlingModel):
    """Produto retornado pela API do Bling."""

    id: int | None = None
    parent_product_id: int | None = Field(default=None, alias="idProdutoPai")
    name: str | None = Field(default=None, alias="nome")
    code: str | None = Field(default=None, alias="codigo")
    price: float | None = Field(default=None, alias="preco")
    cost_price: float | None = Field(default=None, alias="precoCusto")
    stock: dict[str, object] | None = Field(default=None, alias="estoque")
    product_type: str | None = Field(default=None, alias="tipo")
    status: str | None = Field(default=None, alias="situacao")
    format: str | None = Field(default=None, alias="formato")
    short_description: str | None = Field(default=None, alias="descricaoCurta")
    image_url: str | None = Field(default=None, alias="imagemURL")
    variations: list[Product] = Field(default_factory=list, alias="variacoes")


class ProductCreateRequest(Product):
    """Payload aceito por ``POST /produtos``."""


class ProductUpdateRequest(Product):
    """Payload aceito por ``PUT /produtos/{idProduto}``."""


class ProductPatchRequest(BlingModel):
    """Payload aceito por ``PATCH /produtos/{idProduto}``."""

    name: str | None = Field(default=None, alias="nome")
    code: str | None = Field(default=None, alias="codigo")
    price: float | None = Field(default=None, alias="preco")
    product_type: str | None = Field(default=None, alias="tipo")
    status: str | None = Field(default=None, alias="situacao")
    format: str | None = Field(default=None, alias="formato")
    short_description: str | None = Field(default=None, alias="descricaoCurta")


class ProductListResponse(BlingModel):
    """Response de ``GET /produtos``."""

    data: list[Product] = Field(default_factory=list)


class ProductResponse(BlingModel):
    """Response de ``GET /produtos/{idProduto}``."""

    data: Product


class ProductMutationResult(BlingModel):
    """Resultado de criação/alteração de produto."""

    id: int | None = None
    variations: dict[str, object] | None = None
    warnings: list[str] = Field(default_factory=list)


class ProductMutationResponse(BlingModel):
    """Response de criação/alteração de produto."""

    data: ProductMutationResult


class ProductAlertsResponse(BlingModel):
    """Response de operações em lote que retornam alertas."""

    alerts: list[dict[str, object]] = Field(default_factory=list, alias="alertas")
