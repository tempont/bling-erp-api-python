# Naturezas de Operações

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
naturezas = client.naturezas_operacoes.listar(
    situacao=1,
)
tributacao = client.naturezas_operacoes.obter_tributacao(
    12345678, calculo={...})
```

## Operações

### `listar`

- Bling: `GET /naturezas-operacoes`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém naturezas de operações

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |
| `situacao` | `situacao` | `query` | não |
| `descricao` | `descricao` | `query` | não |

- Schemas de response: 200: NaturezasOperacoesDadosDTO, 400: ErrorResponse

### `obter_tributacao`

- Bling: `POST /naturezas-operacoes/{idNaturezaOperacao}/obter-tributacao`
- Ação oficial: `ObterTributacao`
- Resumo oficial: Obtém regras de tributação da natureza de operação

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_natureza_operacao` | `idNaturezaOperacao` | `path` | sim |

- Schemas de request: `CalculosImpostosCalculoDTO`
- Schemas de response: 200: CalculosImpostosDadosDTO, 404: ErrorResponse, 400: ErrorResponse
