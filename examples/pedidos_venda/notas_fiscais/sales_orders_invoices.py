"""Example: Sales Orders (Pedidos de Venda) — Invoice Generation.

Demonstrates generating NF-e and NFC-e from sales orders.

Endpoints:
    - POST /pedidos/vendas/{idPedidoVenda}/gerar-nfe
    - POST /pedidos/vendas/{idPedidoVenda}/gerar-nfce

Docs:
    - https://developer.bling.com.br/referencia#/Pedidos%20de%20Venda/post_pedidos_vendas__idPedidoVenda__gerar-nfe
    - https://developer.bling.com.br/referencia#/Pedidos%20de%20Venda/post_pedidos_vendas__idPedidoVenda__gerar-nfce
"""

from __future__ import annotations

from bling_erp_api import BlingClient

ID_PEDIDO_EXEMPLO = 12345678  # Exemplo — substitua pelo ID real.

## ---------------------------------------------------------------------------
## INVOICE GENERATION
## ---------------------------------------------------------------------------


def gerar_nota_fiscal_pedido(id_pedido_venda: int) -> None:
    """Gera uma NF-e a partir do pedido de venda."""
    with BlingClient.from_env() as client:
        client.pedidos_vendas.gerar_nota_fiscal(id_pedido_venda=id_pedido_venda)


def gerar_nota_fiscal_consumidor_pedido(id_pedido_venda: int) -> None:
    """Gera uma NFC-e a partir do pedido de venda."""
    with BlingClient.from_env() as client:
        client.pedidos_vendas.gerar_nota_fiscal_consumidor(id_pedido_venda=id_pedido_venda)


def main() -> None:
    """Demonstrate invoice generation for sales orders."""
    print("Invoice operations must be explicitly enabled.")

    # Invoice operations (commented out)
    # gerar_nota_fiscal_pedido(ID_PEDIDO_EXEMPLO)
    # time.sleep(1)
    # gerar_nota_fiscal_consumidor_pedido(ID_PEDIDO_EXEMPLO)
    # time.sleep(1)


if __name__ == "__main__":
    main()
