# Produtos - Estruturas

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
# Veja as operacoes geradas abaixo.
```

## Operações

### `remover_varios`

- Bling: `DELETE /produtos/estruturas`
- Ação oficial: `RemoverMultiplos`
- Resumo oficial: Remove a estrutura de múltiplos produtos

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `ids_produtos` | `idsProdutos[]` | `query` | sim |

- Schemas de response: 200: Error, 400: ErrorResponse

### `obter`

- Bling: `GET /produtos/estruturas/{idProdutoEstrutura}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém a estrutura de um produto com composição

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_produto_estrutura` | `idProdutoEstrutura` | `path` | sim |

- Schemas de response: 200: ProdutosEstruturaDTO, 404: ErrorResponse

### `alterar`

- Bling: `PUT /produtos/estruturas/{idProdutoEstrutura}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera a estrutura de um produto com composição

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_produto_estrutura` | `idProdutoEstrutura` | `path` | sim |

- Schemas de request: `ProdutosEstruturaDTO`
- Schemas de response: 400: ErrorResponse, 404: ErrorResponse

### `remover_componentes`

- Bling: `DELETE /produtos/estruturas/{idProdutoEstrutura}/componentes`
- Ação oficial: `RemoverComponenteMultiplos`
- Resumo oficial: Remove componentes específicos de um produto com composição

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_produto_estrutura` | `idProdutoEstrutura` | `path` | sim |
| `ids_componentes` | `idsComponentes[]` | `query` | sim |

- Schemas de response: 400: ErrorResponse, 404: ErrorResponse

### `vincular_componentes`

- Bling: `POST /produtos/estruturas/{idProdutoEstrutura}/componentes`
- Ação oficial: `VincularComponenteMultiplos`
- Resumo oficial: Adiciona componente(s) a uma estrutura

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_produto_estrutura` | `idProdutoEstrutura` | `path` | sim |

- Schemas de request: `ProdutosComponenteDTO`
- Schemas de response: 400: ErrorResponse, 404: ErrorResponse

### `alterar_componente`

- Bling: `PATCH /produtos/estruturas/{idProdutoEstrutura}/componentes/{idComponente}`
- Ação oficial: `AlterarComponente`
- Resumo oficial: Altera um componente de uma estrutura

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_produto_estrutura` | `idProdutoEstrutura` | `path` | sim |
| `id_componente` | `idComponente` | `path` | sim |

- Schemas de request: `ProdutosComponenteDTO`
- Schemas de response: 400: ErrorResponse, 404: ErrorResponse
