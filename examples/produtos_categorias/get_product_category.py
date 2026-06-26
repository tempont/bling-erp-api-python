"""Example: Get a single product category."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.product_categories import (
    CategoriasProdutosIdCategoriaProdutoGetResponse200,
)


def main() -> None:
    """Retrieve a product category by ID."""
    with BlingClient.from_env() as client:
        response = client.categorias_produtos.obter(id_categoria_produto=123456)
        parsed = CategoriasProdutosIdCategoriaProdutoGetResponse200.model_validate(response)
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
