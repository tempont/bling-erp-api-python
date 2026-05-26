# Anúncios - Categorias

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
categorias = client.ad_categories.listar()
categoria = client.ad_categories.obter(123456)
```

## Operações

### `listar`

- Bling: `GET /anuncios/categorias`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém categorias de anúncios

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `tipo_integracao` | `tipoIntegracao` | `query` | sim |
| `id_loja` | `idLoja` | `query` | sim |
| `id_categoria` | `idCategoria` | `query` | não |
| `tipo_produto` | `tipoProduto` | `query` | não |

- Schemas de response: 200: AnunciosCategoriaDTO, 400: ErrorResponse

### `obter`

- Bling: `GET /anuncios/categorias/{idCategoria}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém uma categoria de anúncio

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_categoria` | `idCategoria` | `path` | sim |
| `tipo_integracao` | `tipoIntegracao` | `query` | sim |
| `id_loja` | `idLoja` | `query` | sim |

- Schemas de response: 200: AnunciosGetAttributesFromCategoryResponseDTO, 404: ErrorResponse, 400: ErrorResponse
