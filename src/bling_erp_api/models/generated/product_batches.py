"""Semi-generated models for Produtos — Lotes."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from bling_erp_api.models.base import BlingModel


class ProductBatchProductRef(BlingModel):
    id: int


class ProductBatchWarehouseRef(BlingModel):
    id: int


class ProductBatch(BlingModel):
    """Um lote (LotesDTO)."""

    id_lote: int = Field(alias="idLote")
    codigo_lote: str | None = Field(default=None, alias="codigoLote")
    data_fabricacao: str | None = Field(default=None, alias="dataFabricacao")
    data_validade: str | None = Field(default=None, alias="dataValidade")
    dias_permitido_venda: int | None = Field(default=None, alias="diasPermitidoVenda")
    codigo_agregacao: str | None = Field(default=None, alias="codigoAgregacao")
    produto: ProductBatchProductRef
    deposito: ProductBatchWarehouseRef
    status: Literal[1, 2] | None = None


class ProductBatchUpdateRequest(BlingModel):
    """Corpo partial ``PUT /produtos/lotes/{idLote}`` (LotePutRequestDTO)."""

    codigo_lote: str | None = Field(default=None, alias="codigoLote")
    data_fabricacao: str | None = Field(default=None, alias="dataFabricacao")
    data_validade: str | None = Field(default=None, alias="dataValidade")
    dias_permitido_venda: int | None = Field(default=None, alias="diasPermitidoVenda")
    codigo_agregacao: str | None = Field(default=None, alias="codigoAgregacao")


class ProductBatchStatusRequest(BlingModel):
    """``PATCH`` status do lote (LoteStatusDTO)."""

    status: Literal[1, 2]


class ProductBatchSaveResponseLot(BlingModel):
    id: int | None = None
    codigo_lote: str | None = Field(default=None, alias="codigoLote")
    id_produto: int | None = Field(default=None, alias="idProduto")


class ProductBatchSaveResponse(BlingModel):
    saved: list[ProductBatchSaveResponseLot] = Field(default_factory=list)
    errors: list[dict[str, object]] = Field(default_factory=list)


class ProductBatchSaveResponseEnvelope(BlingModel):
    data: ProductBatchSaveResponse


class ProductBatchControlsLotInfo(BlingModel):
    """ProdutoControlaLotesDTO."""

    id_produto: int = Field(alias="idProduto")
    controla_lote: bool | None = Field(default=None, alias="controlaLote")
