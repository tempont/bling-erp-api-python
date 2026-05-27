"""Example: Get shipping labels for sales orders."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.logisticas import LogisticasEtiquetasGetResponse200


def main() -> None:
    """Retrieve shipping labels in PDF format for given sale IDs."""
    with BlingClient.from_env() as client:
        response = client.logisticas_etiquetas.obter(formato="PDF", ids_vendas=[1])
        parsed = LogisticasEtiquetasGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
