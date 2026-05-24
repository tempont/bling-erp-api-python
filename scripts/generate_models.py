"""Plan model generation from the local Bling OpenAPI reference."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from collections.abc import Mapping

SPEC_PATH = Path("specs/bling-openapi-reference.json")
GENERATED_DIR = Path("src/bling_erp_api/models/generated")


def main() -> None:
    """Print a resource grouping plan for future generated models."""
    payload = cast("dict[str, object]", json.loads(SPEC_PATH.read_text(encoding="utf-8")))
    schemas = _mapping(_mapping(payload.get("components")).get("schemas"))
    resources = _resource_names(payload)

    print(f"OpenAPI schemas: {len(schemas)}")  # noqa: T201
    print(f"Generated models directory: {GENERATED_DIR}")  # noqa: T201
    for resource, operations in sorted(resources.items()):
        print(f"- {resource}: {len(operations)} operations")  # noqa: T201


def _resource_names(payload: dict[str, object]) -> dict[str, list[str]]:
    paths = _mapping(payload.get("paths"))
    grouped: dict[str, list[str]] = defaultdict(list)

    for path_object, methods in paths.items():
        methods_mapping = _mapping(methods)
        if not methods_mapping:
            continue
        path = str(path_object)
        for method_object, operation in methods_mapping.items():
            operation_mapping = _mapping(operation)
            if not operation_mapping:
                continue
            method = str(method_object)
            resource = str(operation_mapping.get("x-api-resource") or "unknown")
            action = str(operation_mapping.get("x-api-action") or method)
            grouped[resource].append(f"{method.upper()} {path} ({action})")

    return grouped


def _mapping(value: object) -> Mapping[str, object]:
    if isinstance(value, dict):
        return cast("Mapping[str, object]", value)
    return {}


if __name__ == "__main__":
    main()
