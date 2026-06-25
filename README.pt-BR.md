# Bling ERP API SDK

[![PyPI version](https://img.shields.io/pypi/v/bling-erp-api.svg)](https://pypi.org/project/bling-erp-api/)
[![Python versions](https://img.shields.io/pypi/pyversions/bling-erp-api.svg)](https://pypi.org/project/bling-erp-api/)
[![License: MIT](https://img.shields.io/pypi/l/bling-erp-api.svg)](https://github.com/tempont/bling-erp-api-python/blob/main/LICENSE)
[![CI](https://github.com/tempont/bling-erp-api-python/actions/workflows/ci.yml/badge.svg)](https://github.com/tempont/bling-erp-api-python/actions/workflows/ci.yml)
[![Docs](https://github.com/tempont/bling-erp-api-python/actions/workflows/docs.yml/badge.svg)](https://tempont.github.io/bling-erp-api-python/)
[![Downloads](https://img.shields.io/pypi/dm/bling-erp-api.svg)](https://pypi.org/project/bling-erp-api/)
[![Code style: Ruff](https://img.shields.io/badge/code%20style-Ruff-261230.svg)](https://github.com/astral-sh/ruff)
[![Type checker: basedpyright](https://img.shields.io/badge/type%20checker-basedpyright-blue.svg)](https://github.com/detachhead/basedpyright)

**Português (BR)** | [English](README.md)

SDK Python não oficial para a [API v3 do Bling ERP](https://developer.bling.com.br/referencia).

Acesso tipado e idiomático a mais de 40 recursos do Bling ERP, com transporte síncrono e assíncrono,
autenticação OAuth2, limite de taxa, retry automático e modelos Pydantic.

## Descrição

O **Bling ERP API SDK** é uma biblioteca Python que simplifica a integração com a API v3 do Bling ERP.
Ela oferece uma interface canônica em português (com aliases em inglês para compatibilidade),
modelos tipados com Pydantic v2, validação de contratos OpenAPI, e tratamento robusto de erros
e rate limiting — tudo para que você possa focar no que importa: sua aplicação.

## Recursos

- **40+ módulos de recursos** cobrindo toda a superfície da API do Bling ERP
- **Autenticação OAuth2** via `bling-jwt-auth` — renovação automática de tokens
- **Rate limiting** (3 req/s padrão) com retry em respostas 429 e suporte a `Retry-After`
- **Modelos tipados** com Pydantic v2 — campos em snake_case e mapeamento automático para nomes Bling
- **Transporte síncrono e assíncrono** baseado em HTTPX
- **API canônica em pt-BR** com aliases em inglês para compatibilidade
- **Contratos OpenAPI** — gerados e testados contra a especificação oficial
- **500+ testes** com HTTP mockado
- **Documentação completa** em mkdocs com suporte a busca

## Instalação

```bash
pip install bling-erp-api
```

Ou com `uv`:

```bash
uv add bling-erp-api
```

Requer Python 3.12 ou superior.

## Início Rápido

Defina as variáveis de ambiente necessárias (veja [Autenticação](#autenticação)):

```bash
export BLING_CLIENT_ID="seu_client_id"
export BLING_CLIENT_SECRET="seu_client_secret"
export BLING_REFRESH_TOKEN="seu_refresh_token"
```

Depois use o SDK:

```python
from bling_erp_api import BlingClient

with BlingClient.from_env() as client:
    # Listar produtos da primeira página
    produtos = client.produtos.listar(limit=100)
    for produto in produtos.get("data", []):
        print(produto.get("nome"))

    # Obter um contato
    contato = client.contatos.obter(1)
    print(contato)

    # Criar um pedido de venda
    from bling_erp_api.models.aliases import PedidoVenda

    pedido = PedidoVenda(
        cliente=PedidoVenda.Cliente(nome="Cliente Exemplo"),
        itens=[
            PedidoVenda.Item(
                codigo="PROD-001",
                descricao="Produto Exemplo",
                quantidade=2,
                valor_unitario=49.90,
            )
        ],
    )
    resposta = client.pedidos_vendas.criar(pedido)
    print(resposta)
```

## Autenticação

O SDK utiliza OAuth2 (fluxo de autorização) delegado ao pacote
[`bling-jwt-auth`](https://pypi.org/project/bling-jwt-auth/).

A forma mais simples de começar é com variáveis de ambiente:

```bash
export BLING_CLIENT_ID="seu_client_id"
export BLING_CLIENT_SECRET="seu_client_secret"
export BLING_REFRESH_TOKEN="seu_refresh_token"
export BLING_REDIRECT_URI="sua_redirect_uri"  # opcional
```

Em seguida, crie um cliente com `BlingClient.from_env()`.

Para autenticação personalizada, passe um `token_provider` que implemente
`get_access_token() -> str` ou uma instância de `httpx.Auth`.

Consulte a [documentação de autenticação](https://tempont.github.io/bling-erp-api-python/authentication/)
para mais detalhes.

## Recursos Disponíveis

| Namespace pt-BR                       | Alias EN                           | Descrição                                    |
|---------------------------------------|------------------------------------|----------------------------------------------|
| `client.contatos`                     | `client.contacts`                  | CRUD de contatos e gerenciamento de situação |
| `client.produtos`                     | `client.products`                  | CRUD de produtos e gerenciamento de situação |
| `client.produtos_estruturas`          | `client.product_structures`        | Estruturas de produtos (BOM)                 |
| `client.produtos_fornecedores`        | `client.product_suppliers`         | Fornecedores de produtos                     |
| `client.produtos_lojas`               | `client.product_stores`            | Mapeamento de produtos por loja              |
| `client.lotes`                        | `client.product_batches`           | Lotes de produtos                            |
| `client.lotes_lancamentos`            | `client.product_batch_entries`     | Lançamentos de lotes                         |
| `client.produtos_variacoes`           | `client.product_variations`        | Variações de produtos                        |
| `client.pedidos_vendas`               | `client.sales_orders`              | Pedidos de venda                             |
| `client.pedidos_compras`              | `client.purchase_orders`           | Pedidos de compra                            |
| `client.notas_fiscais`                | `client.invoices`                  | NF-e (notas fiscais eletrônicas)             |
| `client.notas_fiscais_consumidor`     | `client.consumer_invoices`         | NFC-e (notas fiscais ao consumidor)          |
| `client.notas_servicos`               | `client.service_invoices`          | NFS-e (notas fiscais de serviços)            |
| `client.anuncios`                     | `client.ads`                       | Anúncios em marketplaces                     |
| `client.anuncios_categorias`          | `client.ad_categories`             | Categorias de anúncios                       |
| `client.caixas_bancos`                | `client.cash_entries`              | Movimentações de caixa e bancos              |
| `client.borderos`                     | `client.payment_bundles`           | Gerenciamento de borderôs                    |
| `client.categorias_lojas`             | `client.store_categories`          | Categorias de lojas                          |
| `client.categorias_produtos`          | `client.product_categories`        | Categorias de produtos                       |
| `client.categorias_receitas_despesas` | `client.income_expense_categories` | Categorias de receitas e despesas            |
| `client.contas_pagar`                 | `client.accounts_payable`          | Contas a pagar                               |
| `client.contas_receber`               | `client.accounts_receivable`       | Contas a receber                             |
| `client.contas_contabeis`             | `client.financial_accounts`        | Contas contábeis / plano de contas           |
| `client.depositos`                    | `client.warehouses`                | Depósitos                                    |
| `client.empresas`                     | `client.companies`                 | Dados da empresa                             |
| `client.estoques`                     | `client.stock`                     | Saldos de estoque                            |
| `client.formas_pagamentos`            | `client.payment_methods`           | Formas de pagamento                          |
| `client.grupos_produtos`              | `client.product_groups`            | Grupos de produtos                           |
| `client.homologacao`                  | `client.homologation`              | Testes / homologação                         |
| `client.logisticas`                   | `client.logistics`                 | Transportadoras / logísticas                 |
| `client.logisticas_servicos`          | `client.logistics_services`        | Serviços logísticos                          |
| `client.logisticas_objetos`           | `client.logistics_objects`         | Objetos logísticos                           |
| `client.logisticas_etiquetas`         | `client.logistics_labels`          | Etiquetas de envio                           |
| `client.logisticas_remessas`          | `client.logistics_shipments`       | Remessas logísticas                          |
| `client.naturezas_operacoes`          | `client.natures_of_operations`     | Naturezas de operações fiscais               |
| `client.notificacoes`                 | `client.notifications`             | Notificações                                 |
| `client.ordens_producao`              | `client.production_orders`         | Ordens de produção                           |
| `client.propostas_comerciais`         | `client.commercial_proposals`      | Propostas comerciais                         |
| `client.situacoes`                    | `client.situations`                | Situações / status                           |
| `client.situacoes_modulos`            | `client.situation_modules`         | Módulos de situações                         |
| `client.situacoes_transicoes`         | `client.situation_transitions`     | Transições de situações                      |
| `client.vendedores`                   | `client.sellers`                   | Vendedores                                   |
| `client.usuarios`                     | `client.users`                     | Gerenciamento de usuários                    |

## Documentação

A documentação completa está disponível em:

**https://tempont.github.io/bling-erp-api-python/**

- [Comece por aqui](https://tempont.github.io/bling-erp-api-python/getting-started/) — instalação e primeiro uso
- [Autenticação](https://tempont.github.io/bling-erp-api-python/authentication/) — configuração de credenciais OAuth2
- [Paginação](https://tempont.github.io/bling-erp-api-python/pagination/) — navegação por resultados paginados
- [Tratamento de erros](https://tempont.github.io/bling-erp-api-python/errors/) — exceções tipadas
- [Referência da API](https://tempont.github.io/bling-erp-api-python/api-reference/) — documentação completa de classes e métodos

## Contribuindo

Contribuições são bem-vindas! Consulte o guia completo em [`CONTRIBUTING.md`](CONTRIBUTING.md) — em inglês.

### Resumo rápido

1. Faça um fork do repositório
2. Crie um branch para sua feature (`git checkout -b feat/minha-feature`)
3. Instale as dependências: `uv sync --all-groups`
4. Faça suas alterações
5. Verifique com `make check` (executa ruff, basedpyright e pytest)
6. Commit e push, depois abra um Pull Request

Para convenções detalhadas de nomenclatura, docstrings, modelos e implementação,
veja o arquivo [`AGENTS.md`](AGENTS.md) na raiz do projeto.

## Reportando Problemas

Encontrou um bug? Use o [rastreador de issues do GitHub](https://github.com/tempont/bling-erp-api-python/issues).

Ao reportar, inclua:

- Versão do Python (`python --version`)
- Versão do SDK (`bling-erp-api --version`)
- Código mínimo para reproduzir o problema
- Comportamento esperado vs. observado

Problemas de segurança devem ser reportados em privado — entre em contato pelos
canais do GitHub.

## Licença

MIT — veja o arquivo [`LICENSE`](LICENSE).

## Roadmap

- Expansão da geração de modelos Pydantic a partir do OpenAPI spec
- Continuação dos slices verticais para mais recursos (contas, estoques, categorias, logística, anúncios)
- Mais exemplos e documentação interativa
