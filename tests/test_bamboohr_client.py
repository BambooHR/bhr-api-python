"""Tests for bamboohr_sdk.client.bamboohr_client module."""

import logging
from unittest.mock import MagicMock, patch

import pytest

from bamboohr_sdk.client.auth_builder import AuthBuilder
from bamboohr_sdk.client.bamboohr_client import BambooHRClient


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _build_client(**kwargs) -> BambooHRClient:
    """Return a fully-built client with sensible defaults."""
    defaults = {
        "api_key": "test-api-key",
        "domain": "acme",
    }
    defaults.update(kwargs)

    c = BambooHRClient()
    if "api_key" in defaults and defaults["api_key"]:
        c.with_api_key(defaults["api_key"])
    if "domain" in defaults and defaults["domain"]:
        c.for_company(defaults["domain"])
    return c.build()


# ===========================================================================
# Authentication delegation
# ===========================================================================


class TestAuthDelegation:
    """Fluent auth methods delegate to AuthBuilder."""

    def test_with_api_key(self):
        c = BambooHRClient().with_api_key("key123")
        assert c.auth_builder.auth_type == "api_key"

    def test_with_oauth(self):
        c = BambooHRClient().with_oauth("tok")
        assert c.auth_builder.auth_type == "oauth"

    def test_with_oauth_refresh(self):
        c = BambooHRClient().with_oauth_refresh("a", "r", "cid", "cs")
        assert c.auth_builder.auth_type == "oauth_refresh"
        assert c.auth_builder.has_oauth_refresh is True

    def test_on_token_refresh(self):
        cb = lambda *a: None
        c = BambooHRClient().with_api_key("k").on_token_refresh(cb)
        assert c.auth_builder.token_refresh_callback is cb


# ===========================================================================
# Configuration
# ===========================================================================


class TestConfiguration:
    """Tests for configuration fluent methods."""

    def test_for_company(self):
        c = BambooHRClient().for_company("acme")
        assert "acme.bamboohr.com" in c.configuration.host

    def test_for_company_empty_raises(self):
        with pytest.raises(ValueError, match="Company domain cannot be empty"):
            BambooHRClient().for_company("")

    def test_with_host(self):
        c = BambooHRClient().with_host("https://custom.example.com")
        assert c.configuration.host == "https://custom.example.com"

    def test_with_retries(self):
        c = BambooHRClient().with_retries(3)
        assert c.configuration.retries == 3

    def test_with_retries_out_of_range(self):
        with pytest.raises(ValueError, match="between 0 and 5"):
            BambooHRClient().with_retries(10)

    def test_with_retries_negative(self):
        with pytest.raises(ValueError, match="between 0 and 5"):
            BambooHRClient().with_retries(-1)

    def test_with_timeout(self):
        c = BambooHRClient().with_timeout(30.0)
        assert c.timeout == 30.0

    def test_with_timeout_tuple(self):
        c = BambooHRClient().with_timeout((5.0, 30.0))
        assert c.timeout == (5.0, 30.0)

    def test_with_timeout_propagates_to_configuration(self):
        c = _build_client()
        assert c.configuration.timeout is None  # no timeout by default

        c2 = (
            BambooHRClient()
            .with_api_key("k")
            .for_company("acme")
            .with_timeout(15.0)
            .build()
        )
        assert c2.configuration.timeout == 15.0

    def test_with_timeout_tuple_propagates_to_configuration(self):
        c = (
            BambooHRClient()
            .with_api_key("k")
            .for_company("acme")
            .with_timeout((5.0, 30.0))
            .build()
        )
        assert c.configuration.timeout == (5.0, 30.0)

    def test_with_debug(self):
        c = BambooHRClient().with_debug(True)
        assert c.configuration.debug is True

    def test_with_debug_off(self):
        c = BambooHRClient().with_debug(False)
        assert c.configuration.debug is False

    def test_with_http_client(self):
        mock_client = MagicMock()
        c = BambooHRClient().with_http_client(mock_client)
        assert c.api_client is mock_client

    def test_with_logging(self):
        c = BambooHRClient().with_logging(level=logging.DEBUG)
        # Should not raise; just configures the logger
        assert True


# ===========================================================================
# Build & Validation
# ===========================================================================


