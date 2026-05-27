"""Resource para Notificações.

Mapeia os endpoints da API Bling:
- GET /notificacoes — listar notificações (ObterMultiplos)
- GET /notificacoes/quantidade — obter quantidade (ObterMultiplos)
- POST /notificacoes/{idNotificacao}/confirmar-leitura — marcar como lida (Alterar)

Canonical methods are in pt-BR. English aliases available for compatibility.
"""

from bling_erp_api.resources.base import BaseResource
from bling_erp_api.types import JsonObject
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
    ) -> JsonObject:
        """Lista notificações.

        Endpoint: GET /notificacoes

        Lista todas as notificações de uma empresa em um período.

        Args:
            periodo: Ano ou ano-mês (ex: "2025-01") (Bling: ``periodo``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: NotificacoesDadosDTO[]; 400: ErrorResponse
        """
        params = compact_params({"periodo": periodo})
        return self._get("/notificacoes", params=params)

    def obter_quantidade(
        self,
        *,
        periodo: str | None = None,
    ) -> JsonObject:
        """Obtém a quantidade de notificações.

        Endpoint: GET /notificacoes/quantidade

        Obtém a quantidade de notificações de uma empresa em um período.

        Args:
            periodo: Ano ou ano-mês (ex: "2025-01") (Bling: ``periodo``, string, opcional)

        Returns:
            Bling API response. Response schemas: 200: NotificacoesQuantidadeDTO; 400: ErrorResponse
        """
        params = compact_params({"periodo": periodo})
        return self._get("/notificacoes/quantidade", params=params)

    def alterar(
        self,
        id_notificacao: str,
    ) -> JsonObject:
        """Marca notificação como lida.

        Endpoint: POST /notificacoes/{idNotificacao}/confirmar-leitura

        Marca uma notificação como lida pelo usuário.

        Args:
            id_notificacao: ULID da notificação (Bling: ``idNotificacao``, string, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: NotificacoesDadosDTO[]; 400: ErrorResponse
        """
        return self._post(f"/notificacoes/{id_notificacao}/confirmar-leitura")

    # --- English aliases ---

    def list(
        self,
        *,
        period: str | None = None,
    ) -> JsonObject:
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
    ) -> JsonObject:
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
    ) -> JsonObject:
        """Compatibility alias for ``alterar()``.

        Marca notificação como lida.

        Endpoint: POST /notificacoes/{idNotificacao}/confirmar-leitura

        Args:
            notification_id: ULID da notificação (Bling: ``idNotificacao``, string, obrigatório)

        Returns:
            Bling API response. Response schemas: 200: NotificacoesDadosDTO[]; 400: ErrorResponse
        """
        return self.alterar(id_notificacao=notification_id)
