"""
Example 04: Error Handling
===========================

Comprehensive guide to handling API errors with the BambooHR Python SDK.

The SDK provides:
    - Specific exception types for each HTTP error class
    - Built-in retry with exponential backoff
    - Detailed error information with request IDs
    - An error catalog with potential causes and debugging tips

Prerequisites:
    - pip install bamboohr-python

Usage:
    export BAMBOO_COMPANY="yourcompany"
    export BAMBOO_API_KEY="your_api_key_here"
    python examples/04_error_handling.py
"""

import logging
import os

from bamboohr_sdk.api_error_helper import (
    format_detailed_error_message,
    get_error_info,
)
from bamboohr_sdk.client import BambooHRClient
from bamboohr_sdk.exceptions import (
    ApiException,
    AuthenticationFailedException,
    BadRequestException,
    ConflictException,
    PermissionDeniedException,
    ResourceNotFoundException,
    ServerException,
    UnprocessableEntityException,
)

company = os.environ.get("BAMBOO_COMPANY", "yourcompany")
api_key = os.environ.get("BAMBOO_API_KEY", "your_api_key_here")
host = os.environ.get("BAMBOO_HOST")  # Optional: full base URL override


# =====================================================================
# Pattern 1: Specific Exception Handling
# =====================================================================
# The SDK raises specific exception types for each HTTP error status,
# so you can handle different failures appropriately.

print("=== Pattern 1: Specific Exception Handling ===\n")


def fetch_employee_safely(client: BambooHRClient, employee_id: str) -> None:
    """Demonstrate granular error handling for a single API call."""
    try:
        employee = client.employees().get_employee(
            id=employee_id,
            fields="firstName,lastName,workEmail",
        )
        print(f"  Found: {employee.first_name} {employee.last_name}")

    except BadRequestException as bad_request_error:
        # 400 — invalid parameters
        print(f"  Bad request: {bad_request_error.reason}")
        print("  Check that the employee ID and field names are valid.")

    except AuthenticationFailedException:
        # 401 — invalid or expired credentials
        print("  Authentication failed. Check your API key or OAuth tokens.")

    except PermissionDeniedException:
        # 403 — valid credentials but insufficient permissions
        print("  Permission denied. Your API key cannot access this resource.")

    except ResourceNotFoundException:
        # 404 — employee doesn't exist
        print(f"  Employee {employee_id} not found.")

    except ConflictException:
        # 409 — state conflict
        print("  Conflict — the resource state has changed.")

    except UnprocessableEntityException as validation_error:
        # 422 — validation failure
        print(f"  Validation error: {validation_error.body}")

    except ServerException as server_error:
        # 5xx — server-side error
        print(f"  Server error ({server_error.status}): {server_error.reason}")
        if server_error.request_id:
            print(f"  Request ID: {server_error.request_id}")
            print("  Include this when contacting BambooHR support.")

    except ApiException as api_error:
        # Catch-all for any unexpected status codes
        print(f"  Unexpected error ({api_error.status}): {api_error.reason}")


# =====================================================================
# Pattern 2: Automatic Retry with Exponential Backoff
# =====================================================================
# The SDK automatically retries transient failures (408, 429, 504, 598)
# with exponential backoff. Configure via with_retries().

print("=== Pattern 2: Automatic Retry ===\n")

builder = BambooHRClient().with_api_key(api_key).with_retries(3)  # Retry up to 3 times (0-5 allowed)
client_with_retry = (builder.with_host(host) if host else builder.for_company(company)).build()

print("  Client configured with 3 retries.")
print("  Retryable status codes: 408, 429, 504, 598")
print("  Backoff schedule: 100ms, 200ms, 400ms\n")

# The retry is transparent — just make your API call normally:
#
#   directory = client_with_retry.employees().get_employees_directory()
#
# If a transient error occurs, the SDK retries automatically.
# If all retries are exhausted, the final exception is raised.


# =====================================================================
# Pattern 3: Using the Error Catalog
# =====================================================================
# The SDK includes a built-in error catalog with detailed information
# about each HTTP error type, including potential causes and debugging tips.

print("=== Pattern 3: Error Catalog ===\n")


def handle_error_with_catalog(api_error: ApiException) -> None:
    """Use the error catalog for detailed diagnostics."""
    error_info = get_error_info(api_error.status)

    if error_info:
        message = format_detailed_error_message(
            base_message=f"{error_info['title']} ({api_error.status})",
            causes=error_info.get("causes"),
            tips=error_info.get("tips"),
            request_id=api_error.request_id,
        )
        print(message)
    else:
        print(f"Unknown error ({api_error.status}): {api_error.reason}")


# Example: show what the catalog provides for a 429 rate limit error
rate_limit_info = get_error_info(429)
if rate_limit_info:
    print(f"  Error type: {rate_limit_info['type']}")
    print(f"  Title: {rate_limit_info['title']}")
    print("  Potential causes:")
    for cause in rate_limit_info["causes"]:
        print(f"    - {cause}")
    print("  Debugging tips:")
    for tip in rate_limit_info["tips"]:
        print(f"    - {tip}")


