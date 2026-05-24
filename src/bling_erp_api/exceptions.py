"""Exception hierarchy for Bling API failures."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    import httpx

    from bling_erp_api.types import JsonValue

HTTP_BAD_REQUEST = 400
HTTP_UNAUTHORIZED = 401
HTTP_FORBIDDEN = 403
HTTP_NOT_FOUND = 404
HTTP_TOO_MANY_REQUESTS = 429
HTTP_INTERNAL_SERVER_ERROR = 500


class BlingAPIError(Exception):
    """Base class for SDK and API errors."""

    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = None,
        payload: JsonValue | None = None,
        response: httpx.Response | None = None,
    ) -> None:
        """Create an API error with optional response context."""
        super().__init__(message)
        self.status_code = status_code
        self.payload = payload
        self.response = response


class BlingTransportError(BlingAPIError):
    """Raised when the HTTP request cannot be completed."""


class BlingAuthenticationError(BlingAPIError):
    """Raised for authentication and authorization failures."""


class BlingValidationError(BlingAPIError):
    """Raised for request validation failures."""


class BlingNotFoundError(BlingAPIError):
    """Raised when an API resource is not found."""


class BlingRateLimitError(BlingAPIError):
    """Raised when the API rate limit is reached."""


class BlingServerError(BlingAPIError):
    """Raised for Bling server-side failures."""


def raise_for_error_response(response: httpx.Response) -> None:
    """Raise a typed SDK exception for non-successful responses."""
    if response.status_code < HTTP_BAD_REQUEST:
        return

    payload = _safe_json(response)
    message = _extract_error_message(payload) or response.text or response.reason_phrase
    error_type = _error_type_for_status(response.status_code)
    raise error_type(
        message,
        status_code=response.status_code,
        payload=payload,
        response=response,
    )


def _safe_json(response: httpx.Response) -> JsonValue | None:
    try:
        return cast("JsonValue", response.json())
    except ValueError:
        return None


def _extract_error_message(payload: JsonValue | None) -> str | None:
    if not isinstance(payload, dict):
        return None

    error = payload.get("error")
    if isinstance(error, str):
        return error
    if isinstance(error, dict):
        message = error.get("message") or error.get("description")
        if isinstance(message, str):
            return message

    message = payload.get("message") or payload.get("descricao") or payload.get("description")
    return message if isinstance(message, str) else None


def _error_type_for_status(status_code: int) -> type[BlingAPIError]:
    if status_code in {HTTP_UNAUTHORIZED, HTTP_FORBIDDEN}:
        return BlingAuthenticationError
    if status_code == HTTP_NOT_FOUND:
        return BlingNotFoundError
    if status_code == HTTP_TOO_MANY_REQUESTS:
        return BlingRateLimitError
    if HTTP_BAD_REQUEST <= status_code < HTTP_INTERNAL_SERVER_ERROR:
        return BlingValidationError
    if status_code >= HTTP_INTERNAL_SERVER_ERROR:
        return BlingServerError
    return BlingAPIError
