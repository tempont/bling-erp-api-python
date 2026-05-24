"""Smoke tests for package bootstrap."""

import bling_erp_api


def test_package_imports() -> None:
    """Package should import and expose a module docstring."""
    assert bling_erp_api.__doc__ == "Bling ERP API SDK."
