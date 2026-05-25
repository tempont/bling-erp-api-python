# Produtos - Lotes Lancamentos

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
lancs = client.lotes_lancamentos.listar(id_lote=123456789)
saldo_total = client.lotes_lancamentos.obter_saldos_soma(id_produto=123456789)
soma_dep = client.lotes_lancamentos.obter_saldos_soma_deposito(id_produto=123456789, id_deposito=987654321)
```

## Operações

### `obter`

- Bling: `GET /produtos/lotes/lancamentos/{idLancamento}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém um lançamento de um lote de produto

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_lancamento` | `idLancamento` | `path` | sim |

- Schemas de response: 200: LoteLancamentoDTO, 400: ErrorResponse, 404: ErrorResponse

### `alterar_atributo`

- Bling: `PATCH /produtos/lotes/lancamentos/{idLancamento}`
- Ação oficial: `AlterarAtributo`
- Resumo oficial: Altera a observação de um lançamento de um lote de um produto

- Schemas de request: `LoteLancamentoObservacaoDTO`
- Schemas de response: 400: ErrorResponse, 404: ErrorResponse

### `listar`

- Bling: `GET /produtos/lotes/{idLote}/lancamentos`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém os lançamentos de um lote de produto

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_lote` | `idLote` | `path` | sim |

- Schemas de response: 200: LoteLancamentoDTO, 400: ErrorResponse, 404: ErrorResponse

### `criar`

- Bling: `POST /produtos/lotes/{idLote}/lancamentos`
- Ação oficial: `Criar`
- Resumo oficial: Cria um lançamento de um lote

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_lote` | `idLote` | `path` | sim |

- Schemas de request: `LoteLancamentoDTO`
- Schemas de response: 200: LoteLancamentoDTO, 400: ErrorResponse, 404: ErrorResponse

### `obter_saldos`

- Bling: `GET /produtos/{idProduto}/lotes/depositos/{idDeposito}/saldo`
- Ação oficial: `ObterSaldosLote`
- Resumo oficial: Obtém os saldos dos lotes de um produto por depósito

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `ids_lotes` | `idsLotes[]` | `query` | sim |
| `id_produto` | `idProduto` | `path` | sim |
| `id_deposito` | `idDeposito` | `path` | sim |

- Schemas de response: 200: SaldoLoteDTO, 404: ErrorResponse, 400: ErrorResponse

### `obter_saldos_soma_deposito`

- Bling: `GET /produtos/{idProduto}/lotes/depositos/{idDeposito}/saldo/soma`
- Ação oficial: `ObterSaldosLote`
- Resumo oficial: Obtém a soma dos saldos dos lotes de um produto em um depósito

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_produto` | `idProduto` | `path` | sim |
| `id_deposito` | `idDeposito` | `path` | sim |

- Schemas de response: 200: SaldoSomaLotesDTO, 404: ErrorResponse, 400: ErrorResponse

### `obter_saldos_soma`

- Bling: `GET /produtos/{idProduto}/lotes/saldo/soma`
- Ação oficial: `ObterSaldosLote`
- Resumo oficial: Obtém o saldo total dos lotes de um produto

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_produto` | `idProduto` | `path` | sim |

- Schemas de response: 200: SaldoSomaLotesTodosDepositosDTO, 404: ErrorResponse

### `obter_saldos_saldo`

- Bling: `GET /produtos/{idProduto}/lotes/{idLote}/depositos/{idDeposito}/saldo`
- Ação oficial: `ObterSaldosLote`
- Resumo oficial: Obtém o saldo de um lote de produto

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_lote` | `idLote` | `path` | sim |
| `id_produto` | `idProduto` | `path` | sim |
| `id_deposito` | `idDeposito` | `path` | sim |

- Schemas de response: 200: SaldoLoteDTO, 404: ErrorResponse
