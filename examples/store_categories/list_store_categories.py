"""Example: List store categories."""

from bling_erp_api import BlingClient


def main() -> None:
    """List store categories with store filter."""
    with BlingClient.from_env() as client:
        response = client.store_categories.listar(id_loja=1)
        print(response)


if __name__ == "__main__":
    main()
