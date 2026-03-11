# Makefile for BambooHR API Python SDK

# Default OpenAPI spec path - override with environment variable
OPENAPI_SPEC_PATH ?= $(shell echo ~/repos/main/docs/openapi/generated/public.yaml)

# Python interpreter
PYTHON ?= python3

# Package information
PACKAGE_NAME = bamboohr_sdk
PACKAGE_VERSION = 1.0.0
PROJECT_NAME = bamboohr-sdk
PACKAGE_URL = https://www.bamboohr.com/
DEVELOPER_URL = https://github.com/BambooHR/bhr-api-python
DEVELOPER = BambooHR
LICENSE_NAME = MIT

.PHONY: help generate clean cleanup-obsolete test lint typecheck format

help:
	@echo "BambooHR API Python SDK - Available commands:"
	@echo "  make generate          - Generate SDK code from OpenAPI spec"
	@echo "  make generate OPENAPI_SPEC_PATH=/path/to/spec.yaml - Generate using a custom spec path"
	@echo "  make clean             - Remove generated files"
	@echo "  make cleanup-obsolete  - Manually run cleanup of obsolete files"
	@echo "  make test              - Run tests"
	@echo "  make lint              - Run ruff linter"
	@echo "  make format            - Run ruff formatter"
	@echo "  make typecheck         - Run mypy type checker"

generate:
	@echo "Generating Python SDK from OpenAPI spec at $(OPENAPI_SPEC_PATH)..."
	@if [ ! -f "$(OPENAPI_SPEC_PATH)" ]; then \
		echo "Error: OpenAPI spec file not found at $(OPENAPI_SPEC_PATH)"; \
		echo "Please specify the correct path with OPENAPI_SPEC_PATH=/path/to/spec.yaml"; \
		exit 1; \
	fi
	@# Backup the current FILES manifest for cleanup comparison
	@if [ -f ".openapi-generator/FILES" ]; then \
		cp .openapi-generator/FILES .openapi-generator/FILES.old; \
	fi
	openapi-generator generate \
		-i $(OPENAPI_SPEC_PATH) \
		-g python \
		-t ./templates-python \
		--global-property modelTests=false \
		--additional-properties=packageName=$(PACKAGE_NAME),packageVersion=$(PACKAGE_VERSION),projectName=$(PROJECT_NAME),packageUrl=$(PACKAGE_URL),developerOrganization=$(DEVELOPER),developerOrganizationUrl=$(DEVELOPER_URL),licenseName=$(LICENSE_NAME)
	$(PYTHON) scripts/post_generate.py
	@echo "SDK generation complete!"

cleanup-obsolete:
	@echo "Running cleanup of obsolete files..."
	$(PYTHON) scripts/cleanup_obsolete_files.py
	@echo "Cleanup complete!"

clean:
	@echo "Cleaning generated files..."
	@# Preserve hand-written API files before wiping the directory
	@mkdir -p /tmp/bhr-sdk-preserve
	@if [ -f bamboohr_sdk/api/manual_api.py ]; then \
		cp bamboohr_sdk/api/manual_api.py /tmp/bhr-sdk-preserve/; \
	fi
	rm -rf bamboohr_sdk/api bamboohr_sdk/models docs test .openapi-generator
	@# Recreate empty directories with __init__.py
	mkdir -p bamboohr_sdk/api bamboohr_sdk/models
	echo '"""Auto-generated API classes from OpenAPI specification."""' > bamboohr_sdk/api/__init__.py
	echo '"""Auto-generated data models from OpenAPI specification."""' > bamboohr_sdk/models/__init__.py
	@# Restore hand-written API files
	@if [ -f /tmp/bhr-sdk-preserve/manual_api.py ]; then \
		cp /tmp/bhr-sdk-preserve/manual_api.py bamboohr_sdk/api/; \
		rm -rf /tmp/bhr-sdk-preserve; \
	fi
	@echo "Clean complete!"

test:
	@echo "Running tests..."
	$(PYTHON) -m pytest
	@echo "Tests complete!"

lint:
	@echo "Running ruff linter..."
	$(PYTHON) -m ruff check bamboohr_sdk/ tests/
	@echo "Lint complete!"

format:
	@echo "Running ruff formatter..."
	$(PYTHON) -m ruff format bamboohr_sdk/ tests/
	$(PYTHON) -m ruff check --fix bamboohr_sdk/ tests/
	@echo "Format complete!"

typecheck:
	@echo "Running mypy type checker..."
	$(PYTHON) -m mypy bamboohr_sdk/
	@echo "Type check complete!"
