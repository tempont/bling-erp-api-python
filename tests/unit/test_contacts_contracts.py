"""Tests for OpenAPI-derived contacts contracts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import cast

from bling_erp_api.contracts.generated.contacts import CONTACT_OPERATIONS

SPEC_PATH = Path("specs/bling-openapi-reference.json")


def test_contacts_contract_covers_openapi_operations() -> None:
    """Generated contracts should cover every Contatos / ContatosTipos operation."""
    payload = cast("dict[str, object]", json.loads(SPEC_PATH.read_text(encoding="utf-8")))
    paths = cast("dict[str, object]", payload["paths"])
    official_operations = {
        (
            str(method).upper(),
            path,
            str(cast("dict[str, object]", operation)["x-api-action"]),
        )
        for path, methods in paths.items()
        for method, operation in cast("dict[str, object]", methods).items()
        if cast("dict[str, object]", operation).get("x-api-resource")
        in ("Contatos", "ContatosTipos")
    }

    contracted_operations = {
        (operation.method, operation.path, operation.action)
        for operation in CONTACT_OPERATIONS.values()
    }

    assert contracted_operations == official_operations
