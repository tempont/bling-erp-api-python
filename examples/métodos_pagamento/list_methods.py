"""Example: List Payment Methods.

Endpoints:
    - GET /formas-pagamentos

Docs:
    - https://developer.bling.com.br/referencia#/Formas%20de%20Pagamento/get_formas_pagamentos

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.payment_methods import (
        FormasPagamentosGetResponse200,
    )


def listar_formas_pagamento(
    *, pagina: int = 1, limite: int = 100, situacao: int | None = None
) -> FormasPagamentosGetResponse200:
    """Lista formas de pagamento.

    Endpoint: GET /formas-pagamentos

    Lista formas de pagamento com paginação e filtros opcionais.

    Args:
        pagina: Número da página (Bling: ``pagina``, integer, opcional)
        limite: Limite de registros por página (Bling: ``limite``, integer, opcional)
        situacao: Filtrar por situação (Bling: ``situacao``, integer, opcional)

    Returns:
        Bling API response. Response schemas: 200: FormasPagamentosDadosBaseDTO; 400: ErrorResponse
    """
    with BlingClient.from_env() as client:
        return client.formas_pagamentos.listar(pagina=pagina, limite=limite, situacao=situacao)


def main() -> None:
    """Demonstrate listing payment methods."""
    print(listar_formas_pagamento(situacao=1).model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
