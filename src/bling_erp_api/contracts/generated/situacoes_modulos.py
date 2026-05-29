"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

SITUATION_MODULE_OPERATIONS: dict[str, OperationContract] = {
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém módulos.",
            "method": "GET",
            "parameters": [],
            "path": "/situacoes/modulos",
            "request_schema_refs": [],
            "resource": "SituacoesModulos",
            "response_schema_refs": {"200": ["SituacoesModuloBaseDTO", "SituacoesModuloDTO"]},
            "sdk_method": "listar",
            "summary": "Obtém módulos",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém situações de um módulo pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do módulo do sistema",
                    "location": "path",
                    "name": "idModuloSistema",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_modulo_sistema",
                }
            ],
            "path": "/situacoes/modulos/{idModuloSistema}",
            "request_schema_refs": [],
            "resource": "SituacoesModulos",
            "response_schema_refs": {
                "200": ["SituacoesDTO", "SituacoesDadosDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter",
            "summary": "Obtém situações de um módulo",
        }
    ),
    "listar_acoes": OperationContract.model_validate(
        {
            "action": "ObterAcaoMultiplos",
            "description": "Obtém as ações de um módulo pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do módulo do sistema",
                    "location": "path",
                    "name": "idModuloSistema",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_modulo_sistema",
                }
            ],
            "path": "/situacoes/modulos/{idModuloSistema}/acoes",
            "request_schema_refs": [],
            "resource": "SituacoesModulos",
            "response_schema_refs": {"200": ["SituacoesAcaoDTO"], "404": ["ErrorResponse"]},
            "sdk_method": "listar",
            "summary": "Obtém as ações de um módulo",
        }
    ),
    "listar_transicoes": OperationContract.model_validate(
        {
            "action": "ObterTransicaoMultiplos",
            "description": "Obtém as transições de um módulo pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do módulo do sistema",
                    "location": "path",
                    "name": "idModuloSistema",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_modulo_sistema",
                }
            ],
            "path": "/situacoes/modulos/{idModuloSistema}/transicoes",
            "request_schema_refs": [],
            "resource": "SituacoesModulos",
            "response_schema_refs": {"200": ["SituacoesTransicaoDTO"], "404": ["ErrorResponse"]},
            "sdk_method": "listar_transicoes",
            "summary": "Obtém as transições de um módulo",
        }
    ),
}
