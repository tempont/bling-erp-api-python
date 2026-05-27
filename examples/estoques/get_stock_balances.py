"""Exemplo que obtém saldo em estoque de produtos usando o SDK."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.estoques import EstoquesSaldosGetResponse200


def main() -> None:
    """Obtém saldo em estoque de produtos."""
    with BlingClient.from_env() as client:
        response = client.estoques.obter_saldos(ids_produtos=[1, 2])
        parsed = EstoquesSaldosGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
