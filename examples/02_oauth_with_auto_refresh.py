"""
Example 02: OAuth with Automatic Token Refresh
================================================

Demonstrates OAuth 2.0 authentication with automatic token refresh,
including persistent token storage patterns for production use.

The SDK handles token expiration automatically — it refreshes tokens
proactively 5 minutes before they expire, so your API calls never
fail due to an expired token.

Prerequisites:
    - pip install bamboohr-python
    - An OAuth application registered in BambooHR
    - Valid access and refresh tokens (see 03_oauth_complete_flow.py)

Usage:
    export BAMBOO_COMPANY="yourcompany"
    export OAUTH_ACCESS_TOKEN="your_access_token"
    export OAUTH_REFRESH_TOKEN="your_refresh_token"
    export OAUTH_CLIENT_ID="your_client_id"
    export OAUTH_CLIENT_SECRET="your_client_secret"
    python examples/02_oauth_with_auto_refresh.py
"""

import json
import os
from pathlib import Path

from bamboohr_sdk.client import BambooHRClient
from bamboohr_sdk.exceptions import ApiException, AuthenticationFailedException

# ---------------------------------------------------------------------------
# Token Storage
# ---------------------------------------------------------------------------
# In production, store tokens in a database. This file-based example
# demonstrates the pattern — replace with your own storage backend.


class FileTokenStorage:
    """Simple file-based token storage for demonstration.

    In production, replace this with database-backed storage:

        class DatabaseTokenStorage:
            def __init__(self, db, user_id):
                self.db = db
                self.user_id = user_id

            def save_tokens(self, access_token, refresh_token):
                self.db.execute(
                    "UPDATE oauth_tokens SET access_token = %s, "
                    "refresh_token = %s, updated_at = NOW() WHERE user_id = %s",
                    (access_token, refresh_token, self.user_id),
                )

            def get_tokens(self):
                row = self.db.fetch_one(
                    "SELECT access_token, refresh_token FROM oauth_tokens "
                    "WHERE user_id = %s",
                    (self.user_id,),
                )
                return row if row else None
    """

    def __init__(self, filepath: str = ".bamboohr_tokens.json"):
        self.filepath = Path(filepath)

    def save_tokens(self, access_token: str, refresh_token: str | None) -> None:
        """Persist tokens to disk."""
        data = {"access_token": access_token, "refresh_token": refresh_token}
        self.filepath.write_text(json.dumps(data), encoding="utf-8")
        print(f"  [TokenStorage] Tokens saved to {self.filepath}")

    def get_tokens(self) -> dict | None:
        """Load tokens from disk."""
        if not self.filepath.exists():
            return None
        return json.loads(self.filepath.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------

company = os.environ.get("BAMBOO_COMPANY", "yourcompany")
host = os.environ.get("BAMBOO_HOST")  # Optional: full base URL override
access_token = os.environ.get("OAUTH_ACCESS_TOKEN", "")
refresh_token = os.environ.get("OAUTH_REFRESH_TOKEN", "")
client_id = os.environ.get("OAUTH_CLIENT_ID", "")
client_secret = os.environ.get("OAUTH_CLIENT_SECRET", "")

storage = FileTokenStorage()

# Check for previously saved tokens
saved = storage.get_tokens()
if saved:
    print("Using previously saved tokens.")
    access_token = saved["access_token"]
    refresh_token = saved["refresh_token"]

# ---------------------------------------------------------------------------
# Token Refresh Callback
# ---------------------------------------------------------------------------
# This callback is invoked automatically whenever the SDK refreshes your
# tokens. Use it to persist the new tokens so they survive restarts.


def on_token_refresh(
    new_access: str,
    new_refresh: str | None,
    old_access: str,
    old_refresh: str | None,
) -> None:
    """Called automatically when the SDK refreshes OAuth tokens."""
    print("\n  [Callback] Tokens refreshed automatically!")
    print(f"  [Callback] New access token: {new_access[:20]}...")
    storage.save_tokens(new_access, new_refresh)

    # Other common callback actions:
    # - Update session storage
    # - Log the refresh event for monitoring
    # - Notify other services that use the same tokens


# ---------------------------------------------------------------------------
# Build the Client
# ---------------------------------------------------------------------------

print("=== OAuth with Automatic Token Refresh ===\n")

builder = (
    BambooHRClient()
    .with_oauth_refresh(
        access_token=access_token,
        refresh_token=refresh_token,
        client_id=client_id,
        client_secret=client_secret,
        expires_in=3600,  # Token lifetime in seconds (from your OAuth provider)
    )
    .on_token_refresh(on_token_refresh)
    .with_retries(2)
)
client = (builder.with_host(host) if host else builder.for_company(company)).build()

# ---------------------------------------------------------------------------
# Use the Client
# ---------------------------------------------------------------------------
# Make API calls as normal. The SDK handles token refresh transparently.

try:
    directory = client.employees().get_employees_directory()
    employees = directory.employees or []
    print(f"Successfully retrieved {len(employees)} employees via OAuth.\n")

    # The SDK automatically refreshes the token when it's about to expire.
    # You can also inspect token state programmatically:
    token_mgr = client.token_manager
    if token_mgr:
        remaining = token_mgr.seconds_until_expiry()
        if remaining is not None:
            print(f"Token expires in {remaining:.0f} seconds")
        print(f"Needs refresh: {token_mgr.needs_refresh()}")

except AuthenticationFailedException:
    print("Authentication failed. Your tokens may be invalid or expired.")
    print("Run 03_oauth_complete_flow.py to obtain fresh tokens.")

except ApiException as api_error:
    print(f"API error ({api_error.status}): {api_error.reason}")

# ---------------------------------------------------------------------------
# Production Considerations
# ---------------------------------------------------------------------------
#
# 1. Token Storage Security
#    - Encrypt tokens at rest (use your platform's secret management)
#    - Never log full token values
#    - Rotate encryption keys periodically
#
# 2. Concurrency
#    - If multiple processes share tokens, coordinate refresh to avoid races
#    - Consider a token service that centralizes refresh logic
#
# 3. Error Recovery
#    - If refresh fails, prompt the user to re-authorize
#    - Monitor refresh failure rates for early warning
#
# 4. Token Lifetime
#    - The SDK refreshes proactively 5 minutes before expiry
#    - Pass `expires_in` from your OAuth token response for accurate timing
#    - If `expires_in` is not set, the SDK won't auto-refresh based on time
