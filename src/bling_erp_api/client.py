"""Main SDK client."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self

from bling_erp_api.auth import BlingAuthAdapter
from bling_erp_api.config import DEFAULT_API_BASE_URL, DEFAULT_TIMEOUT_SECONDS
from bling_erp_api.resources import (
    ContactsResource,
    InvoicesResource,
    ProductsResource,
    SalesOrdersResource,
)
from bling_erp_api.transport.sync import SyncTransport

if TYPE_CHECKING:
    from types import TracebackType

    import httpx

    from bling_erp_api.auth import AccessTokenProvider


class BlingClient:
    """Synchronous client for the Bling API."""

    def __init__(
        self,
        *,
        token_provider: AccessTokenProvider | None = None,
        auth: httpx.Auth | None = None,
        base_url: str = DEFAULT_API_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
        http_client: httpx.Client | None = None,
    ) -> None:
        """Create a client and attach resource namespaces."""
        resolved_auth = auth or _auth_from_token_provider(token_provider)
        self._transport = SyncTransport(
            auth=resolved_auth,
            base_url=base_url,
            timeout=timeout,
            client=http_client,
        )

        self.contacts = ContactsResource(self._transport)
        self.products = ProductsResource(self._transport)
        self.sales_orders = SalesOrdersResource(self._transport)
        self.invoices = InvoicesResource(self._transport)

    @classmethod
    def from_env(
        cls,
        *,
        base_url: str = DEFAULT_API_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
        http_client: httpx.Client | None = None,
    ) -> Self:
        """Create a client using ``BLING_*`` settings from ``bling-jwt-auth``."""
        return cls(
            auth=BlingAuthAdapter.from_env(),
            base_url=base_url,
            timeout=timeout,
            http_client=http_client,
        )

    def close(self) -> None:
        """Close owned resources."""
        self._transport.close()

    def __enter__(self) -> Self:
        """Return this client for context manager usage."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Close resources when leaving a context manager."""
        self.close()


def _auth_from_token_provider(token_provider: AccessTokenProvider | None) -> httpx.Auth:
    if token_provider is None:
        return BlingAuthAdapter.from_env()
    return BlingAuthAdapter(token_provider)
