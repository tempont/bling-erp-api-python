# Purchase Orders

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
Lista os pedidos de compra.
```

## Operações

### `listar`

- Bling: `GET /pedidos/compras`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém pedidos de compras

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |
| `id_fornecedor` | `idFornecedor` | `query` | não |
| `valor_situacao` | `valorSituacao` | `query` | não |
| `id_situacao` | `idSituacao` | `query` | não |
| `data_inicial` | `dataInicial` | `query` | não |
| `data_final` | `dataFinal` | `query` | não |
| `ids_notas_fiscais` | `idsNotasFiscais[]` | `query` | não |

- Schemas de response: 200: PedidosComprasDadosBaseDTO

### `criar`

- Bling: `POST /pedidos/compras`
- Ação oficial: `Criar`
- Resumo oficial: Cria um pedido de compra

- Schemas de request: `PedidosComprasDadosBaseDTO`, `PedidosComprasDadosDTO`
- Schemas de response: 201: BasePostResponse/PedidosCompraResponse_POST_PUT, 400: ErrorResponse

### `remover`

- Bling: `DELETE /pedidos/compras/{idPedidoCompra}`
- Ação oficial: `Remover`
- Resumo oficial: Remove um pedido de compra

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_pedido_compra` | `idPedidoCompra` | `path` | sim |

- Schemas de response: 404: ErrorResponse

### `obter`

- Bling: `GET /pedidos/compras/{idPedidoCompra}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém um pedido de compra

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_pedido_compra` | `idPedidoCompra` | `path` | sim |

- Schemas de response: 200: PedidosComprasDadosBaseDTO/PedidosComprasDadosDTO, 404: ErrorResponse

### `alterar`

- Bling: `PUT /pedidos/compras/{idPedidoCompra}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera um pedido de compra

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_pedido_compra` | `idPedidoCompra` | `path` | sim |

- Schemas de request: `PedidosComprasDadosBaseDTO`, `PedidosComprasDadosDTO`
- Schemas de response: 200: BasePostResponse/PedidosCompraResponse_POST_PUT, 404: ErrorResponse, 400: ErrorResponse

### `estornar_contas`

- Bling: `POST /pedidos/compras/{idPedidoCompra}/estornar-contas`
- Ação oficial: `EstornarContas`
- Resumo oficial: Estorna as contas de um pedido de compra

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_pedido_compra` | `idPedidoCompra` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `estornar_estoque`

- Bling: `POST /pedidos/compras/{idPedidoCompra}/estornar-estoque`
- Ação oficial: `EstornarEstoque`
- Resumo oficial: Estorna o estoque de um pedido de compra

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_pedido_compra` | `idPedidoCompra` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `lancar_contas`

- Bling: `POST /pedidos/compras/{idPedidoCompra}/lancar-contas`
- Ação oficial: `LancarContas`
- Resumo oficial: Lança as contas de um pedido de compra

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_pedido_compra` | `idPedidoCompra` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `lancar_estoque`

- Bling: `POST /pedidos/compras/{idPedidoCompra}/lancar-estoque`
- Ação oficial: `LancarEstoque`
- Resumo oficial: Lança o estoque de um pedido de compra

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_pedido_compra` | `idPedidoCompra` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse

### `alterar_situacao`

- Bling: `PATCH /pedidos/compras/{idPedidoCompra}/situacoes/{idSituacao}`
- Ação oficial: `AlterarSituacao`
- Resumo oficial: Altera a situação de um pedido de compra

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_pedido_compra` | `idPedidoCompra` | `path` | sim |
| `id_situacao` | `idSituacao` | `path` | sim |

- Schemas de response: 404: ErrorResponse, 400: ErrorResponse
