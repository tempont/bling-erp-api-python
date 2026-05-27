"""Example: Get a single ad by ID."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.ads import AnunciosIdAnuncioGetResponse200


def main() -> None:
    """Retrieve ad details by ID."""
    with BlingClient.from_env() as client:
        response = client.anuncios.obter(123456, tipo_integracao="MercadoLivre", id_loja=1)
        ad = AnunciosIdAnuncioGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(ad.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
