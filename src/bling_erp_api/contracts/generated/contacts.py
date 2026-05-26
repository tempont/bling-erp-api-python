"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

CONTACT_OPERATIONS: dict[str, OperationContract] = {
    "remover_varios": OperationContract.model_validate(
        {
            "action": "RemoverMultiplos",
            "description": "Remove múltiplos contatos pelos IDs.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "IDs dos contatos",
                    "location": "query",
                    "name": "idsContatos[]",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_contatos",
                }
            ],
            "path": "/contatos",
            "request_schema_refs": [],
            "resource": "Contatos",
            "response_schema_refs": {"200": ["ContatosAlertasResponse"], "400": ["ErrorResponse"]},
            "sdk_method": "remover_varios",
            "summary": "Remove múltiplos contatos",
        }
    ),
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém contatos paginados.",
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
                    "description": "Nome, CPF/CNPJ, fantasia, e-mail ou código do contato",
                    "location": "query",
                    "name": "pesquisa",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "pesquisa",
                },
                {
                    "description": "Criterio de listagem <br> `1` Todos <br> `2` Excluídos <br> `3` "
                    "Últimos incluídos <br> `4` Sem movimento",
                    "location": "query",
                    "name": "criterio",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "criterio",
                },
                {
                    "description": "Data de inclusão inicial",
                    "location": "query",
                    "name": "dataInclusaoInicial",
                    "required": False,
                    "schema_format": "datetime",
                    "schema_type": "string",
                    "sdk_name": "data_inclusao_inicial",
                },
                {
                    "description": "Data de inclusão final",
                    "location": "query",
                    "name": "dataInclusaoFinal",
                    "required": False,
                    "schema_format": "datetime",
                    "schema_type": "string",
                    "sdk_name": "data_inclusao_final",
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
                {
                    "description": "ID do tipo do contato",
                    "location": "query",
                    "name": "idTipoContato",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_tipo_contato",
                },
                {
                    "description": "ID do vendedor relacionado ao contato",
                    "location": "query",
                    "name": "idVendedor",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_vendedor",
                },
                {
                    "description": "UF do contato",
                    "location": "query",
                    "name": "uf",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "uf",
                },
                {
                    "description": "Telefone do contato",
                    "location": "query",
                    "name": "telefone",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "telefone",
                },
                {
                    "description": "IDs dos contatos",
                    "location": "query",
                    "name": "idsContatos[]",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "array",
                    "sdk_name": "ids_contatos",
                },
                {
                    "description": " CPF/CNPJ, desconsiderando a pontuação",
                    "location": "query",
                    "name": "numeroDocumento",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "numero_documento",
                },
                {
                    "description": "Tipo de pessoa <br> `1` Física <br> `2` Jurídica <br> `3` "
                    "Estrangeiro",
                    "location": "query",
                    "name": "tipoPessoa",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "tipo_pessoa",
                },
            ],
            "path": "/contatos",
            "request_schema_refs": [],
            "resource": "Contatos",
            "response_schema_refs": {"200": ["ContatosDadosBaseDTO"]},
            "sdk_method": "listar",
            "summary": "Obtém contatos",
        }
    ),
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria um contato.",
            "method": "POST",
            "parameters": [],
            "path": "/contatos",
            "request_schema_refs": ["ContatosDadosBaseDTO", "ContatosDadosDTO"],
            "resource": "Contatos",
            "response_schema_refs": {"201": ["BasePostResponse"], "400": ["ErrorResponse"]},
            "sdk_method": "criar",
            "summary": "Cria um contato",
        }
    ),
    "obter_consumidor_final": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém os dados do contato Consumidor Final. O consumidor final é um contato "
            "padrão do sistema que é criado automaticamente e não pode ser alterado.",
            "method": "GET",
            "parameters": [],
            "path": "/contatos/consumidor-final",
            "request_schema_refs": [],
            "resource": "Contatos",
            "response_schema_refs": {"200": ["ContatosDadosBaseDTO", "ContatosDadosDTO"]},
            "sdk_method": "obter_consumidor_final",
            "summary": "Obtém os dados do contato Consumidor Final",
        }
    ),
    "alterar_situacao_varios": OperationContract.model_validate(
        {
            "action": "AlterarSituacaoMultiplos",
            "description": "Altera a situação de múltiplos contatos pelos IDs.",
            "method": "POST",
            "parameters": [],
            "path": "/contatos/situacoes",
            "request_schema_refs": [],
            "resource": "Contatos",
            "response_schema_refs": {"200": ["ContatosAlertasResponse"], "400": ["ErrorResponse"]},
            "sdk_method": "alterar_situacao_varios",
            "summary": "Altera a situação de múltiplos contatos",
        }
    ),
    "listar_tipos": OperationContract.model_validate(
        {
            "action": "ObterTipoContatoMultiplos",
            "description": "Obtém tipos de contato pelo ID.",
            "method": "GET",
            "parameters": [],
            "path": "/contatos/tipos",
            "request_schema_refs": [],
            "resource": "ContatosTipos",
            "response_schema_refs": {"200": ["ContatosTipoContatoDTO"]},
            "sdk_method": "listar_tipos",
            "summary": "Obtém tipos de contato",
        }
    ),
    "remover": OperationContract.model_validate(
        {
            "action": "Remover",
            "description": "Remove um contato pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID do contato",
                    "location": "path",
                    "name": "idContato",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_contato",
                }
            ],
            "path": "/contatos/{idContato}",
            "request_schema_refs": [],
            "resource": "Contatos",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "remover",
            "summary": "Remove um contato",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém um contato pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do contato",
                    "location": "path",
                    "name": "idContato",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_contato",
                }
            ],
            "path": "/contatos/{idContato}",
            "request_schema_refs": [],
            "resource": "Contatos",
            "response_schema_refs": {
                "200": ["ContatosDadosBaseDTO", "ContatosDadosDTO"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter",
            "summary": "Obtém um contato",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera um contato pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID do contato",
                    "location": "path",
                    "name": "idContato",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_contato",
                }
            ],
            "path": "/contatos/{idContato}",
            "request_schema_refs": ["ContatosDadosBaseDTO", "ContatosDadosDTO"],
            "resource": "Contatos",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "alterar",
            "summary": "Altera um contato",
        }
    ),
    "alterar_situacao": OperationContract.model_validate(
        {
            "action": "AlterarSituacao",
            "description": "Altera a situação de um contato pelo ID.",
            "method": "PATCH",
            "parameters": [
                {
                    "description": "ID do contato",
                    "location": "path",
                    "name": "idContato",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_contato",
                }
            ],
            "path": "/contatos/{idContato}/situacoes",
            "request_schema_refs": [],
            "resource": "Contatos",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "alterar_situacao",
            "summary": "Altera a situação de um contato",
        }
    ),
    "obter_tipo_contato": OperationContract.model_validate(
        {
            "action": "ObterTipoContato",
            "description": "Obtém os tipos de contato de um contato pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do contato",
                    "location": "path",
                    "name": "idContato",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_contato",
                }
            ],
            "path": "/contatos/{idContato}/tipos",
            "request_schema_refs": [],
            "resource": "Contatos",
            "response_schema_refs": {"200": ["ContatosTipoContatoDTO"], "404": ["ErrorResponse"]},
            "sdk_method": "obter_tipo_contato",
            "summary": "Obtém os tipos de contato de um contato",
        }
    ),
}
