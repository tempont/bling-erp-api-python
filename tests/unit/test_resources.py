"""Tests for resource request mapping."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.contacts import ContactsResource

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject, QueryParams


class RecordingTransport:
    """Transport test double that records the latest request."""

    def __init__(self) -> None:
        """Create an empty recorder."""
        self.calls: list[tuple[str, str, QueryParams | None, JsonObject | None]] = []

    def request(
        self,
        method: str,
        path: str,
        *,
        params: QueryParams | None = None,
        json: JsonObject | None = None,
    ) -> JsonObject:
        """Record a request and return a simple response."""
        self.calls.append((method, path, params, json))
        return {"data": []}


def test_contacts_list_maps_to_bling_endpoint() -> None:
    """Contacts listing should use the Portuguese Bling API path."""
    transport = RecordingTransport()
    resource = ContactsResource(transport)

    response = resource.list(page=2, limit=50, name="Ana")

    assert response == {"data": []}
    assert transport.calls == [
        ("GET", "/contatos", {"pagina": 2, "limite": 50, "name": "Ana"}, None)
    ]
