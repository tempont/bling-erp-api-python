# Logísticas

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
logisticas = client.logisticas.listar()
logistica = client.logisticas.obter(123456)
```

## Operações

### `listar`

- Bling: `GET /logisticas`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém logísticas

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |
| `tipo_integracao` | `tipoIntegracao` | `query` | não |
| `tipos_integracoes` | `tiposIntegracoes[]` | `query` | não |
| `situacao` | `situacao` | `query` | não |
| `logisticas_reversas` | `logisticasReversas` | `query` | não |

- Schemas de response: 200: LogisticasDadosBaseDTO, 404: ErrorResponse

### `criar`

- Bling: `POST /logisticas`
- Ação oficial: `Criar`
- Resumo oficial: Cria logística

- Schemas de request: `LogisticasDadosPostDTO`
- Schemas de response: 201: LogisticasLogisticaDTO, 400: ErrorResponse

### `remover`

- Bling: `DELETE /logisticas/{idLogistica}`
- Ação oficial: `Remover`
- Resumo oficial: Remove uma logística

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_logistica` | `idLogistica` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `obter`

- Bling: `GET /logisticas/{idLogistica}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém uma logística

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_logistica` | `idLogistica` | `path` | sim |
| `listar_servicos_inativos` | `listarServicosInativos` | `query` | não |

- Schemas de response: 200: LogisticasDadosDTO, 404: ErrorResponse

### `alterar`

- Bling: `PUT /logisticas/{idLogistica}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera uma logística

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_logistica` | `idLogistica` | `path` | sim |

- Schemas de request: `LogisticasDadosPutDTO`
- Schemas de response: 400: ErrorResponse
