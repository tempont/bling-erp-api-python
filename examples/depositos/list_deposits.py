"""Example: List deposits.

Usage:
    uv run python examples/depositos/list_deposits.py
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.depositos import DepositosGetResponse200


def listar_depositos(
    *,
    pagina: int = 1,
    limite: int = 100,
    descricao: str | None = None,
    situacao: int | None = None,
) -> DepositosGetResponse200:
    """Lista depósitos com filtros opcionais.

    Args:
        pagina: Número da página (opcional).
        limite: Quantidade de registros por página (opcional).
        descricao: Filtro pela descrição do depósito (opcional).
        situacao: Filtro pela situação do depósito (opcional).

    Returns:
        Resposta da API com a lista de depósitos.
    """
    with BlingClient.from_env() as client:
        return client.depositos.listar(
            pagina=pagina,
            limite=limite,
            descricao=descricao,
            situacao=situacao,
        )


def main() -> None:
    """Executa o exemplo."""
    print(listar_depositos(pagina=1, limite=5).model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
