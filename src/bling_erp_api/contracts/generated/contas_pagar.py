"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

CONTAS_PAGAR_OPERATIONS: dict[str, OperationContract] = {
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém contas a pagar paginadas.",
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
                    "description": "Data de emissão inicial da conta a pagar",
                    "location": "query",
                    "name": "dataEmissaoInicial",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_emissao_inicial",
                },
                {
                    "description": "Data de emissão final da conta a pagar",
                    "location": "query",
                    "name": "dataEmissaoFinal",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_emissao_final",
                },
                {
                    "description": "Data de vencimento inicial da conta a pagar",
                    "location": "query",
                    "name": "dataVencimentoInicial",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_vencimento_inicial",
                },
                {
                    "description": "Data de vencimento final da conta a pagar",
                    "location": "query",
                    "name": "dataVencimentoFinal",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_vencimento_final",
                },
                {
                    "description": "Data de pagamento inicial da conta",
                    "location": "query",
                    "name": "dataPagamentoInicial",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_pagamento_inicial",
                },
                {
                    "description": "Data de pagamento final da conta",
                    "location": "query",
                    "name": "dataPagamentoFinal",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_pagamento_final",
                },
                {
                    "description": "`1` Em aberto <br>`2` Recebido <br>`3` Parcialmente recebido "
                    "<br>`4` Devolvido <br>`5` Cancelado",
                    "location": "query",
                    "name": "situacao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "situacao",
                },
                {
                    "description": "ID do contato",
                    "location": "query",
                    "name": "idContato",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_contato",
                },
            ],
            "path": "/contas/pagar",
            "request_schema_refs": [],
            "resource": "ContasPagar",
            "response_schema_refs": {"200": ["ContasDadosBaseDTO"]},
            "sdk_method": "listar",
            "summary": "Obtém contas a pagar",
        }
    ),
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria uma conta a pagar.",
            "method": "POST",
            "parameters": [],
            "path": "/contas/pagar",
            "request_schema_refs": [
                "ContasDadosBaseDTO",
                "ContasPagarDadosDTO",
                "ContasPagarDadosPostDTO",
            ],
            "resource": "ContasPagar",
            "response_schema_refs": {"201": ["BasePostResponse"], "400": ["ErrorResponse"]},
            "sdk_method": "criar",
            "summary": "Cria uma conta a pagar",
        }
    ),
    "remover": OperationContract.model_validate(
        {
            "action": "Remover",
            "description": "Remove uma conta a pagar pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID da conta a pagar",
                    "location": "path",
                    "name": "idContaPagar",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_conta_pagar",
                }
            ],
            "path": "/contas/pagar/{idContaPagar}",
            "request_schema_refs": [],
            "resource": "ContasPagar",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "remover",
            "summary": "Remove uma conta a pagar",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém uma conta a pagar pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID da conta a pagar",
                    "location": "path",
                    "name": "idContaPagar",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_conta_pagar",
                }
            ],
            "path": "/contas/pagar/{idContaPagar}",
            "request_schema_refs": [],
            "resource": "ContasPagar",
            "response_schema_refs": {
                "200": ["ContasDadosBaseDTO", "ContasPagarDadosDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter",
            "summary": "Obtém uma conta a pagar",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Atualiza uma conta a pagar pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID da conta a pagar",
                    "location": "path",
                    "name": "idContaPagar",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_conta_pagar",
                }
            ],
            "path": "/contas/pagar/{idContaPagar}",
            "request_schema_refs": ["ContasDadosBaseDTO", "ContasPagarDadosDTO"],
            "resource": "ContasPagar",
            "response_schema_refs": {
                "200": ["BasePostResponse"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "alterar",
            "summary": "Atualiza uma conta a pagar",
        }
    ),
    "baixar": OperationContract.model_validate(
        {
            "action": "BaixarConta",
            "description": "Cria o recebimento de uma conta a pagar.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID da conta a pagar",
                    "location": "path",
                    "name": "idContaPagar",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_conta_pagar",
                }
            ],
            "path": "/contas/pagar/{idContaPagar}/baixar",
            "request_schema_refs": ["ContasBaixarContaDTO"],
            "resource": "ContasPagar",
            "response_schema_refs": {"400": ["ErrorResponse"]},
            "sdk_method": "baixar",
            "summary": "Cria o recebimento de uma conta a pagar",
        }
    ),
}
