"""Semi-generated models for Produtos — Lojas."""

from __future__ import annotations

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class ProductStoreProductRef(BlingModel):
    id: int


class ProductStoreShopRef(BlingModel):
    id: int


class ProductStoreVendorRef(BlingModel):
    id: int


class ProductStoreBrandRef(BlingModel):
    id: int


class ProductStoreCategoryRef(BlingModel):
    id: int


class ProductStoreLink(BlingModel):
    """Vinculo persistido entre produto e loja."""

    record_id: int | None = Field(default=None, alias="id")
    codigo_loja: str = Field(alias="codigo")
    preco: float | None = None
    promotional_price: float | None = Field(default=None, alias="precoPromocional")
    produto: ProductStoreProductRef
    loja: ProductStoreShopRef
    fornecedor_loja: ProductStoreVendorRef | None = Field(default=None, alias="fornecedorLoja")
    marca_loja: ProductStoreBrandRef | None = Field(default=None, alias="marcaLoja")
    categorias_produtos: list[ProductStoreCategoryRef] | None = Field(
        default=None, alias="categoriasProdutos"
    )


class ProductStoreLinkCreate(ProductStoreLink):
    """Payload de criação (base + dados)."""


class ProductStoreMutationResponse(BlingModel):
    """Resposta 201 típica com id do vínculo."""

    record_id: int | None = Field(default=None, alias="id")


class ProductStoreMutationEnvelope(BlingModel):
    """Envelope com ``data`` contendo resultado de POST/PUT."""

    data: ProductStoreMutationResponse | dict[str, object]
