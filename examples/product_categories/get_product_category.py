"""Example: Get a single product category."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.product_categories import (
    CategoriasProdutosIdCategoriaProdutoGetResponse200,
)


def main() -> None:
    """Retrieve a product category by ID."""
    with BlingClient.from_env() as client:
        response = client.product_categories.obter(123456)
        parsed = CategoriasProdutosIdCategoriaProdutoGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
