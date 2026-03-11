"""
Example 03: Complete OAuth 2.0 Authorization Flow
===================================================

Production-ready implementation of the full OAuth 2.0 authorization code
flow for BambooHR, covering:

    1. Building the authorization URL
    2. Exchanging the authorization code for tokens
    3. Using tokens with the SDK
    4. Refreshing tokens manually
    5. Security best practices

This example shows the HTTP-level OAuth steps that happen *before* you
use the SDK. Once you have tokens, use with_oauth_refresh() as shown
in 02_oauth_with_auto_refresh.py.

Prerequisites:
    - pip install bamboohr-sdk httpx
    - An OAuth application registered in BambooHR
    - A redirect URI configured in your app settings

Usage:
    export BAMBOO_COMPANY="yourcompany"
    export OAUTH_CLIENT_ID="your_client_id"
    export OAUTH_CLIENT_SECRET="your_client_secret"
    export OAUTH_REDIRECT_URI="https://yourapp.com/callback"
    python examples/03_oauth_complete_flow.py
"""

import os
import secrets
from urllib.parse import urlencode

import httpx

from bamboohr_sdk.client import BambooHRClient

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

company = os.environ.get("BAMBOO_COMPANY", "yourcompany")
host = os.environ.get("BAMBOO_HOST")  # Optional: full base URL override
client_id = os.environ.get("OAUTH_CLIENT_ID", "your_client_id")
client_secret = os.environ.get("OAUTH_CLIENT_SECRET", "your_client_secret")
redirect_uri = os.environ.get("OAUTH_REDIRECT_URI", "https://yourapp.com/callback")

BASE_URL = host or f"https://{company}.bamboohr.com"

print("=== Complete OAuth 2.0 Flow ===\n")

# ---------------------------------------------------------------------------
# Step 1: Build the Authorization URL
# ---------------------------------------------------------------------------
# Direct the user's browser to this URL. They'll log in to BambooHR and
# grant your application access.

# Generate a cryptographic state parameter for CSRF protection
state = secrets.token_hex(16)

authorization_params = {
    "client_id": client_id,
    "response_type": "code",
    "redirect_uri": redirect_uri,
    "state": state,
}

authorization_url = f"{BASE_URL}/authorize.php?{urlencode(authorization_params)}"

print("Step 1: Direct the user to this authorization URL:\n")
print(f"  {authorization_url}\n")
print(f"  State token (save for verification): {state}\n")

# In a web application:
#   - Store `state` in the user's session
#   - Redirect the browser to `authorization_url`
#   - BambooHR will redirect back to your `redirect_uri` with `code` and `state`

# ---------------------------------------------------------------------------
# Step 2: Exchange Authorization Code for Tokens
# ---------------------------------------------------------------------------
# After the user authorizes, BambooHR redirects to your redirect_uri with:
#   ?code=AUTHORIZATION_CODE&state=STATE_VALUE
#
# Verify the state matches, then exchange the code for tokens.


