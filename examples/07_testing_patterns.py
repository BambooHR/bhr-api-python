"""
Example 07: Testing Patterns
==============================

Demonstrates how to write testable code with the BambooHR Python SDK,
covering:

    1. Dependency injection for testability
    2. Mocking the SDK client with unittest.mock
    3. Testing error handling paths
    4. Testing OAuth token refresh callbacks
    5. Integration test patterns

All examples use Python's built-in ``unittest`` and ``unittest.mock`` —
no additional test dependencies required (though pytest works too).

Prerequisites:
    - pip install bamboohr-python

Usage:
    python -m pytest examples/07_testing_patterns.py -v
    # or
    python examples/07_testing_patterns.py
"""

from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from bamboohr_sdk.client import BambooHRClient
from bamboohr_sdk.exceptions import (
    ApiException,
    AuthenticationFailedException,
    ResourceNotFoundException,
    ServerException,
)

# ---------------------------------------------------------------------------
# The Service Under Test
# ---------------------------------------------------------------------------
# This is the same pattern from 06_complete_application.py — a service
# class that accepts a BambooHRClient via constructor injection.


class EmployeeService:
    """Service that wraps BambooHR employee operations.

    Designed for testability via constructor injection.
    """

    def __init__(self, client: BambooHRClient) -> None:
        self._client = client

    def get_employee_name(self, employee_id: str) -> str:
        """Fetch an employee's display name.

        Returns "Unknown" if the employee is not found.
        """
        try:
            employee = self._client.employees().get_employee(
                id=employee_id,
                fields="firstName,lastName",
            )
            return f"{employee.first_name} {employee.last_name}"
        except ResourceNotFoundException:
            return "Unknown"

    def get_department_headcount(self) -> dict[str, int]:
        """Count employees by department from the directory."""
        directory = self._client.employees().get_employees_directory()
        counts: dict[str, int] = {}
        for emp in directory.employees or []:
            dept = emp.get("department") or "Unassigned"
            counts[dept] = counts.get(dept, 0) + 1
        return counts

    def is_api_healthy(self) -> bool:
        """Health check — returns False if the API is unreachable."""
        try:
            self._client.employees().get_employees_directory()
            return True
        except ApiException:
            return False


# =====================================================================
# Pattern 1: Basic Mocking
# =====================================================================


class TestEmployeeServiceBasicMocking(unittest.TestCase):
    """Demonstrates basic mocking of the BambooHRClient."""

    def setUp(self) -> None:
        """Create a mock client for each test."""
        self.mock_client = MagicMock(spec=BambooHRClient)
        self.service = EmployeeService(self.mock_client)

    def test_get_employee_name(self) -> None:
        """Test fetching an employee's name."""
        # Arrange: configure the mock to return employee data
        mock_employee = MagicMock()
        mock_employee.first_name = "Jane"
        mock_employee.last_name = "Smith"

        self.mock_client.employees().get_employee.return_value = mock_employee

        # Act
        name = self.service.get_employee_name("123")

        # Assert
        self.assertEqual(name, "Jane Smith")
        self.mock_client.employees().get_employee.assert_called_once_with(
            id="123",
            fields="firstName,lastName",
        )

    def test_get_employee_name_not_found(self) -> None:
        """Test graceful handling when employee doesn't exist."""
        self.mock_client.employees().get_employee.side_effect = ResourceNotFoundException(status=404, reason="Not found")

        name = self.service.get_employee_name("999")

        self.assertEqual(name, "Unknown")

    def test_get_department_headcount(self) -> None:
        """Test department counting logic."""
        mock_directory = MagicMock()
        # Directory employees are dicts with camelCase keys (list[dict[str, Any]])
        emp1 = {"id": "1", "displayName": "Alice", "department": "Engineering"}
        emp2 = {"id": "2", "displayName": "Bob", "department": "Engineering"}
        emp3 = {"id": "3", "displayName": "Carol", "department": "Marketing"}
        mock_directory.employees = [emp1, emp2, emp3]

        self.mock_client.employees().get_employees_directory.return_value = mock_directory

        counts = self.service.get_department_headcount()

        self.assertEqual(counts, {"Engineering": 2, "Marketing": 1})


