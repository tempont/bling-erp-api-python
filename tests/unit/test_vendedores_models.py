"""Model tests for Vendedores models."""

import json
from pathlib import Path
from typing import Any

from bling_erp_api.models.generated.vendedores import (
    VendedoresIdVendedorGetResponse200,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def _load_fixture(name: str) -> dict[str, Any]:
    return json.loads((FIXTURES_DIR / name).read_text())


class TestVendedoresModels:
    """Tests for Vendedores models deserialization."""

    def test_deserialize_get(self) -> None:
        """Should deserialize a VendedoresIdVendedorGetResponse200 from fixture."""
        data = _load_fixture("vendedores_get.json")
        response = VendedoresIdVendedorGetResponse200(**data)
        item = response.data
        assert item is not None
        assert item.id == 12345678
        assert item.desconto_limite == 10.0
        assert item.contato is not None
        assert item.contato.nome == "Vendedor Teste"

    def test_deserialize_comissoes(self) -> None:
        """Should deserialize nested comissoes list from fixture."""
        data = _load_fixture("vendedores_get.json")
        response = VendedoresIdVendedorGetResponse200(**data)
        item = response.data
        assert item is not None
        comissoes = item.comissoes
        assert len(comissoes) == 1
        assert comissoes[0].desconto_maximo == 15.0

    def test_deserialize_extra_allowed(self) -> None:
        """Extra fields (campoNovoBling) should be preserved via BlingModel extra='allow'."""
        data = _load_fixture("vendedores_get.json")
        response = VendedoresIdVendedorGetResponse200(**data)
        item = response.data
        assert item is not None
        assert getattr(item, "campoNovoBling", None) == "mantido"  # pyright: ignore[reportAttributeAccessIssue]
