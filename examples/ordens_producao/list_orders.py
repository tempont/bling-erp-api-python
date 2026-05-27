"""Example: List production orders filtered by status."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.ordens_producao import OrdensProducaoGetResponse200


def main() -> None:
    """List open production orders."""
    with BlingClient.from_env() as client:
        response = client.ordens_producao.listar(ids_situacoes=[1])
        parsed = OrdensProducaoGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
