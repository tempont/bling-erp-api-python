"""Example: Create Homologation Product.

Demonstrates creating a homologation product through the Bling API.

Endpoint:
    - POST /homologacao/produtos

Docs:
    - https://developer.bling.com.br/referencia#/Homologa%C3%A7%C3%A3o/post_homologacao_produtos

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.homologation import (
        HomologacaoProdutosPostResponse201,
    )
    from bling_erp_api.types import JsonObject


def criar_produto_homologacao(dados: JsonObject) -> HomologacaoProdutosPostResponse201:
    """Cria um produto de homologação.

    Endpoint: POST /homologacao/produtos

    Cria um novo produto para homologação na API do Bling.

    Args:
        dados: Dados do produto de homologação (Bling: request body, JsonObject, obrigatório)

    Returns:
        Bling API response. Response schemas: 201: HomologacaoProdutosPostResponse201; 400: ErrorResponse
    """
    with BlingClient.from_env() as client:
        return client.homologacao.criar(dados=dados)


def main() -> None:
    """Demonstrate creating a homologation product."""
    payload: JsonObject = {
        "nome": "Produto Homologação",
        "preco": 10.0,
        "codigo": "TEST-001",
    }
    result = criar_produto_homologacao(payload)
    print(result.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
