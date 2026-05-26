# Categorias - Lojas

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
categorias = client.store_categories.listar()
categoria = client.store_categories.obter(123456)
```

## Operações

### `listar`

- Bling: `GET /categorias/lojas`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém categorias de lojas virtuais vinculadas a de produtos

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |
| `id_loja` | `idLoja` | `query` | não |
| `id_categoria_produto` | `idCategoriaProduto` | `query` | não |
| `id_categoria_produto_pai` | `idCategoriaProdutoPai` | `query` | não |

- Schemas de response: 200: CategoriasLojasDadosDTO

### `criar`

- Bling: `POST /categorias/lojas`
- Ação oficial: `Criar`
- Resumo oficial: Cria o vínculo de uma categoria da loja com a de produto

- Schemas de request: `CategoriasLojasDadosDTO`
- Schemas de response: 201: BasePostResponse, 400: ErrorResponse

### `remover`

- Bling: `DELETE /categorias/lojas/{idCategoriaLoja}`
- Ação oficial: `Remover`
- Resumo oficial: Remove o vínculo de uma categoria da loja com a de produto

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_categoria_loja` | `idCategoriaLoja` | `path` | sim |

- Schemas de response: 404: ErrorResponse

### `obter`

- Bling: `GET /categorias/lojas/{idCategoriaLoja}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém uma categoria da loja vinculada a de produto

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_categoria_loja` | `idCategoriaLoja` | `path` | sim |

- Schemas de response: 200: CategoriasLojasDadosDTO, 404: ErrorResponse

### `alterar`

- Bling: `PUT /categorias/lojas/{idCategoriaLoja}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera o vínculo de uma categoria da loja com a de produto

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_categoria_loja` | `idCategoriaLoja` | `path` | sim |

- Schemas de request: `CategoriasLojasDadosDTO`
- Schemas de response: 404: ErrorResponse, 400: ErrorResponse
