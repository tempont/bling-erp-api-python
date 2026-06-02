"""Tests for the BlingDate custom field type."""

from __future__ import annotations

from datetime import date

import pytest
from pydantic import BaseModel, ValidationError

from bling_erp_api.models.fields import BlingDate  # noqa: TC001


class ModelWithOptionalDate(BaseModel):
    """Pydantic model with an optional BlingDate field for testing."""

    value: BlingDate | None = None


class TestParseBlingDate:
    """Unit tests for the _parse_bling_date validator."""

    def test_none_returns_none(self) -> None:
        """None input should pass through as None."""
        model = ModelWithOptionalDate(value=None)
        assert model.value is None

    def test_date_object_passthrough(self) -> None:
        """A date object should pass through unchanged."""
        d = date(2020, 1, 1)
        model = ModelWithOptionalDate(value=d)
        assert model.value == d

    def test_valid_iso_string(self) -> None:
        """A valid ISO date string should be parsed to a date object."""
        model = ModelWithOptionalDate(value="2020-01-01")  # type: ignore[reportArgumentType]
        assert model.value == date(2020, 1, 1)

    def test_zero_date_sentinel_0000_00_00(self) -> None:
        """Bling zero-date sentinel ``0000-00-00`` should be parsed as None."""
        model = ModelWithOptionalDate(value="0000-00-00")  # type: ignore[reportArgumentType]
        assert model.value is None

    def test_zero_date_sentinel_datetime(self) -> None:
        """Zero-date with datetime component should be parsed as None."""
        model = ModelWithOptionalDate(value="0000-00-00 00:00:00")  # type: ignore[reportArgumentType]
        assert model.value is None

    def test_sentinel_0001_01_01(self) -> None:
        """The minimum-date sentinel ``0001-01-01`` should be parsed as None."""
        model = ModelWithOptionalDate(value="0001-01-01")  # type: ignore[reportArgumentType]
        assert model.value is None

    def test_empty_string(self) -> None:
        """An empty string should be parsed as None."""
        model = ModelWithOptionalDate(value="")  # type: ignore[reportArgumentType]
        assert model.value is None

    def test_whitespace_string(self) -> None:
        """A whitespace-only string should be parsed as None."""
        model = ModelWithOptionalDate(value="   ")  # type: ignore[reportArgumentType]
        assert model.value is None

    def test_invalid_string_raises(self) -> None:
        """An invalid date string should raise a ValidationError."""
        with pytest.raises(ValidationError):
            ModelWithOptionalDate(value="not-a-date")  # type: ignore[reportArgumentType]

    def test_integer_raises(self) -> None:
        """An integer value should raise a ValidationError."""
        with pytest.raises(ValidationError):
            ModelWithOptionalDate(value=42)  # type: ignore[arg-type]

    def test_bool_raises(self) -> None:
        """A boolean value should raise a ValidationError."""
        with pytest.raises(ValidationError):
            ModelWithOptionalDate(value=True)  # type: ignore[arg-type]

    def test_list_raises(self) -> None:
        """A list value should raise a ValidationError."""
        with pytest.raises(ValidationError):
            ModelWithOptionalDate(value=["2020-01-01"])  # type: ignore[arg-type]

    def test_default_none_when_missing(self) -> None:
        """A model without the field should default to None."""
        model = ModelWithOptionalDate()
        assert model.value is None


class TestBlingDateSerialization:
    """Serialization behavior of BlingDate fields."""

    def test_valid_date_serializes_as_iso_string(self) -> None:
        """A valid date should serialize to an ISO string in JSON mode."""
        model = ModelWithOptionalDate(value=date(2020, 1, 1))
        dumped = model.model_dump(mode="json")
        assert dumped["value"] == "2020-01-01"

    def test_none_excluded_when_exclude_none(self) -> None:
        """None should be excluded from JSON output with exclude_none=True."""
        model = ModelWithOptionalDate(value=None)
        dumped = model.model_dump(mode="json", exclude_none=True)
        assert "value" not in dumped

    def test_none_included_when_not_excluded(self) -> None:
        """None should be included as null in JSON output by default."""
        model = ModelWithOptionalDate(value=None)
        dumped = model.model_dump(mode="json")
        assert dumped["value"] is None
