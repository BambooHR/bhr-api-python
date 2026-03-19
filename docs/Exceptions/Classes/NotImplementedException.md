# NotImplementedException

**Module**: `bamboohr_sdk.exceptions`
**Extends**: `ServerException`
**HTTP Status Code**: 501

## Description

Not implemented

## Usage

```python
from bamboohr_sdk.exceptions import NotImplementedException

try:
    # API call that might fail with 501 status code
    client.employees().get_employees_directory()
except NotImplementedException as e:
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

- The API endpoint does not support the requested functionality
- The feature is planned but not yet available
- Using a method that is not supported by this resource

## Debugging Tips

- Check API documentation to verify the feature is supported
- Confirm you are using the correct API version
- Consider alternative approaches to achieve your goal
- Contact support to inquire about feature availability

## Constructor

```python
NotImplementedException(
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
