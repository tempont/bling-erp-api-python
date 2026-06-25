"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

LOGISTICAS_OBJETOS_OPERATIONS: dict[str, OperationContract] = {
    "criar_objeto": OperationContract.model_validate(
        {
            "action": "CriarLogisticaObjeto",
            "description": "Cria um objeto de logística personalizada.",
            "method": "POST",
            "parameters": [],
            "path": "/logisticas/objetos",
            "request_schema_refs": ["LogisticasObjetosDadosCreateRequestDTO"],
            "resource": "Logisticas",
            "response_schema_refs": {
                "201": ["LogisticasObjetosObjetoDTO"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "criar_objeto",
            "summary": "Cria um objeto de logística",
        }
    ),
    "remover_objeto": OperationContract.model_validate(
        {
            "action": "RemoverObjetoLogistico",
            "description": "Remove um objeto de logística personalizada que não esteja em uma PLP.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID do objeto logístico",
                    "location": "path",
                    "name": "idObjeto",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_objeto",
                }
            ],
            "path": "/logisticas/objetos/{idObjeto}",
            "request_schema_refs": [],
            "resource": "Logisticas",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "remover_objeto",
            "summary": "Remove um objeto de logística personalizada",
        }
    ),
    "obter_objeto": OperationContract.model_validate(
        {
            "action": "ObterObjetoLogistico",
            "description": "Obtém um objeto de logística pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do objeto logístico",
                    "location": "path",
                    "name": "idObjeto",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_objeto",
                }
            ],
            "path": "/logisticas/objetos/{idObjeto}",
            "request_schema_refs": [],
            "resource": "Logisticas",
            "response_schema_refs": {
                "200": ["LogisticasObjetosDadosDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter_objeto",
            "summary": "Obtém um objeto de logística",
        }
    ),
    "alterar_objeto": OperationContract.model_validate(
        {
            "action": "AlterarLogisticaObjeto",
            "description": "Altera dados de um objeto de logística personalizada pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID do objeto logístico",
                    "location": "path",
                    "name": "idObjeto",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_objeto",
                }
            ],
            "path": "/logisticas/objetos/{idObjeto}",
            "request_schema_refs": ["LogisticasObjetosUpdateRequestDTO"],
            "resource": "Logisticas",
            "response_schema_refs": {
                "200": ["LogisticasObjetosObjetoDTO"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "alterar_objeto",
            "summary": "Altera um objeto de logística pelo ID",
        }
    ),
}
