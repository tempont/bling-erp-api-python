"""Validate that the local OpenAPI reference has the expected shape."""

from __future__ import annotations

import json
from pathlib import Path

SPEC_PATH = Path("specs/bling-openapi-reference.json")


def main() -> None:
    """Validate the bundled OpenAPI document."""
    payload = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    if payload.get("openapi") is None:
        msg = "Missing OpenAPI version"
        raise SystemExit(msg)
    if not isinstance(payload.get("paths"), dict):
        msg = "Missing OpenAPI paths"
        raise SystemExit(msg)
    if not isinstance(payload.get("components"), dict):
        msg = "Missing OpenAPI components"
        raise SystemExit(msg)

    print(f"Validated {len(payload['paths'])} OpenAPI paths from {SPEC_PATH}")  # noqa: T201


if __name__ == "__main__":
    main()
