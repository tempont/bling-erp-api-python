"""Exemplo: obter regras de tributação."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.naturezas_operacoes import (
    CalculosImpostosCalculoDTO,
    NaturezasOperacoesIdNaturezaOperacaoObterTributacaoPostResponse200,
)
from bling_erp_api.models.generated.schemas.calculos_impostos import (
    CalculosImpostosLojaDTO,
    CalculosImpostosMunicipioDTO,
    CalculosImpostosProdutoDTO,
)

client = BlingClient.from_env()
tributacao = client.naturezas_operacoes.obter_tributacao(
    id_natureza_operacao=12345678,
    # Model: CalculosImpostosCalculoDTO
    #   Required: tipo_nota (int), uf (str), municipio (CalculosImpostosMunicipioDTO),
    #             loja (CalculosImpostosLojaDTO), produto (CalculosImpostosProdutoDTO)
    #   Optional: obter_regras (bool|None), crt (int|None)
    calculo=CalculosImpostosCalculoDTO(
        tipo_nota=1,
        uf="RS",
        municipio=CalculosImpostosMunicipioDTO(id=4302105),
        loja=CalculosImpostosLojaDTO(id=12345678),
        produto=CalculosImpostosProdutoDTO(
            id=98765,
            valor_unitario=100.0,
            cupom_fiscal=0,
            origem=0,
            quantidade=1.0,
        ),
    ).model_dump(by_alias=True),
)
tributacao_parsed = NaturezasOperacoesIdNaturezaOperacaoObterTributacaoPostResponse200(**tributacao)  # type: ignore[reportArgumentType]
print(tributacao_parsed.model_dump_json(indent=2, by_alias=True))
