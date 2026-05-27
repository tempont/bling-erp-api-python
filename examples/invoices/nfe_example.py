"""Example: NF-e (Nota Fiscal Eletrônica) workflow.

Demonstrates listing, creating, retrieving, and authorizing NF-e invoices.

Usage:
    BLING_API_KEY="your_key" python examples/invoices/nfe_example.py
"""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.invoices import NfeGetResponse200


def main() -> None:
    """Run the NF-e example workflow."""
    client = BlingClient.from_env()

    # Access the NF-e resource (pt-BR canonical name)
    nfe = client.notas_fiscais
    # Or use the English alias: client.invoices

    # 1. List NF-e invoices with filters
    print("Listing NF-e invoices...")
    result = nfe.listar(
        pagina=1,
        limite=10,
        situacao=3,  # 3 = Autorizada
        data_emissao_inicial="2024-01-01",
        data_emissao_final="2024-12-31",
    )
    parsed = NfeGetResponse200(**result)  # type: ignore[reportArgumentType]
    print(parsed.model_dump_json(indent=2, by_alias=True))

    # NOTE: Uncomment and replace raw dict with NfePostRequest(...) for typed payload construction.
    # 2. Create a new NF-e (requires valid contact, items, etc.)
    # nfe_data = {
    #     "tipo": 1,  # 1 = Saída
    #     "numero": "123",
    #     "dataOperacao": "2024-06-01",
    #     "contato": {"id": 123},
    #     "naturezaOperacao": {"id": 1},
    #     "loja": {"id": 1},
    #     "finalidade": 1,
    #     "itens": [
    #         {
    #             "codigo": "PROD-001",
    #             "descricao": "Product description",
    #             "unidade": "UN",
    #             "quantidade": 1,
    #             "valor": 100.00,
    #             "tipo": "P",
    #             "origem": 0,
    #         }
    #     ],
    #     "parcelas": [
    #         {"data": "2024-07-01", "valor": 100.00, "formaPagamento": {"id": 1}}
    #     ],
    # }
    # created = nfe.criar(nfe_data)
    # print(f"Created NF-e: {created}")

    # 3. Get a specific NF-e by ID
    # invoice = nfe.obter(12345)
    # print(f"Invoice details: {invoice}")

    # 4. Authorize (send to SEFAZ) an NF-e
    # nfe.autorizar(12345, enviar_email=True)

    # 5. Get NF-e document (XML/PDF) by access key
    # doc = nfe.obter_documento_nota_fiscal(
    #     "35240112345678901234567890123456789012345678",
    #     formato="pdf",
    # )
    # print(f"Document: {doc}")

    # 6. Stock management
    # nfe.lancar_estoque(12345)           # Post stock for all warehouses
    # nfe.lancar_estoque(12345, id_deposito=1)  # Post stock for specific warehouse
    # nfe.estornar_estoque(12345)         # Reverse stock

    # 7. Account management
    # nfe.lancar_contas(12345)           # Post accounts
    # nfe.estornar_contas(12345)         # Reverse accounts

    # 8. Delete multiple invoices
    # nfe.remover_varios([1, 2, 3])


if __name__ == "__main__":
    main()
