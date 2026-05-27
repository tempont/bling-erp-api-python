"""Example: Get a single logistics object by ID."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.logisticas import LogisticasObjetosIdObjetoGetResponse200


def main() -> None:
    """Retrieve a logistics object by ID."""
    with BlingClient.from_env() as client:
        response = client.logisticas_objetos.obter(1)
        parsed = LogisticasObjetosIdObjetoGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
