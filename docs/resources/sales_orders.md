# Pedidos de venda

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
pedidos = client.pedidos_vendas.listar(
    data_inicial="2024-01-01",
    ids_situacoes=[123456],
)
pedido = client.pedidos_vendas.obter(123456)
```

## Operações

### `remover_varios`

- Bling: `DELETE /pedidos/vendas`
- Ação oficial: `RemoverMultiplos`
- Resumo oficial: Remove pedidos de vendas

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `ids_pedidos_vendas` | `idsPedidosVendas[]` | `query` | sim |


### `listar`

- Bling: `GET /pedidos/vendas`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém pedidos de vendas

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |
| `id_contato` | `idContato` | `query` | não |
| `ids_situacoes` | `idsSituacoes[]` | `query` | não |
| `data_inicial` | `dataInicial` | `query` | não |
| `data_final` | `dataFinal` | `query` | não |
| `data_alteracao_inicial` | `dataAlteracaoInicial` | `query` | não |
| `data_alteracao_final` | `dataAlteracaoFinal` | `query` | não |
| `data_prevista_inicial` | `dataPrevistaInicial` | `query` | não |
| `data_prevista_final` | `dataPrevistaFinal` | `query` | não |
| `numero` | `numero` | `query` | não |
| `id_loja` | `idLoja` | `query` | não |
| `id_vendedor` | `idVendedor` | `query` | não |
| `id_controle_caixa` | `idControleCaixa` | `query` | não |
| `numeros_lojas` | `numerosLojas[]` | `query` | não |
| `id_unidade_negocio` | `idUnidadeNegocio` | `query` | não |

- Schemas de response: 200: VendasDadosBaseDTO

### `criar`

- Bling: `POST /pedidos/vendas`
- Ação oficial: `Criar`
- Resumo oficial: Cria um pedido de venda

- Schemas de request: `VendasDadosBaseDTO`, `VendasDadosDTO`
- Schemas de response: 201: BasePostResponse/VendasResponse_POST_PUT, 400: ErrorResponse

### `remover`

- Bling: `DELETE /pedidos/vendas/{idPedidoVenda}`
- Ação oficial: `Remover`
- Resumo oficial: Remove um pedido de venda

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_pedido_venda` | `idPedidoVenda` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `obter`

- Bling: `GET /pedidos/vendas/{idPedidoVenda}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém um pedido de venda

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_pedido_venda` | `idPedidoVenda` | `path` | sim |

- Schemas de response: 200: VendasDadosBaseDTO/VendasDadosDTO, 404: ErrorResponse

### `alterar`

- Bling: `PUT /pedidos/vendas/{idPedidoVenda}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera um pedido de venda

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_pedido_venda` | `idPedidoVenda` | `path` | sim |

- Schemas de request: `VendasDadosBaseDTO_PUT`, `VendasDadosDTO`
- Schemas de response: 200: BasePostResponse/VendasResponse_POST_PUT, 404: ErrorResponse, 400: ErrorResponse

### `estornar_contas`

- Bling: `POST /pedidos/vendas/{idPedidoVenda}/estornar-contas`
- Ação oficial: `EstornarContas`
- Resumo oficial: Estorna as contas de um pedido de venda

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_pedido_venda` | `idPedidoVenda` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `estornar_estoque`

- Bling: `POST /pedidos/vendas/{idPedidoVenda}/estornar-estoque`
- Ação oficial: `EstornarEstoque`
- Resumo oficial: Estorna o estoque de um pedido de venda

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_pedido_venda` | `idPedidoVenda` | `path` | sim |

- Schemas de response: 404: ErrorResponse

### `gerar_nota_fiscal_consumidor`

- Bling: `POST /pedidos/vendas/{idPedidoVenda}/gerar-nfce`
- Ação oficial: `GerarNotaFiscalConsumidor`
- Resumo oficial: Gera nota fiscal de consumidor eletrônica a partir do pedido de venda

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_pedido_venda` | `idPedidoVenda` | `path` | sim |

- Schemas de response: 201: VendasCreateInvoiceResponseDTO, 404: ErrorResponse, 400: ErrorResponse

### `gerar_nota_fiscal`

- Bling: `POST /pedidos/vendas/{idPedidoVenda}/gerar-nfe`
- Ação oficial: `GerarNotaFiscal`
- Resumo oficial: Gera nota fiscal eletrônica a partir do pedido de venda

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_pedido_venda` | `idPedidoVenda` | `path` | sim |

- Schemas de response: 201: VendasCreateInvoiceResponseDTO, 404: ErrorResponse, 400: ErrorResponse

### `lancar_contas`

- Bling: `POST /pedidos/vendas/{idPedidoVenda}/lancar-contas`
- Ação oficial: `LancarContas`
- Resumo oficial: Lança as contas de um pedido de venda

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_pedido_venda` | `idPedidoVenda` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `lancar_estoque`

- Bling: `POST /pedidos/vendas/{idPedidoVenda}/lancar-estoque`
- Ação oficial: `LancarEstoque`
- Resumo oficial: Lança o estoque de um pedido de venda no depósito padrão

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_pedido_venda` | `idPedidoVenda` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `lancar_estoque_id_deposito`

- Bling: `POST /pedidos/vendas/{idPedidoVenda}/lancar-estoque/{idDeposito}`
- Ação oficial: `LancarEstoqueDeposito`
- Resumo oficial: Lança o estoque de um pedido de venda especificando o depósito

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_pedido_venda` | `idPedidoVenda` | `path` | sim |
| `id_deposito` | `idDeposito` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `alterar_situacao`

- Bling: `PATCH /pedidos/vendas/{idPedidoVenda}/situacoes/{idSituacao}`
- Ação oficial: `AlterarSituacao`
- Resumo oficial: Altera a situação de um pedido de venda

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_pedido_venda` | `idPedidoVenda` | `path` | sim |
| `id_situacao` | `idSituacao` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse
