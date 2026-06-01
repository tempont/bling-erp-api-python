"""Exemplo que lista todos os tipos de contato do Bling."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.contacts import ContatosTiposGetResponse200


def main() -> None:
    """Lista tipos disponíveis (cliente, fornecedor, etc.)."""
    with BlingClient.from_env() as client:
        response = client.contatos.listar_tipos()
        parsed = ContatosTiposGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
