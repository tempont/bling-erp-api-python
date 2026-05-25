"""Exemplos de leitura de lançamentos e saldos de lotes."""

from bling_erp_api import BlingClient


def main() -> None:
    """Consulta lançamentos e saldos de lotes (somente leitura)."""
    id_lote = 123456789  # Exemplo — substitua pelo ID real.
    id_lancamento = 987654321  # Exemplo — substitua pelo ID real.
    id_produto = 111222333  # Exemplo — substitua pelo ID real.
    id_deposito = 444555666  # Exemplo — substitua pelo ID real.
    with BlingClient.from_env() as client:
        lancs = client.lotes_lancamentos.listar(id_lote=id_lote)
        print("listar lancamentos:", lancs)
        one = client.lotes_lancamentos.obter(id_lancamento)
        print("obter lancamento:", one)
        soma = client.lotes_lancamentos.obter_saldos_soma(id_produto=id_produto)
        print("saldo soma (todos depositos):", soma)
        soma_dep = client.lotes_lancamentos.obter_saldos_soma_deposito(
            id_produto=id_produto,
            id_deposito=id_deposito,
        )
        print("saldo soma deposito:", soma_dep)
        saldos = client.lotes_lancamentos.obter_saldos(
            id_produto=id_produto,
            id_deposito=id_deposito,
            ids_lotes=[id_lote],
        )
        print("saldos por deposito:", saldos)
        saldo = client.lotes_lancamentos.obter_saldos_saldo(
            id_produto=id_produto,
            id_lote=id_lote,
            id_deposito=id_deposito,
        )
        print("saldo lote+deposito:", saldo)


if __name__ == "__main__":
    main()
