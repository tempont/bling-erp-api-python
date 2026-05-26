"""Model tests for NFS-e (NFSe) models."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from bling_erp_api.models.generated.nfse import (
    ConfiguracaoNotaServicoDadosBaseDTO,
    NotasServicosCancelamentoDTO,
    NotasServicosContatoBaseDTO,
    NotasServicosDadosBaseDTO,
    NotasServicosDadosBaseDTO_POST,
    NotasServicosDadosDTO_POST,
    NotasServicosListResponse,
    NotasServicosParcelaDTO,
    NotasServicosServicoDTO,
)

FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "responses"


def _load_fixture(name: str) -> dict[str, Any]:
    """Load a JSON fixture and return the parsed dict."""
    path = FIXTURES_DIR / name
    return json.loads(path.read_text(encoding="utf-8"))


class TestNfseListResponse:
    """Tests for NFS-e list response deserialization."""

    def test_deserialize_nfse_list(self) -> None:
        """Deserializa ``nfse_list.json`` e verifica campos do item."""
        data = _load_fixture("nfse_list.json")
        response = NotasServicosListResponse.model_validate(data)
        assert len(response.data) == 1
        item = response.data[0]
        assert item.id == 111
        assert item.numero == "000000111"
        assert item.numero_rps == "RPS-000001"
        assert item.serie == "1"
        assert item.situacao == 3
        assert item.data_emissao == "2024-03-10"
        assert item.valor == 5000.00

    def test_deserialize_nfse_list_contato(self) -> None:
        """Deserializa contato aninhado na lista NFS-e."""
        data = _load_fixture("nfse_list.json")
        response = NotasServicosListResponse.model_validate(data)
        contato = response.data[0].contato
        assert contato is not None
        assert contato.id == 300
        assert contato.nome == "Empresa Serviços Ltda"
        assert contato.numero_documento == "98765432000111"
        assert contato.email == "servicos@exemplo.com.br"


class TestNfseConfiguracao:
    """Tests for NFS-e configuration deserialization."""

    def test_deserialize_config(self) -> None:
        """Deserializa ``nfse_configuracoes.json`` campos básicos/ISS."""
        data = _load_fixture("nfse_configuracoes.json")
        config = ConfiguracaoNotaServicoDadosBaseDTO.model_validate(data)
        assert config.basicas is not None
        assert config.basicas.emissor_padrao == 1
        assert config.basicas.natureza_operacao == 1
        assert config.iss is not None
        assert config.iss.zerar is False
        assert config.iss.reter is True
        assert config.iss.descontar is False

    def test_deserialize_config_controle(self) -> None:
        """Deserializa controle/numeracaoRPS na configuração."""
        data = _load_fixture("nfse_configuracoes.json")
        config = ConfiguracaoNotaServicoDadosBaseDTO.model_validate(data)
        assert config.controle is not None
        assert config.controle.numeracao_rps is not None
        assert config.controle.numeracao_rps.cnpj_emitente == "12345678000199"
        assert config.controle.numeracao_rps.id == 1

    def test_deserialize_config_impostos(self) -> None:
        """Deserializa impostos na configuração."""
        data = _load_fixture("nfse_configuracoes.json")
        config = ConfiguracaoNotaServicoDadosBaseDTO.model_validate(data)
        assert config.impostos is not None
        assert config.impostos.bloquear_retencao_pessoa_fisica is False

    def test_deserialize_config_envio_email(self) -> None:
        """Deserializa envioEmail na configuração."""
        data = _load_fixture("nfse_configuracoes.json")
        config = ConfiguracaoNotaServicoDadosBaseDTO.model_validate(data)
        assert config.envio_email is not None
        assert config.envio_email.enviar_boleto_rps is False

    def test_deserialize_config_adicionais(self) -> None:
        """Deserializa adicionais na configuração."""
        data = _load_fixture("nfse_configuracoes.json")
        config = ConfiguracaoNotaServicoDadosBaseDTO.model_validate(data)
        assert config.adicionais is not None
        assert config.adicionais.cfps == "9201"
        assert config.adicionais.tipo_emissao == "T"


class TestNfseModelsDirect:
    """Tests for direct NFS-e model instantiation."""

    def test_dados_base_dto_fields(self) -> None:
        """Cria ``NotasServicosDadosBaseDTO`` com argumentos nomeados."""
        model = NotasServicosDadosBaseDTO(
            id=1,
            numero="111",
            numeroRPS="RPS-001",
            serie="1",
            dataEmissao="2024-03-10",
            valor=1000.0,
        )
        assert model.id == 1
        assert model.numero == "111"
        assert model.numero_rps == "RPS-001"
        assert model.serie == "1"
        assert model.valor == 1000.0

    def test_dados_base_post_dto_fields(self) -> None:
        """Cria ``NotasServicosDadosBaseDTO_POST`` com argumentos nomeados."""
        model = NotasServicosDadosBaseDTO_POST(
            numero="222",
            numeroRPS="RPS-002",
            serie="1",
        )
        assert model.numero == "222"
        assert model.numero_rps == "RPS-002"

    def test_dados_post_dto_fields(self) -> None:
        """Cria ``NotasServicosDadosDTO_POST`` com argumentos nomeados."""
        model = NotasServicosDadosDTO_POST(
            data="2024-04-01",
            baseCalculo=1000.0,
            reterISS=True,
            desconto=50.0,
        )
        assert model.data == "2024-04-01"
        assert model.base_calculo == 1000.0
        assert model.reter_iss is True
        assert model.desconto == 50.0

    def test_cancelamento_dto_fields(self) -> None:
        """Cria ``NotasServicosCancelamentoDTO`` com argumentos nomeados."""
        model = NotasServicosCancelamentoDTO(
            codigoMotivo=1,
            justificativa="Erro na emissão da nota",
        )
        assert model.codigo_motivo == 1
        assert model.justificativa == "Erro na emissão da nota"

    def test_contato_base_dto_fields(self) -> None:
        """Cria ``NotasServicosContatoBaseDTO`` com argumentos nomeados."""
        model = NotasServicosContatoBaseDTO(
            id=100,
            nome="Cliente Teste",
            numeroDocumento="12345678901",
            email="teste@email.com",
        )
        assert model.id == 100
        assert model.nome == "Cliente Teste"
        assert model.numero_documento == "12345678901"

    def test_servico_dto_fields(self) -> None:
        """Cria ``NotasServicosServicoDTO`` com argumentos nomeados."""
        model = NotasServicosServicoDTO(
            codigo="SERV-001",
            descricao="Consultoria em TI",
            valor=5000.00,
        )
        assert model.codigo == "SERV-001"
        assert model.descricao == "Consultoria em TI"
        assert model.valor == 5000.00

    def test_parcela_dto_fields(self) -> None:
        """Cria ``NotasServicosParcelaDTO`` com argumentos nomeados."""
        model = NotasServicosParcelaDTO(
            data="2024-05-01",
            valor=2500.00,
            observacoes="Parcela 1/2",
        )
        assert model.data == "2024-05-01"
        assert model.valor == 2500.00
        assert model.observacoes == "Parcela 1/2"

    def test_dados_base_dto_extra_allow(self) -> None:
        """BlingModel allows extra fields."""
        model = NotasServicosDadosBaseDTO(campoPersonalizado=True, id=1)  # pyright: ignore[reportCallIssue]
        assert model.id == 1
        assert model.campoPersonalizado is True  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
