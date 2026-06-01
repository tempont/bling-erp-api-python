"""Exemplo que remove um contato."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.contacts import ContatosDeleteResponse200

CONTATO_ID = 12345678


def main() -> None:
    """Remove um contato pelo ID."""
    with BlingClient.from_env() as client:
        response = client.contatos.remover(CONTATO_ID)
        parsed = ContatosDeleteResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
