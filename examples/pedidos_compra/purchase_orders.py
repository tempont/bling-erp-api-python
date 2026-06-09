"""Example: Purchase Orders (Pedidos de Compra) — CRUD Operations.

Demonstrates listing, creating, retrieving, updating, and managing purchase orders
through the Bling pedidos de compra API.

Endpoints:
    - GET /pedidos/compras
    - GET /pedidos/compras/{idPedidoCompra}
    - POST /pedidos/compras
    - PUT /pedidos/compras/{idPedidoCompra}
    - PATCH /pedidos/compras/{idPedidoCompra}/situacoes/{idSituacao}
    - DELETE /pedidos/compras/{idPedidoCompra}

Docs:
    - https://developer.bling.com.br/referencia#/Pedidos%20-%20Compras/get_pedidos_compras
    - https://developer.bling.com.br/referencia#/Pedidos%20-%20Compras/get_pedidos_compras__idPedidoCompra_
    - https://developer.bling.com.br/referencia#/Pedidos%20-%20Compras/post_pedidos_compras
    - https://developer.bling.com.br/referencia#/Pedidos%20-%20Compras/put_pedidos_compras__idPedidoCompra_
    - https://developer.bling.com.br/referencia#/Pedidos%20-%20Compras/patch_pedidos_compras__idPedidoCompra__situacoes__idSituacao_
    - https://developer.bling.com.br/referencia#/Pedidos%20-%20Compras/delete_pedidos_compras__idPedidoCompra_
"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.purchase_orders import (
        PedidosComprasIdPedidoCompraPutRequest,
        PedidosComprasPostRequest,
    )
    from bling_erp_api.types import JsonObject

ID_PEDIDO_EXEMPLO = 12345678  # Exemplo — substitua pelo ID real.

## ---------------------------------------------------------------------------
## LIST PURCHASE ORDERS
## ---------------------------------------------------------------------------


def listar_pedidos_compra() -> JsonObject:
    """Lista pedidos de compra com filtros."""
    with BlingClient.from_env() as client:
        return client.pedidos_compras.listar(
            pagina=1,
            limite=10,
            id_fornecedor=500,
            valor_situacao=0,
            data_inicial="2024-01-01",
            data_final="2024-12-31",
        )


def iterar_pedidos_compra() -> list[dict[str, object]]:
    """Itera automaticamente sobre todos os pedidos de compra."""
    with BlingClient.from_env() as client:
        return list(client.pedidos_compras.iterar(limite=10))  # type: ignore[return-type]


## ---------------------------------------------------------------------------
## GET PURCHASE ORDER BY ID
## ---------------------------------------------------------------------------


def obter_pedido_compra(id_pedido_compra: int) -> JsonObject:
    """Obtém um pedido de compra pelo ID."""
    with BlingClient.from_env() as client:
        return client.pedidos_compras.obter(id_pedido_compra=id_pedido_compra)


## ---------------------------------------------------------------------------
## CREATE PURCHASE ORDER
## ---------------------------------------------------------------------------


def criar_pedido_compra(dados: PedidosComprasPostRequest) -> JsonObject:
    """Cria um novo pedido de compra."""
    with BlingClient.from_env() as client:
        return client.pedidos_compras.criar(dados=dados)


## ---------------------------------------------------------------------------
## UPDATE PURCHASE ORDER
## ---------------------------------------------------------------------------


def alterar_pedido_compra(
    id_pedido_compra: int, dados: PedidosComprasIdPedidoCompraPutRequest
) -> JsonObject:
    """Atualiza um pedido de compra (PUT)."""
    with BlingClient.from_env() as client:
        return client.pedidos_compras.alterar(id_pedido_compra=id_pedido_compra, dados=dados)


## ---------------------------------------------------------------------------
## UPDATE PURCHASE ORDER STATUS
## ---------------------------------------------------------------------------


def alterar_situacao_pedido_compra(id_pedido_compra: int, id_situacao: int) -> JsonObject:
    """Altera a situação de um pedido de compra."""
    with BlingClient.from_env() as client:
        return client.pedidos_compras.alterar_situacao(
            id_pedido_compra=id_pedido_compra, id_situacao=id_situacao
        )


## ---------------------------------------------------------------------------
## DELETE PURCHASE ORDER
## ---------------------------------------------------------------------------


def remover_pedido_compra(id_pedido_compra: int) -> JsonObject:
    """Remove um pedido de compra pelo ID."""
    with BlingClient.from_env() as client:
        return client.pedidos_compras.remover(id_pedido_compra=id_pedido_compra)


def main() -> None:
    """Demonstrate purchase order operations."""
    # Read operations
    print(listar_pedidos_compra())
    time.sleep(1)

    print(obter_pedido_compra(ID_PEDIDO_EXEMPLO))
    time.sleep(1)

    print(iterar_pedidos_compra())
    time.sleep(1)

    # Write operations (commented out)
    # order_data = PedidosComprasPostRequest(
    #     fornecedor={"id": 500},
    #     itens=[
    #         {
    #             "descricao": "Matéria-prima A",
    #             "codigoFornecedor": "MP-A-001",
    #             "unidade": "KG",
    #             "valor": 750.00,
    #             "quantidade": 10,
    #         }
    #     ],
    #     parcelas=[
    #         {
    #             "dataVencimento": "2024-05-15",
    #             "valor": 7500.00,
    #             "formaPagamento": {"id": 1},
    #         }
    #     ],
    # )
    # print(criar_pedido_compra(order_data))
    # time.sleep(1)
    # alterar_pedido_compra(
    #     ID_PEDIDO_EXEMPLO,
    #     PedidosComprasIdPedidoCompraPutRequest(
    #         itens=[
    #             {
    #                 "descricao": "Matéria-prima B",
    #                 "codigoFornecedor": "MP-B-001",
    #                 "unidade": "KG",
    #                 "valor": 800.00,
    #                 "quantidade": 5,
    #             }
    #         ]
    #     ),
    # )
    # time.sleep(1)
    # alterar_situacao_pedido_compra(ID_PEDIDO_EXEMPLO, 1)  # 1 = Atendido
    # time.sleep(1)
    # remover_pedido_compra(ID_PEDIDO_EXEMPLO)
    # time.sleep(1)


if __name__ == "__main__":
    main()
