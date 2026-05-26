"""Example: List income/expense categories with type filter."""

from bling_erp_api import BlingClient


def main() -> None:
    """List income/expense categories filtered by type (2=Revenue)."""
    with BlingClient.from_env() as client:
        response = client.income_expense_categories.listar(tipo=2)
        print(response)


if __name__ == "__main__":
    main()
