"""Model aliases for public SDK compatibility."""

from bling_erp_api.models.generated.contacts import Contact
from bling_erp_api.models.generated.products import (
    Product,
    ProductCreateRequest,
    ProductListResponse,
    ProductMutationResponse,
    ProductPatchRequest,
    ProductResponse,
    ProductUpdateRequest,
)
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
    "ProductCreateRequest",
    "ProductListResponse",
    "ProductMutationResponse",
    "ProductPatchRequest",
    "ProductResponse",
    "ProductUpdateRequest",
    "SalesOrder",
    "SalesOrderCreateRequest",
    "SalesOrderInvoiceResponse",
    "SalesOrderListResponse",
    "SalesOrderMutationResponse",
    "SalesOrderResponse",
    "SalesOrderUpdateRequest",
]
