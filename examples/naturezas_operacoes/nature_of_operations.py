"""Example: Natureza de Operações (Nature of Operations).

Demonstrates listing natures of operations and obtaining tax calculations.

Endpoints:
    - GET /naturezas-operacoes
    - POST /naturezas-operacoes/{idNaturezaOperacao}/obter-tributacao

Docs:
    - https://developer.bling.com.br/referencia#/Naturezas%20de%20Opera%C3%A7%C3%B5es/get_naturezas_operacoes
    - https://developer.bling.com.br/referencia#/Naturezas%20de%20Opera%C3%A7%C3%B5es/post_naturezas_operacoes__idNaturezaOperacao__obter_tributacao

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.naturezas_operacoes import (
        NaturezasOperacoesGetResponse200,
        NaturezasOperacoesIdNaturezaOperacaoObterTributacaoPostResponse200,
    )
    from bling_erp_api.types import JsonObject


## ---------------------------------------------------------------------------
## LIST NATURES OF OPERATIONS
## ---------------------------------------------------------------------------


def listar_naturezas(
    *,
    pagina: int = 1,
    limite: int = 10,
    situacao: int | None = None,
    descricao: str | None = None,
) -> NaturezasOperacoesGetResponse200:
    """Lista naturezas de operação com filtros opcionais.

    Endpoint: GET /naturezas-operacoes

    Lista naturezas de operação com paginação e filtros opcionais.

    Args:
        pagina: Página da listagem (Bling: ``pagina``, integer, opcional)
        limite: Limite de registros por página (Bling: ``limite``, integer, opcional)
        situacao: Filtrar por situação (Bling: ``situacao``, integer, opcional)
        descricao: Filtrar por descrição (Bling: ``descricao``, string, opcional)

    Returns:
        Bling API response. Response schemas: 200: NaturezasOperacoesDadosDTO[]
    """
    with BlingClient.from_env() as client:
        return client.naturezas_operacoes.listar(
            pagina=pagina,
            limite=limite,
            situacao=situacao,
            descricao=descricao,
        )


## ---------------------------------------------------------------------------
## GET TAX CALCULATION
## ---------------------------------------------------------------------------


def obter_tributacao(
    id_natureza_operacao: int,
    calculo: JsonObject,
) -> NaturezasOperacoesIdNaturezaOperacaoObterTributacaoPostResponse200:
    """Obtém a tributação para uma natureza de operação.

    Endpoint: POST /naturezas-operacoes/{idNaturezaOperacao}/obter-tributacao

    Obtém as regras de tributação que incidem sobre o item para uma
    natureza de operação.

    Args:
        id_natureza_operacao: ID da natureza de operação
            (Bling: ``idNaturezaOperacao``, integer, obrigatório)
        calculo: Dados para o cálculo de impostos
            (Bling: corpo da requisição, obrigatório)

    Returns:
        Bling API response. Response schemas: 200: CalculosImpostosDadosDTO
    """
    with BlingClient.from_env() as client:
        return client.naturezas_operacoes.obter_tributacao(
            id_natureza_operacao=id_natureza_operacao,
            calculo=calculo,
        )


## ---------------------------------------------------------------------------
## MAIN
## ---------------------------------------------------------------------------


def main() -> None:
    """Demonstrate nature of operations."""
    # List natures of operations (read operation)
    result = listar_naturezas(pagina=1, limite=5)
    print(result.model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    # Get tax calculation for a specific nature of operations (read operation)
    tax_nature_id = 1001  # Exemplo — substitua pelo ID real.
    calculation: JsonObject = {
        "tipoNota": 1,
        "uf": "SP",
        "municipio": {"id": 1},
        "loja": {"id": 1},
        "produto": {
            "id": 1,
            "codigo": "001",
            "tipo": "P",
            "origem": 0,
            "ncm": "12345678",
            "quantidade": 1,
            "valorUnitario": 100.0,
            "modalidadeBaseCalculo": 0,
            "total": 100.0,
            "gtin": "SEM GTIN",
            "gtinTributavel": "SEM GTIN",
        },
    }
    result = obter_tributacao(tax_nature_id, calculation)
    print(result.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
