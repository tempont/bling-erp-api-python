"""Exemplo que obtém um contato por ID."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.contacts import ContatosIdContatoGetResponse200

CONTATO_ID = 12345678


def main() -> None:
    """Consulta um contato pelo ``id`` do Bling."""
    with BlingClient.from_env() as client:
        response = client.contatos.obter(CONTATO_ID)
        contact = ContatosIdContatoGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(contact.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
