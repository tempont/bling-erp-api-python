"""Example: Logistics Services Operations.

Demonstrates operations on logistics services through the Bling logistics services API.

Endpoints:
    - GET /logisticas/servicos
    - GET /logisticas/servicos/{idLogisticaServico}
    - POST /logisticas/servicos
    - PUT /logisticas/servicos/{idLogisticaServico}

Docs:
    - https://developer.bling.com.br/referencia#/Logisticas
"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.logisticas import (
        LogisticasServicosDadosCreateRequestDTO,
        LogisticasServicosDadosSaveRequestDTO,
        LogisticasServicosGetResponse200,
        LogisticasServicosIdLogisticaServicoGetResponse200,
        LogisticasServicosIdLogisticaServicoPutResponse200,
        LogisticasServicosPostResponse201,
    )
    from bling_erp_api.types import JsonObject

## ---------------------------------------------------------------------------
## LIST SERVICES
## ---------------------------------------------------------------------------


def listar_servicos(*, pagina: int = 1, limite: int = 10) -> LogisticasServicosGetResponse200:
    """Lista serviços de logísticas."""
    with BlingClient.from_env() as client:
        return client.logisticas_servicos.listar(pagina=pagina, limite=limite)


## ---------------------------------------------------------------------------
## GET A SERVICE BY ID
## ---------------------------------------------------------------------------


def obter_servico(
    id_logistica_servico: int,
) -> LogisticasServicosIdLogisticaServicoGetResponse200:
    """Obtém um serviço de logística pelo ID."""
    with BlingClient.from_env() as client:
        return client.logisticas_servicos.obter(id_logistica_servico=id_logistica_servico)


## ---------------------------------------------------------------------------
## CREATE A SERVICE
## ---------------------------------------------------------------------------


def criar_servico(
    dados: LogisticasServicosDadosCreateRequestDTO,
) -> LogisticasServicosPostResponse201:
    """Cria um novo serviço de logística."""
    with BlingClient.from_env() as client:
        return client.logisticas_servicos.criar(dados=dados)


## ---------------------------------------------------------------------------
## UPDATE A SERVICE (PUT)
## ---------------------------------------------------------------------------


def alterar_servico(
    id_logistica_servico: int,
    dados: LogisticasServicosDadosSaveRequestDTO,
) -> LogisticasServicosIdLogisticaServicoPutResponse200:
    """Altera um serviço de logística."""
    with BlingClient.from_env() as client:
        return client.logisticas_servicos.alterar(
            id_logistica_servico=id_logistica_servico, dados=dados
        )


## ---------------------------------------------------------------------------
## UPDATE SITUATION (PATCH)
## ---------------------------------------------------------------------------


def alterar_situacao_servico(id_logistica_servico: int, ativo: bool) -> JsonObject:  # noqa: FBT001
    """Altera a situação de um serviço de logística.

    Endpoint: PATCH /logisticas/servicos/{idLogisticaServico}/situacoes

    Args:
        id_logistica_servico: ID do serviço de logística (Bling: ``idLogisticaServico``, integer, obrigatório)
        ativo: Situação ativo/inativo (Bling: ``ativo``, boolean, obrigatório)

    Returns:
        Bling API response.
    """
    with BlingClient.from_env() as client:
        return client.logisticas_servicos.alterar_situacao(
            id_logistica_servico=id_logistica_servico, ativo=ativo
        )


def set_status(service_id: int, active: bool) -> JsonObject:  # noqa: FBT001
    """Compatibility alias for ``alterar_situacao_servico()``.

    Altera a situação de um serviço de logística.

    Endpoint: PATCH /logisticas/servicos/{idLogisticaServico}/situacoes

    Args:
        service_id: ID do serviço de logística (Bling: ``idLogisticaServico``, integer, obrigatório)
        active: Situação ativo/inativo (Bling: ``ativo``, boolean, obrigatório)

    Returns:
        Bling API response.
    """
    return alterar_situacao_servico(id_logistica_servico=service_id, ativo=active)


def main() -> None:
    """Demonstrate logistics services operations."""
    # Read operations
    print(listar_servicos(pagina=1, limite=5).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    print(obter_servico(id_logistica_servico=201).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    # Write operations (commented out)
    # payload = LogisticasServicosDadosSaveRequestDTO(
    #     descricao="PAC",
    #     frete_item=15.50,
    #     estimativa_entrega=5,
    #     transportador=LogisticasServicosTransportadorDTO(id=1001),
    # )
    # print(
    #     alterar_servico(id_logistica_servico=201, dados=payload).model_dump_json(
    #         indent=2,
    #         by_alias=True,
    #     )
    # )
    # time.sleep(1)

    # create_payload = LogisticasServicosDadosCreateRequestDTO(
    #     logistica=LogisticasServicosLogisticaDTO(id=101),
    #     servicos=[payload],
    # )
    # print(criar_servico(create_payload).model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)


if __name__ == "__main__":
    main()
