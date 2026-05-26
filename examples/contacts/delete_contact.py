"""Exemplo que remove um contato."""

from bling_erp_api import BlingClient

CONTATO_ID = 12345678


def main() -> None:
    """Remove um contato pelo ID."""
    with BlingClient.from_env() as client:
        response = client.contatos.remover(CONTATO_ID)
        print(response)


if __name__ == "__main__":
    main()
