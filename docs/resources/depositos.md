# Depósitos

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
depositos = client.depositos.listar()
deposito = client.depositos.obter(123456)
```

## Operações

### `listar`

- Bling: `GET /depositos`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém depósitos

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |
| `descricao` | `descricao` | `query` | não |
| `situacao` | `situacao` | `query` | não |

- Schemas de response: 200: DepositosDadosDTO

### `criar`

- Bling: `POST /depositos`
- Ação oficial: `Criar`
- Resumo oficial: Cria um depósito

- Schemas de request: `DepositosDadosDTO`
- Schemas de response: 201: BasePostResponse, 400: ErrorResponse

### `obter`

- Bling: `GET /depositos/{idDeposito}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém um depósito

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_deposito` | `idDeposito` | `path` | sim |

- Schemas de response: 200: DepositosDadosDTO, 404: ErrorResponse

### `alterar`

- Bling: `PUT /depositos/{idDeposito}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera um depósito

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_deposito` | `idDeposito` | `path` | sim |

- Schemas de request: `DepositosDadosDTO`
- Schemas de response: 200: BasePostResponse/ErrorField, 400: ErrorResponse, 404: ErrorResponse
