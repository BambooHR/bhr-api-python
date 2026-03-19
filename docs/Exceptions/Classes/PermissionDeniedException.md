# PermissionDeniedException

**Module**: `bamboohr_sdk.exceptions`
**Extends**: `ClientException`
**HTTP Status Code**: 403

## Description

Permission denied

## Usage

```python
from bamboohr_sdk.exceptions import PermissionDeniedException

try:
    # API call that might fail with 403 status code
    client.employees().get_employees_directory()
except PermissionDeniedException as e:
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

- API key lacks required permissions
- Account restrictions in place
- IP address restrictions

## Debugging Tips

- Verify your API key has the necessary permissions
- Contact your BambooHR administrator to review API access permissions
- Check if IP restrictions are in place for API access

## Constructor

```python
PermissionDeniedException(
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
