"""Tests for 204 No Content response handling.

Verifies that:
- ``_parse_response`` never returns ``None`` for 204 (empty) responses
- ``_validate_response`` handles ``None`` payload gracefully
- Raw ``ValidationError`` is wrapped in ``BlingAPIError`` with context
- Resource methods receiving 204 responses return ``{}`` or empty models
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from pydantic import BaseModel

from bling_erp_api.exceptions import BlingAPIError
from bling_erp_api.resources.base import (
    BaseResource,
    _parse_response,  # pyright: ignore[reportPrivateUsage]
)
from bling_erp_api.resources.contacts import ContactsResource
from bling_erp_api.resources.product_groups import ProductGroupsResource

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject

# ---------------------------------------------------------------------------
# Test helpers
# ---------------------------------------------------------------------------


class SimpleModel(BaseModel):
    """A simple Pydantic model with a required field."""

    name: str


class ModelWithOptionalData(BaseModel):
    """A model with optional data field."""

    data: str | None = None


class _BaseForTest(BaseResource):
    """Minimal BaseResource for testing _validate_response without transport."""

    def __init__(self) -> None:  # type: ignore[override]
        """Skip transport init — _validate_response does not need it."""


TEST_RESOURCE = _BaseForTest()


class RecordingTransport204:
    """Transport that simulates a 204 No Content response (empty dict)."""

    def __init__(self) -> None:
        """Initialize recorder."""
        self.calls: list[tuple[str, str, object, object]] = []

    def request(
        self,
        method: str,
        path: str,
        *,
        params: object = None,
        json: object = None,
        headers: object = None,  # noqa: ARG002
    ) -> JsonObject:
        """Record request and return empty dict (204 simulation)."""
        self.calls.append((method, path, params, json))
        return {}


# ---------------------------------------------------------------------------
# _parse_response tests — B7 fix
# ---------------------------------------------------------------------------


def test_parse_response_never_returns_none() -> None:
    """_parse_response should never return None for any input."""
    result = _parse_response("DELETE", "/contatos/123", {})
    assert result is not None
    assert result == {}


def test_parse_response_with_arbitrary_path_returns_payload() -> None:
    """_parse_response with an unknown path should still return the payload."""
    payload: JsonObject = {"foo": "bar"}
    result = _parse_response("GET", "/unknown/path", payload)
    assert result == payload


def test_parse_response_returns_empty_dict_for_empty_payload() -> None:
    """_parse_response should return {} not None for empty payload."""
    result = _parse_response("DELETE", "/some/resource", {})
    assert result == {}


def test_parse_response_type_is_dict_not_none() -> None:
    """Ensure _parse_response return is always a dict, even for 204-like inputs."""
    result = _parse_response("DELETE", "/contatos/999", {})
    assert isinstance(result, dict)


# ---------------------------------------------------------------------------
# _validate_response tests — B8 fix
# ---------------------------------------------------------------------------


def test_validate_response_none_payload_does_not_crash() -> None:
    """_validate_response with None payload should not crash."""
    result = TEST_RESOURCE._validate_response(ModelWithOptionalData, None)  # noqa: SLF001  # pyright: ignore[reportPrivateUsage]
    # Must not crash; returns a cast dict-or-model
    assert result is not None


def test_validate_response_none_payload_returns_empty_dict() -> None:
    """_validate_response(None) returns {} (cast) without error."""
    result = TEST_RESOURCE._validate_response(ModelWithOptionalData, None)  # noqa: SLF001  # pyright: ignore[reportPrivateUsage]
    # The result is cast("TResponse", {}) — a plain dict at runtime
    assert result is not None
    assert len(result) == 0  # type: ignore[arg-type]


def test_validate_response_invalid_payload_raises_bling_api_error() -> None:
    """_validate_response with an invalid payload should raise BlingAPIError."""
    with pytest.raises(BlingAPIError) as exc_info:
        TEST_RESOURCE._validate_response(SimpleModel, {"wrong_field": 123})  # noqa: SLF001  # pyright: ignore[reportPrivateUsage]
    assert "Failed to validate response" in str(exc_info.value)


def test_validate_response_invalid_payload_not_raw_validation_error() -> None:
    """Raw ValidationError must not propagate — only BlingAPIError."""
    with pytest.raises(BlingAPIError):
        TEST_RESOURCE._validate_response(SimpleModel, {"nope": True})  # noqa: SLF001  # pyright: ignore[reportPrivateUsage]


def test_validate_response_data_empty_list_fallback_preserved() -> None:
    """The existing {'data': []} fallback in _validate_response is preserved."""
    result = TEST_RESOURCE._validate_response(  # noqa: SLF001  # pyright: ignore[reportPrivateUsage]
        ModelWithOptionalData, {"data": []}
    )
    assert result is not None


# ---------------------------------------------------------------------------
# End-to-end resource method tests
# ---------------------------------------------------------------------------

from bling_erp_api.models.generated.schemas.contatos import (  # noqa: E402
    ContatosDeleteResponse200,
)
from bling_erp_api.models.generated.schemas.grupos_produtos import (  # noqa: E402
    GruposProdutosDeleteResponse200,
)


def test_resource_delete_method_returns_empty_dict_for_204() -> None:
    """A resource DELETE method should return {} (not None) for a 204 response."""
    transport = RecordingTransport204()
    resource = ContactsResource(transport)  # type: ignore[arg-type]

    result = resource.remover(123)

    assert result == {}
    assert transport.calls == [
        ("DELETE", "/contatos/123", None, None),
    ]


def test_resource_remover_varios_does_not_crash_with_204() -> None:
    """remover_varios() should not crash when receiving a 204 (empty) response.

    This exercises the _parse_response + _validate_response pipeline
    with an empty dict payload coming from the transport.
    """
    transport = RecordingTransport204()
    resource = ContactsResource(transport)  # type: ignore[arg-type]

    result = resource.remover_varios([201, 202])

    assert isinstance(result, ContatosDeleteResponse200)
    assert result.data is None
    assert transport.calls == [
        ("DELETE", "/contatos", {"idsContatos[]": [201, 202]}, None),
    ]


def test_resource_remover_varios_with_product_groups_204() -> None:
    """Another resource's remover_varios also handles 204 gracefully."""
    transport = RecordingTransport204()
    resource = ProductGroupsResource(transport)  # type: ignore[arg-type]

    result = resource.remover_varios([10, 20, 30])

    assert isinstance(result, GruposProdutosDeleteResponse200)
    assert result.data is None
