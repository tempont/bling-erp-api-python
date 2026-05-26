"""Example: NFC-e (Nota Fiscal do Consumidor Eletrônica) workflow.

Demonstrates listing, creating, retrieving, and authorizing NFC-e invoices.

Usage:
    BLING_API_KEY="your_key" python examples/invoices/nfce_example.py
"""

from bling_erp_api import BlingClient


def main() -> None:
    """Run the NFC-e example workflow."""
    client = BlingClient.from_env()

    # Access the NFC-e resource
    nfce = client.notas_fiscais_consumidor
    # Or use the English alias: client.consumer_invoices

    # 1. List NFC-e invoices with filters
    print("Listing NFC-e invoices...")
    result = nfce.listar(
        pagina=1,
        limite=10,
        situacao=3,  # 3 = Autorizada
        data_emissao_inicial="2024-01-01",
        data_emissao_final="2024-12-31",
    )
    print(f"Found NFC-e invoices: {result}")

    # 2. Create a new NFC-e
    # nfce_data = {
    #     "tipo": 1,
    #     "numero": "456",
    #     "dataOperacao": "2024-06-01",
    #     "contato": {"nome": "Consumer Name", "tipoPessoa": "F", "numeroDocumento": "12345678901", "contribuinte": 9},
    #     "naturezaOperacao": {"id": 2},
    #     "loja": {"id": 1},
    #     "finalidade": 1,
    #     "itens": [
    #         {"codigo": "PROD-002", "descricao": "Retail product", "unidade": "UN", "quantidade": 1, "valor": 50.00, "tipo": "P", "origem": 0}
    #     ],
    #     "parcelas": [
    #         {"data": "2024-06-01", "valor": 50.00, "formaPagamento": {"id": 1}}
    #     ],
    # }
    # created = nfce.criar(nfce_data)
    # print(f"Created NFC-e: {created}")

    # 3. Get a specific NFC-e
    # invoice = nfce.obter(54321)
    # print(f"NFC-e details: {invoice}")

    # 4. Authorize NFC-e
    # nfce.autorizar(54321, enviar_email=True)

    # 5. Stock and account actions (same pattern as NF-e)
    # nfce.lancar_estoque(54321)
    # nfce.estornar_estoque(54321)
    # nfce.lancar_contas(54321)
    # nfce.estornar_contas(54321)


if __name__ == "__main__":
    main()
