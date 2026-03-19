# ClientException

**Module**: `bamboohr_sdk.exceptions`
**Extends**: `ApiException`

## Description

Base class for all client-side (4xx) exceptions.

## Usage

```python
from bamboohr_sdk.exceptions import ClientException

try:
    # API call that might fail with a 4xx status code
    client.employees().get_employees_directory()
except ClientException as e:
    # Handle any client error exception
    print(f"{type(e).__name__}: {e.status} {e.reason}")
```

## Client Exception Types

The following specific exception types extend `ClientException`:

- [BadRequestException](BadRequestException.md)
- [AuthenticationFailedException](AuthenticationFailedException.md)
- [PermissionDeniedException](PermissionDeniedException.md)
- [ResourceNotFoundException](ResourceNotFoundException.md)
- [MethodNotAllowedException](MethodNotAllowedException.md)
- [RequestTimeoutException](RequestTimeoutException.md)
- [ConflictException](ConflictException.md)
- [PayloadTooLargeException](PayloadTooLargeException.md)
- [UnsupportedMediaTypeException](UnsupportedMediaTypeException.md)
- [UnprocessableEntityException](UnprocessableEntityException.md)
- [RateLimitExceededException](RateLimitExceededException.md)
