"""Resource namespaces exposed by the SDK client."""

from bling_erp_api.resources.contacts import ContactsResource
from bling_erp_api.resources.invoices import InvoicesResource
from bling_erp_api.resources.products import ProductsResource
from bling_erp_api.resources.sales_orders import SalesOrdersResource

__all__ = [
    "ContactsResource",
    "InvoicesResource",
    "ProductsResource",
    "SalesOrdersResource",
]
