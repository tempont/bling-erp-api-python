"""Example: Get an Ad by ID.

Demonstrates fetching a single ad through the Bling Anúncios API.

Endpoint:
    - GET /anuncios/{idAnuncio}

Docs:
    - https://developer.bling.com.br/referencia#/Anúncios/get_anuncios__idAnuncio_

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.ads import AnunciosIdAnuncioGetResponse200

# Replace with a real ad ID from your Bling account.
AD_ID: int | None = 123456


def obter_anuncio(
    ad_id: int, *, tipo_integracao: str = "MercadoLivre", id_loja: int = 1
) -> AnunciosIdAnuncioGetResponse200:
    """Obtém um anúncio pelo ID.

    Endpoint: GET /anuncios/{idAnuncio}

    Obtém os dados de um anúncio específico.

    Args:
        ad_id: ID do anúncio (Bling: ``idAnuncio``, integer, obrigatório)
        tipo_integracao: Tipo da integração (Bling: ``tipoIntegracao``, string, obrigatório)
        id_loja: ID da loja (Bling: ``idLoja``, integer, obrigatório)

    Returns:
        Bling API response. Response schemas: 200: AnunciosGetByIdResponseDTO; 400: ErrorResponse; 404: ErrorResponse
    """
    with BlingClient.from_env() as client:
        return client.anuncios.obter(
            id_anuncio=ad_id, tipo_integracao=tipo_integracao, id_loja=id_loja
        )


def main() -> None:
    """Demonstrate single ad retrieval."""
    if AD_ID is None:
        print("Configure AD_ID before running this example.")
        return

    result = obter_anuncio(AD_ID)
    print(result.model_dump_json(indent=2, by_alias=True))
    time.sleep(1)


if __name__ == "__main__":
    main()
