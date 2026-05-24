"""Smoke tests for package bootstrap."""

import bling_erp_api


def test_package_imports() -> None:
    """Package should import and expose the public client."""
    assert bling_erp_api.BlingClient is not None
