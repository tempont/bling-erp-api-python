# Vendedores

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
Lista os vendedores.
```

## Operações

### `listar`

- Bling: `GET /vendedores`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém vendedores

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |
| `nome_contato` | `nomeContato` | `query` | não |
| `situacao_contato` | `situacaoContato` | `query` | não |
| `id_contato` | `idContato` | `query` | não |
| `id_loja` | `idLoja` | `query` | não |
| `data_alteracao_inicial` | `dataAlteracaoInicial` | `query` | não |
| `data_alteracao_final` | `dataAlteracaoFinal` | `query` | não |

- Schemas de response: 200: VendedoresDadosBaseDTO

### `obter`

- Bling: `GET /vendedores/{idVendedor}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém um vendedor

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_vendedor` | `idVendedor` | `path` | sim |

- Schemas de response: 200: VendedoresDadosBaseDTO/VendedoresDadosDTO, 404: ErrorResponse
