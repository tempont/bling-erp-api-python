"""Exemplo que cria um contato."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.contacts import ContatosPostRequest, ContatosPostResponse201


def main() -> None:
    """Cria um contato simplificado."""
    payload = ContatosPostRequest.model_construct(
        id=0, nome="Nova Empresa LTDA", tipo="J", situacao="A"
    )
    with BlingClient.from_env() as client:
        response = client.contatos.criar(payload)
        parsed = ContatosPostResponse201(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
