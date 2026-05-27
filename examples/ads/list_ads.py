"""Example: List ads with filters."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.ads import AnunciosGetResponse200


def main() -> None:
    """List ads with integration type and store filters."""
    with BlingClient.from_env() as client:
        response = client.anuncios.listar(
            tipo_integracao="MercadoLivre",
            id_loja=1,
            situacao=1,
            limite=10,
        )
        parsed = AnunciosGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
