"""Tests for BlingAuth environment bootstrap."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_jwt_auth import BlingAuth

if TYPE_CHECKING:
    import pytest


def test_auth_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    """BlingAuth should load from required BLING_* environment variables."""
    monkeypatch.setenv("BLING_CLIENT_ID", "test-client-id")
    monkeypatch.setenv("BLING_CLIENT_SECRET", "test-client-secret")
    monkeypatch.setenv("BLING_REDIRECT_URI", "http://localhost:8080/oauth/callback")

    auth = BlingAuth.from_env()
    assert auth is not None
