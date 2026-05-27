"""Example: Get a single logistics entry by ID."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.logisticas import LogisticasIdLogisticaGetResponse200


def main() -> None:
    """Retrieve logistics details by ID."""
    with BlingClient.from_env() as client:
        response = client.logisticas.obter(101)
        parsed = LogisticasIdLogisticaGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
