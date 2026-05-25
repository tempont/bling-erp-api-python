"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

PRODUCT_STORE_OPERATIONS: dict[str, OperationContract] = {
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém vínculos de produtos com lojas paginados.",
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
                    "description": "ID do produto",
                    "location": "query",
                    "name": "idProduto",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto",
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
                    "description": "ID da categoria do produto vinculada à loja",
                    "location": "query",
                    "name": "idCategoriaProduto",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_categoria_produto",
                },
                {
                    "description": "Data de alteração inicial",
                    "location": "query",
                    "name": "dataAlteracaoInicial",
                    "required": False,
                    "schema_format": "datetime",
                    "schema_type": "string",
                    "sdk_name": "data_alteracao_inicial",
                },
                {
                    "description": "Data de alteração final",
                    "location": "query",
                    "name": "dataAlteracaoFinal",
                    "required": False,
                    "schema_format": "datetime",
                    "schema_type": "string",
                    "sdk_name": "data_alteracao_final",
                },
            ],
            "path": "/produtos/lojas",
            "request_schema_refs": [],
            "resource": "ProdutosLojas",
            "response_schema_refs": {"200": ["ProdutosLojasDadosDTO"], "400": ["ErrorResponse"]},
            "sdk_method": "listar",
            "summary": "Obtém vínculos de produtos com lojas",
        }
    ),
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria o vínculo de um produto com uma loja.",
            "method": "POST",
            "parameters": [],
            "path": "/produtos/lojas",
            "request_schema_refs": ["ProdutosLojasDadosBaseDTO", "ProdutosLojasDadosDTO"],
            "resource": "ProdutosLojas",
            "response_schema_refs": {
                "201": ["BasePostResponse", "ProdutosLojasResponse_POST_PUT"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "criar",
            "summary": "Cria o vínculo de um produto com uma loja",
        }
    ),
    "remover": OperationContract.model_validate(
        {
            "action": "Remover",
            "description": "Remove o vínculo de um produto com uma loja pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID do vínculo do produto com a loja",
                    "location": "path",
                    "name": "idProdutoLoja",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto_loja",
                }
            ],
            "path": "/produtos/lojas/{idProdutoLoja}",
            "request_schema_refs": [],
            "resource": "ProdutosLojas",
            "response_schema_refs": {"404": ["ErrorResponse"]},
            "sdk_method": "remover",
            "summary": "Remove o vínculo de um produto com uma loja",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém um vínculo de produto com loja pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do vínculo do produto com a loja",
                    "location": "path",
                    "name": "idProdutoLoja",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto_loja",
                }
            ],
            "path": "/produtos/lojas/{idProdutoLoja}",
            "request_schema_refs": [],
            "resource": "ProdutosLojas",
            "response_schema_refs": {
                "200": ["ProdutosLojasDadosBaseDTO", "ProdutosLojasDadosDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter",
            "summary": "Obtém um vínculo de produto com loja",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera o vínculo de um produto com uma loja pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID do vínculo do produto com a loja",
                    "location": "path",
                    "name": "idProdutoLoja",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto_loja",
                }
            ],
            "path": "/produtos/lojas/{idProdutoLoja}",
            "request_schema_refs": ["ProdutosLojasDadosBaseDTO", "ProdutosLojasDadosDTO"],
            "resource": "ProdutosLojas",
            "response_schema_refs": {
                "200": ["BasePostResponse", "ProdutosLojasResponse_POST_PUT"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "alterar",
            "summary": "Altera o vínculo de um produto com uma loja",
        }
    ),
}
