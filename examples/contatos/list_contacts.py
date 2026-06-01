"""Exemplo que lista contatos usando o SDK."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.contacts import ContatosGetResponse200


def main() -> None:
    """Lista a primeira página de contatos."""
    with BlingClient.from_env() as client:
        response = client.contatos.listar(pesquisa="Ana", limite=10)
        parsed = ContatosGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
