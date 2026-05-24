# bling-erp-api

Unofficial Python SDK for the Bling ERP API v3.

The project is intentionally structured around:

- a `src/` package layout;
- a hand-written HTTP/resource layer;
- authentication delegated to `bling-jwt-auth`;
- generated or semi-generated models under `src/bling_erp_api/models/generated/`;
- resource modules that can grow endpoint by endpoint.

## Quick Start

```python
from bling_erp_api import BlingClient

with BlingClient.from_env() as client:
    products = client.products.list(limit=10)
```

## Project Layout

```text
src/bling_erp_api/
├── client.py
├── auth/
├── transport/
├── resources/
├── models/
└── utils/
```

## Authentication

Authentication is handled by `bling-jwt-auth`. The SDK only needs a token
provider with a `get_access_token()` method, or it can build one from `BLING_*`
environment variables with `BlingClient.from_env()`.
