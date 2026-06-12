"""Example: NF-e (Nota Fiscal Eletrônica) Operations.

Demonstrates listing, retrieving, and other NF-e operations.

Endpoints:
    - GET /nfe
    - GET /nfe/{idNotaFiscal}
    - POST /nfe
    - PUT /nfe/{idNotaFiscal}
    - POST /nfe/{idNotaFiscal}/enviar
    - GET /nfe/documento/{chaveAcesso}

Docs:
    - https://developer.bling.com.br/referencia#/NF-e

"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.invoices import (
        NfeDocumentoChaveAcessoGetResponse200,
        NfeGetResponse200,
        NfeIdNotaFiscalEnviarPostResponse200,
        NfeIdNotaFiscalGetResponse200,
        NfeIdNotaFiscalPutRequest,
        NfeIdNotaFiscalPutResponse200,
        NfePostRequest,
        NfePostResponse201,
    )

## ---------------------------------------------------------------------------
## LIST NF-e
## ---------------------------------------------------------------------------


def listar_notas(  # noqa: PLR0913
    *,
    pagina: int = 1,
    limite: int = 10,
    situacao: int | None = None,
    tipo: int | None = None,
    data_emissao_inicial: str | None = None,
    data_emissao_final: str | None = None,
) -> NfeGetResponse200:
    """Lista NF-e.

    Endpoint: GET /nfe

    Obtém lista paginada de NF-e com filtros opcionais.

    Args:
        pagina: Número da página (Bling: pagina, integer, opcional)
        limite: Registros por página (Bling: limite, integer, opcional)
        situacao: Situação da NF-e (Bling: situacao, integer, opcional)
        tipo: Tipo da NF-e (Bling: tipo, integer, opcional)
        data_emissao_inicial: Data de emissão inicial (Bling: dataEmissaoInicial, string, opcional)
        data_emissao_final: Data de emissão final (Bling: dataEmissaoFinal, string, opcional)

    Returns:
        Bling API response. Response schemas: 200: NfeGetResponse200; 404: ErrorResponse
    """
    with BlingClient.from_env() as client:
        return client.notas_fiscais.listar(
            pagina=pagina,
            limite=limite,
            situacao=situacao,
            tipo=tipo,
            data_emissao_inicial=data_emissao_inicial,
            data_emissao_final=data_emissao_final,
        )


## ---------------------------------------------------------------------------
## GET A NF-e BY ID
## ---------------------------------------------------------------------------


def obter_nota(id_nota_fiscal: int) -> NfeIdNotaFiscalGetResponse200:
    """Obtém uma NF-e pelo ID.

    Endpoint: GET /nfe/{idNotaFiscal}

    Obtém uma nota fiscal eletrônica pelo ID.

    Args:
        id_nota_fiscal: ID da nota fiscal (Bling: idNotaFiscal, integer, obrigatório)

    Returns:
        Bling API response. Response schemas: 200: NfeIdNotaFiscalGetResponse200; 404: ErrorResponse
    """
    with BlingClient.from_env() as client:
        return client.notas_fiscais.obter(id_nota_fiscal=id_nota_fiscal)


## ---------------------------------------------------------------------------
## CREATE A NF-e  (commented out to avoid side effects)
## ---------------------------------------------------------------------------


def criar_nota(dados: NfePostRequest) -> NfePostResponse201:
    """Cria uma NF-e.

    Endpoint: POST /nfe

    Cria uma nova nota fiscal eletrônica.

    Args:
        dados: Dados da NF-e (Bling: JsonObject, obrigatório)

    Returns:
        Bling API response. Response schemas: 201: NfePostResponse201; 400: ErrorResponse
    """
    with BlingClient.from_env() as client:
        return client.notas_fiscais.criar(dados=dados)


## ---------------------------------------------------------------------------
## UPDATE A NF-e (PUT)  (commented out to avoid side effects)
## ---------------------------------------------------------------------------


def alterar_nota(
    id_nota_fiscal: int, dados: NfeIdNotaFiscalPutRequest
) -> NfeIdNotaFiscalPutResponse200:
    """Altera uma NF-e.

    Endpoint: PUT /nfe/{idNotaFiscal}

    Altera uma nota fiscal eletrônica pelo ID.

    Args:
        id_nota_fiscal: ID da nota fiscal (Bling: idNotaFiscal, integer, obrigatório)
        dados: Dados da NF-e para atualização (Bling: JsonObject, obrigatório)

    Returns:
        Bling API response. Response schemas: 200: NfeIdNotaFiscalPutResponse200; 400: ErrorResponse; 404: ErrorResponse
    """
    with BlingClient.from_env() as client:
        return client.notas_fiscais.alterar(id_nota_fiscal=id_nota_fiscal, dados=dados)


## ---------------------------------------------------------------------------
## AUTHORIZE (SEND TO SEFAZ) A NF-e  (commented out to avoid side effects)
## ---------------------------------------------------------------------------


def autorizar_nota(id_nota_fiscal: int) -> NfeIdNotaFiscalEnviarPostResponse200:
    """Autoriza (envia para a SEFAZ) uma NF-e.

    Endpoint: POST /nfe/{idNotaFiscal}/enviar

    Envia uma NF-e para autorização da SEFAZ.

    Args:
        id_nota_fiscal: ID da nota fiscal (Bling: idNotaFiscal, integer, obrigatório)

    Returns:
        Bling API response. Response schemas: 200: NfeIdNotaFiscalEnviarPostResponse200; 400: ErrorResponse; 404: ErrorResponse
    """
    with BlingClient.from_env() as client:
        return client.notas_fiscais.autorizar(id_nota_fiscal=id_nota_fiscal)


## ---------------------------------------------------------------------------
## GET NF-e DOCUMENT BY ACCESS KEY  (commented out to avoid side effects)
## ---------------------------------------------------------------------------


def obter_documento(chave_acesso: str) -> NfeDocumentoChaveAcessoGetResponse200:
    """Obtém o documento (XML/DANFE) de uma NF-e.

    Endpoint: GET /nfe/documento/{chaveAcesso}

    Obtém o documento de uma NF-e pela chave de acesso.

    Args:
        chave_acesso: Chave de acesso da NF-e (Bling: chaveAcesso, string, obrigatório)

    Returns:
        Bling API response. Response schemas: 200: NfeDocumentoChaveAcessoGetResponse200; 400: ErrorResponse; 404: ErrorResponse
    """
    with BlingClient.from_env() as client:
        return client.notas_fiscais.obter_documento_nota_fiscal(chave_acesso=chave_acesso)


def main() -> None:
    """Demonstrate NF-e operations."""
    # Read operations
    print(listar_notas(pagina=1, limite=5).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    print(obter_nota(id_nota_fiscal=12345).model_dump_json(indent=2, by_alias=True))
    time.sleep(1)

    # Write operations (commented out to avoid side effects)
    # payload = NfePostRequest(
    #     tipo=1,
    #     numero="123",
    #     data_operacao="2024-06-01",
    #     contato=NotasFiscaisContatoDTO(id=123),
    #     natureza_operacao=NotasFiscaisNaturezaOperacaoDTO(id=1),
    #     loja=NotasFiscaisLojaDTO(id=1),
    #     finalidade=1,
    #     itens=[
    #         NotasFiscaisItemDTO(
    #             codigo="PROD-001",
    #             descricao="Product description",
    #             unidade="UN",
    #             quantidade=1,
    #             valor=100.00,
    #             tipo="P",
    #             origem=0,
    #         ),
    #     ],
    #     parcelas=[
    #         NotasFiscaisParcelaDTO(
    #             data="2024-07-01", valor=100.00, forma_pagamento={"id": 1}
    #         ),
    #     ],
    # )
    # print(criar_nota(payload).model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)
    # update_payload = NfeIdNotaFiscalPutRequest(
    #     tipo=1,
    #     numero="123",
    #     data_operacao="2024-06-01",
    #     contato=NotasFiscaisContatoDTO(id=123),
    #     natureza_operacao=NotasFiscaisNaturezaOperacaoDTO(id=1),
    #     loja=NotasFiscaisLojaDTO(id=1),
    #     finalidade=1,
    # )
    # print(alterar_nota(12345, update_payload).model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)
    # print(autorizar_nota(12345).model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)
    # print(obter_documento("35240112345678901234567890123456789012345678").model_dump_json(indent=2, by_alias=True))
    # time.sleep(1)


if __name__ == "__main__":
    main()
