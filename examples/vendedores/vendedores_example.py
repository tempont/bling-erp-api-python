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

    # pt-BR canonical: client.vendedores
    # EN alias: client.sellers
    vendedores = client.vendedores

    # List sellers with filters
    result = vendedores.listar(
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
