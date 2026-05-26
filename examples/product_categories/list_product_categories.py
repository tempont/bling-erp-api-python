"""Example: List product categories."""

from bling_erp_api import BlingClient


def main() -> None:
    """List product categories with pagination."""
    with BlingClient.from_env() as client:
        response = client.product_categories.listar(limite=50)
        print(response)


if __name__ == "__main__":
    main()
