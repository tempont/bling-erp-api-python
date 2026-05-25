"""Model mapping tests para variações de produtos."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.product_variations import (
    ProductVariationAttributeOption,
    ProductVariationCombinationRequest,
)
from bling_erp_api.models.generated.products import Product

FIXTURE_PATH = Path("tests/fixtures/responses/product_variation_obter.json")


def test_variation_fixture_wraps_produto_principal() -> None:
    """``ProdutosVariacoes`` deve mapear para o modelo principal com variações."""
    payload = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    product = Product.model_validate(payload["data"])
    assert product.id == 998877665
    assert len(product.variations) == 1
    assert product.variations[0].id == 112233445


def test_variation_combo_request_aliases() -> None:
    """Combinações usam aliases Bling nos dumps JSON."""
    request = ProductVariationCombinationRequest.model_validate(
        {
            "produtoPai": {"id": 9},
            "atributos": [{"nome": "Cor", "opcoes": ["Azul"]}],
        }
    )
    dumped = request.model_dump(mode="json", by_alias=True, exclude_none=True)
    assert dumped == {
        "produtoPai": {"id": 9},
        "atributos": [{"nome": "Cor", "opcoes": ["Azul"]}],
    }


def test_attribute_option_handles_empty_opcoes() -> None:
    """Atributos sem opções devem aparecer como lista vazia."""
    attr = ProductVariationAttributeOption.model_validate({"nome": "Tam"})
    assert attr.opcoes == []
