"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

PAYMENT_METHOD_OPERATIONS: dict[str, OperationContract] = {
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém formas de pagamentos paginadas.",
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
                    "description": "Descrição da forma de pagamento",
                    "location": "query",
                    "name": "descricao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "descricao",
                },
                {
                    "description": "`1` Dinheiro<br>`2` Cheque<br>`3` Cartão de Crédito<br>`4` Cartão "
                    "de Débito<br>`5` Cartão da Loja (Private Label)<br>`10` Vale "
                    "Alimentação<br>`11` Vale Refeição<br>`12` Vale Presente<br>`13` "
                    "Vale Combustível<br>`14` Duplicata Mercantil<br>`15` Boleto "
                    "Bancário<br>`16` Depósito Bancário<br>`17` Pagamento Instantâneo "
                    "(PIX) - Dinâmico<br>`18` Transferência Bancária, Carteira "
                    "Digital<br>`19` Programa de Fidelidade, Cashback, Crédito "
                    "Virtual<br>`20` Pagamento Instantâneo (PIX) – Estático<br>`21` "
                    "Crédito em loja<br>`22` Pagamento Eletrônico não Informado - "
                    "falha de hardware do sistema emissor<br>`90` Sem "
                    "pagamento<br>`99` Outros",
                    "location": "query",
                    "name": "tiposPagamentos[]",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "tipos_pagamentos",
                },
                {
                    "description": "`0` Inativa<br>`1` Ativa",
                    "location": "query",
                    "name": "situacao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "situacao",
                },
            ],
            "path": "/formas-pagamentos",
            "request_schema_refs": [],
            "resource": "FormasPagamentos",
            "response_schema_refs": {"200": ["FormasPagamentosDadosBaseDTO"]},
            "sdk_method": "listar",
            "summary": "Obtém formas de pagamentos",
        }
    ),
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria uma forma de pagamento.",
            "method": "POST",
            "parameters": [],
            "path": "/formas-pagamentos",
            "request_schema_refs": ["FormasPagamentosDadosBaseDTO", "FormasPagamentosDadosDTO"],
            "resource": "FormasPagamentos",
            "response_schema_refs": {"201": ["BasePostResponse"], "400": ["ErrorResponse"]},
            "sdk_method": "criar",
            "summary": "Cria uma forma de pagamento",
        }
    ),
    "remover": OperationContract.model_validate(
        {
            "action": "Remover",
            "description": "Remove uma forma de pagamento pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID da forma de pagamento",
                    "location": "path",
                    "name": "idFormaPagamento",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_forma_pagamento",
                }
            ],
            "path": "/formas-pagamentos/{idFormaPagamento}",
            "request_schema_refs": [],
            "resource": "FormasPagamentos",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "remover",
            "summary": "Remove uma forma de pagamento",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém uma forma de pagamento pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID da forma de pagamento",
                    "location": "path",
                    "name": "idFormaPagamento",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_forma_pagamento",
                }
            ],
            "path": "/formas-pagamentos/{idFormaPagamento}",
            "request_schema_refs": [],
            "resource": "FormasPagamentos",
            "response_schema_refs": {
                "200": ["FormasPagamentosDadosBaseDTO", "FormasPagamentosDadosDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter",
            "summary": "Obtém uma forma de pagamento",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera uma forma de pagamento pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID da forma de pagamento",
                    "location": "path",
                    "name": "idFormaPagamento",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_forma_pagamento",
                }
            ],
            "path": "/formas-pagamentos/{idFormaPagamento}",
            "request_schema_refs": ["FormasPagamentosDadosBaseDTO", "FormasPagamentosDadosDTO"],
            "resource": "FormasPagamentos",
            "response_schema_refs": {
                "200": ["BasePostResponse"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "alterar",
            "summary": "Altera uma forma de pagamento",
        }
    ),
    "alterar_padrao": OperationContract.model_validate(
        {
            "action": "AlterarAtributo",
            "description": "Altera o padrão de uma forma de pagamento pelo ID.",
            "method": "PATCH",
            "parameters": [
                {
                    "description": "ID da forma de pagamento",
                    "location": "path",
                    "name": "idFormaPagamento",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_forma_pagamento",
                }
            ],
            "path": "/formas-pagamentos/{idFormaPagamento}/padrao",
            "request_schema_refs": ["FormasPagamentosDefinirPadraoDTO"],
            "resource": "FormasPagamentos",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "alterar_padrao",
            "summary": "Altera o padrão de uma forma de pagamento",
        }
    ),
    "alterar_situacao": OperationContract.model_validate(
        {
            "action": "AlterarSituacao",
            "description": "Altera a situação de uma forma de pagamento pelo ID.",
            "method": "PATCH",
            "parameters": [
                {
                    "description": "ID da forma de pagamento",
                    "location": "path",
                    "name": "idFormaPagamento",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_forma_pagamento",
                }
            ],
            "path": "/formas-pagamentos/{idFormaPagamento}/situacao",
            "request_schema_refs": ["FormasPagamentosAlterarSituacaoDTO"],
            "resource": "FormasPagamentos",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "alterar_situacao",
            "summary": "Altera a situação de uma forma de pagamento",
        }
    ),
}
