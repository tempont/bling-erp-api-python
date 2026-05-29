"""Model tests for Propostas Comerciais (Commercial Proposals) models."""

import json
from datetime import date
from pathlib import Path

from bling_erp_api.models.generated.propostas_comerciais import (
    PropostasComerciaisGetResponse200,
    PropostasComerciaisIdPropostaComercialGetResponse200,
    PropostasComerciaisPostRequest,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def _load_fixture(name: str) -> dict[str, object]:
    return json.loads((FIXTURES_DIR / name).read_text())


class TestCommercialProposalsListResponse:
    """Tests for the commercial proposals list response model (PropostasComerciaisGetResponse200)."""

    def test_deserialize_list(self) -> None:
        """Should deserialize list fixture with two items."""
        data = _load_fixture("propostas_comerciais_list.json")
        response = PropostasComerciaisGetResponse200.model_validate(data)  # type: ignore[reportUnknownMemberType]
        assert response.data is not None
        assert len(response.data) == 2
        item = response.data[0]
        assert item.id == 5001
        assert item.data == date(2024, 5, 10)
        assert item.situacao == "Pendente"
        assert item.total == 3500.0

    def test_deserialize_list_contato(self) -> None:
        """Should deserialize contato sub-object."""
        data = _load_fixture("propostas_comerciais_list.json")
        response = PropostasComerciaisGetResponse200.model_validate(data)  # type: ignore[reportUnknownMemberType]
        assert response.data is not None
        assert response.data[0].contato is not None
        assert response.data[0].contato.id == 800

    def test_deserialize_list_loja(self) -> None:
        """Should deserialize loja sub-object."""
        data = _load_fixture("propostas_comerciais_list.json")
        response = PropostasComerciaisGetResponse200.model_validate(data)  # type: ignore[reportUnknownMemberType]
        assert response.data is not None
        assert response.data[0].loja is not None
        assert response.data[0].loja.id == 1

    def test_deserialize_list_extra_allowed(self) -> None:
        """Extra fields (campoNovoBling) should be preserved."""
        data = _load_fixture("propostas_comerciais_list.json")
        response = PropostasComerciaisGetResponse200.model_validate(data)  # type: ignore[reportUnknownMemberType]
        assert response.data is not None
        # pyright doesn't know about extra fields on Pydantic models with extra="allow"
        assert getattr(response.data[0], "campoNovoBling", None) == "mantido"  # pyright: ignore[reportAttributeAccessIssue]


class TestCommercialProposalsGetResponse:
    """Tests for the commercial proposal detail response model (PropostasComerciaisIdPropostaComercialGetResponse200).

    Note: This model inherits directly from OrcamentosDadosBaseDTO + OrcamentosDadosDTO
    (no ``data`` wrapper). The fixture has the API ``data`` envelope; the test unwraps it.
    """

    def test_deserialize_get(self) -> None:
        """Should deserialize get fixture with base and detail fields."""
        data = _load_fixture("propostas_comerciais_get.json")
        inner = data["data"]
        assert isinstance(inner, dict)
        response = PropostasComerciaisIdPropostaComercialGetResponse200.model_validate(inner)  # type: ignore[reportUnknownMemberType]
        assert response.id == 5001
        assert response.situacao == "Pendente"
        assert response.observacoes == "Proposta válida por 30 dias"

    def test_deserialize_get_itens(self) -> None:
        """Should deserialize itens as typed OrcamentosItemDTO instances."""
        data = _load_fixture("propostas_comerciais_get.json")
        inner = data["data"]
        assert isinstance(inner, dict)
        response = PropostasComerciaisIdPropostaComercialGetResponse200.model_validate(inner)  # type: ignore[reportUnknownMemberType]
        itens = response.itens
        assert len(itens) == 1
        assert itens[0].codigo == "CONS-001"
        assert itens[0].valor == 3000.0

    def test_deserialize_get_parcelas(self) -> None:
        """Should deserialize parcelas as typed OrcamentosParcelaDTO instances."""
        data = _load_fixture("propostas_comerciais_get.json")
        inner = data["data"]
        assert isinstance(inner, dict)
        response = PropostasComerciaisIdPropostaComercialGetResponse200.model_validate(inner)  # type: ignore[reportUnknownMemberType]
        parcelas = response.parcelas
        assert parcelas is not None
        assert len(parcelas) == 1
        assert parcelas[0].valor == 3500.0

    def test_deserialize_get_vendedor(self) -> None:
        """Should deserialize vendedor as OrcamentosVendedorDTO."""
        data = _load_fixture("propostas_comerciais_get.json")
        inner = data["data"]
        assert isinstance(inner, dict)
        response = PropostasComerciaisIdPropostaComercialGetResponse200.model_validate(inner)  # type: ignore[reportUnknownMemberType]
        assert response.vendedor is not None
        assert response.vendedor.id == 50


class TestCommercialProposalsRequestModels:
    """Tests for commercial proposal request models (PropostasComerciaisPostRequest)."""

    def test_post_request_accepts_fields(self) -> None:
        """Should construct PropostasComerciaisPostRequest with snake_case fields."""
        model = PropostasComerciaisPostRequest.model_validate(  # type: ignore[reportUnknownMemberType]
            {
                "contato": {"id": 800},
                "itens": [
                    {
                        "codigo": "SERV-1",
                        "descricaoDetalhada": "Service",
                        "quantidade": 1,
                        "valor": 100.0,
                    }
                ],
                "parcelas": [
                    {
                        "dataVencimento": "2024-06-01",
                        "valor": 100.0,
                        "formaPagamento": {"id": 1},
                    }
                ],
            }
        )
        assert model.contato is not None
        assert model.contato.id == 800
        assert len(model.itens) == 1
        assert model.itens[0].codigo == "SERV-1"
