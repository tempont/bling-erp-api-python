"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

CONTAS_RECEBER_OPERATIONS: dict[str, OperationContract] = {
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém contas a receber paginadas.",
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
                    "description": "`1` Em aberto <br>`2` Recebido <br>`3` Parcialmente recebido "
                    "<br>`4` Devolvido <br>`5` Cancelado",
                    "location": "query",
                    "name": "situacoes[]",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "situacoes",
                },
                {
                    "description": "Referente ao campo que será considerado ao filtrar por data "
                    "inicial e final<br>`E` Data de emissão <br> `V` Data de "
                    "vencimento <br> `R` Data de recebimento",
                    "location": "query",
                    "name": "tipoFiltroData",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "tipo_filtro_data",
                },
                {
                    "description": "Data inicial. Por padrão, um ano antes da data atual.",
                    "location": "query",
                    "name": "dataInicial",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_inicial",
                },
                {
                    "description": "Data final. Por padrão, a data atual.",
                    "location": "query",
                    "name": "dataFinal",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_final",
                },
                {
                    "description": "IDs das categorias de receitas e despesas",
                    "location": "query",
                    "name": "idsCategorias[]",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_categorias",
                },
                {
                    "description": "ID da conta financeira",
                    "location": "query",
                    "name": "idPortador",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_portador",
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
                    "description": "ID do vendedor",
                    "location": "query",
                    "name": "idVendedor",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_vendedor",
                },
                {
                    "description": "ID da forma de pagamento",
                    "location": "query",
                    "name": "idFormaPagamento",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_forma_pagamento",
                },
                {
                    "description": "Obtém contas com ou sem boletos emitidos via integração, `0` para "
                    "boletos não emitidos e `1` para boletos emitidos",
                    "location": "query",
                    "name": "boletoGerado",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "boleto_gerado",
                },
            ],
            "path": "/contas/receber",
            "request_schema_refs": [],
            "resource": "ContasReceber",
            "response_schema_refs": {"200": ["ContasReceberDadosListDTO"]},
            "sdk_method": "listar",
            "summary": "Obtém contas a receber",
        }
    ),
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria uma conta a receber.",
            "method": "POST",
            "parameters": [],
            "path": "/contas/receber",
            "request_schema_refs": [
                "ContasDadosBaseDTO",
                "ContasReceberDadosBaseDTO",
                "ContasReceberDadosDTO",
            ],
            "resource": "ContasReceber",
            "response_schema_refs": {"201": ["BasePostResponse"], "400": ["ErrorResponse"]},
            "sdk_method": "criar",
            "summary": "Cria uma conta a receber",
        }
    ),
    "obter_boletos": OperationContract.model_validate(
        {
            "action": "ObterBoletos",
            "description": "Obtém os boletos vinculados a um idOrigem, o qual corresponde ao ID de uma venda "
            "ou nota fiscal.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID da venda ou nota fiscal",
                    "location": "query",
                    "name": "idOrigem",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_origem",
                },
                {
                    "description": "`1` Em aberto <br>`2` Recebido <br>`3` Parcialmente recebido "
                    "<br>`4` Devolvido <br>`5` Parcialmente devolvido <br>`6` "
                    "Cancelado",
                    "location": "query",
                    "name": "situacoes[]",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "situacoes",
                },
            ],
            "path": "/contas/receber/boletos",
            "request_schema_refs": [],
            "resource": "ContasReceber",
            "response_schema_refs": {
                "200": ["ContasReceberBoletosDadosBaseDTO"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "obter_boletos",
            "summary": "Obtém boletos de contas a receber",
        }
    ),
    "cancelar_boletos": OperationContract.model_validate(
        {
            "action": "CancelarBoletos",
            "description": "Cancela um ou todos os boletos em aberto vinculados a uma venda ou nota fiscal.",
            "method": "POST",
            "parameters": [],
            "path": "/contas/receber/boletos/cancelar",
            "request_schema_refs": ["ContasReceberBoletosCancelarDTO"],
            "resource": "ContasReceber",
            "response_schema_refs": {},
            "sdk_method": "cancelar_boletos",
            "summary": "Cancela boletos de contas a receber",
        }
    ),
    "remover": OperationContract.model_validate(
        {
            "action": "Remover",
            "description": "Remove uma conta a receber pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID da conta a receber",
                    "location": "path",
                    "name": "idContaReceber",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_conta_receber",
                }
            ],
            "path": "/contas/receber/{idContaReceber}",
            "request_schema_refs": [],
            "resource": "ContasReceber",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "remover",
            "summary": "Remove uma conta a receber",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém uma conta a receber pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID da conta a receber",
                    "location": "path",
                    "name": "idContaReceber",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_conta_receber",
                }
            ],
            "path": "/contas/receber/{idContaReceber}",
            "request_schema_refs": [],
            "resource": "ContasReceber",
            "response_schema_refs": {
                "200": [
                    "ContasReceberDadosBaseDTO",
                    "ContasReceberDadosDTO",
                    "ContasReceberDadosListDTO",
                ],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter",
            "summary": "Obtém uma conta a receber",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera uma conta a receber pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID da conta a receber",
                    "location": "path",
                    "name": "idContaReceber",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_conta_receber",
                }
            ],
            "path": "/contas/receber/{idContaReceber}",
            "request_schema_refs": ["ContasDadosBaseDTO", "ContasReceberDadosBaseDTO"],
            "resource": "ContasReceber",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "alterar",
            "summary": "Altera uma conta a receber",
        }
    ),
    "baixar": OperationContract.model_validate(
        {
            "action": "BaixarConta",
            "description": "Cria o recebimento de uma conta a receber.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID da conta a receber",
                    "location": "path",
                    "name": "idContaReceber",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_conta_receber",
                }
            ],
            "path": "/contas/receber/{idContaReceber}/baixar",
            "request_schema_refs": ["ContasBaixarContaDTO"],
            "resource": "ContasReceber",
            "response_schema_refs": {"400": ["ErrorResponse"]},
            "sdk_method": "baixar",
            "summary": "Cria o recebimento de uma conta a receber",
        }
    ),
}
