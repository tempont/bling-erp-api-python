"""Exemplo que obtém saldo em estoque por depósito usando o SDK."""

from bling_erp_api import BlingClient


def main() -> None:
    """Obtém saldo em estoque de produtos pelo ID do depósito."""
    with BlingClient.from_env() as client:
        response = client.estoques.obter_saldos_por_deposito(1, ids_produtos=[1])
        print(response)


if __name__ == "__main__":
    main()
