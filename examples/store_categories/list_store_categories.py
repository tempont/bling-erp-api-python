"""Example: List store categories."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.store_categories import CategoriasLojasGetResponse200


def main() -> None:
    """List store categories with store filter."""
    with BlingClient.from_env() as client:
        response = client.store_categories.listar(id_loja=1)
        parsed = CategoriasLojasGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
