# HTTP Status Codes and Error Handling

This document provides information about HTTP status codes that may be returned by the BambooHR API, along with potential causes and debugging tips for each code.

## Exception Classes

The SDK provides exception classes for each HTTP status code. For detailed documentation on each exception class, see the links below:

### Base Exception
- [ApiException](Classes/ApiException.md) - Base exception class for all API errors

### Server & Client Exceptions
- [ClientException](Classes/ClientException.md) - Base class for 4xx errors
- [ServerException](Classes/ServerException.md) - Base class for 5xx errors

### Client Exceptions (4xx)
- [BadRequestException](Classes/BadRequestException.md) - 400 Bad request
- [AuthenticationFailedException](Classes/AuthenticationFailedException.md) - 401 Authentication failed
- [PermissionDeniedException](Classes/PermissionDeniedException.md) - 403 Permission denied
- [ResourceNotFoundException](Classes/ResourceNotFoundException.md) - 404 Resource not found
- [MethodNotAllowedException](Classes/MethodNotAllowedException.md) - 405 Method not allowed
- [RequestTimeoutException](Classes/RequestTimeoutException.md) - 408 Request timeout
- [ConflictException](Classes/ConflictException.md) - 409 Conflict
- [PayloadTooLargeException](Classes/PayloadTooLargeException.md) - 413 Payload too large
- [UnsupportedMediaTypeException](Classes/UnsupportedMediaTypeException.md) - 415 Unsupported media type
- [UnprocessableEntityException](Classes/UnprocessableEntityException.md) - 422 Unprocessable entity
- [RateLimitExceededException](Classes/RateLimitExceededException.md) - 429 Rate limit exceeded

### Server Exceptions (5xx)
- [InternalServerErrorException](Classes/InternalServerErrorException.md) - 500 Internal server error
- [NotImplementedException](Classes/NotImplementedException.md) - 501 Not implemented
- [BadGatewayException](Classes/BadGatewayException.md) - 502 Bad gateway
- [ServiceUnavailableException](Classes/ServiceUnavailableException.md) - 503 Service unavailable
- [GatewayTimeoutException](Classes/GatewayTimeoutException.md) - 504 Gateway timeout
- [InsufficientStorageException](Classes/InsufficientStorageException.md) - 507 Insufficient storage
- [NetworkReadTimeoutException](Classes/NetworkReadTimeoutException.md) - 598 Network read timeout

## Error Handling in the SDK

When an error occurs, the SDK will raise an exception with details about the error. The exception will include:

- The HTTP status code
- The reason phrase
- A request ID (extracted from response headers) for debugging with BambooHR support
- Potential causes and debugging tips via `potential_causes()` and `debugging_tips()` methods

The exception type will be a subclass of `ClientException` or `ServerException` based on the HTTP status code.

### Example Error Handling

```python
from bamboohr_sdk.exceptions import (
    ApiException,
    ClientException,
    ServerException,
    AuthenticationFailedException,
    ResourceNotFoundException,
)

try:
    result = client.employees().get_employees_directory()
except AuthenticationFailedException as auth_error:
    # Handle authentication errors specifically
    print(f"Auth failed: {auth_error.reason}")
    print(f"Tips: {auth_error.debugging_tips()}")
except ResourceNotFoundException as not_found_error:
    # Handle 404 errors specifically
    print(f"Not found: {not_found_error.reason}")
except ClientException as client_error:
    # Handle all other client errors (4xx status codes)
    print(f"Client error ({client_error.status}): {client_error.reason}")
except ServerException as server_error:
    # Handle server errors (5xx status codes)
    print(f"Server error ({server_error.status}): {server_error.reason}")
except ApiException as api_error:
    # Handle any other API exceptions
    print(f"API error ({api_error.status}): {api_error.reason}")
    if api_error.request_id:
        print(f"Request ID: {api_error.request_id}")
    if api_error.body:
        print(f"Response body: {api_error.body}")
```

## Automatic Retry Recommendations

- **Retry recommended**: 408, 429, 504, 598

The SDK will automatically retry requests with these status codes based on the `retries` configuration option (default: 1 retry). Configure via:

```python
client = (
    BambooHRClient()
    .with_api_key("your-api-key")
    .for_company("acme")
    .with_retries(3)  # 0–5 retries
    .build()
)
```
