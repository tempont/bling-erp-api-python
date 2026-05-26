"""Exemplo que obtém um contato por ID."""

from bling_erp_api import BlingClient

CONTATO_ID = 12345678


def main() -> None:
    """Consulta um contato pelo ``id`` do Bling."""
    with BlingClient.from_env() as client:
        response = client.contatos.obter(CONTATO_ID)
        print(response)


if __name__ == "__main__":
    main()
