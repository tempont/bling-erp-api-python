"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

PRODUCT_BATCH_ENTRY_OPERATIONS: dict[str, OperationContract] = {
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém um lançamento de um lote de produto pelo ID do lançamento.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do lançamento",
                    "location": "path",
                    "name": "idLancamento",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_lancamento",
                }
            ],
            "path": "/produtos/lotes/lancamentos/{idLancamento}",
            "request_schema_refs": [],
            "resource": "LotesLancamentos",
            "response_schema_refs": {
                "200": ["LoteLancamentoDTO"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter",
            "summary": "Obtém um lançamento de um lote de produto",
        }
    ),
    "alterar_atributo": OperationContract.model_validate(
        {
            "action": "AlterarAtributo",
            "description": "Altera a observação de um lançamento de um lote de um produto pelo ID do "
            "lançamento.",
            "method": "PATCH",
            "parameters": [],
            "path": "/produtos/lotes/lancamentos/{idLancamento}",
            "request_schema_refs": ["LoteLancamentoObservacaoDTO"],
            "resource": "LotesLancamentos",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "alterar_atributo",
            "summary": "Altera a observação de um lançamento de um lote de um produto",
        }
    ),
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém os lançamentos de um lote de produto pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do lote",
                    "location": "path",
                    "name": "idLote",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_lote",
                }
            ],
            "path": "/produtos/lotes/{idLote}/lancamentos",
            "request_schema_refs": [],
            "resource": "LotesLancamentos",
            "response_schema_refs": {
                "200": ["LoteLancamentoDTO"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "listar",
            "summary": "Obtém os lançamentos de um lote de produto",
        }
    ),
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Inclui lançamento de um lote.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID do lote",
                    "location": "path",
                    "name": "idLote",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_lote",
                }
            ],
            "path": "/produtos/lotes/{idLote}/lancamentos",
            "request_schema_refs": ["LoteLancamentoDTO"],
            "resource": "LotesLancamentos",
            "response_schema_refs": {
                "200": ["LoteLancamentoDTO"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "criar",
            "summary": "Cria um lançamento de um lote",
        }
    ),
    "obter_saldos": OperationContract.model_validate(
        {
            "action": "ObterSaldosLote",
            "description": "Obtém os saldos dos lotes de um produto por depósito.",
            "method": "GET",
            "parameters": [
                {
                    "description": "IDs dos lotes",
                    "location": "query",
                    "name": "idsLotes[]",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_lotes",
                },
                {
                    "description": "ID do produto",
                    "location": "path",
                    "name": "idProduto",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto",
                },
                {
                    "description": "ID do depósito",
                    "location": "path",
                    "name": "idDeposito",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_deposito",
                },
            ],
            "path": "/produtos/{idProduto}/lotes/depositos/{idDeposito}/saldo",
            "request_schema_refs": [],
            "resource": "LotesLancamentos",
            "response_schema_refs": {
                "200": ["SaldoLoteDTO"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter_saldos",
            "summary": "Obtém os saldos dos lotes de um produto por depósito",
        }
    ),
    "obter_saldos_soma": OperationContract.model_validate(
        {
            "action": "ObterSaldosLote",
            "description": "Obtém o saldo total dos lotes de um produto pelo ID do produto.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do produto",
                    "location": "path",
                    "name": "idProduto",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto",
                }
            ],
            "path": "/produtos/{idProduto}/lotes/saldo/soma",
            "request_schema_refs": [],
            "resource": "LotesLancamentos",
            "response_schema_refs": {
                "200": ["SaldoSomaLotesTodosDepositosDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter_saldos",
            "summary": "Obtém o saldo total dos lotes de um produto",
        }
    ),
    "obter_saldos_saldo": OperationContract.model_validate(
        {
            "action": "ObterSaldosLote",
            "description": "Obtém o saldo de um lote de produto.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do lote",
                    "location": "path",
                    "name": "idLote",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_lote",
                },
                {
                    "description": "ID do produto",
                    "location": "path",
                    "name": "idProduto",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto",
                },
                {
                    "description": "ID do depósito",
                    "location": "path",
                    "name": "idDeposito",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_deposito",
                },
            ],
            "path": "/produtos/{idProduto}/lotes/{idLote}/depositos/{idDeposito}/saldo",
            "request_schema_refs": [],
            "resource": "LotesLancamentos",
            "response_schema_refs": {"200": ["SaldoLoteDTO"], "404": ["ErrorResponse"]},
            "sdk_method": "obter_saldos",
            "summary": "Obtém o saldo de um lote de produto",
        }
    ),
}
