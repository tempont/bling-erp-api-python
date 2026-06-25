"""Stable model aliases for public export."""

# Products
# Ad categories
from bling_erp_api.models.generated.ad_categories import (
    AnunciosCategoriaDTO,
    AnunciosCategoriasGetResponse200,
    AnunciosCategoriasIdCategoriaGetResponse200,
)

# Ads
from bling_erp_api.models.generated.ads import (
    AnunciosGetAllResponseDTO,
    AnunciosGetByIdResponseDTO,
    AnunciosGetResponse200,
    AnunciosIdAnuncioGetResponse200,
    AnunciosPostResponse201,
    AnunciosSaveRequest,
    AnunciosSaveResponseDTO,
)

# Contacts
from bling_erp_api.models.generated.contacts import (
    ContatosDadosBaseDTO,
    ContatosDadosDTO,
    ContatosDeleteResponse200,
    ContatosGetResponse200,
    ContatosIdContatoGetResponse200,
    ContatosIdContatoPutRequest,
    ContatosPostRequest,
    ContatosPostResponse201,
    ContatosSituacoesPostRequest,
    ContatosSituacoesPostResponse200,
)

# Contas a pagar
from bling_erp_api.models.generated.contas_pagar import (
    ContasBaixarContaDTO,
    ContasDadosBaseDTO,
    ContasPagarDadosDTO,
    ContasPagarDadosPostDTO,
    ContasPagarGetResponse200,
    ContasPagarIdContaPagarGetResponse200,
    ContasPagarIdContaPagarPutRequest,
    ContasPagarIdContaPagarPutResponse200,
    ContasPagarPostRequest,
    ContasPagarPostResponse201,
)

# Contas a receber
from bling_erp_api.models.generated.contas_receber import (
    ContasReceberBoletosCancelarDTO,
    ContasReceberDadosBaseDTO,
    ContasReceberDadosDTO,
    ContasReceberDadosListDTO,
    ContasReceberGetResponse200,
    ContasReceberIdContaReceberGetResponse200,
    ContasReceberIdContaReceberPutRequest,
    ContasReceberPostRequest,
    ContasReceberPostResponse201,
)

# Homologation
from bling_erp_api.models.generated.homologation import (
    HomologacaoDadosBaseDTO,
    HomologacaoDadosDTO,
    HomologacaoProdutosGetResponse200,
    HomologacaoProdutosPostResponse201,
)
from bling_erp_api.models.generated.invoices import (
    NfceGetResponse200,
    NfceIdNotaFiscalConsumidorEnviarPostResponse200,
    NfceIdNotaFiscalConsumidorGetResponse200,
    NfceIdNotaFiscalConsumidorPutRequest,
    NfceIdNotaFiscalConsumidorPutResponse200,
    NfcePostRequest,
    NfcePostResponse201,
    NfeDeleteResponse200,
    NfeDocumentoChaveAcessoGetResponse200,
    NfeGetResponse200,
    NfeIdNotaFiscalEnviarPostResponse200,
    NfeIdNotaFiscalGetResponse200,
    NfeIdNotaFiscalPutRequest,
    NfeIdNotaFiscalPutResponse200,
    NfePostRequest,
    NfePostResponse201,
    NotaFiscalResponsePOST,
    NotasFiscaisDadosBaseDTO,
)

# NFSe
from bling_erp_api.models.generated.nfse import (
    NfseGetResponse200,
    NfseIdNotaServicoEnviarPostResponse200,
    NfseIdNotaServicoGetResponse200,
    NfsePostRequest,
    NfsePostResponse201,
    NotasServicosDadosBaseDTO,
    NotasServicosDadosDTO,
    NotasServicosResponsePOSTPUT,
)
from bling_erp_api.models.generated.products import (
    ProdutosDadosBaseDTO,
    ProdutosDadosDTO,
    ProdutosDeleteResponse200,
    ProdutosGetResponse200,
    ProdutosIdProdutoGetResponse200,
    ProdutosIdProdutoSituacoesPatchRequest,
    ProdutosResponsePOSTPUT,
    ProdutosSituacoesPostRequest,
    ProdutosSituacoesPostResponse200,
)

# Commercial proposals
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

# Purchase orders
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

# Sales orders
from bling_erp_api.models.generated.sales_orders import (
    PedidosVendasDeleteResponse200,
    PedidosVendasGetResponse200,
    PedidosVendasIdPedidoVendaGetResponse200,
    PedidosVendasIdPedidoVendaPutRequest,
    PedidosVendasIdPedidoVendaPutResponse200,
    PedidosVendasPostRequest,
    PedidosVendasPostResponse201,
    VendasDadosBaseDTO,
    VendasDadosDTO,
    VendasResponsePOSTPUT,
)

# Situations
from bling_erp_api.models.generated.situacoes import (
    SituacoesDadosDTO,
    SituacoesDTO,
    SituacoesIdSituacaoGetResponse200,
    SituacoesIdSituacaoPutRequest,
    SituacoesIdSituacaoPutResponse200,
    SituacoesPostRequest,
    SituacoesPostResponse201,
)
from bling_erp_api.models.generated.situacoes_modulos import (
    SituacoesModuloDTO,
)
from bling_erp_api.models.generated.situacoes_transicoes import (
    SituacoesTransicaoDTO,
)

