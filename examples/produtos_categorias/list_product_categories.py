"""Example: List product categories."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.product_categories import CategoriasProdutosGetResponse200


def main() -> None:
    """List product categories with pagination."""
    with BlingClient.from_env() as client:
        response = client.categorias_produtos.listar(limite=50)
        parsed = CategoriasProdutosGetResponse200.model_validate(response)
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
