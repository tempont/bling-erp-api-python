"""Example: Notifications (Notificações) Workflow Examples.

Demonstrates listing, counting, and marking notifications as read through the Bling API.

Endpoints:
    - GET /notificacoes
    - GET /notificacoes/quantidade
    - POST /notificacoes/{idNotificacao}/confirmar-leitura

Docs:
    - https://developer.bling.com.br/referencia#/Notifica%C3%A7%C3%B5es/get_notificacoes
    - https://developer.bling.com.br/referencia#/Notifica%C3%A7%C3%B5es/get_notificacoes_quantidade
    - https://developer.bling.com.br/referencia#/Notifica%C3%A7%C3%B5es/post_notificacoes__idNotificacao__confirmar_leitura

"""

from __future__ import annotations

import time

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.notificacoes import (
    NotificacoesGetResponse200,
    NotificacoesIdNotificacaoConfirmarLeituraPostResponse200,
    NotificacoesQuantidadeGetResponse200,
)

## ---------------------------------------------------------------------------
## LIST NOTIFICATIONS
## ---------------------------------------------------------------------------


def list_notifications(period: str | None = None) -> NotificacoesGetResponse200:
    """List notifications, optionally filtered by period (YYYY-MM)."""
    with BlingClient.from_env() as client:
        response = client.notificacoes.listar(periodo=period)
    return NotificacoesGetResponse200.model_validate(response)


## ---------------------------------------------------------------------------
## GET NOTIFICATION COUNT
## ---------------------------------------------------------------------------


def get_notification_count(period: str | None = None) -> NotificacoesQuantidadeGetResponse200:
    """Get the count of notifications in a period (YYYY-MM)."""
    with BlingClient.from_env() as client:
        response = client.notificacoes.obter_quantidade(periodo=period)
    return NotificacoesQuantidadeGetResponse200.model_validate(response)


## ---------------------------------------------------------------------------
## MARK NOTIFICATION AS READ
## ---------------------------------------------------------------------------


def mark_notification_as_read(
    notification_id: str,
) -> NotificacoesIdNotificacaoConfirmarLeituraPostResponse200:
    """Mark a notification as read by its ULID."""
    with BlingClient.from_env() as client:
        response = client.notificacoes.confirmar_leitura(id_notificacao=notification_id)
    return NotificacoesIdNotificacaoConfirmarLeituraPostResponse200.model_validate(response)


def main() -> None:
    """Demonstrate notification operations."""
    notification_id = "01ARZ3NDEKTSV4RRFFQ69G5FAV"  # Exemplo — substitua pelo ULID real.

    # List notifications
    print("=== List notifications ===")
    response = list_notifications(period="2025-01")
    print(response.model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    # Get count
    print("=== Get notification count ===")
    response = get_notification_count(period="2025")
    print(response.model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    # Mark as read
    print("=== Mark notification as read ===")
    response = mark_notification_as_read(notification_id)
    print(response.model_dump_json(indent=2, by_alias=True))
    time.sleep(1)


if __name__ == "__main__":
    main()
