"""Example: NFS-e (Nota Fiscal de Serviço Eletrônica) workflow.

Demonstrates listing, creating, retrieving, authorizing, and canceling NFS-e invoices,
plus managing NFS-e configuration.

Usage:
    BLING_API_KEY="your_key" python examples/invoices/nfse_example.py
"""

from bling_erp_api import BlingClient


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
    print(f"Found NFS-e invoices: {result}")

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

    # 3. Get a specific NFS-e
    # invoice = nfse.obter(111)
    # print(f"NFS-e details: {invoice}")

    # 4. Authorize (send) NFS-e
    # nfse.autorizar(111)

    # 5. Cancel NFS-e
    # cancel_data = {
    #     "codigoMotivo": 1,  # 1 = Erro na emissão
    #     "justificativa": "Incorrect service value",
    # }
    # nfse.cancelar(111, cancel_data)

    # 6. Get NFS-e configuration
    print("Getting NFS-e configuration...")
    config = nfse.obter_configuracoes()
    print(f"Current configuration: {config}")

    # 7. Update NFS-e configuration
    # new_config = {
    #     "basicas": {"emissorPadrao": 1, "naturezaOperacao": 2},
    #     "ISS": {"zerar": False, "reter": True, "descontar": False},
    # }
    # nfse.alterar_configuracoes(new_config)

    # 8. Delete NFS-e
    # nfse.remover(111)


if __name__ == "__main__":
    main()
