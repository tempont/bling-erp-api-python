.PHONY: check build deploy sync

UV := uv

sync:
	$(UV) sync --all-groups

check: sync
	$(UV) run ruff check .
	$(UV) run ruff format --check .
	$(UV) run basedpyright
	$(UV) run python -m pytest

build:
	$(UV) build

deploy: build
	$(UV) publish
