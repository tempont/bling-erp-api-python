# Borderôs

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
bordero = client.borderos.obter(123456)
```

## Operações

### `remover`

- Bling: `DELETE /borderos/{idBordero}`
- Ação oficial: `Remover`
- Resumo oficial: Remove um borderô

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_bordero` | `idBordero` | `path` | sim |

- Schemas de response: 400: ErrorResponse, 404: ErrorResponse

### `obter`

- Bling: `GET /borderos/{idBordero}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém um borderô

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_bordero` | `idBordero` | `path` | sim |

- Schemas de response: 200: BorderosDadosDTO, 404: ErrorResponse
