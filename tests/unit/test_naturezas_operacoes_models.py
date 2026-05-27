"""Testes de modelos Pydantic para Naturezas de Operações."""

import json
from pathlib import Path

from bling_erp_api.models.generated.calculos_impostos import (
    CalculosImpostosCalculoDTO,
    CalculosImpostosDadosDTO,
)
from bling_erp_api.models.generated.naturezas_operacoes import (
    NaturezasOperacoesDadosDTO,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def test_naturezas_operacoes_dados_dto_from_list():
    """Deserializa resposta de listagem com NaturezasOperacoesDadosDTO."""
    path = FIXTURES_DIR / "naturezas_operacoes_list.json"
    payload = json.loads(path.read_text())
    items = [NaturezasOperacoesDadosDTO.model_validate(item) for item in payload["data"]]
    assert items[0].id == 1001
    assert items[0].descricao == "Venda de Mercadoria"
    assert items[0].situacao == 1
    assert items[0].padrao == 1
    assert items[1].id == 1002
    assert items[1].descricao == "Compra de Mercadoria"


def test_calculos_impostos_calculo_dto():
    """Valida construção de CalculosImpostosCalculoDTO."""
    dto = CalculosImpostosCalculoDTO.model_validate(
        {
            "tipoNota": 1,
            "uf": "RS",
            "municipio": {"id": 4302105},
            "loja": {"id": 12345678},
            "produto": {
                "id": 98765,
                "valorUnitario": 100.0,
                "cupomFiscal": 0,
                "origem": 0,
                "quantidade": 1.0,
            },
        }
    )
    assert dto.tipo_nota == 1
    assert dto.uf == "RS"
    assert dto.municipio.id == 4302105
    assert dto.loja.id == 12345678
    assert dto.produto.id == 98765


def test_calculos_impostos_dados_dto_from_tributacao():
    """Deserializa resposta de tributação com CalculosImpostosDadosDTO."""
    path = FIXTURES_DIR / "naturezas_operacoes_tributacao.json"
    payload = json.loads(path.read_text())
    dto = CalculosImpostosDadosDTO.model_validate(payload["data"])
    assert dto.cfop == 5102
    assert dto.icms is not None
    assert dto.icms.aliquota == 18.0
    assert dto.icms.valor_imposto == 18.0
    assert dto.pis is not None
    assert dto.pis.aliquota == 1.65
