# Paginação

## Parâmetros page e limit

Endpoints de listagem aceitam os parâmetros `page` e `limit` para controlar
a paginação:

```python
from bling_erp_api import BlingClient

with BlingClient.from_env() as client:
    # Página 1, 20 itens por página (padrão)
    response = client.produtos.listar(page=1, limit=20)

    # Página 3, 50 itens por página
    response = client.produtos.listar(page=3, limit=50)
```

## Autopaginação com iterar() / iterate()

Para percorrer todos os resultados sem gerenciar páginas manualmente, use
o método `iterar()` (pt-BR) ou `iterate()` (EN):

```python
with BlingClient.from_env() as client:
    # Itera sobre todas as páginas
    for produto in client.produtos.iterar(limit=100):
        print(produto.get("id"), produto.get("nome"))
```

Você também pode passar filtros:

```python
for produto in client.produtos.iterar(
    situacao="A",
    limit=50,
):
    print(produto.get("nome"))
```

A autopaginação é implementada nos seguintes recursos:

| Recurso | Método pt-BR | Método EN |
|---|---|---|
| Produtos | `produtos.iterar()` | `products.iterate()` |
| Pedidos de Venda | `pedidos_vendas.iterar()` | `sales_orders.iterate()` |
| Pedidos de Compra | `pedidos_compras.iterar()` | `purchase_orders.iterate()` |
| Contatos | `contatos.iterar()` | `contacts.iterate()` |
| Anúncios | `anuncios.iterar()` | `ads.iterate()` |
| Propostas Comerciais | `propostas_comerciais.iterar()` | `commercial_proposals.iterate()` |

## next_page_payload Helper

Para recursos que não possuem autopaginação nativa, você pode usar o helper
`next_page_payload` do transport para paginar manualmente:

```python
from bling_erp_api import BlingClient

with BlingClient.from_env() as client:
    page = 1
    limit = 100
    all_items = []

    while True:
        response = client.contatos.listar(page=page, limit=limit)
        data = response.get("data", [])
        if not data:
            break
        all_items.extend(data)
        page += 1
```

## Comportamento

- O valor padrão de `page` é `1`
- O valor padrão de `limit` varia por recurso (geralmente 100)
- O limite máximo de `limit` depende da API do Bling (geralmente 100 ou 200)
- A API retorna `data` como uma lista de objetos na resposta bem-sucedida
- Quando não há mais páginas, a lista `data` vem vazia
