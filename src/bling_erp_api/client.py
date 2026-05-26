"""Main SDK client."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self

from bling_erp_api.auth import BlingAuthAdapter
from bling_erp_api.config import (
    DEFAULT_API_BASE_URL,
    DEFAULT_RATE_LIMIT_MAX_REQUESTS,
    DEFAULT_RATE_LIMIT_MAX_RETRIES,
    DEFAULT_RATE_LIMIT_PERIOD_SECONDS,
    DEFAULT_TIMEOUT_SECONDS,
)
from bling_erp_api.resources import (
    AdCategoriesResource,
    AdsResource,
    BorderosResource,
    CaixasBancosResource,
    ContactsResource,
    NfceResource,
    NfeResource,
    NfseResource,
    ProductBatchEntriesResource,
    ProductBatchesResource,
    ProductsResource,
    ProductStoresResource,
    ProductStructuresResource,
    ProductSuppliersResource,
    ProductVariationsResource,
    SalesOrdersResource,
)
from bling_erp_api.transport.sync import SyncTransport

if TYPE_CHECKING:
    from types import TracebackType

    import httpx

    from bling_erp_api.auth import AccessTokenProvider


class BlingClient:
    """Synchronous client for the Bling API."""

    def __init__(  # noqa: PLR0913
        self,
        *,
        token_provider: AccessTokenProvider | None = None,
        auth: httpx.Auth | None = None,
        base_url: str = DEFAULT_API_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
        http_client: httpx.Client | None = None,
        rate_limit_max_requests: int | None = DEFAULT_RATE_LIMIT_MAX_REQUESTS,
        rate_limit_period_seconds: float = DEFAULT_RATE_LIMIT_PERIOD_SECONDS,
        rate_limit_max_retries: int = DEFAULT_RATE_LIMIT_MAX_RETRIES,
    ) -> None:
        """Create a client and attach resource namespaces."""
        resolved_auth = auth or _auth_from_token_provider(token_provider)
        self._transport = SyncTransport(
            auth=resolved_auth,
            base_url=base_url,
            timeout=timeout,
            client=http_client,
            rate_limit_max_requests=rate_limit_max_requests,
            rate_limit_period_seconds=rate_limit_period_seconds,
            rate_limit_max_retries=rate_limit_max_retries,
        )

        self._contacts = ContactsResource(self._transport)
        self._products = ProductsResource(self._transport)
        self._produtos_estruturas = ProductStructuresResource(self._transport)
        self._produtos_fornecedores = ProductSuppliersResource(self._transport)
        self._produtos_lojas = ProductStoresResource(self._transport)
        self._lotes = ProductBatchesResource(self._transport)
        self._lotes_lancamentos = ProductBatchEntriesResource(self._transport)
        self._produtos_variacoes = ProductVariationsResource(self._transport)
        self._sales_orders = SalesOrdersResource(self._transport)
        self._nfe = NfeResource(self._transport)
        self._nfce = NfceResource(self._transport)
        self._nfse = NfseResource(self._transport)
        self._anuncios = AdsResource(self._transport)
        self._anuncios_categorias = AdCategoriesResource(self._transport)
        self._caixas_bancos = CaixasBancosResource(self._transport)
        self._borderos = BorderosResource(self._transport)

    # -- Resource namespace properties (with IDE-visible docstrings) --

    @property
    def contacts(self) -> ContactsResource:
        """Operações de contatos (/contatos)."""
        return self._contacts

    @property
    def contatos(self) -> ContactsResource:
        """Alias pt-BR para ``contacts``. Operações em ``/contatos``."""
        return self._contacts

    @property
    def products(self) -> ProductsResource:
        """Operações de produtos (/produtos). Bling API v3."""
        return self._products

    @property
    def produtos(self) -> ProductsResource:
        """Alias pt-BR para ``products``. Operações de produtos (/produtos)."""
        return self._products

    @property
    def produtos_estruturas(self) -> ProductStructuresResource:
        """Operações de estruturas de produtos (/produtos/estruturas)."""
        return self._produtos_estruturas

    @property
    def product_structures(self) -> ProductStructuresResource:
        """Alias em inglês para ``produtos_estruturas``. Product structures (/produtos/estruturas)."""
        return self._produtos_estruturas

    @property
    def produtos_fornecedores(self) -> ProductSuppliersResource:
        """Operações de fornecedores de produtos (/produtos/fornecedores)."""
        return self._produtos_fornecedores

    @property
    def product_suppliers(self) -> ProductSuppliersResource:
        """Alias em inglês para ``produtos_fornecedores``. Product suppliers (/produtos/fornecedores)."""
        return self._produtos_fornecedores

    @property
    def produtos_lojas(self) -> ProductStoresResource:
        """Operações de lojas de produtos (/produtos/lojas)."""
        return self._produtos_lojas

    @property
    def product_stores(self) -> ProductStoresResource:
        """Alias em inglês para ``produtos_lojas``. Product stores (/produtos/lojas)."""
        return self._produtos_lojas

    @property
    def lotes(self) -> ProductBatchesResource:
        """Operações de lotes de produtos (/produtos/lotes)."""
        return self._lotes

    @property
    def product_batches(self) -> ProductBatchesResource:
        """Alias em inglês para ``lotes``. Product batches (/produtos/lotes)."""
        return self._lotes

    @property
    def lotes_lancamentos(self) -> ProductBatchEntriesResource:
        """Operações de lançamentos de lotes (/produtos/lotes/lancamentos)."""
        return self._lotes_lancamentos

    @property
    def product_batch_entries(self) -> ProductBatchEntriesResource:
        """Alias em inglês para ``lotes_lancamentos``. Product batch entries (/produtos/lotes/lancamentos)."""
        return self._lotes_lancamentos

    @property
    def produtos_variacoes(self) -> ProductVariationsResource:
        """Operações de variações de produtos (/produtos/variacoes)."""
        return self._produtos_variacoes

    @property
    def product_variations(self) -> ProductVariationsResource:
        """Alias em inglês para ``produtos_variacoes``. Product variations (/produtos/variacoes)."""
        return self._produtos_variacoes

    @property
    def sales_orders(self) -> SalesOrdersResource:
        """Operações de pedidos de venda (/pedidos/vendas). Bling API v3."""
        return self._sales_orders

    @property
    def pedidos_vendas(self) -> SalesOrdersResource:
        """Alias pt-BR para ``sales_orders``. Operações de pedidos de venda (/pedidos/vendas)."""
        return self._sales_orders

    @property
    def notas_fiscais(self) -> NfeResource:
        """Operações de notas fiscais eletrônicas (/nfe)."""
        return self._nfe

    @property
    def invoices(self) -> NfeResource:
        """Alias em inglês para ``notas_fiscais``. NF-e (/nfe)."""
        return self._nfe

    @property
    def notas_fiscais_consumidor(self) -> NfceResource:
        """Operações de notas fiscais do consumidor (/nfce)."""
        return self._nfce

    @property
    def consumer_invoices(self) -> NfceResource:
        """Alias em inglês para ``notas_fiscais_consumidor``. NFC-e (/nfce)."""
        return self._nfce

    @property
    def notas_servicos(self) -> NfseResource:
        """Operações de notas fiscais de serviço (/nfse)."""
        return self._nfse

    @property
    def service_invoices(self) -> NfseResource:
        """Alias em inglês para ``notas_servicos``. NFS-e (/nfse)."""
        return self._nfse

    @property
    def anuncios(self) -> AdsResource:
        """Anúncios (Ads) — operações em ``/anuncios``."""
        return self._anuncios

    @property
    def ads(self) -> AdsResource:
        """Alias for ``anuncios``. Ads operations on ``/anuncios``."""
        return self.anuncios

    @property
    def anuncios_categorias(self) -> AdCategoriesResource:
        """Categorias de anúncios — operações em ``/anuncios/categorias``."""
        return self._anuncios_categorias

    @property
    def ad_categories(self) -> AdCategoriesResource:
        """Alias for ``anuncios_categorias``. Ad category operations on ``/anuncios/categorias``."""
        return self.anuncios_categorias

    @property
    def caixas_bancos(self) -> CaixasBancosResource:
        """Lançamentos de caixas e bancos — operações em ``/caixas``."""
        return self._caixas_bancos

    @property
    def cash_entries(self) -> CaixasBancosResource:
        """Alias for ``caixas_bancos``. Cash/bank entry operations on ``/caixas``."""
        return self.caixas_bancos

    @property
    def borderos(self) -> BorderosResource:
        """Borderôs — operações em ``/borderos``."""
        return self._borderos

    @classmethod
    def from_env(  # noqa: PLR0913
        cls,
        *,
        base_url: str = DEFAULT_API_BASE_URL,
        timeout: float = DEFAULT_TIMEOUT_SECONDS,
        http_client: httpx.Client | None = None,
        rate_limit_max_requests: int | None = DEFAULT_RATE_LIMIT_MAX_REQUESTS,
        rate_limit_period_seconds: float = DEFAULT_RATE_LIMIT_PERIOD_SECONDS,
        rate_limit_max_retries: int = DEFAULT_RATE_LIMIT_MAX_RETRIES,
    ) -> Self:
        """Create a client using ``BLING_*`` settings from ``bling-jwt-auth``."""
        return cls(
            auth=BlingAuthAdapter.from_env(),
            base_url=base_url,
            timeout=timeout,
            http_client=http_client,
            rate_limit_max_requests=rate_limit_max_requests,
            rate_limit_period_seconds=rate_limit_period_seconds,
            rate_limit_max_retries=rate_limit_max_retries,
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
