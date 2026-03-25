"""
Example 05: Common API Patterns
=================================

Practical examples of the most common BambooHR API operations:

    1. Employee Directory
    2. Employee CRUD (Create, Read, Update)
    3. Time Off Requests
    4. Custom Reports
    5. Employee Files
    6. Webhooks
    7. Tabular Data

Each pattern shows the SDK call, response handling, and error handling.

Prerequisites:
    - pip install bamboohr-python
    - BambooHR API key or OAuth tokens

Usage:
    export BAMBOO_COMPANY="yourcompany"
    export BAMBOO_API_KEY="your_api_key_here"
    python examples/05_common_api_patterns.py
"""

import os

from bamboohr_sdk.client import BambooHRClient
from bamboohr_sdk.exceptions import ApiException, NotFoundException
from bamboohr_sdk.models import (
    Employee,
    NewWebHook,
    PostNewEmployee,
    RequestCustomReport,
    RequestCustomReportFilters,
    TimeOffRequest,
    TimeOffRequestDatesInner,
)

# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------

company = os.environ.get("BAMBOO_COMPANY", "yourcompany")
api_key = os.environ.get("BAMBOO_API_KEY", "your_api_key_here")
host = os.environ.get("BAMBOO_HOST")  # Optional: full base URL override

builder = BambooHRClient().with_api_key(api_key).with_retries(2)
client = (builder.with_host(host) if host else builder.for_company(company)).build()


# =====================================================================
# 1. Employee Directory
# =====================================================================

print("=== 1. Employee Directory ===\n")

try:
    directory = client.employees().get_employees_directory()
    employees = directory.employees or []
    print(f"Directory contains {len(employees)} employees")

    for emp in employees[:5]:
        print(f"  {emp.get('displayName', 'N/A')} | {emp.get('department', 'N/A')} | {emp.get('jobTitle', 'N/A')}")

except ApiException as api_error:
    print(f"Error: {api_error.reason}")


# =====================================================================
# 2. Employee CRUD
# =====================================================================

print("\n=== 2. Employee CRUD ===\n")

# --- Create ---
print("Creating a new employee...")
try:
    new_employee = PostNewEmployee(
        first_name="Jane",
        last_name="Smith",
    )
    response = client.employees().add_employee(post_new_employee=new_employee)
    print(f"  Created successfully (status {response.status_code})")

    # The new employee's ID is typically in the Location header
    location = response.headers.get("Location", "")
    employee_id = location.rstrip("/").split("/")[-1] if location else None
    print(f"  New employee ID: {employee_id}")

except ApiException as api_error:
    print(f"  Create failed: {api_error.reason}")
    employee_id = None

# --- Read ---
print("\nReading employee data...")
try:
    employee = client.employees().get_employee(
        id="0",  # "0" returns the current API user
        fields="firstName,lastName,workEmail,department,hireDate,jobTitle",
    )
    print(f"  Name: {employee.first_name} {employee.last_name}")

except ApiException as api_error:
    print(f"  Read failed: {api_error.reason}")

# --- Update ---
if employee_id:
    print(f"\nUpdating employee {employee_id}...")
    try:
        updates = Employee(
            first_name="Jane",
            last_name="Smith-Jones",
        )
        client.employees().update_employee(id=employee_id, employee=updates)
        print("  Updated successfully")

    except ApiException as api_error:
        print(f"  Update failed: {api_error.reason}")

# --- List with pagination ---
print("\nListing employees with pagination...")
try:
    result = client.employees().get_employees_list(
        fields="firstName,lastName,department",
    )
    data = result.data or []
    print(f"  Page contains {len(data)} employees")

    # Pagination info is in the _links and meta fields
    if result.meta:
        print(f"  Total count: {result.meta.total_count}")

except ApiException as api_error:
    print(f"  List failed: {api_error.reason}")


# =====================================================================
# 3. Time Off Requests
# =====================================================================

print("\n=== 3. Time Off Requests ===\n")

# --- List time off types ---
print("Available time off types:")
try:
    types_response = client.time_off().get_time_off_types()
    time_off_types = types_response.time_off_types or []
    for tot in time_off_types[:5]:
        print(f"  - {tot.name} (ID: {tot.id})")

except ApiException as api_error:
    print(f"  Error: {api_error.reason}")

# --- Create a time off request ---
print("\nCreating a time off request...")
try:
    time_off_request = TimeOffRequest(
        status="requested",
        start="2026-07-01",
        end="2026-07-05",
        time_off_type_id=1,  # Use an actual type ID from the list above
        dates=[
            TimeOffRequestDatesInner(ymd="2026-07-01", amount=8),
            TimeOffRequestDatesInner(ymd="2026-07-02", amount=8),
            TimeOffRequestDatesInner(ymd="2026-07-03", amount=8),
        ],
    )
    client.time_off().time_off_add_a_time_off_request(
        employee_id="0",
        time_off_request=time_off_request,
    )
    print("  Time off request submitted!")

