# Caixas e Bancos

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
lancamentos = client.caixas_bancos.listar(
    data_inicial="2024-01-01",
    data_final="2024-12-31",
)
```

## Operações

### `listar`

- Bling: `GET /caixas`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém lista de lançamentos de caixas e bancos.

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `data_inicial` | `dataInicial` | `query` | não |
| `data_final` | `dataFinal` | `query` | não |
| `ids_categorias` | `idsCategorias` | `query` | não |
| `id_conta_financeira` | `idContaFinanceira` | `query` | não |
| `pesquisa` | `pesquisa` | `query` | não |
| `valor` | `valor` | `query` | não |
| `situacao_conciliacao` | `situacaoConciliacao` | `query` | não |
| `situacao` | `situacao` | `query` | não |

- Schemas de response: 200: CaixasBancosItemLancamentoDTO, 400: ErrorResponse

### `criar`

- Bling: `POST /caixas`
- Ação oficial: `Criar`
- Resumo oficial: Cria um novo lançamento de caixa e banco.

- Schemas de request: `CaixasBancosSalvarLancamentoDTO`
- Schemas de response: 201: CaixasBancosSalvarLancamentoResponseDTO, 400: ErrorResponse

### `remover`

- Bling: `DELETE /caixas/{idCaixa}`
- Ação oficial: `Remover`
- Resumo oficial: Remove um lançamento de caixa e banco

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_caixa` | `idCaixa` | `path` | sim |

- Schemas de response: 400: ErrorResponse, 404: ErrorResponse

### `obter`

- Bling: `GET /caixas/{idCaixa}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém um lançamento de caixa e banco.

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_caixa` | `idCaixa` | `path` | sim |

- Schemas de response: 200: CaixasBancosLancamentoDTO, 404: ErrorResponse

### `alterar`

- Bling: `PUT /caixas/{idCaixa}`
- Ação oficial: `Alterar`
- Resumo oficial: Atualiza um lançamento de caixa e banco.

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_caixa` | `idCaixa` | `path` | sim |

- Schemas de request: `CaixasBancosSalvarLancamentoDTO`
- Schemas de response: 200: CaixasBancosSalvarLancamentoResponseDTO, 400: ErrorResponse, 404: ErrorResponse
