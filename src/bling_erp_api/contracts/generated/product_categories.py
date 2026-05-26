"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

PRODUCT_CATEGORY_OPERATIONS: dict[str, OperationContract] = {
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém categorias de produtos paginadas.",
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
            ],
            "path": "/categorias/produtos",
            "request_schema_refs": [],
            "resource": "CategoriasProdutos",
            "response_schema_refs": {
                "200": ["CategoriasProdutosCategoriPaiDTO", "CategoriasProdutosDadosDTO"]
            },
            "sdk_method": "listar",
            "summary": "Obtém categorias de produtos",
        }
    ),
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria uma categoria de produto.",
            "method": "POST",
            "parameters": [],
            "path": "/categorias/produtos",
            "request_schema_refs": [
                "CategoriasProdutosCategoriPaiDTO",
                "CategoriasProdutosDadosDTO",
            ],
            "resource": "CategoriasProdutos",
            "response_schema_refs": {"201": ["BasePostResponse"], "400": ["ErrorResponse"]},
            "sdk_method": "criar",
            "summary": "Cria uma categoria de produto",
        }
    ),
    "remover": OperationContract.model_validate(
        {
            "action": "Remover",
            "description": "Remove uma categoria de produto pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID da categoria de produto",
                    "location": "path",
                    "name": "idCategoriaProduto",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_categoria_produto",
                }
            ],
            "path": "/categorias/produtos/{idCategoriaProduto}",
            "request_schema_refs": [],
            "resource": "CategoriasProdutos",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "remover",
            "summary": "Remove uma categoria de produto",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém uma categoria de produto pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID da categoria de produto",
                    "location": "path",
                    "name": "idCategoriaProduto",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_categoria_produto",
                }
            ],
            "path": "/categorias/produtos/{idCategoriaProduto}",
            "request_schema_refs": [],
            "resource": "CategoriasProdutos",
            "response_schema_refs": {
                "200": ["CategoriasProdutosCategoriPaiDTO", "CategoriasProdutosDadosDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter",
            "summary": "Obtém uma categoria de produto",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera uma categoria de produto pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID da categoria de produto",
                    "location": "path",
                    "name": "idCategoriaProduto",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_categoria_produto",
                }
            ],
            "path": "/categorias/produtos/{idCategoriaProduto}",
            "request_schema_refs": ["CategoriasProdutosDadosDTO"],
            "resource": "CategoriasProdutos",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "alterar",
            "summary": "Altera uma categoria de produto",
        }
    ),
}
