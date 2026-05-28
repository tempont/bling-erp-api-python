"""Exemplo que atualiza um contato existente."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.contacts import ContatosIdContatoPutRequest

CONTATO_ID = 12345678


def main() -> None:
    """Altera dados de um contato por ``PUT``."""
    # Model: ContatosIdContatoPutRequest (same fields as ContatosPostRequest)
    #   Required: id (int), nome (str), situacao (str), tipo (str)
    #   Optional: codigo (str|None), numero_documento (str|None), telefone (str|None),
    #             celular (str|None), fantasia (str|None), indicador_ie (int|None),  # noqa: ERA001
    #             ie (str|None), rg (str|None), inscricao_municipal (str|None),  # noqa: ERA001
    #             orgao_emissor (str|None), email (str|None), email_nota_fiscal (str|None),  # noqa: ERA001
    #             orgao_publico (str|None), endereco (ContatosEnderecoDTO|None),  # noqa: ERA001
    #             vendedor (ContatosVendedorDTO|None), dados_adicionais (ContatosDadoAdicionalDTO|None),  # noqa: ERA001
    #             financeiro (ContatosFinanceiroDTO|None), pais (ContatosPaisDTO|None),  # noqa: ERA001
    #             tipos_contato (list[ContatosTipoContatoDTO]|None),  # noqa: ERA001
    #             pessoas_contato (list[ContatosPessoaContatoDTO]|None)  # noqa: ERA001
    payload = ContatosIdContatoPutRequest.model_construct(
        id=0, nome="Nova Empresa LTDA - Matriz", situacao="A", tipo="J"
    )
    with BlingClient.from_env() as client:
        response = client.contatos.alterar(CONTATO_ID, payload)
        # NOTE: No success response model for PUT /contatos/{idContato} (only error responses in OpenAPI spec).
        print(response)


if __name__ == "__main__":
    main()
