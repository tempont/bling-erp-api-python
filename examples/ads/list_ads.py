"""Example: List ads with filters."""

from bling_erp_api import BlingClient


def main() -> None:
    """List ads with integration type and store filters."""
    with BlingClient.from_env() as client:
        response = client.anuncios.listar(
            tipo_integracao="MercadoLivre",
            id_loja=1,
            situacao=1,
            limite=10,
        )
        print(response)


if __name__ == "__main__":
    main()
