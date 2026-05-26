"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

CAIXAS_BANCOS_OPERATIONS: dict[str, OperationContract] = {
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém lista de lançamentos de caixas e bancos.",
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
                    "description": "Data inicial de consulta de movimentações, só serão retornados os "
                    "lançamento a partir dessa data. Caso não informado, o padrão será "
                    "o primeiro dia do mês atual.",
                    "location": "query",
                    "name": "dataInicial",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_inicial",
                },
                {
                    "description": "Data final de consulta de movimentações, só serão retornados os "
                    "lançamento até essa data. Caso não informado, o padrão será o "
                    "último dia do mês atual.",
                    "location": "query",
                    "name": "dataFinal",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_final",
                },
                {
                    "description": "IDs das categorias de movimentações.",
                    "location": "query",
                    "name": "idsCategorias",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_categorias",
                },
                {
                    "description": "ID da conta financeira.",
                    "location": "query",
                    "name": "idContaFinanceira",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_conta_financeira",
                },
                {
                    "description": "Pesquisa por descrição do lançamento.",
                    "location": "query",
                    "name": "pesquisa",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "pesquisa",
                },
                {
                    "description": "Valor do lançamento.",
                    "location": "query",
                    "name": "valor",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "number",
                    "sdk_name": "valor",
                },
                {
                    "description": "Situação da conciliação do lançamento <br> `1` Registros "
                    "conciliados <br> `2` Registros não conciliados <br> `3` Todos os "
                    "registros",
                    "location": "query",
                    "name": "situacaoConciliacao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "situacao_conciliacao",
                },
                {
                    "description": "Situação do lançamento.<br>'R' para registros<br>'E' para "
                    "excluídos",
                    "location": "query",
                    "name": "situacao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "situacao",
                },
            ],
            "path": "/caixas",
            "request_schema_refs": [],
            "resource": "Caixas",
            "response_schema_refs": {
                "200": ["CaixasBancosItemLancamentoDTO"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "listar",
            "summary": "Obtém lista de lançamentos de caixas e bancos.",
        }
    ),
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria um novo lançamento de caixa e banco com os dados fornecidos.",
            "method": "POST",
            "parameters": [],
            "path": "/caixas",
            "request_schema_refs": ["CaixasBancosSalvarLancamentoDTO"],
            "resource": "Caixas",
            "response_schema_refs": {
                "201": ["CaixasBancosSalvarLancamentoResponseDTO"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "criar",
            "summary": "Cria um novo lançamento de caixa e banco.",
        }
    ),
    "remover": OperationContract.model_validate(
        {
            "action": "Remover",
            "description": "Remove um lançamento de caixa e banco pelo ID. O registro não é excluído "
            "permanentemente, apenas marcado como excluído (exclusão lógica).",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID do lançamento de caixa e banco a ser excluído.",
                    "location": "path",
                    "name": "idCaixa",
                    "required": True,
                    "schema_format": "int64",
                    "schema_type": "integer",
                    "sdk_name": "id_caixa",
                }
            ],
            "path": "/caixas/{idCaixa}",
            "request_schema_refs": [],
            "resource": "Caixas",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "remover",
            "summary": "Remove um lançamento de caixa e banco",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém um lançamento de caixa e banco.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do lançamento de caixas e bancos",
                    "location": "path",
                    "name": "idCaixa",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_caixa",
                }
            ],
            "path": "/caixas/{idCaixa}",
            "request_schema_refs": [],
            "resource": "Caixas",
            "response_schema_refs": {
                "200": ["CaixasBancosLancamentoDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter",
            "summary": "Obtém um lançamento de caixa e banco.",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Atualiza um lançamento de caixa e banco existente com os dados fornecidos.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID do lançamento de caixas e bancos",
                    "location": "path",
                    "name": "idCaixa",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_caixa",
                }
            ],
            "path": "/caixas/{idCaixa}",
            "request_schema_refs": ["CaixasBancosSalvarLancamentoDTO"],
            "resource": "Caixas",
            "response_schema_refs": {
                "200": ["CaixasBancosSalvarLancamentoResponseDTO"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "alterar",
            "summary": "Atualiza um lançamento de caixa e banco.",
        }
    ),
}
