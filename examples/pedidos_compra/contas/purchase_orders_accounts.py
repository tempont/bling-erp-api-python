"""Example: Purchase Orders (Pedidos de Compra) — Accounts Operations.

Demonstrates accounts payable posting and reversal for purchase orders.

Endpoints:
    - POST /pedidos/compras/{idPedidoCompra}/lancar-contas
    - POST /pedidos/compras/{idPedidoCompra}/estornar-contas

Docs:
    - https://developer.bling.com.br/referencia#/Pedidos%20-%20Compras/post_pedidos_compras__idPedidoCompra__lancar_contas
    - https://developer.bling.com.br/referencia#/Pedidos%20-%20Compras/post_pedidos_compras__idPedidoCompra__estornar_contas
"""

from __future__ import annotations

from bling_erp_api import BlingClient

ID_PEDIDO_EXEMPLO = 12345678  # Exemplo — substitua pelo ID real.

## ---------------------------------------------------------------------------
## ACCOUNTS OPERATIONS
## ---------------------------------------------------------------------------


def lancar_contas_pedido_compra(id_pedido_compra: int) -> None:
    """Lança as contas a pagar de um pedido de compra."""
    with BlingClient.from_env() as client:
        client.pedidos_compras.lancar_contas(id_pedido_compra=id_pedido_compra)


def estornar_contas_pedido_compra(id_pedido_compra: int) -> None:
    """Estorna as contas a pagar de um pedido de compra."""
    with BlingClient.from_env() as client:
        client.pedidos_compras.estornar_contas(id_pedido_compra=id_pedido_compra)


def main() -> None:
    """Demonstrate accounts operations for purchase orders."""
    print("Accounts operations must be explicitly enabled.")

    # Accounts operations (commented out)
    # lancar_contas_pedido_compra(ID_PEDIDO_EXEMPLO)
    # time.sleep(1)
    # estornar_contas_pedido_compra(ID_PEDIDO_EXEMPLO)
    # time.sleep(1)


if __name__ == "__main__":
    main()
