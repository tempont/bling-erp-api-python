"""Transport protocols shared by resources."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject, JsonPayload, QueryParams


class Transport(Protocol):
    """Minimal transport contract consumed by resources."""

    def request(
        self,
        method: str,
        path: str,
        *,
        params: QueryParams | None = None,
        json: JsonPayload | None = None,
        headers: dict[str, str] | None = None,
    ) -> JsonObject:
        """Send an HTTP request and return the decoded JSON object."""
        ...
