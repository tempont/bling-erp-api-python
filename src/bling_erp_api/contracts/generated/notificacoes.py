"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

NOTIFICACOES_OPERATIONS: dict[str, OperationContract] = {
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém todas as notificações de uma empresa no período informado. Caso período não "
            "seja informado, será considerado o ano atual.",
            "method": "GET",
            "parameters": [
                {
                    "description": "Apenas ano ou ano e mês em que a empresa foi notificada. Caso não "
                    "informado, será utilizado o ano atual.",
                    "location": "query",
                    "name": "periodo",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "periodo",
                }
            ],
            "path": "/notificacoes",
            "request_schema_refs": [],
            "resource": "Notificacoes",
            "response_schema_refs": {
                "200": ["NotificacoesDadosBaseDTO", "NotificacoesUlidsDTO"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "listar",
            "summary": "Obtém todas as notificações de uma empresa em um período",
        }
    ),
    "obter_quantidade": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém a quantidade de notificações de uma empresa no período informado. Caso "
            "período não seja informado, será considerado o ano atual.",
            "method": "GET",
            "parameters": [
                {
                    "description": "Apenas ano ou ano e mês em que a empresa foi notificada. Caso não "
                    "informado, será utilizado o ano atual.",
                    "location": "query",
                    "name": "periodo",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "periodo",
                }
            ],
            "path": "/notificacoes/quantidade",
            "request_schema_refs": [],
            "resource": "Notificacoes",
            "response_schema_refs": {
                "200": ["NotificacoesQuantidadeDTO"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "obter_quantidade",
            "summary": "Obtém a quantidade de notificações de uma empresa em um período",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Marca a notificação relacionada à empresa como lida.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ULID da notificação.",
                    "location": "path",
                    "name": "idNotificacao",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "id_notificacao",
                }
            ],
            "path": "/notificacoes/{idNotificacao}/confirmar-leitura",
            "request_schema_refs": [],
            "resource": "Notificacoes",
            "response_schema_refs": {
                "200": ["NotificacoesDadosBaseDTO", "NotificacoesUlidsDTO"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "alterar",
            "summary": "Marca notificação como lida",
        }
    ),
}
