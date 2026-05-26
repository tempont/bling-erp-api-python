"""Generated from specs/bling-openapi-reference.json. Do not edit manually."""

from __future__ import annotations

from bling_erp_api.contracts import OperationContract

AD_CATEGORY_OPERATIONS: dict[str, OperationContract] = {
    "listar": OperationContract.model_validate(
        {
            "action": "ObterMultiplos",
            "description": "Obtém categorias de anúncios.",
            "method": "GET",
            "parameters": [
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
                {
                    "description": "ID da categoria",
                    "location": "query",
                    "name": "idCategoria",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "integer",
                    "sdk_name": "id_categoria",
                },
                {
                    "description": "Tipo do produto",
                    "location": "query",
                    "name": "tipoProduto",
                    "required": False,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "tipo_produto",
                },
            ],
            "path": "/anuncios/categorias",
            "request_schema_refs": [],
            "resource": "AnunciosCategorias",
            "response_schema_refs": {"200": ["AnunciosCategoriaDTO"], "400": ["ErrorResponse"]},
            "sdk_method": "listar",
            "summary": "Obtém categorias de anúncios",
        }
    ),
    "obter": OperationContract.model_validate(
        {
            "action": "Obter",
            "description": "Obtém uma categoria de anúncio pelo ID.",
            "method": "GET",
            "parameters": [
                {
                    "description": "ID da categoria no marketplace (ex.: Mercado Livre)",
                    "location": "path",
                    "name": "idCategoria",
                    "required": True,
                    "schema_format": None,
                    "schema_type": "string",
                    "sdk_name": "id_categoria",
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
            "path": "/anuncios/categorias/{idCategoria}",
            "request_schema_refs": [],
            "resource": "AnunciosCategorias",
            "response_schema_refs": {
                "200": ["AnunciosGetAttributesFromCategoryResponseDTO"],
                "400": ["ErrorResponse"],
                "404": ["ErrorResponse"],
            },
            "sdk_method": "obter",
            "summary": "Obtém uma categoria de anúncio",
        }
    ),
}
