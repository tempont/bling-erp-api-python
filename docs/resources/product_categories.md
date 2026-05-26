# Categorias - Produtos

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
categorias = client.product_categories.listar()
categoria = client.product_categories.obter(123456)
```

## Operações

### `listar`

- Bling: `GET /categorias/produtos`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém categorias de produtos

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |

- Schemas de response: 200: CategoriasProdutosCategoriPaiDTO/CategoriasProdutosDadosDTO

### `criar`

- Bling: `POST /categorias/produtos`
- Ação oficial: `Criar`
- Resumo oficial: Cria uma categoria de produto

- Schemas de request: `CategoriasProdutosCategoriPaiDTO`, `CategoriasProdutosDadosDTO`
- Schemas de response: 201: BasePostResponse, 400: ErrorResponse

### `remover`

- Bling: `DELETE /categorias/produtos/{idCategoriaProduto}`
- Ação oficial: `Remover`
- Resumo oficial: Remove uma categoria de produto

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_categoria_produto` | `idCategoriaProduto` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `obter`

- Bling: `GET /categorias/produtos/{idCategoriaProduto}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém uma categoria de produto

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_categoria_produto` | `idCategoriaProduto` | `path` | sim |

- Schemas de response: 200: CategoriasProdutosCategoriPaiDTO/CategoriasProdutosDadosDTO, 404: ErrorResponse

### `alterar`

- Bling: `PUT /categorias/produtos/{idCategoriaProduto}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera uma categoria de produto

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_categoria_produto` | `idCategoriaProduto` | `path` | sim |

- Schemas de request: `CategoriasProdutosDadosDTO`
- Schemas de response: 404: ErrorResponse, 400: ErrorResponse
