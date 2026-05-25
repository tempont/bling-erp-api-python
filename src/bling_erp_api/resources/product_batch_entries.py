"""Produtos — Lotes lançamentos e saldos resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from collections.abc import Sequence

    from bling_erp_api.models.generated.product_batch_entries import (
        ProductBatchEntry,
        ProductBatchEntryObservationPatch,
    )
    from bling_erp_api.types import JsonObject


class ProductBatchEntriesResource(BaseResource):
    """Operações em ``/produtos/lotes/lancamentos`` e saldos de lote."""

    def obter(self, id_lancamento: int) -> JsonObject:
        """Obtém lançamento por ID."""
        return self._get(f"/produtos/lotes/lancamentos/{id_lancamento}")

    def alterar_atributo(
        self,
        id_lancamento: int,
        dados: ProductBatchEntryObservationPatch | JsonObject,
    ) -> JsonObject:
        """Atualiza observação do lançamento (``PATCH``)."""
        return self._patch(
            f"/produtos/lotes/lancamentos/{id_lancamento}",
            json=to_json_object(dados),
        )

    def listar(self, id_lote: int) -> JsonObject:
        """Lista lançamentos de um lote."""
        return self._get(f"/produtos/lotes/{id_lote}/lancamentos")

    def criar(self, id_lote: int, dados: ProductBatchEntry | JsonObject) -> JsonObject:
        """Cria lançamento em um lote."""
        return self._post(f"/produtos/lotes/{id_lote}/lancamentos", json=to_json_object(dados))

    def obter_saldos(
        self,
        id_produto: int,
        id_deposito: int,
        *,
        ids_lotes: Sequence[int],
    ) -> JsonObject:
        """Saldos de vários lotes por produto e depósito."""
        return self._get(
            f"/produtos/{id_produto}/lotes/depositos/{id_deposito}/saldo",
            params=compact_params({"idsLotes[]": list(ids_lotes)}),
        )

    def obter_saldos_soma(self, id_produto: int) -> JsonObject:
        """Soma dos saldos de lotes por produto (todos os depósitos)."""
        return self._get(f"/produtos/{id_produto}/lotes/saldo/soma")

    def obter_saldos_soma_deposito(self, id_produto: int, id_deposito: int) -> JsonObject:
        """Soma dos saldos dos lotes por produto e depósito."""
        return self._get(f"/produtos/{id_produto}/lotes/depositos/{id_deposito}/saldo/soma")

    def obter_saldos_saldo(self, id_produto: int, id_lote: int, id_deposito: int) -> JsonObject:
        """Saldo de um lote específico em um depósito."""
        return self._get(
            f"/produtos/{id_produto}/lotes/{id_lote}/depositos/{id_deposito}/saldo",
        )
