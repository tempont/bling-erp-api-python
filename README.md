# Bling ERP API SDK

[![PyPI version](https://img.shields.io/pypi/v/bling-erp-api.svg)](https://pypi.org/project/bling-erp-api/)
[![Python versions](https://img.shields.io/pypi/pyversions/bling-erp-api.svg)](https://pypi.org/project/bling-erp-api/)
[![License: MIT](https://img.shields.io/pypi/l/bling-erp-api.svg)](https://github.com/tempont/bling-erp-api-python/blob/main/LICENSE)
[![CI](https://github.com/tempont/bling-erp-api-python/actions/workflows/ci.yml/badge.svg)](https://github.com/tempont/bling-erp-api-python/actions/workflows/ci.yml)
[![Downloads](https://img.shields.io/pypi/dm/bling-erp-api.svg)](https://pypi.org/project/bling-erp-api/)
[![Code style: Ruff](https://img.shields.io/badge/code%20style-Ruff-261230.svg)](https://github.com/astral-sh/ruff)
[![Type checker: basedpyright](https://img.shields.io/badge/type%20checker-basedpyright-blue.svg)](https://github.com/detachhead/basedpyright)

[Português (BR)](README.pt-BR.md) | **English**

Unofficial Python SDK for the [Bling ERP API v3](https://lerosa.atlassian.net/wiki/spaces/JSON/pages/25362471/API+v3).

Provides typed, idiomatic access to 40+ Bling ERP resources with sync/async
transports, OAuth2 authentication, rate limiting, and automatic retry.

## Installation

```bash
pip install bling-erp-api
```

Or with `uv`:

```bash
uv add bling-erp-api
```

Python 3.12+ required.

## Quick Start

Set the required environment variables (see [Authentication](#authentication)):

```bash
export BLING_CLIENT_ID="your_client_id"
export BLING_CLIENT_SECRET="your_client_secret"
export BLING_REFRESH_TOKEN="your_refresh_token"
```

Then use the SDK:

```python
from bling_erp_api import BlingClient

with BlingClient.from_env() as client:
    # List products
    products = client.produtos.listar(limit=10)
    for product in products.get("data", []):
        print(product.get("nome"))

    # Get a contact
    contact = client.contatos.obter(1)
    print(contact)
```

## Features

- **40+ resource modules** covering the full Bling ERP API surface
- **OAuth2 authentication** via `bling-jwt-auth` — automatic token refresh
- **Rate limiting** (3 req/s default) with 429 retry and `Retry-After` support
- **Typed models** with Pydantic v2 — snake_case fields, automatic Bling name mapping
- **Sync and async** transports
- **pt-BR canonical API** with English compatibility aliases
- **OpenAPI contract validation** — generated and tested against the spec
- **500+ tests** with mocked HTTP

## Resources

| pt-BR Namespace | EN Alias | Description |
|---|---|---|
| `client.contatos` | `client.contacts` | Contacts CRUD and status management |
| `client.produtos` | `client.products` | Products CRUD and status |
| `client.produtos_estruturas` | `client.product_structures` | Product structures (BOM) |
| `client.produtos_fornecedores` | `client.product_suppliers` | Product suppliers |
| `client.produtos_lojas` | `client.product_stores` | Product store mappings |
| `client.lotes` | `client.product_batches` | Product batches |
| `client.lotes_lancamentos` | `client.product_batch_entries` | Batch entries |
| `client.produtos_variacoes` | `client.product_variations` | Product variations |
| `client.pedidos_vendas` | `client.sales_orders` | Sales orders |
| `client.pedidos_compras` | `client.purchase_orders` | Purchase orders |
| `client.notas_fiscais` | `client.invoices` | NF-e (electronic invoices) |
| `client.notas_fiscais_consumidor` | `client.consumer_invoices` | NFC-e (consumer invoices) |
| `client.notas_servicos` | `client.service_invoices` | NFS-e (service invoices) |
| `client.anuncios` | `client.ads` | Marketplace ads |
| `client.anuncios_categorias` | `client.ad_categories` | Ad categories |
| `client.caixas_bancos` | `client.cash_entries` | Cash and bank entries |
| `client.borderos` | `client.payment_bundles` | Bordero management |
| `client.categorias_lojas` | `client.store_categories` | Store categories |
| `client.categorias_produtos` | `client.product_categories` | Product categories |
| `client.categorias_receitas_despesas` | `client.income_expense_categories` | Income/expense categories |
| `client.contas_pagar` | `client.accounts_payable` | Accounts payable |
| `client.contas_receber` | `client.accounts_receivable` | Accounts receivable |
| `client.contas_contabeis` | `client.financial_accounts` | Financial/chart of accounts |
| `client.depositos` | `client.warehouses` | Warehouses |
| `client.empresas` | `client.companies` | Company data |
| `client.estoques` | `client.stock` | Stock balances |
| `client.formas_pagamentos` | `client.payment_methods` | Payment methods |
| `client.grupos_produtos` | `client.product_groups` | Product groups |
| `client.homologacao` | `client.homologation` | Test/homologation |
| `client.logisticas` | `client.logistics` | Logistics providers |
| `client.logisticas_servicos` | `client.logistics_services` | Logistics services |
| `client.logisticas_objetos` | `client.logistics_objects` | Logistics objects |
| `client.logisticas_etiquetas` | `client.logistics_labels` | Shipping labels |
| `client.logisticas_remessas` | `client.logistics_shipments` | Logistics shipments |
| `client.naturezas_operacoes` | `client.natures_of_operations` | Tax natures |
| `client.notificacoes` | `client.notifications` | Notifications |
| `client.ordens_producao` | `client.production_orders` | Production orders |
| `client.propostas_comerciais` | `client.commercial_proposals` | Commercial proposals |
| `client.situacoes` | `client.situations` | Status/situations |
| `client.situacoes_modulos` | `client.situation_modules` | Situation modules |
| `client.situacoes_transicoes` | `client.situation_transitions` | Situation transitions |
| `client.vendedores` | `client.sellers` | Sellers |
| `client.usuarios` | `client.users` | User management |

## Authentication

The SDK uses OAuth2 (authorization code flow) delegated to the
[`bling-jwt-auth`](https://pypi.org/project/bling-jwt-auth/) package.

The simplest way to get started is with environment variables:

```bash
export BLING_CLIENT_ID="your_client_id"
export BLING_CLIENT_SECRET="your_client_secret"
export BLING_REFRESH_TOKEN="your_refresh_token"
export BLING_REDIRECT_URI="your_redirect_uri"  # optional
```

Then create a client with `BlingClient.from_env()`.

For custom authentication, pass a `token_provider` implementing
`get_access_token() -> str` or an `httpx.Auth` instance.

See the [Authentication documentation](https://tempont.github.io/bling-erp-api-python/authentication/)
for details.

## Documentation

Full documentation is available at:

**https://tempont.github.io/bling-erp-api-python/**

- [Getting Started](https://tempont.github.io/bling-erp-api-python/getting-started/)
- [Authentication](https://tempont.github.io/bling-erp-api-python/authentication/)
- [Pagination](https://tempont.github.io/bling-erp-api-python/pagination/)
- [Error Handling](https://tempont.github.io/bling-erp-api-python/errors/)
- [API Reference](https://tempont.github.io/bling-erp-api-python/api-reference/)

## Contributing

Contributions are welcome! See the full guide in [`CONTRIBUTING.md`](CONTRIBUTING.md).

### Quick start

```bash
git clone https://github.com/tempont/bling-erp-api-python.git
cd bling-erp-api-python
uv sync --all-groups
make check
```

### Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/my-feature`)
3. Make your changes
4. Verify with `make check` (runs ruff, basedpyright, and pytest)
5. Commit with a clear message, push, and open a Pull Request

For detailed conventions on naming, docstrings, models, and resource implementation,
see the [`AGENTS.md`](AGENTS.md) file in the repository root.

## Reporting Issues

Found a bug? Use the [GitHub issue tracker](https://github.com/tempont/bling-erp-api-python/issues).

When reporting, please include:

- Python version (`python --version`)
- SDK version (`bling-erp-api --version`)
- Minimal reproduction code
- Expected vs. actual behavior

For security issues, please report privately through GitHub's security channels.

## License

MIT — see [LICENSE](LICENSE).
