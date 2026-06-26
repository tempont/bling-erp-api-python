"""Example: Get a single income/expense category."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.income_expense_categories import (
    CategoriasReceitasDespesasIdCategoriaGetResponse200,
)


def main() -> None:
    """Retrieve an income/expense category by ID."""
    with BlingClient.from_env() as client:
        response = client.categorias_receitas_despesas.obter(id_categoria=123456)
        parsed = CategoriasReceitasDespesasIdCategoriaGetResponse200.model_validate(response)
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
