"""Exemplo que lista contas a pagar usando o SDK."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.contas_pagar import ContasPagarGetResponse200


def main() -> None:
    """Lista contas a pagar com situação 'Em aberto'."""
    with BlingClient.from_env() as client:
        response = client.contas_pagar.listar(situacao=1)
        parsed = ContasPagarGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
