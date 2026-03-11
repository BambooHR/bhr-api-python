"""
Example 01: Your First API Call
================================

This beginner-friendly example walks you through making your first BambooHR
API call using the Python SDK with API key authentication.

Prerequisites:
    - Python 3.10+
    - pip install bamboohr-sdk
    - A BambooHR account with an API key
      (See: https://documentation.bamboohr.com/docs/getting-started#authentication)

Usage:
    export BAMBOO_COMPANY="yourcompany"
    export BAMBOO_API_KEY="your_api_key_here"
    python examples/01_first_api_call.py
"""

import os

from bamboohr_sdk.client import BambooHRClient
from bamboohr_sdk.exceptions import (
    ApiException,
    BadRequestException,
    ForbiddenException,
    NotFoundException,
    UnauthorizedException,
)

# ---------------------------------------------------------------------------
# Step 1: Configure your credentials
# ---------------------------------------------------------------------------
# Best practice: use environment variables, never hardcode credentials.

company = os.environ.get("BAMBOO_COMPANY", "yourcompany")
api_key = os.environ.get("BAMBOO_API_KEY", "your_api_key_here")
host = os.environ.get("BAMBOO_HOST")  # Optional: full base URL override

# ---------------------------------------------------------------------------
# Step 2: Create the client
# ---------------------------------------------------------------------------
# The SDK uses a fluent builder pattern. Chain configuration calls and
# finish with .build() to validate and prepare the client.

builder = BambooHRClient().with_api_key(api_key)
client = (builder.with_host(host) if host else builder.for_company(company)).build()

# ---------------------------------------------------------------------------
# Step 3: Make your first API call
# ---------------------------------------------------------------------------
# Let's fetch the employee directory — a great starting point because it
# returns useful data without needing to know any employee IDs.

print("=== Your First BambooHR API Call ===\n")

try:
    directory = client.employees().get_employees_directory()

    # The directory response has typed top-level fields. The employees
    # list contains dictionaries with camelCase keys from the API.
    employees = directory.employees or []

    print(f"Found {len(employees)} employees in the directory:\n")
    for emp in employees[:10]:  # Show first 10
        name = emp.get("displayName") or f"{emp.get('firstName', '')} {emp.get('lastName', '')}"
        department = emp.get("department") or "N/A"
        print(f"  - {name} ({department})")

    if len(employees) > 10:
        print(f"  ... and {len(employees) - 10} more")

# ---------------------------------------------------------------------------
# Step 4: Handle errors
# ---------------------------------------------------------------------------
# The SDK raises specific exceptions for each HTTP error type, making it
# easy to handle different failure modes appropriately.

except UnauthorizedException:
    print("Authentication failed!")
    print("  - Verify your API key is correct")
    print("  - Ensure your company subdomain is correct")
    print(f"  - Current subdomain: '{company}'")

except ForbiddenException:
    print("Permission denied!")
    print("  - Your API key may lack the required permissions")
    print("  - Contact your BambooHR administrator")

except NotFoundException:
    print("Resource not found!")
    print(f"  - Verify the company subdomain '{company}' is correct")

except BadRequestException as bad_request_error:
    print(f"Bad request: {bad_request_error.reason}")

except ApiException as api_error:
    # Catch-all for any other API errors
    print(f"API error ({api_error.status}): {api_error.reason}")
    if api_error.request_id:
        print(f"  Request ID: {api_error.request_id}")
        print("  Include this ID when contacting BambooHR support.")

# ---------------------------------------------------------------------------
# Step 5: Fetch a single employee
# ---------------------------------------------------------------------------
# Once you know an employee ID, you can fetch specific fields.

print("\n=== Fetching a Single Employee ===\n")

try:
    employee = client.employees().get_employee(
        id="0",  # "0" is a special ID that returns the current API user
        fields="firstName,lastName,workEmail,department,jobTitle",
    )

    print(f"  Name: {employee.first_name} {employee.last_name}")

except ApiException as api_error:
    print(f"Could not fetch employee: {api_error.reason}")

# ---------------------------------------------------------------------------
# What's next?
# ---------------------------------------------------------------------------
#
# Now that you've made your first API call, explore more:
#
# 1. OAuth authentication:
#    See 02_oauth_with_auto_refresh.py
#
# 2. Error handling and retry:
#    See 04_error_handling.py
#
# 3. Common API patterns (CRUD, time off, reports, webhooks):
#    See 05_common_api_patterns.py
#
# 4. Full API documentation:
#    https://documentation.bamboohr.com
