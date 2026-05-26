# Contas a Receber

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
contas = client.contas_receber.listar(
    situacoes=[1, 2],
    data_inicial="2024-01-01",
)
conta = client.contas_receber.obter(123456)
```

## Operações

### `listar`

- Bling: `GET /contas/receber`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém contas a receber

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |
| `situacoes` | `situacoes[]` | `query` | não |
| `tipo_filtro_data` | `tipoFiltroData` | `query` | não |
| `data_inicial` | `dataInicial` | `query` | não |
| `data_final` | `dataFinal` | `query` | não |
| `ids_categorias` | `idsCategorias[]` | `query` | não |
| `id_portador` | `idPortador` | `query` | não |
| `id_contato` | `idContato` | `query` | não |
| `id_vendedor` | `idVendedor` | `query` | não |
| `id_forma_pagamento` | `idFormaPagamento` | `query` | não |
| `boleto_gerado` | `boletoGerado` | `query` | não |

- Schemas de response: 200: ContasReceberDadosListDTO

### `criar`

- Bling: `POST /contas/receber`
- Ação oficial: `Criar`
- Resumo oficial: Cria uma conta a receber

- Schemas de request: `ContasDadosBaseDTO`, `ContasReceberDadosBaseDTO`, `ContasReceberDadosDTO`
- Schemas de response: 201: BasePostResponse, 400: ErrorResponse

### `obter_boletos`

- Bling: `GET /contas/receber/boletos`
- Ação oficial: `ObterBoletos`
- Resumo oficial: Obtém boletos de contas a receber

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_origem` | `idOrigem` | `query` | sim |
| `situacoes` | `situacoes[]` | `query` | não |

- Schemas de response: 200: ContasReceberBoletosDadosBaseDTO, 400: ErrorResponse

### `cancelar_boletos`

- Bling: `POST /contas/receber/boletos/cancelar`
- Ação oficial: `CancelarBoletos`
- Resumo oficial: Cancela boletos de contas a receber

- Schemas de request: `ContasReceberBoletosCancelarDTO`

### `remover`

- Bling: `DELETE /contas/receber/{idContaReceber}`
- Ação oficial: `Remover`
- Resumo oficial: Remove uma conta a receber

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_conta_receber` | `idContaReceber` | `path` | sim |

- Schemas de response: 400: ErrorResponse, 404: ErrorResponse

### `obter`

- Bling: `GET /contas/receber/{idContaReceber}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém uma conta a receber

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_conta_receber` | `idContaReceber` | `path` | sim |

- Schemas de response: 200: ContasReceberDadosBaseDTO/ContasReceberDadosDTO/ContasReceberDadosListDTO, 404: ErrorResponse

### `alterar`

- Bling: `PUT /contas/receber/{idContaReceber}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera uma conta a receber

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_conta_receber` | `idContaReceber` | `path` | sim |

- Schemas de request: `ContasDadosBaseDTO`, `ContasReceberDadosBaseDTO`
- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `baixar`

- Bling: `POST /contas/receber/{idContaReceber}/baixar`
- Ação oficial: `BaixarConta`
- Resumo oficial: Cria o recebimento de uma conta a receber

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_conta_receber` | `idContaReceber` | `path` | sim |

- Schemas de request: `ContasBaixarContaDTO`
- Schemas de response: 400: ErrorResponse
