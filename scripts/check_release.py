"""Lightweight release sanity checks."""

from __future__ import annotations

import tomllib
from pathlib import Path

PYPROJECT_PATH = Path("pyproject.toml")


def main() -> None:
    """Check release metadata before tagging."""
    payload = tomllib.loads(PYPROJECT_PATH.read_text(encoding="utf-8"))
    project = payload.get("project", {})
    name = project.get("name")
    version = project.get("version")
    if not name or not version:
        msg = "Project name and version are required"
        raise SystemExit(msg)

    print(f"Release candidate: {name} {version}")  # noqa: T201


if __name__ == "__main__":
    main()
