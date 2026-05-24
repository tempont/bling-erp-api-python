"""Products resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource

if TYPE_CHECKING:
    from collections.abc import Iterator

    from bling_erp_api.types import JsonObject, QueryParams, QueryParamValue


class ProductsResource(BaseResource):
    """Operations for Bling products."""

    def list(
        self,
        *,
        page: int = 1,
        limit: int = 100,
        **filters: QueryParamValue,
    ) -> JsonObject:
        """List products."""
        return self._get("/produtos", params={"pagina": page, "limite": limit, **filters})

    def iterate(
        self,
        *,
        page: int = 1,
        limit: int = 100,
        **filters: QueryParamValue,
    ) -> Iterator[JsonObject]:
        """Iterate through products across pages."""
        params: QueryParams = filters
        return self._iterate("/produtos", page=page, limit=limit, params=params)

    def get(self, product_id: int) -> JsonObject:
        """Get a product by id."""
        return self._get(f"/produtos/{product_id}")
