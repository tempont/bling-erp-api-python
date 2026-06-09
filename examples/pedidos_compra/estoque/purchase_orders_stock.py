"""Example: Purchase Orders (Pedidos de Compra) — Stock Operations.

Demonstrates stock posting and reversal for purchase orders.

Endpoints:
    - POST /pedidos/compras/{idPedidoCompra}/lancar-estoque
    - POST /pedidos/compras/{idPedidoCompra}/estornar-estoque

Docs:
    - https://developer.bling.com.br/referencia#/Pedidos%20-%20Compras/post_pedidos_compras__idPedidoCompra__lancar_estoque
    - https://developer.bling.com.br/referencia#/Pedidos%20-%20Compras/post_pedidos_compras__idPedidoCompra__estornar_estoque
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject

ID_PEDIDO_EXEMPLO = 12345678  # Exemplo — substitua pelo ID real.


## ---------------------------------------------------------------------------
## STOCK OPERATIONS
## ---------------------------------------------------------------------------


def lancar_estoque_pedido_compra(id_pedido_compra: int) -> JsonObject:
    """Lança o estoque de um pedido de compra."""
    with BlingClient.from_env() as client:
        return client.pedidos_compras.lancar_estoque(id_pedido_compra=id_pedido_compra)


def estornar_estoque_pedido_compra(id_pedido_compra: int) -> JsonObject:
    """Estorna o estoque de um pedido de compra."""
    with BlingClient.from_env() as client:
        return client.pedidos_compras.estornar_estoque(id_pedido_compra=id_pedido_compra)


def main() -> None:
    """Demonstrate stock operations for purchase orders."""
    print("Stock operations must be explicitly enabled.")

    # Stock operations (commented out)
    # lancar_estoque_pedido_compra(ID_PEDIDO_EXEMPLO)
    # time.sleep(1)
    # estornar_estoque_pedido_compra(ID_PEDIDO_EXEMPLO)
    # time.sleep(1)


if __name__ == "__main__":
    main()
