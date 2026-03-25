# Getting Started with the BambooHR Python SDK

This guide walks you through installing the SDK, configuring authentication, and making your first API call.

## Table of Contents

- [Installation](#installation)
- [Authentication Setup](#authentication-setup)
- [Your First API Call](#your-first-api-call)
- [Configuration Options](#configuration-options)

---

## Installation

Install the SDK from PyPI:

```bash
pip install bamboohr-python
```

**Requirements:** Python 3.10+

The SDK depends on `httpx` (HTTP client) and `pydantic` (model validation). These are installed automatically.

> **Note:** On macOS and some Linux distributions, the system Python installation may be externally managed. If `pip install` fails with a message about managed environments, create a virtual environment first:
> ```bash
> python3 -m venv .venv
> source .venv/bin/activate
> pip install bamboohr-python
> ```

---

## Authentication Setup

The SDK supports two authentication methods. **OAuth 2.0 is recommended for all partner integrations.** See [AUTHENTICATION.md](AUTHENTICATION.md) for full details.

### OAuth 2.0 (Recommended)

Use an OAuth access token obtained through the BambooHR authorization flow:

```python
client = (
    BambooHRClient()
    .with_oauth("your-access-token")
    .for_company("your-company-subdomain")
    .build()
)
```

`for_company("acme")` sets the host to `https://acme.bamboohr.com`. Replace `"acme"` with your company's BambooHR subdomain.

For production integrations, use `with_oauth_refresh()` so the SDK handles token expiration automatically. See [AUTHENTICATION.md](AUTHENTICATION.md) for the full authorization code flow and token refresh setup.

### API Key

API key authentication is available for internal tooling, quick prototyping, or automated scripts where OAuth is not practical. Generate an API key in BambooHR under **Account > API Keys**.

```python
from bamboohr_sdk.client import BambooHRClient

client = (
    BambooHRClient()
    .with_api_key(os.environ["BAMBOO_API_KEY"])
    .for_company("your-company-subdomain")
    .build()
)
```

---

## Your First API Call

### Fetch the Employee Directory

The employee directory is a good starting point — it requires no prior knowledge of employee IDs.

```python
import os
from bamboohr_sdk.client import BambooHRClient
from bamboohr_sdk.exceptions import ApiException, AuthenticationFailedException

client = (
    BambooHRClient()
    .with_api_key(os.environ["BAMBOO_API_KEY"])
    .for_company(os.environ["BAMBOO_COMPANY"])
    .build()
)

try:
    directory = client.employees().get_employees_directory()
    employees = directory.employees or []
    print(f"Found {len(employees)} employees")
    for emp in employees[:5]:
        print(f"  {emp.get('displayName')} — {emp.get('department')}")

except AuthenticationFailedException:
    print("Authentication failed. Check your API key and company subdomain.")

except ApiException as e:
    print(f"API error ({e.status}): {e.reason}")
    if e.request_id:
        print(f"Request ID: {e.request_id}")
```

**Best practice:** Always load credentials from environment variables — never hardcode them.

### Fetch a Single Employee

The `get_employee` endpoint accepts a `fields` parameter specifying which fields to return. The response is deserialized into an `Employee` model that exposes `first_name` and `last_name`. Additional requested fields are available in the raw response body but are not mapped to typed attributes on the model.

```python
employee = client.employees().get_employee(
    id="123",
    fields="firstName,lastName",
)
print(f"{employee.first_name} {employee.last_name}")
```

Pass `id="0"` to fetch the employee associated with the API key.

### Access Other APIs

All APIs are available as methods on the client:

```python
# Time off requests
time_off = client.time_off().get_time_off_requests(
    start="2024-01-01",
    end="2024-12-31",
    status="approved",
)

# Run a report
report = client.reports().get_company_report(id="12345", format="json")

# List webhooks
webhooks = client.webhooks().get_webhooks()
```

For a complete list of available API methods, see the [API Reference](docs/) or browse the [examples](examples/).

---

## Configuration Options

All configuration is set through the `BambooHRClient` builder before calling `.build()`.

### Retries

The SDK automatically retries on HTTP 408, 429, 504, and 598 responses using exponential backoff (100 ms, 200 ms, 400 ms, …):

```python
client = (
    BambooHRClient()
    .with_api_key("your-api-key")
    .for_company("your-company")
    .with_retries(3)  # 0–5, default 1
    .build()
)
```

### Timeout

```python
client = (
    BambooHRClient()
    .with_api_key("your-api-key")
    .for_company("your-company")
    .with_timeout(30.0)          # 30 seconds for all operations
    # or
    .with_timeout((5.0, 30.0))   # (connect timeout, read timeout)
    .build()
)
```

### Logging

Enable SDK logging to see request/response details. Sensitive values (tokens, API keys, Authorization headers) are automatically redacted:

```python
import logging
from bamboohr_sdk.client import BambooHRClient

client = (
    BambooHRClient()
    .with_api_key("your-api-key")
    .for_company("your-company")
    .with_logging(level=logging.DEBUG)  # or logging.INFO
    .build()
)
```

Alternatively, configure the logger directly:

```python
import logging
logging.getLogger("bamboohr_sdk").setLevel(logging.DEBUG)
```

### Custom Host

Override the default host URL (useful for testing or proxying):

```python
client = (
    BambooHRClient()
    .with_api_key("your-api-key")
    .with_host("https://custom.bamboohr.com")
    .build()
)
```

### Accessing Any API Class

Use `get_api()` to access any generated API class not exposed as a named accessor:

```python
from bamboohr_sdk.api.webhook_events_api import WebhookEventsApi

events_api = client.get_api(WebhookEventsApi)
```

---

## Error Handling

The SDK raises typed exceptions for each HTTP status code. Catch the specific type you want to handle, and fall back to `ApiException` for everything else:

```python
from bamboohr_sdk.exceptions import (
    ApiException,
    AuthenticationFailedException,   # 401
    PermissionDeniedException,        # 403
    ResourceNotFoundException,        # 404
    RateLimitExceededException,       # 429
)

try:
    employee = client.employees().get_employee(id="123", fields="firstName")

except AuthenticationFailedException:
    print("Invalid credentials.")

except PermissionDeniedException:
    print("Insufficient permissions.")

except ResourceNotFoundException:
    print("Employee not found.")

except RateLimitExceededException:
    print("Rate limit hit — the SDK will retry automatically if retries > 0.")

except ApiException as e:
    print(f"Unexpected error ({e.status}): {e.reason}")
    if e.request_id:
        print(f"Request ID (include in support requests): {e.request_id}")
```

For the full exception hierarchy and all status codes, see `bamboohr_sdk/exceptions.py`.

---

## Next Steps

- [AUTHENTICATION.md](AUTHENTICATION.md) — OAuth 2.0, automatic token refresh, security best practices
- [examples/](examples/) — runnable examples covering all major patterns
- [BambooHR API documentation](https://documentation.bamboohr.com/docs/getting-started)
- [Webhooks guide](https://documentation.bamboohr.com/docs/webhooks)
