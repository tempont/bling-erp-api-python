"""Exemplo que lista contas a receber usando o SDK."""

from bling_erp_api import BlingClient


def main() -> None:
    """Lista contas a receber com situações 'Em aberto' e 'Recebido'."""
    with BlingClient.from_env() as client:
        response = client.contas_receber.listar(situacoes=[1, 2])
        print(response)


if __name__ == "__main__":
    main()
