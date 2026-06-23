"""Example: Pause an Ad.

Demonstrates pausing an ad through the Bling Anúncios API.

Endpoint:
    - POST /anuncios/{idAnuncio}/pausar

Docs:
    - https://developer.bling.com.br/referencia#/Anúncios/post_anuncios__idAnuncio__pausar

"""

from __future__ import annotations

from bling_erp_api import BlingClient

# Replace with a real ad ID from your Bling account.
AD_ID: int | None = 123456


def pausar_anuncio(ad_id: int, *, tipo_integracao: str = "MercadoLivre", id_loja: int = 1) -> None:
    """Pausa um anúncio.

    Endpoint: POST /anuncios/{idAnuncio}/pausar

    Pausa um anúncio ativo.

    Args:
        ad_id: ID do anúncio (Bling: ``idAnuncio``, integer, obrigatório)
        tipo_integracao: Tipo da integração (Bling: ``tipoIntegracao``, string, obrigatório)
        id_loja: ID da loja (Bling: ``idLoja``, integer, obrigatório)

    Returns:
        None (204 NoContent). Response schemas: 400: ErrorResponse; 404: ErrorResponse
    """
    with BlingClient.from_env() as client:
        client.anuncios.pausar(id_anuncio=ad_id, tipo_integracao=tipo_integracao, id_loja=id_loja)


def main() -> None:
    """Demonstrate pausing an ad."""
    if AD_ID is None:
        print("Configure AD_ID before running this example.")
        return

    # pausar_anuncio(AD_ID)
    # print("Ad paused successfully.")
    # time.sleep(1)
    print("Ad pause example ready (write operations commented out).")


if __name__ == "__main__":
    main()
