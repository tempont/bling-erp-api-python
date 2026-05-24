"""Shared typing aliases for the SDK."""

from __future__ import annotations

from collections.abc import Mapping

type JsonValue = None | bool | int | float | str | list["JsonValue"] | dict[str, "JsonValue"]
type JsonObject = dict[str, JsonValue]
type QueryParamValue = str | int | float | bool
type QueryParams = Mapping[str, QueryParamValue]
