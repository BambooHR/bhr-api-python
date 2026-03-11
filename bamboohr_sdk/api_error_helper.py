"""
ApiErrorHelper — Error catalog and exception factory for BambooHR SDK.

Provides detailed error messages, debugging tips, and request ID support
for API error responses.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from bamboohr_sdk.exceptions import (
    ApiException,
    BadRequestException,
    ForbiddenException,
    NotFoundException,
    ServiceException,
    UnauthorizedException,
    ConflictException,
    UnprocessableEntityException,
)

# Error messages and debugging tips by HTTP status code
ERROR_MESSAGES: Dict[int, Dict[str, Any]] = {
    400: {
        "type": "BadRequest",
        "title": "Bad request",
        "causes": [
            "Invalid request syntax or parameters",
            "Missing required fields",
            "Malformed JSON in request body",
        ],
        "tips": [
            "Check request parameters and ensure they match API documentation",
            "Validate request body format before sending",
            "Ensure all required fields are included",
            "Review API documentation for correct endpoint usage",
        ],
    },
    401: {
        "type": "AuthenticationFailed",
        "title": "Authentication failed",
        "causes": [
            "Invalid API key or password",
            "Expired credentials",
            "Insufficient permissions for this operation",
        ],
        "tips": [
            "Verify your API key and subdomain are correct",
            "Check that your API key has the necessary permissions",
            "Ensure your company subdomain is correct",
            "Try regenerating your API key in the BambooHR system",
        ],
    },
    403: {
        "type": "PermissionDenied",
        "title": "Permission denied",
        "causes": [
            "API key lacks required permissions",
            "Account restrictions in place",
            "IP address restrictions",
        ],
        "tips": [
            "Verify your API key has the necessary permissions",
            "Contact your BambooHR administrator to review API access permissions",
            "Check if IP restrictions are in place for API access",
        ],
    },
    404: {
        "type": "ResourceNotFound",
        "title": "Resource not found",
        "causes": [
            "The requested resource does not exist",
            "Resource may have been deleted",
            "Incorrect resource identifier or path",
        ],
        "tips": [
            "Verify the resource ID or path is correct",
            "Check if the resource exists before attempting to access it",
            "Ensure you are using the correct API version",
            "Confirm the resource has not been deleted or archived",
        ],
    },
    405: {
        "type": "MethodNotAllowed",
        "title": "Method not allowed",
        "causes": [
            "Using an incorrect HTTP method for this endpoint",
            "The endpoint does not support the requested operation",
            "API version mismatch",
        ],
        "tips": [
            "Check API documentation for the correct HTTP method (GET, POST, PUT, DELETE)",
            "Verify the endpoint supports the operation you are attempting",
            "Ensure you are using the correct API version",
        ],
    },
    408: {
        "type": "RequestTimeout",
        "title": "Request timeout",
        "causes": [
            "The server did not receive a complete request in time",
            "Network connectivity issues",
            "Server overload or high latency",
        ],
        "tips": [
            "Check your network connection",
            "Increase request timeout settings",
            "Consider breaking large requests into smaller chunks",
            "Increase the number of retries",
        ],
    },
    409: {
        "type": "Conflict",
        "title": "Conflict",
        "causes": [
            "Resource state conflict with the current request",
            "Concurrent modification of the same resource",
            "Attempting to create a resource that already exists",
            "Violating unique constraints",
        ],
        "tips": [
            "Fetch the latest state of the resource before attempting modifications",
            "Implement optimistic concurrency control",
            "Check for existing resources before creation attempts",
            "Handle conflict resolution in your application logic",
        ],
    },
    413: {
        "type": "PayloadTooLarge",
        "title": "Payload too large",
        "causes": [
            "Request body exceeds the server's size limit",
            "File upload is too large",
            "Batch operation contains too many items",
        ],
        "tips": [
            "Reduce the size of your request payload",
            "Split large requests into smaller chunks",
            "Compress data before sending if appropriate",
            "Check API documentation for size limits",
        ],
    },
    415: {
        "type": "UnsupportedMediaType",
        "title": "Unsupported media type",
        "causes": [
            "Content-Type header is missing or incorrect",
            "Request body format is not supported by the API",
            "Using XML when only JSON is supported (or vice versa)",
        ],
        "tips": [
            "Check that your Content-Type header is set correctly",
            "Verify the API endpoint supports the format you're sending",
            "Convert your payload to a supported format (usually JSON)",
            "Review API documentation for supported media types",
        ],
    },
    422: {
        "type": "UnprocessableEntity",
        "title": "Unprocessable entity",
        "causes": [
            "Request syntax is correct but contains semantic errors",
            "Validation failures in the request data",
            "Business rule violations",
            "Data integrity constraints",
        ],
        "tips": [
            "Check the response body for specific validation error details",
            "Ensure request data meets all business rules and constraints",
            "Validate data before submitting to the API",
            "Review API documentation for field requirements and limitations",
        ],
    },
    429: {
        "type": "RateLimitExceeded",
        "title": "Rate limit exceeded",
        "causes": [
            "Too many requests in a short time period",
            "Exceeding API quota limits",
        ],
        "tips": [
            "Implement exponential backoff retry strategy",
            "Reduce frequency of API calls",
            "Consider caching responses where appropriate",
            "Check the Retry-After header for guidance on when to retry",
        ],
    },
    500: {
        "type": "InternalServerError",
        "title": "Internal server error",
        "causes": [
            "Unexpected condition on the server",
            "Server-side exception or error",
            "Database issues or connectivity problems",
        ],
        "tips": [
            "Retry the request after a short delay",
            "Contact BambooHR support if the problem persists",
            "Include request ID or timestamp when reporting issues",
        ],
    },
    501: {
        "type": "NotImplemented",
        "title": "Not implemented",
        "causes": [
            "The API endpoint does not support the requested functionality",
            "The feature is planned but not yet available",
            "Using a method that is not supported by this resource",
        ],
        "tips": [
            "Check API documentation to verify the feature is supported",
            "Confirm you are using the correct API version",
            "Consider alternative approaches to achieve your goal",
            "Contact support to inquire about feature availability",
        ],
    },
    502: {
        "type": "BadGateway",
        "title": "Bad gateway",
        "causes": [
            "The server received an invalid response from an upstream server",
            "Proxy or gateway configuration issues",
            "Temporary communication failure between servers",
        ],
        "tips": [
            "Retry the request after a delay",
            "Implement automatic retry logic with backoff",
            "Check if the service is experiencing known issues",
            "Verify network connectivity between your client and the API",
        ],
    },
    503: {
        "type": "ServiceUnavailable",
        "title": "Service unavailable",
        "causes": [
            "Server is temporarily overloaded",
            "Server is under maintenance",
            "Service is temporarily down",
        ],
        "tips": [
            "Check the Retry-After header if provided",
            "Consider adding this status code to retryable_status_codes and increasing retries",
            "Consider implementing a circuit breaker pattern",
        ],
    },
    504: {
        "type": "GatewayTimeout",
        "title": "Gateway timeout",
        "causes": [
            "The gateway or proxy did not receive a timely response",
            "BambooHR servers experiencing high load",
            "Complex query taking too long to process",
        ],
        "tips": [
            "Retry the request after a delay",
            "Simplify complex queries if possible",
            "Implement circuit breaker pattern to prevent cascading failures",
        ],
    },
    507: {
        "type": "InsufficientStorage",
        "title": "Insufficient storage",
        "causes": [
            "Server storage capacity has been reached",
            "Quota limits exceeded for your account",
            "Temporary resource constraints on the server",
        ],
        "tips": [
            "Remove unnecessary data if possible",
            "Contact support to discuss storage limitations",
            "Check if there are unused resources that can be deleted",
        ],
    },
    598: {
        "type": "NetworkReadTimeout",
        "title": "Network read timeout",
        "causes": [
            "Network connection was dropped while waiting for response",
            "Proxy or firewall issues",
            "Incomplete data transmission",
        ],
        "tips": [
            "Check network stability and firewall settings",
            "Increase read timeout values in your HTTP client",
            "Implement automatic retry logic for idempotent operations",
            "Consider using a more reliable network connection",
        ],
    },
}

# Mapping from status code to exception class
_STATUS_TO_EXCEPTION: Dict[int, type] = {
    400: BadRequestException,
    401: UnauthorizedException,
    403: ForbiddenException,
    404: NotFoundException,
    409: ConflictException,
    422: UnprocessableEntityException,
}


def create_exception(
    status_code: int,
    reason: str,
    headers: Optional[Any] = None,
    body: Optional[str] = None,
    request_id: Optional[str] = None,
) -> ApiException:
    """Create an appropriate exception based on the HTTP status code.

    :param status_code: The HTTP response status code.
    :param reason: The error reason/message.
    :param headers: The HTTP response headers.
    :param body: The HTTP response body.
    :param request_id: Optional request ID for tracing.
    :return: An ApiException or appropriate subclass.
    """
    # Build the reason message with request ID if available
    message = reason
    if request_id:
        message = f"{reason} [Request ID: {request_id}]"

    # Look up specific exception class
    exc_class = _STATUS_TO_EXCEPTION.get(status_code)
    if exc_class is not None:
        exc = exc_class(status=status_code, reason=message, body=body)
    elif 500 <= status_code <= 599:
        exc = ServiceException(status=status_code, reason=message, body=body)
    else:
        exc = ApiException(status=status_code, reason=message, body=body)

    # Attach headers and request_id
    exc.headers = headers
    if hasattr(exc, "request_id"):
        exc.request_id = request_id

    return exc


def format_detailed_error_message(
    base_message: str,
    causes: Optional[List[str]] = None,
    tips: Optional[List[str]] = None,
    request_id: Optional[str] = None,
) -> str:
    """Format a detailed error message with causes, tips, and request ID.

    :param base_message: The base error message.
    :param causes: List of potential causes.
    :param tips: List of debugging tips.
    :param request_id: Optional request ID to include.
    :return: Formatted error message string.
    """
    parts = [base_message]

    if request_id:
        parts[0] += f" [Request ID: {request_id}]"

    if causes:
        parts.append("This could be due to:")
        for cause in causes:
            parts.append(f"- {cause}")

    if tips:
        parts.append("\nDebugging tips:")
        for tip in tips:
            parts.append(f"- {tip}")
        if request_id:
            parts.append(
                f"- Include this Request ID ({request_id}) when contacting support"
            )

    return "\n".join(parts)


def get_error_info(status_code: int) -> Optional[Dict[str, Any]]:
    """Get error information for a given HTTP status code.

    :param status_code: The HTTP status code.
    :return: Dict with type, title, causes, tips — or None if unknown.
    """
    return ERROR_MESSAGES.get(status_code)
