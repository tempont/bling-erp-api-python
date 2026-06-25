"""Base resource helpers."""

from __future__ import annotations

import contextlib
import importlib
import re
from typing import TYPE_CHECKING, Any, cast

from pydantic import BaseModel, ValidationError

from bling_erp_api.exceptions import BlingAPIError, BlingValidationError
from bling_erp_api.pagination import iter_pages

if TYPE_CHECKING:
    from collections.abc import Iterator

    from bling_erp_api.transport.base import Transport
    from bling_erp_api.types import JsonObject, JsonPayload, QueryParams

_operation_docstrings: dict[str, str] | None
try:
    import bling_erp_api.contracts.generated._docstrings as _docstrings_mod  # type: ignore[attr-defined]

    _operation_docstrings = _docstrings_mod.OPERATION_DOCSTRINGS
except (ImportError, AttributeError):
    _operation_docstrings = None

_operation_models: list[dict[str, object]]
try:
    import bling_erp_api.contracts.generated._operation_models as _op_models_mod  # type: ignore[attr-defined]

    _operation_models = list(_op_models_mod.OPERATION_MODELS)
except (ImportError, AttributeError):
    _operation_models = []

# Map English method names to pt-BR equivalents for resources still using English
_ENGLISH_TO_PTBR: dict[str, str] = {
    "list": "listar",
    "iterate": "iterar",
    "get": "obter",
    "create": "criar",
    "update": "alterar",
    "patch": "alterar_parcialmente",
    "delete": "remover",
}


_PATH_TRAVERSAL_PATTERN = re.compile(
    r"(?:^|/)(?:\.\.(?:/|$)|\.\.%2f|\.\.%5c)",
    re.IGNORECASE,
)


def _validate_path(path: str) -> None:
    """Validate that a URL path does not contain traversal sequences."""
    if _PATH_TRAVERSAL_PATTERN.search(path):
        msg = f"Invalid URL path: path traversal sequences are not allowed in '{path}'"
        raise BlingValidationError(msg)


class BaseResource:
    """Common request helpers for resource namespaces."""

    def __init_subclass__(cls, **kwargs: object) -> None:
        """Auto-populate docstrings from generated OpenAPI contracts."""
        super().__init_subclass__(**kwargs)
        cls._autopopulate_docstrings()

    @classmethod
    def _autopopulate_docstrings(cls) -> None:  # noqa: PLR0912
        """Populate __doc__ on methods that lack substantive docstrings."""
        operation_docstrings = _operation_docstrings
        if operation_docstrings is None:
            return  # Generated file doesn't exist yet during development

        for attr_name in dir(cls):
            if attr_name.startswith("_"):
                continue
            method = getattr(cls, attr_name, None)
            if not callable(method):
                continue

            key = f"{cls.__name__}.{attr_name}"

            # Try pt-BR equivalent if direct key not found
            ptbr_name = _ENGLISH_TO_PTBR.get(attr_name)
            if ptbr_name and key not in operation_docstrings:
                ptbr_key = f"{cls.__name__}.{ptbr_name}"
                if ptbr_key in operation_docstrings:
                    key = ptbr_key

            # Check if this is an English alias — extract canonical method name
            existing_doc = (method.__doc__ or "").strip()
            if "Compatibility alias" in existing_doc:
                # Extract canonical method name from "Compatibility alias for ``X()``."
                match = re.search(r"``(\w+)\(\)``", existing_doc)
                if match:
                    canonical = match.group(1)
                    canonical_key = f"{cls.__name__}.{canonical}"
                    if canonical_key in operation_docstrings:
                        alias_doc = (
                            f"Compatibility alias for ``{canonical}()``.\n\n"
                            f"{operation_docstrings[canonical_key]}"
                        )
                        with contextlib.suppress(AttributeError):
                            method.__doc__ = alias_doc  # type: ignore[attr-defined]
                    elif canonical == "iterar":
                        # iterar is a pagination helper, derive from listar
                        listar_key = f"{cls.__name__}.listar"
                        if listar_key in operation_docstrings:
                            alias_doc = (
                                f"Compatibility alias for ``{canonical}()``.\n\n"
                                "Itera pelos registros página a página.\n\n"
                                f"{operation_docstrings[listar_key]}"
                            )
                            with contextlib.suppress(AttributeError):
                                method.__doc__ = alias_doc  # type: ignore[attr-defined]
                continue

            # Handle iterar/iterate pagination helpers: derive from listar
            if attr_name in ("iterar", "iterate") and key not in operation_docstrings:
                listar_key = f"{cls.__name__}.listar"
                if listar_key in operation_docstrings and not is_substantive_docstring(
                    existing_doc
                ):
                    if attr_name == "iterar":
                        prefix = "Itera pelos registros página a página.\n\nUsa os mesmos filtros de ``listar()``.\n\n"
                    else:
                        prefix = "Iterate through records page by page.\n\nUses the same filters as ``listar()``.\n\n"
                    iterar_doc = prefix + operation_docstrings[listar_key]
                    with contextlib.suppress(AttributeError):
                        method.__doc__ = iterar_doc  # type: ignore[attr-defined]
                continue

            # For canonical methods: use generated docstring if existing one is minimal
            if key in operation_docstrings and not is_substantive_docstring(existing_doc):
                with contextlib.suppress(AttributeError):
                    method.__doc__ = operation_docstrings[key]  # type: ignore[attr-defined]

    def __init__(self, transport: Transport) -> None:
        """Create a resource bound to a transport."""
        self._transport = transport

    def _get(self, path: str, *, params: QueryParams | None = None) -> JsonObject:
        """Send a GET request."""
        _validate_path(path)
        payload = self._transport.request("GET", path, params=params)
        return cast("JsonObject", _parse_response("GET", path, payload))

    def _post(
        self,
        path: str,
        *,
        params: QueryParams | None = None,
        json: JsonPayload | None = None,
        headers: dict[str, str] | None = None,
    ) -> JsonObject:
        """Send a POST request."""
        _validate_path(path)
        payload = self._transport.request("POST", path, params=params, json=json, headers=headers)
        return cast("JsonObject", _parse_response("POST", path, payload))

    def _put(
        self,
        path: str,
        *,
        json: JsonPayload | None = None,
        headers: dict[str, str] | None = None,
    ) -> JsonObject:
        """Send a PUT request."""
        _validate_path(path)
        payload = self._transport.request("PUT", path, json=json, headers=headers)
        return cast("JsonObject", _parse_response("PUT", path, payload))

    def _patch(
        self,
        path: str,
        *,
        json: JsonPayload | None = None,
        headers: dict[str, str] | None = None,
    ) -> JsonObject:
        """Send a PATCH request."""
        _validate_path(path)
        payload = self._transport.request("PATCH", path, json=json, headers=headers)
        return cast("JsonObject", _parse_response("PATCH", path, payload))

    def _delete(
        self,
        path: str,
        *,
        params: QueryParams | None = None,
        headers: dict[str, str] | None = None,
    ) -> JsonObject:
        """Send a DELETE request."""
        _validate_path(path)
        payload = self._transport.request("DELETE", path, params=params, headers=headers)
        return cast("JsonObject", _parse_response("DELETE", path, payload))

    def _validate_response[TResponse: BaseModel](
        self,
        model: type[TResponse],
        payload: object,
    ) -> TResponse:
        """Validate a parsed response against a concrete response model."""
        if payload is None:
            return cast("TResponse", cast("Any", {}))
        try:
            return model.model_validate(payload)
        except ValidationError as exc:
            if payload == {"data": []}:
                try:
                    return model.model_validate({"data": None})
                except ValidationError:
                    return cast("TResponse", payload)
            msg = f"Failed to validate response: {exc}"
            raise BlingAPIError(msg) from exc

    def _iterate(
        self,
        path: str,
        *,
        page: int = 1,
        limit: int = 100,
        params: QueryParams | None = None,
    ) -> Iterator[JsonObject]:
        """Iterate through paginated records for an endpoint."""
        _validate_path(path)
        item_model = _response_item_model("GET", path)

        def fetch_page(next_page: int) -> JsonObject:
            return self._transport.request(
                "GET",
                path,
                params={"pagina": next_page, "limite": limit, **dict(params or {})},
            )

        for record in iter_pages(fetch_page, start_page=page):
            if item_model is None:
                yield record
            else:
                yield cast("JsonObject", item_model.model_validate(record).model_dump(mode="json"))


