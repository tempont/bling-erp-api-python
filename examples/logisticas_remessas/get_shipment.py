"""Example: Get a single shipment (remessa) by ID."""

from bling_erp_api import BlingClient


def main() -> None:
    """Retrieve shipment details by ID."""
    with BlingClient.from_env() as client:
        response = client.logisticas_remessas.obter(501)
        print(response)


if __name__ == "__main__":
    main()
