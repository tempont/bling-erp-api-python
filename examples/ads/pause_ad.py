"""Example: Pause an ad."""

from bling_erp_api import BlingClient


def main() -> None:
    """Pause an existing ad by ID."""
    with BlingClient.from_env() as client:
        response = client.anuncios.pausar(123456, tipo_integracao="MercadoLivre", id_loja=1)
        print(response)


if __name__ == "__main__":
    main()
