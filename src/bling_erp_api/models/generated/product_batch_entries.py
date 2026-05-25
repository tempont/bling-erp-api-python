"""Semi-generated models for Produtos — Lotes lançamentos e saldos."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from bling_erp_api.models.base import BlingModel
from bling_erp_api.models.generated.product_batches import (
    ProductBatchProductRef,
    ProductBatchWarehouseRef,
)


class ProductBatchEntry(BlingModel):
    """LoteLancamentoDTO."""

    entry_id: int | None = Field(default=None, alias="id")
    id_lote: int = Field(alias="idLote")
    quantity: int | None = Field(default=None, alias="quantidade")
    tipo_lancamento: Literal[1, 2, 3] | None = Field(default=None, alias="tipoLancamento")
    data: str | None = None
    id_origem: int | None = Field(default=None, alias="idOrigem")
    observacao: str


class ProductBatchEntryObservationPatch(BlingModel):
    observacao: str


class BalancePerLotWarehouse(BlingModel):
    id_lote: int | None = Field(default=None, alias="idLote")
    produto: ProductBatchProductRef | None = None
    deposito: ProductBatchWarehouseRef | None = None
    saldo_atual: float | None = Field(default=None, alias="saldoAtual")


class BalanceSumPerWarehouse(BlingModel):
    produto: ProductBatchProductRef | None = None
    deposito: ProductBatchWarehouseRef | None = None
    saldo_total: float | None = Field(default=None, alias="saldoTotal")


class BalanceSumAllWarehouses(BlingModel):
    produto: ProductBatchProductRef | None = None
    saldo_total: float | None = Field(default=None, alias="saldoTotal")
