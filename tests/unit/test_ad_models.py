"""Model tests for Ads (Anúncios) Pydantic models."""

from __future__ import annotations

import json
from pathlib import Path

from bling_erp_api.models.generated.ads import (
    AdsIntegracaoRef,
    AdsLojaRef,
    AdsProdutoRef,
    AnunciosGetAllResponseDTO,
    AnunciosGetByIdResponseDTO,
    AnunciosSaveRequest,
    AnunciosSaveResponseDTO,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def test_anuncios_get_all_response_dto_from_fixture() -> None:
    """Deserialize AnunciosGetAllResponseDTO from fixture JSON."""
    payload = json.loads((FIXTURES_DIR / "ads_list.json").read_text(encoding="utf-8"))
    model = AnunciosGetAllResponseDTO.model_validate(payload["data"])
    assert model.id == 1
    assert model.titulo == "Anúncio 1"
    assert model.situacao == 1


def test_anuncios_get_by_id_response_dto_from_fixture() -> None:
    """Deserialize AnunciosGetByIdResponseDTO from fixture JSON."""
    payload = json.loads((FIXTURES_DIR / "ads_get.json").read_text(encoding="utf-8"))
    model = AnunciosGetByIdResponseDTO.model_validate(payload["data"])
    assert model.id == 1
    assert model.produto is not None
    assert model.produto.id == 12345
    assert model.titulo == "Anúncio 1"
    assert model.status == 1
    assert model.atributos is not None
    assert len(model.atributos) == 1
    assert model.atributos[0].nome == "Cor"
    assert model.imagens is not None
    assert len(model.imagens) == 1
    assert model.variacoes is not None
    assert len(model.variacoes) == 1


def test_anuncios_save_request_serialization() -> None:
    """Serialize AnunciosSaveRequest to dict with Bling camelCase aliases."""
    request = AnunciosSaveRequest(
        produto=AdsProdutoRef(id=123),
        integracao=AdsIntegracaoRef(tipo="MercadoLivre"),
        loja=AdsLojaRef(id=1),
        nome="Meu Anúncio",
    )
    result = request.model_dump(by_alias=True, exclude_none=True)
    assert result["produto"]["id"] == 123
    assert result["integracao"]["tipo"] == "MercadoLivre"
    assert result["loja"]["id"] == 1
    assert result["nome"] == "Meu Anúncio"


def test_anuncios_save_response_dto_from_fixture() -> None:
    """Deserialize AnunciosSaveResponseDTO from fixture JSON."""
    payload = json.loads((FIXTURES_DIR / "ads_create.json").read_text(encoding="utf-8"))
    model = AnunciosSaveResponseDTO.model_validate(payload["data"])
    assert model.id == 123
    assert model.ids_variacoes == [456, 789]