# =====================================================================
# Pattern 2: Testing Error Handling
# =====================================================================


class TestErrorHandling(unittest.TestCase):
    """Test that errors are handled correctly."""

    def setUp(self) -> None:
        self.mock_client = MagicMock(spec=BambooHRClient)
        self.service = EmployeeService(self.mock_client)

    def test_health_check_succeeds(self) -> None:
        """Health check returns True when API is reachable."""
        self.mock_client.employees().get_employees_directory.return_value = MagicMock()

        self.assertTrue(self.service.is_api_healthy())

    def test_health_check_fails_on_auth_error(self) -> None:
        """Health check returns False on authentication failure."""
        self.mock_client.employees().get_employees_directory.side_effect = AuthenticationFailedException(
            status=401, reason="Unauthorized"
        )

        self.assertFalse(self.service.is_api_healthy())

    def test_health_check_fails_on_server_error(self) -> None:
        """Health check returns False on server error."""
        self.mock_client.employees().get_employees_directory.side_effect = ServerException(
            status=500, reason="Internal Server Error"
        )

        self.assertFalse(self.service.is_api_healthy())

    def test_get_employee_propagates_auth_errors(self) -> None:
        """Auth errors propagate (they're not caught by get_employee_name)."""
        self.mock_client.employees().get_employee.side_effect = AuthenticationFailedException(status=401, reason="Unauthorized")

        with self.assertRaises(AuthenticationFailedException):
            self.service.get_employee_name("123")


# =====================================================================
# Pattern 3: Testing OAuth Token Refresh
# =====================================================================


class TestOAuthTokenRefresh(unittest.TestCase):
    """Test token refresh callback behavior."""

    def test_token_refresh_callback_is_invoked(self) -> None:
        """Verify the callback receives old and new tokens."""
        captured_tokens: list[tuple] = []

        def on_refresh(
            new_access: str,
            new_refresh: str | None,
            old_access: str,
            old_refresh: str | None,
        ) -> None:
            captured_tokens.append((new_access, new_refresh, old_access, old_refresh))

        # Build a client with the callback
        # (We won't actually make API calls — just verify wiring)
        client = (
            BambooHRClient()
            .with_oauth_refresh(
                access_token="old_access",
                refresh_token="old_refresh",
                client_id="test_id",
                client_secret="test_secret",
                expires_in=3600,
            )
            .on_token_refresh(on_refresh)
            .for_company("testcompany")
            .build()
        )

        # Simulate a token refresh by updating the token manager directly
        from bamboohr_sdk.client.auth.token_manager import TokenResponse

        token_mgr = client.token_manager
        self.assertIsNotNone(token_mgr)

        token_mgr.update_tokens(
            TokenResponse(
                access_token="new_access",
                refresh_token="new_refresh",
                expires_in=7200,
            )
        )

        # Verify callback was called with correct tokens
        self.assertEqual(len(captured_tokens), 1)
        new_access, new_refresh, old_access, old_refresh = captured_tokens[0]
        self.assertEqual(new_access, "new_access")
        self.assertEqual(new_refresh, "new_refresh")
        self.assertEqual(old_access, "old_access")
        self.assertEqual(old_refresh, "old_refresh")


# =====================================================================
# Pattern 4: Integration Test Base Class
# =====================================================================


class BambooHRIntegrationTest(unittest.TestCase):
    """Base class for integration tests that call the real BambooHR API.

    Skips automatically if credentials are not configured. Set these
    environment variables to run integration tests:

        BAMBOO_COMPANY=yourcompany
        BAMBOO_API_KEY=your_api_key
    """

    client: BambooHRClient

    @classmethod
    def setUpClass(cls) -> None:
        import os

        company = os.environ.get("BAMBOO_COMPANY")
        api_key = os.environ.get("BAMBOO_API_KEY")
        host = os.environ.get("BAMBOO_HOST")

        if not company or not api_key:
            raise unittest.SkipTest("Integration tests require BAMBOO_COMPANY and BAMBOO_API_KEY")

        builder = BambooHRClient().with_api_key(api_key).with_retries(2)
        cls.client = (builder.with_host(host) if host else builder.for_company(company)).build()


