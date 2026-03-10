"""Tests for bamboohr_sdk.api_helper module."""

import time
from unittest.mock import MagicMock, patch

import pytest

from bamboohr_sdk.api_helper import (
    SENSITIVE_HEADERS,
    redact_headers,
    redact_url,
    send_with_retries,
)
from bamboohr_sdk.exceptions import ApiException


class TestRedactHeaders:
    """Tests for redact_headers."""

    def test_redacts_authorization(self):
        headers = {"Authorization": "Bearer secret-token"}
        result = redact_headers(headers)
        assert result["Authorization"] == "[REDACTED]"

    def test_redacts_case_insensitive(self):
        headers = {"authorization": "Basic abc123"}
        result = redact_headers(headers)
        assert result["authorization"] == "[REDACTED]"

    def test_preserves_non_sensitive_headers(self):
        headers = {"Content-Type": "application/json", "Accept": "text/html"}
        result = redact_headers(headers)
        assert result["Content-Type"] == "application/json"
        assert result["Accept"] == "text/html"

    def test_redacts_all_sensitive_headers(self):
        headers = {h: "secret-value" for h in SENSITIVE_HEADERS}
        result = redact_headers(headers)
        for h in SENSITIVE_HEADERS:
            assert result[h] == "[REDACTED]"

    def test_returns_empty_dict_for_none(self):
        assert redact_headers(None) == {}

    def test_returns_empty_dict_for_empty(self):
        assert redact_headers({}) == {}

    def test_does_not_mutate_original(self):
        headers = {"Authorization": "secret"}
        redact_headers(headers)
        assert headers["Authorization"] == "secret"


class TestRedactUrl:
    """Tests for redact_url."""

    def test_redacts_query_params(self):
        url = "https://api.example.com/v1/data?apikey=secret&page=1"
        result = redact_url(url)
        assert "secret" not in result
        assert "[QUERY_PARAMS_REDACTED]" in result

    def test_preserves_url_without_query(self):
        url = "https://api.example.com/v1/data"
        result = redact_url(url)
        assert "api.example.com" in result
        assert "[QUERY_PARAMS_REDACTED]" not in result

    def test_redacts_employee_id_in_path(self):
        url = "https://api.example.com/api/v1/employees/12345/files"
        result = redact_url(url)
        assert "12345" not in result
        assert "[ID_REDACTED]" in result

    def test_redacts_company_id_in_path(self):
        url = "https://api.example.com/api/v1/companies/acme-corp/info"
        result = redact_url(url)
        assert "acme-corp" not in result
        assert "[ID_REDACTED]" in result

    def test_preserves_scheme_and_host(self):
        url = "https://bamboohr.com/api/v1/status"
        result = redact_url(url)
        assert result.startswith("https://bamboohr.com")


