"""Exemplo que obtém o produto da homologação usando o SDK."""

from bling_erp_api import BlingClient


def main() -> None:
    """Obtém o produto da homologação."""
    with BlingClient.from_env() as client:
        response = client.homologacao.obter()
        print(response)


if __name__ == "__main__":
    main()
