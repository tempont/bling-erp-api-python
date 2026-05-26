# Anúncios

Esta página é gerada a partir de `specs/bling-openapi-reference.json`.
A documentação oficial é usada como contrato para paths, métodos e parâmetros.

## Exemplo

```python
anuncios = client.ads.listar(pagina=1, limite=10)
anuncio = client.ads.obter(123456)
```

## Operações

### `listar`

- Bling: `GET /anuncios`
- Ação oficial: `ObterMultiplos`
- Resumo oficial: Obtém anúncios

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `pagina` | `pagina` | `query` | não |
| `limite` | `limite` | `query` | não |
| `situacao` | `situacao` | `query` | não |
| `id_produto` | `idProduto` | `query` | não |
| `tipo_integracao` | `tipoIntegracao` | `query` | sim |
| `id_loja` | `idLoja` | `query` | sim |

- Schemas de response: 200: AnunciosGetAllResponseDTO, 400: ErrorResponse

### `criar`

- Bling: `POST /anuncios`
- Ação oficial: `Criar`
- Resumo oficial: Cria um anúncio

- Schemas de request: `AnunciosSaveRequest`
- Schemas de response: 201: AnunciosSaveResponseDTO, 400: ErrorResponse

### `remover`

- Bling: `DELETE /anuncios/{idAnuncio}`
- Ação oficial: `Remover`
- Resumo oficial: Remove um anúncio

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_anuncio` | `idAnuncio` | `path` | sim |
| `tipo_integracao` | `tipoIntegracao` | `query` | sim |
| `id_loja` | `idLoja` | `query` | sim |

- Schemas de response: 400: ErrorResponse, 404: ErrorResponse

### `obter`

- Bling: `GET /anuncios/{idAnuncio}`
- Ação oficial: `Obter`
- Resumo oficial: Obtém um anúncio

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_anuncio` | `idAnuncio` | `path` | sim |
| `tipo_integracao` | `tipoIntegracao` | `query` | sim |
| `id_loja` | `idLoja` | `query` | sim |

- Schemas de response: 200: AnunciosGetByIdResponseDTO, 400: ErrorResponse, 404: ErrorResponse

### `alterar`

- Bling: `PUT /anuncios/{idAnuncio}`
- Ação oficial: `Alterar`
- Resumo oficial: Altera um anúncio

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_anuncio` | `idAnuncio` | `path` | sim |

- Schemas de request: `AnunciosSaveRequest`
- Schemas de response: 400: ErrorResponse, 404: ErrorResponse

### `pausar`

- Bling: `POST /anuncios/{idAnuncio}/pausar`
- Ação oficial: `Pausar`
- Resumo oficial: Pausa um anúncio

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_anuncio` | `idAnuncio` | `path` | sim |
| `tipo_integracao` | `tipoIntegracao` | `query` | sim |
| `id_loja` | `idLoja` | `query` | sim |

- Schemas de response: 400: ErrorResponse, 404: ErrorResponse

### `publicar`

- Bling: `POST /anuncios/{idAnuncio}/publicar`
- Ação oficial: `Publicar`
- Resumo oficial: Publica um anúncio

| Argumento SDK | Parâmetro Bling | Local | Obrigatório |
| --- | --- | --- | --- |
| `id_anuncio` | `idAnuncio` | `path` | sim |
| `tipo_integracao` | `tipoIntegracao` | `query` | sim |
| `id_loja` | `idLoja` | `query` | sim |

- Schemas de response: 400: ErrorResponse, 404: ErrorResponse
