"""BambooHR OAuth token refresh provider.

Handles the OAuth 2.0 refresh-token grant by POSTing to BambooHR's token
endpoint and returning a :class:`TokenResponse`.
"""

from __future__ import annotations

import json
import logging
from typing import Any, Callable, Dict, Optional
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from bamboohr_sdk.client.auth.token_manager import TokenResponse
from bamboohr_sdk.exceptions import ApiException

logger = logging.getLogger("bamboohr_sdk")

# Type alias for an injectable HTTP send function used in testing.
# Signature: (request: Request) -> (status_code, headers_dict, body_str)
HttpSendFunc = Callable[[Request], tuple]


class BambooHRTokenRefreshProvider:
    """Performs OAuth 2.0 token refresh against BambooHR's token endpoint.

    The endpoint URL is derived from the API host::

        {host}/token.php?request=token

    :param client_id: OAuth client ID.
    :param client_secret: OAuth client secret.
    :param api_host: The API host (e.g. ``"https://acme.bamboohr.com"``).
    :param http_send: Optional callable replacing the default HTTP transport
        (useful for testing). Must accept a :class:`urllib.request.Request`
        and return ``(status_code, headers_dict, body_str)``.
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        api_host: str = "https://example.bamboohr.com",
        http_send: Optional[HttpSendFunc] = None,
    ) -> None:
        self._client_id = client_id
        self._client_secret = client_secret
        self._token_endpoint = self._build_token_endpoint(api_host)
        self._http_send = http_send

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def refresh_token(self, refresh_token: str) -> TokenResponse:
        """Exchange a refresh token for a new access token.

        :param refresh_token: The refresh token to use.
        :return: A :class:`TokenResponse` with the new tokens.
        :raises ApiException: If the refresh request fails.
        """
        body = urlencode(
            {
                "grant_type": "refresh_token",
                "refresh_token": refresh_token,
                "client_id": self._client_id,
                "client_secret": self._client_secret,
            }
        ).encode("utf-8")

        req = Request(
            self._token_endpoint,
            data=body,
            method="POST",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
            },
        )

        logger.debug("Sending token refresh request to %s", self._token_endpoint)

        status_code, headers, response_body = self._send(req)

        if status_code < 200 or status_code >= 300:
            logger.error(
                "Token refresh failed (status=%d, endpoint=%s)",
                status_code,
                self._token_endpoint,
            )
            raise ApiException(
                status=status_code,
                reason=f"Token refresh failed with status {status_code}",
                body=response_body,
            )

        try:
            data: Dict[str, Any] = json.loads(response_body)
        except (json.JSONDecodeError, TypeError) as exc:
            raise ApiException(
                status=500,
                reason=f"Invalid JSON response from token endpoint: {exc}",
                body=response_body,
            )

        if "access_token" not in data:
            raise ApiException(
                status=500,
                reason="Token response missing required access_token field",
                body=response_body,
            )

        logger.debug(
            "Token refresh succeeded (has_new_refresh=%s, has_expiry=%s)",
            "refresh_token" in data,
            "expires_in" in data,
        )

        return TokenResponse(
            access_token=data["access_token"],
            refresh_token=data.get("refresh_token"),
            expires_in=(
                int(data["expires_in"]) if "expires_in" in data else None
            ),
        )

    # ------------------------------------------------------------------
    # Introspection
    # ------------------------------------------------------------------

    @property
    def token_endpoint(self) -> str:
        """Return the token endpoint URL."""
        return self._token_endpoint

    @property
    def client_id(self) -> str:
        """Return the OAuth client ID."""
        return self._client_id

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _build_token_endpoint(api_host: str) -> str:
        """Derive the token endpoint from the API host."""
        return api_host.rstrip("/") + "/token.php?request=token"

    def _send(self, req: Request) -> tuple:
        """Send the HTTP request and return ``(status, headers, body)``.

        Uses the injected ``http_send`` callable if provided; otherwise
        falls back to :func:`urllib.request.urlopen`.
        """
        if self._http_send is not None:
            return self._http_send(req)

        try:
            with urlopen(req, timeout=30) as resp:
                return (
                    resp.status,
                    dict(resp.headers),
                    resp.read().decode("utf-8"),
                )
        except HTTPError as exc:
            body = ""
            if exc.fp:
                body = exc.fp.read().decode("utf-8", errors="replace")
            logger.error(
                "Token refresh HTTP error (status=%d, reason=%s)",
                exc.code,
                exc.reason,
            )
            raise ApiException(
                status=exc.code,
                reason=f"Token refresh request failed: {exc.reason}",
                body=body,
            )
        except URLError as exc:
            logger.error("Token refresh connection error: %s", exc.reason)
            raise ApiException(
                status=0,
                reason=f"Token refresh request failed: {exc.reason}",
            )
