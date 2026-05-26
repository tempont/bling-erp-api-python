"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

DEPOSITO_OPERATIONS: dict[str, OperationContract] = {
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém depósitos paginados.",
            "method": "GET",
            "parameters": [
                {
                    "description": "N° da página da listagem",
                    "location": "query",
                    "name": "pagina",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "pagina",
                },
                {
                    "description": "Quantidade de registros que devem ser exibidos por página",
                    "location": "query",
                    "name": "limite",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "limite",
                },
                {
                    "description": "Descrição do depósito",
                    "location": "query",
                    "name": "descricao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "descricao",
                },
                {
                    "description": "`0` Inativo <br> `1` Ativo",
                    "location": "query",
                    "name": "situacao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "situacao",
                },
            ],
            "path": "/depositos",
            "request_schema_refs": [],
            "resource": "Depositos",
            "response_schema_refs": {"200": ["DepositosDadosDTO"]},
            "sdk_method": "listar",
            "summary": "Obtém depósitos",
        }
    ),
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria um depósito. Até 100 depósitos podem ser criados.",
            "method": "POST",
            "parameters": [],
            "path": "/depositos",
            "request_schema_refs": ["DepositosDadosDTO"],
            "resource": "Depositos",
            "response_schema_refs": {"201": ["BasePostResponse"], "400": ["ErrorResponse"]},
            "sdk_method": "criar",
            "summary": "Cria um depósito",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém um depósito pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do depósito",
                    "location": "path",
                    "name": "idDeposito",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_deposito",
                }
            ],
            "path": "/depositos/{idDeposito}",
            "request_schema_refs": [],
            "resource": "Depositos",
            "response_schema_refs": {"200": ["DepositosDadosDTO"], "404": ["ErrorResponse"]},
            "sdk_method": "obter",
            "summary": "Obtém um depósito",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera um depósito pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID do depósito",
                    "location": "path",
                    "name": "idDeposito",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_deposito",
                }
            ],
            "path": "/depositos/{idDeposito}",
            "request_schema_refs": ["DepositosDadosDTO"],
            "resource": "Depositos",
            "response_schema_refs": {
                "200": ["BasePostResponse", "ErrorField"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "alterar",
            "summary": "Altera um depósito",
        }
    ),
}
