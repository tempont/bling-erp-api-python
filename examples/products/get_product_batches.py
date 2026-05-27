"""Exemplos de leitura de lotes de produtos."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.product_batches import (
    ProdutosLotesControlaLoteGetResponse200,
    ProdutosLotesGetResponse200,
    ProdutosLotesIdLoteGetResponse200,
)


def main() -> None:
    """Lista lotes, obtém um lote e consulta controle de lote por produto."""
    ids_produtos = [123456789]  # Exemplo — substitua pelos IDs reais.
    id_lote = 987654321  # Exemplo — substitua pelo ID real.
    with BlingClient.from_env() as client:
        lista = client.lotes.listar(ids_produtos=ids_produtos, limite=10)
        parsed = ProdutosLotesGetResponse200(**lista)  # type: ignore[reportArgumentType]
        print("listar:", parsed.model_dump_json(indent=2, by_alias=True))
        detail = client.lotes.obter(id_lote)
        parsed = ProdutosLotesIdLoteGetResponse200(**detail)  # type: ignore[reportArgumentType]
        print("obter:", parsed.model_dump_json(indent=2, by_alias=True))
        controle = client.lotes.listar_produtos_controlam_lote(ids_produtos=ids_produtos)
        parsed = ProdutosLotesControlaLoteGetResponse200(**controle)  # type: ignore[reportArgumentType]
        print("controla_lote:", parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
