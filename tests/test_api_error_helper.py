"""Tests for bamboohr_sdk.api_error_helper module."""

import pytest

from bamboohr_sdk.api_error_helper import (
    ERROR_MESSAGES,
    create_exception,
    format_detailed_error_message,
    get_error_info,
)
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
)


class TestCreateException:
    """Tests for the create_exception factory."""

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
            (418, ClientException),  # Unknown 4xx → base ClientException
            (599, ServerException),  # Unknown 5xx → base ServerException
            (302, ApiException),  # Non-error status → base ApiException
        ],
    )
    def test_creates_correct_exception_class(self, status_code, expected_class):
        exc = create_exception(status_code, "test reason")
        assert isinstance(exc, expected_class)
        assert exc.status == status_code

    def test_includes_request_id_in_reason(self):
        exc = create_exception(500, "Server Error", request_id="req-abc-123")
        assert "req-abc-123" in exc.reason

    def test_without_request_id(self):
        exc = create_exception(404, "Not Found")
        assert exc.reason == "Not Found"

    def test_attaches_headers(self):
        headers = {"content-type": "application/json"}
        exc = create_exception(400, "Bad Request", headers=headers)
        assert exc.headers == headers

    def test_attaches_body(self):
        exc = create_exception(500, "Error", body='{"error": "details"}')
        assert exc.body == '{"error": "details"}'

    def test_attaches_request_id_attribute(self):
        exc = create_exception(401, "Unauthorized", request_id="req-xyz")
        assert exc.request_id == "req-xyz"


class TestGetErrorInfo:
    """Tests for the get_error_info lookup."""

    def test_known_status_code(self):
        info = get_error_info(429)
        assert info is not None
        assert info["type"] == "RateLimitExceeded"
        assert "causes" in info
        assert "tips" in info

    def test_unknown_status_code_returns_none(self):
        assert get_error_info(999) is None

    @pytest.mark.parametrize(
        "status_code",
        [400, 401, 403, 404, 405, 408, 409, 413, 415, 422, 429, 500, 501, 502, 503, 504, 507, 598],
    )
    def test_all_documented_codes_have_entries(self, status_code):
        info = get_error_info(status_code)
        assert info is not None
        assert "type" in info
        assert "title" in info
        assert "causes" in info
        assert "tips" in info
        assert len(info["causes"]) > 0
        assert len(info["tips"]) > 0


class TestFormatDetailedErrorMessage:
    """Tests for format_detailed_error_message."""

    def test_base_message_only(self):
        msg = format_detailed_error_message("Something failed")
        assert msg == "Something failed"

    def test_with_request_id(self):
        msg = format_detailed_error_message("Failed", request_id="req-123")
        assert "req-123" in msg

    def test_with_causes(self):
        msg = format_detailed_error_message(
            "Error", causes=["Cause A", "Cause B"]
        )
        assert "This could be due to:" in msg
        assert "- Cause A" in msg
        assert "- Cause B" in msg

    def test_with_tips(self):
        msg = format_detailed_error_message("Error", tips=["Try X", "Try Y"])
        assert "Debugging tips:" in msg
        assert "- Try X" in msg
        assert "- Try Y" in msg

    def test_with_tips_and_request_id(self):
        msg = format_detailed_error_message(
            "Error", tips=["Try X"], request_id="req-456"
        )
        assert "Include this Request ID (req-456)" in msg

    def test_full_message(self):
        msg = format_detailed_error_message(
            "Request failed",
            causes=["Bad input"],
            tips=["Check params"],
            request_id="req-789",
        )
        assert "Request failed [Request ID: req-789]" in msg
        assert "- Bad input" in msg
        assert "- Check params" in msg
