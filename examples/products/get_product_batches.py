"""Exemplos de leitura de lotes de produtos."""

from bling_erp_api import BlingClient


def main() -> None:
    """Lista lotes, obtém um lote e consulta controle de lote por produto."""
    ids_produtos = [123456789]  # Exemplo — substitua pelos IDs reais.
    id_lote = 987654321  # Exemplo — substitua pelo ID real.
    with BlingClient.from_env() as client:
        lista = client.lotes.listar(ids_produtos=ids_produtos, limite=10)
        print("listar:", lista)
        detail = client.lotes.obter(id_lote)
        print("obter:", detail)
        controle = client.lotes.listar_produtos_controlam_lote(ids_produtos=ids_produtos)
        print("controla_lote:", controle)


if __name__ == "__main__":
    main()
