"""OAuth callback parsing and in-memory CSRF state validation for CLI flows."""

from __future__ import annotations

import secrets
from urllib.parse import parse_qs, urlparse


class OAuthCallbackError(ValueError):
    """Raised when callback input is invalid or state does not match."""


def parse_oauth_callback(raw: str) -> tuple[str, str]:
    """Extract ``code`` and ``state`` from a callback URL or query string.

    Accepts a full redirect URL, a ``?code=...&state=...`` fragment, or a bare
    ``code=...&state=...`` query string copied from the browser address bar.

    Args:
        raw: User-provided callback text from the OAuth redirect.

    Returns:
        A tuple of ``(code, state)``.

    Raises:
        OAuthCallbackError: If required parameters are missing or malformed.
    """
    value = raw.strip()
    if not value:
        msg = "Callback URL or query string is required"
        raise OAuthCallbackError(msg)

    if "://" in value:
        query = urlparse(value).query
    elif value.startswith("?"):
        query = value[1:]
    elif "=" in value:
        query = value
    else:
        msg = (
            "Paste the full redirect URL or query string (code=...&state=...), "
            "not only the authorization code"
        )
        raise OAuthCallbackError(msg)

    params = parse_qs(query, keep_blank_values=False)
    code_values = params.get("code", [])
    state_values = params.get("state", [])

    if not code_values or not code_values[0]:
        msg = "Missing 'code' parameter in callback"
        raise OAuthCallbackError(msg)
    if not state_values or not state_values[0]:
        msg = "Missing 'state' parameter in callback"
        raise OAuthCallbackError(msg)

    return code_values[0], state_values[0]


def verify_oauth_state(received_state: str, expected_state: str) -> None:
    """Ensure the callback state matches the value generated for this CLI session.

    The expected state lives only in process memory for the duration of the
    setup command; no database or file is required.

    Args:
        received_state: ``state`` query parameter from the OAuth redirect.
        expected_state: Random value generated before opening the authorize URL.

    Raises:
        OAuthCallbackError: If the states do not match.
    """
    if not expected_state:
        msg = "Expected OAuth state was not generated for this session"
        raise OAuthCallbackError(msg)
    if not secrets.compare_digest(received_state, expected_state):
        msg = "OAuth state mismatch; aborting to prevent CSRF"
        raise OAuthCallbackError(msg)
