"""Exemplo que lista grupos de produtos usando o SDK."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.product_groups import GruposProdutosGetResponse200


def main() -> None:
    """Lista grupos de produtos."""
    with BlingClient.from_env() as client:
        response = client.grupos_produtos.listar()
        parsed = GruposProdutosGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
