"""Example: Get a single bordero by ID."""

from bling_erp_api import BlingClient


def main() -> None:
    """Retrieve bordero details by ID."""
    with BlingClient.from_env() as client:
        response = client.borderos.obter(123456)
        print(response)


if __name__ == "__main__":
    main()
