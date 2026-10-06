.PHONY: check build codegen codegen-check deploy sync

UV := uv
UV_RUN := $(UV) run --all-groups
GENERATED_DIRS := src/bling_erp_api/models/generated src/bling_erp_api/contracts/generated docs/resources
UNTRACKED_GENERATED := git ls-files --others --exclude-standard -- $(GENERATED_DIRS)

sync:
	$(UV) sync --all-groups

check: sync
	$(UV_RUN) ruff check .
	$(UV_RUN) ruff format --check .
	$(UV_RUN) basedpyright
	$(UV_RUN) python -m pytest

codegen:
	$(UV_RUN) python scripts/generate_models.py
	$(UV_RUN) python scripts/generate_openapi_contracts.py

codegen-check:
	@if $(UNTRACKED_GENERATED) | grep -q .; then \
		echo "ERROR: untracked files detected in generated directories:" >&2; \
		$(UNTRACKED_GENERATED) >&2; \
		echo "Run 'make codegen' and commit the generated artifacts." >&2; \
		exit 1; \
	fi
	$(MAKE) codegen
	git diff --exit-code -- $(GENERATED_DIRS)
	@if $(UNTRACKED_GENERATED) | grep -q .; then \
		echo "ERROR: codegen produced files that are not tracked by git:" >&2; \
		$(UNTRACKED_GENERATED) >&2; \
		echo "Run 'make codegen' and commit the generated artifacts." >&2; \
		exit 1; \
	fi

build:
	$(UV) build

deploy: build
	$(UV) publish
