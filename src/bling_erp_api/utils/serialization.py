"""Serialization helpers."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from pydantic import BaseModel

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject


def to_json_object(value: BaseModel | JsonObject) -> JsonObject:
    """Convert supported SDK payloads into JSON objects."""
    if isinstance(value, BaseModel):
        return cast("JsonObject", value.model_dump(mode="json", exclude_none=True))
    return value
