# BambooHR Python SDK

Official Python SDK for the [BambooHR API](https://documentation.bamboohr.com).

## Requirements

- Python 3.10+

## Installation

```bash
pip install bamboohr-sdk
```

### Development Setup

```bash
# Clone the repository
git clone https://github.com/BambooHR/bhr-api-python.git
cd bhr-api-python

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install with dev dependencies
pip install -e ".[dev]"
```

## Development

### Linting & Formatting

```bash
# Check linting
ruff check bamboohr_sdk/ tests/

# Auto-fix linting issues
ruff check --fix bamboohr_sdk/ tests/

# Format code
ruff format bamboohr_sdk/ tests/
```

### Type Checking

```bash
mypy bamboohr_sdk/
```

### Testing

```bash
pytest
```

## Project Structure

```
bhr-api-python/
├── bamboohr_sdk/               # Main package
│   ├── api/                    # Auto-generated API classes
│   ├── models/                 # Auto-generated data models
│   ├── client/                 # Custom API client & auth
│   │   ├── auth/               # TokenManager, RefreshProvider
│   │   ├── middleware/         # OAuth2, RequestId middleware
│   │   └── logger/            # SecureLogger
│   └── exceptions/            # Custom exception hierarchy
├── test/                       # Auto-generated API test stubs
├── tests/                      # Custom hand-written tests
├── docs/                       # Auto-generated API documentation
├── templates-python/           # Custom openapi-generator templates
├── scripts/                    # Post-generation scripts
├── examples/                   # Usage examples
└── pyproject.toml              # Project configuration
```

### Protecting Implemented Tests

The `test/` directory contains auto-generated API test stubs created by `make generate`.
These stubs are overwritten on each regeneration. Once you implement real test logic in a
test file, add it to `.openapi-generator-ignore` to prevent it from being overwritten:

```
# .openapi-generator-ignore
test/test_employees_api.py
test/test_time_tracking_api.py
```

This ensures your implemented tests survive regeneration while new API test stubs are still
generated for any newly added APIs.

## License

MIT
