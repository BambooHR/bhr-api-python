"""Tests for BambooHR SDK exceptions customizations (request_id support)."""

import pytest

from bamboohr_sdk.exceptions import (
    ApiException,
    BadRequestException,
    ServiceException,
    UnauthorizedException,
    _extract_request_id,
)


class TestRequestIdSupport:
    """Tests for request_id in ApiException."""

    def test_request_id_explicit(self):
        exc = ApiException(status=500, reason="Error", request_id="req-123")
        assert exc.request_id == "req-123"

    def test_request_id_default_none(self):
        exc = ApiException(status=400, reason="Bad")
        assert exc.request_id is None

    def test_request_id_in_str(self):
        exc = ApiException(status=500, reason="Error", request_id="req-abc")
        s = str(exc)
        assert "Request ID: req-abc" in s

    def test_no_request_id_in_str_when_none(self):
        exc = ApiException(status=500, reason="Error")
        s = str(exc)
        assert "Request ID" not in s

    def test_request_id_auto_extracted_from_x_request_id(self):
        class FakeResp:
            status = 500
            reason = "Error"
            data = b""
            def getheaders(self):
                return {"x-request-id": "auto-123"}

        exc = ApiException(http_resp=FakeResp())
        assert exc.request_id == "auto-123"

    def test_request_id_auto_extracted_from_x_bamboohr_request_id(self):
        class FakeResp:
            status = 500
            reason = "Error"
            data = b""
            def getheaders(self):
                return {"x-bamboohr-request-id": "bhr-456"}

        exc = ApiException(http_resp=FakeResp())
        assert exc.request_id == "bhr-456"

    def test_request_id_auto_extracted_from_request_id(self):
        class FakeResp:
            status = 500
            reason = "Error"
            data = b""
            def getheaders(self):
                return {"request-id": "plain-789"}

        exc = ApiException(http_resp=FakeResp())
        assert exc.request_id == "plain-789"

    def test_explicit_request_id_not_overridden_by_headers(self):
        class FakeResp:
            status = 500
            reason = "Error"
            data = b""
            def getheaders(self):
                return {"x-request-id": "from-header"}

        exc = ApiException(
            http_resp=FakeResp(), request_id="explicit-id"
        )
        assert exc.request_id == "explicit-id"

    def test_no_request_id_when_header_missing(self):
        class FakeResp:
            status = 500
            reason = "Error"
            data = b""
            def getheaders(self):
                return {"content-type": "text/plain"}

        exc = ApiException(http_resp=FakeResp())
        assert exc.request_id is None

    def test_subclass_inherits_request_id(self):
        exc = BadRequestException(
            status=400, reason="Bad", request_id="sub-123"
        )
        assert exc.request_id == "sub-123"

    def test_service_exception_request_id(self):
        exc = ServiceException(
            status=503, reason="Unavailable", request_id="svc-456"
        )
        assert exc.request_id == "svc-456"
        assert "Request ID: svc-456" in str(exc)


class TestExtractRequestId:
    """Tests for the _extract_request_id helper."""

    def test_returns_none_for_none_headers(self):
        assert _extract_request_id(None) is None

    def test_returns_none_for_empty_headers(self):
        assert _extract_request_id({}) is None

    def test_extracts_x_request_id(self):
        assert _extract_request_id({"x-request-id": "abc"}) == "abc"

    def test_priority_order(self):
        headers = {
            "x-request-id": "first",
            "x-bamboohr-request-id": "second",
            "request-id": "third",
        }
        assert _extract_request_id(headers) == "first"

    def test_falls_back_to_later_headers(self):
        headers = {"request-id": "fallback"}
        assert _extract_request_id(headers) == "fallback"
