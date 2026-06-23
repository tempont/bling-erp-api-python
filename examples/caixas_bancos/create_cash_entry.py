"""Example: Create a new cash/bank entry."""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.caixas_bancos import CaixasBancosSalvarLancamentoDTO

if TYPE_CHECKING:
    from bling_erp_api.models.generated.caixas_bancos import (
        CaixasBancosSalvarLancamentoResponseDTO,
    )


def criar_lancamento(
    dados: CaixasBancosSalvarLancamentoDTO,
) -> CaixasBancosSalvarLancamentoResponseDTO:
    """Cria um novo lançamento de caixa e banco.

    Endpoint: POST /caixas

    Cria um novo lançamento de caixa e banco.

    Args:
        dados: Dados do lançamento. Request body schema: CaixasBancosSalvarLancamentoDTO

    Returns:
        Bling API response. Response schemas: 201: CaixasBancosSalvarLancamentoResponseDTO; 400: ErrorResponse
    """
    with BlingClient.from_env() as client:
        return client.caixas_bancos.criar(lancamento=dados)


def main() -> None:
    """Create a new cash/bank entry (credit)."""
    payload = CaixasBancosSalvarLancamentoDTO(
        data=date(2025, 2, 1),
        valor=350.00,
        deb_cred="C",
        competencia=date(2025, 2, 1),
        observacoes="Venda balcão",
    )
    resultado = criar_lancamento(dados=payload)
    print(resultado.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
