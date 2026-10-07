"""Custom field types for Bling API models."""

from __future__ import annotations

from datetime import date, datetime
from typing import Annotated
from zoneinfo import ZoneInfo

from pydantic import AfterValidator
from pydantic.functional_serializers import PlainSerializer
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


def _serialize_bling_date(value: date | None) -> str | None:
    """Serialize a ``BlingDate`` as an ISO date string, preserving ``None``."""
    return value.isoformat() if value is not None else None


BlingDate = Annotated[
    date,
    PlainValidator(_parse_bling_date),
    PlainSerializer(_serialize_bling_date, return_type=str | None, when_used="json"),
]


def _localize_bling_datetime(value: datetime) -> datetime:
    """Interpret offset-free Bling timestamps in America/Sao_Paulo.

    Preserve explicit offsets and use the IANA timezone rules for naive values,
    including historical daylight saving time. Invalid timestamps still fail
    Pydantic's normal datetime validation before this validator is called.
    """
    if value.tzinfo is None or value.utcoffset() is None:
        return value.replace(tzinfo=ZoneInfo("America/Sao_Paulo"))
    return value


BlingDatetime = Annotated[datetime, AfterValidator(_localize_bling_datetime)]
