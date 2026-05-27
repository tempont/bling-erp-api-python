"""Example: Get shipping labels for sales orders."""

from bling_erp_api import BlingClient


def main() -> None:
    """Retrieve shipping labels in PDF format for given sale IDs."""
    with BlingClient.from_env() as client:
        response = client.logisticas_etiquetas.obter(formato="PDF", ids_vendas=[1])
        print(response)


if __name__ == "__main__":
    main()