# =====================================================================
# Pattern 4: Centralized Error Handler
# =====================================================================
# For larger applications, centralize error handling in a reusable class.

print("\n=== Pattern 4: Centralized Error Handler ===\n")


class BambooHRErrorHandler:
    """Centralized error handler for BambooHR API calls.

    Provides consistent logging, monitoring integration, and user-friendly
    error messages across your application.
    """

    def __init__(self, logger: logging.Logger | None = None):
        self.logger = logger or logging.getLogger(__name__)

    def handle(self, error: ApiException, context: str = "") -> None:
        """Handle an API exception with logging and diagnostics.

        Args:
            error: The API exception to handle.
            context: Description of what operation was being attempted.
        """
        prefix = f"[{context}] " if context else ""

        # Log with appropriate severity
        if isinstance(error, (AuthenticationFailedException, PermissionDeniedException)):
            self.logger.error("%sAuth error (%s): %s", prefix, error.status, error.reason)
        elif isinstance(error, ServerException):
            self.logger.error(
                "%sServer error (%s): %s [request_id=%s]",
                prefix,
                error.status,
                error.reason,
                error.request_id,
            )
        elif isinstance(error, ResourceNotFoundException):
            self.logger.warning("%sNot found: %s", prefix, error.reason)
        else:
            self.logger.error("%sAPI error (%s): %s", prefix, error.status, error.reason)

        # Enrich with error catalog
        error_info = get_error_info(error.status)
        if error_info:
            self.logger.debug("%sPotential causes: %s", prefix, "; ".join(error_info.get("causes", [])))

        # Integration point for error tracking services:
        #   sentry_sdk.capture_exception(error)
        #   bugsnag.notify(error)
        #   datadog.statsd.increment("bamboohr.api_errors", tags=[f"status:{error.status}"])


error_handler = BambooHRErrorHandler()

# Usage:
#   try:
#       employee = client.employees().get_employee(id="123")
#   except ApiException as api_error:
#       error_handler.handle(api_error, context="fetch_employee")

print("  Centralized handler created.")
print("  Provides: consistent logging, error catalog integration, monitoring hooks\n")


# =====================================================================
# Pattern 5: Graceful Degradation
# =====================================================================
# For non-critical operations, fail gracefully rather than crashing.

print("=== Pattern 5: Graceful Degradation ===\n")


def get_employee_photo_url(client: BambooHRClient, employee_id: str) -> str | None:
    """Fetch employee photo URL, returning None if unavailable.

    Photos are non-critical — the UI can show a placeholder instead.
    """
    try:
        client.photos().get_employee_photo(id=employee_id, size="small")
        return f"https://{company}.bamboohr.com/employees/photos/?h={employee_id}"
    except ResourceNotFoundException:
        return None  # No photo uploaded — use placeholder
    except ApiException:
        return None  # Any other error — degrade gracefully


def get_employee_with_fallback(client: BambooHRClient, employee_id: str) -> dict:
    """Fetch employee data with graceful degradation for optional fields."""
    result = {"id": employee_id}

    # Core data — let errors propagate
    employee = client.employees().get_employee(
        id=employee_id,
        fields="firstName,lastName,workEmail",
    )
    result["name"] = f"{employee.first_name} {employee.last_name}"

    # Optional data — degrade gracefully
    result["photo_url"] = get_employee_photo_url(client, employee_id)

    return result


print("  Core operations: let errors propagate to caller")
print("  Optional operations: catch and return fallback values")


# =====================================================================
# Pattern 6: Debug Logging
# =====================================================================
# Enable SDK debug logging to see request/response details.

print("\n=== Pattern 6: Debug Logging ===\n")

# Option A: Enable via the client builder
builder = BambooHRClient().with_api_key(api_key).with_logging(level=logging.DEBUG)
debug_client = (builder.with_host(host) if host else builder.for_company(company)).build()

# Option B: Configure Python's logging directly
#   logging.getLogger("bamboohr_sdk").setLevel(logging.DEBUG)

print("  SDK logging enabled at DEBUG level.")
print("  Sensitive data (API keys, tokens) is automatically redacted in logs.")
print("  Request IDs are included in all exception messages.\n")

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
#
# Exception Hierarchy:
#   ApiException (base)
#   ├── ClientException (4xx)
#   │   ├── BadRequestException           (400)
#   │   ├── AuthenticationFailedException (401)
#   │   ├── PermissionDeniedException     (403)
#   │   ├── ResourceNotFoundException     (404)
#   │   ├── ConflictException             (409)
#   │   ├── UnprocessableEntityException  (422)
#   │   └── RateLimitExceededException    (429)
#   └── ServerException (5xx)
#       ├── InternalServerErrorException  (500)
#       ├── ServiceUnavailableException   (503)
#       └── GatewayTimeoutException       (504)
#
# Best Practices:
#   1. Catch specific exceptions for error-specific handling
#   2. Use the error catalog for detailed diagnostics
#   3. Enable retries for transient failures: .with_retries(3)
#   4. Log request IDs for production debugging
#   5. Degrade gracefully for non-critical operations
#   6. Centralize error handling in larger applications
