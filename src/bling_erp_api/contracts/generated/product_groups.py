"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

PRODUCT_GROUP_OPERATIONS: dict[str, OperationContract] = {
    "remover_varios": OperationContract.model_validate(
        {
            "action": "RemoverMultiplos",
            "description": "Remove múltiplos grupos de produtos pelos IDs.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "IDs dos grupos de produtos",
                    "location": "query",
                    "name": "idsGruposProdutos[]",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_grupos_produtos",
                }
            ],
            "path": "/grupos-produtos",
            "request_schema_refs": [],
            "resource": "GruposProdutos",
            "response_schema_refs": {"200": ["ErrorResponse"], "400": ["ErrorResponse"]},
            "sdk_method": "remover_varios",
            "summary": "Remove múltiplos grupos de produtos",
        }
    ),
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém grupos de produtos paginados.",
            "method": "GET",
            "parameters": [
                {
                    "description": "O nome do grupo",
                    "location": "query",
                    "name": "nome",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "nome",
                },
                {
                    "description": "O nome do grupo pai",
                    "location": "query",
                    "name": "nomePai",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "nome_pai",
                },
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
            ],
            "path": "/grupos-produtos",
            "request_schema_refs": [],
            "resource": "GruposProdutos",
            "response_schema_refs": {"200": ["GruposProdutosDadosDTO"]},
            "sdk_method": "listar",
            "summary": "Obtém grupos de produtos",
        }
    ),
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria um grupo de produtos.",
            "method": "POST",
            "parameters": [],
            "path": "/grupos-produtos",
            "request_schema_refs": ["GruposProdutosDadosDTO", "GruposProdutosGrupoProdutoPaiDTO"],
            "resource": "GruposProdutos",
            "response_schema_refs": {"201": ["BasePostResponse"], "400": ["ErrorResponse"]},
            "sdk_method": "criar",
            "summary": "Cria um grupo de produtos",
        }
    ),
    "remover": OperationContract.model_validate(
        {
            "action": "Remover",
            "description": "Remove um grupo de produtos pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID do grupo de produto",
                    "location": "path",
                    "name": "idGrupoProduto",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_grupo_produto",
                }
            ],
            "path": "/grupos-produtos/{idGrupoProduto}",
            "request_schema_refs": [],
            "resource": "GruposProdutos",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "remover",
            "summary": "Remove um grupo de produtos",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém um grupo de produtos pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do grupo de produto",
                    "location": "path",
                    "name": "idGrupoProduto",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_grupo_produto",
                }
            ],
            "path": "/grupos-produtos/{idGrupoProduto}",
            "request_schema_refs": [],
            "resource": "GruposProdutos",
            "response_schema_refs": {
                "200": ["GruposProdutosDadosDTO", "GruposProdutosGrupoProdutoPaiDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter",
            "summary": "Obtém um grupo de produtos",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera um grupo de produtos pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID do grupo de produto",
                    "location": "path",
                    "name": "idGrupoProduto",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_grupo_produto",
                }
            ],
            "path": "/grupos-produtos/{idGrupoProduto}",
            "request_schema_refs": ["GruposProdutosDadosDTO", "GruposProdutosGrupoProdutoPaiDTO"],
            "resource": "GruposProdutos",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "alterar",
            "summary": "Altera um grupo de produtos",
        }
    ),
}
