# CLAUDE.md

# Project Overview
- Project name: BambooHR Python SDK
- What it does: Official Python SDK providing a type-safe, Pythonic interface to the BambooHR REST API with auto-generated client classes, fluent builder pattern, automatic token refresh, and retry logic
- Primary language: Python 3.10+

# Tech Stack
- Framework: Client SDK (no web framework); fluent builder pattern wrapping auto-generated OpenAPI client
- HTTP client: httpx (primary), urllib3 (fallback)
- Validation/Models: Pydantic v2
- Testing: pytest, pytest-asyncio, pytest-cov
- Linting: ruff; Type checking: mypy (strict mode)
- Code generation: OpenAPI Generator with custom Mustache templates in `templates-python/` (these templates inject retry logic, request ID tracking, OAuth middleware, etc. into the generated output)

# File Structure
- Hand-written source: `bamboohr_sdk/client/` (auth, builder, middleware, logging)
- Auto-generated APIs: `bamboohr_sdk/api/` — do NOT edit directly
- Auto-generated models: `bamboohr_sdk/models/` — do NOT edit directly
- Shared helpers: `bamboohr_sdk/exceptions.py`, `bamboohr_sdk/api_helper.py`, `bamboohr_sdk/api_error_helper.py`
- Tests: `tests/` (hand-written); `test/` (auto-generated stubs — mostly ignored)
- Examples: `examples/` — 7 progressive usage examples (see `07_testing_patterns.py` for mocking/testing guidance)
- Scripts: `scripts/` — post-generation scripts (`post_generate.py`, `update_error_docs.py`, `generate_exceptions.py`, etc.)
- Config: `pyproject.toml`

# Development Commands
```bash
make generate              # Generate SDK from OpenAPI spec (override with OPENAPI_SPEC_PATH=...)
make clean                 # Remove generated files (preserves manual_api.py)
make cleanup-obsolete      # Remove files in old manifest no longer in new manifest
make generate-error-docs   # Regenerate exception classes and error catalog
make test                  # Run pytest + classify_semver.sh bash tests
make lint                  # Run ruff linter
make format                # Run ruff formatter
make typecheck             # Run mypy
make classify-semver OLD=specs/public.yaml NEW=/tmp/new.yaml           # Classify semver bump
make classify-semver OLD=specs/public.yaml NEW=/tmp/new.yaml APPLY=true  # Classify + bump version
```

> **Note:** There are no GitHub Actions workflows yet. Run `make lint`, `make typecheck`, and `make test` locally before pushing.

# SDK Generation Pipeline

The SDK is auto-generated from `specs/public.yaml` using OpenAPI Generator. `make generate` runs the generator then calls `scripts/post_generate.py` for cleanup.

**Semver classification** (`scripts/classify_semver.sh`) — compares two OpenAPI specs using `oasdiff` and outputs a bump level (`major` / `minor` / `patch` / `none`). Used in the automated release pipeline (epic SPN-2923).

```bash
# Dependencies: brew install oasdiff jq
bash scripts/classify_semver.sh OLD_SPEC NEW_SPEC           # classify only
bash scripts/classify_semver.sh --apply OLD_SPEC NEW_SPEC   # classify + bump pyproject.toml
```

Classification rules (highest wins):
- `oasdiff breaking --fail-on ERR` exits 1 → **major**
- changelog level 3 (ERR) → **major** (safety net)
- changelog level 2 (WARN) → **minor**
- changelog level 1 (INFO) additive/unknown → **minor**; deprecations only → **patch**
- `--apply` bumps `pyproject.toml` for all levels including major

`scripts/oasdiff-severity-levels.txt` suppresses scope-change noise (~34 false-positive entries on every diff). Do NOT add `#` comments to this file — oasdiff will reject it. See `scripts/README.md` for full research notes.

