"""Fluent API client for the BambooHR SDK.

Provides a builder-pattern interface for configuring authentication,
company domain, retries, timeouts, logging, and accessing API resources.

Usage::

    from bamboohr_sdk.client import BambooHRClient

    client = (
        BambooHRClient()
        .with_api_key("your-api-key")
        .for_company("acme")
        .with_retries(3)
        .build()
    )

    employees = client.employees().get_employee_by_id(company_domain="acme", id="123")
"""

from __future__ import annotations

import logging
from typing import Any, Callable, Dict, Optional, Type, TypeVar, Union

from bamboohr_sdk.api_client import ApiClient
from bamboohr_sdk.client.auth_builder import AuthBuilder, TokenRefreshCallback
from bamboohr_sdk.client.auth.token_manager import TokenManager
from bamboohr_sdk.client.auth.token_refresh_provider import BambooHRTokenRefreshProvider
from bamboohr_sdk.client.middleware.oauth2_middleware import OAuth2Middleware
from bamboohr_sdk.configuration import Configuration

logger = logging.getLogger("bamboohr_sdk")

T = TypeVar("T")

# Default placeholder host that indicates the company domain hasn't been set
_DEFAULT_HOST = "https://companySubDomain.bamboohr.com"


class BambooHRClient:
    """Fluent API client for configuring and using the BambooHR SDK.

    This class wraps the auto-generated SDK classes to provide a cleaner,
    more intuitive interface for authentication and configuration.

    :param auth_builder: Optional pre-configured :class:`AuthBuilder`.
    """

    def __init__(self, auth_builder: Optional[AuthBuilder] = None) -> None:
        self._config = Configuration()
        self._auth_builder = auth_builder or AuthBuilder()
        self._api_client: Optional[ApiClient] = None
        self._timeout: Optional[Union[float, tuple]] = None
        self._built = False

        # OAuth refresh components (created in build() when applicable)
        self._token_manager: Optional[TokenManager] = None
        self._refresh_provider: Optional[BambooHRTokenRefreshProvider] = None
        self._oauth2_middleware: Optional[OAuth2Middleware] = None

        # Cache for API accessor instances
        self._api_cache: Dict[type, Any] = {}

    # ------------------------------------------------------------------
    # Authentication (delegated to AuthBuilder)
    # ------------------------------------------------------------------

    def with_api_key(self, api_key: str) -> BambooHRClient:
        """Configure API key authentication.

        :param api_key: Your BambooHR API key.
        :return: self for chaining.
        """
        self._auth_builder.with_api_key(api_key)
        logger.debug("Configured API key authentication")
        return self

    def with_oauth(self, token: str) -> BambooHRClient:
        """Configure OAuth bearer token authentication.

        :param token: Your OAuth access token.
        :return: self for chaining.
        """
        self._auth_builder.with_oauth(token)
        logger.debug("Configured OAuth authentication")
        return self

    def with_oauth_refresh(
        self,
        access_token: str,
        refresh_token: str,
        client_id: str,
        client_secret: str,
        expires_in: Optional[int] = None,
    ) -> BambooHRClient:
        """Configure OAuth with automatic token refresh.

        :param access_token: Current OAuth access token.
        :param refresh_token: OAuth refresh token.
        :param client_id: OAuth client ID.
        :param client_secret: OAuth client secret.
        :param expires_in: Seconds until the access token expires (optional).
        :return: self for chaining.
        """
        self._auth_builder.with_oauth_refresh(
            access_token, refresh_token, client_id, client_secret, expires_in
        )
        logger.debug(
            "Configured OAuth with automatic refresh (has_expiry=%s)",
            expires_in is not None,
        )
        return self

    def on_token_refresh(self, callback: TokenRefreshCallback) -> BambooHRClient:
        """Register a callback invoked when OAuth tokens are refreshed.

        :param callback: Callable receiving
            ``(new_access_token, new_refresh_token, old_access_token, old_refresh_token)``.
        :return: self for chaining.
        """
        self._auth_builder.on_token_refresh(callback)
        logger.debug("Token refresh callback registered")
        return self

    # ------------------------------------------------------------------
    # Configuration
    # ------------------------------------------------------------------

    def for_company(self, domain: str) -> BambooHRClient:
        """Set the company subdomain.

        :param domain: Your company's BambooHR subdomain
            (e.g. ``"acme"`` for ``acme.bamboohr.com``).
        :return: self for chaining.
        """
        if not domain:
            raise ValueError("Company domain cannot be empty")
        self._config.host = f"https://{domain}.bamboohr.com"
        logger.debug("Set company domain: %s", domain)
        return self

    def with_host(self, host: str) -> BambooHRClient:
        """Set a custom host URL.

        :param host: Full host URL (e.g. ``"https://custom.bamboohr.com"``).
        :return: self for chaining.
        """
        self._config.host = host
        return self

    def with_retries(self, retries: int) -> BambooHRClient:
        """Configure the number of application-level retries.

        :param retries: Number of retries (0–5).
        :return: self for chaining.
        :raises ValueError: If *retries* is outside the 0–5 range.
        """
        if not 0 <= retries <= 5:
            raise ValueError(
                f"Retries must be between 0 and 5, got {retries}"
            )
        self._config.retries = retries
        return self

    def with_timeout(self, seconds: Union[float, tuple]) -> BambooHRClient:
        """Configure the request timeout.

        :param seconds: Timeout in seconds. Pass a ``float`` for a single
            timeout or a ``(connect, read)`` tuple for separate values.
        :return: self for chaining.
        """
        self._timeout = seconds
        return self

    def with_debug(self, debug: bool = True) -> BambooHRClient:
        """Enable or disable debug mode.

        :param debug: Whether to enable debug mode.
        :return: self for chaining.
        """
        self._config.debug = debug
        logger.debug("Debug mode %s", "enabled" if debug else "disabled")
        return self

    def with_http_client(self, client: ApiClient) -> BambooHRClient:
        """Inject a custom :class:`ApiClient` instance.

        This replaces the auto-created client entirely — useful for testing
        or advanced customisation.

        :param client: Pre-configured ``ApiClient``.
        :return: self for chaining.
        """
        self._api_client = client
        logger.debug("Custom HTTP client configured")
        return self

    def with_logging(
        self,
        log_logger: Optional[logging.Logger] = None,
        level: int = logging.INFO,
    ) -> BambooHRClient:
        """Enable SDK logging.

        :param log_logger: A :class:`logging.Logger` instance.
            Defaults to the ``bamboohr_sdk`` logger.
        :param level: Logging level (e.g. ``logging.DEBUG``).
        :return: self for chaining.
        """
        target = log_logger or logger
        target.setLevel(level)
        if not target.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(
                logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
            )
            target.addHandler(handler)
        logger.info("Logging enabled at level %s", logging.getLevelName(level))
        return self

    # ------------------------------------------------------------------
    # Build
    # ------------------------------------------------------------------

    def build(self) -> BambooHRClient:
        """Validate configuration and prepare the client for use.

        :return: self (now ready for API calls).
        :raises ValueError: If authentication or company domain is missing.
        """
        logger.info("Building BambooHR API client")

        # Apply authentication to Configuration
        if self._auth_builder.is_configured:
            self._auth_builder.apply_to(self._config)
            auth_info = self._auth_builder.get_sanitized_info()
            logger.info("Authentication configured: %s", auth_info)

        # Validate
        self._validate_configuration()

        # Initialize OAuth refresh if configured
        if self._auth_builder.has_oauth_refresh:
            self._setup_oauth_refresh()

        # Create the generated ApiClient if not injected
        if self._api_client is None:
            self._api_client = ApiClient(configuration=self._config)

        # Clear API cache on rebuild
        self._api_cache.clear()
        self._built = True

        logger.info("BambooHR API client built successfully")
        return self

    # ------------------------------------------------------------------
    # Generic API accessor
    # ------------------------------------------------------------------

    def get_api(self, api_class: Type[T]) -> T:
        """Get an instance of any generated API class.

        Instances are cached for the lifetime of this client; the same
        :class:`ApiClient` is shared across all accessors.

        :param api_class: The API class to instantiate
            (e.g. ``EmployeesApi``).
        :return: An instance of *api_class*.
        :raises RuntimeError: If :meth:`build` has not been called.
        """
        self._ensure_built()

        if api_class not in self._api_cache:
            self._api_cache[api_class] = api_class(api_client=self._api_client)
            logger.debug("Created API instance: %s", api_class.__name__)

        return self._api_cache[api_class]

    # ------------------------------------------------------------------
    # Convenience API accessors
    # ------------------------------------------------------------------

    def employees(self):
        """Access the Employees API."""
        from bamboohr_sdk.api.employees_api import EmployeesApi
        return self.get_api(EmployeesApi)

    def time_off(self):
        """Access the Time Off API."""
        from bamboohr_sdk.api.time_off_api import TimeOffApi
        return self.get_api(TimeOffApi)

    def benefits(self):
        """Access the Benefits API."""
        from bamboohr_sdk.api.benefits_api import BenefitsApi
        return self.get_api(BenefitsApi)

    def reports(self):
        """Access the Reports API."""
        from bamboohr_sdk.api.reports_api import ReportsApi
        return self.get_api(ReportsApi)

    def tabular_data(self):
        """Access the Tabular Data API."""
        from bamboohr_sdk.api.tabular_data_api import TabularDataApi
        return self.get_api(TabularDataApi)

    def photos(self):
        """Access the Photos API."""
        from bamboohr_sdk.api.photos_api import PhotosApi
        return self.get_api(PhotosApi)

    def webhooks(self):
        """Access the Webhooks API."""
        from bamboohr_sdk.api.webhooks_api import WebhooksApi
        return self.get_api(WebhooksApi)

    def goals(self):
        """Access the Goals API."""
        from bamboohr_sdk.api.goals_api import GoalsApi
        return self.get_api(GoalsApi)

    def training(self):
        """Access the Training API."""
        from bamboohr_sdk.api.training_api import TrainingApi
        return self.get_api(TrainingApi)

    def time_tracking(self):
        """Access the Time Tracking API."""
        from bamboohr_sdk.api.time_tracking_api import TimeTrackingApi
        return self.get_api(TimeTrackingApi)

    def account_information(self):
        """Access the Account Information API."""
        from bamboohr_sdk.api.account_information_api import AccountInformationApi
        return self.get_api(AccountInformationApi)

    def applicant_tracking(self):
        """Access the Applicant Tracking API."""
        from bamboohr_sdk.api.applicant_tracking_api import ApplicantTrackingApi
        return self.get_api(ApplicantTrackingApi)

    def company_files(self):
        """Access the Company Files API."""
        from bamboohr_sdk.api.company_files_api import CompanyFilesApi
        return self.get_api(CompanyFilesApi)

    def employee_files(self):
        """Access the Employee Files API."""
        from bamboohr_sdk.api.employee_files_api import EmployeeFilesApi
        return self.get_api(EmployeeFilesApi)

    def custom_reports(self):
        """Access the Custom Reports API."""
        from bamboohr_sdk.api.custom_reports_api import CustomReportsApi
        return self.get_api(CustomReportsApi)

    def datasets(self):
        """Access the Datasets API."""
        from bamboohr_sdk.api.datasets_api import DatasetsApi
        return self.get_api(DatasetsApi)

    def hours(self):
        """Access the Hours API."""
        from bamboohr_sdk.api.hours_api import HoursApi
        return self.get_api(HoursApi)

    def last_change_information(self):
        """Access the Last Change Information API."""
        from bamboohr_sdk.api.last_change_information_api import LastChangeInformationApi
        return self.get_api(LastChangeInformationApi)

    def login(self):
        """Access the Login API."""
        from bamboohr_sdk.api.login_api import LoginApi
        return self.get_api(LoginApi)

    # ------------------------------------------------------------------
    # Introspection
    # ------------------------------------------------------------------

    @property
    def configuration(self) -> Configuration:
        """Return the underlying :class:`Configuration` object."""
        return self._config

    @property
    def auth_builder(self) -> AuthBuilder:
        """Return the :class:`AuthBuilder` instance."""
        return self._auth_builder

    @property
    def api_client(self) -> Optional[ApiClient]:
        """Return the generated :class:`ApiClient`, or ``None`` before build."""
        return self._api_client

    @property
    def timeout(self) -> Optional[Union[float, tuple]]:
        """Return the configured timeout."""
        return self._timeout

    @property
    def token_manager(self) -> Optional[TokenManager]:
        """Return the :class:`TokenManager`, or ``None`` if OAuth refresh is not configured."""
        return self._token_manager

    @property
    def oauth2_middleware(self) -> Optional[OAuth2Middleware]:
        """Return the :class:`OAuth2Middleware`, or ``None`` if OAuth refresh is not configured."""
        return self._oauth2_middleware

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _ensure_built(self) -> None:
        """Raise if :meth:`build` has not been called."""
        if not self._built:
            raise RuntimeError(
                "Client has not been built. Call .build() before accessing APIs."
            )

    def _setup_oauth_refresh(self) -> None:
        """Create TokenManager, RefreshProvider, and OAuth2Middleware."""
        ab = self._auth_builder

        refresh_token = ab.refresh_token
        client_id = ab.client_id
        client_secret = ab.client_secret
        expires_in = ab.expires_in
        access_token = self._config.access_token

        if not refresh_token or not client_id or not client_secret:
            logger.warning(
                "OAuth refresh configured but missing required parameters"
            )
            return

        self._token_manager = TokenManager(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_in=expires_in,
            on_token_refresh=ab.token_refresh_callback,
        )

        api_host = self._config.host
        self._refresh_provider = BambooHRTokenRefreshProvider(
            client_id=client_id,
            client_secret=client_secret,
            api_host=api_host,
        )

        self._oauth2_middleware = OAuth2Middleware(
            token_manager=self._token_manager,
            refresh_provider=self._refresh_provider,
            config=self._config,
        )

        logger.info(
            "OAuth token refresh enabled (has_expiry=%s, has_callback=%s)",
            expires_in is not None,
            ab.token_refresh_callback is not None,
        )

    def _validate_configuration(self) -> None:
        """Validate that required configuration is present.

        :raises ValueError: If authentication or company domain is missing.
        """
        # Authentication check
        has_api_key = bool(self._config.username)
        has_oauth = bool(self._config.access_token)

        if not has_api_key and not has_oauth:
            raise ValueError(
                "Authentication is required. "
                "Use with_api_key() or with_oauth() before calling build()."
            )

        # Company domain check
        host = self._config.host
        if not host or host == _DEFAULT_HOST:
            raise ValueError(
                "Company domain is required. "
                "Use for_company() to set your company subdomain."
            )
