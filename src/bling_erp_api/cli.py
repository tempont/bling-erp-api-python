"""Command-line entry point for SDK maintenance commands."""

from __future__ import annotations

import argparse

from bling_erp_api._version import __version__


def main() -> None:
    """Run the SDK CLI."""
    parser = argparse.ArgumentParser(
        prog="bling-erp-api",
        description="Bling ERP API SDK",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"bling-erp-api {__version__}",
    )
    parser.parse_args()
    print(f"Bling ERP API SDK v{__version__}")  # noqa: T201
    print("Documentation: https://tempont.github.io/bling-erp-api-python/")  # noqa: T201
