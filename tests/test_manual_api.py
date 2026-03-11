"""Tests for bamboohr_sdk.api.manual_api module."""

import json
from unittest.mock import MagicMock, patch, PropertyMock

import pytest

from bamboohr_sdk.api.manual_api import ManualApi
from bamboohr_sdk.api_client import ApiClient
from bamboohr_sdk.api_response import ApiResponse
from bamboohr_sdk.client.bamboohr_client import BambooHRClient
from bamboohr_sdk.exceptions import (
    ApiException,
    BadRequestException,
    AuthenticationFailedException,
    PermissionDeniedException,
    ResourceNotFoundException,
    InternalServerErrorException,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _build_client(**kwargs) -> BambooHRClient:
    """Return a fully-built client with sensible defaults."""
    defaults = {"api_key": "test-api-key", "domain": "acme"}
    defaults.update(kwargs)
    c = BambooHRClient()
    if defaults.get("api_key"):
        c.with_api_key(defaults["api_key"])
    if defaults.get("domain"):
        c.for_company(defaults["domain"])
    return c.build()


def _mock_response(status=200, body=b'{"ok": true}', headers=None):
    """Create a mock RESTResponse."""
    resp = MagicMock()
    resp.status = status
    resp.reason = "OK" if status == 200 else "Error"
    resp.data = body
    resp.read.return_value = body
    resp.getheaders.return_value = headers or {"content-type": "application/json"}
    resp.getheader.side_effect = lambda name, default=None: (headers or {}).get(name, default)
    return resp


# ===========================================================================
# Construction
# ===========================================================================


class TestManualApiConstruction:
    """Tests for ManualApi initialisation."""

    def test_uses_provided_api_client(self):
        client = _build_client()
        api = ManualApi(api_client=client.api_client)
        assert api.api_client is client.api_client

    def test_defaults_to_default_api_client(self):
        api = ManualApi()
        assert api.api_client is not None

    def test_accessible_via_bamboohr_client(self):
        client = _build_client()
        api = client.manual()
        assert isinstance(api, ManualApi)
        assert api.api_client is client.api_client

    def test_cached_via_bamboohr_client(self):
        client = _build_client()
        api1 = client.manual()
        api2 = client.manual()
        assert api1 is api2


# ===========================================================================
# GET requests
# ===========================================================================


class TestGet:
    """Tests for ManualApi.get()."""

    def test_basic_get(self):
        client = _build_client()
        api = client.manual()
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response()
            resp = api.get("/api/gateway.php/acme/v1/employees/directory")

        assert isinstance(resp, ApiResponse)
        assert resp.status_code == 200
        assert resp.data == {"ok": True}

    def test_get_with_query_params(self):
        client = _build_client()
        api = client.manual()
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response()
            api.get("/api/gateway.php/acme/v1/employees", query_params={"status": "active"})

        _, kwargs = mock_req.call_args
        # The URL should contain the query parameter
        call_args = mock_req.call_args
        url = call_args[0][1] if len(call_args[0]) > 1 else kwargs.get("url", "")
        assert "status=active" in url

    def test_get_with_custom_headers(self):
        client = _build_client()
        api = client.manual()
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response()
            api.get(
                "/api/gateway.php/acme/v1/test",
                headers={"X-Custom": "value"},
            )

        call_args = mock_req.call_args
        sent_headers = call_args[1].get("headers", call_args[0][2] if len(call_args[0]) > 2 else {})
        assert sent_headers.get("X-Custom") == "value"

    def test_get_includes_auth_header(self):
        client = _build_client()
        api = client.manual()
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response()
            api.get("/api/gateway.php/acme/v1/test")

        call_args = mock_req.call_args
        sent_headers = call_args[1].get("headers", call_args[0][2] if len(call_args[0]) > 2 else {})
        assert "Authorization" in sent_headers

    def test_get_includes_user_agent(self):
        client = _build_client()
        api = client.manual()
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response()
            api.get("/api/gateway.php/acme/v1/test")

        call_args = mock_req.call_args
        sent_headers = call_args[1].get("headers", call_args[0][2] if len(call_args[0]) > 2 else {})
        assert "User-Agent" in sent_headers

    def test_get_with_timeout(self):
        client = _build_client()
        api = client.manual()
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response()
            api.get("/api/gateway.php/acme/v1/test", _request_timeout=5.0)

        _, kwargs = mock_req.call_args
        assert kwargs["_request_timeout"] == 5.0


# ===========================================================================
# POST requests
# ===========================================================================


class TestPost:
    """Tests for ManualApi.post()."""

    def test_post_with_json_body(self):
        client = _build_client()
        api = client.manual()
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response(status=201, body=b'{"id": 42}')
            resp = api.post(
                "/api/gateway.php/acme/v1/employees",
                body={"firstName": "Jane", "lastName": "Doe"},
            )

        assert resp.status_code == 201
        assert resp.data == {"id": 42}

    def test_post_with_string_body(self):
        client = _build_client()
        api = client.manual()
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response()
            api.post(
                "/api/gateway.php/acme/v1/test",
                body="raw string body",
            )

        # Should not raise
        mock_req.assert_called_once()

    def test_post_with_no_body(self):
        client = _build_client()
        api = client.manual()
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response()
            api.post("/api/gateway.php/acme/v1/test")

        mock_req.assert_called_once()


# ===========================================================================
# PUT requests
# ===========================================================================


class TestPut:
    """Tests for ManualApi.put()."""

    def test_put_with_body(self):
        client = _build_client()
        api = client.manual()
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response()
            resp = api.put(
                "/api/gateway.php/acme/v1/employees/123",
                body={"firstName": "Updated"},
            )

        assert resp.status_code == 200


# ===========================================================================
# DELETE requests
# ===========================================================================


class TestDelete:
    """Tests for ManualApi.delete()."""

    def test_delete_basic(self):
        client = _build_client()
        api = client.manual()
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response()
            resp = api.delete("/api/gateway.php/acme/v1/employees/123")

        assert resp.status_code == 200

    def test_delete_with_body(self):
        client = _build_client()
        api = client.manual()
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response()
            resp = api.delete(
                "/api/gateway.php/acme/v1/employees/123",
                body={"reason": "test"},
            )

        assert resp.status_code == 200


# ===========================================================================
# Error handling
# ===========================================================================


class TestErrorHandling:
    """Tests for error handling in ManualApi."""

    def test_400_raises_bad_request(self):
        client = _build_client()
        api = client.manual()
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response(status=400, body=b'{"error": "bad input"}')
            with pytest.raises(BadRequestException) as exc_info:
                api.get("/api/gateway.php/acme/v1/test")
            assert exc_info.value.status == 400

    def test_401_raises_authentication_failed(self):
        client = _build_client()
        api = client.manual()
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response(status=401, body=b'{"error": "unauthorized"}')
            with pytest.raises(AuthenticationFailedException):
                api.get("/api/gateway.php/acme/v1/test")

    def test_403_raises_permission_denied(self):
        client = _build_client()
        api = client.manual()
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response(status=403, body=b'{"error": "forbidden"}')
            with pytest.raises(PermissionDeniedException):
                api.get("/api/gateway.php/acme/v1/test")

    def test_404_raises_not_found(self):
        client = _build_client()
        api = client.manual()
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response(status=404, body=b'{"error": "not found"}')
            with pytest.raises(ResourceNotFoundException):
                api.get("/api/gateway.php/acme/v1/test")

    def test_500_raises_internal_server_error(self):
        client = _build_client()
        api = client.manual()
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response(status=500, body=b'{"error": "server error"}')
            with pytest.raises(InternalServerErrorException):
                api.get("/api/gateway.php/acme/v1/test")


# ===========================================================================
# Response handling
# ===========================================================================


class TestResponseHandling:
    """Tests for response data handling."""

    def test_json_response_decoded(self):
        client = _build_client()
        api = client.manual()
        body = json.dumps({"employees": [{"id": 1}, {"id": 2}]}).encode()
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response(body=body)
            resp = api.get("/api/gateway.php/acme/v1/employees")

        assert resp.data == {"employees": [{"id": 1}, {"id": 2}]}

    def test_non_json_response_returned_as_string(self):
        client = _build_client()
        api = client.manual()
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response(body=b"<xml>data</xml>")
            resp = api.get("/api/gateway.php/acme/v1/test")

        assert resp.data == "<xml>data</xml>"

    def test_empty_response_body(self):
        client = _build_client()
        api = client.manual()
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response(body=b"")
            resp = api.get("/api/gateway.php/acme/v1/test")

        assert resp.data is None
        assert resp.status_code == 200

    def test_raw_data_available(self):
        client = _build_client()
        api = client.manual()
        raw = b'{"key": "value"}'
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response(body=raw)
            resp = api.get("/api/gateway.php/acme/v1/test")

        assert resp.raw_data == raw

    def test_headers_available(self):
        client = _build_client()
        api = client.manual()
        resp_headers = {"content-type": "application/json", "x-request-id": "abc-123"}
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response(headers=resp_headers)
            resp = api.get("/api/gateway.php/acme/v1/test")

        assert resp.headers == resp_headers


# ===========================================================================
# Request method
# ===========================================================================


class TestRequestMethod:
    """Tests for the core request() method."""

    def test_custom_method_patch(self):
        client = _build_client()
        api = client.manual()
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response()
            resp = api.request("PATCH", "/api/gateway.php/acme/v1/test")

        assert resp.status_code == 200
        call_args = mock_req.call_args
        assert call_args[0][0] == "PATCH"

    def test_method_uppercased(self):
        client = _build_client()
        api = client.manual()
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response()
            api.request("get", "/api/gateway.php/acme/v1/test")

        call_args = mock_req.call_args
        assert call_args[0][0] == "GET"


# ===========================================================================
# OAuth authentication
# ===========================================================================


class TestOAuthAuth:
    """Tests for OAuth authentication through ManualApi."""

    def test_oauth_bearer_token_included(self):
        client = BambooHRClient().with_oauth("my-oauth-token").for_company("acme").build()
        api = client.manual()
        with patch.object(client.api_client.rest_client, "request") as mock_req:
            mock_req.return_value = _mock_response()
            api.get("/api/gateway.php/acme/v1/test")

        call_args = mock_req.call_args
        sent_headers = call_args[1].get("headers", call_args[0][2] if len(call_args[0]) > 2 else {})
        auth = sent_headers.get("Authorization", "")
        assert auth.startswith("Bearer ")
        assert "my-oauth-token" in auth


# ===========================================================================
# Helper methods
# ===========================================================================


class TestHelpers:
    """Tests for ManualApi helper methods."""

    def test_dict_to_query_tuples_none(self):
        assert ManualApi._dict_to_query_tuples(None) is None

    def test_dict_to_query_tuples_empty(self):
        assert ManualApi._dict_to_query_tuples({}) is None

    def test_dict_to_query_tuples_converts(self):
        result = ManualApi._dict_to_query_tuples({"a": "1", "b": 2})
        assert ("a", "1") in result
        assert ("b", "2") in result

    def test_prepare_body_none(self):
        assert ManualApi._prepare_body(None) is None

    def test_prepare_body_dict(self):
        body = {"key": "value"}
        assert ManualApi._prepare_body(body) == body

    def test_prepare_body_list(self):
        body = [1, 2, 3]
        assert ManualApi._prepare_body(body) == body

    def test_prepare_body_string(self):
        assert ManualApi._prepare_body("raw") == "raw"
