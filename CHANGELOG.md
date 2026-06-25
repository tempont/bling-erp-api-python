# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Breaking Changes

- `VendedoresResource.list()` parameter names changed from Portuguese to English
- 408 status code reclassified from `BlingValidationError` to `BlingTransportError`
- `NotificacoesResource.alterar()` renamed to `confirmar_leitura()` (`alterar()` is now a compatibility alias)
- `HomologationResource.set_status()` renamed to `update_status()` (`set_status()` is now a compatibility alias)
- `to_json_object()` no longer drops explicitly-set default values

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
