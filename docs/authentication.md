# Autenticação

## Visão Geral

O SDK delega a autenticação ao pacote [`bling-jwt-auth`](https://pypi.org/project/bling-jwt-auth/),
que implementa o fluxo de **Authorization Code** do OAuth2 para a API do Bling ERP.

O SDK precisa apenas de um objeto que forneça tokens de acesso. Isso pode ser:

- Um adaptador construído a partir de variáveis de ambiente
- Um adaptador com um `token_provider` personalizado
- Uma instância `httpx.Auth` passada diretamente

## Variáveis de Ambiente

A maneira mais simples de configurar a autenticação é através de variáveis
de ambiente. O `BlingClient.from_env()` lê as seguintes variáveis:

| Variável | Descrição | Obrigatória |
|---|---|---|
| `BLING_CLIENT_ID` | Client ID da sua aplicação no Bling | Sim |
| `BLING_CLIENT_SECRET` | Client Secret da sua aplicação no Bling | Sim |
| `BLING_REFRESH_TOKEN` | Refresh token para obter novos access tokens | Sim |
| `BLING_REDIRECT_URI` | URI de redirecionamento configurada no Bling | Não (default: `urn:ietf:wg:oauth:2.0:oob`) |

```bash
export BLING_CLIENT_ID="seu_client_id"
export BLING_CLIENT_SECRET="seu_client_secret"
export BLING_REFRESH_TOKEN="seu_refresh_token"
```

## Criando um Client com from_env()

```python
from bling_erp_api import BlingClient

# Lê as variáveis BLING_* do ambiente
client = BlingClient.from_env()

# Opcionalmente, use como context manager
with BlingClient.from_env() as client:
    # ...
```

Você também pode passar parâmetros adicionais:

```python
client = BlingClient.from_env(
    base_url="https://api.bling.com.br/api/v3",
    timeout=30.0,
    rate_limit_max_requests=5,
    rate_limit_period_seconds=1.0,
)
```

## Custom Token Provider

Se você precisa de controle mais fino sobre a autenticação, implemente o
protocolo `AccessTokenProvider`:

```python
from httpx import Auth
from bling_erp_api import BlingClient
from bling_jwt_auth import BlingAuth

# Usando bling-jwt-auth diretamente
auth = BlingAuth(
    client_id="seu_client_id",
    client_secret="seu_client_secret",
    refresh_token="seu_refresh_token",
)

client = BlingClient(auth=auth)
```

Ou implemente seu próprio provedor:

```python
class MyTokenProvider:
    def get_access_token(self) -> str:
        # Sua lógica de obtenção de token
        return "seu_access_token"

client = BlingClient(token_provider=MyTokenProvider())
```

## O Fluxo OAuth2

O `bling-jwt-auth` gerencia automaticamente:

1. Obtenção do access token usando o refresh token
2. Renovação automática quando o token expira
3. Refresh de token quando necessário

Para obter o refresh token inicial, você precisa passar pelo fluxo de
autorização do Bling. Veja a documentação do
[bling-jwt-auth](https://pypi.org/project/bling-jwt-auth/) para instruções
detalhadas.
