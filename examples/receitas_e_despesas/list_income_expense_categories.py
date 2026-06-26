"""Example: List income/expense categories with type filter."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.income_expense_categories import (
    CategoriasReceitasDespesasGetResponse200,
)


def main() -> None:
    """List income/expense categories filtered by type (2=Revenue)."""
    with BlingClient.from_env() as client:
        response = client.categorias_receitas_despesas.listar(tipo=2)
        parsed = CategoriasReceitasDespesasGetResponse200.model_validate(response)
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
