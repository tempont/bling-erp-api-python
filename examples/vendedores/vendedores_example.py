"""Example: Vendedores (Sellers) workflow.

Demonstrates listing and retrieving sellers.

Usage:
    BLING_API_KEY="your_key" python examples/vendedores/vendedores_example.py
"""

from __future__ import annotations

from bling_erp_api import BlingClient


def main() -> None:
    """Run the sellers example."""
    client = BlingClient.from_env()

    # client.vendedores / client sellers
    vendors = client.vendedores

    # List sellers with filters
    result = vendors.listar(
        pagina=1,
        limite=10,
        situacao_contato="A",  # A = Ativo
    )
    print(f"Sellers: {result}")

    # Get a specific seller
    # seller = vendedores.obter(12345678)
    # print(f"Seller: {seller}")


if __name__ == "__main__":
    main()
