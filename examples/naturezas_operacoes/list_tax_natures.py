"""Exemplo: listar naturezas de operação."""

from bling_erp_api import BlingClient

client = BlingClient.from_env()
naturezas = client.naturezas_operacoes.listar(situacao=1, limite=10)
print(naturezas)
