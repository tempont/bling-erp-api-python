"""Exemplos de leitura de vínculos entre produto e loja."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.product_stores import (
    ProdutosLojasGetResponse200,
    ProdutosLojasIdProdutoLojaGetResponse200,
)


def main() -> None:
    """Lista vínculos e busca um registro pelo ID."""
    id_produto = 123456789  # Exemplo — substitua pelo ID real.
    id_produto_loja = 987654321  # Exemplo — substitua pelo ID real.
    with BlingClient.from_env() as client:
        lista = client.produtos_lojas.listar(limite=10, id_produto=id_produto)
        parsed = ProdutosLojasGetResponse200(**lista)  # type: ignore[reportArgumentType]
        print("listar:", parsed.model_dump_json(indent=2, by_alias=True))
        detail = client.produtos_lojas.obter(id_produto_loja)
        parsed = ProdutosLojasIdProdutoLojaGetResponse200(**detail)  # type: ignore[reportArgumentType]
        print("obter:", parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
