"""Example: Proposta Comercial (Commercial Proposal) single-record workflow.

Demonstrates retrieving, updating, changing status, and deleting one commercial
proposal.

Endpoints:
    - GET /propostas-comerciais/{idPropostaComercial}
    - PUT /propostas-comerciais/{idPropostaComercial}
    - PATCH /propostas-comerciais/{idPropostaComercial}/situacoes
    - DELETE /propostas-comerciais/{idPropostaComercial}

Docs:
    - https://developer.bling.com.br/referencia#/Propostas%20Comerciais/get_propostas_comerciais__idPropostaComercial_
    - https://developer.bling.com.br/referencia#/Propostas%20Comerciais/put_propostas_comerciais__idPropostaComercial_
    - https://developer.bling.com.br/referencia#/Propostas%20Comerciais/patch_propostas_comerciais__idPropostaComercial__situacoes
    - https://developer.bling.com.br/referencia#/Propostas%20Comerciais/delete_propostas_comerciais__idPropostaComercial_
"""

from __future__ import annotations

import json
from datetime import date
from typing import TYPE_CHECKING

from pydantic import BaseModel

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.propostas_comerciais import (
    PropostasComerciaisIdPropostaComercialPutRequest,
)
from bling_erp_api.models.generated.schemas.orcamentos import (
    OrcamentosContatoDTO,
    OrcamentosFormaPagamentoDTO,
    OrcamentosItemDTO,
    OrcamentosParcelaDTO,
    OrcamentosProdutoDTO,
)

if TYPE_CHECKING:
    from bling_erp_api.models.aliases import (
        PropostasComerciaisIdPropostaComercialGetResponse200,
    )
    from bling_erp_api.types import JsonObject


# ---------------------------------------------------------------------------
# IDs da sua conta Bling - substitua pelos valores reais antes de executar.
# ---------------------------------------------------------------------------
PROPOSAL_ID = 25966071122
CONTACT_ID = 18164239939
PRODUCT_ID = 16656139131
PAYMENT_METHOD_ID = 10143530


def dump_response(response: BaseModel | JsonObject | None) -> str:
    """Serialize modeled and no-content responses with the same example shape."""
    if isinstance(response, BaseModel):
        return response.model_dump_json(indent=2, by_alias=True)
    return json.dumps(response, indent=2, ensure_ascii=False)


def get_proposal(proposal_id: int) -> PropostasComerciaisIdPropostaComercialGetResponse200:
    """Get a commercial proposal by ID."""
    with BlingClient.from_env() as client:
        return client.propostas_comerciais.obter(id_proposta_comercial=proposal_id)


def update_proposal_dict(proposal_id: int) -> JsonObject | None:
    """Update a proposal using a plain dict payload with Bling field names."""
    data: dict[str, object] = {
        "contato": {"id": CONTACT_ID},
        "itens": [
            {
                "produto": {"id": PRODUCT_ID},
                "quantidade": 1.0,
                "valor": 100.00,
            }
        ],
        "parcelas": [
            {
                "dataVencimento": "2026-06-30",
                "valor": 100.00,
                "formaPagamento": {"id": PAYMENT_METHOD_ID},
            }
        ],
    }

    with BlingClient.from_env() as client:
        return client.propostas_comerciais.alterar(
            id_proposta_comercial=proposal_id,
            dados=data,
        )


def update_proposal_model(proposal_id: int) -> JsonObject | None:
    """Update a proposal using generated Pydantic request models."""
    data = PropostasComerciaisIdPropostaComercialPutRequest(
        contato=OrcamentosContatoDTO(id=CONTACT_ID),
        itens=[
            OrcamentosItemDTO(
                produto=OrcamentosProdutoDTO(id=PRODUCT_ID),
                quantidade=1.0,
                valor=100.00,
            )
        ],
        parcelas=[
            OrcamentosParcelaDTO(
                data_vencimento=date(2026, 6, 30),
                valor=100.00,
                forma_pagamento=OrcamentosFormaPagamentoDTO(id=PAYMENT_METHOD_ID),
            )
        ],
    )

    with BlingClient.from_env() as client:
        return client.propostas_comerciais.alterar(
            id_proposta_comercial=proposal_id,
            dados=data,
        )


def update_proposal_status(proposal_id: int, status: str) -> JsonObject | None:
    """Update a commercial proposal status."""
    with BlingClient.from_env() as client:
        return client.propostas_comerciais.alterar_situacao(
            id_proposta_comercial=proposal_id,
            situacao=status,
        )


def delete_proposal(proposal_id: int) -> JsonObject | None:
    """Delete a commercial proposal by ID."""
    with BlingClient.from_env() as client:
        return client.propostas_comerciais.remover(id_proposta_comercial=proposal_id)


def main() -> None:
    """Run safe read example and keep write operations explicit."""
    print("=== Getting proposal ===")
    proposal = get_proposal(PROPOSAL_ID)
    print(proposal.model_dump_json(indent=2, by_alias=True))

    # PUT/PATCH/DELETE endpoints usually return 204 NoContent. When that
    # happens, dump_response() prints null to keep the output pattern explicit.

    # print("\n=== Updating proposal (dict payload) ===")
    # updated = update_proposal_dict(PROPOSAL_ID)
    # print(dump_response(updated))

    # print("\n=== Updating proposal (Pydantic models) ===")
    # updated_with_model = update_proposal_model(PROPOSAL_ID)
    # print(dump_response(updated_with_model))

    # print("\n=== Updating proposal status ===")
    # status_updated = update_proposal_status(PROPOSAL_ID, "Aprovado")
    # print(dump_response(status_updated))

    # print("\n=== Deleting proposal ===")
    # deleted = delete_proposal(PROPOSAL_ID)
    # print(dump_response(deleted))


if __name__ == "__main__":
    main()
