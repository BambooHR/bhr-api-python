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
│   ├── api_helper.py           # Retry logic & logging utilities
│   └── api_error_helper.py    # Error catalog & exception factory
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

## SDK Features

The BambooHR Python SDK includes the following built-in features:

### Retry with Exponential Backoff

All API requests are automatically retried on transient failures. Configure via `Configuration`:

```python
from bamboohr_sdk import Configuration

config = Configuration(
    host="https://api.bamboohr.com",
    retries=3,                              # 0-5, default 1
    retryable_status_codes=[408, 429, 504],  # default: [408, 429, 504, 598]
)
```

### HTTPS Enforcement

All host URLs are automatically upgraded to HTTPS. Setting `host="http://..."` or `host="example.com"` will both resolve to `https://...`.

### Custom User-Agent

All requests include the header `User-Agent: BHR-SDK/{version}/Python`.

### Request ID Support

Exceptions automatically extract the request ID from response headers (`x-request-id`, `x-bamboohr-request-id`, or `request-id`) for easier debugging:

```python
try:
    api.some_endpoint()
except ApiException as e:
    print(e.request_id)  # Extracted from response headers
```

### Secure Logging

The SDK uses Python's `logging` module under the `bamboohr_sdk` logger name. Sensitive headers (Authorization, API keys, cookies) and URL query parameters are automatically redacted in log output.

```python
import logging
logging.getLogger("bamboohr_sdk").setLevel(logging.DEBUG)
```

### Raw Response for Void Endpoints

Endpoints without a defined return type return an `ApiResponse` object instead of `None`, giving access to status code, headers, and raw response data.

## License

MIT
