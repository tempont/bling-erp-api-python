# Logísticas - Objetos

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
objeto = client.logisticas_objetos.obter(1)
```

## Operações

### `criar_objeto`

- Bling: `POST /logisticas/objetos`
- Ação oficial: `CriarLogisticaObjeto`
- Resumo oficial: Cria um objeto de logística

- Schemas de request: `LogisticasObjetosDadosCreateRequestDTO`
- Schemas de response: 201: LogisticasObjetosObjetoDTO, 400: ErrorResponse

### `remover_objeto`

- Bling: `DELETE /logisticas/objetos/{idObjeto}`
- Ação oficial: `RemoverObjetoLogistico`
- Resumo oficial: Remove um objeto de logística personalizada

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_objeto` | `idObjeto` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `obter_objeto`

- Bling: `GET /logisticas/objetos/{idObjeto}`
- Ação oficial: `ObterObjetoLogistico`
- Resumo oficial: Obtém um objeto de logística

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_objeto` | `idObjeto` | `path` | sim |

- Schemas de response: 200: LogisticasObjetosDadosDTO, 404: ErrorResponse

### `alterar_objeto`

- Bling: `PUT /logisticas/objetos/{idObjeto}`
- Ação oficial: `AlterarLogisticaObjeto`
- Resumo oficial: Altera um objeto de logística pelo ID

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_objeto` | `idObjeto` | `path` | sim |

- Schemas de request: `LogisticasObjetosUpdateRequestDTO`
- Schemas de response: 200: LogisticasObjetosObjetoDTO, 400: ErrorResponse, 404: ErrorResponse
