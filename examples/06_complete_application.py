"""
Example 06: Complete Application
==================================

A real-world example showing how to structure a production application
that uses the BambooHR SDK. This implements an employee onboarding
dashboard service that:

    - Lists recent hires
    - Retrieves employee details
    - Checks time off balances
    - Generates onboarding reports

Demonstrates:
    - Service class pattern with dependency injection
    - Factory methods for different auth modes
    - Structured error handling
    - Reusable client across operations

Prerequisites:
    - pip install bamboohr-python

Usage:
    export BAMBOO_COMPANY="yourcompany"
    export BAMBOO_API_KEY="your_api_key_here"
    python examples/06_complete_application.py
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass, field

from bamboohr_sdk.client import BambooHRClient
from bamboohr_sdk.exceptions import ApiException, NotFoundException, ServiceException

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Data Transfer Objects
# ---------------------------------------------------------------------------
# Use simple dataclasses to decouple your application's data model from
# the SDK's API response models.


@dataclass
class OnboardingEmployee:
    """An employee in the onboarding pipeline."""

    id: str
    name: str
    department: str = ""
    job_title: str = ""
    hire_date: str = ""
    work_email: str = ""
    manager: str = ""


@dataclass
class OnboardingReport:
    """Summary report for onboarding status."""

    total_new_hires: int = 0
    by_department: dict[str, int] = field(default_factory=dict)
    employees: list[OnboardingEmployee] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Service Class
# ---------------------------------------------------------------------------


class OnboardingService:
    """Employee onboarding dashboard service.

    Encapsulates all BambooHR API interactions for the onboarding workflow.
    The BambooHRClient is injected via the constructor, making this class
    easy to test with a mock client.

    Args:
        client: A configured and built BambooHRClient instance.
    """

    def __init__(self, client: BambooHRClient) -> None:
        self._client = client

    # --- Factory Methods ---

    @classmethod
    def with_api_key(cls, company: str, api_key: str, *, host: str | None = None) -> OnboardingService:
        """Create a service instance using API key authentication."""
        builder = BambooHRClient().with_api_key(api_key).with_retries(3)
        client = (builder.with_host(host) if host else builder.for_company(company)).build()
        return cls(client)

    @classmethod
    def with_oauth(
        cls,
        company: str,
        access_token: str,
        refresh_token: str,
        client_id: str,
        client_secret: str,
        *,
        host: str | None = None,
        expires_in: int | None = None,
        on_refresh: object = None,
    ) -> OnboardingService:
        """Create a service instance using OAuth authentication."""
        builder = (
            BambooHRClient()
            .with_oauth_refresh(
                access_token=access_token,
                refresh_token=refresh_token,
                client_id=client_id,
                client_secret=client_secret,
                expires_in=expires_in,
            )
            .with_retries(3)
        )
        if on_refresh:
            builder.on_token_refresh(on_refresh)
        builder = builder.with_host(host) if host else builder.for_company(company)
        return cls(builder.build())

    # --- Business Operations ---

    def get_new_hires(self, limit: int = 50) -> list[OnboardingEmployee]:
        """Retrieve recent new hires from the employee directory.

        Args:
            limit: Maximum number of employees to return.

        Returns:
            List of OnboardingEmployee objects.
        """
        try:
            directory = self._client.employees().get_employees_directory()
            employees = directory.employees or []

            # Map API response to our domain model
            result = []
            for emp in employees[:limit]:
                result.append(
                    OnboardingEmployee(
                        id=str(emp.get("id", "")),
                        name=emp.get("displayName") or f"{emp.get('firstName', '')} {emp.get('lastName', '')}",
                        department=emp.get("department") or "",
                        job_title=emp.get("jobTitle") or "",
                    )
                )
            return result

        except ApiException as api_error:
            logger.error("Failed to fetch new hires: %s", api_error.reason)
            raise

    def get_employee_details(self, employee_id: str) -> OnboardingEmployee:
        """Fetch detailed information for a single employee.

        Args:
            employee_id: The BambooHR employee ID.

        Returns:
            OnboardingEmployee with full details.

        Raises:
            NotFoundException: If the employee doesn't exist.
            ApiException: For other API errors.
        """
        employee = self._client.employees().get_employee(
            id=employee_id,
            fields="firstName,lastName,department,jobTitle,hireDate,workEmail",
        )

        return OnboardingEmployee(
            id=employee_id,
            name=f"{employee.first_name} {employee.last_name}",
            department=employee.department or "",
            job_title=employee.job_title or "",
            hire_date=employee.hire_date or "",
            work_email=employee.work_email or "",
        )

    def get_time_off_balance(self, employee_id: str) -> list[dict]:
        """Fetch time off balances for an employee.

        Returns an empty list if the balance cannot be retrieved
        (non-critical data — graceful degradation).
        """
        try:
            balances = self._client.time_off().time_off_get_time_off_balance(
                employee_id=int(employee_id),
            )
            return [
                {
                    "type": entry.time_off_type or "Unknown",
                    "balance": entry.balance or 0,
                    "units": entry.units or "hours",
                }
                for entry in (balances or [])
            ]
        except ApiException as api_error:
            logger.warning(
                "Could not fetch time off balance for %s: %s",
                employee_id,
                api_error.reason,
            )
            return []  # Non-critical — degrade gracefully

    def generate_onboarding_report(self) -> OnboardingReport:
        """Generate a summary report of the onboarding pipeline.

        Returns:
            OnboardingReport with aggregated data.
        """
        employees = self.get_new_hires()

        by_department: dict[str, int] = {}
        for emp in employees:
            dept = emp.department or "Unassigned"
            by_department[dept] = by_department.get(dept, 0) + 1

        return OnboardingReport(
            total_new_hires=len(employees),
            by_department=by_department,
            employees=employees,
        )


# ---------------------------------------------------------------------------
# Application Entry Point
# ---------------------------------------------------------------------------


def main() -> None:
    """Run the onboarding dashboard demo."""
    company = os.environ.get("BAMBOO_COMPANY", "yourcompany")
    api_key = os.environ.get("BAMBOO_API_KEY", "your_api_key_here")
    host = os.environ.get("BAMBOO_HOST")  # Optional: full base URL override

    print("=== Employee Onboarding Dashboard ===\n")

    # Create the service (swap with_oauth for production)
    service = OnboardingService.with_api_key(company, api_key, host=host)

    # --- Generate Report ---
    try:
        report = service.generate_onboarding_report()
        print(f"Total employees: {report.total_new_hires}\n")

        print("By department:")
        for dept, count in sorted(report.by_department.items()):
            print(f"  {dept}: {count}")

        print(f"\nEmployees ({min(5, len(report.employees))} shown):")
        for emp in report.employees[:5]:
            print(f"  - {emp.name} | {emp.department} | {emp.job_title}")

    except ServiceException as server_error:
        print(f"Server error: {server_error.reason}")
        if server_error.request_id:
            print(f"Request ID: {server_error.request_id}")
    except ApiException as api_error:
        print(f"API error: {api_error.reason}")

    # --- Employee Details ---
    print("\n--- Current User Details ---\n")

    try:
        details = service.get_employee_details("0")
        print(f"  Name:       {details.name}")
        print(f"  Department: {details.department}")
        print(f"  Job Title:  {details.job_title}")
        print(f"  Hire Date:  {details.hire_date}")
        print(f"  Email:      {details.work_email}")

    except NotFoundException:
        print("  Employee not found")
    except ApiException as api_error:
        print(f"  Error: {api_error.reason}")


if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------------
# Architecture Notes
# ---------------------------------------------------------------------------
#
# This example demonstrates several production patterns:
#
# 1. Dependency Injection
#    The service accepts a BambooHRClient in its constructor. This makes
#    it trivial to inject a mock client in tests (see 07_testing_patterns.py).
#
# 2. Factory Methods
#    with_api_key() and with_oauth() encapsulate client construction,
#    keeping calling code clean and auth-mode-agnostic.
#
# 3. Domain Decoupling
#    OnboardingEmployee is our own dataclass, not an SDK model. This
#    insulates our application from SDK API changes.
#
# 4. Graceful Degradation
#    get_time_off_balance() returns an empty list on failure rather than
#    crashing, because time off data is non-critical for the dashboard.
#
# 5. Structured Error Handling
#    Critical operations (get_employee_details) propagate exceptions.
#    Non-critical operations (get_time_off_balance) catch and log.
