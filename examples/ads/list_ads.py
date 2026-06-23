"""Example: List Ads.

Demonstrates listing ads through the Bling Anúncios API with optional filters.

Endpoint:
    - GET /anuncios

Docs:
    - https://developer.bling.com.br/referencia#/Anúncios/get_anuncios

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.ads import AnunciosGetResponse200


def listar_anuncios(
    *,
    tipo_integracao: str = "MercadoLivre",
    id_loja: int = 1,
    situacao: int | None = None,
    pagina: int = 1,
    limite: int = 10,
) -> AnunciosGetResponse200:
    """Lista anúncios com filtros opcionais.

    Endpoint: GET /anuncios

    Lista anúncios da loja de integração especificada.

    Args:
        tipo_integracao: Tipo da integração (Bling: ``tipoIntegracao``, string, obrigatório)
        id_loja: ID da loja (Bling: ``idLoja``, integer, obrigatório)
        situacao: Situação do anúncio (Bling: ``situacao``, integer, opcional)
        pagina: Número da página (Bling: ``pagina``, integer, opcional)
        limite: Limite de registros por página (Bling: ``limite``, integer, opcional)

    Returns:
        Bling API response. Response schemas: 200: AnunciosGetAllResponseDTO; 400: ErrorResponse
    """
    with BlingClient.from_env() as client:
        return client.anuncios.listar(
            tipo_integracao=tipo_integracao,
            id_loja=id_loja,
            situacao=situacao,
            pagina=pagina,
            limite=limite,
        )


def main() -> None:
    """Demonstrate ad listing."""
    result = listar_anuncios(limite=5)
    print(result.model_dump_json(indent=2, by_alias=True))
    time.sleep(1)


if __name__ == "__main__":
    main()