class TestBuild:
    """Tests for build() and validation."""

    def test_successful_build(self):
        client = _build_client()
        assert client.api_client is not None

    def test_missing_auth_raises(self):
        with pytest.raises(ValueError, match="Authentication is required"):
            BambooHRClient().for_company("acme").build()

    def test_missing_company_raises(self):
        with pytest.raises(ValueError, match="Company domain is required"):
            BambooHRClient().with_api_key("key").build()

    def test_default_host_raises(self):
        """The placeholder host should be rejected."""
        with pytest.raises(ValueError, match="Company domain is required"):
            c = BambooHRClient().with_api_key("key")
            # Don't call for_company — host stays at the default
            c.build()

    def test_build_with_oauth(self):
        client = (
            BambooHRClient()
            .with_oauth("token")
            .for_company("acme")
            .build()
        )
        assert client.api_client is not None
        assert client.configuration.access_token == "token"

    def test_build_with_api_key_sets_basic_auth(self):
        client = _build_client(api_key="my-key")
        assert client.configuration.username == "my-key"
        assert client.configuration.password == "x"

    def test_rebuild_clears_cache(self):
        client = _build_client()
        # Access an API to populate cache
        emp1 = client.employees()
        # Rebuild
        client.build()
        emp2 = client.employees()
        # After rebuild, cache was cleared so new instance is created
        assert emp1 is not emp2

    def test_chaining_returns_self(self):
        c = BambooHRClient()
        result = (
            c.with_api_key("k")
            .for_company("acme")
            .with_retries(2)
            .with_timeout(10.0)
            .with_debug(False)
        )
        assert result is c

    def test_build_with_injected_http_client(self):
        mock_client = MagicMock()
        client = (
            BambooHRClient()
            .with_api_key("k")
            .for_company("acme")
            .with_http_client(mock_client)
            .build()
        )
        # The injected client should be used, not a new one
        assert client.api_client is mock_client


# ===========================================================================
# API accessors
# ===========================================================================


class TestAPIAccessors:
    """Tests for convenience API accessor methods."""

    def test_raises_before_build(self):
        c = BambooHRClient().with_api_key("k").for_company("acme")
        with pytest.raises(RuntimeError, match="not been built"):
            c.employees()

    def test_employees(self):
        from bamboohr_sdk.api.employees_api import EmployeesApi
        client = _build_client()
        api = client.employees()
        assert isinstance(api, EmployeesApi)

    def test_time_off(self):
        from bamboohr_sdk.api.time_off_api import TimeOffApi
        client = _build_client()
        assert isinstance(client.time_off(), TimeOffApi)

    def test_benefits(self):
        from bamboohr_sdk.api.benefits_api import BenefitsApi
        client = _build_client()
        assert isinstance(client.benefits(), BenefitsApi)

    def test_reports(self):
        from bamboohr_sdk.api.reports_api import ReportsApi
        client = _build_client()
        assert isinstance(client.reports(), ReportsApi)

    def test_tabular_data(self):
        from bamboohr_sdk.api.tabular_data_api import TabularDataApi
        client = _build_client()
        assert isinstance(client.tabular_data(), TabularDataApi)

    def test_photos(self):
        from bamboohr_sdk.api.photos_api import PhotosApi
        client = _build_client()
        assert isinstance(client.photos(), PhotosApi)

    def test_webhooks(self):
        from bamboohr_sdk.api.webhooks_api import WebhooksApi
        client = _build_client()
        assert isinstance(client.webhooks(), WebhooksApi)

    def test_goals(self):
        from bamboohr_sdk.api.goals_api import GoalsApi
        client = _build_client()
        assert isinstance(client.goals(), GoalsApi)

    def test_training(self):
        from bamboohr_sdk.api.training_api import TrainingApi
        client = _build_client()
        assert isinstance(client.training(), TrainingApi)

    def test_time_tracking(self):
        from bamboohr_sdk.api.time_tracking_api import TimeTrackingApi
        client = _build_client()
        assert isinstance(client.time_tracking(), TimeTrackingApi)

    def test_account_information(self):
        from bamboohr_sdk.api.account_information_api import AccountInformationApi
        client = _build_client()
        assert isinstance(client.account_information(), AccountInformationApi)

    def test_applicant_tracking(self):
        from bamboohr_sdk.api.applicant_tracking_api import ApplicantTrackingApi
        client = _build_client()
        assert isinstance(client.applicant_tracking(), ApplicantTrackingApi)

    def test_company_files(self):
        from bamboohr_sdk.api.company_files_api import CompanyFilesApi
        client = _build_client()
        assert isinstance(client.company_files(), CompanyFilesApi)

    def test_employee_files(self):
        from bamboohr_sdk.api.employee_files_api import EmployeeFilesApi
        client = _build_client()
        assert isinstance(client.employee_files(), EmployeeFilesApi)

    def test_custom_reports(self):
        from bamboohr_sdk.api.custom_reports_api import CustomReportsApi
        client = _build_client()
        assert isinstance(client.custom_reports(), CustomReportsApi)

    def test_datasets(self):
        from bamboohr_sdk.api.datasets_api import DatasetsApi
        client = _build_client()
        assert isinstance(client.datasets(), DatasetsApi)

    def test_hours(self):
        from bamboohr_sdk.api.hours_api import HoursApi
        client = _build_client()
        assert isinstance(client.hours(), HoursApi)

    def test_last_change_information(self):
        from bamboohr_sdk.api.last_change_information_api import LastChangeInformationApi
        client = _build_client()
        assert isinstance(client.last_change_information(), LastChangeInformationApi)

    def test_login(self):
        from bamboohr_sdk.api.login_api import LoginApi
        client = _build_client()
        assert isinstance(client.login(), LoginApi)


