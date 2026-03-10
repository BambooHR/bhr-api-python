"""Tests for BambooHR SDK Configuration customizations."""

import pytest

from bamboohr_sdk.configuration import Configuration


class TestHTTPSEnforcement:
    """Tests for HTTPS enforcement in Configuration."""

    def test_converts_http_to_https(self):
        c = Configuration(host="http://example.bamboohr.com")
        assert c.host == "https://example.bamboohr.com"

    def test_adds_https_when_no_scheme(self):
        c = Configuration(host="example.bamboohr.com")
        assert c.host == "https://example.bamboohr.com"

    def test_preserves_existing_https(self):
        c = Configuration(host="https://example.bamboohr.com")
        assert c.host == "https://example.bamboohr.com"

    def test_host_setter_enforces_https(self):
        c = Configuration()
        c.host = "http://new-host.bamboohr.com"
        assert c.host == "https://new-host.bamboohr.com"

    def test_host_setter_adds_https(self):
        c = Configuration()
        c.host = "new-host.bamboohr.com"
        assert c.host == "https://new-host.bamboohr.com"

    def test_default_host_is_https(self):
        c = Configuration()
        assert c.host.startswith("https://")

    def test_empty_host_not_modified(self):
        result = Configuration._enforce_https("")
        assert result == ""


class TestRetriesConfig:
    """Tests for application-level retries configuration."""

    def test_default_retries(self):
        c = Configuration()
        assert c.retries == 1

    def test_custom_retries(self):
        c = Configuration(retries=3)
        assert c.retries == 3

    def test_zero_retries(self):
        c = Configuration(retries=0)
        assert c.retries == 0

    def test_max_retries(self):
        c = Configuration(retries=5)
        assert c.retries == 5


class TestRetryableStatusCodes:
    """Tests for retryable status codes configuration."""

    def test_default_retryable_status_codes(self):
        c = Configuration()
        assert c.retryable_status_codes == [408, 429, 504, 598]

    def test_custom_retryable_status_codes(self):
        c = Configuration(retryable_status_codes=[429, 503])
        assert c.retryable_status_codes == [429, 503]

    def test_empty_retryable_status_codes(self):
        c = Configuration(retryable_status_codes=[])
        assert c.retryable_status_codes == []

    def test_retryable_status_codes_is_independent_copy(self):
        """Ensure modifying the config doesn't affect the default list."""
        c1 = Configuration()
        c2 = Configuration()
        c1.retryable_status_codes.append(503)
        assert 503 not in c2.retryable_status_codes


class TestSDKUserAgent:
    """Tests for SDK User-Agent configuration."""

    def test_sdk_user_agent_format(self):
        c = Configuration()
        ua = c.sdk_user_agent
        assert ua.startswith("BHR-SDK/")
        assert ua.endswith("/Python")

    def test_sdk_user_agent_contains_version(self):
        c = Configuration()
        # Should be BHR-SDK/{version}/Python
        parts = c.sdk_user_agent.split("/")
        assert len(parts) == 3
        assert parts[0] == "BHR-SDK"
        assert parts[2] == "Python"
        # Version should be a valid semver-like string
        assert len(parts[1]) > 0


class TestDebugReport:
    """Tests for the debug report."""

    def test_debug_report_contains_bamboohr(self):
        c = Configuration()
        report = c.to_debug_report()
        assert "BambooHR" in report
