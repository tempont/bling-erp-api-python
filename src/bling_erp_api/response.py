"""Response parsing helpers."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

import httpx

from bling_erp_api.exceptions import BlingTransportError

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject, JsonValue


def response_json(response: httpx.Response) -> JsonValue:
    """Decode an HTTP response as JSON."""
    try:
        return cast("JsonValue", response.json())
    except (ValueError, AttributeError, httpx.HTTPError) as exc:
        msg = f"Failed to parse JSON response: {exc}"
        raise BlingTransportError(msg) from exc


def response_json_object(response: httpx.Response) -> JsonObject:
    """Decode an HTTP response and require a JSON object body."""
    if not response.content:
        return {}

    payload = response_json(response)
    if isinstance(payload, dict):
        return payload

    msg = "Expected Bling API response body to be a JSON object"
    raise ValueError(msg)
