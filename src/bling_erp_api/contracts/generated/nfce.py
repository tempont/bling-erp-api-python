"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

NFCE_OPERATIONS: dict[str, OperationContract] = {
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém notas fiscais de consumidor paginadas.",
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
                    "description": "ID do contato do transportador",
                    "location": "query",
                    "name": "idTransportador",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_transportador",
                },
                {
                    "description": "Chave de acesso",
                    "location": "query",
                    "name": "chaveAcesso",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "chave_acesso",
                },
                {
                    "description": "Número da nota fiscal de consumidor",
                    "location": "query",
                    "name": "numero",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "numero",
                },
                {
                    "description": "Série",
                    "location": "query",
                    "name": "serie",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "serie",
                },
                {
                    "description": "`1` Pendente<br>`2` Cancelada<br>`3` Aguardando recibo<br>`4` "
                    "Rejeitada<br>`5` Autorizada<br>`6` Emitida DANFE<br>`7` "
                    "Registrada<br>`8` Aguardando protocolo<br>`9` Denegada<br>`10` "
                    "Consulta situação<br>`11` Bloqueada",
                    "location": "query",
                    "name": "situacao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "situacao",
                },
                {
                    "description": "Data e hora inicial de emissão",
                    "location": "query",
                    "name": "dataEmissaoInicial",
                    "required": False,
                    "schema_format": "datetime",
                    "schema_type": "string",
                    "sdk_name": "data_emissao_inicial",
                },
                {
                    "description": "Data e hora final de emissão",
                    "location": "query",
                    "name": "dataEmissaoFinal",
                    "required": False,
                    "schema_format": "datetime",
                    "schema_type": "string",
                    "sdk_name": "data_emissao_final",
                },
            ],
            "path": "/nfce",
            "request_schema_refs": [],
            "resource": "NotasFiscais",
            "response_schema_refs": {"200": ["NotasFiscaisDadosBaseDTO"], "404": ["ErrorResponse"]},
            "sdk_method": "listar",
            "summary": "Obtém notas fiscais de consumidor",
        }
    ),
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria uma nota fiscal de consumidor.",
            "method": "POST",
            "parameters": [],
            "path": "/nfce",
            "request_schema_refs": ["NotasFiscaisDadosBaseDTO", "NotasFiscaisDadosPostDTO"],
            "resource": "NotasFiscais",
            "response_schema_refs": {
                "201": ["BasePostResponse", "NotaFiscalResponse_POST"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "criar",
            "summary": "Cria uma nota fiscal de consumidor",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém uma nota fiscal de consumidor pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID da nota fiscal de consumidor",
                    "location": "path",
                    "name": "idNotaFiscalConsumidor",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_nota_fiscal_consumidor",
                }
            ],
            "path": "/nfce/{idNotaFiscalConsumidor}",
            "request_schema_refs": [],
            "resource": "NotasFiscais",
            "response_schema_refs": {
                "200": ["NotasFiscaisDadosBaseDTO", "NotasFiscaisDadosGetDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter",
            "summary": "Obtém uma nota fiscal de consumidor",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera uma nota fiscal de consumidor.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID da nota fiscal de consumidor",
                    "location": "path",
                    "name": "idNotaFiscalConsumidor",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_nota_fiscal_consumidor",
                }
            ],
            "path": "/nfce/{idNotaFiscalConsumidor}",
            "request_schema_refs": ["NotasFiscaisDadosBaseDTO", "NotasFiscaisDadosPostDTO"],
            "resource": "NotasFiscais",
            "response_schema_refs": {
                "200": ["BasePostResponse", "NotaFiscalResponse_POST"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "alterar",
            "summary": "Altera uma nota fiscal de consumidor",
        }
    ),
    "autorizar": OperationContract.model_validate(
        {
            "action": "Autorizar",
            "description": "Envia uma nota de consumidor pelo ID para emissão na Sefaz.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID da nota fiscal de consumidor",
                    "location": "path",
                    "name": "idNotaFiscalConsumidor",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_nota_fiscal_consumidor",
                }
            ],
            "path": "/nfce/{idNotaFiscalConsumidor}/enviar",
            "request_schema_refs": [],
            "resource": "NotasFiscais",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "autorizar",
            "summary": "Envia uma nota de consumidor",
        }
    ),
    "estornar_contas": OperationContract.model_validate(
        {
            "action": "EstornarContas",
            "description": "Estorna as contas de uma nota fiscal pelo ID.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID da nota fiscal de consumidor",
                    "location": "path",
                    "name": "idNotaFiscalConsumidor",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_nota_fiscal_consumidor",
                }
            ],
            "path": "/nfce/{idNotaFiscalConsumidor}/estornar-contas",
            "request_schema_refs": [],
            "resource": "NotasFiscais",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "estornar_contas",
            "summary": "Estorna as contas de uma nota fiscal",
        }
    ),
    "estornar_estoque": OperationContract.model_validate(
        {
            "action": "EstornarEstoque",
            "description": "Estorna o estoque de uma nota fiscal pelo ID.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID da nota fiscal de consumidor",
                    "location": "path",
                    "name": "idNotaFiscalConsumidor",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_nota_fiscal_consumidor",
                }
            ],
            "path": "/nfce/{idNotaFiscalConsumidor}/estornar-estoque",
            "request_schema_refs": [],
            "resource": "NotasFiscais",
            "response_schema_refs": {"404": ["ErrorResponse"]},
            "sdk_method": "estornar_estoque",
            "summary": "Estorna o estoque de uma nota fiscal",
        }
    ),
    "lancar_contas": OperationContract.model_validate(
        {
            "action": "LancarContas",
            "description": "Lança as contas de uma nota fiscal pelo ID.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID da nota fiscal de consumidor",
                    "location": "path",
                    "name": "idNotaFiscalConsumidor",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_nota_fiscal_consumidor",
                }
            ],
            "path": "/nfce/{idNotaFiscalConsumidor}/lancar-contas",
            "request_schema_refs": [],
            "resource": "NotasFiscais",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "lancar_contas",
            "summary": "Lança as contas de uma nota fiscal",
        }
    ),
    "lancar_estoque": OperationContract.model_validate(
        {
            "action": "LancarEstoque",
            "description": "Lança o estoque de uma nota fiscal pelo ID, no depósito padrão.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID da nota fiscal de consumidor",
                    "location": "path",
                    "name": "idNotaFiscalConsumidor",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_nota_fiscal_consumidor",
                }
            ],
            "path": "/nfce/{idNotaFiscalConsumidor}/lancar-estoque",
            "request_schema_refs": [],
            "resource": "NotasFiscais",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "lancar_estoque",
            "summary": "Lança o estoque de uma nota fiscal no depósito padrão",
        }
    ),
    "lancar_estoque_id_deposito": OperationContract.model_validate(
        {
            "action": "LancarEstoqueDeposito",
            "description": "Lança o estoque de uma nota fiscal pelo ID, especificando o ID do depósito.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID da nota fiscal de consumidor",
                    "location": "path",
                    "name": "idNotaFiscalConsumidor",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_nota_fiscal_consumidor",
                },
                {
                    "description": "ID do depósito",
                    "location": "path",
                    "name": "idDeposito",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_deposito",
                },
            ],
            "path": "/nfce/{idNotaFiscalConsumidor}/lancar-estoque/{idDeposito}",
            "request_schema_refs": [],
            "resource": "NotasFiscais",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "lancar_estoque",
            "summary": "Lança o estoque de uma nota fiscal especificando o depósito",
        }
    ),
}
