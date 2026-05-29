# Situation Transitions

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
Lista as transicoes de situacoes.
```

## Operações

### `criar`

- Bling: `POST /situacoes/transicoes`
- Ação oficial: `Criar`
- Resumo oficial: Cria uma transição

- Schemas de request: `SituacoesTransicaoDTO`
- Schemas de response: 201: BasePostResponse, 400: ErrorResponse

### `remover`

- Bling: `DELETE /situacoes/transicoes/{idTransicao}`
- Ação oficial: `Remover`
- Resumo oficial: Remove uma transição

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_transicao` | `idTransicao` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `obter`

- Bling: `GET /situacoes/transicoes/{idTransicao}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém uma transição

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_transicao` | `idTransicao` | `path` | sim |

- Schemas de response: 200: SituacoesTransicaoDTO, 404: ErrorResponse

### `alterar`

- Bling: `PUT /situacoes/transicoes/{idTransicao}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera uma transição

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_transicao` | `idTransicao` | `path` | sim |

- Schemas de request: `SituacoesTransicaoDTO`
- Schemas de response: 200: BasePostResponse, 400: ErrorResponse
