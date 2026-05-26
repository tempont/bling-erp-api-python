"""Exemplo que lista os tipos de contato vinculados a um contato."""

from bling_erp_api import BlingClient

CONTATO_ID = 12345678


def main() -> None:
    """Consulta tipos de contato de um cliente/fornecedor."""
    with BlingClient.from_env() as client:
        response = client.contatos.obter_tipo_contato(CONTATO_ID)
        print(response)


if __name__ == "__main__":
    main()
