"""Model tests for Produtos models."""

import json
from pathlib import Path
from typing import Any

import pytest
from pydantic import ValidationError

from bling_erp_api.models.generated.products import (
    ProdutosIdProdutoGetResponse200,
)
from bling_erp_api.models.generated.schemas import (
    ProdutosImagemInternaDTO,
    ProdutosImagensDTO,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def _load_fixture(name: str) -> dict[str, Any]:
    return json.loads((FIXTURES_DIR / name).read_text())


def _load_product_imagens() -> ProdutosImagensDTO:
    """Load the product fixture and return the parsed ``midia.imagens`` node."""
    data = _load_fixture("product_obter.json")
    response = ProdutosIdProdutoGetResponse200(**data)
    item = response.data
    assert item is not None
    midia = item.midia
    assert midia is not None
    imagens = midia.imagens
    assert imagens is not None
    return imagens


class TestProdutosModels:
    """Tests for Produtos models deserialization.

    Bug 6: real ``GET /produtos/{idProduto}`` responses often carry
    ``midia.imagens.internas[]`` entries with only ``link`` populated, so every
    field of ``ProdutosImagemInternaDTO`` except ``link`` must be optional.
    """

    def test_deserialize_get_with_link_only_internal_image(self) -> None:
        """Internal image with only ``link`` parses with the other fields as None."""
        imagens = _load_product_imagens()
        internas = imagens.internas
        assert internas is not None
        link_only = internas[0]
        assert link_only.link == "https://cdn.exemplo.com.br/bling/imagens/123456789-a.jpg"
        assert link_only.link_miniatura is None
        assert link_only.validade is None
        assert link_only.ordem is None
        assert link_only.anexo is None
        assert link_only.anexo_vinculo is None

    def test_internal_image_requires_link(self) -> None:
        """An internal image entry without ``link`` must fail validation (link stays required)."""
        with pytest.raises(ValidationError, match="Field required"):
            ProdutosImagemInternaDTO.model_validate({})

    def test_deserialize_get_with_complete_internal_image(self) -> None:
        """Internal image with all fields parses fully populated."""
        imagens = _load_product_imagens()
        internas = imagens.internas
        assert internas is not None
        complete = internas[1]
        assert complete.link == "https://cdn.exemplo.com.br/bling/imagens/123456789-b.jpg"
        assert (
            complete.link_miniatura
            == "https://cdn.exemplo.com.br/bling/imagens/miniatura/123456789-b.jpg"
        )
        assert complete.validade == "2027-12-31 00:00:00"
        assert complete.ordem == 2
        assert complete.anexo is not None
        assert complete.anexo.id == 111222333
        assert complete.anexo_vinculo is not None
        assert complete.anexo_vinculo.id == 444555666

    def test_deserialize_get_with_externas_image(self) -> None:
        """Externas entries (``ProdutosImagemDTO``) parse with only ``link``."""
        imagens = _load_product_imagens()
        externas = imagens.externas
        assert externas is not None
        assert externas[0].link == "https://i.ibb.co/exemplo123/caneta-azul.jpg"

    def test_deserialize_get_with_imagens_url_entry(self) -> None:
        """The link-only ``imagensURL`` entry (``ProdutosImagemDTO``) parses."""
        imagens = _load_product_imagens()
        imagens_url = imagens.imagens_url
        assert imagens_url is not None
        assert len(imagens_url) == 1
        assert imagens_url[0].link == "https://cdn.exemplo.com.br/imagens/can-1001.jpg"
