"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

ESTOQUE_OPERATIONS: dict[str, OperationContract] = {
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria um registro de estoque.",
            "method": "POST",
            "parameters": [],
            "path": "/estoques",
            "request_schema_refs": ["EstoquesDadosBaseDTO", "EstoquesDadosDTO"],
            "resource": "Estoques",
            "response_schema_refs": {"201": ["BasePostResponse"], "400": ["ErrorResponse"]},
            "sdk_method": "criar",
            "summary": "Cria um registro de estoque",
        }
    ),
    "obter_saldos": OperationContract.model_validate(
        {
            "action": "ObterSaldosEstoque",
            "description": "Obtém o saldo em estoque de produtos, em todos os depósitos.",
            "method": "GET",
            "parameters": [
                {
                    "description": "IDs dos produtos",
                    "location": "query",
                    "name": "idsProdutos[]",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_produtos",
                },
                {
                    "description": "Códigos dos produtos",
                    "location": "query",
                    "name": "codigos[]",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "codigos",
                },
                {
                    "description": "Filtra o saldo em estoque <br> `0` zerado <br> `1` positivo <br> "
                    "`2` negativo",
                    "location": "query",
                    "name": "filtroSaldoEstoque",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "filtro_saldo_estoque",
                },
            ],
            "path": "/estoques/saldos",
            "request_schema_refs": [],
            "resource": "Estoques",
            "response_schema_refs": {
                "200": ["EstoquesSaldosBaseDTO", "EstoquesSaldosDTO"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "obter_saldos",
            "summary": "Obtém o saldo em estoque de produtos",
        }
    ),
    "obter_saldos_por_deposito": OperationContract.model_validate(
        {
            "action": "ObterSaldosEstoqueDeposito",
            "description": "Obtém o saldo em estoque de produtos pelo ID do depósito.",
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
                },
                {
                    "description": "IDs dos produtos",
                    "location": "query",
                    "name": "idsProdutos[]",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_produtos",
                },
                {
                    "description": "Códigos dos produtos",
                    "location": "query",
                    "name": "codigos[]",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "codigos",
                },
                {
                    "description": "Filtra o saldo em estoque <br> `0` zerado <br> `1` positivo <br> "
                    "`2` negativo",
                    "location": "query",
                    "name": "filtroSaldoEstoque",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "filtro_saldo_estoque",
                },
            ],
            "path": "/estoques/saldos/{idDeposito}",
            "request_schema_refs": [],
            "resource": "Estoques",
            "response_schema_refs": {
                "200": ["EstoquesSaldosBaseDTO"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter_saldos_por_deposito",
            "summary": "Obtém o saldo em estoque de produtos por depósito",
        }
    ),
}
