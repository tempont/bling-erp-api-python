"""Exemplo que lista depósitos usando o SDK."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.depositos import DepositosGetResponse200


def main() -> None:
    """Lista depósitos com situação 'Ativo'."""
    with BlingClient.from_env() as client:
        response = client.depositos.listar(situacao=1)
        parsed = DepositosGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
