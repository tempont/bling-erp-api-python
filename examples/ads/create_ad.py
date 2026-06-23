"""Example: Create an Ad.

Demonstrates ad creation through the Bling Anúncios API.

Endpoint:
    - POST /anuncios

Docs:
    - https://developer.bling.com.br/referencia#/Anúncios/post_anuncios

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.ads import (
        AnunciosPostResponse201,
        AnunciosSaveRequest,
    )

# Use a real product ID from your Bling account.
PRODUCT_ID: int | None = None


def criar_anuncio(dados: AnunciosSaveRequest) -> AnunciosPostResponse201:
    """Cria um novo anúncio.

    Endpoint: POST /anuncios

    Cria um anúncio para um produto em uma loja de integração.

    Args:
        dados: Dados do anúncio (Bling: ``AnunciosSaveRequest``, obrigatório)

    Returns:
        Bling API response. Response schemas: 201: AnunciosSaveResponseDTO; 400: ErrorResponse
    """
    with BlingClient.from_env() as client:
        return client.anuncios.criar(dados=dados)


def main() -> None:
    """Demonstrate ad creation."""
    if PRODUCT_ID is None:
        print("Configure PRODUCT_ID before running this example.")
        return

    # payload = AnunciosSaveRequest(
    #     produto={"id": PRODUCT_ID},
    #     integracao={"id": 123456},
    #     loja={"id": 1},
    # )
    # result = criar_anuncio(payload)
    # print(result.model_dump_json(indent=2, by_alias=True))
    print("Ad creation example ready (write operations commented out).")


if __name__ == "__main__":
    main()
