"""Example: List all logistics services."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.logisticas import LogisticasServicosGetResponse200


def main() -> None:
    """List logistics services with default pagination."""
    with BlingClient.from_env() as client:
        response = client.logisticas_servicos.listar()
        parsed = LogisticasServicosGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
