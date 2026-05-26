"""Resource namespaces exposed by the SDK client."""

from bling_erp_api.resources.ad_categories import AdCategoriesResource
from bling_erp_api.resources.ads import AdsResource
from bling_erp_api.resources.borderos import BorderosResource
from bling_erp_api.resources.caixas_bancos import CaixasBancosResource
from bling_erp_api.resources.contacts import ContactsResource
from bling_erp_api.resources.income_expense_categories import (
    IncomeExpenseCategoriesResource,
)
from bling_erp_api.resources.nfce import NfceResource
from bling_erp_api.resources.nfe import NfeResource
from bling_erp_api.resources.nfse import NfseResource
from bling_erp_api.resources.product_batch_entries import ProductBatchEntriesResource
from bling_erp_api.resources.product_batches import ProductBatchesResource
from bling_erp_api.resources.product_categories import ProductCategoriesResource
from bling_erp_api.resources.product_stores import ProductStoresResource
from bling_erp_api.resources.product_structures import ProductStructuresResource
from bling_erp_api.resources.product_suppliers import ProductSuppliersResource
from bling_erp_api.resources.product_variations import ProductVariationsResource
from bling_erp_api.resources.products import ProductsResource
from bling_erp_api.resources.sales_orders import SalesOrdersResource
from bling_erp_api.resources.store_categories import StoreCategoriesResource

__all__ = [
    "AdCategoriesResource",
    "AdsResource",
    "BorderosResource",
    "CaixasBancosResource",
    "ContactsResource",
    "IncomeExpenseCategoriesResource",
    "NfceResource",
    "NfeResource",
    "NfseResource",
    "ProductBatchEntriesResource",
    "ProductBatchesResource",
    "ProductCategoriesResource",
    "ProductStoresResource",
    "ProductStructuresResource",
    "ProductSuppliersResource",
    "ProductVariationsResource",
    "ProductsResource",
    "SalesOrdersResource",
    "StoreCategoriesResource",
]
