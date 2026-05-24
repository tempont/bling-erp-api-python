"""Plan resource generation from OpenAPI metadata."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from collections.abc import Mapping

SPEC_PATH = Path("specs/bling-openapi-reference.json")
RESOURCES_DIR = Path("src/bling_erp_api/resources")


def main() -> None:
    """Print the resource modules suggested by OpenAPI metadata."""
    payload = cast("dict[str, object]", json.loads(SPEC_PATH.read_text(encoding="utf-8")))
    resources = _resources_by_metadata(payload)
    print(f"Resource output directory: {RESOURCES_DIR}")  # noqa: T201
    for resource, paths in sorted(resources.items()):
        print(f"- {resource}: {len(paths)} paths")  # noqa: T201


def _resources_by_metadata(payload: dict[str, object]) -> dict[str, set[str]]:
    paths = _mapping(payload.get("paths"))
    resources: dict[str, set[str]] = defaultdict(set)

    for path_object, methods in paths.items():
        methods_mapping = _mapping(methods)
        if not methods_mapping:
            continue
        path = str(path_object)
        for operation in methods_mapping.values():
            operation_mapping = _mapping(operation)
            resource = str(operation_mapping.get("x-api-resource") or "unknown")
            resources[resource].add(path)

    return resources


def _mapping(value: object) -> Mapping[str, object]:
    if isinstance(value, dict):
        return cast("Mapping[str, object]", value)
    return {}


if __name__ == "__main__":
    main()
