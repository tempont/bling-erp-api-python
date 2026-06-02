"""Custom field types for Bling API models."""

from __future__ import annotations

from datetime import date
from typing import Annotated

from pydantic.functional_validators import PlainValidator


def _parse_bling_date(value: object) -> date | None:
    """Parse a date value from the Bling API, handling MySQL zero-date sentinels.

    Accepts:
    - Valid ISO date strings ("2020-01-01") → parsed as ``date``
    - ``None`` → ``None``
    - Already-parsed ``date`` objects → passthrough
    - ``"0000-00-00"`` and other zero-date sentinels → ``None``
    - Empty string or whitespace-only → ``None``

    Raises ``ValueError`` for other invalid values.
    """
    if value is None:
        return None
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        stripped = value.strip()
        if not stripped or stripped in {"0000-00-00", "0000-00-00 00:00:00", "0001-01-01"}:
            return None
        return date.fromisoformat(stripped)
    msg = f"Invalid date value: {value!r}"
    raise ValueError(msg)


BlingDate = Annotated[date, PlainValidator(_parse_bling_date)]
