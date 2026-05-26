"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

STORE_CATEGORY_OPERATIONS: dict[str, OperationContract] = {
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém categorias de lojas virtuais vinculadas a de produtos paginadas.",
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
                    "description": "ID da loja",
                    "location": "query",
                    "name": "idLoja",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_loja",
                },
                {
                    "description": "ID da categoria do produto",
                    "location": "query",
                    "name": "idCategoriaProduto",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_categoria_produto",
                },
                {
                    "description": "ID da categoria do produto pai",
                    "location": "query",
                    "name": "idCategoriaProdutoPai",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_categoria_produto_pai",
                },
            ],
            "path": "/categorias/lojas",
            "request_schema_refs": [],
            "resource": "CategoriasLojas",
            "response_schema_refs": {"200": ["CategoriasLojasDadosDTO"]},
            "sdk_method": "listar",
            "summary": "Obtém categorias de lojas virtuais vinculadas a de produtos",
        }
    ),
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria o vínculo de uma categoria da loja com a de produto.",
            "method": "POST",
            "parameters": [],
            "path": "/categorias/lojas",
            "request_schema_refs": ["CategoriasLojasDadosDTO"],
            "resource": "CategoriasLojas",
            "response_schema_refs": {"201": ["BasePostResponse"], "400": ["ErrorResponse"]},
            "sdk_method": "criar",
            "summary": "Cria o vínculo de uma categoria da loja com a de produto",
        }
    ),
    "remover": OperationContract.model_validate(
        {
            "action": "Remover",
            "description": "Remove o vínculo de uma categoria da loja com a de produto pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID do vínculo da categoria de produto com a da loja",
                    "location": "path",
                    "name": "idCategoriaLoja",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_categoria_loja",
                }
            ],
            "path": "/categorias/lojas/{idCategoriaLoja}",
            "request_schema_refs": [],
            "resource": "CategoriasLojas",
            "response_schema_refs": {"404": ["ErrorResponse"]},
            "sdk_method": "remover",
            "summary": "Remove o vínculo de uma categoria da loja com a de produto",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém uma categoria da loja vinculada a de produto pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do vínculo da categoria de produto com a da loja",
                    "location": "path",
                    "name": "idCategoriaLoja",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_categoria_loja",
                }
            ],
            "path": "/categorias/lojas/{idCategoriaLoja}",
            "request_schema_refs": [],
            "resource": "CategoriasLojas",
            "response_schema_refs": {"200": ["CategoriasLojasDadosDTO"], "404": ["ErrorResponse"]},
            "sdk_method": "obter",
            "summary": "Obtém uma categoria da loja vinculada a de produto",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera o vínculo de uma categoria da loja com a de produto pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID do vínculo da categoria de produto com a da loja",
                    "location": "path",
                    "name": "idCategoriaLoja",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_categoria_loja",
                }
            ],
            "path": "/categorias/lojas/{idCategoriaLoja}",
            "request_schema_refs": ["CategoriasLojasDadosDTO"],
            "resource": "CategoriasLojas",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "alterar",
            "summary": "Altera o vínculo de uma categoria da loja com a de produto",
        }
    ),
}
