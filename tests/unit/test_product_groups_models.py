"""Model tests for GruposProdutos Pydantic models."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.product_groups import (
    GruposProdutosDadosDTO,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def test_grupos_produtos_dados_dto_from_fixture() -> None:
    """Deserialize GruposProdutosDadosDTO from fixture JSON."""
    payload = json.loads((FIXTURES_DIR / "product_groups_get.json").read_text(encoding="utf-8"))
    model = GruposProdutosDadosDTO.model_validate(payload["data"])
    assert model.nome == "Eletrônicos"
    assert model.grupo_produto_pai is not None
    assert model.grupo_produto_pai.id == 10
