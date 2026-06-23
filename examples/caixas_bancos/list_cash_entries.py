"""Example: List cash/bank entries with date filters."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.caixas_bancos import CaixasGetResponse200


def listar_lancamentos(
    *,
    pagina: int = 1,
    data_inicial: str | None = None,
    data_final: str | None = None,
    situacao: str | None = None,
) -> CaixasGetResponse200:
    """Lista lançamentos de caixas e bancos.

    Endpoint: GET /caixas

    Obtém lista paginada de lançamentos de caixas e bancos com filtros opcionais.

    Args:
        pagina: N° da página (Bling: ``pagina``, integer, opcional)
        data_inicial: Data inicial de consulta (Bling: ``dataInicial``, string, opcional)
        data_final: Data final de consulta (Bling: ``dataFinal``, string, opcional)
        situacao: Situação do lançamento (Bling: ``situacao``, string, opcional)

    Returns:
        Bling API response. Response schemas: 200: CaixasGetResponse200; 400: ErrorResponse
    """
    with BlingClient.from_env() as client:
        return client.caixas_bancos.listar(
            pagina=pagina,
            data_inicial=data_inicial,
            data_final=data_final,
            situacao=situacao,
        )


def main() -> None:
    """List cash/bank entries with date filters."""
    resultado = listar_lancamentos(
        data_inicial="2024-01-01",
        data_final="2024-12-31",
    )
    print(resultado.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
