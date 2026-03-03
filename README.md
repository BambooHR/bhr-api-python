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
ruff check src/ tests/

# Auto-fix linting issues
ruff check --fix src/ tests/

# Format code
ruff format src/ tests/
```

### Type Checking

```bash
mypy src/bamboohr_sdk/
```

### Testing

```bash
pytest
```

## Project Structure

```
bhr-api-python/
├── src/
│   └── bamboohr_sdk/           # Main package
│       ├── api/                 # Auto-generated API classes
│       ├── model/               # Auto-generated data models
│       ├── client/              # Custom API client & auth
│       │   ├── auth/            # TokenManager, RefreshProvider
│       │   ├── middleware/      # OAuth2, RequestId middleware
│       │   └── logger/         # SecureLogger
│       └── exceptions/         # Custom exception hierarchy
├── templates-python/            # Custom openapi-generator templates
├── scripts/                     # Post-generation scripts
├── tests/                       # Test suite
├── examples/                    # Usage examples
└── pyproject.toml               # Project configuration
```

## License

MIT
