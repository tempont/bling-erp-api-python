# Formas de Pagamentos

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
formas = client.payment_methods.listar()
forma = client.payment_methods.obter(123456)
```

## Operações

### `listar`

- Bling: `GET /formas-pagamentos`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém formas de pagamentos

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |
| `descricao` | `descricao` | `query` | não |
| `tipos_pagamentos` | `tiposPagamentos[]` | `query` | não |
| `situacao` | `situacao` | `query` | não |

- Schemas de response: 200: FormasPagamentosDadosBaseDTO

### `criar`

- Bling: `POST /formas-pagamentos`
- Ação oficial: `Criar`
- Resumo oficial: Cria uma forma de pagamento

- Schemas de request: `FormasPagamentosDadosBaseDTO`, `FormasPagamentosDadosDTO`
- Schemas de response: 201: BasePostResponse, 400: ErrorResponse

### `remover`

- Bling: `DELETE /formas-pagamentos/{idFormaPagamento}`
- Ação oficial: `Remover`
- Resumo oficial: Remove uma forma de pagamento

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_forma_pagamento` | `idFormaPagamento` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `obter`

- Bling: `GET /formas-pagamentos/{idFormaPagamento}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém uma forma de pagamento

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_forma_pagamento` | `idFormaPagamento` | `path` | sim |

- Schemas de response: 200: FormasPagamentosDadosBaseDTO/FormasPagamentosDadosDTO, 404: ErrorResponse

### `alterar`

- Bling: `PUT /formas-pagamentos/{idFormaPagamento}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera uma forma de pagamento

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_forma_pagamento` | `idFormaPagamento` | `path` | sim |

- Schemas de request: `FormasPagamentosDadosBaseDTO`, `FormasPagamentosDadosDTO`
- Schemas de response: 200: BasePostResponse, 404: ErrorResponse, 400: ErrorResponse

### `alterar_padrao`

- Bling: `PATCH /formas-pagamentos/{idFormaPagamento}/padrao`
- Ação oficial: `AlterarAtributo`
- Resumo oficial: Altera o padrão de uma forma de pagamento

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_forma_pagamento` | `idFormaPagamento` | `path` | sim |

- Schemas de request: `FormasPagamentosDefinirPadraoDTO`
- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `alterar_situacao`

- Bling: `PATCH /formas-pagamentos/{idFormaPagamento}/situacao`
- Ação oficial: `AlterarSituacao`
- Resumo oficial: Altera a situação de uma forma de pagamento

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_forma_pagamento` | `idFormaPagamento` | `path` | sim |

- Schemas de request: `FormasPagamentosAlterarSituacaoDTO`
- Schemas de response: 404: ErrorResponse, 400: ErrorResponse
