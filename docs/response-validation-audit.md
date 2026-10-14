# Auditoria de validação de respostas — 2026-10-07

Esta investigação partiu da falha de `GET /logisticas/objetos/{idObjeto}` no
SDK 0.3.1: o Bling envia `rastreamento.ultimaAlteracao` sem offset, enquanto
o modelo gerado exigia `AwareDatetime`.

## Problemas confirmados e correções

| Problema | Evidência | Correção |
| --- | --- | --- |
| Timestamp sem fuso rejeitado | Reprodução com `2026-10-07 11:24:02`; o próprio OpenAPI contém exemplo sem offset | `BlingDatetime` interpreta valores sem fuso como `America/Sao_Paulo` e preserva offsets explícitos |
| Mesmo problema em remessas | `LogisticasRemessasRastreamentoDTO.ultimaAlteracao` também era `AwareDatetime` | Mesmo tipo aplicado pelo gerador; teste de leitura com rastreamento dentro de `objetos[]` |
| Data zerada rejeitada | Cinco objetos reais apresentaram sentinela de data zerada durante a investigação | Sentinelas de ausência viram `None`; datas malformadas comuns continuam falhando |

O tipo usa as regras IANA de São Paulo, incluindo o horário de verão histórico.
A dependência `tzdata` permite a mesma interpretação em sistemas sem base de
fusos. As chaves obrigatórias, os aliases e a proteção contra valores
conflitantes continuam sendo validados.

## Varredura dos modelos e do OpenAPI

- Os dois campos acima eram os únicos campos gerados com `AwareDatetime`.
- Há 52 propriedades com formato `date` nos componentes do OpenAPI. Seus
  exemplos passaram pelo parser `BlingDate`, que já trata datas zeradas.
- Quatro propriedades usam o formato não padronizado `datetime`:
  `NotasFiscaisDadosBaseDTO.dataEmissao`, `dataOperacao` e
  `NotificacoesDadosBaseDTO.dataEnvio`, `dataLeitura`. O gerador as mantém como
  texto; elas não exigem timezone e não foram convertidas nesta correção.
- Um teste percorre os exemplos `date-time` do OpenAPI e os valida com os
  campos dos modelos gerados, para detectar novamente uma incompatibilidade
  entre o exemplo oficial e o parser.

## Amostragem real, somente leitura

As consultas usaram `doppler run --project bling-sdk --config dev` e o
transporte do SDK com `rate_limit_max_requests=1` e
`rate_limit_period_seconds=2.1`. O limitador permaneceu habilitado, inclusive
para retries. Os relatórios exibiram somente rotas sem IDs, tipos e locais
de erros e resultados de validação. Payloads, identificadores, valores
financeiros e credenciais não foram salvos. As fixtures são sintéticas.

| Recurso | Resultado observado |
| --- | --- |
| Pedidos de venda, listagem e detalhe | Validação e serialização passaram |
| Produtos, listagem e detalhe | Validação e serialização passaram |
| Contatos, listagem e detalhe | Validação e serialização passaram |
| NF-e, listagem e detalhe | Validação e serialização passaram |
| Contas a pagar e a receber, listagem e detalhe | Validação e serialização passaram |
| Logísticas, listagem | Validação e serialização passaram |
| Objetos de logística | Oito leituras pelo método público passaram após as duas correções, com timestamp ausente representado por `None` |
| NFS-e | Listagem validada; sem registros para verificar detalhe |
| NFC-e | API retornou erro de autenticação/acesso; modelos não foram validados com payload real |
| Remessas por logística | API retornou erro de validação nas duas logísticas consultadas; detalhes permanecem cobertos por fixture sintética e teste do método público |

As amostras reais de rastreamento verificadas nesta execução tinham data
zerada. Datas sem fuso válidas foram verificadas com o valor relatado, os
exemplos oficiais e testes locais. A amostragem não prova que todos os
payloads possíveis de todos os endpoints sejam aceitos.

## Limite em relação ao Django

A atualização do Django foi excluída desta etapa a pedido do usuário. O SDK
corrige as duas falhas confirmadas de leitura. A persistência de NF-e/DANFE
em `sync_order()` e a recuperação de fichas antigas dependem do aplicativo
consumidor e não foram alteradas ou validadas aqui.
