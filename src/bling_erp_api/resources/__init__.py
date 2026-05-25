"""Resource namespaces exposed by the SDK client."""

from bling_erp_api.resources.contacts import ContactsResource
from bling_erp_api.resources.invoices import InvoicesResource
from bling_erp_api.resources.product_batch_entries import ProductBatchEntriesResource
from bling_erp_api.resources.product_batches import ProductBatchesResource
from bling_erp_api.resources.product_stores import ProductStoresResource
from bling_erp_api.resources.product_structures import ProductStructuresResource
from bling_erp_api.resources.product_suppliers import ProductSuppliersResource
from bling_erp_api.resources.product_variations import ProductVariationsResource
from bling_erp_api.resources.products import ProductsResource
from bling_erp_api.resources.sales_orders import SalesOrdersResource

__all__ = [
    "ContactsResource",
    "InvoicesResource",
    "ProductBatchEntriesResource",
    "ProductBatchesResource",
    "ProductStoresResource",
    "ProductStructuresResource",
    "ProductSuppliersResource",
    "ProductVariationsResource",
    "ProductsResource",
    "SalesOrdersResource",
]
