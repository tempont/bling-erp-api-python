"""Example: Pedidos de Venda (Sales Orders) workflow.

Demonstrates listing, creating, retrieving, and updating sales orders
using both pt-BR canonical names and English aliases.

Usage:
    BLING_API_KEY="your_key" python examples/sales_orders/sales_orders_example.py
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject


def main() -> None:
    """Run the sales orders example workflow."""
    client = BlingClient.from_env()

    # Access the sales orders resource
    # Canonical pt-BR name:
    pedidos = client.pedidos_vendas
    # Or English alias: client.sales_orders

    # 1. List sales orders with filters
    print("Listing sales orders...")
    result: JsonObject = pedidos.listar(
        pagina=1,
        limite=10,
        data_inicial="2024-01-01",
        data_final="2024-12-31",
        ids_situacoes=[9],  # 9 = Atendido
    )
    print(f"Found sales orders: {result}")

    # 2. Create a new sales order (commented — requires valid data)
    # from bling_erp_api.models.generated.sales_orders import PedidosVendasPostRequest
    # order = PedidosVendasPostRequest(
    #     contato={"id": 123, "nome": "Cliente Exemplo"},
    #     itens=[
    #         {
    #             "codigo": "SKU-001",
    #             "descricao": "Product A",
    #             "unidade": "UN",
    #             "quantidade": 2,
    #             "valor": 50.00,
    #         }
    #     ],
    #     parcelas=[
    #         {
    #             "dataVencimento": "2024-07-01",
    #             "valor": 100.00,
    #             "formaPagamento": {"id": 1},
    #         }
    #     ],
    # )
    # created = pedidos.criar(order)
    # print(f"Created order: {created}")

    # 3. Get a specific sales order
    # order = pedidos.obter(12345678)
    # print(f"Order details: {order}")

    # 4. Update an existing sales order
    # pedidos.alterar(12345678, order_data)

    # 5. Update order status
    # pedidos.alterar_situacao(12345678, 9)  # Mark as attended

    # 6. Stock and account actions
    # pedidos.lancar_estoque(12345678)
    # pedidos.estornar_estoque(12345678)
    # pedidos.lancar_contas(12345678)
    # pedidos.estornar_contas(12345678)

    # 7. Generate invoices from the order
    # pedidos.gerar_nota_fiscal(12345678)
    # pedidos.gerar_nota_fiscal_consumidor(12345678)

    # 8. Delete orders
    # pedidos.remover(12345678)
    # pedidos.remover_varios([1, 2, 3])


if __name__ == "__main__":
    main()
