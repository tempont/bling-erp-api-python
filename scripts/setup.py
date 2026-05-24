"""One-shot CLI helper to complete Bling OAuth and persist tokens."""

from __future__ import annotations

import secrets
import sys

from bling_jwt_auth import BlingAuthSettings, OAuthClient, TokenManager, create_token_store

from bling_erp_api.auth.authenticate import (
    OAuthCallbackError,
    parse_oauth_callback,
    verify_oauth_state,
)


def main() -> None:
    """Run the interactive OAuth setup flow.

    This script will:
    - Load the BlingAuthSettings from the environment variables.
    - Create a token store.
    - Create an OAuth client.
    - Create a token manager.
    - Build the authorization URL.
    """
    print("Starting authentication...")  # noqa: T201
    settings = BlingAuthSettings.load()
    store = create_token_store(settings)

    with OAuthClient(settings) as oauth:
        manager = TokenManager(oauth, store, settings)
        expected_state = secrets.token_urlsafe(32)
        url = oauth.build_authorization_url(state=expected_state)
        print("Open this URL in your browser:\n", url)  # noqa: T201
        print(  # noqa: T201
            "\nAfter authorization, paste the full callback URL "
            "(or the query string with code and state):"
        )

        try:
            callback = input("Callback URL: ").strip()
            code, received_state = parse_oauth_callback(callback)
            verify_oauth_state(received_state, expected_state)
        except OAuthCallbackError as exc:
            print(f"Authentication failed: {exc}", file=sys.stderr)  # noqa: T201
            sys.exit(1)

        manager.save_from_code(code)

    print("Authentication successful.")  # noqa: T201


if __name__ == "__main__":
    main()
