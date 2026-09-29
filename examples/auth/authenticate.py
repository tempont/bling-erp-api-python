"""Exemplo de código para autenticação com o Bling de forma interativa.

Usa o pacote bling_jwt_auth e valida o ``state`` OAuth com os helpers de
``bling_erp_api.auth`` (``parse_oauth_callback`` + ``verify_oauth_state``).

Documentação: https://github.com/tempont/bling-jwt-auth-python
Variáveis (obrigatórias):
    - BLING_CLIENT_ID
    - BLING_CLIENT_SECRET
    - BLING_REDIRECT_URI

Podem vir do ambiente ou de um arquivo `.env` no diretório corrente.
`pydantic-settings` resolve o `.env` a partir do CWD, não do diretório
deste script.
"""  # noqa

import os
import sys

from bling_jwt_auth import BlingAuthSettings, OAuthClient, TokenManager, create_token_store
from pydantic import ValidationError

from bling_erp_api.auth import parse_oauth_callback, verify_oauth_state

_FIELD_TO_ENV = {
    "client_id": "BLING_CLIENT_ID",
    "client_secret": "BLING_CLIENT_SECRET",
    "redirect_uri": "BLING_REDIRECT_URI",
}

# 1. Carrega os settings de variáveis de ambiente.
try:
    settings = BlingAuthSettings.load()
except ValidationError as exc:
    missing = sorted(
        {
            _FIELD_TO_ENV.get(str(err["loc"][0]), str(err["loc"][0]))
            for err in exc.errors()
            if err["type"] == "missing"
        }
    )
    details = "; ".join(f"{'.'.join(map(str, err['loc']))}: {err['msg']}" for err in exc.errors())
    print(
        "\n⚠️  Falha ao carregar as credenciais OAuth do Bling.\n\n"
        f"Variáveis obrigatórias ausentes: {', '.join(missing)}\n"
        f"Detalhes: {details}\n\n"
        "As credenciais são lidas das variáveis de ambiente `BLING_*` ou de um\n"
        "arquivo `.env` no diretório corrente (de onde o comando foi executado).\n\n"
        "Como resolver:\n"
        "  1. Exporte as variáveis `BLING_*` no ambiente antes de executar\n"
        "     este script; ou\n"
        "  2. Copie `.env.example` para `.env` na raiz do projeto e preencha\n"
        "     as variáveis com os dados da aplicação OAuth registrada no Bling.\n\n"
        "Nota: o `.env` é resolvido a partir do diretório corrente (CWD),\n"
        "não do diretório deste script. Se as credenciais vêm de um\n"
        "gerenciador de segredos, garanta que as variáveis sejam injetadas\n"
        "no processo que executa este comando.\n",
        file=sys.stderr,
    )
    sys.exit(1)

# 2. Cria o armazenamento de tokens. (default: SQLite)
store = create_token_store(settings)

# 3. Cria o cliente Oauth e o TokenManager e inicia a autenticação via CLI/Browser.
with OAuthClient(settings) as oauth:
    manager = TokenManager(oauth, store, settings)

    # 4. Build authorization URL for the browser with a CSRF state value.
    state = os.urandom(16).hex()
    auth_url = oauth.build_authorization_url(state=state)
    print(f"Open in browser: {auth_url}")
    # User opens URL, approves access, Bling redirects to
    # BLING_REDIRECT_URI?code=...&state=...

    # 5. Parse the callback (full URL or query string), verify the state
    #    against this session and exchange the code for tokens
    #    (saves to store automatically).
    raw_callback = input(
        "Paste callback URL or query string (code=...&state=... even from error page): "
    ).strip()
    code, received_state = parse_oauth_callback(raw_callback)
    verify_oauth_state(received_state, state)
    manager.save_from_code(code)

    # 6. Now ready — every subsequent call auto-refreshes
    token = manager.get_access_token()
    print("Access token acquired successfully.")
