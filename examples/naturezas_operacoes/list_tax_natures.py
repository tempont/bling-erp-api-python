"""Exemplo: listar naturezas de operação."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.naturezas_operacoes import NaturezasOperacoesGetResponse200

client = BlingClient.from_env()
naturezas = client.naturezas_operacoes.listar(situacao=1, limite=10)
parsed = NaturezasOperacoesGetResponse200(**naturezas)  # type: ignore[reportArgumentType]
print(parsed.model_dump_json(indent=2, by_alias=True))
