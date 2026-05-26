"""Exemplo que lista todos os tipos de contato do Bling."""

from bling_erp_api import BlingClient


def main() -> None:
    """Lista tipos disponíveis (cliente, fornecedor, etc.)."""
    with BlingClient.from_env() as client:
        response = client.contatos.listar_tipos()
        print(response)


if __name__ == "__main__":
    main()
