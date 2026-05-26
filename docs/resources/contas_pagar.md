# Contas a Pagar

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
contas = client.contas_pagar.listar(
    situacao=1,
    data_vencimento_inicial="2024-01-01",
)
conta = client.contas_pagar.obter(123456)
```

## Operações

### `listar`

- Bling: `GET /contas/pagar`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém contas a pagar

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |
| `data_emissao_inicial` | `dataEmissaoInicial` | `query` | não |
| `data_emissao_final` | `dataEmissaoFinal` | `query` | não |
| `data_vencimento_inicial` | `dataVencimentoInicial` | `query` | não |
| `data_vencimento_final` | `dataVencimentoFinal` | `query` | não |
| `data_pagamento_inicial` | `dataPagamentoInicial` | `query` | não |
| `data_pagamento_final` | `dataPagamentoFinal` | `query` | não |
| `situacao` | `situacao` | `query` | não |
| `id_contato` | `idContato` | `query` | não |

- Schemas de response: 200: ContasDadosBaseDTO

### `criar`

- Bling: `POST /contas/pagar`
- Ação oficial: `Criar`
- Resumo oficial: Cria uma conta a pagar

- Schemas de request: `ContasDadosBaseDTO`, `ContasPagarDadosDTO`, `ContasPagarDadosPostDTO`
- Schemas de response: 201: BasePostResponse, 400: ErrorResponse

### `remover`

- Bling: `DELETE /contas/pagar/{idContaPagar}`
- Ação oficial: `Remover`
- Resumo oficial: Remove uma conta a pagar

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_conta_pagar` | `idContaPagar` | `path` | sim |

- Schemas de response: 400: ErrorResponse, 404: ErrorResponse

### `obter`

- Bling: `GET /contas/pagar/{idContaPagar}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém uma conta a pagar

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_conta_pagar` | `idContaPagar` | `path` | sim |

- Schemas de response: 200: ContasDadosBaseDTO/ContasPagarDadosDTO, 404: ErrorResponse

### `alterar`

- Bling: `PUT /contas/pagar/{idContaPagar}`
- Ação oficial: `Alterar`
- Resumo oficial: Atualiza uma conta a pagar

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_conta_pagar` | `idContaPagar` | `path` | sim |

- Schemas de request: `ContasDadosBaseDTO`, `ContasPagarDadosDTO`
- Schemas de response: 200: BasePostResponse, 400: ErrorResponse, 404: ErrorResponse

### `baixar`

- Bling: `POST /contas/pagar/{idContaPagar}/baixar`
- Ação oficial: `BaixarConta`
- Resumo oficial: Cria o recebimento de uma conta a pagar

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_conta_pagar` | `idContaPagar` | `path` | sim |

- Schemas de request: `ContasBaixarContaDTO`
- Schemas de response: 400: ErrorResponse
