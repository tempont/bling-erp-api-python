"""Invoices resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource

if TYPE_CHECKING:
    from collections.abc import Iterator

    from bling_erp_api.types import JsonObject, QueryParams, QueryParamValue


class InvoicesResource(BaseResource):
    """Operations for Bling invoices."""

    def list(
        self,
        *,
        page: int = 1,
        limit: int = 100,
        **filters: QueryParamValue,
    ) -> JsonObject:
        """List invoices."""
        return self._get("/notas/fiscais", params={"pagina": page, "limite": limit, **filters})

    def iterate(
        self,
        *,
        page: int = 1,
        limit: int = 100,
        **filters: QueryParamValue,
    ) -> Iterator[JsonObject]:
        """Iterate through invoices across pages."""
        params: QueryParams = filters
        return self._iterate("/notas/fiscais", page=page, limit=limit, params=params)

    def get(self, invoice_id: int) -> JsonObject:
        """Get an invoice by id."""
        return self._get(f"/notas/fiscais/{invoice_id}")
