"""Tests for bamboohr_sdk.client.auth.token_refresh_provider module."""

import json

import pytest

from bamboohr_sdk.client.auth.token_refresh_provider import BambooHRTokenRefreshProvider
from bamboohr_sdk.exceptions import ApiException


def _fake_send(status_code, body_dict=None, body_str=None):
    """Return a fake http_send callable that returns a fixed response."""
    def send(req):
        b = body_str if body_str is not None else json.dumps(body_dict or {})
        return (status_code, {"Content-Type": "application/json"}, b)
    return send


# ===========================================================================
# Construction
# ===========================================================================


class TestConstruction:
    """Tests for provider construction."""

    def test_token_endpoint_derived_from_host(self):
        p = BambooHRTokenRefreshProvider("cid", "cs", "https://acme.bamboohr.com")
        assert p.token_endpoint == "https://acme.bamboohr.com/token.php?request=token"

    def test_trailing_slash_stripped(self):
        p = BambooHRTokenRefreshProvider("cid", "cs", "https://acme.bamboohr.com/")
        assert p.token_endpoint == "https://acme.bamboohr.com/token.php?request=token"

    def test_client_id_property(self):
        p = BambooHRTokenRefreshProvider("my-client", "cs")
        assert p.client_id == "my-client"


# ===========================================================================
# Successful refresh
# ===========================================================================


class TestSuccessfulRefresh:
    """Tests for successful token refresh responses."""

    def test_returns_token_response(self):
        send = _fake_send(200, {
            "access_token": "new-at",
            "refresh_token": "new-rt",
            "expires_in": 3600,
        })
        p = BambooHRTokenRefreshProvider("cid", "cs", http_send=send)
        tr = p.refresh_token("old-rt")
        assert tr.access_token == "new-at"
        assert tr.refresh_token == "new-rt"
        assert tr.expires_in == 3600

    def test_without_refresh_token_in_response(self):
        send = _fake_send(200, {"access_token": "new-at"})
        p = BambooHRTokenRefreshProvider("cid", "cs", http_send=send)
        tr = p.refresh_token("old-rt")
        assert tr.access_token == "new-at"
        assert tr.refresh_token is None
        assert tr.expires_in is None

    def test_without_expires_in(self):
        send = _fake_send(200, {"access_token": "a", "refresh_token": "r"})
        p = BambooHRTokenRefreshProvider("cid", "cs", http_send=send)
        tr = p.refresh_token("rt")
        assert tr.expires_in is None

    def test_sends_correct_params(self):
        """Verify the POST body includes the correct form parameters."""
        captured = {}

        def send(req):
            captured["url"] = req.full_url
            captured["data"] = req.data.decode("utf-8")
            captured["method"] = req.method
            captured["headers"] = dict(req.headers)
            return (200, {}, json.dumps({"access_token": "at"}))

        p = BambooHRTokenRefreshProvider(
            "my-cid", "my-secret", "https://acme.bamboohr.com", http_send=send
        )
        p.refresh_token("my-refresh-token")

        assert captured["method"] == "POST"
        assert "grant_type=refresh_token" in captured["data"]
        assert "refresh_token=my-refresh-token" in captured["data"]
        assert "client_id=my-cid" in captured["data"]
        assert "client_secret=my-secret" in captured["data"]
        assert captured["headers"]["Content-type"] == "application/x-www-form-urlencoded"


# ===========================================================================
# Error cases
# ===========================================================================


class TestRefreshErrors:
    """Tests for error handling during token refresh."""

    def test_non_2xx_raises_api_exception(self):
        send = _fake_send(400, {"error": "invalid_grant"})
        p = BambooHRTokenRefreshProvider("cid", "cs", http_send=send)
        with pytest.raises(ApiException) as exc_info:
            p.refresh_token("bad-rt")
        assert exc_info.value.status == 400

    def test_invalid_json_raises_api_exception(self):
        send = _fake_send(200, body_str="not-json{{{")
        p = BambooHRTokenRefreshProvider("cid", "cs", http_send=send)
        with pytest.raises(ApiException) as exc_info:
            p.refresh_token("rt")
        assert exc_info.value.status == 500
        assert "Invalid JSON" in exc_info.value.reason

    def test_missing_access_token_raises(self):
        send = _fake_send(200, {"refresh_token": "rt"})
        p = BambooHRTokenRefreshProvider("cid", "cs", http_send=send)
        with pytest.raises(ApiException) as exc_info:
            p.refresh_token("rt")
        assert "access_token" in exc_info.value.reason

    def test_server_error(self):
        send = _fake_send(500, {"error": "server_error"})
        p = BambooHRTokenRefreshProvider("cid", "cs", http_send=send)
        with pytest.raises(ApiException) as exc_info:
            p.refresh_token("rt")
        assert exc_info.value.status == 500
