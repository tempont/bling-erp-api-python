"""Exemplo que altera a situação de um contato."""

from bling_erp_api import BlingClient

CONTATO_ID = 12345678


def main() -> None:
    """Define situação ``A`` (ativo) para o contato informado."""
    with BlingClient.from_env() as client:
        response = client.contatos.alterar_situacao(CONTATO_ID, "A")
        print(response)


if __name__ == "__main__":
    main()
