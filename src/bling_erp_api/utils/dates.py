"""Date formatting helpers."""

from __future__ import annotations

from datetime import date, datetime


def format_date(value: date | datetime) -> str:
    """Format a date-like value for Bling query parameters."""
    return value.date().isoformat() if isinstance(value, datetime) else value.isoformat()
