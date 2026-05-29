"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

PURCHASE_ORDER_OPERATIONS: dict[str, OperationContract] = {
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém pedidos de compras paginados.",
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
                    "description": "ID do contato do tipo fornecedor",
                    "location": "query",
                    "name": "idFornecedor",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_fornecedor",
                },
                {
                    "description": "Valor da situação",
                    "location": "query",
                    "name": "valorSituacao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "valor_situacao",
                },
                {
                    "description": "ID da situação",
                    "location": "query",
                    "name": "idSituacao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_situacao",
                },
                {
                    "description": "Data inicial do período da compra",
                    "location": "query",
                    "name": "dataInicial",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_inicial",
                },
                {
                    "description": "Data final do período da compra",
                    "location": "query",
                    "name": "dataFinal",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_final",
                },
                {
                    "description": "IDs das notas fiscais de entrada",
                    "location": "query",
                    "name": "idsNotasFiscais[]",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_notas_fiscais",
                },
            ],
            "path": "/pedidos/compras",
            "request_schema_refs": [],
            "resource": "PedidosCompra",
            "response_schema_refs": {"200": ["PedidosComprasDadosBaseDTO"]},
            "sdk_method": "listar",
            "summary": "Obtém pedidos de compras",
        }
    ),
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria um pedido de compra.",
            "method": "POST",
            "parameters": [],
            "path": "/pedidos/compras",
            "request_schema_refs": ["PedidosComprasDadosBaseDTO", "PedidosComprasDadosDTO"],
            "resource": "PedidosCompra",
            "response_schema_refs": {
                "201": ["BasePostResponse", "PedidosCompraResponse_POST_PUT"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "criar",
            "summary": "Cria um pedido de compra",
        }
    ),
    "remover": OperationContract.model_validate(
        {
            "action": "Remover",
            "description": "Remove um pedido de compra pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID do pedido de compra",
                    "location": "path",
                    "name": "idPedidoCompra",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_pedido_compra",
                }
            ],
            "path": "/pedidos/compras/{idPedidoCompra}",
            "request_schema_refs": [],
            "resource": "PedidosCompra",
            "response_schema_refs": {"404": ["ErrorResponse"]},
            "sdk_method": "remover",
            "summary": "Remove um pedido de compra",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém um pedido de compra pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do pedido de compra",
                    "location": "path",
                    "name": "idPedidoCompra",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_pedido_compra",
                }
            ],
            "path": "/pedidos/compras/{idPedidoCompra}",
            "request_schema_refs": [],
            "resource": "PedidosCompra",
            "response_schema_refs": {
                "200": ["PedidosComprasDadosBaseDTO", "PedidosComprasDadosDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter",
            "summary": "Obtém um pedido de compra",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera um pedido de compra pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID do pedido de compra",
                    "location": "path",
                    "name": "idPedidoCompra",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_pedido_compra",
                }
            ],
            "path": "/pedidos/compras/{idPedidoCompra}",
            "request_schema_refs": ["PedidosComprasDadosBaseDTO", "PedidosComprasDadosDTO"],
            "resource": "PedidosCompra",
            "response_schema_refs": {
                "200": ["BasePostResponse", "PedidosCompraResponse_POST_PUT"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "alterar",
            "summary": "Altera um pedido de compra",
        }
    ),
    "estornar_contas": OperationContract.model_validate(
        {
            "action": "EstornarContas",
            "description": "Estorna as contas de um pedido de compra pelo ID.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID do pedido de compra",
                    "location": "path",
                    "name": "idPedidoCompra",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_pedido_compra",
                }
            ],
            "path": "/pedidos/compras/{idPedidoCompra}/estornar-contas",
            "request_schema_refs": [],
            "resource": "PedidosCompra",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "estornar_contas",
            "summary": "Estorna as contas de um pedido de compra",
        }
    ),
    "estornar_estoque": OperationContract.model_validate(
        {
            "action": "EstornarEstoque",
            "description": "Estorna o estoque de um pedido de compra pelo ID.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID do pedido de compra",
                    "location": "path",
                    "name": "idPedidoCompra",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_pedido_compra",
                }
            ],
            "path": "/pedidos/compras/{idPedidoCompra}/estornar-estoque",
            "request_schema_refs": [],
            "resource": "PedidosCompra",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "estornar_estoque",
            "summary": "Estorna o estoque de um pedido de compra",
        }
    ),
    "lancar_contas": OperationContract.model_validate(
        {
            "action": "LancarContas",
            "description": "Lança as contas de um pedido de compra pelo ID.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID do pedido de compra",
                    "location": "path",
                    "name": "idPedidoCompra",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_pedido_compra",
                }
            ],
            "path": "/pedidos/compras/{idPedidoCompra}/lancar-contas",
            "request_schema_refs": [],
            "resource": "PedidosCompra",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "lancar_contas",
            "summary": "Lança as contas de um pedido de compra",
        }
    ),
    "lancar_estoque": OperationContract.model_validate(
        {
            "action": "LancarEstoque",
            "description": "Lança o estoque de um pedido de compra pelo ID.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID do pedido de compra",
                    "location": "path",
                    "name": "idPedidoCompra",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_pedido_compra",
                }
            ],
            "path": "/pedidos/compras/{idPedidoCompra}/lancar-estoque",
            "request_schema_refs": [],
            "resource": "PedidosCompra",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "lancar_estoque",
            "summary": "Lança o estoque de um pedido de compra",
        }
    ),
    "alterar_situacao": OperationContract.model_validate(
        {
            "action": "AlterarSituacao",
            "description": "Altera a situação de um pedido de compra pelo ID.",
            "method": "PATCH",
            "parameters": [
                {
                    "description": "ID do pedido de compra",
                    "location": "path",
                    "name": "idPedidoCompra",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_pedido_compra",
                },
                {
                    "description": "ID da situação do pedido de compra",
                    "location": "path",
                    "name": "idSituacao",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_situacao",
                },
            ],
            "path": "/pedidos/compras/{idPedidoCompra}/situacoes/{idSituacao}",
            "request_schema_refs": [],
            "resource": "PedidosCompra",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "alterar_situacao",
            "summary": "Altera a situação de um pedido de compra",
        }
    ),
}
