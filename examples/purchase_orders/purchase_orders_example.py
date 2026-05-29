"""Example: Pedidos de Compra (Purchase Orders) workflow.

Demonstrates listing, creating, retrieving, updating, and managing
purchase orders using both pt-BR canonical names and English aliases.

Usage:
    BLING_API_KEY="your_key" python examples/purchase_orders/purchase_orders_example.py
"""

from bling_erp_api import BlingClient


def main() -> None:
    """Run the purchase orders example workflow."""
    client = BlingClient.from_env()

    # Access the purchase orders resource
    # Canonical pt-BR name:
    pedidos = client.pedidos_compras
    # Or English alias: client.purchase_orders

    # 1. List purchase orders with filters
    print("Listing purchase orders...")
    result = pedidos.listar(
        pagina=1,
        limite=10,
        id_fornecedor=500,
        valor_situacao=0,  # 0 = Em aberto
        data_inicial="2024-01-01",
        data_final="2024-12-31",
    )
    print(f"Found purchase orders: {result}")

    # 2. Create a new purchase order (commented — requires valid data)
    # from bling_erp_api.models.generated.purchase_orders import PedidosComprasPostRequest
    # order = PedidosComprasPostRequest(
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
    # created = pedidos.criar(order)
    # print(f"Created purchase order: {created}")

    # 3. Get a specific purchase order
    # order = pedidos.obter(1001)
    # print(f"Order details: {order}")

    # 4. Update an existing purchase order
    # pedidos.alterar(1001, updated_data)

    # 5. Update order status
    # pedidos.alterar_situacao(1001, 1)  # 1 = Atendido

    # 6. Stock and account actions
    # pedidos.lancar_estoque(1001)
    # pedidos.estornar_estoque(1001)
    # pedidos.lancar_contas(1001)
    # pedidos.estornar_contas(1001)

    # 7. Delete a purchase order
    # pedidos.remover(1001)


if __name__ == "__main__":
    main()
