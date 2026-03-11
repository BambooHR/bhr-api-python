"""Secure logging utilities with sensitive data redaction.

Provides a :class:`SecureLogFilter` for automatic redaction and re-exports
the lower-level helpers from :mod:`bamboohr_sdk.api_helper`::

    from bamboohr_sdk.client.logger import SecureLogFilter, redact_headers
"""

from bamboohr_sdk.api_helper import (
    SENSITIVE_HEADERS,
    redact_headers,
    redact_url,
)
from bamboohr_sdk.client.logger.secure_log_filter import (
    SecureLogFilter,
    mask_value,
    redact_context,
    redact_string,
)

__all__ = [
    "SENSITIVE_HEADERS",
    "SecureLogFilter",
    "mask_value",
    "redact_context",
    "redact_headers",
    "redact_string",
    "redact_url",
]
