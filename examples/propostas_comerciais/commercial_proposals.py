"""Example: Propostas Comerciais (Commercial Proposals) workflow.

Demonstrates listing and creating multiple commercial proposals.

Endpoints:
    - GET /propostas-comerciais
    - POST /propostas-comerciais
    - DELETE /propostas-comerciais

Docs:
    - https://developer.bling.com.br/referencia#/Propostas%20Comerciais/get_propostas_comerciais
    - https://developer.bling.com.br/referencia#/Propostas%20Comerciais/post_propostas_comerciais
"""

from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING, cast

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.propostas_comerciais import PropostasComerciaisPostRequest
from bling_erp_api.models.generated.schemas.orcamentos import (
    OrcamentosContatoDTO,
    OrcamentosFormaPagamentoDTO,
    OrcamentosItemDTO,
    OrcamentosParcelaDTO,
    OrcamentosProdutoDTO,
)

if TYPE_CHECKING:
    from bling_erp_api.models.aliases import (
        PropostasComerciaisDeleteResponse200,
        PropostasComerciaisGetResponse200,
        PropostasComerciaisIdPropostaComercialGetResponse200,
    )


# ---------------------------------------------------------------------------
# IDs da sua conta Bling — substitua pelos valores reais
# ---------------------------------------------------------------------------
CONTACT_ID = 18164239939  # ID real de um contato existente
PRODUCT_ID = 16656139131  # ID real de um produto existente
PAYMENT_METHOD_ID = 10143530  # Substitua pelo ID real de uma forma de pagamento existente
PROPOSALS_TO_DELETE = [25966071122]  # IDs das propostas a serem deletadas

# ---------------------------------------------------------------------------


def list_proposals() -> PropostasComerciaisGetResponse200:
    """List all proposals."""
    with BlingClient.from_env() as client:
        return client.propostas_comerciais.listar()


# ---------------------------------------------------------------------------
# Versão 1: payload mínimo com dict puro (chaves Bling/camelCase)
# Não precisa instanciar nenhum modelo — ideal para testes rápidos.
# ---------------------------------------------------------------------------
def create_proposal_dict() -> PropostasComerciaisIdPropostaComercialGetResponse200:
    """Create a proposal using a plain dict payload (no models needed)."""
    data: dict[str, object] = {
        "contato": {"id": CONTACT_ID},
        "itens": [
            {
                "produto": {"id": PRODUCT_ID},
                "quantidade": 1.0,
                "valor": 100.00,
            },
        ],
        "parcelas": [
            {
                "dataVencimento": "2026-06-30",
                "valor": 100.00,
                "formaPagamento": {"id": PAYMENT_METHOD_ID},
            },
        ],
    }

    with BlingClient.from_env() as client:
        response = client.propostas_comerciais.criar(
            dados=cast("PropostasComerciaisPostRequest", data)
        )
        print("Proposta criada (dict):", response.model_dump_json(indent=2, by_alias=True))
        if response.data is None:
            msg = "Failed to create proposal: no data in response"
            raise RuntimeError(msg)
        return client.propostas_comerciais.obter(id_proposta_comercial=response.data.id)


# ---------------------------------------------------------------------------
# Versão 2: payload com modelos Pydantic (campos Python/snake_case)
# Prefira esta versão quando quiser autocomplete, validação e serialização tipada.
# ---------------------------------------------------------------------------
def create_proposal_model() -> PropostasComerciaisIdPropostaComercialGetResponse200:
    """Create a proposal using generated Pydantic request models."""
    data = PropostasComerciaisPostRequest(
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
        response = client.propostas_comerciais.criar(dados=data)
        print("Proposta criada (model):", response.model_dump_json(indent=2, by_alias=True))
        if response.data is None:
            msg = "Failed to create proposal: no data in response"
            raise RuntimeError(msg)
        return client.propostas_comerciais.obter(id_proposta_comercial=response.data.id)


# ---------------------------------------------------------------------------
def delete_proposals(id_list: list[int]) -> PropostasComerciaisDeleteResponse200:
    """Delete proposals by ID."""
    with BlingClient.from_env() as client:
        return client.propostas_comerciais.remover_varios(ids_propostas_comerciais=id_list)


def main() -> None:
    """Run examples."""
    print("=== Listing proposals ===")
    proposals = list_proposals()
    print(proposals.model_dump_json(indent=2, by_alias=True))

    print("\n=== Creating proposal (dict payload) ===")
    created = create_proposal_dict()
    print(created.model_dump_json(indent=2, by_alias=True))

    # print("\n=== Creating proposal (Pydantic models) ===")
    # created_with_model = create_proposal_model()
    # print(created_with_model.model_dump_json(indent=2, by_alias=True))

    print("\n=== Deleting proposals ===")
    deleted = delete_proposals(id_list=PROPOSALS_TO_DELETE)
    print(deleted.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
