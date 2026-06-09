"""Example: Sales Orders (Pedidos de Venda) — CRUD Operations.

Demonstrates listing, creating, retrieving, updating, and managing sales orders
through the Bling pedidos de venda API.

Endpoints:
    - GET /pedidos/vendas
    - GET /pedidos/vendas/{idPedidoVenda}
    - POST /pedidos/vendas
    - PUT /pedidos/vendas/{idPedidoVenda}
    - PATCH /pedidos/vendas/{idPedidoVenda}/situacoes/{idSituacao}
    - DELETE /pedidos/vendas/{idPedidoVenda}
    - DELETE /pedidos/vendas

Docs:
    - https://developer.bling.com.br/referencia#/Pedidos%20de%20Venda/get_pedidos_vendas
    - https://developer.bling.com.br/referencia#/Pedidos%20de%20Venda/get_pedidos_vendas__idPedidoVenda_
    - https://developer.bling.com.br/referencia#/Pedidos%20de%20Venda/post_pedidos_vendas
    - https://developer.bling.com.br/referencia#/Pedidos%20de%20Venda/put_pedidos_vendas__idPedidoVenda_
    - https://developer.bling.com.br/referencia#/Pedidos%20de%20Venda/patch_pedidos_vendas__idPedidoVenda__situacoes__idSituacao_
    - https://developer.bling.com.br/referencia#/Pedidos%20de%20Venda/delete_pedidos_vendas__idPedidoVenda_
    - https://developer.bling.com.br/referencia#/Pedidos%20de%20Venda/delete_pedidos_vendas
"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from collections.abc import Sequence

    from bling_erp_api.models.generated.sales_orders import (
        PedidosVendasGetResponse200,
        PedidosVendasIdPedidoVendaGetResponse200,
        PedidosVendasIdPedidoVendaPutRequest,
        PedidosVendasPostRequest,
    )

ID_PEDIDO_EXEMPLO = 12345678  # Exemplo — substitua pelo ID real.

## ---------------------------------------------------------------------------
## LIST SALES ORDERS
## ---------------------------------------------------------------------------


def listar_pedidos() -> PedidosVendasGetResponse200:
    """Lista pedidos de venda com filtros."""
    with BlingClient.from_env() as client:
        return client.pedidos_vendas.listar(pagina=1, limite=10, ids_situacoes=[9])  # type: ignore[return-type]


def iterar_pedidos() -> list[dict[str, object]]:
    """Itera automaticamente sobre todos os pedidos de venda."""
    with BlingClient.from_env() as client:
        return list(client.pedidos_vendas.iterar(limite=10))  # type: ignore[return-type]


## ---------------------------------------------------------------------------
## GET SALES ORDER BY ID
## ---------------------------------------------------------------------------


def obter_pedido(id_pedido_venda: int) -> PedidosVendasIdPedidoVendaGetResponse200:
    """Obtém um pedido de venda pelo ID."""
    with BlingClient.from_env() as client:
        return client.pedidos_vendas.obter(id_pedido_venda=id_pedido_venda)  # type: ignore[return-type]


## ---------------------------------------------------------------------------
## CREATE SALES ORDER
## ---------------------------------------------------------------------------


def criar_pedido(dados: PedidosVendasPostRequest) -> None:
    """Cria um novo pedido de venda."""
    with BlingClient.from_env() as client:
        client.pedidos_vendas.criar(dados=dados)


## ---------------------------------------------------------------------------
## UPDATE SALES ORDER
## ---------------------------------------------------------------------------


def alterar_pedido(id_pedido_venda: int, dados: PedidosVendasIdPedidoVendaPutRequest) -> None:
    """Atualiza um pedido de venda (PUT)."""
    with BlingClient.from_env() as client:
        client.pedidos_vendas.alterar(id_pedido_venda=id_pedido_venda, dados=dados)


## ---------------------------------------------------------------------------
## UPDATE SALES ORDER STATUS
## ---------------------------------------------------------------------------


def alterar_situacao_pedido(id_pedido_venda: int, id_situacao: int) -> None:
    """Altera a situação de um pedido de venda."""
    with BlingClient.from_env() as client:
        client.pedidos_vendas.alterar_situacao(
            id_pedido_venda=id_pedido_venda, id_situacao=id_situacao
        )


## ---------------------------------------------------------------------------
## DELETE SALES ORDER(S)
## ---------------------------------------------------------------------------


def remover_pedido(id_pedido_venda: int) -> None:
    """Remove um pedido de venda pelo ID."""
    with BlingClient.from_env() as client:
        client.pedidos_vendas.remover(id_pedido_venda=id_pedido_venda)


def remover_pedidos_varios(ids_pedidos_vendas: Sequence[int]) -> None:
    """Remove múltiplos pedidos de venda."""
    with BlingClient.from_env() as client:
        client.pedidos_vendas.remover_varios(ids_pedidos_vendas=ids_pedidos_vendas)


def main() -> None:
    """Demonstrate sales order operations."""
    # Read operations
    print(listar_pedidos().model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    print(obter_pedido(ID_PEDIDO_EXEMPLO).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    print(iterar_pedidos())
    time.sleep(1)

    # Write operations (commented out)
    # order_data = PedidosVendasPostRequest(
    #     contato={"id": 123, "nome": "Cliente Exemplo"},
    #     itens=[
    #         {
    #             "codigo": "SKU-001",
    #             "descricao": "Produto A",
    #             "unidade": "UN",
    #             "quantidade": 2,
    #             "valor": 50.0,
    #         }
    #     ],
    #     parcelas=[
    #         {
    #             "dataVencimento": "2024-07-01",
    #             "valor": 100.0,
    #             "formaPagamento": {"id": 1},
    #         }
    #     ],
    # )
    # criar_pedido(order_data)
    # time.sleep(1)
    # alterar_pedido(
    #     ID_PEDIDO_EXEMPLO,
    #     PedidosVendasIdPedidoVendaPutRequest(
    #         itens=[
    #             {
    #                 "codigo": "SKU-001",
    #                 "descricao": "Produto B",
    #                 "unidade": "UN",
    #                 "quantidade": 1,
    #                 "valor": 50.0,
    #             }
    #         ]
    #     ),
    # )
    # time.sleep(1)
    # alterar_situacao_pedido(ID_PEDIDO_EXEMPLO, 9)
    # time.sleep(1)
    # remover_pedido(ID_PEDIDO_EXEMPLO)
    # time.sleep(1)
    # remover_pedidos_varios([ID_PEDIDO_EXEMPLO])
    # time.sleep(1)


if __name__ == "__main__":
    main()
