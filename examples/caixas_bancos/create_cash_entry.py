"""Example: Create a new cash/bank entry."""

from datetime import date

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.caixas_bancos import (
    CaixasBancosSalvarLancamentoDTO,
    CaixasBancosSalvarLancamentoResponseDTO,
)


def main() -> None:
    """Create a new cash/bank entry (credit)."""
    # Model: CaixasBancosSalvarLancamentoDTO  # noqa: ERA001
    #   Required: data (date), valor (float), deb_cred (str), competencia (date), observacoes (str)
    #   Optional: id (int|None), transferencia (str|None),
    #             conta_financeira (ContasFinanceirasDadosBasicosDTO|None),  # noqa: ERA001
    #             categoria (CaixasBancosDadosBasicosCategoriaDTO|None),  # noqa: ERA001
    #             origem (CaixasBancosDadosBasicosOrigemDTO|None),  # noqa: ERA001
    #             contato (CaixasBancosDadosBasicoContatoDTO|None)  # noqa: ERA001
    payload = CaixasBancosSalvarLancamentoDTO.model_construct(
        data=date(2025, 2, 1),
        valor=350.00,
        debCred="C",
        competencia=date(2025, 2, 1),
        observacoes="Venda balcão",
        contaFinanceira={"id": 1},
        categoria={"id": 10},
    )
    with BlingClient.from_env() as client:
        response = client.caixas_bancos.criar(payload)
        parsed = CaixasBancosSalvarLancamentoResponseDTO(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
