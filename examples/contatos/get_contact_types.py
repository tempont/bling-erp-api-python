"""Exemplo que lista os tipos de contato vinculados a um contato."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.contacts import ContatosIdContatoTiposGetResponse200

CONTATO_ID = 12345678


def main() -> None:
    """Consulta tipos de contato de um cliente/fornecedor."""
    with BlingClient.from_env() as client:
        response = client.contatos.obter_tipo_contato(CONTATO_ID)
        parsed = ContatosIdContatoTiposGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