class TestAPIAccessorCaching:
    """Tests for API accessor instance caching."""

    def test_same_instance_returned(self):
        client = _build_client()
        emp1 = client.employees()
        emp2 = client.employees()
        assert emp1 is emp2

    def test_different_apis_different_instances(self):
        client = _build_client()
        emp = client.employees()
        benefits = client.benefits()
        assert emp is not benefits

    def test_get_api_generic(self):
        from bamboohr_sdk.api.employees_api import EmployeesApi
        client = _build_client()
        api = client.get_api(EmployeesApi)
        assert isinstance(api, EmployeesApi)
        # Cached — same instance as the convenience accessor
        assert api is client.employees()


# ===========================================================================
# Pre-configured AuthBuilder
# ===========================================================================


class TestTimeoutCoalesce:
    """Tests that ApiClient.call_api uses config timeout as default."""

    def test_config_timeout_used_when_no_per_request_timeout(self):
        client = (
            BambooHRClient()
            .with_api_key("k")
            .for_company("acme")
            .with_timeout(15.0)
            .build()
        )
        api_client = client.api_client
        with patch.object(api_client.rest_client, "request") as mock_req:
            mock_resp = MagicMock()
            mock_resp.status = 200
            mock_resp.getheaders.return_value = {}
            mock_req.return_value = mock_resp

            api_client.call_api("GET", "https://acme.bamboohr.com/api/v1/test")
            _, kwargs = mock_req.call_args
            assert kwargs["_request_timeout"] == 15.0

    def test_per_request_timeout_overrides_config(self):
        client = (
            BambooHRClient()
            .with_api_key("k")
            .for_company("acme")
            .with_timeout(15.0)
            .build()
        )
        api_client = client.api_client
        with patch.object(api_client.rest_client, "request") as mock_req:
            mock_resp = MagicMock()
            mock_resp.status = 200
            mock_resp.getheaders.return_value = {}
            mock_req.return_value = mock_resp

            api_client.call_api("GET", "https://acme.bamboohr.com/api/v1/test", _request_timeout=5.0)
            _, kwargs = mock_req.call_args
            assert kwargs["_request_timeout"] == 5.0

    def test_no_timeout_when_neither_set(self):
        client = _build_client()
        api_client = client.api_client
        with patch.object(api_client.rest_client, "request") as mock_req:
            mock_resp = MagicMock()
            mock_resp.status = 200
            mock_resp.getheaders.return_value = {}
            mock_req.return_value = mock_resp

            api_client.call_api("GET", "https://acme.bamboohr.com/api/v1/test")
            _, kwargs = mock_req.call_args
            assert kwargs["_request_timeout"] is None


class TestLastRequestId:
    """Tests for last_request_id property on BambooHRClient."""

    def test_last_request_id_none_before_build(self):
        client = BambooHRClient()
        assert client.last_request_id is None

    def test_last_request_id_none_before_any_request(self):
        client = _build_client()
        assert client.last_request_id is None

    def test_last_request_id_extracted_after_call(self):
        client = _build_client()
        api_client = client.api_client
        with patch.object(api_client.rest_client, "request") as mock_req:
            mock_resp = MagicMock()
            mock_resp.status = 200
            mock_resp.getheader.return_value = "req-id-xyz"
            mock_resp.getheaders.return_value = {"x-request-id": "req-id-xyz"}
            mock_req.return_value = mock_resp

            api_client.call_api("GET", "https://acme.bamboohr.com/api/v1/test")
            assert client.last_request_id == "req-id-xyz"

    def test_last_request_id_updates_on_each_call(self):
        client = _build_client()
        api_client = client.api_client
        with patch.object(api_client.rest_client, "request") as mock_req:
            mock_resp1 = MagicMock()
            mock_resp1.status = 200
            mock_resp1.getheader.return_value = "first-id"
            mock_req.return_value = mock_resp1
            api_client.call_api("GET", "https://acme.bamboohr.com/api/v1/test")
            assert client.last_request_id == "first-id"

            mock_resp2 = MagicMock()
            mock_resp2.status = 200
            mock_resp2.getheader.return_value = "second-id"
            mock_req.return_value = mock_resp2
            api_client.call_api("GET", "https://acme.bamboohr.com/api/v1/test")
            assert client.last_request_id == "second-id"


class TestPreConfiguredAuthBuilder:
    """Tests for injecting a pre-configured AuthBuilder."""

    def test_accepts_auth_builder(self):
        ab = AuthBuilder().with_api_key("pre-key")
        client = BambooHRClient(auth_builder=ab).for_company("acme").build()
        assert client.configuration.username == "pre-key"
