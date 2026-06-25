"""Exception hierarchy for Bling API failures."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from collections.abc import Mapping

    import httpx

    from bling_erp_api.types import JsonValue

HTTP_BAD_REQUEST = 400
HTTP_UNAUTHORIZED = 401
HTTP_FORBIDDEN = 403
HTTP_NOT_FOUND = 404
HTTP_TOO_MANY_REQUESTS = 429
HTTP_METHOD_NOT_ALLOWED = 405
HTTP_REQUEST_TIMEOUT = 408
HTTP_CONFLICT = 409
HTTP_UNSUPPORTED_MEDIA_TYPE = 415
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


class BlingMethodNotAllowedError(BlingAPIError):
    """Raised when the API returns 405 Method Not Allowed."""


class BlingConflictError(BlingAPIError):
    """Raised when the API returns 409 Conflict."""


class BlingUnsupportedMediaTypeError(BlingAPIError):
    """Raised when the API returns 415 Unsupported Media Type."""


class BlingServerError(BlingAPIError):
    """Raised for Bling server-side failures."""


def raise_for_error_response(response: httpx.Response) -> None:
    """Raise a typed SDK exception for non-successful responses."""
    if response.status_code < HTTP_BAD_REQUEST:
        return

    payload = _safe_json(response)
    api_message = _extract_error_message(payload) or response.text or response.reason_phrase
    message = _format_error_message(
        api_message,
        status_code=response.status_code,
        request_target=_request_target(response),
    )
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
        message = _error_text(cast("Mapping[str, object]", error))
        if message is not None:
            return message

    return _error_text(cast("Mapping[str, object]", payload))


def _error_text(error: Mapping[str, object]) -> str | None:
    message = _string_value(error.get("message") or error.get("descricao"))
    description = _string_value(error.get("description"))
    error_type = _string_value(error.get("type"))
    fields = _format_error_fields(error.get("fields"))

    parts: list[str] = []
    if error_type is not None:
        parts.append(error_type)
    if message is not None:
        parts.append(message)
    if description is not None and description != message:
        parts.append(description)
    if fields is not None:
        parts.append(f"fields: {fields}")

    return "; ".join(parts) if parts else None


def _format_error_fields(value: object) -> str | None:
    if not isinstance(value, list):
        return None

    fields = [_format_error_field(item) for item in cast("list[object]", value)]
    fields = [field for field in fields if field is not None]
    return "; ".join(fields) if fields else None


def _format_error_field(value: object) -> str | None:
    if not isinstance(value, dict):
        return None

    field = cast("Mapping[str, object]", value)
    message = _string_value(field.get("msg") or field.get("message"))
    element = _string_value(field.get("element") or field.get("namespace"))
    code = field.get("code")
    collection = _format_error_collection(field.get("collection"))

    label = element or "field"
    if isinstance(code, int):
        label = f"{label} ({code})"
    formatted = label if message is None else f"{label}: {message}"
    if collection is not None:
        return f"{formatted}; {collection}"
    return formatted


def _format_error_collection(value: object) -> str | None:
    if not isinstance(value, list):
        return None

    items = [_format_error_collection_item(item) for item in cast("list[object]", value)]
    items = [item for item in items if item is not None]
    return "; ".join(items) if items else None


def _format_error_collection_item(value: object) -> str | None:
    if not isinstance(value, dict):
        return None

    item = cast("Mapping[str, object]", value)
    message = _string_value(item.get("msg") or item.get("message"))
    element = _string_value(item.get("element") or item.get("namespace"))
    index = item.get("index")
    code = item.get("code")

    label = element or "item"
    if isinstance(index, int):
        label = f"{label}[{index}]"
    if isinstance(code, int):
        label = f"{label} ({code})"
    if message is None:
        return label
    return f"{label}: {message}"


def _string_value(value: object) -> str | None:
    return value if isinstance(value, str) and value else None


def _format_error_message(
    api_message: str,
    *,
    status_code: int,
    request_target: str | None,
) -> str:
    if request_target is None:
        return f"Bling API returned {status_code}: {api_message}"
    return f"{request_target} returned {status_code}: {api_message}"


def _request_target(response: httpx.Response) -> str | None:
    try:
        request = response.request
    except RuntimeError:
        return None

    path = request.url.raw_path.decode("ascii", errors="replace")
    return f"{request.method} {path}"


_STATUS_CODE_MAP: dict[int, type[BlingAPIError]] = {
    HTTP_BAD_REQUEST: BlingValidationError,
    HTTP_UNAUTHORIZED: BlingAuthenticationError,
    HTTP_FORBIDDEN: BlingAuthenticationError,
    HTTP_NOT_FOUND: BlingNotFoundError,
    HTTP_METHOD_NOT_ALLOWED: BlingMethodNotAllowedError,
    HTTP_REQUEST_TIMEOUT: BlingTransportError,
    HTTP_CONFLICT: BlingConflictError,
    HTTP_UNSUPPORTED_MEDIA_TYPE: BlingUnsupportedMediaTypeError,
    HTTP_TOO_MANY_REQUESTS: BlingRateLimitError,
}


def _error_type_for_status(status_code: int) -> type[BlingAPIError]:
    error_type = _STATUS_CODE_MAP.get(status_code)
    if error_type is not None:
        return error_type
    if HTTP_BAD_REQUEST <= status_code < HTTP_INTERNAL_SERVER_ERROR:
        return BlingAPIError
    if status_code >= HTTP_INTERNAL_SERVER_ERROR:
        return BlingServerError
    return BlingAPIError