# Conventions
- snake_case for functions/variables, PascalCase for classes; API classes suffixed with `Api`
- All hand-written code must pass `mypy --strict`; auto-generated code has relaxed mypy rules (see `pyproject.toml`)
- Line length: 120 chars; double quotes (enforced by ruff)
- All public methods require type annotations and docstrings with `:param:`, `:return:`, `:raises:` sections
- Logging: use logger name `"bamboohr_sdk"`; `SecureLogFilter` (a standard `logging.Filter`) is attached automatically via `.with_logging(secure=True)` (the default) to redact credentials from log output
- Exception variables: use descriptive names (e.g., `authFailedException`), never `e`

# Constraints
- Most files in `bamboohr_sdk/api/` and `bamboohr_sdk/models/` are **auto-generated** — edits are lost on `make generate`
- To preserve a file across regeneration, add it to `.openapi-generator-ignore`
- Only `bamboohr_sdk/api/manual_api.py` is hand-written inside `api/`
- Do not add dependencies without discussion; runtime deps are intentionally minimal (httpx, pydantic, python-dateutil, urllib3)
- Minimum Python version is 3.10; use `from __future__ import annotations` in new files

# Common Patterns

## Fluent Builder
```python
BambooHRClient().with_api_key("key").for_company("acme").with_retries(3).build()
```

All builder methods:
- `.with_api_key(key)` / `.with_oauth(access, refresh, expires_at)`
- `.for_company(subdomain)`
- `.with_retries(n)` — max 5; automatic on 408/429/504/598 with exponential backoff
- `.on_token_refresh(callback)` — callback receives `(new_access, new_refresh, old_access, old_refresh)`
- `.with_timeout(seconds)` — float or `(connect, read)` tuple
- `.with_host(url)` — override API base URL
- `.with_debug(True)` — enable debug mode
- `.with_http_client(client)` — inject a custom `ApiClient`
- `.with_logging(secure=True)` — attach `SecureLogFilter` (default on)

## API Access
`client.employees()` returns an `EmployeesApi` instance — never instantiate API classes directly.

Available accessors: `employees`, `time_off`, `benefits`, `reports`, `tabular_data`, `photos`, `webhooks`, `goals`, `training`, `time_tracking`, `account_information`, `applicant_tracking`, `company_files`, `employee_files`, `custom_reports`, `datasets`, `hours`, `last_change_information`, `login`, `manual`

## Custom / Unsupported Endpoints
Use `client.manual()` (returns `ManualApi`) to call endpoints not yet in the generated SDK. Inherits all SDK auth, retry, and logging behavior.

## Exception Handling
Catch specific subclasses before broad `ApiException`; extract `request_id` for tracing:
```python
except AuthenticationFailedException as authFailedException: ...
except ResourceNotFoundException as notFoundException: ...
except ApiException as apiException:
    trace = apiException.request_id
```

Full hierarchy:
```
ApiException (base)
├── ClientException (4xx)
│   ├── BadRequestException (400)
│   ├── AuthenticationFailedException (401)
│   ├── PermissionDeniedException (403)
│   ├── ResourceNotFoundException (404)
│   ├── MethodNotAllowedException (405)
│   ├── ConflictException (409)
│   ├── PayloadTooLargeException (413)
│   ├── UnsupportedMediaTypeException (415)
│   ├── UnprocessableEntityException (422)
│   └── RateLimitExceededException (429)
└── ServerException (5xx)
    ├── InternalServerErrorException (500)
    ├── NotImplementedException (501)
    ├── BadGatewayException (502)
    ├── ServiceUnavailableException (503)
    └── GatewayTimeoutException (504)
```

## OAuth Token Refresh
Two refresh modes:
- **Proactive**: tokens are refreshed 5 minutes before expiry
- **Reactive**: a 401 response triggers an immediate refresh + single retry (guarded against recursion)

## Request ID Tracking
`client.last_request_id` exposes the `x-request-id` header from the most recent response (thread-safe via `threading.local`). Use for tracing and debugging.

## Pydantic Models
All use `ConfigDict(populate_by_name=True)` for camelCase↔snake_case alias support; serialize with `.to_dict()` / `.to_json()`.

## Testing
See `examples/07_testing_patterns.py` for mocking strategy, error path testing, and integration test patterns. Use `unittest.mock` to patch the generated API classes — do not make real HTTP calls in unit tests.
