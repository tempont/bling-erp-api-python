# Estoques

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
saldos = client.estoques.obter_saldos(ids_produtos=[123, 456])
saldos_dep = client.estoques.obter_saldos_por_deposito(1, ids_produtos=[123])
```

## Operações

### `criar`

- Bling: `POST /estoques`
- Ação oficial: `Criar`
- Resumo oficial: Cria um registro de estoque

- Schemas de request: `EstoquesDadosBaseDTO`, `EstoquesDadosDTO`
- Schemas de response: 201: BasePostResponse, 400: ErrorResponse

### `obter_saldos`

- Bling: `GET /estoques/saldos`
- Ação oficial: `ObterSaldosEstoque`
- Resumo oficial: Obtém o saldo em estoque de produtos

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `ids_produtos` | `idsProdutos[]` | `query` | sim |
| `codigos` | `codigos[]` | `query` | não |
| `filtro_saldo_estoque` | `filtroSaldoEstoque` | `query` | não |

- Schemas de response: 200: EstoquesSaldosBaseDTO/EstoquesSaldosDTO, 400: ErrorResponse

### `obter_saldos_por_deposito`

- Bling: `GET /estoques/saldos/{idDeposito}`
- Ação oficial: `ObterSaldosEstoqueDeposito`
- Resumo oficial: Obtém o saldo em estoque de produtos por depósito

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_deposito` | `idDeposito` | `path` | sim |
| `ids_produtos` | `idsProdutos[]` | `query` | sim |
| `codigos` | `codigos[]` | `query` | não |
| `filtro_saldo_estoque` | `filtroSaldoEstoque` | `query` | não |

- Schemas de response: 200: EstoquesSaldosBaseDTO, 400: ErrorResponse, 404: ErrorResponse
