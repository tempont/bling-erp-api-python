"""Exemplos de leitura de vínculos entre produto e loja."""

from bling_erp_api import BlingClient


def main() -> None:
    """Lista vínculos e busca um registro pelo ID."""
    id_produto = 123456789  # Exemplo — substitua pelo ID real.
    id_produto_loja = 987654321  # Exemplo — substitua pelo ID real.
    with BlingClient.from_env() as client:
        lista = client.produtos_lojas.listar(limite=10, id_produto=id_produto)
        print("listar:", lista)
        detail = client.produtos_lojas.obter(id_produto_loja)
        print("obter:", detail)


if __name__ == "__main__":
    main()
