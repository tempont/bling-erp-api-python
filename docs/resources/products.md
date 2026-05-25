# Produtos

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
produtos = client.produtos.listar(
    nome="Camiseta",
    ids_produtos=[123456],
)
produto = client.produtos.obter(123456)
```

## Operações

### `remover_varios`

- Bling: `DELETE /produtos`
- Ação oficial: `RemoverMultiplos`
- Resumo oficial: Remove múltiplos produtos

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `ids_produtos` | `idsProdutos[]` | `query` | sim |

- Schemas de response: 200: ProdutosAlertasResponse, 400: ErrorResponse

### `listar`

- Bling: `GET /produtos`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém produtos

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |
| `criterio` | `criterio` | `query` | não |
| `tipo` | `tipo` | `query` | não |
| `id_componente` | `idComponente` | `query` | não |
| `data_inclusao_inicial` | `dataInclusaoInicial` | `query` | não |
| `data_inclusao_final` | `dataInclusaoFinal` | `query` | não |
| `data_alteracao_inicial` | `dataAlteracaoInicial` | `query` | não |
| `data_alteracao_final` | `dataAlteracaoFinal` | `query` | não |
| `id_categoria` | `idCategoria` | `query` | não |
| `id_loja` | `idLoja` | `query` | não |
| `nome` | `nome` | `query` | não |
| `ids_produtos` | `idsProdutos[]` | `query` | não |
| `codigos` | `codigos[]` | `query` | não |
| `gtins` | `gtins[]` | `query` | não |
| `filtro_saldo_estoque` | `filtroSaldoEstoque` | `query` | não |
| `filtro_saldo_estoque_deposito` | `filtroSaldoEstoqueDeposito` | `query` | não |

- Schemas de response: 200: ProdutosDadosBaseDTO

### `criar`

- Bling: `POST /produtos`
- Ação oficial: `Criar`
- Resumo oficial: Cria um produto

- Schemas de request: `ProdutosDadosDTO`
- Schemas de response: 201: ProdutosResponse_POST_PUT, 400: ErrorResponse, 403: ErrorResponse

### `alterar_situacao_varios`

- Bling: `POST /produtos/situacoes`
- Ação oficial: `AlterarSituacaoMultiplos`
- Resumo oficial: Altera a situação de múltiplos produtos

- Schemas de response: 200: ProdutosAlertasResponse, 400: ErrorResponse

### `remover`

- Bling: `DELETE /produtos/{idProduto}`
- Ação oficial: `Remover`
- Resumo oficial: Remove um produto

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_produto` | `idProduto` | `path` | sim |

- Schemas de response: 404: ErrorResponse

### `obter`

- Bling: `GET /produtos/{idProduto}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém um produto

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_produto` | `idProduto` | `path` | sim |

- Schemas de response: 200: ProdutosDadosDTO, 403: ErrorResponse, 404: ErrorResponse

### `alterar_parcialmente`

- Bling: `PATCH /produtos/{idProduto}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera parcialmente um produto

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_produto` | `idProduto` | `path` | sim |

- Schemas de request: `ProdutosDadosPatchDTO`
- Schemas de response: 200: ProdutosResponse_POST_PUT, 400: ErrorResponse, 403: ErrorResponse

### `alterar`

- Bling: `PUT /produtos/{idProduto}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera um produto

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_produto` | `idProduto` | `path` | sim |

- Schemas de request: `ProdutosDadosDTO`
- Schemas de response: 200: ProdutosResponse_POST_PUT, 400: ErrorResponse, 403: ErrorResponse

### `alterar_situacao`

- Bling: `PATCH /produtos/{idProduto}/situacoes`
- Ação oficial: `AlterarSituacao`
- Resumo oficial: Altera a situação de um produto

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_produto` | `idProduto` | `path` | sim |

- Schemas de response: 400: ErrorResponse, 404: ErrorResponse
