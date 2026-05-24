"""Bling API client factory."""

from bling_jwt_auth import BlingClient


def get_client() -> BlingClient:
    """Get a client to the Bling API."""
    return BlingClient.from_env()
