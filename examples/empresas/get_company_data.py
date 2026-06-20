"""Example: Get Company Basic Data."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.empresas import (
        EmpresasMeDadosBasicosGetResponse200,
    )


def obter_dados_basicos() -> EmpresasMeDadosBasicosGetResponse200:
    """Obtém os dados básicos da empresa.

    Endpoint: GET /empresas/me/dados-basicos

    Returns:
        Bling API response. Response schemas: 200: EmpresasDadosBasicosDTO
    """
    with BlingClient.from_env() as client:
        return client.empresas.obter_dados_basicos()


def main() -> None:
    """Demonstrate getting company basic data."""
    result = obter_dados_basicos()
    print(result.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
