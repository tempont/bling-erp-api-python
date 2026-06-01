"""Model tests for situation models."""

import json
from pathlib import Path
from typing import Any

from bling_erp_api.models.generated.situacoes import (
    SituacoesDadosDTO,
    SituacoesDTO,
)
from bling_erp_api.models.generated.situacoes_modulos import (
    SituacoesAcaoDTO,
    SituacoesModuloDTO,
)
from bling_erp_api.models.generated.situacoes_transicoes import (
    SituacoesTransicaoDTO,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def _load_fixture(name: str) -> dict[str, Any]:
    return json.loads((FIXTURES_DIR / name).read_text())


class TestSituacoesModels:
    """Tests for SituacoesDTO and SituacoesDadosDTO models."""

    def test_deserialize_situacao(self) -> None:
        """Should deserialize a single SituacoesDTO from fixture."""
        data = _load_fixture("situacoes_get.json")
        inner = data["data"]
        model = SituacoesDTO(**inner)  # pyright: ignore[reportUnknownArgumentType]
        assert model.id == 10
        assert model.nome == "Em aberto"

    def test_deserialize_situacao_with_dados(self) -> None:
        """Should deserialize SituacoesDadosDTO with aliased fields."""
        data = _load_fixture("situacoes_get.json")
        inner = data["data"]
        model = SituacoesDadosDTO(
            idHerdado=inner.get("idHerdado"),  # pyright: ignore[reportUnknownArgumentType, reportCallIssue]
            cor=inner.get("cor"),  # pyright: ignore[reportUnknownArgumentType]
        )
        assert model.id_herdado == 5
        assert model.cor == "#E9DC40"


class TestSituacoesModuloModels:
    """Tests for SituacoesModuloDTO and SituacoesAcaoDTO models."""

    def test_deserialize_modulo_list(self) -> None:
        """Should deserialize a list of SituacoesModuloDTO from fixture."""
        data = _load_fixture("situacoes_modulos_list.json")
        items = data["data"]
        models = [SituacoesModuloDTO(**item) for item in items]  # pyright: ignore[reportUnknownArgumentType]
        assert len(models) == 2
        assert models[0].id == 1  # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]
        assert models[0].nome == "Vendas"  # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]
        assert models[0].criar_situacoes is True  # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]

    def test_deserialize_acao_list(self) -> None:
        """Should deserialize a list of SituacoesAcaoDTO from fixture."""
        data = _load_fixture("situacoes_modulos_acoes.json")
        items = data["data"]
        models = [SituacoesAcaoDTO(**item) for item in items]  # pyright: ignore[reportUnknownArgumentType]
        assert len(models) == 2
        assert models[0].id == 1  # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]
        assert models[0].nome == "lancarEstoque"  # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]


class TestSituacoesTransicaoModels:
    """Tests for SituacoesTransicaoDTO model."""

    def test_deserialize_transicao(self) -> None:
        """Should deserialize a SituacoesTransicaoDTO with nested SituacoesDTO."""
        data = _load_fixture("situacoes_modulos_transicoes.json")
        inner = data["data"][0]
        model = SituacoesTransicaoDTO(**inner)  # pyright: ignore[reportUnknownArgumentType]
        assert model.id == 100
        assert model.ativo is True
        assert model.situacao_origem is not None
        assert model.situacao_origem.nome == "Em aberto"

    def test_deserialize_transicao_extra_allowed(self) -> None:
        """Extra fields (campoNovoBling) should be preserved via BlingModel extra='allow'."""
        data = _load_fixture("situacoes_modulos_transicoes.json")
        inner = data["data"][0]
        model = SituacoesTransicaoDTO(**inner)  # pyright: ignore[reportUnknownArgumentType]
        assert getattr(model, "campoNovoBling", None) == "mantido"  # pyright: ignore[reportAttributeAccessIssue]
