# Logísticas - Remessas

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
remessas = client.logisticas_remessas.listar_por_logistica(101)
```

## Operações

### `criar_remessa`

- Bling: `POST /logisticas/remessas`
- Ação oficial: `CriarRemessa`
- Resumo oficial: Cria uma remessa de postagem de uma logística

- Schemas de request: `LogisticasRemessasDadosPostDTO`
- Schemas de response: 201: LogisticasRemessaRemessaDTO, 400: ErrorResponse

### `remover_remessa`

- Bling: `DELETE /logisticas/remessas/{idRemessa}`
- Ação oficial: `RemoverRemessa`
- Resumo oficial: Remove uma remessa de postagem

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_remessa` | `idRemessa` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `obter_remessa`

- Bling: `GET /logisticas/remessas/{idRemessa}`
- Ação oficial: `ObterRemessa`
- Resumo oficial: Obtém uma remessa de postagem

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_remessa` | `idRemessa` | `path` | sim |

- Schemas de response: 200: LogisticasRemessasDadosBaseDTO, 404: ErrorResponse

### `alterar_remessa`

- Bling: `PUT /logisticas/remessas/{idRemessa}`
- Ação oficial: `AlterarRemessa`
- Resumo oficial: Altera uma remessa de postagem

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_remessa` | `idRemessa` | `path` | sim |

- Schemas de request: `LogisticasRemessasDadosBaseDTOCommon`
- Schemas de response: 200: LogisticasRemessaRemessaDTO, 400: ErrorResponse, 404: ErrorResponse

### `listar_remessas_por_logistica`

- Bling: `GET /logisticas/{idLogistica}/remessas`
- Ação oficial: `ObterLogisticaRemessaMultiplos`
- Resumo oficial: Obtém as remessas de postagem de uma logística

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_logistica` | `idLogistica` | `path` | sim |

- Schemas de response: 200: LogisticasRemessasDadosDTO, 404: ErrorResponse, 400: ErrorResponse
