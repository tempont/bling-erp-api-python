"""Example: List financial accounts."""

from __future__ import annotations

from typing import TYPE_CHECKING

from bling_erp_api import BlingClient

if TYPE_CHECKING:
    from bling_erp_api.models.generated.contas_contabeis import (
        ContasContabeisGetResponse200,
    )


def listar_contas(
    *,
    pagina: int = 1,
    limite: int = 100,
    situacoes: list[int] | None = None,
) -> ContasContabeisGetResponse200:
    """Lista contas financeiras."""
    with BlingClient.from_env() as client:
        return client.contas_contabeis.listar(pagina=pagina, limite=limite, situacoes=situacoes)


def main() -> None:
    """List financial accounts with status 'Ativo'."""
    contas = listar_contas(situacoes=[1])
    print(contas.model_dump_json(indent=2, by_alias=True))


if __name__ == "__main__":
    main()
