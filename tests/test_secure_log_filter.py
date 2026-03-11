"""Tests for bamboohr_sdk.client.logger.secure_log_filter."""

import logging
from unittest.mock import MagicMock

import pytest

from bamboohr_sdk.client.logger.secure_log_filter import (
    SecureLogFilter,
    mask_value,
    redact_context,
    redact_string,
    _is_sensitive_key,
)


# ===========================================================================
# mask_value
# ===========================================================================


class TestMaskValue:
    """Tests for mask_value()."""

    def test_none_returns_empty(self):
        assert mask_value(None) == "[EMPTY]"

    def test_empty_string_returns_empty(self):
        assert mask_value("") == "[EMPTY]"

    def test_short_string_fully_redacted(self):
        assert mask_value("abc") == "[REDACTED]"

    def test_eight_chars_fully_redacted(self):
        assert mask_value("12345678") == "[REDACTED]"

    def test_long_string_shows_first_last_four(self):
        result = mask_value("abcdefghijklmnop")
        assert result == "abcd****mnop"

    def test_nine_chars_shows_partial(self):
        result = mask_value("123456789")
        assert result == "1234****6789"

    def test_dict_returns_redacted_object(self):
        assert mask_value({"key": "val"}) == "[REDACTED_OBJECT]"

    def test_list_returns_redacted_object(self):
        assert mask_value([1, 2, 3]) == "[REDACTED_OBJECT]"

    def test_numeric_value_converted_to_string(self):
        assert mask_value(12345) == "[REDACTED]"

    def test_long_numeric_shows_partial(self):
        result = mask_value(123456789012)
        assert result == "1234****9012"


# ===========================================================================
# _is_sensitive_key
# ===========================================================================


class TestIsSensitiveKey:
    """Tests for _is_sensitive_key()."""

    @pytest.mark.parametrize("key", [
        "password",
        "api_key",
        "apikey",
        "access_token",
        "authorization",
        "Authorization",
        "secret",
        "credential",
        "X-Auth-Token",
        "x-api-key",
        "cookie",
        "set-cookie",
        "my_password_field",
        "oauth_token",
    ])
    def test_sensitive_keys_detected(self, key):
        assert _is_sensitive_key(key) is True

    @pytest.mark.parametrize("key", [
        "method",
        "url",
        "status_code",
        "duration_ms",
        "Content-Type",
        "Accept",
    ])
    def test_non_sensitive_keys_pass_through(self, key):
        assert _is_sensitive_key(key) is False


# ===========================================================================
# redact_string
# ===========================================================================


class TestRedactString:
    """Tests for redact_string()."""

    def test_redacts_bearer_token(self):
        result = redact_string("Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9")
        assert result == "Bearer [REDACTED]"

    def test_redacts_basic_auth(self):
        result = redact_string("Basic dXNlcjpwYXNz")
        assert result == "Basic [REDACTED]"

    def test_redacts_inline_api_key(self):
        result = redact_string("api_key=my-secret-key-123")
        assert result == "api_key=[REDACTED]"

    def test_redacts_inline_token(self):
        result = redact_string("token=abc123def456")
        assert result == "token=[REDACTED]"

    def test_preserves_non_sensitive_text(self):
        text = "GET /api/v1/employees returned 200"
        assert redact_string(text) == text

    def test_redacts_bearer_case_insensitive(self):
        result = redact_string("bearer abc123")
        assert result == "Bearer [REDACTED]"

    def test_multiple_patterns_in_one_string(self):
        text = "Authorization: Bearer abc123, api_key=secret456"
        result = redact_string(text)
        assert "Bearer [REDACTED]" in result
        assert "api_key=[REDACTED]" in result


# ===========================================================================
# redact_context
# ===========================================================================


