"""Example: Propostas Comerciais (Commercial Proposals) workflow.

Demonstrates listing, creating, retrieving, and managing commercial proposals
using both pt-BR canonical names and English aliases.

Usage:
    BLING_API_KEY="your_key" python examples/commercial_proposals/commercial_proposals_example.py
"""

from __future__ import annotations

from bling_erp_api import BlingClient


def main() -> None:
    """Run the commercial proposals example."""
    client = BlingClient.from_env()

    # Access the commercial proposals resource
    # Canonical pt-BR name:
    propostas = client.propostas_comerciais
    # Or English alias: client.commercial_proposals

    # 1. List commercial proposals with filters
    print("Listing commercial proposals...")
    result = propostas.listar(
        pagina=1,
        limite=10,
        situacao="Pendente",
        data_inicial="2024-01-01",
        data_final="2024-12-31",
    )
    print(f"Found proposals: {result}")

    # 2. Create a new commercial proposal (commented - requires valid data)
    # from bling_erp_api.models.generated.propostas_comerciais import (
    #     PropostasComerciaisPostRequest,
    # )
    # proposal = PropostasComerciaisPostRequest(
    #     contato={"id": 800},
    #     itens=[
    #         {
    #             "codigo": "SERV-001",
    #             "descricaoDetalhada": "IT Consulting - 40h",
    #             "unidade": "UN",
    #             "quantidade": 1,
    #             "valor": 3000.00,
    #         }
    #     ],
    #     parcelas=[
    #         {
    #             "dataVencimento": "2024-07-01",
    #             "valor": 3000.00,
    #             "formaPagamento": {"id": 1},
    #         }
    #     ],
    # )
    # created = propostas.criar(proposal)
    # print(f"Created proposal: {created}")

    # 3. Get a specific commercial proposal
    # proposal = propostas.obter(5001)
    # print(f"Proposal details: {proposal}")

    # 4. Update an existing proposal
    # propostas.alterar(5001, updated_data)

    # 5. Update proposal status
    # propostas.alterar_situacao(5001, "Aprovado")
    # Available statuses: Pendente, Aguardando, Nao aprovado, Aprovado,
    #                     Concluido, Rascunho

    # 6. Delete proposals
    # propostas.remover(5001)
    # propostas.remover_varios([1, 2, 3])


if __name__ == "__main__":
    main()
