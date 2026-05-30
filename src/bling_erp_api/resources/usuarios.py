"""Usuarios (Users) resource."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api.resources.base import BaseResource

if TYPE_CHECKING:
    from bling_erp_api.types import JsonObject


class UsuariosResource(BaseResource):
    """Usuarios API resource. Maps to /usuarios endpoints.

    Provides password recovery and hash verification endpoints for Bling API
    user management. Canonical methods are in pt-BR following the official
    Bling documentation; English aliases are available for compatibility.
    """

    BASE_PATH = "/usuarios"

    # ------------------------------------------------------------------
    # recuperar_senha / recover_password
    # ------------------------------------------------------------------

    def recuperar_senha(self, email: str) -> JsonObject:
        """Solicita a recuperação de senha por email.

        Endpoint: POST /usuarios/recuperar-senha

        Envia uma solicitação de recuperação de senha para o email informado.
        O email deve pertencer a um usuário cadastrado no sistema.

        Args:
            email: Email do usuário para recuperação de senha
                (Bling: ``email``, string, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: UsuariosRecuperarSenhaPostResponse200;
            400: ErrorResponse; 404: ErrorResponse
        """
        return self._post(
            f"{self.BASE_PATH}/recuperar-senha",
            json={"email": email},
        )

    def recover_password(self, email: str) -> JsonObject:
        """Compatibility alias for ``recuperar_senha()``.

        Solicita a recuperação de senha por email.

        Endpoint: POST /usuarios/recuperar-senha

        Envia uma solicitação de recuperação de senha para o email informado.

        Args:
            email: Email do usuário para recuperação de senha
                (Bling: ``email``, string, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: UsuariosRecuperarSenhaPostResponse200;
            400: ErrorResponse; 404: ErrorResponse
        """
        return self.recuperar_senha(email=email)

    # ------------------------------------------------------------------
    # redefinir_senha / reset_password
    # ------------------------------------------------------------------

    def redefinir_senha(self, hash_value: str, password: str) -> JsonObject:
        """Redefine a senha usando o hash de recuperação.

        Endpoint: PATCH /usuarios/redefinir-senha

        Redefine a senha do usuário utilizando o hash recebido por email
        durante o processo de recuperação de senha.

        Args:
            hash_value: Hash de recuperação enviado por email
                (Bling: ``hash``, string, obrigatório)
            password: Nova senha do usuário
                (Bling: ``password``, string, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: JsonObject; 400: ErrorResponse;
            404: ErrorResponse
        """
        return self._patch(
            f"{self.BASE_PATH}/redefinir-senha",
            json={"hash": hash_value, "password": password},
        )

    def reset_password(self, hash_value: str, password: str) -> JsonObject:
        """Compatibility alias for ``redefinir_senha()``.

        Redefine a senha usando o hash de recuperação.

        Endpoint: PATCH /usuarios/redefinir-senha

        Redefine a senha do usuário utilizando o hash recebido por email
        durante o processo de recuperação de senha.

        Args:
            hash_value: Hash de recuperação enviado por email
                (Bling: ``hash``, string, obrigatório)
            password: Nova senha do usuário
                (Bling: ``password``, string, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: JsonObject; 400: ErrorResponse;
            404: ErrorResponse
        """
        return self.redefinir_senha(hash_value=hash_value, password=password)

    # ------------------------------------------------------------------
    # verificar_hash / verify_hash
    # ------------------------------------------------------------------

    def verificar_hash(self, hash_value: str) -> JsonObject:
        """Verifica se um hash de recuperação é válido.

        Endpoint: GET /usuarios/verificar-hash

        Verifica se um hash de recuperação de senha ainda é válido e não
        expirou.

        Args:
            hash_value: Hash de recuperação a ser verificado
                (Bling: ``hash``, string, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: UsuariosVerificarHashGetResponse200;
            400: ErrorResponse; 404: ErrorResponse
        """
        return self._get(
            f"{self.BASE_PATH}/verificar-hash",
            params={"hash": hash_value},
        )

    def verify_hash(self, hash_value: str) -> JsonObject:
        """Compatibility alias for ``verificar_hash()``.

        Verifica se um hash de recuperação é válido.

        Endpoint: GET /usuarios/verificar-hash

        Verifica se um hash de recuperação de senha ainda é válido e não
        expirou.

        Args:
            hash_value: Hash de recuperação a ser verificado
                (Bling: ``hash``, string, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: UsuariosVerificarHashGetResponse200;
            400: ErrorResponse; 404: ErrorResponse
        """
        return self.verificar_hash(hash_value=hash_value)
