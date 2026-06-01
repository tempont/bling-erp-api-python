"""Example: Vendedores (Sellers) workflow.

Demonstrates listing and retrieving sellers.

Endpoints:
    - GET /vendedores
    - GET /vendedores/{idVendedor}

Docs:
    - https://developer.bling.com.br/referencia#/Vendedores/get_vendedores
    - https://developer.bling.com.br/referencia#/Vendedores/get_vendedores__idVendedor_
"""

from __future__ import annotations

from bling_erp_api import BlingClient


def list_sellers():
    """List all sellers."""
    client = BlingClient.from_env()
    sellers = client.vendedores

    # List sellers with filters (seller.list also works)
    return sellers.listar(
        pagina=1,
        limite=100,
        situacao_contato="A",  # A = Ativo
    )


def get_seller(seller_id: int):
    """Get a specific seller by id."""
    client = BlingClient.from_env()
    return client.vendedores.obter(id_vendedor=seller_id)


if __name__ == "__main__":
    print("Listing sellers...")
    print(list_sellers().model_dump_json(indent=2, by_alias=True))

    seller_id: int | None = None

    if seller_id:
        print(get_seller(seller_id).model_dump_json(indent=2, by_alias=True))
