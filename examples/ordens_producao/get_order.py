"""Example: Get a single production order by ID."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.ordens_producao import (
    OrdensProducaoIdOrdemProducaoGetResponse200,
)


def main() -> None:
    """Retrieve production order details by ID."""
    with BlingClient.from_env() as client:
        response = client.ordens_producao.obter(12345678)
        parsed = OrdensProducaoIdOrdemProducaoGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
