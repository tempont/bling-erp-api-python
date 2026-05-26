"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

INVOICE_OPERATIONS: dict[str, OperationContract] = {
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
                    "description": "ID da nota fiscal",
                    "location": "path",
                    "name": "idNotaFiscal",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_nota_fiscal",
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
            "path": "/nfe/{idNotaFiscal}/lancar-estoque/{idDeposito}",
            "request_schema_refs": [],
            "resource": "NotasFiscais",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "lancar_estoque",
            "summary": "Lança o estoque de uma nota fiscal especificando o depósito",
        }
    ),
    "remover_varios": OperationContract.model_validate(
        {
            "action": "RemoverMultiplos",
            "description": "Remove múltiplas notas fiscais por IDs.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "IDs das notas fiscais",
                    "location": "query",
                    "name": "idsNotas[]",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_notas",
                }
            ],
            "path": "/nfe",
            "request_schema_refs": [],
            "resource": "NotasFiscais",
            "response_schema_refs": {"200": ["NotasFiscaisExclusaoDTO"], "400": ["ErrorResponse"]},
            "sdk_method": "remover_varios",
            "summary": "Remove múltiplas notas fiscais",
        }
    ),
    "listar_nfe": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém notas fiscais paginadas.",
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
                    "description": "Número do pedido na loja",
                    "location": "query",
                    "name": "numeroLoja",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "numero_loja",
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
                    "description": "Número da nota fiscal",
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
                    "Consulta situação<br>`11` Bloqueada<br><br>**Observação:** Caso "
                    "este parâmetro não seja informado, as notas canceladas não serão "
                    "incluídas na consulta.<br><br>",
                    "location": "query",
                    "name": "situacao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "situacao",
                },
                {
                    "description": "`0` Entrada <br> `1` Saída",
                    "location": "query",
                    "name": "tipo",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "tipo",
                },
                {
                    "description": "Data e hora incial de emissão",
                    "location": "query",
                    "name": "dataEmissaoInicial",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_emissao_inicial",
                },
                {
                    "description": "Data e hora final de emissão",
                    "location": "query",
                    "name": "dataEmissaoFinal",
                    "required": False,
                    "schema_format": "date",
                    "schema_type": "string",
                    "sdk_name": "data_emissao_final",
                },
            ],
            "path": "/nfe",
            "request_schema_refs": [],
            "resource": "NotasFiscais",
            "response_schema_refs": {"200": ["NotasFiscaisDadosBaseDTO"]},
            "sdk_method": "listar",
            "summary": "Obtém notas fiscais",
        }
    ),
    "criar_nfe": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria uma nota fiscal.",
            "method": "POST",
            "parameters": [],
            "path": "/nfe",
            "request_schema_refs": ["NotasFiscaisDadosBaseDTO", "NotasFiscaisDadosPostDTO"],
            "resource": "NotasFiscais",
            "response_schema_refs": {
                "201": ["BasePostResponse", "NotaFiscalResponse_POST"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "criar",
            "summary": "Cria uma nota fiscal",
        }
    ),
    "obter_documento_nota_fiscal": OperationContract.model_validate(
        {
            "action": "ObterDocumentoNotaFiscal",
            "description": "Obtém o PDF ou XML de uma nota fiscal pela chave de acesso. O formato desejado "
            "deve ser informado via query param.",
            "method": "GET",
            "parameters": [
                {
                    "description": "Chave de acesso da nota fiscal (44 dígitos)",
                    "location": "path",
                    "name": "chaveAcesso",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "chave_acesso",
                },
                {
                    "description": "Formato do documento. `pdf` para o DANFE em PDF, `xml` para o XML "
                    "da NF-e.",
                    "location": "query",
                    "name": "formato",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "formato",
                },
            ],
            "path": "/nfe/documento/{chaveAcesso}",
            "request_schema_refs": [],
            "resource": "NotasFiscais",
            "response_schema_refs": {
                "200": ["NotasFiscaisDocumentoDTO"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter_documento_nota_fiscal",
            "summary": "Obtém o documento de uma nota fiscal",
        }
    ),
    "obter_id_nota_fiscal": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém uma nota fiscal pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID da nota fiscal",
                    "location": "path",
                    "name": "idNotaFiscal",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_nota_fiscal",
                }
            ],
            "path": "/nfe/{idNotaFiscal}",
            "request_schema_refs": [],
            "resource": "NotasFiscais",
            "response_schema_refs": {
                "200": ["NotasFiscaisDadosBaseDTO", "NotasFiscaisDadosGetDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter",
            "summary": "Obtém uma nota fiscal",
        }
    ),
    "alterar_id_nota_fiscal": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera uma nota fiscal pelo ID. Notas com vínculos possuem restrições de "
            "atualização. Notas autorizadas não podem ter dados fiscais alterados: valores, "
            "impostos, informações do destinatário e qualquer outro dado transmitido no XML da "
            "nota.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID da nota fiscal",
                    "location": "path",
                    "name": "idNotaFiscal",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_nota_fiscal",
                }
            ],
            "path": "/nfe/{idNotaFiscal}",
            "request_schema_refs": ["NotasFiscaisDadosBaseDTO", "NotasFiscaisDadosPostDTO"],
            "resource": "NotasFiscais",
            "response_schema_refs": {
                "200": ["BasePostResponse", "ErrorField", "NotaFiscalResponse_POST"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "alterar",
            "summary": "Altera uma nota fiscal",
        }
    ),
    "autorizar_enviar": OperationContract.model_validate(
        {
            "action": "Autorizar",
            "description": "Envia uma nota fiscal pelo ID para emissão na Sefaz.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID da nota fiscal",
                    "location": "path",
                    "name": "idNotaFiscal",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_nota_fiscal",
                },
                {
                    "description": "Define se deve enviar email após a emissão da nota fiscal",
                    "location": "query",
                    "name": "enviarEmail",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "boolean",
                    "sdk_name": "enviar_email",
                },
            ],
            "path": "/nfe/{idNotaFiscal}/enviar",
            "request_schema_refs": [],
            "resource": "NotasFiscais",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "autorizar",
            "summary": "Envia uma nota fiscal",
        }
    ),
    "estornar_contas_estornar_contas": OperationContract.model_validate(
        {
            "action": "EstornarContas",
            "description": "Estorna as contas de uma nota fiscal pelo ID.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID da nota fiscal",
                    "location": "path",
                    "name": "idNotaFiscal",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_nota_fiscal",
                }
            ],
            "path": "/nfe/{idNotaFiscal}/estornar-contas",
            "request_schema_refs": [],
            "resource": "NotasFiscais",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "estornar_contas",
            "summary": "Estorna as contas de uma nota fiscal",
        }
    ),
    "estornar_estoque_estornar_estoque": OperationContract.model_validate(
        {
            "action": "EstornarEstoque",
            "description": "Estorna o estoque de uma nota fiscal pelo ID.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID da nota fiscal",
                    "location": "path",
                    "name": "idNotaFiscal",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_nota_fiscal",
                }
            ],
            "path": "/nfe/{idNotaFiscal}/estornar-estoque",
            "request_schema_refs": [],
            "resource": "NotasFiscais",
            "response_schema_refs": {"404": ["ErrorResponse"]},
            "sdk_method": "estornar_estoque",
            "summary": "Estorna o estoque de uma nota fiscal",
        }
    ),
    "lancar_contas_lancar_contas": OperationContract.model_validate(
        {
            "action": "LancarContas",
            "description": "Lança as contas de uma nota fiscal pelo ID.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID da nota fiscal",
                    "location": "path",
                    "name": "idNotaFiscal",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_nota_fiscal",
                }
            ],
            "path": "/nfe/{idNotaFiscal}/lancar-contas",
            "request_schema_refs": [],
            "resource": "NotasFiscais",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "lancar_contas",
            "summary": "Lança as contas de uma nota fiscal",
        }
    ),
    "lancar_estoque_lancar_estoque": OperationContract.model_validate(
        {
            "action": "LancarEstoque",
            "description": "Lança o estoque de uma nota fiscal pelo ID, no depósito padrão.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID da nota fiscal",
                    "location": "path",
                    "name": "idNotaFiscal",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_nota_fiscal",
                }
            ],
            "path": "/nfe/{idNotaFiscal}/lancar-estoque",
            "request_schema_refs": [],
            "resource": "NotasFiscais",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "lancar_estoque",
            "summary": "Lança o estoque de uma nota fiscal no depósito padrão",
        }
    ),
}
