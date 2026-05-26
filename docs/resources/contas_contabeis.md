# Contas Financeiras

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
contas = client.contas_contabeis.listar(
    situacoes=[1],
)
conta = client.contas_contabeis.obter(123456)
```

## Operações

### `listar`

- Bling: `GET /contas-contabeis`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém contas financeiras

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |
| `ocultar_invisiveis` | `ocultarInvisiveis` | `query` | não |
| `ocultar_tipo_conta_bancaria` | `ocultarTipoContaBancaria` | `query` | não |
| `situacoes` | `situacoes` | `query` | não |
| `alias_integracao` | `aliasIntegracao` | `query` | não |
| `alias_integracao` | `aliasIntegracao` | `path` | não |
| `ordenacao` | `ordenacao` | `query` | não |

- Schemas de response: 200: ContasContabeisDadosDTO

### `obter`

- Bling: `GET /contas-contabeis/{idContaContabil}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém uma conta financeira

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_conta_contabil` | `idContaContabil` | `path` | sim |

- Schemas de response: 200: ContasContabeisDadosDTO, 404: ErrorResponse
