"""Example: Get Consumer Contact.

Demonstrates how to retrieve the default "Consumidor Final" contact.

Endpoint:
    - GET /contatos/consumidor-final

Docs:
    - https://developer.bling.com.br/referencia#/Contatos/get_contatos_consumidor_final

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.contacts import (
        ContatosConsumidorFinalGetResponse200,
    )


def obter_consumidor_final() -> ContatosConsumidorFinalGetResponse200:
    """Obtém o contato Consumidor Final pré-definido."""
    with BlingClient.from_env() as client:
        return client.contatos.obter_consumidor_final()


def main() -> None:
    """Demonstrate getting the consumer contact."""
    result = obter_consumidor_final()
    print(result.model_dump_json(indent=2, by_alias=True))
    time.sleep(1)


if __name__ == "__main__":
    main()
