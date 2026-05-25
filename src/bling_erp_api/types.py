"""Shared typing aliases for the SDK."""

from __future__ import annotations

from collections.abc import Mapping, Sequence

type JsonValue = None | bool | int | float | str | list["JsonValue"] | dict[str, "JsonValue"]
type JsonObject = dict[str, JsonValue]
type JsonPayload = JsonObject | Sequence[Mapping[str, JsonValue]]
type QueryParamPrimitive = str | int | float | bool
type QueryParamValue = QueryParamPrimitive | Sequence[QueryParamPrimitive]
type QueryParams = Mapping[str, QueryParamValue]
