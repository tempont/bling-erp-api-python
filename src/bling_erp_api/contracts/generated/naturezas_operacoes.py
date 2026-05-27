"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

NATUREZAS_OPERACOES_OPERATIONS: dict[str, OperationContract] = {
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém naturezas de operação paginadas.",
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
                    "description": "`0` Inativo <br> `1` Ativo",
                    "location": "query",
                    "name": "situacao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "situacao",
                },
                {
                    "description": "Descrição da natureza de operação",
                    "location": "query",
                    "name": "descricao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "descricao",
                },
            ],
            "path": "/naturezas-operacoes",
            "request_schema_refs": [],
            "resource": "NaturezasOperacoes",
            "response_schema_refs": {
                "200": ["NaturezasOperacoesDadosDTO"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "listar",
            "summary": "Obtém naturezas de operações",
        }
    ),
    "obter_tributacao": OperationContract.model_validate(
        {
            "action": "ObterTributacao",
            "description": "Obtém regras de tributação que incidem sobre o item, dada uma natureza de "
            "operação.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID da natureza de operação",
                    "location": "path",
                    "name": "idNaturezaOperacao",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_natureza_operacao",
                }
            ],
            "path": "/naturezas-operacoes/{idNaturezaOperacao}/obter-tributacao",
            "request_schema_refs": ["CalculosImpostosCalculoDTO"],
            "resource": "NaturezasOperacoes",
            "response_schema_refs": {
                "200": ["CalculosImpostosDadosDTO"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter_tributacao",
            "summary": "Obtém regras de tributação da natureza de operação",
        }
    ),
}
