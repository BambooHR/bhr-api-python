# Authentication Guide

The BambooHR Python SDK supports two authentication methods: **OAuth 2.0** (recommended) and **API key**. Both are configured through the `BambooHRClient` builder.

**OAuth 2.0 is the recommended authentication method for all partner integrations.** It provides user-level authorization, supports token expiration and rotation, and aligns with modern API security standards. API key authentication is available for quick prototyping or internal tooling where OAuth is not practical.

## Table of Contents

- [OAuth 2.0 Authentication](#oauth-20-authentication)
- [OAuth with Automatic Token Refresh](#oauth-with-automatic-token-refresh)
- [Token Storage Callback](#token-storage-callback)
- [API Key Authentication](#api-key-authentication)
- [Security Best Practices](#security-best-practices)

---

## OAuth 2.0 Authentication

OAuth 2.0 is the recommended authentication method for all partner integrations. It provides user-level authorization and supports automatic token refresh for long-lived integrations.

### Registering an OAuth Application

Register your application in BambooHR to obtain a `client_id` and `client_secret`. Configure a `redirect_uri` that BambooHR will send the authorization code to.

### Authorization Code Flow

**Step 1 — Build the authorization URL and redirect the user:**

```python
import secrets
from urllib.parse import urlencode

company = "your-company-subdomain"
client_id = os.environ["OAUTH_CLIENT_ID"]
redirect_uri = "https://yourapp.com/callback"

state = secrets.token_hex(16)  # Save this in the user's session for CSRF protection

authorization_url = (
    f"https://{company}.bamboohr.com/authorize.php?"
    + urlencode({
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "state": state,
    })
)
# Redirect the user's browser to authorization_url
```

**Step 2 — Exchange the authorization code for tokens:**

After the user authorizes your application, BambooHR redirects to your `redirect_uri` with `?code=...&state=...`. Verify the `state` matches what you stored, then exchange the code:

```python
import httpx

def exchange_code_for_tokens(authorization_code: str) -> dict:
    response = httpx.post(
        f"https://{company}.bamboohr.com/token.php?request=token",
        data={
            "client_id": os.environ["OAUTH_CLIENT_ID"],
            "client_secret": os.environ["OAUTH_CLIENT_SECRET"],
            "grant_type": "authorization_code",
            "code": authorization_code,
            "redirect_uri": redirect_uri,
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    response.raise_for_status()
    return response.json()
    # Returns: {"access_token": "...", "refresh_token": "...", "expires_in": 3600}
```

**Step 3 — Create the SDK client with the access token:**

```python
tokens = exchange_code_for_tokens(code_from_callback)

client = (
    BambooHRClient()
    .with_oauth(tokens["access_token"])
    .for_company("your-company-subdomain")
    .build()
)
```

For long-lived integrations, use `with_oauth_refresh()` (below) so the SDK handles token expiration automatically.

---

## OAuth with Automatic Token Refresh

When configured with a refresh token, the SDK proactively refreshes the access token 5 minutes before it expires. Your API calls continue transparently — no manual intervention required.

### Setup

```python
import os
from bamboohr_sdk.client import BambooHRClient

client = (
    BambooHRClient()
    .with_oauth_refresh(
        access_token=os.environ["OAUTH_ACCESS_TOKEN"],
        refresh_token=os.environ["OAUTH_REFRESH_TOKEN"],
        client_id=os.environ["OAUTH_CLIENT_ID"],
        client_secret=os.environ["OAUTH_CLIENT_SECRET"],
        expires_in=3600,  # Seconds until access token expires (from token response)
    )
    .for_company("your-company-subdomain")
    .build()
)
```

`expires_in` is optional but strongly recommended. Without it, the SDK cannot determine when to proactively refresh and will only refresh reactively on authentication failures.

### How It Works

The SDK maintains a `TokenManager` that tracks token expiration. Before each request, it checks whether the token needs refreshing (i.e., it expires within the next 5 minutes). If so, it calls BambooHR's token endpoint using the refresh token and updates the access token transparently.

Refresh requests are sent to:
```
POST https://{company}.bamboohr.com/token.php?request=token
```

---

## Token Storage Callback

**The SDK does not persist tokens.** When a token refresh occurs, your application is responsible for saving the new tokens so they survive restarts. Use the `on_token_refresh` callback for this.

### Callback Signature

```python
def on_token_refresh(
    new_access_token: str,
    new_refresh_token: str | None,
    old_access_token: str,
    old_refresh_token: str | None,
) -> None:
    ...
```

- `new_access_token` — the new access token to store
- `new_refresh_token` — the new refresh token (may be `None` if not rotated)
- `old_access_token` / `old_refresh_token` — the previous tokens (useful for audit logs)

### Example

```python
def save_tokens(new_access, new_refresh, old_access, old_refresh):
    # Replace with your actual storage backend (database, secrets manager, etc.)
    db.execute(
        "UPDATE oauth_tokens SET access_token = %s, refresh_token = %s WHERE user_id = %s",
        (new_access, new_refresh or old_refresh, current_user_id),
    )

client = (
    BambooHRClient()
    .with_oauth_refresh(
        access_token=stored_tokens["access_token"],
        refresh_token=stored_tokens["refresh_token"],
        client_id=os.environ["OAUTH_CLIENT_ID"],
        client_secret=os.environ["OAUTH_CLIENT_SECRET"],
        expires_in=stored_tokens.get("expires_in"),
    )
    .on_token_refresh(save_tokens)
    .for_company("your-company-subdomain")
    .build()
)
```

### Startup Pattern

If your application loads stored tokens on startup, the tokens may already be expired. Refresh them manually before creating the client:

```python
def refresh_tokens_manually(refresh_token: str) -> dict:
    response = httpx.post(
        f"https://{company}.bamboohr.com/token.php?request=token",
        data={
            "client_id": os.environ["OAUTH_CLIENT_ID"],
            "client_secret": os.environ["OAUTH_CLIENT_SECRET"],
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    response.raise_for_status()
    return response.json()
```

---

## API Key Authentication

API key authentication is available for internal tooling, quick prototyping, or automated scripts where setting up OAuth is not practical. It is not recommended for partner integrations.

### Generating an API Key

1. Log in to BambooHR as an administrator.
2. Navigate to **Account > API Keys**.
3. Click **Add New Key**, give it a name, and copy the generated key.

Reference: [BambooHR authentication documentation](https://documentation.bamboohr.com/docs/getting-started#authentication)

### Usage

```python
import os
from bamboohr_sdk.client import BambooHRClient

client = (
    BambooHRClient()
    .with_api_key(os.environ["BAMBOO_API_KEY"])
    .for_company("your-company-subdomain")
    .build()
)
```

Internally the SDK sends the API key as an HTTP Basic Auth username with `x` as the password, which is the format required by BambooHR.

---

## Security Best Practices

**Credentials**
- Always load API keys and OAuth secrets from environment variables or a secrets manager. Never hardcode them in source code.
- Keep `client_secret` server-side only — never expose it to the browser or include it in mobile app bundles.
- Rotate API keys periodically and revoke any that may have been compromised.

**OAuth flow**
- Always validate the `state` parameter in your OAuth callback to prevent CSRF attacks.
- Use HTTPS for all `redirect_uri` values — BambooHR will not send authorization codes to plain HTTP endpoints.
- Implement token rotation: update your stored refresh token whenever a refresh occurs (use the `on_token_refresh` callback).

**Token storage**
- Encrypt tokens at rest using your platform's secret management (e.g., AWS Secrets Manager, HashiCorp Vault, environment-level encryption).
- Never log full token values. The SDK's built-in `SecureLogFilter` automatically redacts Authorization headers and other sensitive values from log output.
- Scope token storage to the individual user — do not share tokens across users.

**Monitoring**
- Monitor token refresh failure rates. Sustained failures may indicate revoked credentials or a service disruption.
- If a refresh fails, prompt the affected user to re-authorize rather than retrying indefinitely.

---

## Reference

- [BambooHR getting started & authentication](https://documentation.bamboohr.com/docs/getting-started)
- [BambooHR webhooks](https://documentation.bamboohr.com/docs/webhooks)
- `bamboohr_sdk/client/auth_builder.py` — `AuthBuilder` implementation
- `bamboohr_sdk/client/auth/token_manager.py` — token expiration and refresh logic
- `examples/01_first_api_call.py` — API key example
- `examples/02_oauth_with_auto_refresh.py` — OAuth with automatic refresh
- `examples/03_oauth_complete_flow.py` — full OAuth authorization code flow
