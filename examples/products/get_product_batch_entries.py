"""Exemplos de leitura de lançamentos e saldos de lotes."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.product_batch_entries import (
    ProdutosIdProdutoLotesDepositosIdDepositoSaldoGetResponse200,
    ProdutosIdProdutoLotesDepositosIdDepositoSaldoSomaGetResponse200,
    ProdutosIdProdutoLotesIdLoteDepositosIdDepositoSaldoGetResponse200,
    ProdutosIdProdutoLotesSaldoSomaGetResponse200,
    ProdutosLotesIdLoteLancamentosGetResponse200,
    ProdutosLotesLancamentosIdLancamentoGetResponse200,
)


def main() -> None:
    """Consulta lançamentos e saldos de lotes (somente leitura)."""
    id_lote = 123456789  # Exemplo — substitua pelo ID real.
    id_lancamento = 987654321  # Exemplo — substitua pelo ID real.
    id_produto = 111222333  # Exemplo — substitua pelo ID real.
    id_deposito = 444555666  # Exemplo — substitua pelo ID real.
    with BlingClient.from_env() as client:
        lancs = client.lotes_lancamentos.listar(id_lote=id_lote)
        parsed = ProdutosLotesIdLoteLancamentosGetResponse200(**lancs)  # type: ignore[reportArgumentType]
        print("listar lancamentos:", parsed.model_dump_json(indent=2, by_alias=True))
        one = client.lotes_lancamentos.obter(id_lancamento)
        parsed = ProdutosLotesLancamentosIdLancamentoGetResponse200(**one)  # type: ignore[reportArgumentType]
        print("obter lancamento:", parsed.model_dump_json(indent=2, by_alias=True))
        soma = client.lotes_lancamentos.obter_saldos_soma(id_produto=id_produto)
        parsed = ProdutosIdProdutoLotesSaldoSomaGetResponse200(**soma)  # type: ignore[reportArgumentType]
        print("saldo soma (todos depositos):", parsed.model_dump_json(indent=2, by_alias=True))
        soma_dep = client.lotes_lancamentos.obter_saldos_soma_deposito(
            id_produto=id_produto,
            id_deposito=id_deposito,
        )
        parsed = ProdutosIdProdutoLotesDepositosIdDepositoSaldoSomaGetResponse200(**soma_dep)  # type: ignore[reportArgumentType]
        print("saldo soma deposito:", parsed.model_dump_json(indent=2, by_alias=True))
        saldos = client.lotes_lancamentos.obter_saldos(
            id_produto=id_produto,
            id_deposito=id_deposito,
            ids_lotes=[id_lote],
        )
        parsed = ProdutosIdProdutoLotesDepositosIdDepositoSaldoGetResponse200(**saldos)  # type: ignore[reportArgumentType]
        print("saldos por deposito:", parsed.model_dump_json(indent=2, by_alias=True))
        saldo = client.lotes_lancamentos.obter_saldos_saldo(
            id_produto=id_produto,
            id_lote=id_lote,
            id_deposito=id_deposito,
        )
        parsed = ProdutosIdProdutoLotesIdLoteDepositosIdDepositoSaldoGetResponse200(**saldo)  # type: ignore[reportArgumentType]
        print("saldo lote+deposito:", parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
