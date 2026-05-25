"""Model aliases for public SDK compatibility."""

from bling_erp_api.models.generated.contacts import Contact
from bling_erp_api.models.generated.products import Product
from bling_erp_api.models.generated.sales_orders import (
    SalesOrder,
    SalesOrderCreateRequest,
    SalesOrderInvoiceResponse,
    SalesOrderListResponse,
    SalesOrderMutationResponse,
    SalesOrderResponse,
    SalesOrderUpdateRequest,
)

__all__ = [
    "Contact",
    "Product",
    "SalesOrder",
    "SalesOrderCreateRequest",
    "SalesOrderInvoiceResponse",
    "SalesOrderListResponse",
    "SalesOrderMutationResponse",
    "SalesOrderResponse",
    "SalesOrderUpdateRequest",
]
