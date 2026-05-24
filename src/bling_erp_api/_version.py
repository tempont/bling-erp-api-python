"""Package version metadata."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("bling-erp-api")
except PackageNotFoundError:
    __version__ = "0.0.0"
