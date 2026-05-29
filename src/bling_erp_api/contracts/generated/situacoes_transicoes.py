"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

SITUATION_TRANSITION_OPERATIONS: dict[str, OperationContract] = {
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria uma transição.",
            "method": "POST",
            "parameters": [],
            "path": "/situacoes/transicoes",
            "request_schema_refs": ["SituacoesTransicaoDTO"],
            "resource": "SituacoesTransicoes",
            "response_schema_refs": {"201": ["BasePostResponse"], "400": ["ErrorResponse"]},
            "sdk_method": "criar",
            "summary": "Cria uma transição",
        }
    ),
    "remover": OperationContract.model_validate(
        {
            "action": "Remover",
            "description": "Remove uma transição pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID da transição",
                    "location": "path",
                    "name": "idTransicao",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_transicao",
                }
            ],
            "path": "/situacoes/transicoes/{idTransicao}",
            "request_schema_refs": [],
            "resource": "SituacoesTransicoes",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "remover",
            "summary": "Remove uma transição",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém uma transição pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID da transição",
                    "location": "path",
                    "name": "idTransicao",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_transicao",
                }
            ],
            "path": "/situacoes/transicoes/{idTransicao}",
            "request_schema_refs": [],
            "resource": "SituacoesTransicoes",
            "response_schema_refs": {"200": ["SituacoesTransicaoDTO"], "404": ["ErrorResponse"]},
            "sdk_method": "obter",
            "summary": "Obtém uma transição",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera uma transição pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID da transição",
                    "location": "path",
                    "name": "idTransicao",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_transicao",
                }
            ],
            "path": "/situacoes/transicoes/{idTransicao}",
            "request_schema_refs": ["SituacoesTransicaoDTO"],
            "resource": "SituacoesTransicoes",
            "response_schema_refs": {"200": ["BasePostResponse"], "400": ["ErrorResponse"]},
            "sdk_method": "alterar",
            "summary": "Altera uma transição",
        }
    ),
}
