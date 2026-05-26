# Categorias - Receitas e Despesas

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
categorias = client.income_expense_categories.listar(tipo=2)
categoria = client.income_expense_categories.obter(123456)
```

## Operações

### `remover_varios`

- Bling: `DELETE /categorias/receitas-despesas`
- Ação oficial: `RemoverMultiplos`
- Resumo oficial: Remove múltiplas categorias de receita e despesa

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `ids_categorias` | `idsCategorias[]` | `query` | sim |

- Schemas de response: 200: ErrorResponse

### `listar`

- Bling: `GET /categorias/receitas-despesas`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém categorias de receitas e despesas

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |
| `tipo` | `tipo` | `query` | não |
| `situacao` | `situacao` | `query` | não |

- Schemas de response: 200: CategoriasReceitasDespesasDadosBaseDTO

### `criar`

- Bling: `POST /categorias/receitas-despesas`
- Ação oficial: `Criar`
- Resumo oficial: Cria uma categoria de receita e despesa

- Schemas de request: `CategoriasReceitasDespesasDadosBaseDTO`, `CategoriasReceitasDespesasDadosPostDTO`
- Schemas de response: 201: CategoriasReceitasDespesasDadosBaseDTO, 400: ErrorResponse

### `remover`

- Bling: `DELETE /categorias/receitas-despesas/{idCategoria}`
- Ação oficial: `Remover`
- Resumo oficial: Remove uma categoria de receita e despesa

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_categoria` | `idCategoria` | `path` | sim |

- Schemas de response: 400: ErrorResponse, 404: ErrorResponse

### `obter`

- Bling: `GET /categorias/receitas-despesas/{idCategoria}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém uma categoria de receita e despesa

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_categoria` | `idCategoria` | `path` | sim |

- Schemas de response: 200: CategoriasReceitasDespesasDadosBaseDTO/CategoriasReceitasDespesasDadosDTO, 404: ErrorResponse

### `alterar`

- Bling: `PUT /categorias/receitas-despesas/{idCategoria}`
- Ação oficial: `Alterar`
- Resumo oficial: Atualiza uma categoria de receita e despesa

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_categoria` | `idCategoria` | `path` | sim |

- Schemas de request: `CategoriasReceitasDespesasDadosBaseDTO`, `CategoriasReceitasDespesasDadosPostDTO`
- Schemas de response: 200: CategoriasReceitasDespesasDadosBaseDTO, 400: ErrorResponse, 404: ErrorResponse
