"""Stable model aliases for public export."""

from bling_erp_api.models.generated.propostas_comerciais import (
    OrcamentosDadosBaseDTO,
    OrcamentosDadosDTO,
    OrcamentosSituacaoDTO,
    PropostasComerciaisDeleteResponse200,
    PropostasComerciaisGetResponse200,
    PropostasComerciaisIdPropostaComercialGetResponse200,
    PropostasComerciaisPostRequest,
    PropostasComerciaisPostResponse201,
)
from bling_erp_api.models.generated.purchase_orders import (
    PedidosCompraResponsePOSTPUT,
    PedidosComprasDadosBaseDTO,
    PedidosComprasDadosDTO,
    PedidosComprasGetResponse200,
    PedidosComprasIdPedidoCompraGetResponse200,
    PedidosComprasIdPedidoCompraPutRequest,
    PedidosComprasIdPedidoCompraPutResponse200,
    PedidosComprasPostRequest,
    PedidosComprasPostResponse201,
)
from bling_erp_api.models.generated.situacoes import (
    SituacoesDadosDTO,
    SituacoesDTO,
)
from bling_erp_api.models.generated.situacoes_modulos import (
    SituacoesModuloDTO,
)
from bling_erp_api.models.generated.situacoes_transicoes import (
    SituacoesTransicaoDTO,
)
from bling_erp_api.models.generated.vendedores import (
    VendedoresDadosBaseDTO,
    VendedoresDadosDTO,
    VendedoresGetResponse200,
    VendedoresIdVendedorGetResponse200,
)

__all__ = [
    "OrcamentosDadosBaseDTO",
    "OrcamentosDadosDTO",
    "OrcamentosSituacaoDTO",
    "PedidosCompraResponsePOSTPUT",
    "PedidosComprasDadosBaseDTO",
    "PedidosComprasDadosDTO",
    "PedidosComprasGetResponse200",
    "PedidosComprasIdPedidoCompraGetResponse200",
    "PedidosComprasIdPedidoCompraPutRequest",
    "PedidosComprasIdPedidoCompraPutResponse200",
    "PedidosComprasPostRequest",
    "PedidosComprasPostResponse201",
    "PropostasComerciaisDeleteResponse200",
    "PropostasComerciaisGetResponse200",
    "PropostasComerciaisIdPropostaComercialGetResponse200",
    "PropostasComerciaisPostRequest",
    "PropostasComerciaisPostResponse201",
    "SituacoesDTO",
    "SituacoesDadosDTO",
    "SituacoesModuloDTO",
    "SituacoesTransicaoDTO",
    "VendedoresDadosBaseDTO",
    "VendedoresDadosDTO",
    "VendedoresGetResponse200",
    "VendedoresIdVendedorGetResponse200",
]
