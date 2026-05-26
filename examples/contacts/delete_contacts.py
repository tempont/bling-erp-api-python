"""Exemplo que remove vários contatos de uma vez."""

from bling_erp_api import BlingClient


def main() -> None:
    """Remove múltiplos contatos informando os IDs."""
    ids_contatos = [11111111, 22222222]
    with BlingClient.from_env() as client:
        response = client.contatos.remover_varios(ids_contatos)
        print(response)


if __name__ == "__main__":
    main()
