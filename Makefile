.PHONY: check build codegen codegen-check deploy sync

UV := uv

sync:
	$(UV) sync --all-groups

check: sync
	$(UV) run ruff check .
	$(UV) run ruff format --check .
	$(UV) run basedpyright
	$(UV) run python -m pytest

codegen:
	$(UV) run --group codegen python scripts/generate_models.py
	$(UV) run python scripts/generate_openapi_contracts.py

codegen-check: codegen
	git diff --exit-code -- src/bling_erp_api/models/generated src/bling_erp_api/contracts/generated docs/resources

build:
	$(UV) build

deploy: build
	$(UV) publish
