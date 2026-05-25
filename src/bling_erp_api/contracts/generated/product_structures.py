"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

PRODUCT_STRUCTURE_OPERATIONS: dict[str, OperationContract] = {
    "remover_varios": OperationContract.model_validate(
        {
            "action": "RemoverMultiplos",
            "description": "Remove a estrutura de múltiplos produtos com composição pelos IDs.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "IDs dos produtos",
                    "location": "query",
                    "name": "idsProdutos[]",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_produtos",
                }
            ],
            "path": "/produtos/estruturas",
            "request_schema_refs": [],
            "resource": "ProdutosEstruturas",
            "response_schema_refs": {"200": ["Error"], "400": ["ErrorResponse"]},
            "sdk_method": "remover_varios",
            "summary": "Remove a estrutura de múltiplos produtos",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém a estrutura de um produto com composição pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do produto com composição",
                    "location": "path",
                    "name": "idProdutoEstrutura",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto_estrutura",
                }
            ],
            "path": "/produtos/estruturas/{idProdutoEstrutura}",
            "request_schema_refs": [],
            "resource": "ProdutosEstruturas",
            "response_schema_refs": {"200": ["ProdutosEstruturaDTO"], "404": ["ErrorResponse"]},
            "sdk_method": "obter",
            "summary": "Obtém a estrutura de um produto com composição",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera a estrutura de um produto com composição pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID do produto com composição",
                    "location": "path",
                    "name": "idProdutoEstrutura",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto_estrutura",
                }
            ],
            "path": "/produtos/estruturas/{idProdutoEstrutura}",
            "request_schema_refs": ["ProdutosEstruturaDTO"],
            "resource": "ProdutosEstruturas",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "alterar",
            "summary": "Altera a estrutura de um produto com composição",
        }
    ),
    "remover_componentes": OperationContract.model_validate(
        {
            "action": "RemoverComponenteMultiplos",
            "description": "Remove os componentes de um produto com composição pelos IDs dos componentes.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID do produto com composição",
                    "location": "path",
                    "name": "idProdutoEstrutura",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto_estrutura",
                },
                {
                    "description": "IDs dos produtos",
                    "location": "query",
                    "name": "idsComponentes[]",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_componentes",
                },
            ],
            "path": "/produtos/estruturas/{idProdutoEstrutura}/componentes",
            "request_schema_refs": [],
            "resource": "ProdutosEstruturas",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "remover_componentes",
            "summary": "Remove componentes específicos de um produto com composição",
        }
    ),
    "vincular_componentes": OperationContract.model_validate(
        {
            "action": "VincularComponenteMultiplos",
            "description": "Adiciona múltiplos componentes a uma estrutura pelo ID.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID do produto com composição",
                    "location": "path",
                    "name": "idProdutoEstrutura",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto_estrutura",
                }
            ],
            "path": "/produtos/estruturas/{idProdutoEstrutura}/componentes",
            "request_schema_refs": ["ProdutosComponenteDTO"],
            "resource": "ProdutosEstruturas",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "vincular_componentes",
            "summary": "Adiciona componente(s) a uma estrutura",
        }
    ),
    "alterar_componente": OperationContract.model_validate(
        {
            "action": "AlterarComponente",
            "description": "Altera um componente de uma estrutura pelo ID.",
            "method": "PATCH",
            "parameters": [
                {
                    "description": "ID do produto com composição",
                    "location": "path",
                    "name": "idProdutoEstrutura",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_produto_estrutura",
                },
                {
                    "description": "ID do componente",
                    "location": "path",
                    "name": "idComponente",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_componente",
                },
            ],
            "path": "/produtos/estruturas/{idProdutoEstrutura}/componentes/{idComponente}",
            "request_schema_refs": ["ProdutosComponenteDTO"],
            "resource": "ProdutosEstruturas",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "alterar_componente",
            "summary": "Altera um componente de uma estrutura",
        }
    ),
}