# Vendedores
from bling_erp_api.models.generated.vendedores import (
    VendedoresDadosBaseDTO,
    VendedoresDadosDTO,
    VendedoresGetResponse200,
    VendedoresIdVendedorGetResponse200,
)

__all__ = [
    "AnunciosCategoriaDTO",
    "AnunciosCategoriasGetResponse200",
    "AnunciosCategoriasIdCategoriaGetResponse200",
    "AnunciosGetAllResponseDTO",
    "AnunciosGetByIdResponseDTO",
    "AnunciosGetResponse200",
    "AnunciosIdAnuncioGetResponse200",
    "AnunciosPostResponse201",
    "AnunciosSaveRequest",
    "AnunciosSaveResponseDTO",
    "ContasBaixarContaDTO",
    "ContasDadosBaseDTO",
    "ContasPagarDadosDTO",
    "ContasPagarDadosPostDTO",
    "ContasPagarGetResponse200",
    "ContasPagarIdContaPagarGetResponse200",
    "ContasPagarIdContaPagarPutRequest",
    "ContasPagarIdContaPagarPutResponse200",
    "ContasPagarPostRequest",
    "ContasPagarPostResponse201",
    "ContasReceberBoletosCancelarDTO",
    "ContasReceberDadosBaseDTO",
    "ContasReceberDadosDTO",
    "ContasReceberDadosListDTO",
    "ContasReceberGetResponse200",
    "ContasReceberIdContaReceberGetResponse200",
    "ContasReceberIdContaReceberPutRequest",
    "ContasReceberPostRequest",
    "ContasReceberPostResponse201",
    "ContatosDadosBaseDTO",
    "ContatosDadosDTO",
    "ContatosDeleteResponse200",
    "ContatosGetResponse200",
    "ContatosIdContatoGetResponse200",
    "ContatosIdContatoPutRequest",
    "ContatosPostRequest",
    "ContatosPostResponse201",
    "ContatosSituacoesPostRequest",
    "ContatosSituacoesPostResponse200",
    "HomologacaoDadosBaseDTO",
    "HomologacaoDadosDTO",
    "HomologacaoProdutosGetResponse200",
    "HomologacaoProdutosPostResponse201",
    "NfceGetResponse200",
    "NfceIdNotaFiscalConsumidorEnviarPostResponse200",
    "NfceIdNotaFiscalConsumidorGetResponse200",
    "NfceIdNotaFiscalConsumidorPutRequest",
    "NfceIdNotaFiscalConsumidorPutResponse200",
    "NfcePostRequest",
    "NfcePostResponse201",
    "NfeDeleteResponse200",
    "NfeDocumentoChaveAcessoGetResponse200",
    "NfeGetResponse200",
    "NfeIdNotaFiscalEnviarPostResponse200",
    "NfeIdNotaFiscalGetResponse200",
    "NfeIdNotaFiscalPutRequest",
    "NfeIdNotaFiscalPutResponse200",
    "NfePostRequest",
    "NfePostResponse201",
    "NfseGetResponse200",
    "NfseIdNotaServicoEnviarPostResponse200",
    "NfseIdNotaServicoGetResponse200",
    "NfsePostRequest",
    "NfsePostResponse201",
    "NotaFiscalResponsePOST",
    "NotasFiscaisDadosBaseDTO",
    "NotasServicosDadosBaseDTO",
    "NotasServicosDadosDTO",
    "NotasServicosResponsePOSTPUT",
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
    "PedidosVendasDeleteResponse200",
    "PedidosVendasGetResponse200",
    "PedidosVendasIdPedidoVendaGetResponse200",
    "PedidosVendasIdPedidoVendaPutRequest",
    "PedidosVendasIdPedidoVendaPutResponse200",
    "PedidosVendasPostRequest",
    "PedidosVendasPostResponse201",
    "ProdutosDadosBaseDTO",
    "ProdutosDadosDTO",
    "ProdutosDeleteResponse200",
    "ProdutosGetResponse200",
    "ProdutosIdProdutoGetResponse200",
    "ProdutosIdProdutoSituacoesPatchRequest",
    "ProdutosResponsePOSTPUT",
    "ProdutosSituacoesPostRequest",
    "ProdutosSituacoesPostResponse200",
    "PropostasComerciaisDeleteResponse200",
    "PropostasComerciaisGetResponse200",
    "PropostasComerciaisIdPropostaComercialGetResponse200",
    "PropostasComerciaisPostRequest",
    "PropostasComerciaisPostResponse201",
    "SituacoesDTO",
    "SituacoesDadosDTO",
    "SituacoesIdSituacaoGetResponse200",
    "SituacoesIdSituacaoPutRequest",
    "SituacoesIdSituacaoPutResponse200",
    "SituacoesModuloDTO",
    "SituacoesPostRequest",
    "SituacoesPostResponse201",
    "SituacoesTransicaoDTO",
    "VendasDadosBaseDTO",
    "VendasDadosDTO",
    "VendasResponsePOSTPUT",
    "VendedoresDadosBaseDTO",
    "VendedoresDadosDTO",
    "VendedoresGetResponse200",
    "VendedoresIdVendedorGetResponse200",
]
