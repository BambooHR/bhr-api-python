# UnsupportedMediaTypeException

**Module**: `bamboohr_sdk.exceptions`
**Extends**: `ClientException`
**HTTP Status Code**: 415

## Description

Unsupported media type

## Usage

```python
from bamboohr_sdk.exceptions import UnsupportedMediaTypeException

try:
    # API call that might fail with 415 status code
    client.employees().get_employees_directory()
except UnsupportedMediaTypeException as e:
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

- Content-Type header is missing or incorrect
- Request body format is not supported by the API
- Using XML when only JSON is supported (or vice versa)

## Debugging Tips

- Check that your Content-Type header is set correctly
- Verify the API endpoint supports the format you're sending
- Convert your payload to a supported format (usually JSON)
- Review API documentation for supported media types

## Constructor

```python
UnsupportedMediaTypeException(
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
