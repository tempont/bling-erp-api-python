"""Contract tests for Bling Caixas e Bancos operations."""

from __future__ import annotations

import json
from pathlib import Path
from typing import cast

from bling_erp_api.contracts.generated.caixas_bancos import CAIXAS_BANCOS_OPERATIONS

SPEC_PATH = Path("specs/bling-openapi-reference.json")


def test_caixas_bancos_contracts_cover_all_spec_operations() -> None:
    """Generated contracts should cover every Caixas operation in OpenAPI."""
    payload = cast("dict[str, object]", json.loads(SPEC_PATH.read_text(encoding="utf-8")))
    paths = cast("dict[str, object]", payload["paths"])

    spec_operations: set[tuple[str, str, str]] = set()
    for path, methods in paths.items():
        if path.startswith("/caixas"):
            for method, operation in cast("dict[str, object]", methods).items():
                if method.upper() in ("OPTIONS", "HEAD"):
                    continue
                resource = cast("dict[str, object]", operation).get("x-api-resource", "")
                if resource == "Caixas":
                    spec_operations.add(
                        (
                            str(method).upper(),
                            path,
                            str(cast("dict[str, object]", operation)["x-api-action"]),
                        )
                    )

    contracted_operations = {
        (operation.method, operation.path, operation.action)
        for operation in CAIXAS_BANCOS_OPERATIONS.values()
    }

    assert contracted_operations == spec_operations


def test_caixas_bancos_contracts_no_extra_operations() -> None:
    """Every CAIXAS_BANCOS_OPERATIONS entry action must map to a spec operation."""
    payload = cast("dict[str, object]", json.loads(SPEC_PATH.read_text(encoding="utf-8")))
    paths = cast("dict[str, object]", payload["paths"])

    spec_actions: set[str] = set()
    for path, methods in paths.items():
        if path.startswith("/caixas"):
            for method, operation in cast("dict[str, object]", methods).items():
                if method.upper() in ("OPTIONS", "HEAD"):
                    continue
                resource = cast("dict[str, object]", operation).get("x-api-resource", "")
                if resource == "Caixas":
                    spec_actions.add(str(cast("dict[str, object]", operation)["x-api-action"]))

    contract_actions = {op.action for op in CAIXAS_BANCOS_OPERATIONS.values()}
    assert contract_actions == spec_actions
