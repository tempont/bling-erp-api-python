"""Model tests for Categorias - Receitas e Despesas Pydantic models."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.income_expense_categories import (
    CategoriasReceitasDespesasDadosBaseDTO,
    CategoriasReceitasDespesasDadosDTO,
    CategoriasReceitasDespesasDadosPostDTO,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def test_categorias_receitas_despesas_dados_base_dto_from_fixture() -> None:
    """Deserialize CategoriasReceitasDespesasDadosBaseDTO from fixture (list scenario)."""
    payload = json.loads(
        (FIXTURES_DIR / "income_expense_categories_get.json").read_text(encoding="utf-8")
    )
    model = CategoriasReceitasDespesasDadosBaseDTO.model_validate(payload["data"])
    assert model.id == 300
    assert model.id_categoria_pai == 0
    assert model.descricao == "Vendas de Produtos"
    assert model.tipo == 2


def test_categorias_receitas_despesas_dados_dto_from_fixture() -> None:
    """Deserialize CategoriasReceitasDespesasDadosDTO with situacao field."""
    payload = json.loads(
        (FIXTURES_DIR / "income_expense_categories_get.json").read_text(encoding="utf-8")
    )
    model = CategoriasReceitasDespesasDadosDTO.model_validate(payload["data"])
    assert model.id == 300
    assert model.descricao == "Vendas de Produtos"
    assert model.tipo == 2
    assert model.situacao == 1


def test_categorias_receitas_despesas_dados_post_dto_serialization() -> None:
    """Serialize CategoriasReceitasDespesasDadosPostDTO with camelCase aliases."""
    dados = CategoriasReceitasDespesasDadosPostDTO(
        descricao="Nova Categoria",
        tipo=2,
        idCategoriaPai=5,
        grupoDRE=7,
    )
    result = dados.model_dump(by_alias=True, exclude_none=True)
    assert result["descricao"] == "Nova Categoria"
    assert result["tipo"] == 2
    assert result["idCategoriaPai"] == 5
    assert result["grupoDRE"] == 7
