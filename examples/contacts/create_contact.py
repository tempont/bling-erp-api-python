"""Exemplo que cria um contato."""

from bling_erp_api import BlingClient
from bling_erp_api.models.generated.contacts import ContatosPostRequest, ContatosPostResponse201


def main() -> None:
    """Cria um contato simplificado."""
    # Model: ContatosPostRequest  # noqa: ERA001
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
    payload = ContatosPostRequest.model_construct(
        id=0, nome="Nova Empresa LTDA", tipo="J", situacao="A"
    )
    with BlingClient.from_env() as client:
        response = client.contatos.criar(payload)
        parsed = ContatosPostResponse201(**response)  # type: ignore[reportArgumentType]
        print(parsed.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
