"""Resource para Notificações.

Mapeia os endpoints da API Bling:
- GET /notificacoes — listar notificações (ObterMultiplos)
- GET /notificacoes/quantidade — obter quantidade (ObterMultiplos)
- POST /notificacoes/{idNotificacao}/confirmar-leitura — marcar como lida (Alterar)

Canonical methods are in pt-BR. English aliases available for compatibility.
"""

from __future__ import annotations

from bling_erp_api.models.generated.notificacoes import (
    NotificacoesGetResponse200,
    NotificacoesIdNotificacaoConfirmarLeituraPostResponse200,
    NotificacoesQuantidadeGetResponse200,
)
from bling_erp_api.resources.base import BaseResource
from bling_erp_api.utils.query import compact_params


class NotificacoesResource(BaseResource):
    """Notificações.

    Endpoints mapeados:
    - GET /notificacoes
    - GET /notificacoes/quantidade
    - POST /notificacoes/{idNotificacao}/confirmar-leitura

    Métodos canônicos em pt-BR.
    """

    def listar(
        self,
        *,
        periodo: str | None = None,
    ) -> NotificacoesGetResponse200:
        """Lista notificações.

        Endpoint: GET /notificacoes

        Lista todas as notificações de uma empresa em um período.

        Args:
            periodo: Ano ou ano-mês (ex: "2025-01") (Bling: ``periodo``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: NotificacoesDadosDTO[]; 400: ErrorResponse
        """
        params = compact_params({"periodo": periodo})
        raw = self._get("/notificacoes", params=params)
        return self._validate_response(NotificacoesGetResponse200, raw)

    def obter_quantidade(
        self,
        *,
        periodo: str | None = None,
    ) -> NotificacoesQuantidadeGetResponse200:
        """Obtém a quantidade de notificações.

        Endpoint: GET /notificacoes/quantidade

        Obtém a quantidade de notificações de uma empresa em um período.

        Args:
            periodo: Ano ou ano-mês (ex: "2025-01") (Bling: ``periodo``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: NotificacoesQuantidadeDTO; 400: ErrorResponse
        """
        params = compact_params({"periodo": periodo})
        raw = self._get("/notificacoes/quantidade", params=params)
        return self._validate_response(NotificacoesQuantidadeGetResponse200, raw)

    def confirmar_leitura(
        self,
        id_notificacao: str,
    ) -> NotificacoesIdNotificacaoConfirmarLeituraPostResponse200:
        """Marca notificação como lida.

        Endpoint: POST /notificacoes/{idNotificacao}/confirmar-leitura

        Marca uma notificação como lida pelo usuário.

        Args:
            id_notificacao: ULID da notificação (Bling: ``idNotificacao``, string, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: NotificacoesDadosDTO[]; 400: ErrorResponse
        """
        raw = self._post(f"/notificacoes/{id_notificacao}/confirmar-leitura")
        return self._validate_response(
            NotificacoesIdNotificacaoConfirmarLeituraPostResponse200, raw
        )

    def alterar(
        self,
        id_notificacao: str,
    ) -> NotificacoesIdNotificacaoConfirmarLeituraPostResponse200:
        """Deprecated compatibility alias for ``confirmar_leitura()``.

        Marca notificação como lida.

        Endpoint: POST /notificacoes/{idNotificacao}/confirmar-leitura

        Args:
            id_notificacao: ULID da notificação (Bling: ``idNotificacao``, string, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: NotificacoesDadosDTO[]; 400: ErrorResponse
        """
        return self.confirmar_leitura(id_notificacao=id_notificacao)

    # --- English aliases ---

    def list(
        self,
        *,
        period: str | None = None,
    ) -> NotificacoesGetResponse200:
        """Compatibility alias for ``listar()``.

        Lista notificações.

        Endpoint: GET /notificacoes

        Args:
            period: Ano ou ano-mês (ex: "2025-01") (Bling: ``periodo``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: NotificacoesDadosDTO[]; 400: ErrorResponse
        """
        return self.listar(periodo=period)

    def get_count(
        self,
        *,
        period: str | None = None,
    ) -> NotificacoesQuantidadeGetResponse200:
        """Compatibility alias for ``obter_quantidade()``.

        Obtém a quantidade de notificações.

        Endpoint: GET /notificacoes/quantidade

        Args:
            period: Ano ou ano-mês (ex: "2025-01") (Bling: ``periodo``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: NotificacoesQuantidadeDTO; 400: ErrorResponse
        """
        return self.obter_quantidade(periodo=period)

    def mark_as_read(
        self,
        notification_id: str,
    ) -> NotificacoesIdNotificacaoConfirmarLeituraPostResponse200:
        """Compatibility alias for ``confirmar_leitura()``.

        Marca notificação como lida.

        Endpoint: POST /notificacoes/{idNotificacao}/confirmar-leitura

        Args:
            notification_id: ULID da notificação (Bling: ``idNotificacao``, string, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: NotificacoesDadosDTO[]; 400: ErrorResponse
        """
        return self.confirmar_leitura(id_notificacao=notification_id)