_MIN_SUBSTANTIVE_LINES = 3
_MIN_SUBSTANTIVE_LENGTH = 60


def is_substantive_docstring(doc: str) -> bool:
    """Return True if the docstring is already detailed enough to keep."""
    if not doc.strip():
        return False
    lines = [line.strip() for line in doc.strip().split("\n") if line.strip()]
    if len(lines) >= _MIN_SUBSTANTIVE_LINES:
        return True
    if "Args:" in doc or "Returns:" in doc or "Raises:" in doc:
        return True
    return len(doc) > _MIN_SUBSTANTIVE_LENGTH


def _parse_response(method: str, path: str, payload: JsonObject) -> BaseModel | JsonObject:
    model = _response_model(method, path)
    if model is None:
        return payload
    try:
        return model.model_validate(payload)
    except ValidationError:
        if payload == {"data": []}:
            return payload
        raise


def _response_model(method: str, path: str) -> type[BaseModel] | None:
    entry = _operation_entry(method, path)
    if entry is None:
        return None
    model_path = entry.get("response_model")
    if not isinstance(model_path, str):
        return None
    return _load_model(model_path)


def _response_item_model(method: str, path: str) -> type[BaseModel] | None:
    entry = _operation_entry(method, path)
    if entry is None:
        return None
    model_path = entry.get("response_item_model")
    if not isinstance(model_path, str):
        return None
    return _load_model(model_path)


def _operation_entry(method: str, path: str) -> dict[str, object] | None:
    normalized = path.split("?", maxsplit=1)[0].rstrip("/") or "/"
    matches: list[dict[str, object]] = []
    for entry in _operation_models:
        if entry.get("method") != method:
            continue
        pattern = entry.get("pattern")
        if isinstance(pattern, str) and re.fullmatch(pattern, normalized):
            matches.append(entry)
    if not matches:
        return None
    return max(matches, key=_operation_specificity)


def _operation_specificity(entry: dict[str, object]) -> tuple[int, int, int]:
    path = entry.get("path")
    if not isinstance(path, str):
        return (0, 0, 0)

    segments = [segment for segment in path.strip("/").split("/") if segment]
    literal_segments = [segment for segment in segments if not _is_path_parameter(segment)]
    literal_length = sum(len(segment) for segment in literal_segments)
    return (len(literal_segments), literal_length, len(segments))


def _is_path_parameter(segment: str) -> bool:
    return segment.startswith("{") and segment.endswith("}")


def _load_model(model_path: str) -> type[BaseModel]:
    module_name, class_name = model_path.rsplit(".", maxsplit=1)
    module = importlib.import_module(module_name)
    model = getattr(module, class_name)
    if not isinstance(model, type) or not issubclass(model, BaseModel):
        msg = f"Generated operation model is not a Pydantic model: {model_path}"
        raise TypeError(msg)
    return model
