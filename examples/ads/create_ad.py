"""Example: Create a new ad."""

from bling_erp_api import BlingClient
from bling_erp_api.types import JsonObject

PRODUCT_ID: int | None = None


def main() -> None:
    """Create a new ad with product and integration info."""
    if PRODUCT_ID is None:
        msg = "PRODUCT_ID is required"
        raise ValueError(msg)

    payload: JsonObject = {
        "produto": {"id": PRODUCT_ID},
        "integracao": {"tipo": "MercadoLivre"},
        "loja": {"id": 1},
        "nome": "Meu Anúncio de Teste",
    }
    with BlingClient.from_env() as client:
        response = client.anuncios.criar(payload)
        print(response)


if __name__ == "__main__":
    main()
