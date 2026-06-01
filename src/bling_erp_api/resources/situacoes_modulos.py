"""Situacoes Modulos (Situation Modules) resource."""

from __future__ import annotations

from bling_erp_api.models.generated.situacoes_modulos import (
    SituacoesModulosGetResponse200,
    SituacoesModulosIdModuloSistemaAcoesGetResponse200,
    SituacoesModulosIdModuloSistemaGetResponse200,
    SituacoesModulosIdModuloSistemaTransicoesGetResponse200,
)
from bling_erp_api.resources.base import BaseResource


class SituacoesModulosResource(BaseResource):
    """Situacoes Modulos API resource. Maps to /situacoes/modulos endpoints.

    Provides operations for situation modules (modulos de situacoes) in the
    Bling API. Canonical methods are in pt-BR following the official Bling
    documentation; English aliases are available for compatibility.
    """

    BASE_PATH = "/situacoes/modulos"

    # ------------------------------------------------------------------
    # listar / list
    # ------------------------------------------------------------------

    def listar(self) -> SituacoesModulosGetResponse200:
        """Lista todos os módulos de situações.

        Endpoint: GET /situacoes/modulos

        Lista todos os módulos de situações disponíveis no sistema.

        Returns:
            Bling API response. Response schemas: 200: SituacoesModulosGetResponse200
        """
        raw = self._get(self.BASE_PATH)
        return SituacoesModulosGetResponse200.model_validate(raw)

    def list(self) -> SituacoesModulosGetResponse200:
        """Compatibility alias for ``listar()``.

        Lista todos os módulos de situações.

        Endpoint: GET /situacoes/modulos

        Returns:
            Bling API response. Response schemas: 200: SituacoesModulosGetResponse200
        """
        return self.listar()

    # ------------------------------------------------------------------
    # obter / get
    # ------------------------------------------------------------------

    def obter(self, id_modulo_sistema: int) -> SituacoesModulosIdModuloSistemaGetResponse200:
        """Obtém as situações de um módulo específico.

        Endpoint: GET /situacoes/modulos/{idModuloSistema}

        Obtém as situações de um módulo específico pelo ID.

        Args:
            id_modulo_sistema: ID do módulo do sistema
                (Bling: ``idModuloSistema``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: SituacoesModulosIdModuloSistemaGetResponse200;
            404: ErrorResponse
        """
        raw = self._get(f"{self.BASE_PATH}/{id_modulo_sistema}")
        return SituacoesModulosIdModuloSistemaGetResponse200.model_validate(raw)

    def get(self, module_id: int) -> SituacoesModulosIdModuloSistemaGetResponse200:
        """Compatibility alias for ``obter()``.

        Obtém as situações de um módulo específico.

        Endpoint: GET /situacoes/modulos/{idModuloSistema}

        Args:
            module_id: ID do módulo do sistema
                (Bling: ``idModuloSistema``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: SituacoesModulosIdModuloSistemaGetResponse200;
            404: ErrorResponse
        """
        return self.obter(id_modulo_sistema=module_id)

    # ------------------------------------------------------------------
    # listar_acoes / list_actions
    # ------------------------------------------------------------------

    def listar_acoes(
        self, id_modulo_sistema: int
    ) -> SituacoesModulosIdModuloSistemaAcoesGetResponse200:
        """Lista as ações disponíveis para um módulo.

        Endpoint: GET /situacoes/modulos/{idModuloSistema}/acoes

        Lista as ações disponíveis para um módulo de situação específico.

        Args:
            id_modulo_sistema: ID do módulo do sistema
                (Bling: ``idModuloSistema``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: SituacoesModulosIdModuloSistemaAcoesGetResponse200;
            404: ErrorResponse
        """
        raw = self._get(f"{self.BASE_PATH}/{id_modulo_sistema}/acoes")
        return SituacoesModulosIdModuloSistemaAcoesGetResponse200.model_validate(raw)

    def list_actions(self, module_id: int) -> SituacoesModulosIdModuloSistemaAcoesGetResponse200:
        """Compatibility alias for ``listar_acoes()``.

        Lista as ações disponíveis para um módulo.

        Endpoint: GET /situacoes/modulos/{idModuloSistema}/acoes

        Args:
            module_id: ID do módulo do sistema
                (Bling: ``idModuloSistema``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: SituacoesModulosIdModuloSistemaAcoesGetResponse200;
            404: ErrorResponse
        """
        return self.listar_acoes(id_modulo_sistema=module_id)

    # ------------------------------------------------------------------
    # listar_transicoes / list_transitions
    # ------------------------------------------------------------------

    def listar_transicoes(
        self, id_modulo_sistema: int
    ) -> SituacoesModulosIdModuloSistemaTransicoesGetResponse200:
        """Lista as transições de um módulo.

        Endpoint: GET /situacoes/modulos/{idModuloSistema}/transicoes

        Lista as transições disponíveis para um módulo de situação específico.

        Args:
            id_modulo_sistema: ID do módulo do sistema
                (Bling: ``idModuloSistema``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: SituacoesModulosIdModuloSistemaTransicoesGetResponse200;
            404: ErrorResponse
        """
        raw = self._get(f"{self.BASE_PATH}/{id_modulo_sistema}/transicoes")
        return SituacoesModulosIdModuloSistemaTransicoesGetResponse200.model_validate(raw)

    def list_transitions(
        self, module_id: int
    ) -> SituacoesModulosIdModuloSistemaTransicoesGetResponse200:
        """Compatibility alias for ``listar_transicoes()``.

        Lista as transições de um módulo.

        Endpoint: GET /situacoes/modulos/{idModuloSistema}/transicoes

        Args:
            module_id: ID do módulo do sistema
                (Bling: ``idModuloSistema``, integer, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: SituacoesModulosIdModuloSistemaTransicoesGetResponse200;
            404: ErrorResponse
        """
        return self.listar_transicoes(id_modulo_sistema=module_id)
