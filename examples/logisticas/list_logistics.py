"""Example: List all logistics filtered by integration type."""

from bling_erp_api import BlingClient


def main() -> None:
    """List logistics filtered by Correios integration."""
    with BlingClient.from_env() as client:
        response = client.logisticas.listar(tipo_integracao="Correios")
        print(response)


if __name__ == "__main__":
    main()
