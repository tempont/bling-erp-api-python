"""Contract tests for Bling Logísticas operations."""

from __future__ import annotations

import json
from pathlib import Path
from typing import cast

from bling_erp_api.contracts.generated.logisticas import LOGISTICAS_OPERATIONS
from bling_erp_api.contracts.generated.logisticas_etiquetas import (
    LOGISTICAS_ETIQUETAS_OPERATIONS,
)
from bling_erp_api.contracts.generated.logisticas_objetos import (
    LOGISTICAS_OBJETOS_OPERATIONS,
)
from bling_erp_api.contracts.generated.logisticas_remessas import (
    LOGISTICAS_REMESSAS_OPERATIONS,
)
from bling_erp_api.contracts.generated.logisticas_servicos import (
    LOGISTICAS_SERVICOS_OPERATIONS,
)

SPEC_PATH = Path("specs/bling-openapi-reference.json")

# Base Logistics operations: paths that are NOT sub-resource paths
_BASE_PATH_PREFIXES = ("/logisticas",)
_BASE_EXCLUDE_PREFIXES = (
    "/logisticas/servicos",
    "/logisticas/objetos",
    "/logisticas/etiquetas",
    "/logisticas/remessas",
)

# Sub-resource actions that are included by include_actions
_BASE_EXCLUDE_ACTIONS = frozenset(
    {
        "AlterarSituacaoLogisticaServico",
        "ObterLogisticaRemessaMultiplos",
    }
)


def _is_base_logisticas_path(path: str) -> bool:
    """Check if path belongs to base Logisticas (not a sub-resource)."""
    if not path.startswith(_BASE_PATH_PREFIXES[0]):
        return False
    return all(not path.startswith(exclude) for exclude in _BASE_EXCLUDE_PREFIXES)


def _get_base_spec_operations(payload: dict[str, object]) -> set[tuple[str, str, str]]:
    """Get spec operations belonging to base Logistics (not sub-resources)."""
    paths = cast("dict[str, object]", payload["paths"])
    result: set[tuple[str, str, str]] = set()
    for path, methods in paths.items():
        if not _is_base_logisticas_path(path):
            continue
        for method, operation in cast("dict[str, object]", methods).items():
            if method.upper() in ("OPTIONS", "HEAD"):
                continue
            resource = cast("dict[str, object]", operation).get("x-api-resource", "")
            action = str(cast("dict[str, object]", operation).get("x-api-action", ""))
            if resource == "Logisticas" and action not in _BASE_EXCLUDE_ACTIONS:
                result.add((str(method).upper(), path, action))
    return result


def test_logisticas_contracts_cover_base_operations() -> None:
    """Base LOGISTICAS_OPERATIONS should cover only base logistics operations."""
    payload = cast("dict[str, object]", json.loads(SPEC_PATH.read_text(encoding="utf-8")))
    spec_operations = _get_base_spec_operations(payload)

    contracted_operations = {
        (operation.method, operation.path, operation.action)
        for operation in LOGISTICAS_OPERATIONS.values()
    }

    assert contracted_operations == spec_operations, (
        f"Base logistics contracts differ. Contract: {len(contracted_operations)} ops, "
        f"Spec: {len(spec_operations)} ops"
    )


def test_logisticas_sub_resource_contracts_generated() -> None:
    """Each logistics sub-resource should have its own generated contracts."""
    assert len(LOGISTICAS_SERVICOS_OPERATIONS) >= 3, (
        f"Expected at least 3 servicos operations, got {len(LOGISTICAS_SERVICOS_OPERATIONS)}"
    )
    assert len(LOGISTICAS_OBJETOS_OPERATIONS) >= 3, (
        f"Expected at least 3 objetos operations, got {len(LOGISTICAS_OBJETOS_OPERATIONS)}"
    )
    assert len(LOGISTICAS_ETIQUETAS_OPERATIONS) >= 1, (
        f"Expected at least 1 etiquetas operation, got {len(LOGISTICAS_ETIQUETAS_OPERATIONS)}"
    )
    assert len(LOGISTICAS_REMESSAS_OPERATIONS) >= 4, (
        f"Expected at least 4 remessas operations, got {len(LOGISTICAS_REMESSAS_OPERATIONS)}"
    )
