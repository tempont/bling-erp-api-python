"""Example: Create a new ad."""

from bling_erp_api import BlingClient
from bling_erp_api.types import JsonObject


def main() -> None:
    """Create a new ad with product and integration info."""
    payload: JsonObject = {
        "produto": {"id": 12345},
        "integracao": {"tipo": "MercadoLivre"},
        "loja": {"id": 1},
        "nome": "Meu Anúncio de Teste",
    }
    with BlingClient.from_env() as client:
        response = client.anuncios.criar(payload)
        print(response)


if __name__ == "__main__":
    main()