class TestRedactContext:
    """Tests for redact_context()."""

    def test_redacts_sensitive_dict_keys(self):
        data = {"method": "GET", "authorization": "Bearer secret-token-value", "url": "/api"}
        result = redact_context(data)
        assert result["method"] == "GET"
        assert result["url"] == "/api"
        # mask_value shows first 4 + **** + last 4 for strings > 8 chars
        assert result["authorization"] == "Bear****alue"

    def test_nested_dict_redaction(self):
        data = {"headers": {"Authorization": "Bearer secret-token-value", "Accept": "application/json"}}
        result = redact_context(data)
        assert result["headers"]["Accept"] == "application/json"
        assert result["headers"]["Authorization"] == "Bear****alue"

    def test_list_redaction(self):
        data = [{"password": "secret"}, {"name": "test"}]
        result = redact_context(data)
        assert "secret" not in str(result[0]["password"])
        assert result[1]["name"] == "test"

    def test_string_pattern_redaction_in_values(self):
        data = {"info": "token=mysecrettoken123"}
        result = redact_context(data)
        assert "mysecrettoken123" not in result["info"]

    def test_non_sensitive_values_preserved(self):
        data = {"status": 200, "method": "POST"}
        result = redact_context(data)
        assert result == data

    def test_preserves_non_string_non_dict(self):
        assert redact_context(42) == 42
        assert redact_context(True) is True
        assert redact_context(None) is None


# ===========================================================================
# SecureLogFilter
# ===========================================================================


class TestSecureLogFilter:
    """Tests for SecureLogFilter."""

    def _make_record(self, msg="test message", level=logging.INFO, **extra):
        """Create a LogRecord with extra attributes."""
        record = logging.LogRecord(
            name="bamboohr_sdk",
            level=level,
            pathname="test.py",
            lineno=1,
            msg=msg,
            args=(),
            exc_info=None,
        )
        for k, v in extra.items():
            setattr(record, k, v)
        return record

    def test_filter_returns_true(self):
        filt = SecureLogFilter()
        record = self._make_record()
        assert filt.filter(record) is True

    def test_redacts_bearer_in_message(self):
        filt = SecureLogFilter()
        record = self._make_record(msg="Auth: Bearer eyJabc123")
        filt.filter(record)
        assert "eyJabc123" not in record.msg
        assert "Bearer [REDACTED]" in record.msg

    def test_redacts_sensitive_extra_key(self):
        filt = SecureLogFilter()
        record = self._make_record(password="super-secret-password")
        filt.filter(record)
        assert record.password != "super-secret-password"
        assert "supe" in record.password  # first 4 chars visible
        assert "word" in record.password  # last 4 chars visible

    def test_redacts_dict_extra_values(self):
        filt = SecureLogFilter()
        headers = {"Authorization": "Bearer secret-token-value", "Content-Type": "application/json"}
        record = self._make_record(headers=headers)
        filt.filter(record)
        assert record.headers["Authorization"] == "Bear****alue"
        assert record.headers["Content-Type"] == "application/json"

    def test_disabled_filter_passes_through(self):
        filt = SecureLogFilter(enabled=False)
        record = self._make_record(msg="Bearer secret123")
        filt.filter(record)
        assert "secret123" in record.msg

    def test_enable_disable_toggle(self):
        filt = SecureLogFilter(enabled=True)
        record = self._make_record(msg="Bearer secret123")
        filt.filter(record)
        assert "secret123" not in record.msg

        filt.enabled = False
        record2 = self._make_record(msg="Bearer secret456")
        filt.filter(record2)
        assert "secret456" in record2.msg

    def test_redacts_args_tuple_with_strings(self):
        filt = SecureLogFilter()
        record = self._make_record(msg="Value: %s")
        record.args = ("Bearer eyJtoken123",)
        filt.filter(record)
        assert "eyJtoken123" not in str(record.args)

    def test_redacts_args_dict(self):
        filt = SecureLogFilter()
        record = self._make_record(msg="%(password)s")
        record.args = {"password": "my-secret"}
        filt.filter(record)
        assert "my-secret" not in str(record.args)

    def test_non_sensitive_extra_preserved(self):
        filt = SecureLogFilter()
        record = self._make_record(method="GET", status_code=200)
        filt.filter(record)
        assert record.method == "GET"
        assert record.status_code == 200

    def test_idempotent_attachment(self):
        """SecureLogFilter should not be added twice to the same logger."""
        test_logger = logging.getLogger("test_idempotent")
        filt1 = SecureLogFilter()
        test_logger.addFilter(filt1)

        # Simulate what with_logging does
        if not any(isinstance(f, SecureLogFilter) for f in test_logger.filters):
            test_logger.addFilter(SecureLogFilter())

        secure_filters = [f for f in test_logger.filters if isinstance(f, SecureLogFilter)]
        assert len(secure_filters) == 1

        # Clean up
        test_logger.removeFilter(filt1)
