"""Exemplo que lista contas financeiras usando o SDK."""

from bling_erp_api import BlingClient


def main() -> None:
    """Lista contas financeiras com situação 'Ativo'."""
    with BlingClient.from_env() as client:
        response = client.contas_contabeis.listar(situacoes=[1])
        print(response)


if __name__ == "__main__":
    main()
