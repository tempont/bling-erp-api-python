"""Example: Get a single income/expense category."""

from bling_erp_api import BlingClient


def main() -> None:
    """Retrieve an income/expense category by ID."""
    with BlingClient.from_env() as client:
        response = client.income_expense_categories.obter(123456)
        print(response)


if __name__ == "__main__":
    main()
