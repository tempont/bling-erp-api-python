"""Stable model aliases for public export."""

from bling_erp_api.models.generated.propostas_comerciais import (
    OrcamentosDadosBaseDTO,
    OrcamentosDadosDTO,
    OrcamentosSituacaoDTO,
    PropostasComerciaisGetResponse200,
    PropostasComerciaisIdPropostaComercialGetResponse200,
    PropostasComerciaisPostRequest,
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
    "PropostasComerciaisGetResponse200",
    "PropostasComerciaisIdPropostaComercialGetResponse200",
    "PropostasComerciaisPostRequest",
]
