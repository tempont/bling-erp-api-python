# Getting Started

```python
from bling_erp_api import BlingClient

with BlingClient.from_env() as client:
    products = client.products.list(limit=10)
```
