"""Exemplo que remove vários contatos de uma vez."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.contacts import ContatosDeleteResponse200


def main() -> None:
    """Remove múltiplos contatos informando os IDs."""
    ids_contatos = [11111111, 22222222]
    with BlingClient.from_env() as client:
        response = client.contatos.remover_varios(ids_contatos)
        parsed = ContatosDeleteResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
