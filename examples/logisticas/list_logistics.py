"""Example: List Logistics.

Demonstrates how to list logistics/transport providers through the Bling logistics API.

Endpoint:
    - GET /logisticas

Docs:
    - https://developer.bling.com.br/referencia#/Logisticas/get_logisticas

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.logisticas import (
        LogisticasGetResponse200,
    )


def listar_logisticas(
    *,
    pagina: int = 1,
    limite: int = 10,
    tipo_integracao: str | None = None,
    situacao: str | None = None,
) -> LogisticasGetResponse200:
    """Lista logísticas.

    Args:
        pagina: Número da página (Bling: ``pagina``, integer, opcional)
        limite: Limite de registros (Bling: ``limite``, integer, opcional)
        tipo_integracao: Tipo de integração (Bling: ``tipoIntegracao``, string, opcional)
        situacao: Situação (Bling: ``situacao``, string, opcional)

    Returns:
        Bling API response. Response schemas: 200: LogisticasGetResponse200
    """
    with BlingClient.from_env() as client:
        return client.logisticas.listar(
            pagina=pagina,
            limite=limite,
            tipo_integracao=tipo_integracao,
            situacao=situacao,
        )


def main() -> None:
    """Demonstrate listing logistics filtered by Correios integration."""
    print(
        listar_logisticas(tipo_integracao="Correios", pagina=1, limite=5).model_dump_json(
            indent=2, by_alias=True
        )
    )


if __name__ == "__main__":
    main()
