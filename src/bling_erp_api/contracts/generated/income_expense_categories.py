"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

INCOME_EXPENSE_CATEGORY_OPERATIONS: dict[str, OperationContract] = {
    "remover_varios": OperationContract.model_validate(
        {
            "action": "RemoverMultiplos",
            "description": "Remove múltiplas categorias de receita e despesa a partir de uma lista de IDs.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "IDs das categorias a serem removidas",
                    "location": "query",
                    "name": "idsCategorias[]",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_categorias",
                }
            ],
            "path": "/categorias/receitas-despesas",
            "request_schema_refs": [],
            "resource": "CategoriasReceitasDespesas",
            "response_schema_refs": {"200": ["ErrorResponse"]},
            "sdk_method": "remover_varios",
            "summary": "Remove múltiplas categorias de receita e despesa",
        }
    ),
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém categorias de receitas e despesas paginadas.",
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
                    "description": "`0` Todas<br>`1` Despesa<br>`2` Receita<br>`3` Receita e despesa",
                    "location": "query",
                    "name": "tipo",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "tipo",
                },
                {
                    "description": "`0` Ativas e Inativas<br>`1` Ativas<br>`2` Inativas",
                    "location": "query",
                    "name": "situacao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "situacao",
                },
            ],
            "path": "/categorias/receitas-despesas",
            "request_schema_refs": [],
            "resource": "CategoriasReceitasDespesas",
            "response_schema_refs": {"200": ["CategoriasReceitasDespesasDadosBaseDTO"]},
            "sdk_method": "listar",
            "summary": "Obtém categorias de receitas e despesas",
        }
    ),
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria uma categoria de receita e despesa.",
            "method": "POST",
            "parameters": [],
            "path": "/categorias/receitas-despesas",
            "request_schema_refs": [
                "CategoriasReceitasDespesasDadosBaseDTO",
                "CategoriasReceitasDespesasDadosPostDTO",
            ],
            "resource": "CategoriasReceitasDespesas",
            "response_schema_refs": {
                "201": ["CategoriasReceitasDespesasDadosBaseDTO"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "criar",
            "summary": "Cria uma categoria de receita e despesa",
        }
    ),
    "remover": OperationContract.model_validate(
        {
            "action": "Remover",
            "description": "Remove uma categoria de receita e despesa pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID da categoria de receita e despesa",
                    "location": "path",
                    "name": "idCategoria",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_categoria",
                }
            ],
            "path": "/categorias/receitas-despesas/{idCategoria}",
            "request_schema_refs": [],
            "resource": "CategoriasReceitasDespesas",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "remover",
            "summary": "Remove uma categoria de receita e despesa",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém uma categoria de receita e despesa pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID da categoria de receita e despesa",
                    "location": "path",
                    "name": "idCategoria",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_categoria",
                }
            ],
            "path": "/categorias/receitas-despesas/{idCategoria}",
            "request_schema_refs": [],
            "resource": "CategoriasReceitasDespesas",
            "response_schema_refs": {
                "200": [
                    "CategoriasReceitasDespesasDadosBaseDTO",
                    "CategoriasReceitasDespesasDadosDTO",
                ],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter",
            "summary": "Obtém uma categoria de receita e despesa",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Atualiza uma categoria de receita e despesa a partir do ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID da categoria de receita e despesa",
                    "location": "path",
                    "name": "idCategoria",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_categoria",
                }
            ],
            "path": "/categorias/receitas-despesas/{idCategoria}",
            "request_schema_refs": [
                "CategoriasReceitasDespesasDadosBaseDTO",
                "CategoriasReceitasDespesasDadosPostDTO",
            ],
            "resource": "CategoriasReceitasDespesas",
            "response_schema_refs": {
                "200": ["CategoriasReceitasDespesasDadosBaseDTO"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "alterar",
            "summary": "Atualiza uma categoria de receita e despesa",
        }
    ),
}
