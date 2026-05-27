# Ordens de Produção

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
ordens = client.ordens_producao.listar(
    ids_situacoes=[1, 2],
)
ordem = client.ordens_producao.obter(12345678)
```

## Operações

### `listar`

- Bling: `GET /ordens-producao`
- Ação oficial: `ObterAcaoMultiplos`
- Resumo oficial: Obtém ordens de produção

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |
| `ids_situacoes` | `idsSituacoes[]` | `query` | não |

- Schemas de response: 200: OrdensProducaoDadosBaseDTO

### `criar`

- Bling: `POST /ordens-producao`
- Ação oficial: `Criar`
- Resumo oficial: Cria uma ordem de produção

- Schemas de request: `OrdensProducaoDadosBaseDTO`, `OrdensProducaoDadosPostDTO`
- Schemas de response: 201: BasePostResponse, 400: ErrorResponse

### `criar_multiplos`

- Bling: `POST /ordens-producao/gerar-sob-demanda`
- Ação oficial: `CriarMultiplos`
- Resumo oficial: Gera ordens de produção sob demanda

- Schemas de response: 201: OrdensProducaoDadosGeradosPorDemandaDTO

### `remover`

- Bling: `DELETE /ordens-producao/{idOrdemProducao}`
- Ação oficial: `Remover`
- Resumo oficial: Remove uma ordem de produção

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_ordem_producao` | `idOrdemProducao` | `path` | sim |

- Schemas de response: 404: ErrorResponse

### `obter`

- Bling: `GET /ordens-producao/{idOrdemProducao}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém uma ordem de produção

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_ordem_producao` | `idOrdemProducao` | `path` | sim |

- Schemas de response: 200: OrdensProducaoDadosBaseDTO/OrdensProducaoDadosDTO, 404: ErrorResponse

### `alterar`

- Bling: `PUT /ordens-producao/{idOrdemProducao}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera uma ordem de produção

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_ordem_producao` | `idOrdemProducao` | `path` | sim |

- Schemas de request: `OrdensProducaoDadosBaseDTO`, `OrdensProducaoDadosPostDTO`
- Schemas de response: 400: ErrorResponse, 404: ErrorResponse

### `alterar_situacao`

- Bling: `PUT /ordens-producao/{idOrdemProducao}/situacoes`
- Ação oficial: `AlterarSituacao`
- Resumo oficial: Altera a situação de uma ordem de produção

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_ordem_producao` | `idOrdemProducao` | `path` | sim |

- Schemas de request: `OrdensProducaoSituacaoDadosDTO`
- Schemas de response: 400: ErrorResponse, 404: ErrorResponse
