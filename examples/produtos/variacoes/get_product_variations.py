"""Exemplo de leitura de variações de um produto pai."""

from bling_erp_api import BlingClient


def main() -> None:
    """Obtém o produto pai e variações associadas."""
    id_produto_pai = 123456789  # Exemplo — substitua pelo ID real.
    with BlingClient.from_env() as client:
        response = client.produtos_variacoes.listar(id_produto_pai=id_produto_pai)
        print(response.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
