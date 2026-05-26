"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

AD_OPERATIONS: dict[str, OperationContract] = {
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém anúncios paginados.",
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
                    "description": "Situação do anúncio <br> `1` Publicado <br> `2` Rascunho <br> `3` "
                    "Com problema <br> `4` Pausado",
                    "location": "query",
                    "name": "situacao",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "situacao",
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
                    "description": "Tipo de integração",
                    "location": "query",
                    "name": "tipoIntegracao",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "tipo_integracao",
                },
                {
                    "description": "ID da loja",
                    "location": "query",
                    "name": "idLoja",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_loja",
                },
            ],
            "path": "/anuncios",
            "request_schema_refs": [],
            "resource": "Anuncios",
            "response_schema_refs": {
                "200": ["AnunciosGetAllResponseDTO"],
                "400": ["ErrorResponse"],
            },
            "sdk_method": "listar",
            "summary": "Obtém anúncios",
        }
    ),
    "criar": OperationContract.model_validate(
        {
            "action": "Criar",
            "description": "Cria um anúncio.",
            "method": "POST",
            "parameters": [],
            "path": "/anuncios",
            "request_schema_refs": ["AnunciosSaveRequest"],
            "resource": "Anuncios",
            "response_schema_refs": {"201": ["AnunciosSaveResponseDTO"], "400": ["ErrorResponse"]},
            "sdk_method": "criar",
            "summary": "Cria um anúncio",
        }
    ),
    "remover": OperationContract.model_validate(
        {
            "action": "Remover",
            "description": "Remove um anúncio pelo ID.",
            "method": "DELETE",
            "parameters": [
                {
                    "description": "ID do anúncio",
                    "location": "path",
                    "name": "idAnuncio",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_anuncio",
                },
                {
                    "description": "Tipo de integração",
                    "location": "query",
                    "name": "tipoIntegracao",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "tipo_integracao",
                },
                {
                    "description": "ID da loja",
                    "location": "query",
                    "name": "idLoja",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_loja",
                },
            ],
            "path": "/anuncios/{idAnuncio}",
            "request_schema_refs": [],
            "resource": "Anuncios",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "remover",
            "summary": "Remove um anúncio",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém os detalhes de um anúncio específico pelo seu ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID do anúncio",
                    "location": "path",
                    "name": "idAnuncio",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_anuncio",
                },
                {
                    "description": "Tipo de integração",
                    "location": "query",
                    "name": "tipoIntegracao",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "tipo_integracao",
                },
                {
                    "description": "ID da loja",
                    "location": "query",
                    "name": "idLoja",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_loja",
                },
            ],
            "path": "/anuncios/{idAnuncio}",
            "request_schema_refs": [],
            "resource": "Anuncios",
            "response_schema_refs": {
                "200": ["AnunciosGetByIdResponseDTO"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter",
            "summary": "Obtém um anúncio",
        }
    ),
    "alterar": OperationContract.model_validate(
        {
            "action": "Alterar",
            "description": "Altera um anúncio pelo ID.",
            "method": "PUT",
            "parameters": [
                {
                    "description": "ID do anúncio",
                    "location": "path",
                    "name": "idAnuncio",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_anuncio",
                }
            ],
            "path": "/anuncios/{idAnuncio}",
            "request_schema_refs": ["AnunciosSaveRequest"],
            "resource": "Anuncios",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "alterar",
            "summary": "Altera um anúncio",
        }
    ),
    "pausar": OperationContract.model_validate(
        {
            "action": "Pausar",
            "description": "Altera o status do anúncio para pausado.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID do anúncio",
                    "location": "path",
                    "name": "idAnuncio",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_anuncio",
                },
                {
                    "description": "Tipo de integração",
                    "location": "query",
                    "name": "tipoIntegracao",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "tipo_integracao",
                },
                {
                    "description": "ID da loja",
                    "location": "query",
                    "name": "idLoja",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_loja",
                },
            ],
            "path": "/anuncios/{idAnuncio}/pausar",
            "request_schema_refs": [],
            "resource": "Anuncios",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "pausar",
            "summary": "Pausa um anúncio",
        }
    ),
    "publicar": OperationContract.model_validate(
        {
            "action": "Publicar",
            "description": "Altera o status do anúncio para publicado.",
            "method": "POST",
            "parameters": [
                {
                    "description": "ID do anúncio",
                    "location": "path",
                    "name": "idAnuncio",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_anuncio",
                },
                {
                    "description": "Tipo de integração",
                    "location": "query",
                    "name": "tipoIntegracao",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "tipo_integracao",
                },
                {
                    "description": "ID da loja",
                    "location": "query",
                    "name": "idLoja",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_loja",
                },
            ],
            "path": "/anuncios/{idAnuncio}/publicar",
            "request_schema_refs": [],
            "resource": "Anuncios",
            "response_schema_refs": {"400": ["ErrorResponse"], "404": ["ErrorResponse"]},
            "sdk_method": "publicar",
            "summary": "Publica um anúncio",
        }
    ),
}
