"""Example: Logistics Objects CRUD Operations.

Demonstrates CRUD operations on logistics objects through the Bling logistics API.

Endpoints:
    - POST /logisticas/objetos
    - GET /logisticas/objetos/{idObjeto}
    - PUT /logisticas/objetos/{idObjeto}
    - DELETE /logisticas/objetos/{idObjeto}

Docs:
    - https://developer.bling.com.br/referencia#/Logisticas/post_logisticas_objetos
    - https://developer.bling.com.br/referencia#/Logisticas/get_logisticas_objetos__idObjeto_
    - https://developer.bling.com.br/referencia#/Logisticas/put_logisticas_objetos__idObjeto_
    - https://developer.bling.com.br/referencia#/Logisticas/delete_logisticas_objetos__idObjeto_

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.logisticas import (
        LogisticasObjetosIdObjetoGetResponse200,
        LogisticasObjetosIdObjetoPutResponse200,
        LogisticasObjetosPostResponse201,
    )
    from bling_erp_api.types import JsonObject

## ---------------------------------------------------------------------------
## GET A LOGISTICS OBJECT BY ID
## ---------------------------------------------------------------------------


def obter_objeto(object_id: int) -> LogisticasObjetosIdObjetoGetResponse200:
    """Obtém um objeto de logística pelo ID."""
    with BlingClient.from_env() as client:
        return client.logisticas_objetos.obter(id_objeto=object_id)


## ---------------------------------------------------------------------------
## CREATE A LOGISTICS OBJECT
## ---------------------------------------------------------------------------


def criar_objeto(dados: JsonObject) -> LogisticasObjetosPostResponse201:
    """Cria um novo objeto de logística."""
    with BlingClient.from_env() as client:
        return client.logisticas_objetos.criar(dados=dados)


## ---------------------------------------------------------------------------
## UPDATE A LOGISTICS OBJECT (PUT)
## ---------------------------------------------------------------------------


def alterar_objeto(object_id: int, dados: JsonObject) -> LogisticasObjetosIdObjetoPutResponse200:
    """Atualiza um objeto de logística por completo (PUT)."""
    with BlingClient.from_env() as client:
        return client.logisticas_objetos.alterar(id_objeto=object_id, dados=dados)


## ---------------------------------------------------------------------------
## DELETE A LOGISTICS OBJECT
## ---------------------------------------------------------------------------


def remover_objeto(object_id: int) -> None:
    """Remove um objeto de logística pelo ID."""
    with BlingClient.from_env() as client:
        client.logisticas_objetos.remover(id_objeto=object_id)


def main() -> None:
    """Demonstrate logistics objects CRUD operations."""
    object_id = 1  # Exemplo — substitua pelo ID real.

    # Read operations
    print(obter_objeto(object_id).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    # Write operations (commented out to avoid side effects)
    # payload: JsonObject = {
    #     "pedidoVenda": {
    #         "id": 123,
    #     },
    #     "notaFiscal": {
    #         "numero": "123456",
    #         "serie": "1",
    #     },
    #     "servico": {
    #         "idServico": 1,
    #     },
    #     "dimensao": {
    #         "altura": 10.0,
    #         "largura": 20.0,
    #         "comprimento": 30.0,
    #         "peso": 1.5,
    #     },
    #     "embalagem": {
    #         "idEmbalagem": 1,
    #     },
    # }
    # print(criar_objeto(payload).model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)
    # print(alterar_objeto(object_id, payload).model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)
    # remover_objeto(object_id)
    # time.sleep(1)


if __name__ == "__main__":
    main()
