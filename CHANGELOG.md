# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2026-06-26

### Breaking Changes

- `VendedoresResource.list()` parameter names changed from Portuguese to English
- 408 status code reclassified from `BlingValidationError` to `BlingTransportError`
- `NotificacoesResource.alterar()` renamed to `confirmar_leitura()` (`alterar()` is now a compatibility alias)
- `HomologationResource.set_status()` renamed to `update_status()` (`set_status()` is now a compatibility alias)
- `to_json_object()` no longer drops explicitly-set default values

### Added

- OpenAPI contract generator now correctly segregates NF-e and NFC-e into separate contract modules
- Usuários contracts and docs now generated
- Logistics sub-resources (serviços, objetos, etiquetas, remessas) now have separate contract modules and docs
- Full Google-style docstrings across all ~185 resource methods (Endpoint, Args with Bling notation, Returns with DTO schemas)
- All EN alias docstrings now complete with pt-BR descriptions
- New examples: AnunciosCategorias, FormasPagamentos, SituacoesTransicoes
- CODE_OF_CONDUCT.md
- BlingClient and BlingModel class docstrings enriched
- mkdocs.yml nav updated with new resource docs

### Changed

- Fixed pt-BR titles in generated docs (Situações, Pedidos de Compra, Propostas Comerciais, etc.)
- English-to-pt-BR translations in EN alias docstrings (depositos, estoques, logisticas)
- iterar/iterate docstrings standardized with Bling notation and Returns sections
- Example files converted to pt-BR canonical namespaces
- Response parsing standardized on model_validate()

### Fixed

- errors.md: 408 excluded from BlingValidationError range
- pagination.md: added 6 missing resources to autopagination table
- products.py: canonical docstrings now match AGENTS.md spec
- from_env() docstring corrected (rate limiting is enabled by default)

## [0.1.0] - 2026-06-23

### Added

- Initial public release of the Bling ERP API SDK
- 40+ resource modules covering products, orders, invoices, contacts, logistics, and more
- OAuth2 authentication via bling-jwt-auth
- Sync and async transport with rate limiting and 429 retry
- Pydantic v2 typed models with snake_case public API
- pt-BR canonical methods with English compatibility aliases
- OpenAPI contract generation and validation
- Comprehensive test suite (500+ tests)
