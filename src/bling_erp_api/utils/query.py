"""Query parameter helpers."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Mapping

    from bling_erp_api.types import QueryParams, QueryParamValue


def compact_params(params: Mapping[str, QueryParamValue | None]) -> QueryParams:
    """Drop query parameters with ``None`` values."""
    return {key: value for key, value in params.items() if value is not None}
