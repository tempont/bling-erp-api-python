"""Model tests for Ad Categories Pydantic models."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.ad_categories import (
    AnunciosCategoriaListDTO,
    AnunciosGetAttributesFromCategoryResponseDTO,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def test_anuncios_categoria_list_dto_from_fixture() -> None:
    """Deserialize AnunciosCategoriaListDTO list from fixture JSON."""
    payload = json.loads((FIXTURES_DIR / "ads_categories_list.json").read_text(encoding="utf-8"))
    models = [AnunciosCategoriaListDTO.model_validate(item) for item in payload["data"]]
    assert len(models) == 2
    assert models[0].id == 101
    assert models[0].nome == "Roupas"
    assert models[1].id == 102
    assert models[1].nome == "Eletrônicos"


def test_anuncios_get_attributes_response_dto_from_fixture() -> None:
    """Deserialize AnunciosGetAttributesFromCategoryResponseDTO from fixture JSON."""
    payload = json.loads((FIXTURES_DIR / "ads_categories_get.json").read_text(encoding="utf-8"))
    model = AnunciosGetAttributesFromCategoryResponseDTO.model_validate(payload["data"])
    assert model.id == 1
    assert model.nome == "Atributo 1"
    assert model.obrigatorio is True
    assert model.tipo == "string"
    assert model.unidade_padrao == "unidade"
    assert model.minimo == 1
    assert model.maximo == 10
