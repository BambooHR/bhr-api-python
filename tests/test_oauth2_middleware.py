"""Tests for bamboohr_sdk.client.middleware.oauth2_middleware module."""

from unittest.mock import MagicMock, patch

import pytest

from bamboohr_sdk.client.auth.token_manager import TokenManager, TokenResponse
from bamboohr_sdk.client.auth.token_refresh_provider import BambooHRTokenRefreshProvider
from bamboohr_sdk.client.middleware.oauth2_middleware import OAuth2Middleware
from bamboohr_sdk.configuration import Configuration
from bamboohr_sdk.exceptions import ApiException


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_middleware(
    expires_in=3600,
    refresh_token="rt",
    access_token="at",
    provider_response=None,
):
    """Create a middleware with mocked refresh provider."""
    config = Configuration(host="https://acme.bamboohr.com")
    config.access_token = access_token

    tm = TokenManager(
        access_token=access_token,
        refresh_token=refresh_token,
        expires_in=expires_in,
    )

    provider = MagicMock(spec=BambooHRTokenRefreshProvider)
    if provider_response is not None:
        provider.refresh_token.return_value = provider_response
    else:
        provider.refresh_token.return_value = TokenResponse(
            access_token="refreshed-at",
            refresh_token="refreshed-rt",
            expires_in=7200,
        )

    mw = OAuth2Middleware(
        token_manager=tm,
        refresh_provider=provider,
        config=config,
    )
    return mw, config, provider


# ===========================================================================
# No-op when no refresh capability
# ===========================================================================


class TestNoRefreshCapability:
    """When no refresh token is present, middleware is a pass-through."""

    def test_passes_through(self):
        config = Configuration(host="https://acme.bamboohr.com")
        tm = TokenManager(access_token="at")  # no refresh_token
        provider = MagicMock()
        mw = OAuth2Middleware(tm, provider, config)

        response = MagicMock()
        result = mw.handle(lambda: response)

        assert result is response
        provider.refresh_token.assert_not_called()


# ===========================================================================
# Proactive refresh
# ===========================================================================


class TestProactiveRefresh:
    """Token is refreshed before the request when near expiry."""

    def test_refreshes_when_token_near_expiry(self):
        mw, config, provider = _make_middleware(expires_in=60)  # within 300s buffer

        response = MagicMock()
        result = mw.handle(lambda: response)

        assert result is response
        provider.refresh_token.assert_called_once_with("rt")
        assert config.access_token == "refreshed-at"

    def test_proceeds_if_proactive_refresh_fails(self):
        mw, config, provider = _make_middleware(expires_in=60)
        provider.refresh_token.side_effect = ApiException(status=500, reason="fail")

        response = MagicMock()
        result = mw.handle(lambda: response)

        # Should still succeed — proactive failure is non-fatal
        assert result is response

    def test_no_proactive_refresh_when_not_near_expiry(self):
        mw, config, provider = _make_middleware(expires_in=3600)

        response = MagicMock()
        mw.handle(lambda: response)

        provider.refresh_token.assert_not_called()


# ===========================================================================
# Reactive refresh on 401
# ===========================================================================


class TestReactiveRefresh:
    """Token is refreshed on 401 and request is retried."""

    def test_retries_on_401(self):
        mw, config, provider = _make_middleware(expires_in=3600)

        call_count = 0

        def send_request():
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                raise ApiException(status=401, reason="Unauthorized")
            return MagicMock(status=200)

        result = mw.handle(send_request)

        assert call_count == 2
        provider.refresh_token.assert_called_once_with("rt")
        assert config.access_token == "refreshed-at"
        assert result.status == 200

    def test_raises_if_refresh_fails_on_401(self):
        mw, config, provider = _make_middleware(expires_in=3600)
        provider.refresh_token.side_effect = ApiException(status=500, reason="fail")

        def send_request():
            raise ApiException(status=401, reason="Unauthorized")

        with pytest.raises(ApiException) as exc_info:
            mw.handle(send_request)
        # Should raise the original 401, not the 500 from refresh
        assert exc_info.value.status == 401

    def test_non_401_exception_propagates(self):
        mw, config, provider = _make_middleware(expires_in=3600)

        def send_request():
            raise ApiException(status=403, reason="Forbidden")

        with pytest.raises(ApiException) as exc_info:
            mw.handle(send_request)
        assert exc_info.value.status == 403
        provider.refresh_token.assert_not_called()


# ===========================================================================
# Recursive refresh guard
# ===========================================================================


class TestRecursiveRefreshGuard:
    """Middleware does not retry refresh if already refreshing."""

    def test_does_not_loop(self):
        mw, config, provider = _make_middleware(expires_in=3600)

        # Simulate: first request → 401 → refresh succeeds → retry → 401 again
        call_count = 0

        def send_request():
            nonlocal call_count
            call_count += 1
            raise ApiException(status=401, reason="Unauthorized")

        # The middleware should: attempt → 401 → refresh → retry → 401 → raise
        # (it won't try to refresh again the second time because _is_refreshing
        # is False by then but the call_count proves it only retried once)
        with pytest.raises(ApiException) as exc_info:
            mw.handle(send_request)
        assert exc_info.value.status == 401
        # Called twice: original + one retry after refresh
        assert call_count == 2


# ===========================================================================
# Config synchronization
# ===========================================================================


class TestConfigSync:
    """Configuration.access_token stays in sync after refresh."""

    def test_config_updated_on_proactive_refresh(self):
        mw, config, provider = _make_middleware(expires_in=10)
        mw.handle(lambda: MagicMock())
        assert config.access_token == "refreshed-at"

    def test_config_updated_on_reactive_refresh(self):
        mw, config, provider = _make_middleware(expires_in=3600)

        first_call = True

        def send():
            nonlocal first_call
            if first_call:
                first_call = False
                raise ApiException(status=401, reason="Unauthorized")
            return MagicMock()

        mw.handle(send)
        assert config.access_token == "refreshed-at"


# ===========================================================================
# Token manager update
# ===========================================================================


class TestTokenManagerUpdate:
    """TokenManager tokens are updated after refresh."""

    def test_token_manager_updated_on_refresh(self):
        mw, config, provider = _make_middleware(expires_in=10)
        mw.handle(lambda: MagicMock())
        assert mw.token_manager.access_token == "refreshed-at"
        assert mw.token_manager.refresh_token == "refreshed-rt"


# ===========================================================================
# is_refreshing property
# ===========================================================================


class TestIsRefreshing:
    """Tests for the is_refreshing flag."""

    def test_false_by_default(self):
        mw, _, _ = _make_middleware()
        assert mw.is_refreshing is False

    def test_false_after_refresh(self):
        mw, _, _ = _make_middleware(expires_in=10)
        mw.handle(lambda: MagicMock())
        assert mw.is_refreshing is False

    def test_false_after_failed_refresh(self):
        mw, _, provider = _make_middleware(expires_in=10)
        provider.refresh_token.side_effect = Exception("boom")
        # Proactive fails but request still goes through
        mw.handle(lambda: MagicMock())
        assert mw.is_refreshing is False
