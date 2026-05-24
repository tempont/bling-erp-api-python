"""Contacts resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource

if TYPE_CHECKING:
    from collections.abc import Iterator

    from bling_erp_api.types import JsonObject, QueryParams, QueryParamValue


class ContactsResource(BaseResource):
    """Operations for Bling contacts."""

    def list(
        self,
        *,
        page: int = 1,
        limit: int = 100,
        **filters: QueryParamValue,
    ) -> JsonObject:
        """List contacts."""
        return self._get(
            "/contatos",
            params={"pagina": page, "limite": limit, **filters},
        )

    def iterate(
        self,
        *,
        page: int = 1,
        limit: int = 100,
        **filters: QueryParamValue,
    ) -> Iterator[JsonObject]:
        """Iterate through contacts across pages."""
        params: QueryParams = filters
        return self._iterate("/contatos", page=page, limit=limit, params=params)

    def get(self, contact_id: int) -> JsonObject:
        """Get a contact by id."""
        return self._get(f"/contatos/{contact_id}")

    def create(self, data: JsonObject) -> JsonObject:
        """Create a contact."""
        return self._post("/contatos", json=data)

    def update(self, contact_id: int, data: JsonObject) -> JsonObject:
        """Update a contact."""
        return self._put(f"/contatos/{contact_id}", json=data)

    def delete(self, contact_id: int) -> JsonObject:
        """Delete a contact."""
        return self._delete(f"/contatos/{contact_id}")
