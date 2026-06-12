"""Example: NFC-e (Consumer Invoice) Operations.

Demonstrates CRUD operations on NFC-e invoices through the Bling NFC-e API.

Endpoints:
    - GET /nfce
    - GET /nfce/{idNotaFiscalConsumidor}
    - POST /nfce
    - PUT /nfce/{idNotaFiscalConsumidor}
    - POST /nfce/{idNotaFiscalConsumidor}/enviar

Docs:
    - https://developer.bling.com.br/referencia#/NFC-e
"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

# Imports used at runtime for response model construction
from bling_erp_api.models.generated.invoices import (
    NfceGetResponse200,
    NfceIdNotaFiscalConsumidorGetResponse200,
)

if TYPE_CHECKING:
    from bling_erp_api.models.generated.invoices import (
        NfceIdNotaFiscalConsumidorEnviarPostResponse200,  # noqa: F401  # pyright: ignore[reportUnusedImport]
        NfceIdNotaFiscalConsumidorPutRequest,  # noqa: F401  # pyright: ignore[reportUnusedImport]
        NfceIdNotaFiscalConsumidorPutResponse200,  # noqa: F401  # pyright: ignore[reportUnusedImport]
        NfcePostRequest,  # noqa: F401  # pyright: ignore[reportUnusedImport]
        NfcePostResponse201,  # noqa: F401  # pyright: ignore[reportUnusedImport]
    )

## ---------------------------------------------------------------------------
## LIST NFC-E INVOICES
## ---------------------------------------------------------------------------


def listar_nfce(  # noqa: PLR0913
    *,
    pagina: int = 1,
    limite: int = 10,
    situacao: int | None = None,
    tipo: int | None = None,  # noqa: ARG001
    data_emissao_inicial: str | None = None,
    data_emissao_final: str | None = None,
) -> NfceGetResponse200:
    """Lista notas fiscais do consumidor (NFC-e).

    Endpoint: GET /nfce

    Obtém lista paginada de NFC-e.

    Args:
        pagina: N° da página (Bling: ``pagina``, integer, opcional)
        limite: Registros por página (Bling: ``limite``, integer, opcional)
        situacao: Situação (Bling: ``situacao``, integer, opcional)
        tipo: Tipo (Bling: ``tipo``, integer, opcional — usado apenas para NF-e)
        data_emissao_inicial: Data de emissão inicial (Bling: ``dataEmissaoInicial``, string, opcional)
        data_emissao_final: Data de emissão final (Bling: ``dataEmissaoFinal``, string, opcional)

    Returns:
        Bling API response. Response schemas: 200: NfceGetResponse200; 404: ErrorResponse
    """
    with BlingClient.from_env() as client:
        result = client.notas_fiscais_consumidor.listar(
            pagina=pagina,
            limite=limite,
            situacao=situacao,
            data_emissao_inicial=data_emissao_inicial,
            data_emissao_final=data_emissao_final,
        )
        return NfceGetResponse200(**result)  # type: ignore[reportArgumentType]


## ---------------------------------------------------------------------------
## GET A NFC-E BY ID
## ---------------------------------------------------------------------------


def obter_nfce(id_nota_fiscal: int) -> NfceIdNotaFiscalConsumidorGetResponse200:
    """Obtém uma NFC-e.

    Endpoint: GET /nfce/{idNotaFiscalConsumidor}

    Obtém uma nota fiscal do consumidor pelo ID.

    Args:
        id_nota_fiscal: ID da NFC-e (Bling: ``idNotaFiscalConsumidor``, integer, obrigatório)

    Returns:
        Bling API response. Response schemas: 200: NfceIdNotaFiscalConsumidorGetResponse200; 404: ErrorResponse
    """
    with BlingClient.from_env() as client:
        result = client.notas_fiscais_consumidor.obter(id_nota_fiscal_consumidor=id_nota_fiscal)
        return NfceIdNotaFiscalConsumidorGetResponse200(**result)  # type: ignore[reportArgumentType]


# ## ---------------------------------------------------------------------------
# ## CREATE A NFC-E
# ## ---------------------------------------------------------------------------
#
#
# def criar_nfce(dados: NfcePostRequest) -> NfcePostResponse201:
#     """Cria uma nova NFC-e.
#
#     Endpoint: POST /nfce
#
#     Cria uma nova nota fiscal do consumidor eletrônica.
#
#     Args:
#         dados: Dados da NFC-e (Bling: request body, NfcePostRequest)
#
#     Returns:
#         Bling API response. Response schemas: 201: NfcePostResponse201; 400: ErrorResponse
#     """
#     with BlingClient.from_env() as client:
#         result = client.notas_fiscais_consumidor.criar(dados=dados)
#         return NfcePostResponse201(**result)  # type: ignore[reportArgumentType]
#
#
# ## ---------------------------------------------------------------------------
# ## UPDATE A NFC-E (PUT)
# ## ---------------------------------------------------------------------------
#
#
# def alterar_nfce(
#     id_nota_fiscal: int,
#     dados: NfceIdNotaFiscalConsumidorPutRequest,
# ) -> NfceIdNotaFiscalConsumidorPutResponse200:
#     """Altera uma NFC-e.
#
#     Endpoint: PUT /nfce/{idNotaFiscalConsumidor}
#
#     Altera uma nota fiscal do consumidor pelo ID.
#
#     Args:
#         id_nota_fiscal: ID da NFC-e (Bling: ``idNotaFiscalConsumidor``, integer, obrigatório)
#         dados: Dados da NFC-e para atualização (Bling: request body, NfceIdNotaFiscalConsumidorPutRequest)
#
#     Returns:
#         Bling API response. Response schemas: 200: NfceIdNotaFiscalConsumidorPutResponse200; 400: ErrorResponse; 404: ErrorResponse
#     """
#     with BlingClient.from_env() as client:
#         result = client.notas_fiscais_consumidor.alterar(
#             id_nota_fiscal_consumidor=id_nota_fiscal,
#             dados=dados,
#         )
#         return NfceIdNotaFiscalConsumidorPutResponse200(**result)  # type: ignore[reportArgumentType]
#
#
# ## ---------------------------------------------------------------------------
# ## AUTHORIZE A NFC-E (SEND TO SEFAZ)
# ## ---------------------------------------------------------------------------
#
#
# def enviar_nfce(id_nota_fiscal: int) -> NfceIdNotaFiscalConsumidorEnviarPostResponse200:
#     """Envia uma NFC-e para autorização da SEFAZ.
#
#     Endpoint: POST /nfce/{idNotaFiscalConsumidor}/enviar
#
#     Envia uma NFC-e para autorização da SEFAZ.
#
#     Args:
#         id_nota_fiscal: ID da NFC-e (Bling: ``idNotaFiscalConsumidor``, integer, obrigatório)
#
#     Returns:
#         Bling API response. Response schemas: 200: NfceIdNotaFiscalConsumidorEnviarPostResponse200; 400: ErrorResponse; 404: ErrorResponse
#     """
#     with BlingClient.from_env() as client:
#         result = client.notas_fiscais_consumidor.autorizar(
#             id_nota_fiscal_consumidor=id_nota_fiscal
#         )
#         return NfceIdNotaFiscalConsumidorEnviarPostResponse200(**result)  # type: ignore[reportArgumentType]


def main() -> None:
    """Demonstrate NFC-e operations."""
    id_nota_fiscal = 12345  # noqa: F841  # pyright: ignore[reportUnusedVariable]  # Exemplo — substitua pelo ID real.

    # Read operations
    print(listar_nfce(pagina=1, limite=5).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    # print(obter_nfce(id_nota_fiscal).model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)

    # Write operations (commented out)
    # payload = NfcePostRequest(
    #     tipo=1,
    #     contato={"nome": "Consumidor"},
    # )
    # print(criar_nfce(payload).model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)
    # update_payload = NfceIdNotaFiscalConsumidorPutRequest(
    #     tipo=1,
    #     contato={"nome": "Consumidor"},
    # )
    # print(alterar_nfce(id_nota_fiscal, update_payload).model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)
    # print(enviar_nfce(id_nota_fiscal).model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
