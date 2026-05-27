"""Exemplo que lista contas a receber usando o SDK."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.contas_receber import ContasReceberGetResponse200


def main() -> None:
    """Lista contas a receber com situações 'Em aberto' e 'Recebido'."""
    with BlingClient.from_env() as client:
        response = client.contas_receber.listar(situacoes=[1, 2])
        parsed = ContasReceberGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
