"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

SITUATION_OPERATIONS: dict[str, OperationContract] = {
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria uma situação.",
            "method": "POST",
            "parameters": [],
            "path": "/situacoes",
            "request_schema_refs": ["SituacoesDadosDTO"],
            "resource": "Situacoes",
            "response_schema_refs": {"201": ["BasePostResponse"], "400": ["ErrorResponse"]},
            "sdk_method": "criar",
            "summary": "Cria uma situação",
        }
    ),
    "remover": OperationContract.model_validate(
        {
            "action": "Remover",
            "description": "Remove uma situação pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID da situação",
                    "location": "path",
                    "name": "idSituacao",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_situacao",
                }
            ],
            "path": "/situacoes/{idSituacao}",
            "request_schema_refs": [],
            "resource": "Situacoes",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "remover",
            "summary": "Remove uma situação",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém uma situação pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID da situação",
                    "location": "path",
                    "name": "idSituacao",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_situacao",
                }
            ],
            "path": "/situacoes/{idSituacao}",
            "request_schema_refs": [],
            "resource": "Situacoes",
            "response_schema_refs": {
                "200": ["SituacoesDTO", "SituacoesDadosDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter",
            "summary": "Obtém uma situação",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera uma situação pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID da situação",
                    "location": "path",
                    "name": "idSituacao",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_situacao",
                }
            ],
            "path": "/situacoes/{idSituacao}",
            "request_schema_refs": ["SituacoesDadosDTO"],
            "resource": "Situacoes",
            "response_schema_refs": {"200": ["BasePostResponse"], "400": ["ErrorResponse"]},
            "sdk_method": "alterar",
            "summary": "Altera uma situação",
        }
    ),
}