def exchange_code_for_tokens(authorization_code: str) -> dict:
    """Exchange an authorization code for access and refresh tokens.

    Args:
        authorization_code: The code received from the OAuth callback.

    Returns:
        Token response dict with access_token, refresh_token, expires_in.
    """
    token_url = f"{BASE_URL}/token.php?request=token"

    response = httpx.post(
        token_url,
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "authorization_code",
            "code": authorization_code,
            "redirect_uri": redirect_uri,
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    response.raise_for_status()
    return response.json()


# Example callback handling (in a web framework like Flask or FastAPI):
#
#   @app.get("/callback")
#   def oauth_callback(code: str, state: str):
#       # Verify state matches what we stored in the session
#       if state != session["oauth_state"]:
#           raise ValueError("Invalid state parameter — possible CSRF attack")
#
#       tokens = exchange_code_for_tokens(code)
#       save_tokens_to_database(tokens)
#       return redirect("/dashboard")

print("Step 2: Exchange the authorization code for tokens")
print("  (In production, this happens in your callback handler)\n")

# ---------------------------------------------------------------------------
# Step 3: Use Tokens with the SDK
# ---------------------------------------------------------------------------
# Once you have tokens, create a client with automatic refresh.

print("Step 3: Create an SDK client with your tokens\n")


def create_client(tokens: dict) -> BambooHRClient:
    """Create a BambooHRClient from an OAuth token response."""
    builder = (
        BambooHRClient()
        .with_oauth_refresh(
            access_token=tokens["access_token"],
            refresh_token=tokens["refresh_token"],
            client_id=client_id,
            client_secret=client_secret,
            expires_in=tokens.get("expires_in"),
        )
        .on_token_refresh(
            lambda new_access, new_refresh, old_access, old_refresh: print(
                f"  [Token refreshed] New token: {new_access[:20]}..."
            )
        )
    )
    return (builder.with_host(host) if host else builder.for_company(company)).build()


# Simulated token response for demonstration
demo_tokens = {
    "access_token": "demo_access_token_placeholder",
    "refresh_token": "demo_refresh_token_placeholder",
    "expires_in": 3600,
}

print("  client = create_client(tokens)")
print("  directory = client.employees().get_employees_directory()\n")

# ---------------------------------------------------------------------------
# Step 4: Manual Token Refresh
# ---------------------------------------------------------------------------
# The SDK handles refresh automatically, but you may need manual refresh
# for startup scenarios (e.g., loading saved tokens that may be expired).


def refresh_tokens_manually(current_refresh_token: str) -> dict:
    """Manually refresh an OAuth token pair.

    Useful when loading tokens from storage on application startup.

    Args:
        current_refresh_token: The refresh token to use.

    Returns:
        New token response dict.
    """
    token_url = f"{BASE_URL}/token.php?request=token"

    response = httpx.post(
        token_url,
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "refresh_token",
            "refresh_token": current_refresh_token,
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    response.raise_for_status()
    return response.json()


print("Step 4: Manual token refresh (for startup/recovery)")
print("  new_tokens = refresh_tokens_manually(saved_refresh_token)\n")

# ---------------------------------------------------------------------------
# Step 5: Security Best Practices
# ---------------------------------------------------------------------------

print("Step 5: Security best practices\n")

best_practices = [
    "Always validate the `state` parameter to prevent CSRF attacks",
    "Store tokens encrypted at rest (use your platform's secret management)",
    "Use HTTPS for all redirect URIs — never use HTTP",
    "Keep client_secret server-side only — never expose to the browser",
    "Monitor token refresh failures and alert on sustained errors",
    "Implement token rotation — update stored refresh tokens on each refresh",
    "Set appropriate token lifetimes for your security requirements",
]

for i, practice in enumerate(best_practices, 1):
    print(f"  {i}. {practice}")

# ---------------------------------------------------------------------------
# Complete Web Application Example
# ---------------------------------------------------------------------------
#
# Here's how the full flow fits together in a FastAPI application:
#
#   from fastapi import FastAPI, Request
#   from fastapi.responses import RedirectResponse
#
#   app = FastAPI()
#   token_store = DatabaseTokenStorage(db)
#
#   @app.get("/login")
#   def login(request: Request):
#       state = secrets.token_hex(16)
#       request.session["oauth_state"] = state
#       url = f"{BASE_URL}/authorize.php?" + urlencode({
#           "client_id": client_id,
#           "response_type": "code",
#           "redirect_uri": redirect_uri,
#           "state": state,
#       })
#       return RedirectResponse(url)
#
#   @app.get("/callback")
#   def callback(code: str, state: str, request: Request):
#       if state != request.session.get("oauth_state"):
#           raise HTTPException(403, "Invalid state")
#       tokens = exchange_code_for_tokens(code)
#       token_store.save(request.session["user_id"], tokens)
#       return RedirectResponse("/dashboard")
#
#   @app.get("/dashboard")
#   def dashboard(request: Request):
#       tokens = token_store.load(request.session["user_id"])
#       client = create_client(tokens)
#       directory = client.employees().get_employees_directory()
#       return {"employee_count": len(directory.employees or [])}
