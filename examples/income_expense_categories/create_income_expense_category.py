"""Example: Create a new income/expense category."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.income_expense_categories import (
    CategoriasReceitasDespesasPostRequest,
    CategoriasReceitasDespesasPostResponse201,
)


def main() -> None:
    """Create a new revenue category."""
    # Model: CategoriasReceitasDespesasPostRequest  # noqa: ERA001
    #   Required: descricao (str), tipo (int)
    #   Optional: id (int|None), id_categoria_pai (int|None), grupo_dre (int|None)
    payload = CategoriasReceitasDespesasPostRequest(
        descricao="Consultoria", tipo=2, id_categoria_pai=0
    )
    with BlingClient.from_env() as client:
        response = client.income_expense_categories.criar(payload)
        parsed = CategoriasReceitasDespesasPostResponse201(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
