"""Exemplo que obtém saldo em estoque de produtos usando o SDK."""

from bling_erp_api import BlingClient


def main() -> None:
    """Obtém saldo em estoque de produtos."""
    with BlingClient.from_env() as client:
        response = client.estoques.obter_saldos(ids_produtos=[1, 2])
        print(response)


if __name__ == "__main__":
    main()
