"""Tests for BambooHR SDK exceptions customizations (request_id support)."""

import pytest

from bamboohr_sdk.exceptions import (
    ApiException,
    ClientException,
    ServerException,
    BadRequestException,
    AuthenticationFailedException,
    PermissionDeniedException,
    ResourceNotFoundException,
    MethodNotAllowedException,
    RequestTimeoutException,
    ConflictException,
    PayloadTooLargeException,
    UnsupportedMediaTypeException,
    UnprocessableEntityException,
    RateLimitExceededException,
    InternalServerErrorException,
    NotImplementedException,
    BadGatewayException,
    ServiceUnavailableException,
    GatewayTimeoutException,
    InsufficientStorageException,
    NetworkReadTimeoutException,
    _extract_request_id,
    _STATUS_TO_EXCEPTION_CLASS,
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

    def test_server_exception_request_id(self):
        exc = InternalServerErrorException(
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


# ---------------------------------------------------------------------------
# Exception hierarchy tests
# ---------------------------------------------------------------------------

CLIENT_EXCEPTIONS = [
    BadRequestException,
    AuthenticationFailedException,
    PermissionDeniedException,
    ResourceNotFoundException,
    MethodNotAllowedException,
    RequestTimeoutException,
    ConflictException,
    PayloadTooLargeException,
    UnsupportedMediaTypeException,
    UnprocessableEntityException,
    RateLimitExceededException,
]

SERVER_EXCEPTIONS = [
    InternalServerErrorException,
    NotImplementedException,
    BadGatewayException,
    ServiceUnavailableException,
    GatewayTimeoutException,
    InsufficientStorageException,
    NetworkReadTimeoutException,
]

ALL_SPECIFIC_EXCEPTIONS = CLIENT_EXCEPTIONS + SERVER_EXCEPTIONS


class TestExceptionHierarchy:
    """Tests for the exception class hierarchy."""

    @pytest.mark.parametrize("exc_class", CLIENT_EXCEPTIONS)
    def test_client_exceptions_inherit_from_client_exception(self, exc_class):
        assert issubclass(exc_class, ClientException)
        assert issubclass(exc_class, ApiException)

    @pytest.mark.parametrize("exc_class", SERVER_EXCEPTIONS)
    def test_server_exceptions_inherit_from_server_exception(self, exc_class):
        assert issubclass(exc_class, ServerException)
        assert issubclass(exc_class, ApiException)

    def test_client_exception_inherits_from_api_exception(self):
        assert issubclass(ClientException, ApiException)

    def test_server_exception_inherits_from_api_exception(self):
        assert issubclass(ServerException, ApiException)

    @pytest.mark.parametrize("exc_class", ALL_SPECIFIC_EXCEPTIONS)
    def test_all_exceptions_are_instantiable(self, exc_class):
        exc = exc_class(status=400, reason="test")
        assert exc.status == 400
        assert exc.reason == "test"


class TestPotentialCausesAndDebuggingTips:
    """Tests for potential_causes and debugging_tips on exception classes."""

    @pytest.mark.parametrize("exc_class", ALL_SPECIFIC_EXCEPTIONS)
    def test_has_potential_causes(self, exc_class):
        causes = exc_class.potential_causes()
        assert isinstance(causes, list)
        assert len(causes) > 0
        assert all(isinstance(c, str) for c in causes)

    @pytest.mark.parametrize("exc_class", ALL_SPECIFIC_EXCEPTIONS)
    def test_has_debugging_tips(self, exc_class):
        tips = exc_class.debugging_tips()
        assert isinstance(tips, list)
        assert len(tips) > 0
        assert all(isinstance(t, str) for t in tips)


class TestExceptionInheritanceChain:
    """Tests that specific exceptions are properly chained."""

    def test_authentication_failed_is_client_exception(self):
        exc = AuthenticationFailedException(status=401, reason="Unauthorized")
        assert isinstance(exc, ClientException)
        assert isinstance(exc, ApiException)

    def test_internal_server_error_is_server_exception(self):
        exc = InternalServerErrorException(status=500, reason="Error")
        assert isinstance(exc, ServerException)
        assert isinstance(exc, ApiException)


class TestStatusToExceptionClassMapping:
    """Tests for the _STATUS_TO_EXCEPTION_CLASS mapping."""

    def test_all_18_status_codes_mapped(self):
        expected_codes = {400, 401, 403, 404, 405, 408, 409, 413, 415, 422, 429, 500, 501, 502, 503, 504, 507, 598}
        assert set(_STATUS_TO_EXCEPTION_CLASS.keys()) == expected_codes

    def test_mapping_values_are_exception_subclasses(self):
        for code, exc_class in _STATUS_TO_EXCEPTION_CLASS.items():
            assert issubclass(exc_class, ApiException), f"Code {code} maps to non-ApiException class"


class TestFromResponse:
    """Tests for ApiException.from_response with specific exception classes."""

    def _make_fake_resp(self, status):
        class FakeResp:
            def __init__(self, s):
                self.status = s
                self.reason = "Test"
                self.data = b""
            def getheaders(self):
                return {}
        return FakeResp(status)

    @pytest.mark.parametrize(
        "status_code,expected_class",
        [
            (400, BadRequestException),
            (401, AuthenticationFailedException),
            (403, PermissionDeniedException),
            (404, ResourceNotFoundException),
            (405, MethodNotAllowedException),
            (408, RequestTimeoutException),
            (409, ConflictException),
            (413, PayloadTooLargeException),
            (415, UnsupportedMediaTypeException),
            (422, UnprocessableEntityException),
            (429, RateLimitExceededException),
            (500, InternalServerErrorException),
            (501, NotImplementedException),
            (502, BadGatewayException),
            (503, ServiceUnavailableException),
            (504, GatewayTimeoutException),
            (507, InsufficientStorageException),
            (598, NetworkReadTimeoutException),
        ],
    )
    def test_from_response_raises_specific_exception(self, status_code, expected_class):
        resp = self._make_fake_resp(status_code)
        with pytest.raises(expected_class):
            ApiException.from_response(http_resp=resp, body=None, data=None)

    def test_from_response_unknown_4xx_raises_client_exception(self):
        resp = self._make_fake_resp(418)
        with pytest.raises(ClientException):
            ApiException.from_response(http_resp=resp, body=None, data=None)

    def test_from_response_unknown_5xx_raises_server_exception(self):
        resp = self._make_fake_resp(599)
        with pytest.raises(ServerException):
            ApiException.from_response(http_resp=resp, body=None, data=None)

    def test_from_response_non_error_raises_api_exception(self):
        resp = self._make_fake_resp(302)
        with pytest.raises(ApiException):
            ApiException.from_response(http_resp=resp, body=None, data=None)
