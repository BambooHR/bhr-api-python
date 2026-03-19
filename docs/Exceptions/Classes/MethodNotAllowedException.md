# MethodNotAllowedException

**Module**: `bamboohr_sdk.exceptions`
**Extends**: `ClientException`
**HTTP Status Code**: 405

## Description

Method not allowed

## Usage

```python
from bamboohr_sdk.exceptions import MethodNotAllowedException

try:
    # API call that might fail with 405 status code
    client.employees().get_employees_directory()
except MethodNotAllowedException as e:
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

- Using an incorrect HTTP method for this endpoint
- The endpoint does not support the requested operation
- API version mismatch

## Debugging Tips

- Check API documentation for the correct HTTP method (GET, POST, PUT, DELETE)
- Verify the endpoint supports the operation you are attempting
- Ensure you are using the correct API version

## Constructor

```python
MethodNotAllowedException(
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
