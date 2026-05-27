# Notificações

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
notificacoes = client.notificacoes.listar(
    periodo="2025-01",
)
client.notificacoes.alterar("01ARZ3NDEKTSV4RRFFQ69G5FAV")
```

## Operações

### `listar`

- Bling: `GET /notificacoes`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém todas as notificações de uma empresa em um período

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `periodo` | `periodo` | `query` | não |

- Schemas de response: 200: NotificacoesDadosBaseDTO/NotificacoesUlidsDTO, 400: ErrorResponse

### `obter_quantidade`

- Bling: `GET /notificacoes/quantidade`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém a quantidade de notificações de uma empresa em um período

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `periodo` | `periodo` | `query` | não |

- Schemas de response: 200: NotificacoesQuantidadeDTO, 400: ErrorResponse

### `alterar`

- Bling: `POST /notificacoes/{idNotificacao}/confirmar-leitura`
- Ação oficial: `Alterar`
- Resumo oficial: Marca notificação como lida

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_notificacao` | `idNotificacao` | `path` | sim |

- Schemas de response: 200: NotificacoesDadosBaseDTO/NotificacoesUlidsDTO, 400: ErrorResponse
