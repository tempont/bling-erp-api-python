# Propostas Comerciais

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
Lista as propostas comerciais.
```

## Operações

### `remover_varios`

- Bling: `DELETE /propostas-comerciais`
- Ação oficial: `RemoverMultiplos`
- Resumo oficial: Remove múltiplas propostas comerciais

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `ids_propostas_comerciais` | `idsPropostasComerciais[]` | `query` | sim |

- Schemas de response: 200: ErrorResponse, 400: ErrorResponse

### `listar`

- Bling: `GET /propostas-comerciais`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém propostas comerciais

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `situacao` | `situacao` | `query` | não |
| `id_contato` | `idContato` | `query` | não |
| `data_inicial` | `dataInicial` | `query` | não |
| `data_final` | `dataFinal` | `query` | não |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |

- Schemas de response: 200: OrcamentosDadosBaseDTO

### `criar`

- Bling: `POST /propostas-comerciais`
- Ação oficial: `Criar`
- Resumo oficial: Cria uma proposta comercial

- Schemas de request: `OrcamentosDadosBaseDTO`, `OrcamentosDadosDTO`
- Schemas de response: 201: BasePostResponse, 400: ErrorResponse

### `remover`

- Bling: `DELETE /propostas-comerciais/{idPropostaComercial}`
- Ação oficial: `Remover`
- Resumo oficial: Remove uma proposta comercial

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_proposta_comercial` | `idPropostaComercial` | `path` | sim |

- Schemas de response: 400: ErrorResponse

### `obter`

- Bling: `GET /propostas-comerciais/{idPropostaComercial}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém uma proposta comercial

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_proposta_comercial` | `idPropostaComercial` | `path` | sim |

- Schemas de response: 200: OrcamentosDadosBaseDTO/OrcamentosDadosDTO, 404: ErrorResponse

### `alterar`

- Bling: `PUT /propostas-comerciais/{idPropostaComercial}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera uma proposta comercial

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_proposta_comercial` | `idPropostaComercial` | `path` | sim |

- Schemas de request: `OrcamentosDadosBaseDTO`, `OrcamentosDadosDTO`
- Schemas de response: 400: ErrorResponse, 404: ErrorResponse

### `alterar_situacao`

- Bling: `PATCH /propostas-comerciais/{idPropostaComercial}/situacoes`
- Ação oficial: `AlterarSituacao`
- Resumo oficial: Altera a situação de uma proposta comercial

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_proposta_comercial` | `idPropostaComercial` | `path` | sim |

- Schemas de request: `OrcamentosSituacaoDTO`
- Schemas de response: 400: ErrorResponse, 404: ErrorResponse
