"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

BORDERO_OPERATIONS: dict[str, OperationContract] = {
    "remover": OperationContract.model_validate(
        {
            "action": "Remover",
            "description": "Remove um borderô pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID do bordero",
                    "location": "path",
                    "name": "idBordero",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_bordero",
                }
            ],
            "path": "/borderos/{idBordero}",
            "request_schema_refs": [],
            "resource": "Borderos",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "remover",
            "summary": "Remove um borderô",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém um borderô pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do bordero",
                    "location": "path",
                    "name": "idBordero",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_bordero",
                }
            ],
            "path": "/borderos/{idBordero}",
            "request_schema_refs": [],
            "resource": "Borderos",
            "response_schema_refs": {"200": ["BorderosDadosDTO"], "404": ["ErrorResponse"]},
            "sdk_method": "obter",
            "summary": "Obtém um borderô",
        }
    ),
}
