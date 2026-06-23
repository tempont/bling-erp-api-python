"""Example: NFS-e (Service Invoice) Operations.

Demonstrates listing, retrieving, and configuring NFS-e through the Bling
service invoice API.

Endpoints:
    - GET /nfse
    - GET /nfse/{idNotaServico}
    - POST /nfse
    - POST /nfse/{idNotaServico}/enviar
    - GET /nfse/configuracoes

Docs:
    - https://developer.bling.com.br/referencia#/NFS-e
"""

from __future__ import annotations

import json
import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.nfse import NfsePostRequest, NfsePostResponse201
    from bling_erp_api.types import JsonObject

## ---------------------------------------------------------------------------
## LIST NFS-E INVOICES
## ---------------------------------------------------------------------------


def listar_nfse(
    *,
    pagina: int = 1,
    limite: int = 10,
    situacao: int | None = None,
    data_emissao_inicial: str | None = None,
    data_emissao_final: str | None = None,
) -> JsonObject:
    """Lista notas fiscais de serviço (NFS-e)."""
    with BlingClient.from_env() as client:
        return client.notas_servicos.listar(
            pagina=pagina,
            limite=limite,
            situacao=situacao,
            data_emissao_inicial=data_emissao_inicial,
            data_emissao_final=data_emissao_final,
        )


## ---------------------------------------------------------------------------
## GET AN NFS-E INVOICE BY ID
## ---------------------------------------------------------------------------


def obter_nfse(id_nota_servico: int) -> JsonObject:
    """Obtém uma NFS-e pelo ID."""
    with BlingClient.from_env() as client:
        return client.notas_servicos.obter(id_nota_servico=id_nota_servico)


## ---------------------------------------------------------------------------
## GET NFS-E CONFIGURATION
## ---------------------------------------------------------------------------


def obter_configuracoes() -> JsonObject:
    """Obtém as configurações de NFS-e."""
    with BlingClient.from_env() as client:
        return client.notas_servicos.obter_configuracoes()


## ---------------------------------------------------------------------------
## CREATE AN NFS-E INVOICE
## ---------------------------------------------------------------------------


def criar_nfse(dados: NfsePostRequest) -> NfsePostResponse201:
    """Cria uma nova NFS-e."""
    with BlingClient.from_env() as client:
        return client.notas_servicos.criar(dados=dados)


## ---------------------------------------------------------------------------
## AUTHORIZE (SEND) AN NFS-E INVOICE
## ---------------------------------------------------------------------------


def enviar_nfse(id_nota_servico: int) -> JsonObject:
    """Autoriza (envia) uma NFS-e."""
    with BlingClient.from_env() as client:
        return client.notas_servicos.autorizar(id_nota_servico=id_nota_servico)


def main() -> None:
    """Demonstrate NFS-e operations."""
    # Read operations
    print(json.dumps(listar_nfse(pagina=1, limite=5), indent=2, ensure_ascii=False))
    time.sleep(1)

    nfse_id = 123456789  # Exemplo — substitua pelo ID real.
    print(json.dumps(obter_nfse(id_nota_servico=nfse_id), indent=2, ensure_ascii=False))
    time.sleep(1)

    print(json.dumps(obter_configuracoes(), indent=2, ensure_ascii=False))
    time.sleep(1)

    # Write operations (commented out)
    # payload = NfsePostRequest(...)
    # print(json.dumps(criar_nfse(payload), indent=2, ensure_ascii=False))
    # time.sleep(1)
    # print(json.dumps(enviar_nfse(nfse_id), indent=2, ensure_ascii=False))
    # time.sleep(1)


if __name__ == "__main__":
    main()
