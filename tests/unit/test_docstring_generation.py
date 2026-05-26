"""Tests for docstring generation from OpenAPI contracts."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import cast

# Use importlib to load generate_openapi_contracts since scripts/ has no
# __init__.py and uv run pytest does not make it importable as a package.
_scripts_path = Path(__file__).resolve().parents[2] / "scripts" / "generate_openapi_contracts.py"
_spec = importlib.util.spec_from_file_location("generate_openapi_contracts", _scripts_path)
assert _spec is not None, f"Could not load spec from {_scripts_path}"
assert _spec.loader is not None, f"Loader is None for spec from {_scripts_path}"
_gen_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_gen_module)
_generate_docstring = _gen_module._generate_docstring  # noqa: SLF001


def test_generate_docstring_for_list_operation() -> None:
    """Docstring for a list operation includes summary, endpoint, params, and response schemas."""
    contract = cast(
        "dict[str, object]",
        {
            "sdk_method": "listar",
            "method": "GET",
            "path": "/produtos",
            "resource": "Produtos",
            "action": "ObterMultiplos",
            "summary": "Obtém produtos",
            "description": "Obtém produtos paginados.",
            "parameters": [
                {
                    "name": "pagina",
                    "location": "query",
                    "sdk_name": "pagina",
                    "required": False,
                    "description": "N° da página da listagem",
                    "schema_type": "integer",
                    "schema_format": None,
                },
                {
                    "name": "limite",
                    "location": "query",
                    "sdk_name": "limite",
                    "required": False,
                    "description": "Limite",
                    "schema_type": "integer",
                    "schema_format": None,
                },
                {
                    "name": "nome",
                    "location": "query",
                    "sdk_name": "nome",
                    "required": False,
                    "description": None,
                    "schema_type": "string",
                    "schema_format": None,
                },
            ],
            "request_schema_refs": [],
            "response_schema_refs": {"200": ["ProdutosDadosDTO"]},
        },
    )

    docstring = _generate_docstring(contract)

    assert docstring.startswith("Obtém produtos.\n")
    assert "Endpoint: GET /produtos" in docstring
    assert "Args:" in docstring
    assert "pagina: N° da página da listagem" in docstring
    assert "limite: Limite" in docstring
    assert "nome: Filtrar por nome." in docstring  # Fallback description
    assert "(Bling: ``pagina``, integer, opcional)" in docstring
    assert "Response schemas: 200: ProdutosDadosDTO" in docstring


def test_generate_docstring_for_get_operation() -> None:
    """Docstring for a GET-by-ID operation includes path parameter."""
    contract = cast(
        "dict[str, object]",
        {
            "sdk_method": "obter",
            "method": "GET",
            "path": "/produtos/{idProduto}",
            "resource": "Produtos",
            "action": "Obter",
            "summary": "Obtém um produto",
            "description": "Obtém um produto pelo ID.",
            "parameters": [
                {
                    "name": "idProduto",
                    "location": "path",
                    "sdk_name": "id_produto",
                    "required": True,
                    "description": "ID do produto",
                    "schema_type": "integer",
                    "schema_format": None,
                },
            ],
            "request_schema_refs": [],
            "response_schema_refs": {"200": ["ProdutosDadosDTO"]},
        },
    )

    docstring = _generate_docstring(contract)

    assert docstring.startswith("Obtém um produto.\n")
    assert "Endpoint: GET /produtos/{idProduto}" in docstring
    assert "id_produto: ID do produto" in docstring
    assert "(Bling: ``idProduto``, integer, obrigatório)" in docstring


def test_generate_docstring_for_create_operation() -> None:
    """Docstring for a POST operation includes request schema."""
    contract = cast(
        "dict[str, object]",
        {
            "sdk_method": "criar",
            "method": "POST",
            "path": "/produtos",
            "resource": "Produtos",
            "action": "Criar",
            "summary": "Cria um produto",
            "description": "Cria um produto.",
            "parameters": [],
            "request_schema_refs": ["ProdutosDadosDTO"],
            "response_schema_refs": {"201": ["ProdutosDadosDTO"]},
        },
    )

    docstring = _generate_docstring(contract)

    assert docstring.startswith("Cria um produto.\n")
    assert "Request body schema: ProdutosDadosDTO" in docstring
    assert "Args:" not in docstring  # No parameters


def test_generate_docstring_no_response_schemas() -> None:
    """Docstring without response schemas omits Returns section."""
    contract = cast(
        "dict[str, object]",
        {
            "sdk_method": "remover",
            "method": "DELETE",
            "path": "/produtos/{idProduto}",
            "resource": "Produtos",
            "action": "Remover",
            "summary": "Remove um produto",
            "description": None,
            "parameters": [
                {
                    "name": "idProduto",
                    "location": "path",
                    "sdk_name": "id_produto",
                    "required": True,
                    "description": "ID do produto",
                    "schema_type": "integer",
                    "schema_format": None,
                },
            ],
            "request_schema_refs": [],
            "response_schema_refs": {},
        },
    )

    docstring = _generate_docstring(contract)

    assert "Returns:" not in docstring
    assert "id_produto: ID do produto" in docstring
