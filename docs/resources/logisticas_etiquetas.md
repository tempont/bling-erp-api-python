# Logísticas - Etiquetas

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
etiquetas = client.logisticas_etiquetas.obter(formato='PDF', ids_vendas=[1])
```

## Operações

### `obter_etiquetas`

- Bling: `GET /logisticas/etiquetas`
- Ação oficial: `ObterEtiquetaMultiplos`
- Resumo oficial: Obtém etiquetas das vendas

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `formato` | `formato` | `query` | sim |
| `ids_vendas` | `idsVendas[]` | `query` | sim |

- Schemas de response: 200: LogisticasEtiquetasDadosResponseDTO, 400: ErrorResponse, 404: ErrorResponse
