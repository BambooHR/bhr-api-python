# GatewayTimeoutException

**Module**: `bamboohr_sdk.exceptions`
**Extends**: `ServerException`
**HTTP Status Code**: 504

## Description

Gateway timeout

## Usage

```python
from bamboohr_sdk.exceptions import GatewayTimeoutException

try:
    # API call that might fail with 504 status code
    client.employees().get_employees_directory()
except GatewayTimeoutException as e:
    # Handle the exception
    print(e)

    # Access additional information
    causes = e.potential_causes()
    tips = e.debugging_tips()

    # Access response data
    print(f"Status: {e.status}")
    print(f"Request ID: {e.request_id}")
    if e.body:
        print(f"Response body: {e.body}")
```

## Potential Causes

- The gateway or proxy did not receive a timely response
- BambooHR servers experiencing high load
- Complex query taking too long to process

## Debugging Tips

- Retry the request after a delay
- Simplify complex queries if possible
- Implement circuit breaker pattern to prevent cascading failures

## Constructor

```python
GatewayTimeoutException(
    status=None,
    reason=None,
    http_resp=None,
    *,
    body: str | None = None,
    data: Any | None = None,
    request_id: str | None = None,
)
```

### Parameters

| Name | Type | Description |
|------|------|-------------|
| `status` | int \| None | HTTP status code |
| `reason` | str \| None | HTTP reason phrase |
| `http_resp` | RESTResponse \| None | The raw HTTP response object |
| `body` | str \| None | HTTP response body |
| `data` | Any \| None | Deserialized response data |
| `request_id` | str \| None | Request ID from response headers |

## Methods

### potential_causes()

Returns a list of potential causes for this exception.

```python
@staticmethod
def potential_causes() -> list[str]
```

### debugging_tips()

Returns a list of debugging tips for this exception.

```python
@staticmethod
def debugging_tips() -> list[str]
```
