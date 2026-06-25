# Contributing

Thank you for considering contributing to the Bling ERP API SDK!

## Development Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/tempont/bling-erp-api-python.git
   cd bling-erp-api-python
   ```

2. Install dependencies with `uv`:

   ```bash
   uv sync --all-groups
   ```

3. Run the full check suite to verify everything works:

   ```bash
   make check
   ```

## Code Style

This project uses:

- **Ruff** for linting and formatting (see `pyproject.toml` for configuration)
- **basedpyright** for type checking (strict mode)

Run linting and formatting before committing:

```bash
uv run ruff check . && uv run ruff format --check .
```

Or let pre-commit handle it:

```bash
uv run pre-commit run --all-files
```

## Code Generation

Some models and contracts are generated from the Bling OpenAPI specification:

```bash
make codegen
```

This runs the scripts under `scripts/`:

- `generate_openapi_contracts.py` — generates resource contracts
- `generate_models.py` — generates Pydantic models

Generated files live in:

- `src/bling_erp_api/contracts/generated/`
- `src/bling_erp_api/models/generated/`
- `docs/resources/`

## Testing

Run the test suite:

```bash
uv run python -m pytest
```

Or with coverage:

```bash
uv run python -m pytest --cov=bling_erp_api
```

**Important**: Tests must not make real API calls unless explicitly gated behind environment variables. Use `pytest-httpx` for HTTP mocking.

## Adding a New Endpoint

Follow the checklist in `AGENTS.md` (located in the repository root) for adding new endpoints. The key steps are:

1. Find the operation in `specs/bling-openapi-reference.json`
2. Add resource/action mappings to `scripts/generate_openapi_contracts.py`
3. Run contract generation
4. Create or update the resource class in `src/bling_erp_api/resources/`
5. Add the resource namespace to the client
6. Add tests (contract tests, resource mapping tests, model tests)

## Pull Request Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/my-feature`)
3. Make your changes
4. Run `make check` to verify
5. Commit with a clear message
6. Push and open a pull request

## Project Conventions

For deep conventions on naming, docstrings, model structure, and resource implementation, see the `AGENTS.md` file in the repository root. It documents the complete project design decisions and per-endpoint checklist.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
