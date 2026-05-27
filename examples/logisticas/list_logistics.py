"""Example: List all logistics filtered by integration type."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.logisticas import LogisticasGetResponse200


def main() -> None:
    """List logistics filtered by Correios integration."""
    with BlingClient.from_env() as client:
        response = client.logisticas.listar(tipo_integracao="Correios")
        parsed = LogisticasGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
