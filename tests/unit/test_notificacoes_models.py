"""Testes de modelos Pydantic para Notificações."""

import json
from pathlib import Path

from bling_erp_api.models.generated.notificacoes import (
    NotificacoesDadosDTO,
    NotificacoesQuantidadeDTO,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def test_notificacoes_dados_dto_from_list() -> None:
    """Valida que NotificacoesDadosDTO consegue ler a fixture de listagem."""
    path = FIXTURES_DIR / "notificacoes_list.json"
    payload = json.loads(path.read_text())
    items = [NotificacoesDadosDTO.model_validate(item) for item in payload["data"]]
    assert len(items) == 2
    assert items[0].id == "01ARZ3NDEKTSV4RRFFQ69G5FAV"
    assert items[0].emitente == "Bling"
    assert items[0].modulo == "FISCAL"
    assert items[1].titulo == "CT-e Autorizado"


def test_notificacoes_quantidade_dto() -> None:
    """Valida que NotificacoesQuantidadeDTO consegue ler a fixture de quantidade."""
    path = FIXTURES_DIR / "notificacoes_quantidade.json"
    payload = json.loads(path.read_text())
    dto = NotificacoesQuantidadeDTO.model_validate(payload["data"])
    assert dto.quantidade == 42
