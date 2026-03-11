"""Tests for bamboohr_sdk.client.auth.token_manager module."""

import time
from unittest.mock import MagicMock

import pytest

from bamboohr_sdk.client.auth.token_manager import (
    EXPIRY_BUFFER_SECONDS,
    TokenManager,
    TokenResponse,
)


# ===========================================================================
# TokenResponse
# ===========================================================================


class TestTokenResponse:
    """Tests for the TokenResponse dataclass."""

    def test_basic_fields(self):
        tr = TokenResponse(access_token="abc", refresh_token="def", expires_in=3600)
        assert tr.access_token == "abc"
        assert tr.refresh_token == "def"
        assert tr.expires_in == 3600

    def test_defaults(self):
        tr = TokenResponse(access_token="abc")
        assert tr.refresh_token is None
        assert tr.expires_in is None

    def test_has_refresh_token_true(self):
        tr = TokenResponse(access_token="a", refresh_token="r")
        assert tr.has_refresh_token is True

    def test_has_refresh_token_false(self):
        tr = TokenResponse(access_token="a")
        assert tr.has_refresh_token is False

    def test_get_expires_at_with_value(self):
        tr = TokenResponse(access_token="a", expires_in=3600)
        before = time.time()
        exp = tr.get_expires_at()
        after = time.time()
        assert exp is not None
        assert before + 3600 <= exp <= after + 3600

    def test_get_expires_at_none(self):
        tr = TokenResponse(access_token="a")
        assert tr.get_expires_at() is None

    def test_frozen(self):
        tr = TokenResponse(access_token="a")
        with pytest.raises(AttributeError):
            tr.access_token = "b"


# ===========================================================================
# TokenManager — construction
# ===========================================================================


class TestTokenManagerInit:
    """Tests for TokenManager construction."""

    def test_basic_init(self):
        tm = TokenManager(access_token="at", refresh_token="rt", expires_in=3600)
        assert tm.access_token == "at"
        assert tm.refresh_token == "rt"
        assert tm.has_refresh_capability is True

    def test_no_refresh_token(self):
        tm = TokenManager(access_token="at")
        assert tm.refresh_token is None
        assert tm.has_refresh_capability is False

    def test_expires_at_computed(self):
        before = time.time()
        tm = TokenManager(access_token="at", expires_in=100)
        after = time.time()
        assert tm.expires_at is not None
        assert before + 100 <= tm.expires_at <= after + 100

    def test_expires_at_none_without_expires_in(self):
        tm = TokenManager(access_token="at")
        assert tm.expires_at is None


# ===========================================================================
# TokenManager — expiration checks
# ===========================================================================


class TestNeedsRefresh:
    """Tests for TokenManager.needs_refresh()."""

    def test_false_without_refresh_token(self):
        tm = TokenManager(access_token="at", expires_in=1)
        assert tm.needs_refresh() is False

    def test_false_without_expires_at(self):
        tm = TokenManager(access_token="at", refresh_token="rt")
        assert tm.needs_refresh() is False

    def test_false_when_not_near_expiry(self):
        tm = TokenManager(
            access_token="at", refresh_token="rt", expires_in=EXPIRY_BUFFER_SECONDS + 600
        )
        assert tm.needs_refresh() is False

    def test_true_within_buffer(self):
        # Token expires in 60 seconds (well within the 300s buffer)
        tm = TokenManager(access_token="at", refresh_token="rt", expires_in=60)
        assert tm.needs_refresh() is True

    def test_true_when_expired(self):
        # Token already expired
        tm = TokenManager(access_token="at", refresh_token="rt", expires_in=-10)
        assert tm.needs_refresh() is True


class TestIsExpired:
    """Tests for TokenManager.is_expired()."""

    def test_false_when_no_expiry(self):
        tm = TokenManager(access_token="at")
        assert tm.is_expired() is False

    def test_false_when_not_expired(self):
        tm = TokenManager(access_token="at", expires_in=3600)
        assert tm.is_expired() is False

    def test_true_when_expired(self):
        tm = TokenManager(access_token="at", expires_in=-10)
        assert tm.is_expired() is True


class TestSecondsUntilExpiry:
    """Tests for TokenManager.seconds_until_expiry()."""

    def test_none_when_no_expiry(self):
        tm = TokenManager(access_token="at")
        assert tm.seconds_until_expiry() is None

    def test_positive_value(self):
        tm = TokenManager(access_token="at", expires_in=3600)
        secs = tm.seconds_until_expiry()
        assert secs is not None
        assert 3598 <= secs <= 3600

    def test_zero_when_expired(self):
        tm = TokenManager(access_token="at", expires_in=-100)
        assert tm.seconds_until_expiry() == 0.0


# ===========================================================================
# TokenManager — update_tokens
# ===========================================================================


class TestUpdateTokens:
    """Tests for TokenManager.update_tokens()."""

    def test_updates_access_token(self):
        tm = TokenManager(access_token="old-at", refresh_token="rt")
        tm.update_tokens(TokenResponse(access_token="new-at"))
        assert tm.access_token == "new-at"

    def test_updates_refresh_token_on_rotation(self):
        tm = TokenManager(access_token="at", refresh_token="old-rt")
        tm.update_tokens(TokenResponse(access_token="new-at", refresh_token="new-rt"))
        assert tm.refresh_token == "new-rt"

    def test_keeps_refresh_token_when_not_provided(self):
        tm = TokenManager(access_token="at", refresh_token="old-rt")
        tm.update_tokens(TokenResponse(access_token="new-at"))
        assert tm.refresh_token == "old-rt"

    def test_updates_expires_at(self):
        tm = TokenManager(access_token="at", expires_in=100)
        before = time.time()
        tm.update_tokens(TokenResponse(access_token="new", expires_in=7200))
        after = time.time()
        assert tm.expires_at is not None
        assert before + 7200 <= tm.expires_at <= after + 7200

    def test_clears_expires_at_when_none(self):
        tm = TokenManager(access_token="at", expires_in=100)
        tm.update_tokens(TokenResponse(access_token="new"))
        assert tm.expires_at is None

    def test_invokes_callback(self):
        callback = MagicMock()
        tm = TokenManager(
            access_token="old-at",
            refresh_token="old-rt",
            on_token_refresh=callback,
        )
        tm.update_tokens(TokenResponse(access_token="new-at", refresh_token="new-rt"))

        callback.assert_called_once_with("new-at", "new-rt", "old-at", "old-rt")

    def test_no_callback_when_not_set(self):
        tm = TokenManager(access_token="at")
        # Should not raise
        tm.update_tokens(TokenResponse(access_token="new"))

    def test_callback_receives_old_refresh_none(self):
        callback = MagicMock()
        tm = TokenManager(access_token="old-at", on_token_refresh=callback)
        tm.update_tokens(TokenResponse(access_token="new-at"))
        callback.assert_called_once_with("new-at", None, "old-at", None)


class TestSetRefreshCallback:
    """Tests for set_refresh_callback."""

    def test_replaces_callback(self):
        cb1 = MagicMock()
        cb2 = MagicMock()
        tm = TokenManager(access_token="at", on_token_refresh=cb1)
        tm.set_refresh_callback(cb2)
        tm.update_tokens(TokenResponse(access_token="new"))
        cb1.assert_not_called()
        cb2.assert_called_once()
