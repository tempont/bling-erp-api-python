# Empresas

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
dados = client.empresas.obter_dados_basicos()
```

## Operações

### `obter_dados_basicos`

- Bling: `GET /empresas/me/dados-basicos`
- Ação oficial: `Obter`
- Resumo oficial: Obtém dados básicos da empresa

- Schemas de response: 200: EmpresasDadosBasicosDTO
