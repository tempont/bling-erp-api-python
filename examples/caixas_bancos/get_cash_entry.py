"""Example: Get a single cash/bank entry by ID."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.caixas_bancos import CaixasBancosLancamentoDTO


def obter_lancamento(id_caixa: int) -> CaixasBancosLancamentoDTO:
    """Obtém um lançamento de caixa e banco pelo ID.

    Endpoint: GET /caixas/{idCaixa}

    Obtém os detalhes de um lançamento pelo ID.

    Args:
        id_caixa: ID do lançamento (Bling: ``idCaixa``, integer, obrigatório)

    Returns:
        Bling API response. Response schemas: 200: CaixasBancosLancamentoDTO; 404: ErrorResponse
    """
    with BlingClient.from_env() as client:
        return client.caixas_bancos.obter(id_caixa=id_caixa)


def main() -> None:
    """Retrieve cash/bank entry details by ID."""
    resultado = obter_lancamento(id_caixa=12345678)
    print(resultado.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
