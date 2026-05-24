"""Tests for OAuth callback parsing and state verification."""

import pytest

from bling_erp_api.auth.authenticate import (
    OAuthCallbackError,
    parse_oauth_callback,
    verify_oauth_state,
)

CALLBACK_URL = "http://localhost:8080/oauth/callback?code=abc123&state=expected-state-value"


def test_parse_oauth_callback_from_full_url() -> None:
    """Full redirect URLs should yield code and state."""
    code, state = parse_oauth_callback(CALLBACK_URL)
    assert code == "abc123"
    assert state == "expected-state-value"


def test_parse_oauth_callback_from_query_string() -> None:
    """Bare query strings should also be accepted."""
    code, state = parse_oauth_callback("code=abc123&state=expected-state-value")
    assert code == "abc123"
    assert state == "expected-state-value"


def test_parse_oauth_callback_rejects_code_only() -> None:
    """Pasting only the authorization code should fail with guidance."""
    with pytest.raises(OAuthCallbackError, match="not only the authorization code"):
        parse_oauth_callback("abc123")


def test_parse_oauth_callback_rejects_missing_state() -> None:
    """Callbacks without state must be rejected."""
    with pytest.raises(OAuthCallbackError, match="Missing 'state'"):
        parse_oauth_callback("code=abc123")


def test_verify_oauth_state_accepts_matching_value() -> None:
    """Matching states should pass without error."""
    verify_oauth_state("same-value", "same-value")


def test_verify_oauth_state_rejects_mismatch() -> None:
    """Mismatched states should abort the flow."""
    with pytest.raises(OAuthCallbackError, match="state mismatch"):
        verify_oauth_state("received", "expected")
