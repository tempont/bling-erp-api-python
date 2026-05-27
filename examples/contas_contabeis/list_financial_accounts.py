"""Exemplo que lista contas financeiras usando o SDK."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.contas_contabeis import ContasContabeisGetResponse200


def main() -> None:
    """Lista contas financeiras com situação 'Ativo'."""
    with BlingClient.from_env() as client:
        response = client.contas_contabeis.listar(situacoes=[1])
        parsed = ContasContabeisGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
