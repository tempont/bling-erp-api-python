"""Exemplos de leitura de vínculos entre produto e fornecedor."""

from bling_erp_api import BlingClient


def main() -> None:
    """Lista vínculos e busca um registro pelo ID."""
    id_produto = 123456789  # Exemplo — substitua pelo ID real.
    id_produto_fornecedor = 987654321  # Exemplo — substitua pelo ID real.
    with BlingClient.from_env() as client:
        lista = client.produtos_fornecedores.listar(limite=10, id_produto=id_produto)
        print("listar:", lista)
        detail = client.produtos_fornecedores.obter(id_produto_fornecedor)
        print("obter:", detail)


if __name__ == "__main__":
    main()
