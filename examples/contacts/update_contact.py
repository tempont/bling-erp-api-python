"""Exemplo que atualiza um contato existente."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.contacts import ContatosIdContatoPutRequest

CONTATO_ID = 12345678


def main() -> None:
    """Altera dados de um contato por ``PUT``."""
    payload = ContatosIdContatoPutRequest.model_construct(
        id=0, nome="Nova Empresa LTDA - Matriz", situacao="A", tipo="J"
    )
    with BlingClient.from_env() as client:
        response = client.contatos.alterar(CONTATO_ID, payload)
        # NOTE: No success response model for PUT /contatos/{idContato} (only error responses in OpenAPI spec).
        print(response)


if __name__ == "__main__":
    main()
