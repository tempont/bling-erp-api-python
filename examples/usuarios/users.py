"""Example: Usuarios (Users) workflow.

Demonstrates password recovery, reset, and hash verification.

Endpoints:
    - GET /usuarios/verificar-hash
    - PATCH /usuarios/redefinir-senha
    - POST /usuarios/recuperar-senha

Docs:
    - https://developer.bling.com.br/referencia#/Usu%C3%A1rios/get_usuarios_verificar_hash
    - https://developer.bling.com.br/referencia#/Usu%C3%A1rios/patch_usuarios_redefinir_senha
    - https://developer.bling.com.br/referencia#/Usu%C3%A1rios/post_usuarios_recuperar_senha
"""

from __future__ import annotations

from bling_erp_api import BlingClient


def verify_hash(email_hash: str):
    """Verify a password recovery hash.

    Endpoint:
        GET /usuarios/verificar-hash

    Args:
        email_hash: Hash to be verified sent by e-mail.

    """
    client = BlingClient.from_env()
    user = client.usuarios

    return user.verificar_hash(hash_value=email_hash)


def redefine_password(email_hash: str, password: str) -> None:
    """Reset password using a given hash sent by e-mail.

    Endpoint:
        PATCH /usuarios/redefinir-senha

    Args:
        email_hash: Hash to be verified sent by e-mail.
        password: New password.

    """
    client = BlingClient.from_env()
    user = client.usuarios

    user.redefinir_senha(hash_value=email_hash, password=password)


def recover_password(email: str) -> None:
    """Request password recovery.

    Endpoint:
        POST /usuarios/recuperar-senha

    Args:
        email: E-mail of the user to recover password.

    """
    client = BlingClient.from_env()
    user = client.usuarios

    user.recuperar_senha(email=email)


def main() -> None:
    """Run the users example."""
    client = BlingClient.from_env()

    # client.usuarios / client.users
    usuarios = client.usuarios
    print(f"Usuarios resource ready: {usuarios.BASE_PATH}")

    # Request password recovery
    # usuarios.recuperar_senha(email="teste@exemplo.com")

    # Verify recovery hash
    # result = usuarios.verificar_hash("abc123hash")
    # print(f"Hash valid: {result}")

    # Reset password using hash
    # usuarios.redefinir_senha("abc123hash", "newSecurePassword123")


if __name__ == "__main__":
    main()
