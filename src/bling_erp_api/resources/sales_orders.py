"""Sales orders resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource

if TYPE_CHECKING:
    from collections.abc import Iterator

    from bling_erp_api.types import JsonObject, QueryParams, QueryParamValue


class SalesOrdersResource(BaseResource):
    """Operations for Bling sales orders."""

    def list(
        self,
        *,
        page: int = 1,
        limit: int = 100,
        **filters: QueryParamValue,
    ) -> JsonObject:
        """List sales orders."""
        return self._get("/pedidos/vendas", params={"pagina": page, "limite": limit, **filters})

    def iterate(
        self,
        *,
        page: int = 1,
        limit: int = 100,
        **filters: QueryParamValue,
    ) -> Iterator[JsonObject]:
        """Iterate through sales orders across pages."""
        params: QueryParams = filters
        return self._iterate("/pedidos/vendas", page=page, limit=limit, params=params)

    def get(self, order_id: int) -> JsonObject:
        """Get a sales order by id."""
        return self._get(f"/pedidos/vendas/{order_id}")
