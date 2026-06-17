"""Example: Get Homologation Products.

Demonstrates retrieving homologation products from the Bling API.

Endpoint:
    - GET /homologacao/produtos

Docs:
    - https://developer.bling.com.br/referencia#/Homologa%C3%A7%C3%A3o/get_homologacao_produtos

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.homologation import (
        HomologacaoProdutosGetResponse200,
    )


def obter_produtos_homologacao() -> HomologacaoProdutosGetResponse200:
    """Obtém os produtos de homologação.

    Endpoint: GET /homologacao/produtos

    Obtém a lista de produtos cadastrados para homologação na API do Bling.

    Returns:
        Bling API response. Response schemas: 200: HomologacaoProdutosGetResponse200
    """
    with BlingClient.from_env() as client:
        return client.homologacao.obter()


def main() -> None:
    """Demonstrate retrieving homologation products."""
    result = obter_produtos_homologacao()
    print(result.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
