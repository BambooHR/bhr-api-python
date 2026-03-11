"""Authentication builder for the BambooHR SDK.

Provides a fluent interface for configuring API key or OAuth authentication,
including OAuth with automatic token refresh.
"""

from __future__ import annotations

from typing import Any, Callable, Dict, Optional

from bamboohr_sdk.client.logger.secure_log_filter import mask_value
from bamboohr_sdk.configuration import Configuration


# Type alias for the token refresh callback:
#   (new_access_token, new_refresh_token, old_access_token, old_refresh_token) -> None
TokenRefreshCallback = Callable[[str, Optional[str], str, Optional[str]], None]


class AuthBuilder:
    """Fluent builder for configuring SDK authentication.

    Supports three authentication modes:

    1. **API key** – simplest form, recommended for server-to-server integrations::

        auth = AuthBuilder().with_api_key("your-api-key")

    2. **OAuth bearer token** – for short-lived access tokens::

        auth = AuthBuilder().with_oauth("access-token")

    3. **OAuth with automatic refresh** – manages token lifecycle::

        auth = (
            AuthBuilder()
            .with_oauth_refresh(
                access_token="...",
                refresh_token="...",
                client_id="...",
                client_secret="...",
                expires_in=3600,
            )
            .on_token_refresh(my_callback)
        )
    """

    def __init__(self) -> None:
        self._auth_type: Optional[str] = None
        self._api_key: Optional[str] = None
        self._oauth_token: Optional[str] = None
        self._refresh_token: Optional[str] = None
        self._client_id: Optional[str] = None
        self._client_secret: Optional[str] = None
        self._expires_in: Optional[int] = None
        self._on_token_refresh: Optional[TokenRefreshCallback] = None

    # ------------------------------------------------------------------
    # Fluent configuration methods
    # ------------------------------------------------------------------

    def with_api_key(self, api_key: str) -> AuthBuilder:
        """Configure authentication using an API key.

        :param api_key: Your BambooHR API key.
        :return: self for chaining.
        """
        if not api_key:
            raise ValueError("API key cannot be empty")
        self._auth_type = "api_key"
        self._api_key = api_key
        return self

    def with_oauth(self, token: str) -> AuthBuilder:
        """Configure authentication using an OAuth bearer token.

        :param token: Your OAuth access token.
        :return: self for chaining.
        """
        if not token:
            raise ValueError("OAuth token cannot be empty")
        self._auth_type = "oauth"
        self._oauth_token = token
        return self

    def with_oauth_refresh(
        self,
        access_token: str,
        refresh_token: str,
        client_id: str,
        client_secret: str,
        expires_in: Optional[int] = None,
    ) -> AuthBuilder:
        """Configure OAuth with automatic token refresh.

        :param access_token: Current OAuth access token.
        :param refresh_token: OAuth refresh token.
        :param client_id: OAuth client ID.
        :param client_secret: OAuth client secret.
        :param expires_in: Seconds until the access token expires (optional).
        :return: self for chaining.
        """
        if not access_token:
            raise ValueError("OAuth access token cannot be empty")
        if not refresh_token:
            raise ValueError("OAuth refresh token cannot be empty")
        if not client_id:
            raise ValueError("OAuth client ID cannot be empty")
        if not client_secret:
            raise ValueError("OAuth client secret cannot be empty")

        self._auth_type = "oauth_refresh"
        self._oauth_token = access_token
        self._refresh_token = refresh_token
        self._client_id = client_id
        self._client_secret = client_secret
        self._expires_in = expires_in
        return self

    def on_token_refresh(self, callback: TokenRefreshCallback) -> AuthBuilder:
        """Register a callback invoked when OAuth tokens are refreshed.

        The callback signature is::

            def callback(
                new_access_token: str,
                new_refresh_token: Optional[str],
                old_access_token: str,
                old_refresh_token: Optional[str],
            ) -> None: ...

        :param callback: Callable to invoke on token refresh.
        :return: self for chaining.
        """
        if not callable(callback):
            raise TypeError("Token refresh callback must be callable")
        self._on_token_refresh = callback
        return self

    # ------------------------------------------------------------------
    # Query helpers
    # ------------------------------------------------------------------

    @property
    def is_configured(self) -> bool:
        """Return True if an authentication method has been set."""
        return self._auth_type is not None

    @property
    def auth_type(self) -> Optional[str]:
        """Return the configured authentication type."""
        return self._auth_type

    @property
    def has_oauth_refresh(self) -> bool:
        """Return True if OAuth with refresh is configured."""
        return self._auth_type == "oauth_refresh"

    @property
    def refresh_token(self) -> Optional[str]:
        return self._refresh_token

    @property
    def client_id(self) -> Optional[str]:
        return self._client_id

    @property
    def client_secret(self) -> Optional[str]:
        return self._client_secret

    @property
    def expires_in(self) -> Optional[int]:
        return self._expires_in

    @property
    def token_refresh_callback(self) -> Optional[TokenRefreshCallback]:
        return self._on_token_refresh

    # ------------------------------------------------------------------
    # Apply to Configuration
    # ------------------------------------------------------------------

    def apply_to(self, config: Configuration) -> None:
        """Apply the authentication settings to a :class:`Configuration`.

        :param config: The configuration object to update.
        :raises ValueError: If no authentication method has been configured.
        """
        self.validate()

        if self._auth_type == "api_key":
            # BambooHR uses HTTP Basic with the API key as username and 'x' as password
            config.username = self._api_key
            config.password = "x"
        elif self._auth_type in ("oauth", "oauth_refresh"):
            config.access_token = self._oauth_token
        else:
            raise ValueError(f"Unknown authentication type: {self._auth_type}")

    def validate(self) -> None:
        """Validate the current authentication configuration.

        :raises ValueError: If the configuration is invalid or incomplete.
        """
        if self._auth_type is None:
            raise ValueError(
                "No authentication method configured. "
                "Use with_api_key() or with_oauth()"
            )

        if self._auth_type == "api_key":
            if not self._api_key:
                raise ValueError("API key cannot be empty")

        elif self._auth_type == "oauth":
            if not self._oauth_token:
                raise ValueError("OAuth token cannot be empty")

        elif self._auth_type == "oauth_refresh":
            if not self._oauth_token:
                raise ValueError("OAuth access token cannot be empty")
            if not self._refresh_token:
                raise ValueError("OAuth refresh token cannot be empty")
            if not self._client_id:
                raise ValueError("OAuth client ID cannot be empty")
            if not self._client_secret:
                raise ValueError("OAuth client secret cannot be empty")

    # ------------------------------------------------------------------
    # Logging / debugging
    # ------------------------------------------------------------------

    def get_sanitized_info(self) -> Dict[str, Any]:
        """Return a dict of auth info safe for logging (secrets masked).

        :return: Dictionary with sanitized authentication details.
        """
        if self._auth_type is None:
            return {"type": "none", "configured": False}

        info: Dict[str, Any] = {
            "type": self._auth_type,
            "configured": True,
        }

        if self._auth_type == "api_key":
            info["api_key"] = mask_value(self._api_key)
        elif self._auth_type == "oauth":
            info["oauth_token"] = mask_value(self._oauth_token)
        elif self._auth_type == "oauth_refresh":
            info["oauth_token"] = mask_value(self._oauth_token)
            info["refresh_token"] = mask_value(self._refresh_token)
            info["client_id"] = self._client_id
            info["has_callback"] = self._on_token_refresh is not None

        return info

    def reset(self) -> AuthBuilder:
        """Clear all authentication settings.

        :return: self for chaining.
        """
        self._auth_type = None
        self._api_key = None
        self._oauth_token = None
        self._refresh_token = None
        self._client_id = None
        self._client_secret = None
        self._expires_in = None
        self._on_token_refresh = None
        return self


