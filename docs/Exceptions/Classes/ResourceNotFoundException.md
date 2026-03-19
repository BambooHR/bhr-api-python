# ResourceNotFoundException

**Module**: `bamboohr_sdk.exceptions`
**Extends**: `ClientException`
**HTTP Status Code**: 404

## Description

Resource not found

## Usage

```python
from bamboohr_sdk.exceptions import ResourceNotFoundException

try:
    # API call that might fail with 404 status code
    client.employees().get_employees_directory()
except ResourceNotFoundException as e:
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

- The requested resource does not exist
- Resource may have been deleted
- Incorrect resource identifier or path

## Debugging Tips

- Verify the resource ID or path is correct
- Check if the resource exists before attempting to access it
- Ensure you are using the correct API version
- Confirm the resource has not been deleted or archived

## Constructor

```python
ResourceNotFoundException(
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
