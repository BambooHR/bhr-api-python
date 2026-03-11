"""Manual API for custom/ad-hoc API calls.

Allows developers to make HTTP requests to BambooHR endpoints that are not
yet covered by the auto-generated SDK, while still leveraging the built-in
authentication, error handling, retry logic, and logging infrastructure.

This class is **hand-written** (not auto-generated).

Usage::

    client = BambooHRClient().with_api_key("key").for_company("acme").build()
    api = client.manual()

    # Simple GET
    response = api.get("/api/gateway.php/acme/v1/employees/directory")

    # POST with JSON body
    response = api.post(
        "/api/gateway.php/acme/v1/employees",
        body={"firstName": "Jane", "lastName": "Doe"},
    )

"""

from __future__ import annotations

import json
import logging
from typing import Any, Dict, List, Optional, Tuple, Union
from urllib.parse import urlencode

from bamboohr_sdk.api_client import ApiClient
from bamboohr_sdk.api_response import ApiResponse
from bamboohr_sdk import rest
from bamboohr_sdk.exceptions import ApiException

logger = logging.getLogger("bamboohr_sdk")


class ManualApi:
    """Provides manual/custom API calls using the SDK infrastructure.

    All requests go through the same :class:`~bamboohr_sdk.api_client.ApiClient`
    pipeline as the auto-generated endpoints, which means they automatically
    get:

    - **Authentication** (API key or OAuth Bearer token)
    - **Default headers** (User-Agent, etc.)
    - **Retry logic** with exponential backoff
    - **Timeout** from :class:`~bamboohr_sdk.configuration.Configuration`
    - **Request ID tracking** via :class:`RequestIdMiddleware`
    - **Error handling** with typed exceptions

    :param api_client: An :class:`ApiClient` instance (usually provided by
        :class:`~bamboohr_sdk.client.bamboohr_client.BambooHRClient`).
    """

    def __init__(self, api_client: Optional[ApiClient] = None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    # ------------------------------------------------------------------
    # Convenience HTTP-verb methods
    # ------------------------------------------------------------------

    def get(
        self,
        resource_path: str,
        query_params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        _request_timeout: Optional[Union[float, Tuple[float, float]]] = None,
    ) -> ApiResponse:
        """Perform a GET request.

        :param resource_path: API path (e.g. ``"/api/gateway.php/acme/v1/employees/directory"``).
        :param query_params: Optional query string parameters.
        :param headers: Optional extra headers (merged with defaults).
        :param _request_timeout: Per-request timeout override.
        :return: :class:`ApiResponse` with ``status_code``, ``data``, ``headers``, and ``raw_data``.
        """
        return self.request("GET", resource_path, query_params=query_params, headers=headers, _request_timeout=_request_timeout)

    def post(
        self,
        resource_path: str,
        query_params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        body: Any = None,
        _request_timeout: Optional[Union[float, Tuple[float, float]]] = None,
    ) -> ApiResponse:
        """Perform a POST request.

        :param resource_path: API path.
        :param query_params: Optional query string parameters.
        :param headers: Optional extra headers.
        :param body: Request body (will be JSON-encoded if a dict/list).
        :param _request_timeout: Per-request timeout override.
        :return: :class:`ApiResponse`.
        """
        return self.request("POST", resource_path, query_params=query_params, headers=headers, body=body, _request_timeout=_request_timeout)

    def put(
        self,
        resource_path: str,
        query_params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        body: Any = None,
        _request_timeout: Optional[Union[float, Tuple[float, float]]] = None,
    ) -> ApiResponse:
        """Perform a PUT request.

        :param resource_path: API path.
        :param query_params: Optional query string parameters.
        :param headers: Optional extra headers.
        :param body: Request body (will be JSON-encoded if a dict/list).
        :param _request_timeout: Per-request timeout override.
        :return: :class:`ApiResponse`.
        """
        return self.request("PUT", resource_path, query_params=query_params, headers=headers, body=body, _request_timeout=_request_timeout)

    def delete(
        self,
        resource_path: str,
        query_params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        body: Any = None,
        _request_timeout: Optional[Union[float, Tuple[float, float]]] = None,
    ) -> ApiResponse:
        """Perform a DELETE request.

        :param resource_path: API path.
        :param query_params: Optional query string parameters.
        :param headers: Optional extra headers.
        :param body: Request body (will be JSON-encoded if a dict/list).
        :param _request_timeout: Per-request timeout override.
        :return: :class:`ApiResponse`.
        """
        return self.request("DELETE", resource_path, query_params=query_params, headers=headers, body=body, _request_timeout=_request_timeout)

    # ------------------------------------------------------------------
    # Core request method
    # ------------------------------------------------------------------

    def request(
        self,
        method: str,
        resource_path: str,
        query_params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        body: Any = None,
        _request_timeout: Optional[Union[float, Tuple[float, float]]] = None,
    ) -> ApiResponse:
        """Perform an arbitrary HTTP request through the SDK infrastructure.

        This method builds the full URL from ``Configuration.host`` +
        *resource_path*, applies authentication headers, merges default
        headers, and delegates to :meth:`ApiClient.call_api` for retry
        logic, timeout handling, and request-ID tracking.

        :param method: HTTP verb (``"GET"``, ``"POST"``, ``"PUT"``, ``"DELETE"``, etc.).
        :param resource_path: API path appended to the configured host.
        :param query_params: Query string parameters as a dict.
        :param headers: Extra request headers (merged with SDK defaults + auth).
        :param body: Request body.  Dicts and lists are automatically
            JSON-serialised; strings are sent as-is.
        :param _request_timeout: Per-request timeout override.
        :return: :class:`ApiResponse` containing status code, decoded data,
            response headers, and raw bytes.
        :raises ApiException: On non-2xx responses (with typed subclasses).
        """
        method = method.upper()

        logger.debug(
            "ManualApi.request %s %s",
            method,
            resource_path,
        )

        # --- Build request through param_serialize for auth + defaults ---
        _param = self.api_client.param_serialize(
            method=method,
            resource_path=resource_path,
            query_params=self._dict_to_query_tuples(query_params),
            header_params=headers or {},
            body=self._prepare_body(body),
            auth_settings=["basic", "oauth"],
        )

        # _param is (method, url, header_params, body, post_params)
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout,
        )
        response_data.read()

        return self._build_response(response_data)

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _prepare_body(body: Any) -> Any:
        """Encode the body for transmission.

        Dicts and lists are JSON-serialised; ``None`` and strings are
        passed through unchanged.
        """
        if body is None:
            return None
        if isinstance(body, (dict, list)):
            return body
        return body

    @staticmethod
    def _dict_to_query_tuples(
        params: Optional[Dict[str, Any]],
    ) -> Optional[List[Tuple[str, str]]]:
        """Convert a flat dict to the list-of-tuples format expected by
        :meth:`ApiClient.param_serialize`.
        """
        if not params:
            return None
        return [(str(k), str(v)) for k, v in params.items()]

    def _build_response(self, response_data: rest.RESTResponse) -> ApiResponse:
        """Wrap a raw :class:`RESTResponse` in an :class:`ApiResponse`.

        For non-2xx responses, an :class:`ApiException` (or typed subclass) is
        raised — the same behaviour as the auto-generated endpoints.
        """
        status = response_data.status
        raw = response_data.data
        response_headers = response_data.getheaders()

        # Attempt to decode JSON; fall back to raw string
        return_data: Any = None
        if raw:
            try:
                return_data = json.loads(raw)
            except (json.JSONDecodeError, UnicodeDecodeError):
                return_data = raw.decode("utf-8", errors="replace") if isinstance(raw, bytes) else raw

        if not 200 <= status <= 299:
            raise ApiException.from_response(
                http_resp=response_data,
                body=raw.decode("utf-8", errors="replace") if isinstance(raw, bytes) else str(raw),
                data=return_data,
            )

        logger.debug(
            "ManualApi response (status=%d, method=%s)",
            status,
            response_data.response.request_method if hasattr(response_data.response, "request_method") else "?",
        )

        return ApiResponse(
            status_code=status,
            data=return_data,
            headers=response_headers,
            raw_data=raw,
        )
