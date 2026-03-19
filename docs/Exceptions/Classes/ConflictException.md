# ConflictException

**Module**: `bamboohr_sdk.exceptions`
**Extends**: `ClientException`
**HTTP Status Code**: 409

## Description

Conflict

## Usage

```python
from bamboohr_sdk.exceptions import ConflictException

try:
    # API call that might fail with 409 status code
    client.employees().get_employees_directory()
except ConflictException as e:
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

- Resource state conflict with the current request
- Concurrent modification of the same resource
- Attempting to create a resource that already exists
- Violating unique constraints

## Debugging Tips

- Fetch the latest state of the resource before attempting modifications
- Implement optimistic concurrency control
- Check for existing resources before creation attempts
- Handle conflict resolution in your application logic

## Constructor

```python
ConflictException(
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
