"""Model tests for Categorias - Produtos Pydantic models."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.product_categories import (
    CategoriasProdutosCategoriPaiDTO,
    CategoriasProdutosDadosDTO,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def test_categorias_produtos_dados_dto_from_fixture() -> None:
    """Deserialize CategoriasProdutosDadosDTO from fixture JSON."""
    payload = json.loads((FIXTURES_DIR / "product_categories_get.json").read_text(encoding="utf-8"))
    model = CategoriasProdutosDadosDTO.model_validate(payload["data"])
    assert model.id == 200
    assert model.descricao == "Camisetas"
    assert model.categoria_pai is not None
    assert model.categoria_pai.id == 10


def test_categorias_produtos_dados_dto_serialization() -> None:
    """Serialize CategoriasProdutosDadosDTO with camelCase aliases."""
    dados = CategoriasProdutosDadosDTO(
        id=1,
        descricao="Nova Categoria",
        categoriaPai=CategoriasProdutosCategoriPaiDTO(id=5),
    )
    result = dados.model_dump(by_alias=True, exclude_none=True)
    assert result["id"] == 1
    assert result["descricao"] == "Nova Categoria"
    assert result["categoriaPai"]["id"] == 5
