"""Exemplo: obter regras de tributação."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.naturezas_operacoes import (
    CalculosImpostosCalculoDTO,
    NaturezasOperacoesIdNaturezaOperacaoObterTributacaoPostResponse200,
)

client = BlingClient.from_env()
tributacao = client.naturezas_operacoes.obter_tributacao(
    id_natureza_operacao=12345678,
    calculo=CalculosImpostosCalculoDTO.model_construct(
        tipoNota=1,
        uf="RS",
        municipio={"id": 4302105},
        loja={"id": 12345678},
        produto={
            "id": 98765,
            "valorUnitario": 100.0,
            "cupomFiscal": 0,
            "origem": 0,
            "quantidade": 1.0,
        },
    ).model_dump(by_alias=True),
)
tributacao_parsed = NaturezasOperacoesIdNaturezaOperacaoObterTributacaoPostResponse200(**tributacao)  # type: ignore[reportArgumentType]
print(tributacao_parsed.model_dump_json(indent=2, by_alias=True))
