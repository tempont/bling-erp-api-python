"""Base resource helpers."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.pagination import iter_pages

if TYPE_CHECKING:
    from collections.abc import Iterator

    from bling_erp_api.transport.base import Transport
    from bling_erp_api.types import JsonObject, QueryParams


class BaseResource:
    """Common request helpers for resource namespaces."""

    def __init__(self, transport: Transport) -> None:
        """Create a resource bound to a transport."""
        self._transport = transport

    def _get(self, path: str, *, params: QueryParams | None = None) -> JsonObject:
        """Send a GET request."""
        return self._transport.request("GET", path, params=params)

    def _post(self, path: str, *, json: JsonObject | None = None) -> JsonObject:
        """Send a POST request."""
        return self._transport.request("POST", path, json=json)

    def _put(self, path: str, *, json: JsonObject | None = None) -> JsonObject:
        """Send a PUT request."""
        return self._transport.request("PUT", path, json=json)

    def _patch(self, path: str, *, json: JsonObject | None = None) -> JsonObject:
        """Send a PATCH request."""
        return self._transport.request("PATCH", path, json=json)

    def _delete(self, path: str, *, params: QueryParams | None = None) -> JsonObject:
        """Send a DELETE request."""
        return self._transport.request("DELETE", path, params=params)

    def _iterate(
        self,
        path: str,
        *,
        page: int = 1,
        limit: int = 100,
        params: QueryParams | None = None,
    ) -> Iterator[JsonObject]:
        """Iterate through paginated records for an endpoint."""
        return iter_pages(
            lambda next_page: self._get(
                path,
                params={"pagina": next_page, "limite": limit, **dict(params or {})},
            ),
            start_page=page,
        )
