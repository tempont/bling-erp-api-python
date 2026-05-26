"""Example: Create a new income/expense category."""

from bling_erp_api import BlingClient
from bling_erp_api.types import JsonObject


def main() -> None:
    """Create a new revenue category."""
    payload: JsonObject = {
        "descricao": "Consultoria",
        "tipo": 2,
        "idCategoriaPai": 0,
    }
    with BlingClient.from_env() as client:
        response = client.income_expense_categories.criar(payload)
        print(response)


if __name__ == "__main__":
    main()
