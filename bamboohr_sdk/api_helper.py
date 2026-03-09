"""
ApiHelper — Retry logic and logging utilities for BambooHR SDK.

Provides request retry with exponential backoff, request/response logging
with sensitive data redaction. Mirrors the PHP SDK's ApiHelper.
"""

from __future__ import annotations

import logging
import re
import time
from typing import Any, Callable, Dict, List, Optional, Set, Tuple
from urllib.parse import urlparse, urlunparse

from bamboohr_sdk.api_error_helper import create_exception, get_error_info
from bamboohr_sdk.exceptions import ApiException

logger = logging.getLogger("bamboohr_sdk")

# Headers whose values should be redacted in logs
SENSITIVE_HEADERS: Set[str] = {
    "authorization",
    "cookie",
    "set-cookie",
    "x-api-key",
    "api-key",
    "x-auth-token",
    "x-auth",
    "x-user-id",
    "x-email",
    "x-csrf-token",
    "x-bamboohr-token",
    "x-bamboohr-key",
}

# Path segments that contain potentially sensitive IDs
_SENSITIVE_PATH_PATTERNS: List[Tuple[str, str]] = [
    (r"(/users/)[^/]+(/|$)", r"\1[ID_REDACTED]\2"),
    (r"(/employees/)[^/]+(/|$)", r"\1[ID_REDACTED]\2"),
    (r"(/companies/)[^/]+(/|$)", r"\1[ID_REDACTED]\2"),
]


def redact_headers(headers: Optional[Dict[str, str]]) -> Dict[str, str]:
    """Redact sensitive header values for safe logging.

    :param headers: Original request/response headers.
    :return: A copy with sensitive values replaced by '[REDACTED]'.
    """
    if not headers:
        return {}

    redacted: Dict[str, str] = {}
    for name, value in headers.items():
        if name.lower() in SENSITIVE_HEADERS:
            redacted[name] = "[REDACTED]"
        else:
            redacted[name] = value
    return redacted


def redact_url(url: str) -> str:
    """Redact sensitive information from a URL for safe logging.

    Redacts query parameters and known-sensitive path segments.

    :param url: The original URL.
    :return: A redacted URL safe for logging.
    """
    parsed = urlparse(url)
    path = parsed.path

    for pattern, replacement in _SENSITIVE_PATH_PATTERNS:
        path = re.sub(pattern, replacement, path)

    query = "[QUERY_PARAMS_REDACTED]" if parsed.query else ""

    return urlunparse((
        parsed.scheme,
        parsed.netloc,
        path,
        "",  # params
        query.lstrip("?") if query else "",
        "",  # fragment
    ))


def send_with_retries(
    request_fn: Callable[[], Any],
    *,
    method: str,
    url: str,
    headers: Optional[Dict[str, str]] = None,
    max_retries: int = 1,
    retryable_status_codes: Optional[List[int]] = None,
) -> Any:
    """Execute an HTTP request with retry logic and exponential backoff.

    :param request_fn: A callable that performs the HTTP request and returns
        a RESTResponse. Should raise ApiException on HTTP errors.
    :param method: The HTTP method (for logging).
    :param url: The request URL (for logging).
    :param headers: The request headers (for logging, will be redacted).
    :param max_retries: Maximum number of retry attempts (0-5).
    :param retryable_status_codes: Status codes eligible for retry.
    :return: The RESTResponse from a successful request.
    :raises ApiException: If the request fails after all retries.
    """
    if retryable_status_codes is None:
        retryable_status_codes = [408, 429, 504, 598]

    attempt = 0
    redacted_url = redact_url(url)
    redacted_headers = redact_headers(headers)

    logger.info(
        "API Request",
        extra={
            "method": method,
            "uri": redacted_url,
            "headers": redacted_headers,
            "max_retries": max_retries,
        },
    )

    start_time = time.monotonic()

    while True:
        attempt += 1
        attempt_start = time.monotonic()

        try:
            response = request_fn()

            total_ms = (time.monotonic() - start_time) * 1000
            attempt_ms = (time.monotonic() - attempt_start) * 1000

            logger.info(
                "API Response",
                extra={
                    "method": method,
                    "uri": redacted_url,
                    "status_code": response.status,
                    "reason": response.reason,
                    "total_duration_ms": round(total_ms, 2),
                    "attempt_duration_ms": round(attempt_ms, 2),
                    "attempt": attempt,
                },
            )

            # Check if we got a retryable status code from a "successful" urllib3 response
            if (
                response.status in retryable_status_codes
                and attempt <= max_retries
            ):
                delay = 0.1 * (2 ** (attempt - 1))  # 100ms, 200ms, 400ms, ...
                logger.warning(
                    "Retryable status %d, retrying in %.1fs (attempt %d/%d)",
                    response.status,
                    delay,
                    attempt,
                    max_retries,
                )
                time.sleep(delay)
                continue

            return response

        except ApiException as exc:
            status_code = exc.status or 0
            total_ms = (time.monotonic() - start_time) * 1000
            attempt_ms = (time.monotonic() - attempt_start) * 1000
            will_retry = (
                status_code in retryable_status_codes and attempt <= max_retries
            )

            logger.error(
                "API Error Response",
                extra={
                    "method": method,
                    "uri": redacted_url,
                    "status_code": status_code,
                    "reason": str(exc),
                    "total_duration_ms": round(total_ms, 2),
                    "attempt_duration_ms": round(attempt_ms, 2),
                    "attempt": attempt,
                    "will_retry": will_retry,
                },
            )

            if will_retry:
                delay = 0.1 * (2 ** (attempt - 1))
                time.sleep(delay)
                continue

            raise

        except Exception as exc:
            total_ms = (time.monotonic() - start_time) * 1000
            attempt_ms = (time.monotonic() - attempt_start) * 1000
            will_retry = attempt <= max_retries

            logger.error(
                "API Connection Error",
                extra={
                    "method": method,
                    "uri": redacted_url,
                    "error": str(exc),
                    "total_duration_ms": round(total_ms, 2),
                    "attempt_duration_ms": round(attempt_ms, 2),
                    "attempt": attempt,
                    "will_retry": will_retry,
                },
            )

            if will_retry:
                delay = 0.1 * (2 ** (attempt - 1))
                time.sleep(delay)
                continue

            raise ApiException(status=0, reason=str(exc)) from exc

    # Should never reach here, but satisfy type checkers
    raise ApiException(
        status=0,
        reason="Request failed after maximum retries",
    )
