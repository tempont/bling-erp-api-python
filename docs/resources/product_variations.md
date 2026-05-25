# Produtos - Variacoes

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
# Veja as operacoes geradas abaixo.
```

## Operações

### `gerar_combinacoes`

- Bling: `POST /produtos/variacoes/atributos/gerar-combinacoes`
- Ação oficial: `GerarCombinacoes`
- Resumo oficial: Retorna o produto pai com combinações de novas variações

- Schemas de request: `ProdutosVariacoesCombinacaoDadosDTO`
- Schemas de response: 200: ProdutosDadosDTO, 400: ErrorResponse

### `listar`

- Bling: `GET /produtos/variacoes/{idProdutoPai}`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém o produto e variações

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_produto_pai` | `idProdutoPai` | `path` | sim |

- Schemas de response: 200: ProdutosDadosDTO, 404: ErrorResponse

### `alterar_atributo`

- Bling: `PATCH /produtos/variacoes/{idProdutoPai}/atributos`
- Ação oficial: `AlterarAtributo`
- Resumo oficial: Altera o nome do atributo nas variações

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_produto_pai` | `idProdutoPai` | `path` | sim |

- Schemas de request: `ProdutosVariacoesDadosAtributoDTO`
- Schemas de response: 200: BasePostResponse, 400: ErrorResponse
