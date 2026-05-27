"""Example: Publish an ad."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.ads import AnunciosIdAnuncioGetResponse200


def main() -> None:
    """Publish an existing ad by ID."""
    with BlingClient.from_env() as client:
        response = client.anuncios.publicar(123456, tipo_integracao="MercadoLivre", id_loja=1)
        ad = AnunciosIdAnuncioGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(ad.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
