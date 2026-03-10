"""OAuth 2.0 middleware for automatic token refresh.

Wraps API request callables with proactive and reactive token refresh:

1. **Proactive** — refreshes the token *before* a request if it is about to
   expire (within the 5-minute buffer).
2. **Reactive** — on a 401 response, refreshes the token and retries the
   request exactly once.

The middleware guards against recursive refresh attempts.
"""

from __future__ import annotations

import logging
from typing import Any, Callable, Optional

from bamboohr_sdk.client.auth.token_manager import TokenManager
from bamboohr_sdk.client.auth.token_refresh_provider import BambooHRTokenRefreshProvider
from bamboohr_sdk.configuration import Configuration
from bamboohr_sdk.exceptions import ApiException

logger = logging.getLogger("bamboohr_sdk")


class OAuth2Middleware:
    """Handles automatic OAuth token refresh around API requests.

    :param token_manager: :class:`TokenManager` holding the current tokens.
    :param refresh_provider: Provider that performs the token refresh HTTP call.
    :param config: SDK :class:`Configuration` whose ``access_token`` is kept in
        sync with newly refreshed tokens.
    """

    def __init__(
        self,
        token_manager: TokenManager,
        refresh_provider: BambooHRTokenRefreshProvider,
        config: Configuration,
    ) -> None:
        self._token_manager = token_manager
        self._refresh_provider = refresh_provider
        self._config = config
        self._is_refreshing = False

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def handle(self, send_request: Callable[[], Any]) -> Any:
        """Execute *send_request* with automatic token refresh.

        :param send_request: A zero-argument callable that performs the HTTP
            request and returns a response object (typically
            :class:`rest.RESTResponse`).  On a 401, it should raise
            :class:`ApiException` with ``status == 401``.
        :return: The response from *send_request*.
        :raises ApiException: If the request fails and cannot be recovered.
        """
        if not self._token_manager.has_refresh_capability:
            return send_request()

        # --- Proactive refresh ---
        if self._token_manager.needs_refresh() and not self._is_refreshing:
            try:
                self._refresh_access_token()
                logger.debug("Proactive token refresh succeeded")
            except Exception:
                # If proactive refresh fails, proceed anyway — the reactive
                # path may still recover on a 401.
                logger.debug("Proactive token refresh failed; proceeding with current token")

        # --- Send the request ---
        try:
            return send_request()
        except ApiException as exc:
            if exc.status != 401:
                raise

            # --- Reactive refresh on 401 ---
            if self._is_refreshing:
                # Already tried refreshing; don't loop.
                raise

            logger.debug("Received 401; attempting reactive token refresh")
            try:
                self._refresh_access_token()
            except Exception:
                # Refresh failed — raise the original 401.
                raise exc

            # Retry the request with the fresh token.
            return send_request()

    @property
    def is_refreshing(self) -> bool:
        """Return True if a refresh is currently in progress."""
        return self._is_refreshing

    @property
    def token_manager(self) -> TokenManager:
        """Return the underlying :class:`TokenManager`."""
        return self._token_manager

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _refresh_access_token(self) -> None:
        """Perform the token refresh and update internal state."""
        self._is_refreshing = True
        try:
            refresh_token = self._token_manager.refresh_token
            if refresh_token is None:
                raise ApiException(
                    status=401,
                    reason="No refresh token available",
                )

            token_response = self._refresh_provider.refresh_token(refresh_token)
            self._token_manager.update_tokens(token_response)

            # Keep Configuration in sync
            self._config.access_token = self._token_manager.access_token
            logger.info("OAuth token refreshed successfully")
        finally:
            self._is_refreshing = False
