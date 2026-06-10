"""Example: Sales Orders (Pedidos de Venda) — Stock Operations.

Demonstrates stock posting and reversal for sales orders.

Endpoints:
    - POST /pedidos/vendas/{idPedidoVenda}/lancar-estoque
    - POST /pedidos/vendas/{idPedidoVenda}/lancar-estoque/{idDeposito}
    - POST /pedidos/vendas/{idPedidoVenda}/estornar-estoque

Docs:
    - https://developer.bling.com.br/referencia#/Pedidos%20-%20Vendas/post_pedidos_vendas__idPedidoVenda__lancar_estoque
    - https://developer.bling.com.br/referencia#/Pedidos%20-%20Vendas/post_pedidos_vendas__idPedidoVenda__lancar_estoque__idDeposito_
    - https://developer.bling.com.br/referencia#/Pedidos%20-%20Vendas/post_pedidos_vendas__idPedidoVenda__lancar_estoque
"""

from __future__ import annotations

from bling_erp_api import BlingClient

ID_PEDIDO_EXEMPLO = 12345678  # Exemplo — substitua pelo ID real.

## ---------------------------------------------------------------------------
## STOCK OPERATIONS
## ---------------------------------------------------------------------------


def lancar_estoque_pedido(id_pedido_venda: int, id_deposito: int | None = None) -> None:
    """Lança o estoque de um pedido de venda."""
    with BlingClient.from_env() as client:
        if id_deposito is not None:
            client.pedidos_vendas.lancar_estoque(
                id_pedido_venda=id_pedido_venda, id_deposito=id_deposito
            )
        else:
            client.pedidos_vendas.lancar_estoque(id_pedido_venda=id_pedido_venda)


def estornar_estoque_pedido(id_pedido_venda: int) -> None:
    """Estorna o estoque de um pedido de venda."""
    with BlingClient.from_env() as client:
        client.pedidos_vendas.estornar_estoque(id_pedido_venda=id_pedido_venda)


def main() -> None:
    """Demonstrate stock operations for sales orders."""
    print("Stock operations must be explicitly enabled.")

    # Stock operations (commented out)
    # lancar_estoque_pedido(ID_PEDIDO_EXEMPLO)
    # time.sleep(1)
    # estornar_estoque_pedido(ID_PEDIDO_EXEMPLO)
    # time.sleep(1)


if __name__ == "__main__":
    main()
