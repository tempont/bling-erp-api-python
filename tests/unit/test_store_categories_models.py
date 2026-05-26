"""Model tests for Categorias - Lojas Pydantic models."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.store_categories import (
    CategoriasLojasCategoriaProdutoDTO,
    CategoriasLojasDadosDTO,
    CategoriasLojasLojaDTO,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def test_categorias_lojas_dados_dto_from_fixture() -> None:
    """Deserialize CategoriasLojasDadosDTO from fixture JSON."""
    payload = json.loads((FIXTURES_DIR / "store_categories_get.json").read_text(encoding="utf-8"))
    model = CategoriasLojasDadosDTO.model_validate(payload["data"])
    assert model.id == 100
    assert model.loja is not None
    assert model.loja.id == 1
    assert model.descricao == "Eletrônicos"
    assert model.codigo == "MLB1234"
    assert model.categoria_produto is not None
    assert model.categoria_produto.id == 50


def test_categorias_lojas_dados_dto_serialization() -> None:
    """Serialize CategoriasLojasDadosDTO with camelCase aliases."""
    dados = CategoriasLojasDadosDTO(
        loja=CategoriasLojasLojaDTO(id=1),
        descricao="Teste",
        codigo="ABC",
        categoriaProduto=CategoriasLojasCategoriaProdutoDTO(id=42),
    )
    result = dados.model_dump(by_alias=True, exclude_none=True)
    assert result["loja"]["id"] == 1
    assert result["descricao"] == "Teste"
    assert result["codigo"] == "ABC"
    assert result["categoriaProduto"]["id"] == 42
