# UnprocessableEntityException

**Module**: `bamboohr_sdk.exceptions`
**Extends**: `ClientException`
**HTTP Status Code**: 422

## Description

Unprocessable entity

## Usage

```python
from bamboohr_sdk.exceptions import UnprocessableEntityException

try:
    # API call that might fail with 422 status code
    client.employees().get_employees_directory()
except UnprocessableEntityException as e:
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

- Request syntax is correct but contains semantic errors
- Validation failures in the request data
- Business rule violations
- Data integrity constraints

## Debugging Tips

- Check the response body for specific validation error details
- Ensure request data meets all business rules and constraints
- Validate data before submitting to the API
- Review API documentation for field requirements and limitations

## Constructor

```python
UnprocessableEntityException(
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
