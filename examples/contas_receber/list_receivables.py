"""Example: List receivables.

Endpoints:
    - GET /contas/receber

Docs:
    - https://developer.bling.com.br/referencia#/Contas%20a%20Receber/get_contas_receber

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.contas_receber import (
        ContasReceberGetResponse200,
    )


def listar_contas(
    *, pagina: int = 1, limite: int = 100, situacoes: list[int] | None = None
) -> ContasReceberGetResponse200:
    """Lista contas a receber.

    Args:
        pagina: Número da página (Bling: ``pagina``, integer, opcional)
        limite: Limite de registros (Bling: ``limite``, integer, opcional)
        situacoes: Situações das contas (Bling: ``situacoes``, array of integers, opcional)

    Returns:
        Bling API response. Response schemas: 200: ContasReceberGetResponse200
    """
    with BlingClient.from_env() as client:
        return client.contas_receber.listar(pagina=pagina, limite=limite, situacoes=situacoes)


def main() -> None:
    """Lista as primeiras 5 contas com situação 'Em aberto' e 'Recebido'."""
    print(
        listar_contas(pagina=1, limite=5, situacoes=[1, 2]).model_dump_json(indent=2, by_alias=True)
    )
    time.sleep(1)


if __name__ == "__main__":
    main()
