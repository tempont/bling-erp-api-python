"""Example: Get a single ad by ID."""

from bling_erp_api import BlingClient


def main() -> None:
    """Retrieve ad details by ID."""
    with BlingClient.from_env() as client:
        response = client.anuncios.obter(123456, tipo_integracao="MercadoLivre", id_loja=1)
        print(response)


if __name__ == "__main__":
    main()
