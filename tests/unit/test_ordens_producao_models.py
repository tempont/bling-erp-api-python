"""Testes de modelos Pydantic para Ordens de Produção."""

import json
from pathlib import Path

from bling_erp_api.models.generated.ordens_producao import (
    OrdensProducaoCreateRequestDTO,
    OrdensProducaoDadosBaseDTO,
    OrdensProducaoDadosGeradosPorDemandaDTO,
    OrdensProducaoDetailResponseDTO,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def test_ordens_producao_dados_base_dto_from_list() -> None:
    """Valida que OrdensProducaoDadosBaseDTO consegue ler a fixture de listagem."""
    path = FIXTURES_DIR / "ordens_producao_list.json"
    payload = json.loads(path.read_text())
    items = [OrdensProducaoDadosBaseDTO.model_validate(item) for item in payload["data"]]
    assert items[0].id == 1
    assert items[0].numero == 1001
    assert items[0].deposito is not None
    assert items[0].deposito.id_origem == 10
    assert items[0].situacao is not None
    assert items[0].situacao.nome == "Em aberto"


def test_ordens_producao_detail_dto() -> None:
    """Valida que OrdensProducaoDetailResponseDTO consegue ler a fixture de detalhe."""
    path = FIXTURES_DIR / "ordens_producao_get.json"
    payload = json.loads(path.read_text())
    dto = OrdensProducaoDetailResponseDTO.model_validate(payload["data"])
    assert dto.id == 1
    assert dto.data_previsao_inicio == "2025-02-01"
    assert dto.itens is not None
    assert dto.itens[0].produto is not None
    assert dto.itens[0].produto.nome == "Produto A"
    assert dto.vendas is not None
    assert dto.vendas[0].numero == 5001
    assert dto.vendas[0].contato is not None
    assert dto.vendas[0].contato.nome == "Cliente X"


def test_ordens_producao_create_request_dto() -> None:
    """Valida que OrdensProducaoCreateRequestDTO aceita dados mínimos."""
    dto = OrdensProducaoCreateRequestDTO.model_validate(
        {
            "numero": 2001,
            "deposito": {"idOrigem": 10, "idDestino": 30},
            "situacao": {"id": 1},
            "itens": [
                {"produto": {"id": 100}, "quantidade": 10.0},
            ],
        }
    )
    assert dto.numero == 2001
    assert dto.deposito is not None
    assert dto.deposito.id_origem == 10
    assert dto.itens is not None
    assert dto.itens[0].produto is not None
    assert dto.itens[0].produto.id == 100


def test_ordens_producao_gerados_por_demanda_dto() -> None:
    """Valida que OrdensProducaoDadosGeradosPorDemandaDTO consegue ler a fixture."""
    path = FIXTURES_DIR / "ordens_producao_gerar.json"
    payload = json.loads(path.read_text())
    items = [
        OrdensProducaoDadosGeradosPorDemandaDTO.model_validate(item) for item in payload["data"]
    ]
    assert items[0].id == 10
    assert items[0].deposito is not None
    assert items[0].deposito.id_destino == 20
    assert items[0].itens is not None
    assert items[0].itens[0].produto is not None
    assert items[0].itens[0].produto.nome == "Produto A"
