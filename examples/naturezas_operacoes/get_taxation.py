"""Exemplo: obter regras de tributação."""

from bling_erp_api import BlingClient

client = BlingClient.from_env()
tributacao = client.naturezas_operacoes.obter_tributacao(
    id_natureza_operacao=12345678,
    calculo={
        "tipoNota": 1,
        "uf": "RS",
        "municipio": {"id": 4302105},
        "loja": {"id": 12345678},
        "produto": {
            "id": 98765,
            "valorUnitario": 100.0,
            "cupomFiscal": 0,
            "origem": 0,
            "quantidade": 1.0,
        },
    },
)
print(tributacao)
