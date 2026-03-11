"""OAuth token manager for the BambooHR SDK.

Manages token state, expiration tracking, and refresh callback notifications.
"""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Callable, Optional


# Type alias for the token refresh callback
TokenRefreshCallback = Callable[[str, Optional[str], str, Optional[str]], None]

# Proactive refresh buffer: refresh 5 minutes before expiry
EXPIRY_BUFFER_SECONDS = 300


@dataclass(frozen=True)
class TokenResponse:
    """Immutable response from a token refresh request.

    :param access_token: The new access token.
    :param refresh_token: New refresh token (may be rotated), or ``None``.
    :param expires_in: Seconds until the access token expires, or ``None``.
    """

    access_token: str
    refresh_token: Optional[str] = None
    expires_in: Optional[int] = None

    @property
    def has_refresh_token(self) -> bool:
        """Return True if a new refresh token was included."""
        return self.refresh_token is not None

    def get_expires_at(self) -> Optional[float]:
        """Return the absolute expiration timestamp, or ``None``."""
        if self.expires_in is None:
            return None
        return time.time() + self.expires_in


class TokenManager:
    """Manages OAuth token state and refresh logic.

    Responsibilities:

    - Store current access and refresh tokens
    - Track token expiration
    - Determine when tokens need to be refreshed
    - Notify callbacks when tokens are updated

    :param access_token: The current access token.
    :param refresh_token: The refresh token (required for auto-refresh).
    :param expires_in: Seconds until the access token expires (optional).
    :param on_token_refresh: Callback invoked when tokens are updated.
    """

    def __init__(
        self,
        access_token: str,
        refresh_token: Optional[str] = None,
        expires_in: Optional[int] = None,
        on_token_refresh: Optional[TokenRefreshCallback] = None,
    ) -> None:
        self._access_token = access_token
        self._refresh_token = refresh_token
        self._expires_at: Optional[float] = (
            (time.time() + expires_in) if expires_in is not None else None
        )
        self._on_token_refresh = on_token_refresh

    # ------------------------------------------------------------------
    # Token accessors
    # ------------------------------------------------------------------

    @property
    def access_token(self) -> str:
        """Return the current access token."""
        return self._access_token

    @property
    def refresh_token(self) -> Optional[str]:
        """Return the current refresh token."""
        return self._refresh_token

    @property
    def expires_at(self) -> Optional[float]:
        """Return the token expiration timestamp, or ``None``."""
        return self._expires_at

    @property
    def has_refresh_capability(self) -> bool:
        """Return True if a refresh token is available."""
        return self._refresh_token is not None

    # ------------------------------------------------------------------
    # Expiration checks
    # ------------------------------------------------------------------

    def needs_refresh(self) -> bool:
        """Return True if the token should be proactively refreshed.

        Returns True when:

        - A refresh token is available, **and**
        - The token will expire within the buffer period (5 min).
        """
        if not self.has_refresh_capability:
            return False
        if self._expires_at is None:
            return False
        return time.time() >= (self._expires_at - EXPIRY_BUFFER_SECONDS)

    def is_expired(self) -> bool:
        """Return True if the access token is past its expiration time."""
        if self._expires_at is None:
            return False
        return time.time() >= self._expires_at

    def seconds_until_expiry(self) -> Optional[float]:
        """Return seconds until expiry, or ``None`` if unknown."""
        if self._expires_at is None:
            return None
        return max(0.0, self._expires_at - time.time())

    # ------------------------------------------------------------------
    # Token updates
    # ------------------------------------------------------------------

    def update_tokens(self, token_response: TokenResponse) -> None:
        """Update stored tokens from a refresh response.

        Invokes the registered callback (if any) with old and new tokens.

        :param token_response: The :class:`TokenResponse` from the provider.
        """
        old_access = self._access_token
        old_refresh = self._refresh_token

        self._access_token = token_response.access_token

        if token_response.has_refresh_token:
            self._refresh_token = token_response.refresh_token

        self._expires_at = token_response.get_expires_at()

        if self._on_token_refresh is not None:
            self._on_token_refresh(
                self._access_token,
                self._refresh_token,
                old_access,
                old_refresh,
            )

    def set_refresh_callback(self, callback: TokenRefreshCallback) -> None:
        """Set (or replace) the token-refresh callback.

        :param callback: Callable receiving
            ``(new_access, new_refresh, old_access, old_refresh)``.
        """
        self._on_token_refresh = callback