except ApiException as api_error:
    print(f"  Error: {api_error.reason}")

# --- Who's out ---
print("\nWho's out this week:")
try:
    response = client.time_off().get_a_list_of_who_is_out(
        start="2026-03-10",
        end="2026-03-14",
    )
    print(f"  Response status: {response.status_code}")

except ApiException as api_error:
    print(f"  Error: {api_error.reason}")


# =====================================================================
# 4. Custom Reports
# =====================================================================

print("\n=== 4. Custom Reports ===\n")

# --- Run a custom report ---
print("Requesting a custom report...")
try:
    report_request = RequestCustomReport(
        title="Active Employees",
        filters=RequestCustomReportFilters(
            last_changed={"includeNull": "no"},
        ),
        fields=["firstName", "lastName", "department", "hireDate", "status"],
    )
    report_response = client.reports().request_custom_report(
        format="JSON",
        request_custom_report=report_request,
    )
    print(f"  Report status: {report_response.status_code}")

except ApiException as api_error:
    print(f"  Error: {api_error.reason}")

# --- Run a saved report ---
print("\nRunning a saved company report...")
try:
    saved_report = client.reports().get_company_report(
        id="1",  # Use an actual report ID
        format="JSON",
    )
    print(f"  Report status: {saved_report.status_code}")

except NotFoundException:
    print("  Report not found (use a valid report ID)")
except ApiException as api_error:
    print(f"  Error: {api_error.reason}")


# =====================================================================
# 5. Employee Files
# =====================================================================

print("\n=== 5. Employee Files ===\n")

# --- List files ---
print("Listing employee files...")
try:
    files_response = client.employee_files().list_employee_files(id="0")
    print(f"  Response status: {files_response.status_code}")

except ApiException as api_error:
    print(f"  Error: {api_error.reason}")

# --- Upload a file ---
# print("\nUploading a file...")
# try:
#     client.employee_files().upload_employee_file(id="123")
#     print("  File uploaded successfully")
# except ApiException as api_error:
#     print(f"  Error: {api_error.reason}")


# =====================================================================
# 6. Webhooks
# =====================================================================

print("\n=== 6. Webhooks ===\n")

# --- List webhooks ---
print("Listing webhooks...")
try:
    webhooks = client.webhooks().get_webhook_list()
    webhook_list = webhooks.webhooks or []
    print(f"  Found {len(webhook_list)} webhooks")
    for wh in webhook_list[:5]:
        print(f"  - {wh.name} (ID: {wh.id}, URL: {wh.url})")

except ApiException as api_error:
    print(f"  Error: {api_error.reason}")

# --- Create a webhook ---
print("\nCreating a webhook...")
try:
    new_webhook = NewWebHook(
        name="Employee Changes",
        url="https://yourapp.com/webhooks/bamboohr",
        monitor_fields=["firstName", "lastName", "department"],
        format="json",
        include_company_domain=True,
    )
    created = client.webhooks().post_webhook(new_web_hook=new_webhook)
    print(f"  Created webhook: {created.name} (ID: {created.id})")

    # The response includes a private key for verifying webhook signatures
    if created.private_key:
        print(f"  Private key (save this!): {created.private_key[:20]}...")
        print("  Use this key to verify webhook payloads via HMAC-SHA256")

except ApiException as api_error:
    print(f"  Error: {api_error.reason}")

# --- Get available fields ---
print("\nAvailable webhook monitor fields:")
try:
    fields = client.webhooks().get_monitor_fields()
    field_list = fields.fields or []
    for field in field_list[:10]:
        print(f"  - {field.name} ({field.alias})")
    if len(field_list) > 10:
        print(f"  ... and {len(field_list) - 10} more")

except ApiException as api_error:
    print(f"  Error: {api_error.reason}")


# =====================================================================
# 7. Tabular Data
# =====================================================================

print("\n=== 7. Tabular Data ===\n")

# --- Read table rows ---
print("Reading job history table...")
try:
    table_data = client.tabular_data().get_employee_table_row(
        id="0",
        table="jobInfo",
    )
    print(f"  Response status: {table_data.status_code}")

except ApiException as api_error:
    print(f"  Error: {api_error.reason}")

# --- Get changed table data ---
print("\nGetting recently changed table data...")
try:
    changes = client.tabular_data().get_changed_employee_table_data(
        table="jobInfo",
        since="2026-01-01T00:00:00Z",
    )
    print(f"  Response status: {changes.status_code}")

except ApiException as api_error:
    print(f"  Error: {api_error.reason}")

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
print("\n=== Summary ===\n")
print("The SDK provides typed methods for all BambooHR API endpoints.")
print("Key patterns:")
print("  - All methods return typed Pydantic models or ApiResponse objects")
print("  - Use .to_dict() on any model to get a plain dictionary")
print("  - All methods accept optional _request_timeout and _headers overrides")
print("  - Void endpoints return ApiResponse with status_code and headers")
