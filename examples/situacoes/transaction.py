"""Example: Transactions Status Workflow.

Demonstrates CRUD for managing transitions.

Endpoints:
    - GET /situacoes/transicoes/{idTransicao}
    - POST /situacoes/transicoes
    - DELETE /situacoes/transicoes/{idTransicao}
    - PUT /situacoes/transicoes/{idTransicao}

Docs:
    - https://developer.bling.com.br/referencia#/Situa%C3%A7%C3%B5es%20-%20Transi%C3%A7%C3%B5es/get_situacoes_transicoes__idTransicao_
    - https://developer.bling.com.br/referencia#/Situa%C3%A7%C3%B5es%20-%20Transi%C3%A7%C3%B5es/post_situacoes_transicoes
    - https://developer.bling.com.br/referencia#/Situa%C3%A7%C3%B5es%20-%20Transi%C3%A7%C3%B5es/delete_situacoes_transicoes__idTransicao_
    - https://developer.bling.com.br/referencia#/Situa%C3%A7%C3%B5es%20-%20Transi%C3%A7%C3%B5es/put_situacoes_transicoes__idTransicao_
"""

from __future__ import annotations

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.situacoes import (
    SituacoesIdSituacaoPutRequest,
    SituacoesPostRequest,
)


def get(situation_id: int):
    """Get a status by ID."""
    client = BlingClient.from_env()
    return client.situacoes.obter(id_situacao=situation_id)


def post(module_id: int, name: str, color: str):
    """Create a new status."""
    client = BlingClient.from_env()

    data = SituacoesPostRequest(
        id_modulo_sistema=module_id,
        nome=name,
        cor=color,
    )
    return client.situacoes.criar(dados=data)


def put(situation_id: int, name: str, color: str):
    """Update a status by ID."""
    client = BlingClient.from_env()

    data = SituacoesIdSituacaoPutRequest(
        id_modulo_sistema=situation_id,
        nome=name,
        cor=color,
    )
    return client.situacoes.alterar(id_situacao=situation_id, dados=data)


def delete(situation_id: int):
    """Delete a status by ID."""
    client = BlingClient.from_env()
    return client.situacoes.remover(id_situacao=situation_id)


def main() -> None:
    """Run the situations example."""

    # post_result = post(module_id=1, name="Test", color="#FF2C2C")
    # print(f"New situation created: {post_result}")

    # English aliases:
    # client.situations, client.situation_modules, client.situation_transitions

    # --- Transactions ---

    # get_result = get(situation_id=1)
    # print(f"Situation fetched: {get_result}")

    # post_result = post(module_id=1, name="Test", color="#FF2C2C")
    # print(f"New situation created: {post_result}")

    # put_result = put(situation_id=1, name="Test", color="#FF2C2C")
    # print(f"Situation updated: {put_result}")

    # delete_result = delete(situation_id=1)
    # print(f"Situation deleted: {delete_result}")


if __name__ == "__main__":
    main()
