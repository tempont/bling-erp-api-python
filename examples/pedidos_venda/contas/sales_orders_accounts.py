"""Example: Sales Orders (Pedidos de Venda) — Accounts Operations.

Demonstrates accounts receivable posting and reversal for sales orders.

Endpoints:
    - POST /pedidos/vendas/{idPedidoVenda}/lancar-contas
    - POST /pedidos/vendas/{idPedidoVenda}/estornar-contas

Docs:
    - https://developer.bling.com.br/referencia#/Pedidos%20-%20Vendas/post_pedidos_vendas__idPedidoVenda__lancar_contas
    - https://developer.bling.com.br/referencia#/Pedidos%20-%20Vendas/post_pedidos_vendas__idPedidoVenda__estornar_contas
"""

from __future__ import annotations

from bling_erp_api import BlingClient

ID_PEDIDO_EXEMPLO = 12345678  # Exemplo — substitua pelo ID real.

## ---------------------------------------------------------------------------
## ACCOUNTS OPERATIONS
## ---------------------------------------------------------------------------


def lancar_contas_pedido(id_pedido_venda: int) -> None:
    """Lança as contas a receber de um pedido de venda."""
    with BlingClient.from_env() as client:
        client.pedidos_vendas.lancar_contas(id_pedido_venda=id_pedido_venda)


def estornar_contas_pedido(id_pedido_venda: int) -> None:
    """Estorna as contas a receber de um pedido de venda."""
    with BlingClient.from_env() as client:
        client.pedidos_vendas.estornar_contas(id_pedido_venda=id_pedido_venda)


def main() -> None:
    """Demonstrate accounts operations for sales orders."""
    print("Accounts operations must be explicitly enabled.")

    # Accounts operations (commented out)
    # lancar_contas_pedido(ID_PEDIDO_EXEMPLO)
    # time.sleep(1)
    # estornar_contas_pedido(ID_PEDIDO_EXEMPLO)
    # time.sleep(1)


if __name__ == "__main__":
    main()