class TestDirectoryIntegration(BambooHRIntegrationTest):
    """Integration test: verify directory endpoint works end-to-end."""

    def test_directory_returns_employees(self) -> None:
        directory = self.client.employees().get_employees_directory()
        self.assertIsNotNone(directory.employees)
        self.assertGreater(len(directory.employees), 0)

    def test_current_user_is_fetchable(self) -> None:
        employee = self.client.employees().get_employee(
            id="0",
            fields="firstName,lastName",
        )
        self.assertIsNotNone(employee.first_name)


# =====================================================================
# Pattern 5: Factory for Test Fixtures
# =====================================================================


class MockEmployeeFactory:
    """Factory for creating mock employee objects in tests.

    Centralizes test data creation so tests stay clean and DRY.
    """

    @staticmethod
    def create(
        first_name: str = "Test",
        last_name: str = "User",
        department: str = "Engineering",
        **kwargs: object,
    ) -> MagicMock:
        """Create a mock employee with sensible defaults."""
        mock = MagicMock()
        mock.first_name = first_name
        mock.last_name = last_name
        mock.department = department
        mock.display_name = f"{first_name} {last_name}"
        mock.job_title = kwargs.get("job_title", "Software Engineer")
        mock.work_email = kwargs.get("work_email", f"{first_name.lower()}.{last_name.lower()}@example.com")
        mock.hire_date = kwargs.get("hire_date", "2026-01-15")
        mock.id = kwargs.get("id", "123")
        return mock

    @staticmethod
    def create_directory(employees: list[dict] | None = None) -> MagicMock:
        """Create a mock directory response.

        Directory employees are dicts with camelCase keys, matching the real
        API response shape (list[dict[str, Any]]).
        """
        mock_dir = MagicMock()
        mock_dir.employees = employees or [
            {"id": "1", "displayName": "Alice Smith", "department": "Engineering"},
            {"id": "2", "displayName": "Bob Jones", "department": "Marketing"},
            {"id": "3", "displayName": "Carol White", "department": "Engineering"},
        ]
        return mock_dir


class TestWithFactory(unittest.TestCase):
    """Demonstrate using the mock factory for cleaner tests."""

    def test_headcount_with_factory(self) -> None:
        mock_client = MagicMock(spec=BambooHRClient)
        service = EmployeeService(mock_client)

        mock_client.employees().get_employees_directory.return_value = MockEmployeeFactory.create_directory()

        counts = service.get_department_headcount()
        self.assertEqual(counts["Engineering"], 2)
        self.assertEqual(counts["Marketing"], 1)


# ---------------------------------------------------------------------------
# Run tests
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=== BambooHR SDK Testing Patterns ===\n")
    print("Running tests...\n")
    unittest.main(verbosity=2)

# ---------------------------------------------------------------------------
# Best Practices
# ---------------------------------------------------------------------------
#
# 1. Unit Tests
#    - Always inject the client via constructor (not global state)
#    - Use MagicMock(spec=BambooHRClient) to catch typos in method names
#    - Test both success and error paths
#
# 2. Integration Tests
#    - Use the BambooHRIntegrationTest base class to auto-skip
#    - Never hardcode credentials
#    - Keep integration tests idempotent (clean up created resources)
#
# 3. OAuth Tests
#    - Test callback wiring by simulating token refresh
#    - Verify old + new tokens are passed correctly
#
# 4. Test Data
#    - Use factories for consistent, readable test data
#    - Avoid copying real employee data into tests
#
# 5. CI/CD
#    - Run unit tests on every PR (no credentials needed)
#    - Run integration tests in a dedicated environment with real credentials
#    - Mock external calls in unit tests — never hit the real API
