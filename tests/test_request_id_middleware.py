"""Tests for bamboohr_sdk.client.middleware.request_id_middleware."""

import threading
from unittest.mock import MagicMock

import pytest

from bamboohr_sdk.client.middleware.request_id_middleware import (
    REQUEST_ID_HEADER,
    RequestIdMiddleware,
)


class TestRequestIdMiddleware:
    """Tests for RequestIdMiddleware."""

    def test_initial_last_request_id_is_none(self):
        mw = RequestIdMiddleware()
        assert mw.last_request_id is None

    def test_extract_from_getheader(self):
        """Extracts x-request-id via the getheader() interface (RESTResponse)."""
        mw = RequestIdMiddleware()
        response = MagicMock()
        response.getheader.return_value = "req-abc-123"
        result = mw.extract_request_id(response)
        assert result == "req-abc-123"
        assert mw.last_request_id == "req-abc-123"
        response.getheader.assert_called_once_with(REQUEST_ID_HEADER)

    def test_extract_from_headers_dict(self):
        """Falls back to response.headers.get() when getheader is absent."""
        mw = RequestIdMiddleware()
        response = MagicMock(spec=[])  # no getheader attribute
        response.headers = {REQUEST_ID_HEADER: "req-dict-456"}
        result = mw.extract_request_id(response)
        assert result == "req-dict-456"
        assert mw.last_request_id == "req-dict-456"

    def test_returns_none_when_header_missing(self):
        mw = RequestIdMiddleware()
        response = MagicMock()
        response.getheader.return_value = None
        response.headers = {}
        result = mw.extract_request_id(response)
        assert result is None
        assert mw.last_request_id is None

    def test_overwrites_previous_request_id(self):
        mw = RequestIdMiddleware()
        resp1 = MagicMock()
        resp1.getheader.return_value = "first-id"
        resp2 = MagicMock()
        resp2.getheader.return_value = "second-id"

        mw.extract_request_id(resp1)
        assert mw.last_request_id == "first-id"

        mw.extract_request_id(resp2)
        assert mw.last_request_id == "second-id"

    def test_reset_clears_request_id(self):
        mw = RequestIdMiddleware()
        response = MagicMock()
        response.getheader.return_value = "some-id"
        mw.extract_request_id(response)
        assert mw.last_request_id == "some-id"

        mw.reset()
        assert mw.last_request_id is None

    def test_thread_isolation(self):
        """Each thread should have its own last_request_id."""
        mw = RequestIdMiddleware()
        results = {}

        def worker(thread_name, request_id):
            response = MagicMock()
            response.getheader.return_value = request_id
            mw.extract_request_id(response)
            results[thread_name] = mw.last_request_id

        t1 = threading.Thread(target=worker, args=("t1", "id-thread-1"))
        t2 = threading.Thread(target=worker, args=("t2", "id-thread-2"))
        t1.start()
        t1.join()
        t2.start()
        t2.join()

        assert results["t1"] == "id-thread-1"
        assert results["t2"] == "id-thread-2"

    def test_getheader_returns_none_falls_back_to_headers(self):
        """When getheader returns None, falls back to headers dict."""
        mw = RequestIdMiddleware()
        response = MagicMock()
        response.getheader.return_value = None
        response.headers = {REQUEST_ID_HEADER: "fallback-id"}
        result = mw.extract_request_id(response)
        assert result == "fallback-id"
        assert mw.last_request_id == "fallback-id"

    def test_no_headers_attribute_and_no_getheader(self):
        """Handles objects with neither getheader nor headers gracefully."""
        mw = RequestIdMiddleware()
        response = MagicMock(spec=[])  # no attributes at all
        result = mw.extract_request_id(response)
        assert result is None
        assert mw.last_request_id is None