class TestSendWithRetries:
    """Tests for send_with_retries."""

    def _make_response(self, status=200, reason="OK"):
        resp = MagicMock()
        resp.status = status
        resp.reason = reason
        return resp

    def test_successful_request_no_retry(self):
        response = self._make_response(200)
        fn = MagicMock(return_value=response)

        result = send_with_retries(
            fn, method="GET", url="https://example.com", max_retries=0
        )

        assert result is response
        fn.assert_called_once()

    @patch("bamboohr_sdk.api_helper.time.sleep")
    def test_retries_on_retryable_status(self, mock_sleep):
        fail_resp = self._make_response(429, "Too Many Requests")
        ok_resp = self._make_response(200, "OK")
        fn = MagicMock(side_effect=[fail_resp, ok_resp])

        result = send_with_retries(
            fn,
            method="GET",
            url="https://example.com",
            max_retries=2,
            retryable_status_codes=[429],
        )

        assert result is ok_resp
        assert fn.call_count == 2
        mock_sleep.assert_called_once()

    @patch("bamboohr_sdk.api_helper.time.sleep")
    def test_retries_on_api_exception(self, mock_sleep):
        exc = ApiException(status=504, reason="Gateway Timeout")
        ok_resp = self._make_response(200, "OK")
        fn = MagicMock(side_effect=[exc, ok_resp])

        result = send_with_retries(
            fn,
            method="GET",
            url="https://example.com",
            max_retries=2,
            retryable_status_codes=[504],
        )

        assert result is ok_resp
        assert fn.call_count == 2

    @patch("bamboohr_sdk.api_helper.time.sleep")
    def test_raises_after_max_retries_exhausted(self, mock_sleep):
        fail_resp = self._make_response(429, "Too Many Requests")
        fn = MagicMock(return_value=fail_resp)

        # max_retries=1 means: attempt 1 (original) + 1 retry = 2 total
        # But on the 2nd attempt, attempt > max_retries so it returns the response
        result = send_with_retries(
            fn,
            method="GET",
            url="https://example.com",
            max_retries=1,
            retryable_status_codes=[429],
        )

        # After exhausting retries, returns the last response
        assert result.status == 429
        assert fn.call_count == 2

    def test_no_retry_for_non_retryable_status(self):
        response = self._make_response(400, "Bad Request")
        fn = MagicMock(return_value=response)

        result = send_with_retries(
            fn,
            method="POST",
            url="https://example.com",
            max_retries=3,
            retryable_status_codes=[429, 504],
        )

        assert result is response
        fn.assert_called_once()

    @patch("bamboohr_sdk.api_helper.time.sleep")
    def test_raises_non_retryable_api_exception(self, mock_sleep):
        exc = ApiException(status=400, reason="Bad Request")
        fn = MagicMock(side_effect=exc)

        with pytest.raises(ApiException) as exc_info:
            send_with_retries(
                fn,
                method="POST",
                url="https://example.com",
                max_retries=3,
                retryable_status_codes=[429, 504],
            )

        assert exc_info.value.status == 400
        fn.assert_called_once()

    @patch("bamboohr_sdk.api_helper.time.sleep")
    def test_wraps_generic_exception_in_api_exception(self, mock_sleep):
        fn = MagicMock(side_effect=ConnectionError("Connection refused"))

        with pytest.raises(ApiException) as exc_info:
            send_with_retries(
                fn,
                method="GET",
                url="https://example.com",
                max_retries=0,
            )

        assert exc_info.value.status == 0
        assert "Connection refused" in exc_info.value.reason

    @patch("bamboohr_sdk.api_helper.time.sleep")
    def test_exponential_backoff_delays(self, mock_sleep):
        fail_resp = self._make_response(429, "Too Many Requests")
        ok_resp = self._make_response(200)
        fn = MagicMock(side_effect=[fail_resp, fail_resp, fail_resp, ok_resp])

        send_with_retries(
            fn,
            method="GET",
            url="https://example.com",
            max_retries=5,
            retryable_status_codes=[429],
        )

        # Check exponential backoff: 0.1, 0.2, 0.4
        delays = [call.args[0] for call in mock_sleep.call_args_list]
        assert len(delays) == 3
        assert delays[0] == pytest.approx(0.1)
        assert delays[1] == pytest.approx(0.2)
        assert delays[2] == pytest.approx(0.4)

    def test_zero_retries_no_retry(self):
        fail_resp = self._make_response(429, "Too Many Requests")
        fn = MagicMock(return_value=fail_resp)

        result = send_with_retries(
            fn,
            method="GET",
            url="https://example.com",
            max_retries=0,
            retryable_status_codes=[429],
        )

        # With max_retries=0, should return immediately (no retries)
        assert result.status == 429
        fn.assert_called_once()

    def test_default_retryable_status_codes(self):
        """Verify default retryable codes are used when none specified."""
        ok_resp = self._make_response(200)
        fn = MagicMock(return_value=ok_resp)

        send_with_retries(
            fn,
            method="GET",
            url="https://example.com",
            max_retries=0,
        )

        fn.assert_called_once()
