"""Request ID middleware for extracting and tracking API request IDs.

Extracts the ``x-request-id`` header from API responses and makes it
available for tracing and debugging.  Modelled after the PHP SDK's
``RequestIdMiddleware``.
"""

from __future__ import annotations

import logging
import threading
from typing import Optional

logger = logging.getLogger("bamboohr_sdk")

# Header name is matched case-insensitively by urllib3, but we store the
# canonical lowercase form for look-ups.
REQUEST_ID_HEADER = "x-request-id"


class RequestIdMiddleware:
    """Tracks the ``x-request-id`` header returned by BambooHR API responses.

    Thread-safe: each thread sees its own *last_request_id* via a
    :class:`threading.local`.

    Usage::

        middleware = RequestIdMiddleware()
        # After an API call, extract the request ID from the response:
        middleware.extract_request_id(response)
        # Retrieve it later for logging / error reporting:
        print(middleware.last_request_id)
    """

    def __init__(self) -> None:
        self._local = threading.local()

    @property
    def last_request_id(self) -> Optional[str]:
        """Return the most recent request ID, or ``None`` if not yet set."""
        return getattr(self._local, "last_request_id", None)

    def extract_request_id(self, response) -> Optional[str]:
        """Extract the request ID from a response object.

        Supports any object with a ``getheader(name, default)`` method
        (e.g. :class:`~bamboohr_sdk.rest.RESTResponse`) as well as plain
        ``dict``-like header containers.

        :param response: The HTTP response object.
        :return: The extracted request ID, or ``None``.
        """
        request_id: Optional[str] = None

        # RESTResponse style
        if hasattr(response, "getheader"):
            request_id = response.getheader(REQUEST_ID_HEADER)

        # Fallback: dict-like headers attribute
        if request_id is None and hasattr(response, "headers"):
            headers = response.headers
            if hasattr(headers, "get"):
                request_id = headers.get(REQUEST_ID_HEADER)

        if request_id:
            self._local.last_request_id = request_id
            logger.debug("Extracted request ID: %s", request_id)
        else:
            logger.debug("No %s header in response", REQUEST_ID_HEADER)

        return request_id

    def reset(self) -> None:
        """Clear the stored request ID for the current thread."""
        self._local.last_request_id = None
