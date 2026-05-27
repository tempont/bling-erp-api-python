"""Example: NFS-e (Nota Fiscal de Serviço Eletrônica) workflow.

Demonstrates listing, creating, retrieving, authorizing, and canceling NFS-e invoices,
plus managing NFS-e configuration.

Usage:
    BLING_API_KEY="your_key" python examples/invoices/nfse_example.py
"""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.nfse import (
    ConfiguracaoNotaServicoDadosBaseDTO,
    NfseGetResponse200,
)


def main() -> None:
    """Run the NFS-e example workflow."""
    client = BlingClient.from_env()

    # Access the NFS-e resource
    nfse = client.notas_servicos
    # Or use the English alias: client.service_invoices

    # 1. List NFS-e invoices
    print("Listing NFS-e invoices...")
    result = nfse.listar(
        pagina=1,
        limite=10,
        situacao=3,  # 3 = Autorizada
        data_emissao_inicial="2024-01-01",
        data_emissao_final="2024-12-31",
    )
    parsed = NfseGetResponse200(**result)  # type: ignore[reportArgumentType]
    print(parsed.model_dump_json(indent=2, by_alias=True))

    # NOTE: Uncomment and replace raw dict with NfsePostRequest(...) for typed payload construction.
    # 2. Create a new NFS-e
    # nfse_data = {
    #     "numero": "111",
    #     "numeroRPS": "RPS-001",
    #     "serie": "1",
    #     "contato": {
    #         "nome": "Service Client Ltda",
    #         "numeroDocumento": "98765432000111",
    #         "email": "client@example.com",
    #         "ie": "123456789",
    #         "telefone": "1133334444",
    #         "endereco": {
    #             "endereco": "Av Principal",
    #             "numero": "1000",
    #             "bairro": "Centro",
    #             "municipio": "São Paulo",
    #             "uf": "SP",
    #         },
    #     },
    #     "data": "2024-06-01",
    #     "servicos": [
    #         {"codigo": "SERV-001", "descricao": "IT Consulting", "valor": 5000.00}
    #     ],
    #     "parcelas": [
    #         {"data": "2024-07-01", "valor": 5000.00, "formaPagamento": {"id": 1}}
    #     ],
    # }
    # created = nfse.criar(nfse_data)
    # print(f"Created NFS-e: {created}")

    # NOTE: Uncomment and parse response with NfseIdNotaServicoGetResponse200 for typed output.
    # 3. Get a specific NFS-e
    # invoice = nfse.obter(111)
    # print(f"NFS-e details: {invoice}")

    # NOTE: Uncomment and use typed model for typed payload construction.
    # 4. Authorize (send) NFS-e
    # nfse.autorizar(111)

    # NOTE: Uncomment and use NotasServicosCancelamentoDTO for typed payload construction.
    # 5. Cancel NFS-e
    # cancel_data = {
    #     "codigoMotivo": 1,  # 1 = Erro na emissão
    #     "justificativa": "Incorrect service value",
    # }
    # nfse.cancelar(111, cancel_data)

    # 6. Get NFS-e configuration
    print("Getting NFS-e configuration...")
    config = nfse.obter_configuracoes()
    parsed_config = ConfiguracaoNotaServicoDadosBaseDTO(**config)  # type: ignore[reportArgumentType]
    print(parsed_config.model_dump_json(indent=2, by_alias=True))

    # NOTE: Uncomment and use appropriate config model for typed payload construction.
    # 7. Update NFS-e configuration
    # new_config = {
    #     "basicas": {"emissorPadrao": 1, "naturezaOperacao": 2},
    #     "ISS": {"zerar": False, "reter": True, "descontar": False},
    # }
    # nfse.alterar_configuracoes(new_config)

    # NOTE: Uncomment for typed payload handling.
    # 8. Delete NFS-e
    # nfse.remover(111)


if __name__ == "__main__":
    main()
