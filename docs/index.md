# Bling ERP API SDK

Python SDK for the [Bling ERP API v3](https://www.bling.com.br/).

## Visão Geral

O **Bling ERP API SDK** é um SDK Python não oficial que fornece acesso
tipado e idiomático à API v3 do Bling ERP. Com ele, você pode integrar
seus sistemas Python com mais de 40 recursos do Bling, incluindo produtos,
pedidos, notas fiscais, contatos, logística, e muito mais.

## Principais Funcionalidades

- **40+ recursos** — produtos, pedidos, notas fiscais, contatos, logística, estoque, finanças
- **Autenticação OAuth2** — gerenciada automaticamente via `bling-jwt-auth`
- **Rate limiting** — 3 requisições/segundo com retry automático em 429
- **Modelos tipados** — Pydantic v2 com campos em snake_case e aliases para nomes Bling
- **API pt-BR + EN** — métodos canônicos em português com aliases em inglês
- **Transporte síncrono e assíncrono**
- **Contratos OpenAPI** — geração e validação contra a especificação oficial

## Comece por aqui

```python
from bling_erp_api import BlingClient

with BlingClient.from_env() as client:
    produtos = client.produtos.listar(limit=10)
    for produto in produtos.get("data", []):
        print(produto.get("nome"))
```

## Quick Links

- [Comece por aqui (Getting Started)](getting-started.md) — instalação e primeiro uso
- [Autenticação](authentication.md) — configuração de credenciais OAuth2
- [Paginação](pagination.md) — navegando por resultados paginados
- [Erros](errors.md) — tratamento de exceções tipadas
- [Referência da API](api-reference/index.md) — documentação completa de todas as classes e métodos

## Arquitetura

O SDK é estruturado em camadas:

```
bling_erp_api/
├── client.py          # Cliente principal (BlingClient)
├── auth/              # Adaptador de autenticação OAuth2
├── transport/         # Transporte HTTP com rate limiting
├── resources/         # Recursos da API (produtos, pedidos, etc.)
├── models/            # Modelos Pydantic tipados
├── contracts/         # Contratos gerados do OpenAPI
└── utils/             # Utilitários diversos
```

Cada recurso (ex.: `client.produtos`, `client.contatos`) expõe métodos
para as operações da API Bling, seguindo uma convenção consistente de nomenclatura.
