# BambooHR Python SDK Examples

Practical examples to help you get started with the BambooHR Python SDK.

## Quick Start

All examples are runnable Python scripts. To use them:

```bash
# Set your environment variables
export BAMBOO_COMPANY="mycompany"
export BAMBOO_API_KEY="your_api_key_here"

# Optional: override the base URL (for staging, self-hosted, etc.)
# export BAMBOO_HOST="https://mycompany.custom-domain.com"

# For OAuth examples
export OAUTH_CLIENT_ID="your_client_id"
export OAUTH_CLIENT_SECRET="your_client_secret"

# Run an example
python examples/01_first_api_call.py
```

## Examples Overview

### 01. First API Call
**File:** `01_first_api_call.py`
**Difficulty:** Beginner

Your first BambooHR API call — connect with an API key, fetch the employee directory, and handle common errors.

**What you'll learn:**
- Creating a client with the builder pattern
- Fetching the employee directory
- Handling specific exception types
- Reading individual employee data

---

### 02. OAuth with Automatic Token Refresh
**File:** `02_oauth_with_auto_refresh.py`
**Difficulty:** Intermediate

Set up OAuth 2.0 authentication with automatic token refresh. The SDK refreshes tokens proactively 5 minutes before they expire.

**What you'll learn:**
- Configuring OAuth with `with_oauth_refresh()`
- Token refresh callbacks for persistent storage
- File-based and database-backed token storage patterns
- Inspecting token state programmatically

**Key feature:**
```python
client = (
    BambooHRClient()
    .with_oauth_refresh(
        access_token=tokens["access_token"],
        refresh_token=tokens["refresh_token"],
        client_id=os.environ["OAUTH_CLIENT_ID"],
        client_secret=os.environ["OAUTH_CLIENT_SECRET"],
        expires_in=tokens["expires_in"],
    )
    .on_token_refresh(lambda new_access, new_refresh, old_access, old_refresh:
        save_tokens(new_access, new_refresh)
    )
    .for_company("yourcompany")
    .build()
)
```

---

### 03. OAuth Complete Flow
**File:** `03_oauth_complete_flow.py`
**Difficulty:** Intermediate

The full OAuth 2.0 authorization code flow — from building the authorization URL through code exchange to using tokens with the SDK.

**What you'll learn:**
- Building the authorization URL with CSRF protection
- Exchanging authorization codes for tokens
- Manual token refresh for startup scenarios
- Security best practices
- Complete web application example (FastAPI)

---

### 04. Error Handling
**File:** `04_error_handling.py`
**Difficulty:** Intermediate

Comprehensive guide to handling API errors, including retry strategies, the built-in error catalog, and production patterns.

**What you'll learn:**
- Specific exception types for each HTTP error
- Automatic retry with exponential backoff
- Using the error catalog for diagnostics
- Centralized error handling pattern
- Graceful degradation for non-critical operations
- Debug logging with sensitive data redaction

**Exception hierarchy:**
```
ApiException (base)
├── BadRequestException        (400)
├── UnauthorizedException      (401)
├── ForbiddenException         (403)
├── NotFoundException          (404)
├── ConflictException          (409)
├── UnprocessableEntityException (422)
└── ServiceException           (5xx)
```

---

### 05. Common API Patterns
**File:** `05_common_api_patterns.py`
**Difficulty:** Beginner to Intermediate

Practical examples of the most common BambooHR API operations.

**Covers:**
- Employee directory and listing with pagination
- Employee CRUD (create, read, update)
- Time off types, requests, and balances
- Custom and saved reports
- Employee file management
- Webhook creation and management
- Tabular data (job history, etc.)

---

### 06. Complete Application
**File:** `06_complete_application.py`
**Difficulty:** Advanced

A real-world employee onboarding dashboard service demonstrating production architecture patterns.

**What you'll learn:**
- Service class pattern with dependency injection
- Factory methods for API key and OAuth authentication
- Domain model decoupling from SDK models
- Graceful degradation for non-critical data
- Structured error handling (propagate vs. catch)

---

### 07. Testing Patterns
**File:** `07_testing_patterns.py`
**Difficulty:** Intermediate to Advanced

How to write testable code with the SDK, including mocking, error path testing, and integration test infrastructure.

**What you'll learn:**
- Mocking BambooHRClient with `unittest.mock`
- Testing success and error paths
- Verifying OAuth token refresh callbacks
- Integration test base class (auto-skips without credentials)
- Test data factories for clean, DRY tests

**Run the tests:**
```bash
python -m pytest examples/07_testing_patterns.py -v
```

---

## Running the Examples

### Prerequisites

1. **Python 3.10+**
   ```bash
   python --version
   ```

2. **Install the SDK**
   ```bash
   pip install bamboohr-sdk
   ```

3. **Set environment variables**

   Create a `.env` file or export directly:
   ```bash
   export BAMBOO_COMPANY="mycompany"
   export BAMBOO_API_KEY="your_api_key_here"

   # Optional: override the base URL
   # export BAMBOO_HOST="https://mycompany.custom-domain.com"

   # For OAuth examples
   export OAUTH_CLIENT_ID="your_client_id"
   export OAUTH_CLIENT_SECRET="your_client_secret"
   export OAUTH_ACCESS_TOKEN="your_access_token"
   export OAUTH_REFRESH_TOKEN="your_refresh_token"
   ```

### Running

```bash
# Run a specific example
python examples/01_first_api_call.py

# Run all examples
for file in examples/0*.py; do
    echo "=== Running $file ==="
    python "$file"
    echo ""
done

# Run the test example
python -m pytest examples/07_testing_patterns.py -v
```

## Recommended Learning Path

### Getting Started
1. Read the main [README.md](../README.md)
2. Run **Example 01** — First API Call
3. Run **Example 05** — Common API Patterns
4. Identify which patterns match your use case

### Adding OAuth
1. Run **Example 03** — OAuth Complete Flow (understand the authorization flow)
2. Run **Example 02** — OAuth with Auto Refresh (implement in your app)
3. Set up persistent token storage (database)

### Production Readiness
1. Review **Example 04** — Error Handling
2. Review **Example 06** — Complete Application (architecture patterns)
3. Review **Example 07** — Testing Patterns
4. Add comprehensive error handling and logging

## Troubleshooting

### "Authentication failed" errors
Verify your API key or OAuth tokens:
```bash
# Test API key with curl
curl -u "YOUR_API_KEY:x" https://mycompany.bamboohr.com/api/gateway.php/mycompany/v1/employees/directory

# Check environment variables
echo $BAMBOO_API_KEY
```

### "Company domain is required" errors
Ensure `BAMBOO_COMPANY` is set to your BambooHR subdomain (the part before `.bamboohr.com`).

### OAuth token refresh not working
1. Verify `client_id` and `client_secret` are correct
2. Ensure the refresh token hasn't expired
3. Check that `expires_in` is being passed from your token response
4. Review Example 02 for proper implementation

### Import errors
Ensure the SDK is installed:
```bash
pip install bamboohr-sdk
```

## Additional Resources

- **SDK Documentation:** [README.md](../README.md)
- **API Documentation:** https://documentation.bamboohr.com
- **API Reference:** See the `docs/` directory for auto-generated API docs
