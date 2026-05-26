# Grupos de Produtos

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
grupos = client.product_groups.listar()
grupo = client.product_groups.obter(123456)
```

## Operações

### `remover_varios`

- Bling: `DELETE /grupos-produtos`
- Ação oficial: `RemoverMultiplos`
- Resumo oficial: Remove múltiplos grupos de produtos

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `ids_grupos_produtos` | `idsGruposProdutos[]` | `query` | sim |

- Schemas de response: 200: ErrorResponse, 400: ErrorResponse

### `listar`

- Bling: `GET /grupos-produtos`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém grupos de produtos

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `nome` | `nome` | `query` | não |
| `nome_pai` | `nomePai` | `query` | não |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |

- Schemas de response: 200: GruposProdutosDadosDTO

### `criar`

- Bling: `POST /grupos-produtos`
- Ação oficial: `Criar`
- Resumo oficial: Cria um grupo de produtos

- Schemas de request: `GruposProdutosDadosDTO`, `GruposProdutosGrupoProdutoPaiDTO`
- Schemas de response: 201: BasePostResponse, 400: ErrorResponse

### `remover`

- Bling: `DELETE /grupos-produtos/{idGrupoProduto}`
- Ação oficial: `Remover`
- Resumo oficial: Remove um grupo de produtos

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_grupo_produto` | `idGrupoProduto` | `path` | sim |

- Schemas de response: 400: ErrorResponse, 404: ErrorResponse

### `obter`

- Bling: `GET /grupos-produtos/{idGrupoProduto}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém um grupo de produtos

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_grupo_produto` | `idGrupoProduto` | `path` | sim |

- Schemas de response: 200: GruposProdutosDadosDTO/GruposProdutosGrupoProdutoPaiDTO, 404: ErrorResponse

### `alterar`

- Bling: `PUT /grupos-produtos/{idGrupoProduto}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera um grupo de produtos

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_grupo_produto` | `idGrupoProduto` | `path` | sim |

- Schemas de request: `GruposProdutosDadosDTO`, `GruposProdutosGrupoProdutoPaiDTO`
- Schemas de response: 400: ErrorResponse, 404: ErrorResponse
