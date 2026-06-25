"""Pagination helpers for list endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Iterator

    from bling_erp_api.types import JsonObject


def extract_records(payload: JsonObject) -> list[JsonObject]:
    """Extract record objects from a Bling list response."""
    data = payload.get("data")
    if not isinstance(data, list):
        return []

    return [item for item in data if isinstance(item, dict)]


def iter_pages(
    fetch_page: Callable[[int], JsonObject], *, start_page: int = 1
) -> Iterator[JsonObject]:
    """Iterate records until a page returns no records."""
    page = start_page
    while True:
        payload = fetch_page(page)
        records = extract_records(payload)
        if not records:
            return

        yield from records
        page += 1


def next_page_payload(payload: JsonObject, *, next_page: int) -> JsonObject:
    """Create normalized pagination metadata for future response wrappers.

    Note:
        The full response is retained in memory under the ``"raw"`` key.
        For large paginated datasets this could lead to significant memory
        growth — use with care.
    """
    return {"page": next_page, "raw": payload}
