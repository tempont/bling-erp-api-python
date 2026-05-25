# Produtos - Lojas

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
# Veja as operacoes geradas abaixo.
```

## Operações

### `listar`

- Bling: `GET /produtos/lojas`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém vínculos de produtos com lojas

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |
| `id_produto` | `idProduto` | `query` | não |
| `id_loja` | `idLoja` | `query` | não |
| `id_categoria_produto` | `idCategoriaProduto` | `query` | não |
| `data_alteracao_inicial` | `dataAlteracaoInicial` | `query` | não |
| `data_alteracao_final` | `dataAlteracaoFinal` | `query` | não |

- Schemas de response: 200: ProdutosLojasDadosDTO, 400: ErrorResponse

### `criar`

- Bling: `POST /produtos/lojas`
- Ação oficial: `Criar`
- Resumo oficial: Cria o vínculo de um produto com uma loja

- Schemas de request: `ProdutosLojasDadosBaseDTO`, `ProdutosLojasDadosDTO`
- Schemas de response: 201: BasePostResponse/ProdutosLojasResponse_POST_PUT, 400: ErrorResponse

### `remover`

- Bling: `DELETE /produtos/lojas/{idProdutoLoja}`
- Ação oficial: `Remover`
- Resumo oficial: Remove o vínculo de um produto com uma loja

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_produto_loja` | `idProdutoLoja` | `path` | sim |

- Schemas de response: 404: ErrorResponse

### `obter`

- Bling: `GET /produtos/lojas/{idProdutoLoja}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém um vínculo de produto com loja

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_produto_loja` | `idProdutoLoja` | `path` | sim |

- Schemas de response: 200: ProdutosLojasDadosBaseDTO/ProdutosLojasDadosDTO, 404: ErrorResponse

### `alterar`

- Bling: `PUT /produtos/lojas/{idProdutoLoja}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera o vínculo de um produto com uma loja

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_produto_loja` | `idProdutoLoja` | `path` | sim |

- Schemas de request: `ProdutosLojasDadosBaseDTO`, `ProdutosLojasDadosDTO`
- Schemas de response: 200: BasePostResponse/ProdutosLojasResponse_POST_PUT, 400: ErrorResponse, 404: ErrorResponse
