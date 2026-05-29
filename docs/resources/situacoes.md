# Situations

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
Lista as situacoes.
```

## Operações

### `criar`

- Bling: `POST /situacoes`
- Ação oficial: `Criar`
- Resumo oficial: Cria uma situação

- Schemas de request: `SituacoesDadosDTO`
- Schemas de response: 201: BasePostResponse, 400: ErrorResponse

### `remover`

- Bling: `DELETE /situacoes/{idSituacao}`
- Ação oficial: `Remover`
- Resumo oficial: Remove uma situação

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_situacao` | `idSituacao` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `obter`

- Bling: `GET /situacoes/{idSituacao}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém uma situação

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_situacao` | `idSituacao` | `path` | sim |

- Schemas de response: 200: SituacoesDTO/SituacoesDadosDTO, 404: ErrorResponse

### `alterar`

- Bling: `PUT /situacoes/{idSituacao}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera uma situação

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_situacao` | `idSituacao` | `path` | sim |

- Schemas de request: `SituacoesDadosDTO`
- Schemas de response: 200: BasePostResponse, 400: ErrorResponse
