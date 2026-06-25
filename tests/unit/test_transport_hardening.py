"""Tests for transport/serialization/exception hardening (Slice 6)."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

import httpx
import pytest
from pydantic import BaseModel

from bling_erp_api.exceptions import (
    BlingAPIError,
    BlingConflictError,
    BlingMethodNotAllowedError,
    BlingRateLimitError,
    BlingServerError,
    BlingTransportError,
    BlingUnsupportedMediaTypeError,
    BlingValidationError,
    raise_for_error_response,
)
from bling_erp_api.response import response_json, response_json_object
from bling_erp_api.transport.sync import (
    DEFAULT_RETRY_AFTER_RATE_LIMIT_SECONDS,
    SyncTransport,
    _sleep_retry_after,  # pyright: ignore[reportPrivateUsage]
)
from bling_erp_api.utils.serialization import to_json_object

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject

# ---------------------------------------------------------------------------
# H9 — Retry-After HTTP-date parsing + bounds
# ---------------------------------------------------------------------------


class TestRetryAfterParsing:
    """Retry-After header parsing for both seconds and HTTP-date formats."""

    def test_retry_after_seconds_format(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Retry-After with integer seconds should use that delay."""
        delays: list[float] = []

        def capture_sleep(delay: float) -> None:
            delays.append(delay)

        monkeypatch.setattr("bling_erp_api.transport.sync.time.sleep", capture_sleep)

        request = httpx.Request("GET", "https://api.bling.test/Api/v3/test")
        response = httpx.Response(429, request=request, headers={"Retry-After": "5"})

        _sleep_retry_after(response)
        assert len(delays) == 1
        assert abs(delays[0] - 5.0) < 0.01

    def test_retry_after_http_date_format(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Retry-After with HTTP-date should parse and compute (past → 0)."""
        delays: list[float] = []

        def capture_sleep(delay: float) -> None:
            delays.append(delay)

        monkeypatch.setattr("bling_erp_api.transport.sync.time.sleep", capture_sleep)

        request = httpx.Request("GET", "https://api.bling.test/Api/v3/test")
        # HTTP-date in the past → delay capped to 0; no sleep call
        response = httpx.Response(
            429, request=request, headers={"Retry-After": "Mon, 01 Jan 2020 00:00:00 GMT"}
        )

        _sleep_retry_after(response)
        # delay is 0.0 → sleep is not called
        assert len(delays) == 0

    def test_retry_after_infinite_uses_default(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Retry-After: inf should not hang; fall back to default."""
        delays: list[float] = []

        def capture_sleep(delay: float) -> None:
            delays.append(delay)

        monkeypatch.setattr("bling_erp_api.transport.sync.time.sleep", capture_sleep)

        request = httpx.Request("GET", "https://api.bling.test/Api/v3/test")
        response = httpx.Response(429, request=request, headers={"Retry-After": "inf"})

        _sleep_retry_after(response)
        assert len(delays) == 1
        assert abs(delays[0] - DEFAULT_RETRY_AFTER_RATE_LIMIT_SECONDS) < 0.01

    def test_retry_after_nan_uses_default(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Retry-After: nan should not hang; fall back to default."""
        delays: list[float] = []

        def capture_sleep(delay: float) -> None:
            delays.append(delay)

        monkeypatch.setattr("bling_erp_api.transport.sync.time.sleep", capture_sleep)

        request = httpx.Request("GET", "https://api.bling.test/Api/v3/test")
        response = httpx.Response(429, request=request, headers={"Retry-After": "nan"})

        _sleep_retry_after(response)
        assert len(delays) == 1
        assert abs(delays[0] - DEFAULT_RETRY_AFTER_RATE_LIMIT_SECONDS) < 0.01

    def test_retry_after_bounds_capped_at_300(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Retry-After delay should be capped at 300 seconds."""
        delays: list[float] = []

        def capture_sleep(delay: float) -> None:
            delays.append(delay)

        monkeypatch.setattr("bling_erp_api.transport.sync.time.sleep", capture_sleep)

        request = httpx.Request("GET", "https://api.bling.test/Api/v3/test")
        response = httpx.Response(429, request=request, headers={"Retry-After": "500"})

        _sleep_retry_after(response)
        assert len(delays) == 1
        assert delays[0] == 300.0

    def test_retry_after_future_http_date_positive_delay(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """HTTP-date in the future should produce a positive delay."""
        delays: list[float] = []

        def capture_sleep(delay: float) -> None:
            delays.append(delay)

        monkeypatch.setattr("bling_erp_api.transport.sync.time.sleep", capture_sleep)

        request = httpx.Request("GET", "https://api.bling.test/Api/v3/test")
        # Use a date far in the future
        response = httpx.Response(
            429,
            request=request,
            headers={"Retry-After": "Mon, 01 Jan 2099 00:00:00 GMT"},
        )

        _sleep_retry_after(response)
        assert len(delays) == 1
        assert delays[0] > 0

    def test_retry_after_no_header_uses_default(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """No Retry-After header should use the default delay."""
        delays: list[float] = []

        def capture_sleep(delay: float) -> None:
            delays.append(delay)

        monkeypatch.setattr("bling_erp_api.transport.sync.time.sleep", capture_sleep)

        request = httpx.Request("GET", "https://api.bling.test/Api/v3/test")
        response = httpx.Response(429, request=request)

        _sleep_retry_after(response)
        assert len(delays) == 1
        assert abs(delays[0] - DEFAULT_RETRY_AFTER_RATE_LIMIT_SECONDS) < 0.01


# ---------------------------------------------------------------------------
# H10 — to_json_object no longer drops explicitly-set default values
# ---------------------------------------------------------------------------


class ModelWithDefaults(BaseModel):
    """Model with a field that has a default value."""

    name: str
    active: bool = True
    quantity: int = 0


class TestToJsonObject:
    """to_json_object should keep explicitly-set defaults."""

    def test_explicit_default_not_dropped(self) -> None:
        """When a field is set to its default explicitly, it must be present."""
        model = ModelWithDefaults(name="test", active=True, quantity=0)
        result = to_json_object(model)
        assert result == {"name": "test", "active": True, "quantity": 0}

    def test_none_value_still_dropped(self) -> None:
        """None values should still be excluded."""
        model = ModelWithDefaults(name="test", active=True, quantity=0)
        # Manually set name to None after construction
        model.name = None  # type: ignore[assignment]
        result = to_json_object(model)
        assert "name" not in result
        assert result == {"active": True, "quantity": 0}

    def test_non_default_values_preserved(self) -> None:
        """Non-default values must be preserved."""
        model = ModelWithDefaults(name="custom", active=False, quantity=10)
        result = to_json_object(model)
        assert result == {"name": "custom", "active": False, "quantity": 10}

    def test_raw_dict_passthrough(self) -> None:
        """Raw dict values should pass through unchanged."""
        payload: JsonObject = cast("JsonObject", {"foo": "bar"})
        result = to_json_object(payload)
        assert result == payload


# ---------------------------------------------------------------------------
# H11 — 4xx exception granularity
# ---------------------------------------------------------------------------


class TestExceptionMapping:
    """Status code to exception type mapping."""

    def test_400_validation_error(self) -> None:
        """400 should map to BlingValidationError."""
        request = httpx.Request("GET", "https://api.bling.test/Api/v3/test")
        response = httpx.Response(400, json={"error": {"message": "Bad request"}}, request=request)
        with pytest.raises(BlingAPIError) as exc_info:
            raise_for_error_response(response)
        assert type(exc_info.value) is BlingValidationError

    def test_405_method_not_allowed(self) -> None:
        """405 should map to BlingMethodNotAllowedError."""
        request = httpx.Request("POST", "https://api.bling.test/Api/v3/test")
        response = httpx.Response(
            405, json={"error": {"message": "Method not allowed"}}, request=request
        )
        with pytest.raises(BlingAPIError) as exc_info:
            raise_for_error_response(response)
        assert type(exc_info.value) is BlingMethodNotAllowedError

    def test_409_conflict(self) -> None:
        """409 should map to BlingConflictError."""
        request = httpx.Request("POST", "https://api.bling.test/Api/v3/test")
        response = httpx.Response(409, json={"error": {"message": "Conflict"}}, request=request)
        with pytest.raises(BlingAPIError) as exc_info:
            raise_for_error_response(response)
        assert type(exc_info.value) is BlingConflictError

    def test_415_unsupported_media_type(self) -> None:
        """415 should map to BlingUnsupportedMediaTypeError."""
        request = httpx.Request("POST", "https://api.bling.test/Api/v3/test")
        response = httpx.Response(
            415,
            json={"error": {"message": "Unsupported media type"}},
            request=request,
        )
        with pytest.raises(BlingAPIError) as exc_info:
            raise_for_error_response(response)
        assert type(exc_info.value) is BlingUnsupportedMediaTypeError

    def test_422_other_4xx_uses_generic_error(self) -> None:
        """422 should map to generic BlingAPIError, not BlingValidationError."""
        request = httpx.Request("POST", "https://api.bling.test/Api/v3/test")
        response = httpx.Response(
            422,
            json={"error": {"message": "Unprocessable entity"}},
            request=request,
        )
        with pytest.raises(BlingAPIError) as exc_info:
            raise_for_error_response(response)
        assert type(exc_info.value) is BlingAPIError
        assert not isinstance(exc_info.value, type(BlingRateLimitError))

    def test_408_timeout_uses_transport_error(self) -> None:
        """408 should map to BlingTransportError."""
        request = httpx.Request("GET", "https://api.bling.test/Api/v3/test")
        response = httpx.Response(
            408,
            json={"error": {"message": "Request timeout"}},
            request=request,
        )
        with pytest.raises(BlingAPIError) as exc_info:
            raise_for_error_response(response)
        assert type(exc_info.value) is BlingTransportError

    def test_429_rate_limit(self) -> None:
        """429 should map to BlingRateLimitError."""
        request = httpx.Request("GET", "https://api.bling.test/Api/v3/test")
        response = httpx.Response(
            429,
            json={"error": {"message": "Rate limit"}},
            request=request,
        )
        with pytest.raises(BlingAPIError) as exc_info:
            raise_for_error_response(response)
        assert isinstance(exc_info.value, BlingRateLimitError)

    def test_500_server_error(self) -> None:
        """500 should map to BlingServerError."""
        request = httpx.Request("GET", "https://api.bling.test/Api/v3/test")
        response = httpx.Response(
            500,
            json={"error": {"message": "Server error"}},
            request=request,
        )
        with pytest.raises(BlingAPIError) as exc_info:
            raise_for_error_response(response)
        assert type(exc_info.value) is BlingServerError


# ---------------------------------------------------------------------------
# H12 — Closed-state tracking
# ---------------------------------------------------------------------------


class TestClosedTransport:
    """SyncTransport should raise after close()."""

    def test_request_after_close_raises_transport_error(self) -> None:
        """Calling request() after close() raises BlingTransportError."""
        transport = SyncTransport(
            auth=httpx.BasicAuth("client", "secret"),
            client=httpx.Client(
                base_url="https://api.bling.test/Api/v3",
                transport=httpx.MockTransport(lambda r: httpx.Response(200, json={}, request=r)),
            ),
            rate_limit_max_requests=None,
        )
        transport.close()
        with pytest.raises(BlingTransportError, match="Transport is closed"):
            transport.request("GET", "/test")

    def test_close_is_idempotent(self) -> None:
        """Calling close() multiple times should not raise."""
        transport = SyncTransport(
            auth=httpx.BasicAuth("client", "secret"),
            client=httpx.Client(
                base_url="https://api.bling.test/Api/v3",
                transport=httpx.MockTransport(lambda r: httpx.Response(200, json={}, request=r)),
            ),
            rate_limit_max_requests=None,
        )
        transport.close()
        transport.close()  # second call should be safe


# ---------------------------------------------------------------------------
# M3 — response_json guard
# ---------------------------------------------------------------------------


class TestResponseJson:
    """response_json and response_json_object guards."""

    def test_response_json_on_empty_body_raises_transport_error(self) -> None:
        """response_json with no content should raise BlingTransportError."""
        response = httpx.Response(204)
        with pytest.raises(BlingTransportError, match="Failed to parse JSON response"):
            response_json(response)

    def test_response_json_valid_json_returns_value(self) -> None:
        """response_json with valid JSON should return the decoded value."""
        response = httpx.Response(200, json={"key": "value"})
        result = response_json(response)
        assert result == {"key": "value"}

    def test_response_json_object_empty_body_returns_empty_dict(self) -> None:
        """response_json_object with no content should return {}."""
        response = httpx.Response(204)
        result = response_json_object(response)
        assert result == {}

    def test_response_json_object_valid_body_returns_dict(self) -> None:
        """response_json_object with valid JSON object should return it."""
        response = httpx.Response(200, json={"data": [1, 2, 3]})
        result = response_json_object(response)
        assert result == {"data": [1, 2, 3]}
