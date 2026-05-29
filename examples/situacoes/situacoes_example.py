"""Example: Situacoes (Situations), Modulos, and Transicoes workflow.

Demonstrates CRUD for situations, listing modules, and managing transitions.

Usage:
    BLING_API_KEY="your_key" python examples/situacoes/situacoes_example.py
"""

from __future__ import annotations

from bling_erp_api import BlingClient


def main() -> None:
    """Run the situations example."""
    client = BlingClient.from_env()

    # Access the three situation resources
    # pt-BR canonical names:
    situacoes = client.situacoes
    modulos = client.situacoes_modulos
    transicoes = client.situacoes_transicoes
    # English aliases:
    # client.situations, client.situation_modules, client.situation_transitions

    # --- Situacoes Modulos ---
    print("Listing situation modules...")
    result = modulos.listar()
    print(f"Modules: {result}")

    # Get situations for a specific module
    # module_situations = modulos.obter(id_modulo_sistema=1)
    # print(f"Module situations: {module_situations}")

    # List available actions for a module
    # actions = modulos.listar_acoes(id_modulo_sistema=1)
    # print(f"Actions: {actions}")

    # List transitions for a module
    # trans_list = modulos.listar_transicoes(id_modulo_sistema=1)
    # print(f"Transitions: {trans_list}")

    # --- Situacoes (CRUD) ---
    # Create a new situation
    # new_situation = situacoes.criar({
    #     "nome": "Nova Situacao",
    #     "idModuloSistema": 1,
    #     "cor": "#FF5733",
    # })
    # print(f"Created: {new_situation}")

    # Get a situation
    # situation = situacoes.obter(10)
    # print(f"Situation: {situation}")

    # Update a situation
    # situacoes.alterar(10, {"nome": "Updated", "cor": "#00FF00"})

    # Delete a situation
    # situacoes.remover(10)

    # --- Situacoes Transicoes (CRUD) ---
    # Create a transition
    # new_transition = transicoes.criar({
    #     "situacaoOrigem": {"id": 10},
    #     "situacaoDestino": {"id": 11},
    # })
    # print(f"Created transition: {new_transition}")

    # Get a transition
    # transition = transicoes.obter(100)
    # print(f"Transition: {transition}")

    # Update a transition
    # transicoes.alterar(100, {"ativo": False})

    # Delete a transition
    # transicoes.remover(100)

    print(f"Other resources: {situacoes.BASE_PATH}, {transicoes.BASE_PATH}")
    print(f"Situations: {situacoes.BASE_PATH}, {transicoes.BASE_PATH}")


if __name__ == "__main__":
    main()
