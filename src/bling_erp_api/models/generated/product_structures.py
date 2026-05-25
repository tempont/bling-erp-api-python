"""Semi-generated models for Produtos — Estruturas."""

from __future__ import annotations

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class ProductStructureComponentProduct(BlingModel):
    """Referência ao produto componente."""

    id: int = Field(alias="id")


class ProductStructureComponent(BlingModel):
    """Componente em uma estrutura de produto."""

    produto: ProductStructureComponentProduct
    quantity: float = Field(alias="quantidade")


class ProductStructure(BlingModel):
    """Estrutura (composição) de produto conforme ProdutosEstruturaDTO."""

    stock_kind: str = Field(alias="tipoEstoque")
    launch_kind: str = Field(alias="lancamentoEstoque")
    componentes: list[ProductStructureComponent] = Field(default_factory=list)


class ProductStructureUpdateRequest(ProductStructure):
    """Payload ``PUT`` em ``/produtos/estruturas/{idProdutoEstrutura}``."""


class ProductStructureResponse(BlingModel):
    """Resposta ``GET`` de estrutura de produto."""

    data: ProductStructure
