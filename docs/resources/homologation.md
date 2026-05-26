# Homologação

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
produto = client.homologation.obter()
result = client.homologation.criar({'nome': 'Produto Teste', 'preco': 10.00})
```

## Operações

### `obter`

- Bling: `GET /homologacao/produtos`
- Ação oficial: `Obter`
- Resumo oficial: Obtém o produto da homologação

- Schemas de response: 200: HomologacaoDadosBaseDTO

### `criar`

- Bling: `POST /homologacao/produtos`
- Ação oficial: `Criar`
- Resumo oficial: Cria o produto da homologação

- Schemas de request: `HomologacaoDadosBaseDTO`
- Schemas de response: 201: HomologacaoDadosBaseDTO/HomologacaoDadosDTO, 400: ErrorResponse

### `remover`

- Bling: `DELETE /homologacao/produtos/{idProdutoHomologacao}`
- Ação oficial: `Remover`
- Resumo oficial: Remove o produto da homologação

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_produto_homologacao` | `idProdutoHomologacao` | `path` | sim |

- Schemas de response: 400: ErrorResponse

### `alterar`

- Bling: `PUT /homologacao/produtos/{idProdutoHomologacao}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera o produto da homologação

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_produto_homologacao` | `idProdutoHomologacao` | `path` | sim |

- Schemas de request: `HomologacaoDadosBaseDTO`
- Schemas de response: 400: ErrorResponse

### `alterar_situacao`

- Bling: `PATCH /homologacao/produtos/{idProdutoHomologacao}/situacoes`
- Ação oficial: `AlterarSituacao`
- Resumo oficial: Altera a situação do produto da homologação

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_produto_homologacao` | `idProdutoHomologacao` | `path` | sim |

- Schemas de request: `HomologacaoSituacaoDTO`
- Schemas de response: 400: ErrorResponse
