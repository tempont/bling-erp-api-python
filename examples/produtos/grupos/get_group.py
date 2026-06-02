"""Exemplo que obtém um grupo de produtos pelo ID usando o SDK."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.product_groups import GruposProdutosIdGrupoProdutoGetResponse200


def main() -> None:
    """Obtém um grupo de produtos pelo ID."""
    with BlingClient.from_env() as client:
        response = client.grupos_produtos.obter(100)
        parsed = GruposProdutosIdGrupoProdutoGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
