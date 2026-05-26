"""Model tests for NotasFiscais (NF-e/NFC-e) models."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from bling_erp_api.models.generated.invoices import (
    NotaFiscalGetResponse,
    NotasFiscaisDadosBaseDTO,
    NotasFiscaisDadosPostDTO,
    NotasFiscaisDocumentoDTO,
    NotasFiscaisExclusaoDTO,
    NotasFiscaisItemDTO,
    NotasFiscaisListResponse,
    NotasFiscaisLojaDTO,
    NotasFiscaisNaturezaOperacaoDTO,
    NotasFiscaisVendedorDTO,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def _load_fixture(name: str) -> dict[str, Any]:
    """Load a JSON fixture and return the parsed dict."""
    path = FIXTURES_DIR / name
    return json.loads(path.read_text(encoding="utf-8"))


class TestNotasFiscaisListResponse:
    """Tests for NF-e/NFC-e list response deserialization."""

    def test_deserialize_nfe_list(self) -> None:
        """Deserializa ``nfe_list.json`` e verifica campos do item."""
        data = _load_fixture("nfe_list.json")
        response = NotasFiscaisListResponse.model_validate(data)
        assert len(response.data) == 1
        item = response.data[0]
        assert item.id == 12345
        assert item.tipo == 1
        assert item.situacao == 3
        assert item.numero == "000001234"
        assert item.chave_acesso == "35240112345678901234567890123456789012345678"
        assert item.data_emissao == "2024-01-15 10:30:00"
        assert item.data_operacao == "2024-01-15"

    def test_deserialize_nfe_list_contato(self) -> None:
        """Deserializa contato aninhado na lista NF-e."""
        data = _load_fixture("nfe_list.json")
        response = NotasFiscaisListResponse.model_validate(data)
        contato = response.data[0].contato
        assert contato is not None
        assert contato.id == 100
        assert contato.nome == "Cliente Exemplo Ltda"
        assert contato.tipo_pessoa == "J"
        assert contato.numero_documento == "12345678000199"
        assert contato.ie == "123456789"
        assert contato.contribuinte == 1

    def test_deserialize_nfe_list_contato_endereco(self) -> None:
        """Deserializa endereço aninhado no contato da lista."""
        data = _load_fixture("nfe_list.json")
        response = NotasFiscaisListResponse.model_validate(data)
        contato = response.data[0].contato
        assert contato is not None
        endereco = contato.endereco
        assert endereco is not None
        assert endereco.endereco == "Rua Exemplo"
        assert endereco.numero == "100"
        assert endereco.bairro == "Centro"
        assert endereco.municipio == "São Paulo"
        assert endereco.uf == "SP"

    def test_deserialize_nfe_list_natureza_operacao(self) -> None:
        """Deserializa naturezaOperacao aninhada."""
        data = _load_fixture("nfe_list.json")
        response = NotasFiscaisListResponse.model_validate(data)
        natureza = response.data[0].natureza_operacao
        assert natureza is not None
        assert natureza.id == 1

    def test_deserialize_nfe_list_loja(self) -> None:
        """Deserializa loja aninhada na lista."""
        data = _load_fixture("nfe_list.json")
        response = NotasFiscaisListResponse.model_validate(data)
        loja = response.data[0].loja
        assert loja is not None
        assert loja.id == 1
        assert loja.numero == "001"

    def test_deserialize_nfce_list(self) -> None:
        """Deserializa ``nfce_list.json`` (NFC-e)."""
        data = _load_fixture("nfce_list.json")
        response = NotasFiscaisListResponse.model_validate(data)
        assert len(response.data) == 1
        item = response.data[0]
        assert item.id == 54321
        assert item.tipo == 1
        assert item.situacao == 3
        assert item.numero == "000054321"
        contato = item.contato
        assert contato is not None
        assert contato.nome == "Consumidor Final"
        assert contato.tipo_pessoa == "F"


class TestNotaFiscalGetResponse:
    """Tests for single NF-e get response."""

    def test_deserialize_nfe_get(self) -> None:
        """Deserializa ``nfe_get.json`` e verifica campos do dict interno."""
        data = _load_fixture("nfe_get.json")
        response = NotaFiscalGetResponse.model_validate(data)
        assert response.data is not None
        inner = response.data
        assert isinstance(inner, dict)
        assert inner.get("id") == 12345
        assert inner.get("numero") == "000001234"
        assert inner.get("valorNota") == 1500.50
        assert inner.get("finalidade") == 1

    def test_deserialize_nfe_get_itens(self) -> None:
        """Deserializa itens da NF-e get."""
        data = _load_fixture("nfe_get.json")
        response = NotaFiscalGetResponse.model_validate(data)
        assert response.data is not None
        inner = response.data
        itens = inner.get("itens", [])
        assert len(itens) == 1
        assert itens[0]["codigo"] == "PROD-001"

    def test_deserialize_nfe_get_parcelas(self) -> None:
        """Deserializa parcelas da NF-e get."""
        data = _load_fixture("nfe_get.json")
        response = NotaFiscalGetResponse.model_validate(data)
        assert response.data is not None
        inner = response.data
        parcelas = inner.get("parcelas", [])
        assert len(parcelas) == 1
        assert parcelas[0]["data"] == "2024-02-15"


class TestNotasFiscaisModelsDirect:
    """Tests for direct model instantiation."""

    def test_dados_base_dto_fields(self) -> None:
        """Cria ``NotasFiscaisDadosBaseDTO`` com argumentos nomeados."""
        model = NotasFiscaisDadosBaseDTO(
            id=1,
            tipo=1,
            numero="123",
            dataOperacao="2024-01-01",
        )
        assert model.id == 1
        assert model.tipo == 1
        assert model.numero == "123"
        assert model.data_operacao == "2024-01-01"
        # Optional fields default to None
        assert model.situacao is None
        assert model.contato is None

    def test_dados_base_dto_extra_allow(self) -> None:
        """BlingModel allows extra fields not defined in the model."""
        model = NotasFiscaisDadosBaseDTO(campoExtra="valor_extra", id=1)  # pyright: ignore[reportCallIssue]
        assert model.id == 1
        assert model.campoExtra == "valor_extra"  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

    def test_dados_post_dto_fields(self) -> None:
        """Cria ``NotasFiscaisDadosPostDTO`` com argumentos nomeados."""
        model = NotasFiscaisDadosPostDTO(
            finalidade=1,
            observacoes="Teste",
            desconto=10.0,
        )
        assert model.finalidade == 1
        assert model.observacoes == "Teste"
        assert model.desconto == 10.0
        # Optional fields
        assert model.seguro is None

    def test_item_dto_fields(self) -> None:
        """Cria ``NotasFiscaisItemDTO`` com argumentos nomeados."""
        model = NotasFiscaisItemDTO(
            codigo="PROD-001",
            descricao="Produto Teste",
            quantidade=5.0,
            valor=100.0,
        )
        assert model.codigo == "PROD-001"
        assert model.descricao == "Produto Teste"
        assert model.quantidade == 5.0
        assert model.valor == 100.0

    def test_exclusao_dto_fields(self) -> None:
        """Cria ``NotasFiscaisExclusaoDTO`` com argumentos nomeados."""
        model = NotasFiscaisExclusaoDTO(
            idsExcluidos=[1, 2, 3],
            alertas=["Erro ao excluir ID 4"],
        )
        assert model.ids_excluidos == [1, 2, 3]
        assert model.alertas == ["Erro ao excluir ID 4"]

    def test_documento_dto_fields(self) -> None:
        """Cria ``NotasFiscaisDocumentoDTO`` com argumentos nomeados."""
        model = NotasFiscaisDocumentoDTO(
            nome="NFe35240112345678901234567890123456789012345678.xml",
            conteudo="H4sIAAAAAAAA...",
        )
        assert model.nome is not None
        assert model.nome.startswith("NFe")
        assert model.conteudo == "H4sIAAAAAAAA..."

    def test_loja_dto_minimal(self) -> None:
        """Cria ``NotasFiscaisLojaDTO`` apenas com id."""
        model = NotasFiscaisLojaDTO(id=1)
        assert model.id == 1
        assert model.numero is None

    def test_vendedor_dto_minimal(self) -> None:
        """Cria ``NotasFiscaisVendedorDTO`` apenas com id."""
        model = NotasFiscaisVendedorDTO(id=10)
        assert model.id == 10

    def test_natureza_operacao_dto_minimal(self) -> None:
        """Cria ``NotasFiscaisNaturezaOperacaoDTO`` apenas com id."""
        model = NotasFiscaisNaturezaOperacaoDTO(id=1)
        assert model.id == 1
