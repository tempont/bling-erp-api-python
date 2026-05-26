"""Exemplo que altera a situação de vários contatos."""

from bling_erp_api import BlingClient


def main() -> None:
    """Atualiza situação em massa (ex.: ``I`` inativo)."""
    ids_contatos = [11111111, 22222222]
    with BlingClient.from_env() as client:
        response = client.contatos.alterar_situacao_varios(ids_contatos, "I")
        print(response)


if __name__ == "__main__":
    main()
