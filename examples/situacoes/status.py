"""Example: Transactions Status Workflow.

Demonstrates CRUD for managing statuses.

Endpoints:
    - GET /situacoes/{idSituacao}
    - POST /situacoes
    - DELETE /situacoes/{idSituacao}
    - PUT /situacoes/{idSituacao}

Docs:
    - https://developer.bling.com.br/referencia#/Situa%C3%A7%C3%B5es/get_situacoes__idSituacao_
    - https://developer.bling.com.br/referencia#/Situa%C3%A7%C3%B5es/post_situacoes
    - https://developer.bling.com.br/referencia#/Situa%C3%A7%C3%B5es/delete_situacoes__idSituacao_
    - https://developer.bling.com.br/referencia#/Situa%C3%A7%C3%B5es/put_situacoes__idSituacao_
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.situacoes import (
        SituacoesIdSituacaoGetResponse200,
        SituacoesPostRequest,
    )


def get_status(status_id: int) -> SituacoesIdSituacaoGetResponse200:
    """Get a status by ID."""
    client = BlingClient.from_env()
    return client.situacoes.obter(id_situacao=status_id)


def post_status(payload: SituacoesPostRequest):
    """Create a new status."""
    client = BlingClient.from_env()
    return client.situacoes.criar(dados=payload)


def delete_status(situation_id: int):
    """Delete a status by ID."""
    client = BlingClient.from_env()
    return client.situacoes.remover(id_situacao=situation_id)


def put_status(status_id: int, payload: SituacoesPostRequest):
    """Update a status by ID."""
    client = BlingClient.from_env()
    return client.situacoes.alterar(id_situacao=status_id, dados=payload)


def main() -> None:
    """Run the status example."""
    ex_status_id = 6

    print("Getting status...")
    print(get_status(status_id=ex_status_id).model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
