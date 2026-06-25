"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

LOGISTICAS_REMESSAS_OPERATIONS: dict[str, OperationContract] = {
    "criar_remessa": OperationContract.model_validate(
        {
            "action": "CriarRemessa",
            "description": "Cria uma remessa de postagem de uma logística.",
            "method": "POST",
            "parameters": [],
            "path": "/logisticas/remessas",
            "request_schema_refs": ["LogisticasRemessasDadosPostDTO"],
            "resource": "Logisticas",
            "response_schema_refs": {
                "201": ["LogisticasRemessaRemessaDTO"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "criar_remessa",
            "summary": "Cria uma remessa de postagem de uma logística",
        }
    ),
    "remover_remessa": OperationContract.model_validate(
        {
            "action": "RemoverRemessa",
            "description": "Remove uma remessa de postagem pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID da remessa de postagem",
                    "location": "path",
                    "name": "idRemessa",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_remessa",
                }
            ],
            "path": "/logisticas/remessas/{idRemessa}",
            "request_schema_refs": [],
            "resource": "Logisticas",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "remover_remessa",
            "summary": "Remove uma remessa de postagem",
        }
    ),
    "obter_remessa": OperationContract.model_validate(
        {
            "action": "ObterRemessa",
            "description": "Obtém uma remessa de postagem pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID da remessa de postagem",
                    "location": "path",
                    "name": "idRemessa",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_remessa",
                }
            ],
            "path": "/logisticas/remessas/{idRemessa}",
            "request_schema_refs": [],
            "resource": "Logisticas",
            "response_schema_refs": {
                "200": ["LogisticasRemessasDadosBaseDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter_remessa",
            "summary": "Obtém uma remessa de postagem",
        }
    ),
    "alterar_remessa": OperationContract.model_validate(
        {
            "action": "AlterarRemessa",
            "description": "Altera uma remessa de postagem pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID da remessa de postagem",
                    "location": "path",
                    "name": "idRemessa",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_remessa",
                }
            ],
            "path": "/logisticas/remessas/{idRemessa}",
            "request_schema_refs": ["LogisticasRemessasDadosBaseDTOCommon"],
            "resource": "Logisticas",
            "response_schema_refs": {
                "200": ["LogisticasRemessaRemessaDTO"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "alterar_remessa",
            "summary": "Altera uma remessa de postagem",
        }
    ),
    "listar_remessas_por_logistica": OperationContract.model_validate(
        {
            "action": "ObterLogisticaRemessaMultiplos",
            "description": "Obtém as remessas de postagem de uma logística pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID da logística",
                    "location": "path",
                    "name": "idLogistica",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_logistica",
                }
            ],
            "path": "/logisticas/{idLogistica}/remessas",
            "request_schema_refs": [],
            "resource": "Logisticas",
            "response_schema_refs": {
                "200": ["LogisticasRemessasDadosDTO"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "listar_remessas_por_logistica",
            "summary": "Obtém as remessas de postagem de uma logística",
        }
    ),
}
