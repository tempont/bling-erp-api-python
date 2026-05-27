"""Exemplo que obtém o produto da homologação usando o SDK."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.homologation import HomologacaoProdutosGetResponse200


def main() -> None:
    """Obtém o produto da homologação."""
    with BlingClient.from_env() as client:
        response = client.homologacao.obter()
        parsed = HomologacaoProdutosGetResponse200(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
