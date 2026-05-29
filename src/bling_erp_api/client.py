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
    CommercialProposalsResource,
    ContactsResource,
    ContasContabeisResource,
    ContasPagarResource,
    ContasReceberResource,
    DepositosResource,
    EmpresasResource,
    EstoquesResource,
    HomologationResource,
    IncomeExpenseCategoriesResource,
    LogisticasEtiquetasResource,
    LogisticasObjetosResource,
    LogisticasRemessasResource,
    LogisticasResource,
    LogisticasServicosResource,
    NaturezasOperacoesResource,
    NfceResource,
    NfeResource,
    NfseResource,
    NotificacoesResource,
    OrdensProducaoResource,
    PaymentMethodsResource,
    ProductBatchEntriesResource,
    ProductBatchesResource,
    ProductCategoriesResource,
    ProductGroupsResource,
    ProductsResource,
    ProductStoresResource,
    ProductStructuresResource,
    ProductSuppliersResource,
    ProductVariationsResource,
    PurchaseOrdersResource,
    SalesOrdersResource,
    StoreCategoriesResource,
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
        self._purchase_orders = PurchaseOrdersResource(self._transport)
        self._nfe = NfeResource(self._transport)
        self._nfce = NfceResource(self._transport)
        self._nfse = NfseResource(self._transport)
        self._anuncios = AdsResource(self._transport)
        self._anuncios_categorias = AdCategoriesResource(self._transport)
        self._caixas_bancos = CaixasBancosResource(self._transport)
        self._borderos = BorderosResource(self._transport)
        self._store_categories = StoreCategoriesResource(self._transport)
        self._product_categories = ProductCategoriesResource(self._transport)
        self._income_expense_categories = IncomeExpenseCategoriesResource(self._transport)

        self._contas_pagar = ContasPagarResource(self._transport)
        self._contas_receber = ContasReceberResource(self._transport)
        self._contas_contabeis = ContasContabeisResource(self._transport)

        self._depositos = DepositosResource(self._transport)
        self._empresas = EmpresasResource(self._transport)
        self._estoques = EstoquesResource(self._transport)

        self._payment_methods = PaymentMethodsResource(self._transport)
        self._product_groups = ProductGroupsResource(self._transport)
        self._homologation = HomologationResource(self._transport)

        self._logisticas = LogisticasResource(self._transport)
        self._logisticas_servicos = LogisticasServicosResource(self._transport)
        self._logisticas_objetos = LogisticasObjetosResource(self._transport)
        self._logisticas_etiquetas = LogisticasEtiquetasResource(self._transport)
        self._logisticas_remessas = LogisticasRemessasResource(self._transport)
        self._naturezas_operacoes = NaturezasOperacoesResource(self._transport)

        self._notificacoes = NotificacoesResource(self._transport)
        self._ordens_producao = OrdensProducaoResource(self._transport)

        self._commercial_proposals = CommercialProposalsResource(self._transport)

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
    def pedidos_compras(self) -> PurchaseOrdersResource:
        """Pedidos de compra — operações em ``/pedidos/compras``."""
        return self._purchase_orders

    @property
    def purchase_orders(self) -> PurchaseOrdersResource:
        """Alias for ``pedidos_compras``. Purchase order operations on ``/pedidos/compras``."""
        return self._purchase_orders

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

    @property
    def categorias_lojas(self) -> StoreCategoriesResource:
        """Categorias de lojas — operações em ``/categorias/lojas``."""
        return self._store_categories

    @property
    def store_categories(self) -> StoreCategoriesResource:
        """Alias for ``categorias_lojas``. Store category operations on ``/categorias/lojas``."""
        return self.categorias_lojas

    @property
    def categorias_produtos(self) -> ProductCategoriesResource:
        """Categorias de produtos — operações em ``/categorias/produtos``."""
        return self._product_categories

    @property
    def product_categories(self) -> ProductCategoriesResource:
        """Alias for ``categorias_produtos``. Product category operations on ``/categorias/produtos``."""
        return self.categorias_produtos

    @property
    def categorias_receitas_despesas(self) -> IncomeExpenseCategoriesResource:
        """Categorias de receitas e despesas — operações em ``/categorias/receitas-despesas``."""
        return self._income_expense_categories

    @property
    def income_expense_categories(self) -> IncomeExpenseCategoriesResource:
        """Alias for ``categorias_receitas_despesas``. Income/expense category operations on ``/categorias/receitas-despesas``."""
        return self.categorias_receitas_despesas

    @property
    def contas_pagar(self) -> ContasPagarResource:
        """Contas a pagar — operações em ``/contas/pagar``."""
        return self._contas_pagar

    @property
    def accounts_payable(self) -> ContasPagarResource:
        """Alias for ``contas_pagar``. Accounts payable operations on ``/contas/pagar``."""
        return self.contas_pagar

    @property
    def contas_receber(self) -> ContasReceberResource:
        """Contas a receber — operações em ``/contas/receber``."""
        return self._contas_receber

    @property
    def accounts_receivable(self) -> ContasReceberResource:
        """Alias for ``contas_receber``. Accounts receivable operations on ``/contas/receber``."""
        return self.contas_receber

    @property
    def contas_contabeis(self) -> ContasContabeisResource:
        """Contas financeiras — operações em ``/contas-contabeis``."""
        return self._contas_contabeis

    @property
    def financial_accounts(self) -> ContasContabeisResource:
        """Alias for ``contas_contabeis``. Financial accounts operations on ``/contas-contabeis``."""
        return self.contas_contabeis

    @property
    def depositos(self) -> DepositosResource:
        """Depósitos — operações em ``/depositos``."""
        return self._depositos

    @property
    def warehouses(self) -> DepositosResource:
        """Alias for ``depositos``. Warehouse operations on ``/depositos``."""
        return self.depositos

    @property
    def empresas(self) -> EmpresasResource:
        """Empresas — operações em ``/empresas``."""
        return self._empresas

    @property
    def companies(self) -> EmpresasResource:
        """Alias for ``empresas``. Company operations on ``/empresas``."""
        return self.empresas

    @property
    def estoques(self) -> EstoquesResource:
        """Estoques — operações em ``/estoques``."""
        return self._estoques

    @property
    def stock(self) -> EstoquesResource:
        """Alias for ``estoques``. Stock operations on ``/estoques``."""
        return self.estoques

    @property
    def formas_pagamentos(self) -> PaymentMethodsResource:
        """Formas de pagamentos — operações em ``/formas-pagamentos``."""
        return self._payment_methods

    @property
    def payment_methods(self) -> PaymentMethodsResource:
        """Alias for ``formas_pagamentos``. Payment method operations on ``/formas-pagamentos``."""
        return self.formas_pagamentos

    @property
    def grupos_produtos(self) -> ProductGroupsResource:
        """Grupos de produtos — operações em ``/grupos-produtos``."""
        return self._product_groups

    @property
    def product_groups(self) -> ProductGroupsResource:
        """Alias for ``grupos_produtos``. Product group operations on ``/grupos-produtos``."""
        return self.grupos_produtos

    @property
    def homologacao(self) -> HomologationResource:
        """Homologação — operações em ``/homologacao/produtos``."""
        return self._homologation

    @property
    def homologation(self) -> HomologationResource:
        """Alias for ``homologacao``. Homologation operations on ``/homologacao/produtos``."""
        return self.homologacao

    @property
    def logisticas(self) -> LogisticasResource:
        """Logísticas — operações em ``/logisticas``."""
        return self._logisticas

    @property
    def logistics(self) -> LogisticasResource:
        """Alias for ``logisticas``. Logistics operations on ``/logisticas``."""
        return self.logisticas

    @property
    def logisticas_servicos(self) -> LogisticasServicosResource:
        """Serviços de logísticas — operações em ``/logisticas/servicos``."""
        return self._logisticas_servicos

    @property
    def logistics_services(self) -> LogisticasServicosResource:
        """Alias for ``logisticas_servicos``. Logistics service operations on ``/logisticas/servicos``."""
        return self.logisticas_servicos

    @property
    def logisticas_objetos(self) -> LogisticasObjetosResource:
        """Objetos de logísticas — operações em ``/logisticas/objetos``."""
        return self._logisticas_objetos

    @property
    def logistics_objects(self) -> LogisticasObjetosResource:
        """Alias for ``logisticas_objetos``. Logistics object operations on ``/logisticas/objetos``."""
        return self.logisticas_objetos

    @property
    def logisticas_etiquetas(self) -> LogisticasEtiquetasResource:
        """Etiquetas de logísticas — operações em ``/logisticas/etiquetas``."""
        return self._logisticas_etiquetas

    @property
    def logistics_labels(self) -> LogisticasEtiquetasResource:
        """Alias for ``logisticas_etiquetas``. Logistics label operations on ``/logisticas/etiquetas``."""
        return self.logisticas_etiquetas

    @property
    def logisticas_remessas(self) -> LogisticasRemessasResource:
        """Remessas de logísticas — operações em ``/logisticas/remessas``."""
        return self._logisticas_remessas

    @property
    def logistics_shipments(self) -> LogisticasRemessasResource:
        """Alias for ``logisticas_remessas``. Logistics shipment operations on ``/logisticas/remessas``."""
        return self.logisticas_remessas

    @property
    def notificacoes(self) -> NotificacoesResource:
        """Notificações (pt-BR)."""
        return self._notificacoes

    @property
    def notifications(self) -> NotificacoesResource:
        """Notificações (EN alias)."""
        return self._notificacoes

    @property
    def ordens_producao(self) -> OrdensProducaoResource:
        """Ordens de Produção (pt-BR)."""
        return self._ordens_producao

    @property
    def production_orders(self) -> OrdensProducaoResource:
        """Ordens de Produção (EN alias)."""
        return self._ordens_producao

    @property
    def naturezas_operacoes(self) -> NaturezasOperacoesResource:
        """Naturezas de Operações (pt-BR)."""
        return self._naturezas_operacoes

    @property
    def tax_natures(self) -> NaturezasOperacoesResource:
        """Naturezas de Operações (EN alias)."""
        return self._naturezas_operacoes

    @property
    def propostas_comerciais(self) -> CommercialProposalsResource:
        """Propostas Comerciais — operações em ``/propostas-comerciais``."""
        return self._commercial_proposals

    @property
    def commercial_proposals(self) -> CommercialProposalsResource:
        """Alias for ``propostas_comerciais``. Commercial proposals on ``/propostas-comerciais``."""
        return self._commercial_proposals

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
