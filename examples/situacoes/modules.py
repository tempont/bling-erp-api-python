"""Example: Modules Status Workflow.

Demonstrates CRUD for managing statuses.

Endpoints:
    - GET /situacoes/modulos
    - GET /situacoes/modulos/{idModuloSistema}
    - GET /situacoes/modulos/{idModuloSistema}/acoes
    - GET /situacoes/modulos/{idModuloSistema}/transicoes

Docs:
    - https://developer.bling.com.br/referencia#/Situa%C3%A7%C3%B5es%20-%20M%C3%B3dulos/get_situacoes_modulos
    - https://developer.bling.com.br/referencia#/Situa%C3%A7%C3%B5es%20-%20M%C3%B3dulos/get_situacoes_modulos__idModuloSistema_
    - https://developer.bling.com.br/referencia#/Situa%C3%A7%C3%B5es%20-%20M%C3%B3dulos/get_situacoes_modulos__idModuloSistema__acoes
    - https://developer.bling.com.br/referencia#/Situa%C3%A7%C3%B5es%20-%20M%C3%B3dulos/get_situacoes_modulos__idModuloSistema__transicoes
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.situacoes_modulos import (
        SituacoesModulosGetResponse200,
        SituacoesModulosIdModuloSistemaAcoesGetResponse200,
        SituacoesModulosIdModuloSistemaGetResponse200,
        SituacoesModulosIdModuloSistemaTransicoesGetResponse200,
    )


def list_modules() -> SituacoesModulosGetResponse200:
    """List situation modules."""
    client = BlingClient.from_env()
    modulos = client.situacoes_modulos

    return modulos.listar()


def get_module(module_id: int) -> SituacoesModulosIdModuloSistemaGetResponse200:
    """Get a module by ID."""
    client = BlingClient.from_env()
    modulos = client.situacoes_modulos

    return modulos.obter(id_modulo_sistema=module_id)


def get_module_actions(module_id: int) -> SituacoesModulosIdModuloSistemaAcoesGetResponse200:
    """Get module actions."""
    client = BlingClient.from_env()
    modulos = client.situacoes_modulos

    return modulos.listar_acoes(id_modulo_sistema=module_id)


def get_module_transitions(
    module_id: int,
) -> SituacoesModulosIdModuloSistemaTransicoesGetResponse200:
    """Get module transactions.."""
    client = BlingClient.from_env()
    modulos = client.situacoes_modulos

    return modulos.listar_transicoes(id_modulo_sistema=module_id)


def main() -> None:
    """Run the situation modules example."""
    ex_module_id = 98310

    print("Listing modules...")
    print(list_modules().model_dump_json(indent=2, by_alias=True))

    print("Getting module details")
    print(get_module(module_id=98310).model_dump_json(indent=2, by_alias=True))

    print("Getting module actions")
    print(get_module_actions(module_id=ex_module_id).model_dump_json(indent=2, by_alias=True))

    print("Getting module transitions")
    print(get_module_transitions(module_id=ex_module_id).model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
