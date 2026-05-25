# Produtos - Fornecedores

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
fornecedores = client.produtos_fornecedores.listar(
    limite=10, id_produto=123456789
)
um = client.produtos_fornecedores.obter(123456789)
```

## Operações

### `listar`

- Bling: `GET /produtos/fornecedores`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém produtos fornecedores

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |
| `id_produto` | `idProduto` | `query` | não |
| `id_fornecedor` | `idFornecedor` | `query` | não |

- Schemas de response: 200: ProdutosFornecedoresDadosBaseDTO

### `criar`

- Bling: `POST /produtos/fornecedores`
- Ação oficial: `Criar`
- Resumo oficial: Cria um produto fornecedor

- Schemas de request: `ProdutosFornecedoresDadosBaseDTO`, `ProdutosFornecedoresDadosDTO`
- Schemas de response: 201: BasePostResponse, 400: ErrorResponse

### `remover`

- Bling: `DELETE /produtos/fornecedores/{idProdutoFornecedor}`
- Ação oficial: `Remover`
- Resumo oficial: Remove um produto fornecedor

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_produto_fornecedor` | `idProdutoFornecedor` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `obter`

- Bling: `GET /produtos/fornecedores/{idProdutoFornecedor}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém um produto fornecedor

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_produto_fornecedor` | `idProdutoFornecedor` | `path` | sim |

- Schemas de response: 200: ProdutosFornecedoresDadosBaseDTO/ProdutosFornecedoresDadosDTO, 404: ErrorResponse

### `alterar`

- Bling: `PUT /produtos/fornecedores/{idProdutoFornecedor}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera um produto fornecedor

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_produto_fornecedor` | `idProdutoFornecedor` | `path` | sim |

- Schemas de request: `ProdutosFornecedoresDadosBaseUpdateDTO`, `ProdutosFornecedoresDadosUpdateDTO`
- Schemas de response: 200: BasePostResponse, 404: ErrorResponse, 400: ErrorResponse
