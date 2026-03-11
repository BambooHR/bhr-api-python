"""Tests for bamboohr_sdk.client.auth_builder module."""

import pytest

from bamboohr_sdk.client.auth_builder import AuthBuilder
from bamboohr_sdk.client.logger.secure_log_filter import mask_value
from bamboohr_sdk.configuration import Configuration


class TestWithApiKey:
    """Tests for API key authentication."""

    def test_configures_api_key(self):
        ab = AuthBuilder().with_api_key("my-key")
        assert ab.auth_type == "api_key"
        assert ab.is_configured is True

    def test_empty_api_key_raises(self):
        with pytest.raises(ValueError, match="API key cannot be empty"):
            AuthBuilder().with_api_key("")

    def test_apply_sets_basic_auth(self):
        config = Configuration(host="https://acme.bamboohr.com")
        AuthBuilder().with_api_key("test-key").apply_to(config)
        assert config.username == "test-key"
        assert config.password == "x"


class TestWithOAuth:
    """Tests for OAuth bearer token authentication."""

    def test_configures_oauth(self):
        ab = AuthBuilder().with_oauth("token-abc")
        assert ab.auth_type == "oauth"
        assert ab.is_configured is True

    def test_empty_oauth_token_raises(self):
        with pytest.raises(ValueError, match="OAuth token cannot be empty"):
            AuthBuilder().with_oauth("")

    def test_apply_sets_access_token(self):
        config = Configuration(host="https://acme.bamboohr.com")
        AuthBuilder().with_oauth("bearer-token").apply_to(config)
        assert config.access_token == "bearer-token"


class TestWithOAuthRefresh:
    """Tests for OAuth with automatic token refresh."""

    def _builder(self, **overrides):
        defaults = {
            "access_token": "access-123",
            "refresh_token": "refresh-456",
            "client_id": "cid",
            "client_secret": "csecret",
        }
        defaults.update(overrides)
        return AuthBuilder().with_oauth_refresh(**defaults)

    def test_configures_oauth_refresh(self):
        ab = self._builder()
        assert ab.auth_type == "oauth_refresh"
        assert ab.has_oauth_refresh is True
        assert ab.refresh_token == "refresh-456"
        assert ab.client_id == "cid"
        assert ab.client_secret == "csecret"

    def test_with_expires_in(self):
        ab = self._builder(expires_in=3600)
        assert ab.expires_in == 3600

    def test_empty_access_token_raises(self):
        with pytest.raises(ValueError, match="access token"):
            AuthBuilder().with_oauth_refresh("", "r", "c", "s")

    def test_empty_refresh_token_raises(self):
        with pytest.raises(ValueError, match="refresh token"):
            AuthBuilder().with_oauth_refresh("a", "", "c", "s")

    def test_empty_client_id_raises(self):
        with pytest.raises(ValueError, match="client ID"):
            AuthBuilder().with_oauth_refresh("a", "r", "", "s")

    def test_empty_client_secret_raises(self):
        with pytest.raises(ValueError, match="client secret"):
            AuthBuilder().with_oauth_refresh("a", "r", "c", "")

    def test_apply_sets_access_token(self):
        config = Configuration(host="https://acme.bamboohr.com")
        self._builder().apply_to(config)
        assert config.access_token == "access-123"


class TestOnTokenRefresh:
    """Tests for the token refresh callback."""

    def test_registers_callback(self):
        cb = lambda *a: None
        ab = AuthBuilder().with_api_key("k").on_token_refresh(cb)
        assert ab.token_refresh_callback is cb

    def test_non_callable_raises(self):
        with pytest.raises(TypeError, match="callable"):
            AuthBuilder().on_token_refresh("not-a-function")


class TestValidate:
    """Tests for AuthBuilder.validate()."""

    def test_unconfigured_raises(self):
        with pytest.raises(ValueError, match="No authentication method"):
            AuthBuilder().validate()

    def test_api_key_valid(self):
        AuthBuilder().with_api_key("k").validate()  # should not raise

    def test_oauth_valid(self):
        AuthBuilder().with_oauth("t").validate()  # should not raise

    def test_oauth_refresh_valid(self):
        AuthBuilder().with_oauth_refresh("a", "r", "c", "s").validate()


class TestApplyToWithoutConfig:
    """Tests for apply_to without configuration."""

    def test_unconfigured_raises(self):
        config = Configuration(host="https://acme.bamboohr.com")
        with pytest.raises(ValueError, match="No authentication method"):
            AuthBuilder().apply_to(config)


class TestGetSanitizedInfo:
    """Tests for sanitized info output."""

    def test_unconfigured(self):
        info = AuthBuilder().get_sanitized_info()
        assert info == {"type": "none", "configured": False}

    def test_api_key_masks_secret(self):
        info = AuthBuilder().with_api_key("abcdefghijklmnop").get_sanitized_info()
        assert info["type"] == "api_key"
        assert info["configured"] is True
        assert "abcdefghijklmnop" not in info["api_key"]
        assert info["api_key"].startswith("abcd")
        assert info["api_key"].endswith("mnop")

    def test_oauth_masks_token(self):
        info = AuthBuilder().with_oauth("token-very-long-value").get_sanitized_info()
        assert "token-very-long-value" not in info["oauth_token"]

    def test_oauth_refresh_includes_client_id(self):
        info = (
            AuthBuilder()
            .with_oauth_refresh("a-long-token", "r-long-token", "my-client", "secret")
            .get_sanitized_info()
        )
        assert info["client_id"] == "my-client"
        assert info["has_callback"] is False

    def test_oauth_refresh_with_callback(self):
        info = (
            AuthBuilder()
            .with_oauth_refresh("a-long-token", "r-long-token", "cid", "csec")
            .on_token_refresh(lambda *a: None)
            .get_sanitized_info()
        )
        assert info["has_callback"] is True


class TestReset:
    """Tests for reset."""

    def test_clears_all_state(self):
        ab = AuthBuilder().with_api_key("k").on_token_refresh(lambda *a: None)
        ab.reset()
        assert ab.is_configured is False
        assert ab.auth_type is None
        assert ab.token_refresh_callback is None


class TestMaskValue:
    """Tests for the mask_value utility."""

    def test_short_value(self):
        assert mask_value("short") == "[REDACTED]"

    def test_none_value(self):
        assert mask_value(None) == "[EMPTY]"

    def test_empty_value(self):
        assert mask_value("") == "[EMPTY]"

    def test_long_value(self):
        result = mask_value("abcdefghijklmnop")
        assert result == "abcd****mnop"

    def test_exactly_8_chars(self):
        assert mask_value("12345678") == "[REDACTED]"

    def test_9_chars(self):
        result = mask_value("123456789")
        assert result == "1234****6789"
