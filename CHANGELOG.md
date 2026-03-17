# Changelog

All notable changes to the BambooHR Python SDK are documented here.

This project follows [Semantic Versioning](https://semver.org/).

---

## [1.0.0] — Initial Release

### Added

#### Client & Authentication
- `BambooHRClient` — fluent builder for configuring authentication, company domain, retries, timeouts, and logging
- `AuthBuilder` — dedicated authentication builder supporting three modes:
  - API key (HTTP Basic Auth)
  - OAuth 2.0 bearer token
  - OAuth 2.0 with automatic token refresh
- `on_token_refresh` callback — notifies the application when OAuth tokens are refreshed so they can be persisted; the SDK itself does not store tokens
- `TokenManager` — tracks token expiration and triggers proactive refresh 5 minutes before expiry
- `BambooHRTokenRefreshProvider` — handles the token refresh HTTP request against the BambooHR token endpoint
- `OAuth2Middleware` — transparently injects refreshed tokens into outgoing requests

#### API Coverage
Auto-generated API classes covering all public BambooHR endpoints:
- `AccountInformationApi`
- `ApplicantTrackingApi`
- `BenefitsApi`
- `CompanyFilesApi`
- `CustomReportsApi`
- `DatasetsApi`
- `EmployeeFilesApi`
- `EmployeesApi`
- `GoalsApi`
- `HoursApi`
- `LastChangeInformationApi`
- `LoginApi`
- `PhotosApi`
- `ReportsApi`
- `TabularDataApi`
- `TimeOffApi`
- `TimeTrackingApi`
- `TrainingApi`
- `WebhookEventsApi`
- `WebhooksApi`
- `ManualApi` — hand-written client for making arbitrary HTTP requests while using the SDK's built-in authentication, error handling, retry logic, and logging

#### Reliability
- Automatic retry with exponential backoff (100 ms, 200 ms, 400 ms, …) on HTTP 408, 429, 504, and 598 responses; configurable via `with_retries()` (0–5, default 1)
- HTTPS enforcement — host URLs are automatically upgraded from `http://` to `https://`
- Custom `User-Agent` header (`BHR-SDK/{version}/Python`) on all requests
- Request ID extraction — `ApiException.request_id` is automatically populated from `x-request-id`, `x-bamboohr-request-id`, or `request-id` response headers

#### Error Handling
Typed exception hierarchy mapped to HTTP status codes:
- `ApiException` — base class for all API errors
- `ClientException` — base class for 4xx errors
- `ServerException` — base class for 5xx errors
- `BadRequestException` (400)
- `AuthenticationFailedException` (401)
- `PermissionDeniedException` (403)
- `ResourceNotFoundException` (404)
- `MethodNotAllowedException` (405)
- `RequestTimeoutException` (408)
- `ConflictException` (409)
- `PayloadTooLargeException` (413)
- `UnsupportedMediaTypeException` (415)
- `UnprocessableEntityException` (422)
- `RateLimitExceededException` (429)
- `InternalServerErrorException` (500)
- `NotImplementedException` (501)
- `BadGatewayException` (502)
- `ServiceUnavailableException` (503)
- `GatewayTimeoutException` (504)
- `InsufficientStorageException` (507)
- `NetworkReadTimeoutException` (598)

Each exception class includes `potential_causes()` and `debugging_tips()` static methods via `api_error_helper`.

#### Logging
- `SecureLogFilter` — automatically redacts sensitive headers (Authorization, API keys, cookies) and URL query parameters from log output
- SDK logs under the `bamboohr_sdk` logger name using Python's standard `logging` module
- `with_logging()` builder method for convenient log level and filter configuration

#### Models
- Auto-generated Pydantic v2 model classes for all API request and response types

#### Raw Responses
- Endpoints without a defined return type return `ApiResponse` instead of `None`, providing access to status code, headers, and raw response body

#### Documentation
- `README.md` — SDK overview, quick start, features, project structure, development setup
- `GETTING_STARTED.md` — installation, authentication setup, first API call, configuration options
- `AUTHENTICATION.md` — API key, OAuth 2.0, automatic token refresh, token storage callback, security best practices
- `docs/` — per-endpoint API reference for all generated API classes
- `examples/` — runnable examples:
  - `01_first_api_call.py` — API key authentication and basic API calls
  - `02_oauth_with_auto_refresh.py` — OAuth with automatic token refresh and persistent storage
  - `03_oauth_complete_flow.py` — full OAuth 2.0 authorization code flow
  - `04_error_handling.py` — exception types, retry configuration, error catalog
  - `05_common_api_patterns.py` — CRUD patterns across multiple APIs
  - `06_complete_application.py` — production-style application structure
  - `07_testing_patterns.py` — patterns for unit-testing code that uses the SDK
