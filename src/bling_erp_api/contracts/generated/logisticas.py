"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

LOGISTICAS_OPERATIONS: dict[str, OperationContract] = {
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém logísticas paginados.",
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
                    "description": "Parâmetro para filtrar os registros através do tipo da logística.",
                    "location": "query",
                    "name": "tipoIntegracao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "tipo_integracao",
                },
                {
                    "description": "Parâmetro para filtrar os registros através de uma lista de tipos "
                    "de logística.",
                    "location": "query",
                    "name": "tiposIntegracoes[]",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "tipos_integracoes",
                },
                {
                    "description": "Parâmetro para filtrar os registros através da situação<br> `H` "
                    "Habilitado<br> `D` Desabilitado",
                    "location": "query",
                    "name": "situacao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "situacao",
                },
                {
                    "description": "Parâmetro para filtrar apenas as logísticas que possuem serviço "
                    "de reversão. É sobrescrito pelo parâmetro tipoIntegracao, caso "
                    "enviado junto.",
                    "location": "query",
                    "name": "logisticasReversas",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "boolean",
                    "sdk_name": "logisticas_reversas",
                },
            ],
            "path": "/logisticas",
            "request_schema_refs": [],
            "resource": "Logisticas",
            "response_schema_refs": {"200": ["LogisticasDadosBaseDTO"], "404": ["ErrorResponse"]},
            "sdk_method": "listar",
            "summary": "Obtém logísticas",
        }
    ),
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria uma logística.",
            "method": "POST",
            "parameters": [],
            "path": "/logisticas",
            "request_schema_refs": ["LogisticasDadosPostDTO"],
            "resource": "Logisticas",
            "response_schema_refs": {"201": ["LogisticasLogisticaDTO"], "400": ["ErrorResponse"]},
            "sdk_method": "criar",
            "summary": "Cria logística",
        }
    ),
    "obter_etiquetas": OperationContract.model_validate(
        {
            "action": "ObterEtiquetaMultiplos",
            "description": "Obtém as etiquetas dos pedidos de venda a partir dos ID's dos pedidos. No "
            "momento, o filtro está limitado para apenas um ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "Parâmetro para definir o formato do arquivo de impressão.<br> "
                    "`PDF` - Formato PDF<br> `ZPL` - Formato ZPL",
                    "location": "query",
                    "name": "formato",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "formato",
                },
                {
                    "description": "IDs dos pedidos de venda para impressão",
                    "location": "query",
                    "name": "idsVendas[]",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_vendas",
                },
            ],
            "path": "/logisticas/etiquetas",
            "request_schema_refs": [],
            "resource": "Logisticas",
            "response_schema_refs": {
                "200": ["LogisticasEtiquetasDadosResponseDTO"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter_etiquetas",
            "summary": "Obtém etiquetas das vendas",
        }
    ),
    "criar_objeto": OperationContract.model_validate(
        {
            "action": "CriarLogisticaObjeto",
            "description": "Cria um objeto de logística personalizada.",
            "method": "POST",
            "parameters": [],
            "path": "/logisticas/objetos",
            "request_schema_refs": ["LogisticasObjetosDadosCreateRequestDTO"],
            "resource": "Logisticas",
            "response_schema_refs": {
                "201": ["LogisticasObjetosObjetoDTO"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "criar_objeto",
            "summary": "Cria um objeto de logística",
        }
    ),
    "remover_objeto": OperationContract.model_validate(
        {
            "action": "RemoverObjetoLogistico",
            "description": "Remove um objeto de logística personalizada que não esteja em uma PLP.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID do objeto logístico",
                    "location": "path",
                    "name": "idObjeto",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_objeto",
                }
            ],
            "path": "/logisticas/objetos/{idObjeto}",
            "request_schema_refs": [],
            "resource": "Logisticas",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "remover_objeto",
            "summary": "Remove um objeto de logística personalizada",
        }
    ),
    "obter_objeto": OperationContract.model_validate(
        {
            "action": "ObterObjetoLogistico",
            "description": "Obtém um objeto de logística pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do objeto logístico",
                    "location": "path",
                    "name": "idObjeto",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_objeto",
                }
            ],
            "path": "/logisticas/objetos/{idObjeto}",
            "request_schema_refs": [],
            "resource": "Logisticas",
            "response_schema_refs": {
                "200": ["LogisticasObjetosDadosDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter_objeto",
            "summary": "Obtém um objeto de logística",
        }
    ),
    "alterar_objeto": OperationContract.model_validate(
        {
            "action": "AlterarLogisticaObjeto",
            "description": "Altera dados de um objeto de logística personalizada pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID do objeto logístico",
                    "location": "path",
                    "name": "idObjeto",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_objeto",
                }
            ],
            "path": "/logisticas/objetos/{idObjeto}",
            "request_schema_refs": ["LogisticasObjetosUpdateRequestDTO"],
            "resource": "Logisticas",
            "response_schema_refs": {
                "200": ["LogisticasObjetosObjetoDTO"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "alterar_objeto",
            "summary": "Altera um objeto de logística pelo ID",
        }
    ),
    "criar_remessa": OperationContract.model_validate(
        {
            "action": "CriarRemessa",
            "description": "Cria uma remessa de postagem de uma logística.",
            "method": "POST",
            "parameters": [],
            "path": "/logisticas/remessas",
            "request_schema_refs": ["LogisticasRemessasDadosPostDTO"],
            "resource": "Logisticas",
            "response_schema_refs": {
                "201": ["LogisticasRemessaRemessaDTO"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "criar_remessa",
            "summary": "Cria uma remessa de postagem de uma logística",
        }
    ),
    "remover_remessa": OperationContract.model_validate(
        {
            "action": "RemoverRemessa",
            "description": "Remove uma remessa de postagem pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID da remessa de postagem",
                    "location": "path",
                    "name": "idRemessa",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_remessa",
                }
            ],
            "path": "/logisticas/remessas/{idRemessa}",
            "request_schema_refs": [],
            "resource": "Logisticas",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "remover_remessa",
            "summary": "Remove uma remessa de postagem",
        }
    ),
    "obter_remessa": OperationContract.model_validate(
        {
            "action": "ObterRemessa",
            "description": "Obtém uma remessa de postagem pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID da remessa de postagem",
                    "location": "path",
                    "name": "idRemessa",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_remessa",
                }
            ],
            "path": "/logisticas/remessas/{idRemessa}",
            "request_schema_refs": [],
            "resource": "Logisticas",
            "response_schema_refs": {
                "200": ["LogisticasRemessasDadosBaseDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter_remessa",
            "summary": "Obtém uma remessa de postagem",
        }
    ),
    "alterar_remessa": OperationContract.model_validate(
        {
            "action": "AlterarRemessa",
            "description": "Altera uma remessa de postagem pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID da remessa de postagem",
                    "location": "path",
                    "name": "idRemessa",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_remessa",
                }
            ],
            "path": "/logisticas/remessas/{idRemessa}",
            "request_schema_refs": ["LogisticasRemessasDadosBaseDTOCommon"],
            "resource": "Logisticas",
            "response_schema_refs": {
                "200": ["LogisticasRemessaRemessaDTO"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "alterar_remessa",
            "summary": "Altera uma remessa de postagem",
        }
    ),
    "listar_servicos": OperationContract.model_validate(
        {
            "action": "ObterServicoLogisticoMultiplos",
            "description": "Obtém serviços de logísticas paginados.",
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
                    "description": "Parâmetro para filtrar os registros através do tipo da logística.",
                    "location": "query",
                    "name": "tipoIntegracao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "tipo_integracao",
                },
            ],
            "path": "/logisticas/servicos",
            "request_schema_refs": [],
            "resource": "Logisticas",
            "response_schema_refs": {
                "200": ["LogisticasServicosDadosDTO"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "listar_servicos",
            "summary": "Obtém serviços de logísticas",
        }
    ),
    "criar_servico": OperationContract.model_validate(
        {
            "action": "CriarLogisticaServico",
            "description": "Cria um serviço de logística personalizada.",
            "method": "POST",
            "parameters": [],
            "path": "/logisticas/servicos",
            "request_schema_refs": ["LogisticasServicosDadosCreateRequestDTO"],
            "resource": "Logisticas",
            "response_schema_refs": {
                "201": ["LogisticasServicosDadosSaveDTO"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "criar_servico",
            "summary": "Cria um serviço de logística",
        }
    ),
    "obter_servico": OperationContract.model_validate(
        {
            "action": "ObterServicoLogistico",
            "description": "Obtém um servico de logística pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do serviço",
                    "location": "path",
                    "name": "idLogisticaServico",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_logistica_servico",
                }
            ],
            "path": "/logisticas/servicos/{idLogisticaServico}",
            "request_schema_refs": [],
            "resource": "Logisticas",
            "response_schema_refs": {
                "200": ["LogisticasServicosDadosDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter_servico",
            "summary": "Obtém um servico de logística",
        }
    ),
    "alterar_servico": OperationContract.model_validate(
        {
            "action": "AlterarLogisticaServico",
            "description": "Altera dados de um serviço de logística personalizada pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID do serviço",
                    "location": "path",
                    "name": "idLogisticaServico",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_logistica_servico",
                }
            ],
            "path": "/logisticas/servicos/{idLogisticaServico}",
            "request_schema_refs": ["LogisticasServicosDadosSaveRequestDTO"],
            "resource": "Logisticas",
            "response_schema_refs": {
                "200": ["LogisticasServicosDadosSaveDTO"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "alterar_servico",
            "summary": "Altera um serviço de logística pelo ID",
        }
    ),
    "alterar_situacao_servico": OperationContract.model_validate(
        {
            "action": "AlterarSituacaoLogisticaServico",
            "description": "Desativa ou ativa um serviço de uma logística personalizada pelo ID.",
            "method": "PATCH",
            "parameters": [
                {
                    "description": "ID do serviço",
                    "location": "path",
                    "name": "idLogisticaServico",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_logistica_servico",
                }
            ],
            "path": "/logisticas/{idLogisticaServico}/situacoes",
            "request_schema_refs": ["LogisticasServicosDadosSituationDTO"],
            "resource": "Logisticas",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "alterar_situacao_servico",
            "summary": "Desativa ou ativa um serviço de uma logística",
        }
    ),
    "remover": OperationContract.model_validate(
        {
            "action": "Remover",
            "description": "Remove uma logística pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID da logística",
                    "location": "path",
                    "name": "idLogistica",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_logistica",
                }
            ],
            "path": "/logisticas/{idLogistica}",
            "request_schema_refs": [],
            "resource": "Logisticas",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "remover",
            "summary": "Remove uma logística",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém uma logística pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID da logística",
                    "location": "path",
                    "name": "idLogistica",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_logistica",
                },
                {
                    "description": "Parâmetro para incluir serviços inativos na resposta.<br> `true` "
                    "Inclui serviços ativos e inativos<br> `false` Inclui apenas "
                    "serviços ativos (padrão)",
                    "location": "query",
                    "name": "listarServicosInativos",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "boolean",
                    "sdk_name": "listar_servicos_inativos",
                },
            ],
            "path": "/logisticas/{idLogistica}",
            "request_schema_refs": [],
            "resource": "Logisticas",
            "response_schema_refs": {"200": ["LogisticasDadosDTO"], "404": ["ErrorResponse"]},
            "sdk_method": "obter",
            "summary": "Obtém uma logística",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera uma logística pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID da logística",
                    "location": "path",
                    "name": "idLogistica",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_logistica",
                }
            ],
            "path": "/logisticas/{idLogistica}",
            "request_schema_refs": ["LogisticasDadosPutDTO"],
            "resource": "Logisticas",
            "response_schema_refs": {"400": ["ErrorResponse"]},
            "sdk_method": "alterar",
            "summary": "Altera uma logística",
        }
    ),
    "listar_remessas_por_logistica": OperationContract.model_validate(
        {
            "action": "ObterLogisticaRemessaMultiplos",
            "description": "Obtém as remessas de postagem de uma logística pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID da logística",
                    "location": "path",
                    "name": "idLogistica",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_logistica",
                }
            ],
            "path": "/logisticas/{idLogistica}/remessas",
            "request_schema_refs": [],
            "resource": "Logisticas",
            "response_schema_refs": {
                "200": ["LogisticasRemessasDadosDTO"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "listar_remessas_por_logistica",
            "summary": "Obtém as remessas de postagem de uma logística",
        }
    ),
}
