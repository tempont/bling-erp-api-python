"""Exemplo que obtém o contato padrão Consumidor Final."""

from bling_erp_api import BlingClient


def main() -> None:
    """Consulta o contato de consumidor final do sistema."""
    with BlingClient.from_env() as client:
        response = client.contatos.obter_consumidor_final()
        print(response)


if __name__ == "__main__":
    main()
