"""Example: Get a single store category binding."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.store_categories import (
    CategoriasLojasIdCategoriaLojaGetResponse200,
)


def main() -> None:
    """Retrieve a store category binding by ID."""
    with BlingClient.from_env() as client:
        response = client.store_categories.obter(123456)
        parsed = CategoriasLojasIdCategoriaLojaGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
