"""Example: Get a single logistics object by ID."""

from bling_erp_api import BlingClient


def main() -> None:
    """Retrieve a logistics object by ID."""
    with BlingClient.from_env() as client:
        response = client.logisticas_objetos.obter(1)
        print(response)


if __name__ == "__main__":
    main()
