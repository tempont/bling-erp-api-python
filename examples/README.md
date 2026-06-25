# Examples

This directory contains runnable examples for the Bling ERP API SDK.

Each subdirectory corresponds to a resource namespace. Examples use
`BlingClient.from_env()` and require the `BLING_*` environment variables
to be set (see the [Authentication docs](https://tempont.github.io/bling-erp-api-python/authentication/)).

## Resource Examples

| Example Directory | Resource | Description |
|---|---|---|
| `ads/` | Anúncios / Ads | Create, get, list, pause, publish ads |
| `borderos/` | Borderôs | Get and delete borderos |
| `caixas_bancos/` | Caixas e Bancos | Create, get, list cash/bank entries |
| `categorias loja/` | Categorias de Loja | Get and list store categories |
| `contas_contabeis/` | Contas Contábeis | Get and list financial accounts |
| `contas_pagar/` | Contas a Pagar | Get and list accounts payable |
| `contas_receber/` | Contas a Receber | Get and list accounts receivable |
| `contatos/` | Contatos | CRUD operations for contacts |
| `depositos/` | Depósitos | Get, list, and manage warehouses/deposits |
| `empresas/` | Empresas | Get company data |
| `estoques/` | Estoques | Get stock balances by deposit |
| `homologacao/` | Homologação | Create and get test products |
| `logisticas/` | Logísticas | Get and list logistics providers |
| `logisticas_etiquetas/` | Logísticas - Etiquetas | Get shipping labels |
| `logisticas_objetos/` | Logísticas - Objetos | Get tracking objects |
| `logisticas_remessas/` | Logísticas - Remessas | Get shipments |
| `logisticas_servicos/` | Logísticas - Serviços | List logistics services |
| `métodos_pagamento/` | Formas de Pagamento | Payment method operations |
| `naturezas_operacoes/` | Naturezas de Operações | List tax natures and get taxation |
| `notas_fiscais/` | Notas Fiscais | NF-e, NFC-e, and NFS-e examples |
| `notificacoes/` | Notificações | List notifications and get counts |
| `ordens_producao/` | Ordens de Produção | CRUD and generate on demand |
| `pedidos_compra/` | Pedidos de Compra | Purchase order operations |
| `pedidos_venda/` | Pedidos de Venda | Sales order operations |
| `produtos/` | Produtos | Product CRUD and status management |
| `produtos_categorias/` | Categorias de Produtos | Get and list product categories |
| `propostas_comerciais/` | Propostas Comerciais | Commercial proposal operations |
| `receitas_e_despesas/` | Receitas e Despesas | Create, get, list income/expense categories |
| `situacoes/` | Situações | Status, modules, and transitions |
| `usuarios/` | Usuários | User password recovery and management |
| `vendedores/` | Vendedores | List and get sellers |
