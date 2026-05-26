"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

CONTAS_CONTABEIS_OPERATIONS: dict[str, OperationContract] = {
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém contas financeiras paginadas.",
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
                    "description": "Oculta contas financeiras invisíveis",
                    "location": "query",
                    "name": "ocultarInvisiveis",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "boolean",
                    "sdk_name": "ocultar_invisiveis",
                },
                {
                    "description": "Oculta contas financeiras do tipo conta bancária",
                    "location": "query",
                    "name": "ocultarTipoContaBancaria",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "boolean",
                    "sdk_name": "ocultar_tipo_conta_bancaria",
                },
                {
                    "description": "Situação da conta financeira<br> `1` Ativo<br> `2` Inativo<br> "
                    "`3` Pendente<br> `4` Cancelada",
                    "location": "query",
                    "name": "situacoes",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "situacoes",
                },
                {
                    "description": "Alias da integração",
                    "location": "query",
                    "name": "aliasIntegracao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "alias_integracao",
                },
                {
                    "description": "Alias da integração",
                    "location": "path",
                    "name": "aliasIntegracao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "alias_integracao",
                },
                {
                    "description": "Ordenação da obtenção pelos campos: <br> `descricao`",
                    "location": "query",
                    "name": "ordenacao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "ordenacao",
                },
            ],
            "path": "/contas-contabeis",
            "request_schema_refs": [],
            "resource": "ContasContabeis",
            "response_schema_refs": {"200": ["ContasContabeisDadosDTO"]},
            "sdk_method": "listar",
            "summary": "Obtém contas financeiras",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém uma conta financeira pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID da conta financeira",
                    "location": "path",
                    "name": "idContaContabil",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_conta_contabil",
                }
            ],
            "path": "/contas-contabeis/{idContaContabil}",
            "request_schema_refs": [],
            "resource": "ContasContabeis",
            "response_schema_refs": {"200": ["ContasContabeisDadosDTO"], "404": ["ErrorResponse"]},
            "sdk_method": "obter",
            "summary": "Obtém uma conta financeira",
        }
    ),
}
