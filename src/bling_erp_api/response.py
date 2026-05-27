"""Response parsing helpers."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    import httpx

    from bling_erp_api.types import JsonObject, JsonValue


def response_json(response: httpx.Response) -> JsonValue:
    """Decode an HTTP response as JSON."""
    return cast("JsonValue", response.json())


def response_json_object(response: httpx.Response) -> JsonObject:
    """Decode an HTTP response and require a JSON object body."""
    if not response.content:
        return {}

    payload = response_json(response)
    if isinstance(payload, dict):
        return payload

    msg = "Expected Bling API response body to be a JSON object"
    raise ValueError(msg)
