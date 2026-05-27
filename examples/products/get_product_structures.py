"""Exemplo de leitura de estrutura (composição) de produto."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.product_structures import (
    ProdutosEstruturasIdProdutoEstruturaGetResponse200,
)


def main() -> None:
    """Consulta estrutura por ``idProdutoEstrutura``."""
    id_produto_estrutura = 123456789  # Exemplo — substitua pelo ID real do ambiente.
    with BlingClient.from_env() as client:
        response = client.produtos_estruturas.obter(id_produto_estrutura=id_produto_estrutura)
        parsed = ProdutosEstruturasIdProdutoEstruturaGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
