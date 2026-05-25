"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

SALES_ORDER_OPERATIONS: dict[str, OperationContract] = {
    "remover_varios": OperationContract.model_validate(
        {
            "action": "RemoverMultiplos",
            "description": "Remove pedidos de vendas pelos IDs.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "IDs dos pedidos de vendas",
                    "location": "query",
                    "name": "idsPedidosVendas[]",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_pedidos_vendas",
                }
            ],
            "path": "/pedidos/vendas",
            "request_schema_refs": [],
            "resource": "PedidosVenda",
            "response_schema_refs": {},
            "sdk_method": "remover_varios",
            "summary": "Remove pedidos de vendas",
        }
    ),
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém pedidos de vendas paginados.",
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
                    "description": "ID do contato",
                    "location": "query",
                    "name": "idContato",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_contato",
                },
                {
                    "description": "Conjunto de situações",
                    "location": "query",
                    "name": "idsSituacoes[]",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_situacoes",
                },
                {
                    "description": "Data incial",
                    "location": "query",
                    "name": "dataInicial",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_inicial",
                },
                {
                    "description": "Data final",
                    "location": "query",
                    "name": "dataFinal",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_final",
                },
                {
                    "description": "Data inicial da alteração",
                    "location": "query",
                    "name": "dataAlteracaoInicial",
                    "required": False,
                    "schema_format": "datetime",
                    "schema_type": "string",
                    "sdk_name": "data_alteracao_inicial",
                },
                {
                    "description": "Data final da alteração",
                    "location": "query",
                    "name": "dataAlteracaoFinal",
                    "required": False,
                    "schema_format": "datetime",
                    "schema_type": "string",
                    "sdk_name": "data_alteracao_final",
                },
                {
                    "description": "Data inicial prevista",
                    "location": "query",
                    "name": "dataPrevistaInicial",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_prevista_inicial",
                },
                {
                    "description": "Data final prevista",
                    "location": "query",
                    "name": "dataPrevistaFinal",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_prevista_final",
                },
                {
                    "description": "Número do pedido de venda",
                    "location": "query",
                    "name": "numero",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "numero",
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
                    "description": "ID do vendedor",
                    "location": "query",
                    "name": "idVendedor",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_vendedor",
                },
                {
                    "description": "ID do controle de caixa",
                    "location": "query",
                    "name": "idControleCaixa",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_controle_caixa",
                },
                {
                    "description": "Conjunto de números de pedidos nas lojas",
                    "location": "query",
                    "name": "numerosLojas[]",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "numeros_lojas",
                },
                {
                    "description": "ID da unidade de negócio (filial)",
                    "location": "query",
                    "name": "idUnidadeNegocio",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_unidade_negocio",
                },
            ],
            "path": "/pedidos/vendas",
            "request_schema_refs": [],
            "resource": "PedidosVenda",
            "response_schema_refs": {"200": ["VendasDadosBaseDTO"]},
            "sdk_method": "listar",
            "summary": "Obtém pedidos de vendas",
        }
    ),
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria um pedido de venda.",
            "method": "POST",
            "parameters": [],
            "path": "/pedidos/vendas",
            "request_schema_refs": ["VendasDadosBaseDTO", "VendasDadosDTO"],
            "resource": "PedidosVenda",
            "response_schema_refs": {
                "201": ["BasePostResponse", "VendasResponse_POST_PUT"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "criar",
            "summary": "Cria um pedido de venda",
        }
    ),
    "remover": OperationContract.model_validate(
        {
            "action": "Remover",
            "description": "Remove um pedido de venda pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID do pedido de venda",
                    "location": "path",
                    "name": "idPedidoVenda",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_pedido_venda",
                }
            ],
            "path": "/pedidos/vendas/{idPedidoVenda}",
            "request_schema_refs": [],
            "resource": "PedidosVenda",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "remover",
            "summary": "Remove um pedido de venda",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém um pedido de venda pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do pedido de venda",
                    "location": "path",
                    "name": "idPedidoVenda",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_pedido_venda",
                }
            ],
            "path": "/pedidos/vendas/{idPedidoVenda}",
            "request_schema_refs": [],
            "resource": "PedidosVenda",
            "response_schema_refs": {
                "200": ["VendasDadosBaseDTO", "VendasDadosDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter",
            "summary": "Obtém um pedido de venda",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera um pedido de venda pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID do pedido de venda",
                    "location": "path",
                    "name": "idPedidoVenda",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_pedido_venda",
                }
            ],
            "path": "/pedidos/vendas/{idPedidoVenda}",
            "request_schema_refs": ["VendasDadosBaseDTO_PUT", "VendasDadosDTO"],
            "resource": "PedidosVenda",
            "response_schema_refs": {
                "200": ["BasePostResponse", "VendasResponse_POST_PUT"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "alterar",
            "summary": "Altera um pedido de venda",
        }
    ),
    "estornar_contas": OperationContract.model_validate(
        {
            "action": "EstornarContas",
            "description": "Estorna as contas de um pedido de venda pelo ID.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID do pedido de venda",
                    "location": "path",
                    "name": "idPedidoVenda",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_pedido_venda",
                }
            ],
            "path": "/pedidos/vendas/{idPedidoVenda}/estornar-contas",
            "request_schema_refs": [],
            "resource": "PedidosVenda",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "estornar_contas",
            "summary": "Estorna as contas de um pedido de venda",
        }
    ),
    "estornar_estoque": OperationContract.model_validate(
        {
            "action": "EstornarEstoque",
            "description": "Estorna o estoque de um pedido de venda pelo ID.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID do pedido de venda",
                    "location": "path",
                    "name": "idPedidoVenda",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_pedido_venda",
                }
            ],
            "path": "/pedidos/vendas/{idPedidoVenda}/estornar-estoque",
            "request_schema_refs": [],
            "resource": "PedidosVenda",
            "response_schema_refs": {"404": ["ErrorResponse"]},
            "sdk_method": "estornar_estoque",
            "summary": "Estorna o estoque de um pedido de venda",
        }
    ),
    "gerar_nota_fiscal_consumidor": OperationContract.model_validate(
        {
            "action": "GerarNotaFiscalConsumidor",
            "description": "Gera nota fiscal de consumidor eletrônica a partir do pedido de venda pelo ID.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID do pedido de venda",
                    "location": "path",
                    "name": "idPedidoVenda",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_pedido_venda",
                }
            ],
            "path": "/pedidos/vendas/{idPedidoVenda}/gerar-nfce",
            "request_schema_refs": [],
            "resource": "PedidosVenda",
            "response_schema_refs": {
                "201": ["VendasCreateInvoiceResponseDTO"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "gerar_nota_fiscal_consumidor",
            "summary": "Gera nota fiscal de consumidor eletrônica a partir do pedido de venda",
        }
    ),
    "gerar_nota_fiscal": OperationContract.model_validate(
        {
            "action": "GerarNotaFiscal",
            "description": "Gera nota fiscal eletrônica a partir do pedido de venda pelo ID.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID do pedido de venda",
                    "location": "path",
                    "name": "idPedidoVenda",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_pedido_venda",
                }
            ],
            "path": "/pedidos/vendas/{idPedidoVenda}/gerar-nfe",
            "request_schema_refs": [],
            "resource": "PedidosVenda",
            "response_schema_refs": {
                "201": ["VendasCreateInvoiceResponseDTO"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "gerar_nota_fiscal",
            "summary": "Gera nota fiscal eletrônica a partir do pedido de venda",
        }
    ),
    "lancar_contas": OperationContract.model_validate(
        {
            "action": "LancarContas",
            "description": "Lança as contas de um pedido de venda pelo ID.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID do pedido de venda",
                    "location": "path",
                    "name": "idPedidoVenda",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_pedido_venda",
                }
            ],
            "path": "/pedidos/vendas/{idPedidoVenda}/lancar-contas",
            "request_schema_refs": [],
            "resource": "PedidosVenda",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "lancar_contas",
            "summary": "Lança as contas de um pedido de venda",
        }
    ),
    "lancar_estoque": OperationContract.model_validate(
        {
            "action": "LancarEstoque",
            "description": "Lança o estoque de um pedido de venda pelo ID, no depósito padrão.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID do pedido de venda",
                    "location": "path",
                    "name": "idPedidoVenda",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_pedido_venda",
                }
            ],
            "path": "/pedidos/vendas/{idPedidoVenda}/lancar-estoque",
            "request_schema_refs": [],
            "resource": "PedidosVenda",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "lancar_estoque",
            "summary": "Lança o estoque de um pedido de venda no depósito padrão",
        }
    ),
    "lancar_estoque_id_deposito": OperationContract.model_validate(
        {
            "action": "LancarEstoqueDeposito",
            "description": "Lança o estoque de um pedido de venda pelo ID, especificando o ID do depósito.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID do pedido de venda",
                    "location": "path",
                    "name": "idPedidoVenda",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_pedido_venda",
                },
                {
                    "description": "ID do depósito de estoque",
                    "location": "path",
                    "name": "idDeposito",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_deposito",
                },
            ],
            "path": "/pedidos/vendas/{idPedidoVenda}/lancar-estoque/{idDeposito}",
            "request_schema_refs": [],
            "resource": "PedidosVenda",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "lancar_estoque",
            "summary": "Lança o estoque de um pedido de venda especificando o depósito",
        }
    ),
    "alterar_situacao": OperationContract.model_validate(
        {
            "action": "AlterarSituacao",
            "description": "Altera a situação de um pedido de venda pelo ID.",
            "method": "PATCH",
            "parameters": [
                {
                    "description": "ID do pedido de venda",
                    "location": "path",
                    "name": "idPedidoVenda",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_pedido_venda",
                },
                {
                    "description": "ID da situação do pedido de venda",
                    "location": "path",
                    "name": "idSituacao",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_situacao",
                },
            ],
            "path": "/pedidos/vendas/{idPedidoVenda}/situacoes/{idSituacao}",
            "request_schema_refs": [],
            "resource": "PedidosVenda",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "alterar_situacao",
            "summary": "Altera a situação de um pedido de venda",
        }
    ),
}
