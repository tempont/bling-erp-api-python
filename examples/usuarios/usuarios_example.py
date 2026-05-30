"""Example: Usuarios (Users) workflow.

Demonstrates password recovery, reset, and hash verification.

Usage:
    BLING_API_KEY="your_key" python examples/usuarios/usuarios_example.py
"""

from __future__ import annotations

from bling_erp_api import BlingClient


def main() -> None:
    """Run the users example."""
    client = BlingClient.from_env()

    # pt-BR canonical: client.usuarios
    # EN alias: client.users
    usuarios = client.usuarios
    print(f"Usuarios resource ready: {usuarios.BASE_PATH}")

    # Request password recovery
    # usuarios.recuperar_senha("user@example.com")

    # Verify recovery hash
    # result = usuarios.verificar_hash("abc123hash")
    # print(f"Hash valid: {result}")

    # Reset password using hash
    # usuarios.redefinir_senha("abc123hash", "newSecurePassword123")


if __name__ == "__main__":
    main()
