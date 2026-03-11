"""Secure logging filter with automatic sensitive data redaction.

Provides a :class:`logging.Filter` that inspects every log record and
auto-redacts sensitive keys in ``extra`` attributes and common credential
patterns in the log message.  This is the Pythonic equivalent of the PHP
SDK's ``SecureLogger`` — it plugs into stdlib logging rather than wrapping
it in a custom class.

Usage::

    import logging
    from bamboohr_sdk.client.logger.secure_log_filter import SecureLogFilter

    logger = logging.getLogger("bamboohr_sdk")
    logger.addFilter(SecureLogFilter())
"""

from __future__ import annotations

import logging
import re
from typing import Any, Dict, Optional, Set, Tuple

# ---------------------------------------------------------------------------
# Sensitive-key detection
# ---------------------------------------------------------------------------

#: Keys whose *values* should be redacted when they appear in a log record's
#: extra attributes (matched by substring, case-insensitive).
SENSITIVE_KEYS: Set[str] = {
    "password",
    "api_key",
    "apikey",
    "api-key",
    "token",
    "access_token",
    "accesstoken",
    "access-token",
    "oauth_token",
    "oauthtoken",
    "secret",
    "authorization",
    "auth",
    "credential",
    "credentials",
    "cookie",
    "set-cookie",
    "x-api-key",
    "x-auth-token",
    "x-auth",
    "x-csrf-token",
    "x-bamboohr-token",
    "x-bamboohr-key",
}

# ---------------------------------------------------------------------------
# Pattern-based string redaction
# ---------------------------------------------------------------------------

#: Regex patterns that match inline credential values in log messages.
_STRING_PATTERNS: list[Tuple[re.Pattern, str]] = [
    # Bearer tokens
    (re.compile(r"Bearer\s+[a-zA-Z0-9\-._~+/]+=*", re.IGNORECASE), "Bearer [REDACTED]"),
    # Basic auth
    (re.compile(r"Basic\s+[a-zA-Z0-9+/]+=*", re.IGNORECASE), "Basic [REDACTED]"),
    # Inline api_key=... or api-key=...
    (
        re.compile(
            r"""["\']?api[_-]?key["\']?\s*[:=]\s*["\']?[a-zA-Z0-9\-_]+["\']?""",
            re.IGNORECASE,
        ),
        "api_key=[REDACTED]",
    ),
    # Inline token=...
    (
        re.compile(
            r"""["\']?token["\']?\s*[:=]\s*["\']?[a-zA-Z0-9\-_]+["\']?""",
            re.IGNORECASE,
        ),
        "token=[REDACTED]",
    ),
]


# ---------------------------------------------------------------------------
# Value masking
# ---------------------------------------------------------------------------


def mask_value(value: Any) -> str:
    """Mask a sensitive value for safe logging.

    - ``None`` / empty → ``"[EMPTY]"``
    - Non-string collections → ``"[REDACTED_OBJECT]"``
    - Strings ≤ 8 chars → ``"[REDACTED]"``
    - Longer strings → first 4 + ``****`` + last 4

    :param value: The value to mask.
    :return: A safe-to-log string representation.
    """
    if value is None or value == "":
        return "[EMPTY]"

    if isinstance(value, (dict, list, set, tuple)):
        return "[REDACTED_OBJECT]"

    s = str(value)
    if len(s) <= 8:
        return "[REDACTED]"

    return s[:4] + "****" + s[-4:]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _is_sensitive_key(key: str) -> bool:
    """Return True if *key* (lowercased) contains any sensitive substring."""
    key_lower = key.lower()
    return any(sk in key_lower for sk in SENSITIVE_KEYS)


def redact_context(data: Any) -> Any:
    """Recursively redact sensitive values in a context dict / list.

    :param data: Arbitrary data (usually a ``dict`` passed as ``extra``).
    :return: A copy with sensitive values masked.
    """
    if isinstance(data, dict):
        redacted: Dict[str, Any] = {}
        for k, v in data.items():
            if _is_sensitive_key(str(k)):
                redacted[k] = mask_value(v)
            else:
                redacted[k] = redact_context(v)
        return redacted

    if isinstance(data, (list, tuple)):
        return type(data)(redact_context(item) for item in data)

    if isinstance(data, str):
        return redact_string(data)

    return data


def redact_string(text: str) -> str:
    """Apply pattern-based redaction to a plain string.

    Replaces Bearer tokens, Basic auth, and inline ``api_key=``/``token=``
    patterns with safe placeholders.

    :param text: The input string.
    :return: The redacted string.
    """
    for pattern, replacement in _STRING_PATTERNS:
        text = pattern.sub(replacement, text)
    return text


# ---------------------------------------------------------------------------
# The filter
# ---------------------------------------------------------------------------


class SecureLogFilter(logging.Filter):
    """A :class:`logging.Filter` that redacts sensitive data from log records.

    Attach to a logger or handler to automatically scrub credentials from
    ``extra`` attributes and from the log message itself.

    :param name: Standard filter name (passed to ``logging.Filter``).
    :param enabled: Whether redaction is active.  When ``False`` the filter
        still returns ``True`` (allowing the record through) but performs no
        redaction — useful for development.

    Example::

        filt = SecureLogFilter()
        logging.getLogger("bamboohr_sdk").addFilter(filt)

        # Later, to toggle off:
        filt.enabled = False
    """

    #: Attribute names set via ``extra={}`` that we inspect for redaction.
    #: We skip the standard LogRecord attributes to avoid mangling internals.
    _STANDARD_ATTRS = frozenset(logging.LogRecord("", 0, "", 0, "", (), None).__dict__)

    def __init__(self, name: str = "", enabled: bool = True) -> None:
        super().__init__(name)
        self.enabled = enabled

    def filter(self, record: logging.LogRecord) -> bool:
        """Redact the record in-place and allow it through.

        :param record: The log record to process.
        :return: Always ``True`` (the record is never suppressed).
        """
        if not self.enabled:
            return True

        # --- Redact extra attributes ---
        for attr in set(record.__dict__) - self._STANDARD_ATTRS:
            value = getattr(record, attr)
            if _is_sensitive_key(attr):
                setattr(record, attr, mask_value(value))
            elif isinstance(value, (dict, list, tuple)):
                setattr(record, attr, redact_context(value))
            elif isinstance(value, str):
                setattr(record, attr, redact_string(value))

        # --- Redact the message ---
        if isinstance(record.msg, str):
            record.msg = redact_string(record.msg)

        # --- Redact args (%-style formatting) ---
        if record.args:
            if isinstance(record.args, dict):
                record.args = redact_context(record.args)
            elif isinstance(record.args, tuple):
                record.args = tuple(
                    redact_context(a) if isinstance(a, dict)
                    else redact_string(a) if isinstance(a, str)
                    else a
                    for a in record.args
                )

        return True
