"""Exemplo que obtém saldo em estoque por depósito usando o SDK."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.estoques import EstoquesSaldosIdDepositoGetResponse200


def main() -> None:
    """Obtém saldo em estoque de produtos pelo ID do depósito."""
    with BlingClient.from_env() as client:
        response = client.estoques.obter_saldos_por_deposito(1, ids_produtos=[1])
        parsed = EstoquesSaldosIdDepositoGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
