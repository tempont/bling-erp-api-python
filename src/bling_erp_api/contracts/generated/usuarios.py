"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

USUARIO_OPERATIONS: dict[str, OperationContract] = {
    "recuperar_senha": OperationContract.model_validate(
        {
            "action": "post",
            "description": "Envia solicitação de recuperação de senha por e-mail.",
            "method": "POST",
            "parameters": [],
            "path": "/usuarios/recuperar-senha",
            "request_schema_refs": [],
            "resource": "Usuarios",
            "response_schema_refs": {"400": ["ErrorResponse"]},
            "sdk_method": "recuperar_senha",
            "summary": "Envia solicitação de recuperação de senha",
        }
    ),
    "redefinir_senha": OperationContract.model_validate(
        {
            "action": "patch",
            "description": "Redefine senha do usuário utilizando token enviado por e-mail.",
            "method": "PATCH",
            "parameters": [],
            "path": "/usuarios/redefinir-senha",
            "request_schema_refs": [],
            "resource": "Usuarios",
            "response_schema_refs": {"400": ["ErrorResponse"]},
            "sdk_method": "redefinir_senha",
            "summary": "Redefine senha do usuário",
        }
    ),
    "verificar_hash": OperationContract.model_validate(
        {
            "action": "get",
            "description": "Valida o hash recebido por e-mail.",
            "method": "GET",
            "parameters": [
                {
                    "description": None,
                    "location": "query",
                    "name": "hash",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "hash",
                }
            ],
            "path": "/usuarios/verificar-hash",
            "request_schema_refs": [],
            "resource": "Usuarios",
            "response_schema_refs": {"400": ["ErrorResponse"]},
            "sdk_method": "verificar_hash",
            "summary": "Valida o hash recebido",
        }
    ),
}
