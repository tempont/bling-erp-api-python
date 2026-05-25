"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

PRODUCT_SUPPLIER_OPERATIONS: dict[str, OperationContract] = {
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém produtos fornecedores paginados.",
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
                    "description": "ID do contato do tipo fornecedor",
                    "location": "query",
                    "name": "idFornecedor",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_fornecedor",
                },
            ],
            "path": "/produtos/fornecedores",
            "request_schema_refs": [],
            "resource": "ProdutosFornecedores",
            "response_schema_refs": {"200": ["ProdutosFornecedoresDadosBaseDTO"]},
            "sdk_method": "listar",
            "summary": "Obtém produtos fornecedores",
        }
    ),
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria um produto fornecedor.",
            "method": "POST",
            "parameters": [],
            "path": "/produtos/fornecedores",
            "request_schema_refs": [
                "ProdutosFornecedoresDadosBaseDTO",
                "ProdutosFornecedoresDadosDTO",
            ],
            "resource": "ProdutosFornecedores",
            "response_schema_refs": {"201": ["BasePostResponse"], "400": ["ErrorResponse"]},
            "sdk_method": "criar",
            "summary": "Cria um produto fornecedor",
        }
    ),
    "remover": OperationContract.model_validate(
        {
            "action": "Remover",
            "description": "Remove um produto fornecedor pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID do produto fornecedor",
                    "location": "path",
                    "name": "idProdutoFornecedor",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto_fornecedor",
                }
            ],
            "path": "/produtos/fornecedores/{idProdutoFornecedor}",
            "request_schema_refs": [],
            "resource": "ProdutosFornecedores",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "remover",
            "summary": "Remove um produto fornecedor",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém um produto fornecedor pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do produto fornecedor",
                    "location": "path",
                    "name": "idProdutoFornecedor",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto_fornecedor",
                }
            ],
            "path": "/produtos/fornecedores/{idProdutoFornecedor}",
            "request_schema_refs": [],
            "resource": "ProdutosFornecedores",
            "response_schema_refs": {
                "200": ["ProdutosFornecedoresDadosBaseDTO", "ProdutosFornecedoresDadosDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter",
            "summary": "Obtém um produto fornecedor",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera um produto fornecedor pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID do produto fornecedor",
                    "location": "path",
                    "name": "idProdutoFornecedor",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto_fornecedor",
                }
            ],
            "path": "/produtos/fornecedores/{idProdutoFornecedor}",
            "request_schema_refs": [
                "ProdutosFornecedoresDadosBaseUpdateDTO",
                "ProdutosFornecedoresDadosUpdateDTO",
            ],
            "resource": "ProdutosFornecedores",
            "response_schema_refs": {
                "200": ["BasePostResponse"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "alterar",
            "summary": "Altera um produto fornecedor",
        }
    ),
}
