"""Exemplos de leitura de vínculos entre produto e fornecedor."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.product_suppliers import (
    ProdutosFornecedoresGetResponse200,
    ProdutosFornecedoresIdProdutoFornecedorGetResponse200,
)


def main() -> None:
    """Lista vínculos e busca um registro pelo ID."""
    id_produto = 123456789  # Exemplo — substitua pelo ID real.
    id_produto_fornecedor = 987654321  # Exemplo — substitua pelo ID real.
    with BlingClient.from_env() as client:
        lista = client.produtos_fornecedores.listar(limite=10, id_produto=id_produto)
        parsed = ProdutosFornecedoresGetResponse200(**lista)  # type: ignore[reportArgumentType]
        print("listar:", parsed.model_dump_json(indent=2, by_alias=True))
        detail = client.produtos_fornecedores.obter(id_produto_fornecedor)
        parsed = ProdutosFornecedoresIdProdutoFornecedorGetResponse200(**detail)  # type: ignore[reportArgumentType]
        print("obter:", parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
