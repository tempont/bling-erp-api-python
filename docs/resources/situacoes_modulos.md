# Módulos de Situações

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
Lista os modulos de situacoes.
```

## Operações

### `listar`

- Bling: `GET /situacoes/modulos`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém módulos

- Schemas de response: 200: SituacoesModuloBaseDTO/SituacoesModuloDTO

### `obter`

- Bling: `GET /situacoes/modulos/{idModuloSistema}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém situações de um módulo

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_modulo_sistema` | `idModuloSistema` | `path` | sim |

- Schemas de response: 200: SituacoesDTO/SituacoesDadosDTO, 404: ErrorResponse

### `listar_acoes`

- Bling: `GET /situacoes/modulos/{idModuloSistema}/acoes`
- Ação oficial: `ObterAcaoMultiplos`
- Resumo oficial: Obtém as ações de um módulo

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_modulo_sistema` | `idModuloSistema` | `path` | sim |

- Schemas de response: 200: SituacoesAcaoDTO, 404: ErrorResponse

### `listar_transicoes`

- Bling: `GET /situacoes/modulos/{idModuloSistema}/transicoes`
- Ação oficial: `ObterTransicaoMultiplos`
- Resumo oficial: Obtém as transições de um módulo

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_modulo_sistema` | `idModuloSistema` | `path` | sim |

- Schemas de response: 200: SituacoesTransicaoDTO, 404: ErrorResponse
