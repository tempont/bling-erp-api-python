"""Example: Create a new ad."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.ads import AnunciosPostResponse201, AnunciosSaveRequest

PRODUCT_ID: int | None = None


def main() -> None:
    """Create a new ad with product and integration info."""
    if PRODUCT_ID is None:
        msg = "PRODUCT_ID is required"
        raise ValueError(msg)

    payload = AnunciosSaveRequest.model_construct(
        produto={"id": PRODUCT_ID},
        integracao={"tipo": "MercadoLivre"},
        loja={"id": 1},
        nome="Meu Anúncio de Teste",
    )
    with BlingClient.from_env() as client:
        response = client.anuncios.criar(payload)
        parsed = AnunciosPostResponse201(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
