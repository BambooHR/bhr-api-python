# BambooHR Python SDK

Official Python SDK for the [BambooHR API](https://documentation.bamboohr.com).

## Overview

The BambooHR Python SDK provides a type-safe, Pythonic interface to the BambooHR REST API. It includes auto-generated client classes covering all public API endpoints, a fluent builder for authentication and configuration, and production-ready features such as automatic token refresh, retry with exponential backoff, and secure logging.

## Requirements

- Python 3.10+

## Installation

```bash
pip install bamboohr-sdk
```

## Quick Start

```python
from bamboohr_sdk.client import BambooHRClient
from bamboohr_sdk.exceptions import ApiException

client = (
    BambooHRClient()
    .with_oauth("your-access-token")
    .for_company("your-company-subdomain")
    .build()
)

try:
    directory = client.employees().get_employees_directory()
    for emp in directory.employees or []:
        print(emp.get("displayName"))
except ApiException as e:
    print(f"API error ({e.status}): {e.reason}")
```

See [GETTING_STARTED.md](GETTING_STARTED.md) for a full walkthrough and [AUTHENTICATION.md](AUTHENTICATION.md) for all authentication options. **OAuth 2.0 is recommended for all partner integrations** — see the authentication guide for setup.

## Documentation

- [Getting Started Guide](GETTING_STARTED.md) — installation, first API call, configuration options
- [Authentication Guide](AUTHENTICATION.md) — OAuth 2.0 (recommended), API key, automatic token refresh
- [API Reference](docs/) — per-endpoint documentation for all API classes
- [Examples](examples/) — runnable examples covering common patterns
- [BambooHR API Docs](https://documentation.bamboohr.com/docs/getting-started)
- [Changelog](CHANGELOG.md)

## SDK Features

### Retry with Exponential Backoff

All API requests are automatically retried on transient failures (HTTP 408, 429, 504, 598). Configure via `BambooHRClient`:

```python
client = (
    BambooHRClient()
    .with_oauth("your-access-token")
    .for_company("your-company")
    .with_retries(3)  # 0–5, default 1
    .build()
)
```

### HTTPS Enforcement

All host URLs are automatically upgraded to HTTPS. Setting `host="http://..."` or `host="example.com"` will both resolve to `https://...`.

### Custom User-Agent

All requests include the header `User-Agent: BHR-SDK/{version}/Python`.

### Request ID Support

Exceptions automatically extract the request ID from response headers (`x-request-id`, `x-bamboohr-request-id`, or `request-id`) for easier debugging:

```python
try:
    api.some_endpoint()
except ApiException as e:
    print(e.request_id)  # Extracted from response headers
```

### Secure Logging

The SDK uses Python's `logging` module under the `bamboohr_sdk` logger name. Sensitive headers (Authorization, API keys, cookies) and URL query parameters are automatically redacted in log output.

```python
import logging
logging.getLogger("bamboohr_sdk").setLevel(logging.DEBUG)
```

### Raw Response for Void Endpoints

Endpoints without a defined return type return an `ApiResponse` object instead of `None`, giving access to status code, headers, and raw response data.

## API Endpoints

All URIs are relative to *https://companySubDomain.bamboohr.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountInformationApi* | [**baa7162824294d030115568d1d8e6ca7**](docs/AccountInformationApi.md#baa7162824294d030115568d1d8e6ca7) | **GET** /api/v1/meta/timezones/{id} | Get timezone by ID
*AccountInformationApi* | [**call_10d66d8561dd7dac50ff9c21ef63d83b**](docs/AccountInformationApi.md#call_10d66d8561dd7dac50ff9c21ef63d83b) | **GET** /api/v1/meta/timezones/by-zip/{zip} | Get timezone by ZIP code
*AccountInformationApi* | [**call_5c5fb0f1211ae1c9451753f92f1053b6**](docs/AccountInformationApi.md#call_5c5fb0f1211ae1c9451753f92f1053b6) | **GET** /api/v1/meta/timezones | List timezones
*AccountInformationApi* | [**get_all_currency_types**](docs/AccountInformationApi.md#get_all_currency_types) | **GET** /api/v1/meta/currency/types | Get all currency types
*AccountInformationApi* | [**get_all_provinces**](docs/AccountInformationApi.md#get_all_provinces) | **GET** /api/v1/meta/provinces | Get All Provinces
*AccountInformationApi* | [**get_countries_options**](docs/AccountInformationApi.md#get_countries_options) | **GET** /api/v1/meta/countries/options | Get Countries
*AccountInformationApi* | [**get_meta_company**](docs/AccountInformationApi.md#get_meta_company) | **GET** /api/v1/meta/company | Get company properties
*AccountInformationApi* | [**get_states_by_country_id**](docs/AccountInformationApi.md#get_states_by_country_id) | **GET** /api/v1/meta/provinces/{countryId} | List states and provinces for a country by Country ID
*AccountInformationApi* | [**list_fields**](docs/AccountInformationApi.md#list_fields) | **GET** /api/v1/meta/fields | List Fields
*AccountInformationApi* | [**list_list_fields**](docs/AccountInformationApi.md#list_list_fields) | **GET** /api/v1/meta/lists | List List Fields
*AccountInformationApi* | [**list_tabular_fields**](docs/AccountInformationApi.md#list_tabular_fields) | **GET** /api/v1/meta/tables | List Tabular Fields
*AccountInformationApi* | [**list_users**](docs/AccountInformationApi.md#list_users) | **GET** /api/v1/meta/users | List Users
*AccountInformationApi* | [**update_list_field_values**](docs/AccountInformationApi.md#update_list_field_values) | **PUT** /api/v1/meta/lists/{listFieldId} | Update List Field Values
*AlertApi* | [**call_0f0dcb585e5883175b6557c16cf6755a**](docs/AlertApi.md#call_0f0dcb585e5883175b6557c16cf6755a) | **GET** /api/v1/alerts | List alert templates
*AlertConfigurationsApi* | [**a05e93bc2eb9c39a40fbd71e6e07f3c6**](docs/AlertConfigurationsApi.md#a05e93bc2eb9c39a40fbd71e6e07f3c6) | **POST** /api/v1/alert-configurations | Create an alert configuration
*AlertConfigurationsApi* | [**call_14e66bfb5f075043221ce1e843c97493**](docs/AlertConfigurationsApi.md#call_14e66bfb5f075043221ce1e843c97493) | **GET** /api/v1/alert-configurations/{id} | Get an alert configuration
*AlertConfigurationsApi* | [**call_6d0a073cbf3e97fe0409de42c68fe779**](docs/AlertConfigurationsApi.md#call_6d0a073cbf3e97fe0409de42c68fe779) | **GET** /api/v1/alert-configurations | List alert configurations
*AlertConfigurationsApi* | [**eb42aa2fa339ba5c08b147fc13c6a79e**](docs/AlertConfigurationsApi.md#eb42aa2fa339ba5c08b147fc13c6a79e) | **PUT** /api/v1/alert-configurations/{id} | Update an alert configuration
*ApplicantTrackingApi* | [**create_application_comment**](docs/ApplicantTrackingApi.md#create_application_comment) | **POST** /api/v1/applicant_tracking/applications/{applicationId}/comments | Create Job Application Comment
*ApplicantTrackingApi* | [**create_candidate**](docs/ApplicantTrackingApi.md#create_candidate) | **POST** /api/v1/applicant_tracking/application | Create Candidate
*ApplicantTrackingApi* | [**create_job_opening**](docs/ApplicantTrackingApi.md#create_job_opening) | **POST** /api/v1/applicant_tracking/job_opening | Create Job Opening
*ApplicantTrackingApi* | [**get_application_details**](docs/ApplicantTrackingApi.md#get_application_details) | **GET** /api/v1/applicant_tracking/applications/{applicationId} | Get Job Application Details
*ApplicantTrackingApi* | [**get_applications**](docs/ApplicantTrackingApi.md#get_applications) | **GET** /api/v1/applicant_tracking/applications | Get Job Applications
*ApplicantTrackingApi* | [**get_company_locations**](docs/ApplicantTrackingApi.md#get_company_locations) | **GET** /api/v1/applicant_tracking/locations | Get Company Locations
*ApplicantTrackingApi* | [**get_hiring_leads**](docs/ApplicantTrackingApi.md#get_hiring_leads) | **GET** /api/v1/applicant_tracking/hiring_leads | Get Hiring Leads
*ApplicantTrackingApi* | [**get_job_summaries**](docs/ApplicantTrackingApi.md#get_job_summaries) | **GET** /api/v1/applicant_tracking/jobs | Get Job Summaries
*ApplicantTrackingApi* | [**get_statuses**](docs/ApplicantTrackingApi.md#get_statuses) | **GET** /api/v1/applicant_tracking/statuses | Get Applicant Statuses
*ApplicantTrackingApi* | [**update_applicant_status**](docs/ApplicantTrackingApi.md#update_applicant_status) | **POST** /api/v1/applicant_tracking/applications/{applicationId}/status | Update Applicant Status
*BenefitsApi* | [**create_employee_dependent**](docs/BenefitsApi.md#create_employee_dependent) | **POST** /api/v1/employeedependents | Create Employee Dependent
*BenefitsApi* | [**get_employee_dependent**](docs/BenefitsApi.md#get_employee_dependent) | **GET** /api/v1/employeedependents/{id} | Get Employee Dependent
*BenefitsApi* | [**list_benefit_coverages**](docs/BenefitsApi.md#list_benefit_coverages) | **GET** /api/v1/benefitcoverages | List Benefit Coverages
*BenefitsApi* | [**list_benefit_deduction_types**](docs/BenefitsApi.md#list_benefit_deduction_types) | **GET** /api/v1/benefits/settings/deduction_types/all | List Benefit Deduction Types
*BenefitsApi* | [**list_company_benefits**](docs/BenefitsApi.md#list_company_benefits) | **GET** /api/v1/benefit/company_benefit | List Company Benefits
*BenefitsApi* | [**list_employee_benefits**](docs/BenefitsApi.md#list_employee_benefits) | **GET** /api/v1/benefit/employee_benefit | List Employee Benefits
*BenefitsApi* | [**list_employee_dependents**](docs/BenefitsApi.md#list_employee_dependents) | **GET** /api/v1/employeedependents | List Employee Dependents
*BenefitsApi* | [**list_member_benefit_events**](docs/BenefitsApi.md#list_member_benefit_events) | **GET** /api/v1/benefit/member_benefit | List Member Benefit Events
*BenefitsApi* | [**list_member_benefits**](docs/BenefitsApi.md#list_member_benefits) | **GET** /api/v1/benefits/member-benefits | List Member Benefits
*BenefitsApi* | [**update_employee_dependent**](docs/BenefitsApi.md#update_employee_dependent) | **PUT** /api/v1/employeedependents/{id} | Update Employee Dependent
*CompanyApi* | [**put_company_industry_codes**](docs/CompanyApi.md#put_company_industry_codes) | **PUT** /api/v1/company-profile-data/industry-codes | Update Company Industry Codes
*CompanyFilesApi* | [**create_company_file_category**](docs/CompanyFilesApi.md#create_company_file_category) | **POST** /api/v1/files/categories | Create Company File Category
*CompanyFilesApi* | [**delete_company_file**](docs/CompanyFilesApi.md#delete_company_file) | **DELETE** /api/v1/files/{fileId} | Delete Company File
*CompanyFilesApi* | [**get_company_file**](docs/CompanyFilesApi.md#get_company_file) | **GET** /api/v1/files/{fileId} | Get Company File
*CompanyFilesApi* | [**list_company_files**](docs/CompanyFilesApi.md#list_company_files) | **GET** /api/v1/files/view | Get Company Files and Categories
*CompanyFilesApi* | [**update_company_file**](docs/CompanyFilesApi.md#update_company_file) | **POST** /api/v1/files/{fileId} | Update Company File
*CompanyFilesApi* | [**upload_company_file**](docs/CompanyFilesApi.md#upload_company_file) | **POST** /api/v1/files | Upload Company File
*CompanyProfileApi* | [**get_company_profile_integrations**](docs/CompanyProfileApi.md#get_company_profile_integrations) | **GET** /api/v1/company-profile-integrations | Get Company Profile Integrations
*CompanyProfileApi* | [**patch_company_profile_company_information**](docs/CompanyProfileApi.md#patch_company_profile_company_information) | **PATCH** /api/v1/company-profile-data/company-information | Update company information (phone, address, legal name)
*CompanyProfileApi* | [**put_company_profile_display_name**](docs/CompanyProfileApi.md#put_company_profile_display_name) | **PUT** /api/v1/company-profile-data/display-name | Update company display name
*CompensationApi* | [**c5880b509783cd9d7fce9ddf5d6af1be**](docs/CompensationApi.md#c5880b509783cd9d7fce9ddf5d6af1be) | **PUT** /api/v1/compensation/equity/settings | Update company equity settings
*CompensationApi* | [**call_9f398e2652ea47a6dc5121ce5184222a**](docs/CompensationApi.md#call_9f398e2652ea47a6dc5121ce5184222a) | **GET** /api/v1/compensation/tools | List available compensation tools
*CompensationApi* | [**db49fb29f9f04d59afad7c01ce860418**](docs/CompensationApi.md#db49fb29f9f04d59afad7c01ce860418) | **GET** /api/v1/compensation/equity/settings | Get company equity settings
*CompensationBenchmarkingApi* | [**create_compensation_benchmark**](docs/CompensationBenchmarkingApi.md#create_compensation_benchmark) | **POST** /api/v1/compensation/benchmarks | Create Compensation Benchmark
*CompensationBenchmarkingApi* | [**create_compensation_benchmark_source**](docs/CompensationBenchmarkingApi.md#create_compensation_benchmark_source) | **POST** /api/v1/compensation/benchmarks/sources | Create Compensation Benchmark Source
*CompensationBenchmarkingApi* | [**delete_compensation_benchmark**](docs/CompensationBenchmarkingApi.md#delete_compensation_benchmark) | **DELETE** /api/v1/compensation/benchmarks/{id} | Delete Compensation Benchmark
*CompensationBenchmarkingApi* | [**delete_compensation_benchmark_source**](docs/CompensationBenchmarkingApi.md#delete_compensation_benchmark_source) | **DELETE** /api/v1/compensation/benchmarks/sources | Delete Compensation Benchmark Source
*CompensationBenchmarkingApi* | [**export_compensation_benchmark_details**](docs/CompensationBenchmarkingApi.md#export_compensation_benchmark_details) | **GET** /api/v1/compensation/benchmarks/details/export | Export Compensation Benchmark Details
*CompensationBenchmarkingApi* | [**get_compensation_benchmark_details**](docs/CompensationBenchmarkingApi.md#get_compensation_benchmark_details) | **GET** /api/v1/compensation/benchmarks/details | Get Compensation Benchmark Details
*CompensationBenchmarkingApi* | [**import_compensation_benchmarks**](docs/CompensationBenchmarkingApi.md#import_compensation_benchmarks) | **POST** /api/v1/compensation/benchmarks/import | Import Compensation Benchmarks From CSV
*CompensationBenchmarkingApi* | [**list_compensation_benchmark_sources**](docs/CompensationBenchmarkingApi.md#list_compensation_benchmark_sources) | **GET** /api/v1/compensation/benchmarks/sources | List Compensation Benchmark Sources
*CompensationBenchmarkingApi* | [**list_compensation_benchmarks**](docs/CompensationBenchmarkingApi.md#list_compensation_benchmarks) | **GET** /api/v1/compensation/benchmarks | List Compensation Benchmarks
*CompensationBenchmarkingApi* | [**update_compensation_benchmark**](docs/CompensationBenchmarkingApi.md#update_compensation_benchmark) | **PUT** /api/v1/compensation/benchmarks | Update Compensation Benchmark
*CompensationBenchmarkingApi* | [**update_compensation_benchmark_sources**](docs/CompensationBenchmarkingApi.md#update_compensation_benchmark_sources) | **PUT** /api/v1/compensation/benchmarks/sources | Update Compensation Benchmark Sources
*CompensationPlanningApi* | [**a05b6d5f564f805d688ff2c1e37c3990**](docs/CompensationPlanningApi.md#a05b6d5f564f805d688ff2c1e37c3990) | **POST** /api/v1/compensation/planning_cycles/{id}/recommendations/send | Send recommendations to next stage
*CompensationPlanningApi* | [**a6b8da1348a3151fe95adc03aaf64447**](docs/CompensationPlanningApi.md#a6b8da1348a3151fe95adc03aaf64447) | **GET** /api/v1/compensation/planning_cycles/{id}/employees | List employees in compensation planning cycle
*CompensationPlanningApi* | [**b1e467e0eef72350eec61fcfeaf4e19d**](docs/CompensationPlanningApi.md#b1e467e0eef72350eec61fcfeaf4e19d) | **DELETE** /api/v1/compensation/planning_cycles/{id}/approvals/employee/{employeeId} | Remove from approval flow
*CompensationPlanningApi* | [**b3c51254de6918637a971fe4af382a53**](docs/CompensationPlanningApi.md#b3c51254de6918637a971fe4af382a53) | **GET** /api/v1/compensation/planning_cycles/{id}/admins | List compensation planning cycle admins
*CompensationPlanningApi* | [**b65f246186b41a9783a9397c11c703b4**](docs/CompensationPlanningApi.md#b65f246186b41a9783a9397c11c703b4) | **GET** /api/v1/compensation/planning_cycles | List compensation planning cycles
*CompensationPlanningApi* | [**c79f9c5950f983e59d2626faa30c00a1**](docs/CompensationPlanningApi.md#c79f9c5950f983e59d2626faa30c00a1) | **PUT** /api/v1/compensation/planning_cycles/{id}/change_comm/template | Save change comm template
*CompensationPlanningApi* | [**c7c32ed5278ac67e2e518bf7484a75dc**](docs/CompensationPlanningApi.md#c7c32ed5278ac67e2e518bf7484a75dc) | **POST** /api/v1/compensation/planning_cycles/{id}/admins | Add cycle admins
*CompensationPlanningApi* | [**call_100b0cf8c5207b35697ff10370fd5fe1**](docs/CompensationPlanningApi.md#call_100b0cf8c5207b35697ff10370fd5fe1) | **PUT** /api/v1/compensation/planning_cycles/{id} | Update compensation planning cycle
*CompensationPlanningApi* | [**call_1d1fc0f164cb51973a0206b8e2fb2d2d**](docs/CompensationPlanningApi.md#call_1d1fc0f164cb51973a0206b8e2fb2d2d) | **POST** /api/v1/compensation/planning_cycles/{id}/budgets/import | Import budget breakdown
*CompensationPlanningApi* | [**call_1d64402ee192568adbd5e3179a91e6e2**](docs/CompensationPlanningApi.md#call_1d64402ee192568adbd5e3179a91e6e2) | **PUT** /api/v1/compensation/planning_cycles/{id}/budgets/breakdown | Save budget breakdown
*CompensationPlanningApi* | [**call_22ad75be25455279e2987c80851af5fc**](docs/CompensationPlanningApi.md#call_22ad75be25455279e2987c80851af5fc) | **DELETE** /api/v1/compensation/planning_cycles/{id} | Delete compensation planning cycle
*CompensationPlanningApi* | [**call_329acecaa6df729733d0752aa9f6b204**](docs/CompensationPlanningApi.md#call_329acecaa6df729733d0752aa9f6b204) | **GET** /api/v1/compensation/planning_cycles/{id}/worksheet | Get compensation planning cycle worksheet
*CompensationPlanningApi* | [**call_3958585c861325ea7a2cd30a8c74f042**](docs/CompensationPlanningApi.md#call_3958585c861325ea7a2cd30a8c74f042) | **POST** /api/v1/compensation/planning_cycles/{id}/employees | Add employees to cycle
*CompensationPlanningApi* | [**call_3a19f07aa737dc826ba43b9a1c1cd257**](docs/CompensationPlanningApi.md#call_3a19f07aa737dc826ba43b9a1c1cd257) | **PUT** /api/v1/compensation/planning_cycles/{id}/launch | Launch compensation planning cycle
*CompensationPlanningApi* | [**call_4e886b18264480611f380805301c49c4**](docs/CompensationPlanningApi.md#call_4e886b18264480611f380805301c49c4) | **GET** /api/v1/compensation/planning_cycles/{id}/approvals | Get compensation planning approval flows
*CompensationPlanningApi* | [**call_593d5bff120edf2a218a92022a682728**](docs/CompensationPlanningApi.md#call_593d5bff120edf2a218a92022a682728) | **GET** /api/v1/compensation/planning_cycles/{id}/worksheet/export | Export compensation planning cycle worksheet to CSV
*CompensationPlanningApi* | [**call_5c2b55158b0950b1e9211655666645b6**](docs/CompensationPlanningApi.md#call_5c2b55158b0950b1e9211655666645b6) | **GET** /api/v1/compensation/planning_cycles/{id} | Get compensation planning cycle details
*CompensationPlanningApi* | [**call_5c4aab35a34f5760ec044104b5232bf5**](docs/CompensationPlanningApi.md#call_5c4aab35a34f5760ec044104b5232bf5) | **POST** /api/v1/compensation/planning_cycles/{id}/approvals/final_approver/{employeeId} | Set final approver
*CompensationPlanningApi* | [**call_7efceaee2c010f88244dd01ee81e6e7b**](docs/CompensationPlanningApi.md#call_7efceaee2c010f88244dd01ee81e6e7b) | **GET** /api/v1/compensation/planning_cycles/{id}/budgets | Get compensation planning cycle budgets
*CompensationPlanningApi* | [**call_89a5068111ec499135c7d6e9a53d5a30**](docs/CompensationPlanningApi.md#call_89a5068111ec499135c7d6e9a53d5a30) | **DELETE** /api/v1/compensation/planning_cycles/{id}/employees | Remove employees from cycle
*CompensationPlanningApi* | [**call_9bc279d788f6e86b4cd8b2e0d3de91b1**](docs/CompensationPlanningApi.md#call_9bc279d788f6e86b4cd8b2e0d3de91b1) | **GET** /api/v1/compensation/planning_cycles/{id}/summary | Get compensation planning cycle summary
*CompensationPlanningApi* | [**cf87b8e09a001b6fb81dfce6c20ab9e3**](docs/CompensationPlanningApi.md#cf87b8e09a001b6fb81dfce6c20ab9e3) | **PUT** /api/v1/compensation/planning_cycles/{id}/approvals/{templateId} | Update approval flow
*CompensationPlanningApi* | [**d6987e300672a00c7cfe59afebb64156**](docs/CompensationPlanningApi.md#d6987e300672a00c7cfe59afebb64156) | **GET** /api/v1/compensation/planning_cycles/{id}/change_comm | Get change communication letter details
*CompensationPlanningApi* | [**dacd313af2106213fc4696175941ce65**](docs/CompensationPlanningApi.md#dacd313af2106213fc4696175941ce65) | **PUT** /api/v1/compensation/planning_cycles/{id}/budgets/guidelines | Save budget guidelines
*CompensationPlanningApi* | [**e2ac4e1535f296cb8901f209e04caa83**](docs/CompensationPlanningApi.md#e2ac4e1535f296cb8901f209e04caa83) | **POST** /api/v1/compensation/planning_cycles | Create compensation planning cycle
*CompensationPlanningApi* | [**ef7619b0ee4c8dc079aaea870cfbe81b**](docs/CompensationPlanningApi.md#ef7619b0ee4c8dc079aaea870cfbe81b) | **DELETE** /api/v1/compensation/planning_cycles/{id}/admins/{employeeId} | Remove cycle admin
*CompensationPlanningApi* | [**f3883a522dadbe9e11b34f8b656e3adb**](docs/CompensationPlanningApi.md#f3883a522dadbe9e11b34f8b656e3adb) | **POST** /api/v1/compensation/planning_cycles/{id}/recommendations | Save recommendations
*CompensationPlanningApi* | [**f4b431363af6573af46750f32632e88b**](docs/CompensationPlanningApi.md#f4b431363af6573af46750f32632e88b) | **PUT** /api/v1/compensation/planning_cycles/{id}/complete | Complete compensation planning cycle
*CustomReportsApi* | [**get_report_by_id**](docs/CustomReportsApi.md#get_report_by_id) | **GET** /api/v1/custom-reports/{reportId} | Get Report by ID
*CustomReportsApi* | [**list_reports**](docs/CustomReportsApi.md#list_reports) | **GET** /api/v1/custom-reports | List Reports
*DatasetsApi* | [**get_data_from_dataset_v1**](docs/DatasetsApi.md#get_data_from_dataset_v1) | **POST** /api/v1/datasets/{datasetName} | Get Data from Dataset (v1)
*DatasetsApi* | [**get_data_from_dataset_v2**](docs/DatasetsApi.md#get_data_from_dataset_v2) | **POST** /api/v2/datasets/{datasetName}/data | Get Data from Dataset (v2)
*DatasetsApi* | [**get_field_options_v1**](docs/DatasetsApi.md#get_field_options_v1) | **POST** /api/v1/datasets/{datasetName}/field-options | Get Field Options (v1)
*DatasetsApi* | [**get_field_options_v12**](docs/DatasetsApi.md#get_field_options_v12) | **POST** /api/v1_2/datasets/{datasetName}/field-options | Get Field Options (v1.2)
*DatasetsApi* | [**get_fields_from_dataset_v1**](docs/DatasetsApi.md#get_fields_from_dataset_v1) | **GET** /api/v1/datasets/{datasetName}/fields | Get Fields from Dataset (v1)
*DatasetsApi* | [**get_fields_from_dataset_v12**](docs/DatasetsApi.md#get_fields_from_dataset_v12) | **GET** /api/v1_2/datasets/{datasetName}/fields | Get Fields from Dataset (v1.2)
*DatasetsApi* | [**list_datasets_v1**](docs/DatasetsApi.md#list_datasets_v1) | **GET** /api/v1/datasets | List Datasets (v1)
*DatasetsApi* | [**list_datasets_v12**](docs/DatasetsApi.md#list_datasets_v12) | **GET** /api/v1_2/datasets | List Datasets (v1.2)
*EmployeeVerificationApi* | [**get_employee_verification_integration**](docs/EmployeeVerificationApi.md#get_employee_verification_integration) | **GET** /api/v1/employee-verifications/integration | Get employee verification integration status
*EmployeeVerificationApi* | [**list_employee_verifications_by_employee**](docs/EmployeeVerificationApi.md#list_employee_verifications_by_employee) | **GET** /api/v1/employee-verifications/employees/{employeeId} | List employee verification records for an employee
*EmployeeVerificationApi* | [**send_employee_verification_lifecycle_email_by_user**](docs/EmployeeVerificationApi.md#send_employee_verification_lifecycle_email_by_user) | **POST** /api/v1/employee-verifications/users/{userId}/send-email | Send employee verification lifecycle email by user and email type
*EmployeeVerificationApi* | [**update_employee_verification**](docs/EmployeeVerificationApi.md#update_employee_verification) | **PUT** /api/v1/employee-verifications/employees/{employeeId}/{verificationId} | Update an employee verification record
*EmployeeVerificationApi* | [**update_employee_verification_integration**](docs/EmployeeVerificationApi.md#update_employee_verification_integration) | **PUT** /api/v1/employee-verifications/integration | Enable or disable the employee verification integration
*EmployeeFilesApi* | [**create_employee_file_category**](docs/EmployeeFilesApi.md#create_employee_file_category) | **POST** /api/v1/employees/files/categories | Create Employee File Category
*EmployeeFilesApi* | [**delete_employee_file**](docs/EmployeeFilesApi.md#delete_employee_file) | **DELETE** /api/v1/employees/{id}/files/{fileId} | Delete Employee File
*EmployeeFilesApi* | [**get_employee_file**](docs/EmployeeFilesApi.md#get_employee_file) | **GET** /api/v1/employees/{id}/files/{fileId} | Get Employee File
*EmployeeFilesApi* | [**list_employee_files**](docs/EmployeeFilesApi.md#list_employee_files) | **GET** /api/v1/employees/{id}/files/view | List Employee Files
*EmployeeFilesApi* | [**update_employee_file**](docs/EmployeeFilesApi.md#update_employee_file) | **POST** /api/v1/employees/{id}/files/{fileId} | Update Employee File
*EmployeeFilesApi* | [**upload_employee_file**](docs/EmployeeFilesApi.md#upload_employee_file) | **POST** /api/v1/employees/{id}/files | Upload Employee File
*EmployeesApi* | [**create_employee**](docs/EmployeesApi.md#create_employee) | **POST** /api/v1/employees | Create Employee
*EmployeesApi* | [**delete_employee**](docs/EmployeesApi.md#delete_employee) | **DELETE** /api/v1/employees/{id} | Delete employee
*EmployeesApi* | [**get_company_information**](docs/EmployeesApi.md#get_company_information) | **GET** /api/v1/company_information | Get Company Information
*EmployeesApi* | [**get_employee**](docs/EmployeesApi.md#get_employee) | **GET** /api/v1/employees/{id} | Get Employee
*EmployeesApi* | [**get_employees_directory**](docs/EmployeesApi.md#get_employees_directory) | **GET** /api/v1/employees/directory | Get Employees Directory
*EmployeesApi* | [**list_employees**](docs/EmployeesApi.md#list_employees) | **GET** /api/v1/employees | List Employees
*EmployeesApi* | [**update_employee**](docs/EmployeesApi.md#update_employee) | **POST** /api/v1/employees/{id} | Update Employee
*GoalsApi* | [**close_goal**](docs/GoalsApi.md#close_goal) | **POST** /api/v1/performance/employees/{employeeId}/goals/{goalId}/close | Close Goal
*GoalsApi* | [**create_goal**](docs/GoalsApi.md#create_goal) | **POST** /api/v1/performance/employees/{employeeId}/goals | Create Goal
*GoalsApi* | [**create_goal_comment**](docs/GoalsApi.md#create_goal_comment) | **POST** /api/v1/performance/employees/{employeeId}/goals/{goalId}/comments | Create Goal Comment
*GoalsApi* | [**delete_goal**](docs/GoalsApi.md#delete_goal) | **DELETE** /api/v1/performance/employees/{employeeId}/goals/{goalId} | Delete Goal
*GoalsApi* | [**delete_goal_comment**](docs/GoalsApi.md#delete_goal_comment) | **DELETE** /api/v1/performance/employees/{employeeId}/goals/{goalId}/comments/{commentId} | Delete Goal Comment
*GoalsApi* | [**get_alignable_goal_options**](docs/GoalsApi.md#get_alignable_goal_options) | **GET** /api/v1/performance/employees/{employeeId}/goals/alignmentOptions | Get Alignable Goal Options
*GoalsApi* | [**get_goal_aggregate**](docs/GoalsApi.md#get_goal_aggregate) | **GET** /api/v1/performance/employees/{employeeId}/goals/{goalId}/aggregate | Get Goal Aggregate
*GoalsApi* | [**get_goal_creation_permission**](docs/GoalsApi.md#get_goal_creation_permission) | **GET** /api/v1/performance/employees/{employeeId}/goals/canCreateGoals | Get Goal Creation Permission
*GoalsApi* | [**get_goals_aggregate_v1**](docs/GoalsApi.md#get_goals_aggregate_v1) | **GET** /api/v1/performance/employees/{employeeId}/goals/aggregate | Get Goals Aggregate (v1)
*GoalsApi* | [**get_goals_aggregate_v1_1**](docs/GoalsApi.md#get_goals_aggregate_v1_1) | **GET** /api/v1_1/performance/employees/{employeeId}/goals/aggregate | Get Goals Aggregate (v1.1)
*GoalsApi* | [**get_goals_aggregate_v1_2**](docs/GoalsApi.md#get_goals_aggregate_v1_2) | **GET** /api/v1_2/performance/employees/{employeeId}/goals/aggregate | Get Goals Aggregate (v1.2)
*GoalsApi* | [**get_goals_filters_v1**](docs/GoalsApi.md#get_goals_filters_v1) | **GET** /api/v1/performance/employees/{employeeId}/goals/filters | Get Goal Filters (v1)
*GoalsApi* | [**get_goals_filters_v1_1**](docs/GoalsApi.md#get_goals_filters_v1_1) | **GET** /api/v1_1/performance/employees/{employeeId}/goals/filters | Get Goal Filters (v1.1)
*GoalsApi* | [**get_goals_filters_v1_2**](docs/GoalsApi.md#get_goals_filters_v1_2) | **GET** /api/v1_2/performance/employees/{employeeId}/goals/filters | Get Goal Filters (v1.2)
*GoalsApi* | [**list_goal_comments**](docs/GoalsApi.md#list_goal_comments) | **GET** /api/v1/performance/employees/{employeeId}/goals/{goalId}/comments | List Goal Comments
*GoalsApi* | [**list_goal_share_options**](docs/GoalsApi.md#list_goal_share_options) | **GET** /api/v1/performance/employees/{employeeId}/goals/shareOptions | List Goal Sharing Options
*GoalsApi* | [**list_goals**](docs/GoalsApi.md#list_goals) | **GET** /api/v1/performance/employees/{employeeId}/goals | List Goals
*GoalsApi* | [**reopen_goal**](docs/GoalsApi.md#reopen_goal) | **POST** /api/v1/performance/employees/{employeeId}/goals/{goalId}/reopen | Reopen Goal
*GoalsApi* | [**update_goal_comment**](docs/GoalsApi.md#update_goal_comment) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId}/comments/{commentId} | Update Goal Comment
*GoalsApi* | [**update_goal_milestone_progress**](docs/GoalsApi.md#update_goal_milestone_progress) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId}/milestones/{milestoneId}/progress | Update Milestone Progress
*GoalsApi* | [**update_goal_progress**](docs/GoalsApi.md#update_goal_progress) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId}/progress | Update Goal Progress
*GoalsApi* | [**update_goal_sharing**](docs/GoalsApi.md#update_goal_sharing) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId}/sharedWith | Update Goal Sharing
*GoalsApi* | [**update_goal_v1**](docs/GoalsApi.md#update_goal_v1) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId} | Update Goal (v1)
*GoalsApi* | [**update_goal_v1_1**](docs/GoalsApi.md#update_goal_v1_1) | **PUT** /api/v1_1/performance/employees/{employeeId}/goals/{goalId} | Update Goal (v1.1)
*HoursApi* | [**create_or_update_time_tracking_hour_records**](docs/HoursApi.md#create_or_update_time_tracking_hour_records) | **POST** /api/v1/timetracking/record | Create or Update Hour Records
*HoursApi* | [**create_time_tracking_hour_record**](docs/HoursApi.md#create_time_tracking_hour_record) | **POST** /api/v1/timetracking/add | Create Hour Record
*HoursApi* | [**delete_time_tracking_hour_record**](docs/HoursApi.md#delete_time_tracking_hour_record) | **DELETE** /api/v1/timetracking/delete/{id} | Delete Hour Record
*HoursApi* | [**get_time_tracking_record**](docs/HoursApi.md#get_time_tracking_record) | **GET** /api/v1/timetracking/record/{id} | Get Time Tracking Record
*HoursApi* | [**update_time_tracking_record**](docs/HoursApi.md#update_time_tracking_record) | **PUT** /api/v1/timetracking/adjust | Update Hour Record
*LastChangeInformationApi* | [**get_changed_employee_ids**](docs/LastChangeInformationApi.md#get_changed_employee_ids) | **GET** /api/v1/employees/changed | Get Changed Employee IDs
*LocationsApi* | [**create_location**](docs/LocationsApi.md#create_location) | **POST** /api/v1/hris/org/locations | Create a job location
*LocationsApi* | [**delete_location**](docs/LocationsApi.md#delete_location) | **DELETE** /api/v1/hris/org/locations/{id} | Delete a job location
*LocationsApi* | [**get_location**](docs/LocationsApi.md#get_location) | **GET** /api/v1/hris/org/locations/{id} | Get a job location
*LocationsApi* | [**get_locations**](docs/LocationsApi.md#get_locations) | **GET** /api/v1/hris/org/locations | List job locations
*LocationsApi* | [**update_location**](docs/LocationsApi.md#update_location) | **PUT** /api/v1/hris/org/locations/{id} | Update a job location
*LoginApi* | [**login**](docs/LoginApi.md#login) | **POST** /api/v1/login | Login
*OnboardingApi* | [**caa7fc488bcfaef14125398f2ebb987d**](docs/OnboardingApi.md#caa7fc488bcfaef14125398f2ebb987d) | **DELETE** /api/v1/new-hire-packets/{id} | Delete new hire packet
*OnboardingApi* | [**call_0158de7cde2a4c4cf577f0b25070d809**](docs/OnboardingApi.md#call_0158de7cde2a4c4cf577f0b25070d809) | **GET** /api/v1/employees/{employeeId}/onboarding-experiences | List employee onboarding experiences
*OnboardingApi* | [**call_044949386f2d655c6a627ef53f9434b7**](docs/OnboardingApi.md#call_044949386f2d655c6a627ef53f9434b7) | **GET** /api/v1/onboarding/new-hire-widget | Get welcome new hires widget
*OnboardingApi* | [**call_19c7e26a1347ae7eb22919e9b0595c19**](docs/OnboardingApi.md#call_19c7e26a1347ae7eb22919e9b0595c19) | **POST** /api/v1/new-hire-packets/{id}/cancel | Cancel new hire packet
*OnboardingApi* | [**call_1ab0279d46023eb951a434f24df885f1**](docs/OnboardingApi.md#call_1ab0279d46023eb951a434f24df885f1) | **PUT** /api/v1/new-hire-packets/{id} | Update new hire packet
*OnboardingApi* | [**call_288aa996aba16d7a495c62321ea999a9**](docs/OnboardingApi.md#call_288aa996aba16d7a495c62321ea999a9) | **POST** /api/v1/employees/{employeeId}/onboarding-experiences | Create employee onboarding experience
*OnboardingApi* | [**call_696f0a229cdde60b733568e3c4d043d9**](docs/OnboardingApi.md#call_696f0a229cdde60b733568e3c4d043d9) | **GET** /api/v1/new-hire-packets/{id} | Get new hire packet by id
*OnboardingApi* | [**call_847dd061d1d1859e7ce8cb3adfc9faf2**](docs/OnboardingApi.md#call_847dd061d1d1859e7ce8cb3adfc9faf2) | **GET** /api/v1/employees/{employeeId}/onboarding-experiences/{onboardingExperienceId} | Get employee onboarding experience by id
*OnboardingApi* | [**ec1ba8e76f33960b018d0d7518fe97b5**](docs/OnboardingApi.md#ec1ba8e76f33960b018d0d7518fe97b5) | **POST** /api/v1/new-hire-packets | Create new hire packet
*OnboardingApi* | [**f44b802c30cdea2b9076b3f82f99c74d**](docs/OnboardingApi.md#f44b802c30cdea2b9076b3f82f99c74d) | **GET** /api/v1/new-hire-packets | List new hire packets
*OnboardingApi* | [**f49b0f1f2fb1ef2c408ba12916ee9baa**](docs/OnboardingApi.md#f49b0f1f2fb1ef2c408ba12916ee9baa) | **POST** /api/v1/new-hire-packets/{id}/send | Send new hire packet
*OnboardingApi* | [**update_new_hire_packet_gtky_answer_visibility**](docs/OnboardingApi.md#update_new_hire_packet_gtky_answer_visibility) | **PUT** /api/v1/new-hire-packets/{id}/question-visibility | Update GTKY answer visibility for a new hire packet
*PhotosApi* | [**get_employee_photo**](docs/PhotosApi.md#get_employee_photo) | **GET** /api/v1/employees/{employeeId}/photo/{size} | Get Employee Photo
*PhotosApi* | [**upload_employee_photo**](docs/PhotosApi.md#upload_employee_photo) | **POST** /api/v1/employees/{employeeId}/photo | Upload Employee Photo
*PublicAPIApi* | [**a05b6d5f564f805d688ff2c1e37c3990**](docs/PublicAPIApi.md#a05b6d5f564f805d688ff2c1e37c3990) | **POST** /api/v1/compensation/planning_cycles/{id}/recommendations/send | Send recommendations to next stage
*PublicAPIApi* | [**a05e93bc2eb9c39a40fbd71e6e07f3c6**](docs/PublicAPIApi.md#a05e93bc2eb9c39a40fbd71e6e07f3c6) | **POST** /api/v1/alert-configurations | Create an alert configuration
*PublicAPIApi* | [**a6b8da1348a3151fe95adc03aaf64447**](docs/PublicAPIApi.md#a6b8da1348a3151fe95adc03aaf64447) | **GET** /api/v1/compensation/planning_cycles/{id}/employees | List employees in compensation planning cycle
*PublicAPIApi* | [**ad7871529b2a9c6612f8dd3c62192c08**](docs/PublicAPIApi.md#ad7871529b2a9c6612f8dd3c62192c08) | **PUT** /api/v1/pay-grades-and-bands/pay-bands | Update pay bands
*PublicAPIApi* | [**add_total_rewards_employees**](docs/PublicAPIApi.md#add_total_rewards_employees) | **POST** /api/v1/compensation/total_rewards/employees | Add Employees to Total Rewards
*PublicAPIApi* | [**adjust_time_off_balance**](docs/PublicAPIApi.md#adjust_time_off_balance) | **PUT** /api/v1/employees/{employeeId}/time_off/balance_adjustment | Adjust Time Off Balance
*PublicAPIApi* | [**assign_employees_to_break_policy**](docs/PublicAPIApi.md#assign_employees_to_break_policy) | **POST** /api/v1/time-tracking/break-policies/{id}/assign | Assign Employees to Break Policy
*PublicAPIApi* | [**assign_time_off_policies**](docs/PublicAPIApi.md#assign_time_off_policies) | **PUT** /api/v1/employees/{employeeId}/time_off/policies | Assign Time Off Policies
*PublicAPIApi* | [**assign_time_off_policies_v1_1**](docs/PublicAPIApi.md#assign_time_off_policies_v1_1) | **PUT** /api/v1_1/employees/{employeeId}/time_off/policies | Assign Time Off Policies v1.1
*PublicAPIApi* | [**b1e467e0eef72350eec61fcfeaf4e19d**](docs/PublicAPIApi.md#b1e467e0eef72350eec61fcfeaf4e19d) | **DELETE** /api/v1/compensation/planning_cycles/{id}/approvals/employee/{employeeId} | Remove from approval flow
*PublicAPIApi* | [**b3c51254de6918637a971fe4af382a53**](docs/PublicAPIApi.md#b3c51254de6918637a971fe4af382a53) | **GET** /api/v1/compensation/planning_cycles/{id}/admins | List compensation planning cycle admins
*PublicAPIApi* | [**b65f246186b41a9783a9397c11c703b4**](docs/PublicAPIApi.md#b65f246186b41a9783a9397c11c703b4) | **GET** /api/v1/compensation/planning_cycles | List compensation planning cycles
*PublicAPIApi* | [**baa7162824294d030115568d1d8e6ca7**](docs/PublicAPIApi.md#baa7162824294d030115568d1d8e6ca7) | **GET** /api/v1/meta/timezones/{id} | Get timezone by ID
*PublicAPIApi* | [**c5880b509783cd9d7fce9ddf5d6af1be**](docs/PublicAPIApi.md#c5880b509783cd9d7fce9ddf5d6af1be) | **PUT** /api/v1/compensation/equity/settings | Update company equity settings
*PublicAPIApi* | [**c79f9c5950f983e59d2626faa30c00a1**](docs/PublicAPIApi.md#c79f9c5950f983e59d2626faa30c00a1) | **PUT** /api/v1/compensation/planning_cycles/{id}/change_comm/template | Save change comm template
*PublicAPIApi* | [**c7c32ed5278ac67e2e518bf7484a75dc**](docs/PublicAPIApi.md#c7c32ed5278ac67e2e518bf7484a75dc) | **POST** /api/v1/compensation/planning_cycles/{id}/admins | Add cycle admins
*PublicAPIApi* | [**caa7fc488bcfaef14125398f2ebb987d**](docs/PublicAPIApi.md#caa7fc488bcfaef14125398f2ebb987d) | **DELETE** /api/v1/new-hire-packets/{id} | Delete new hire packet
*PublicAPIApi* | [**call_0158de7cde2a4c4cf577f0b25070d809**](docs/PublicAPIApi.md#call_0158de7cde2a4c4cf577f0b25070d809) | **GET** /api/v1/employees/{employeeId}/onboarding-experiences | List employee onboarding experiences
*PublicAPIApi* | [**call_044949386f2d655c6a627ef53f9434b7**](docs/PublicAPIApi.md#call_044949386f2d655c6a627ef53f9434b7) | **GET** /api/v1/onboarding/new-hire-widget | Get welcome new hires widget
*PublicAPIApi* | [**call_0da9c9f851462d2e44dfe866b8e67e74**](docs/PublicAPIApi.md#call_0da9c9f851462d2e44dfe866b8e67e74) | **DELETE** /api/v1/pay-grades-and-bands/levels/{segment} | Delete groups by status or delete one level
*PublicAPIApi* | [**call_0f0dcb585e5883175b6557c16cf6755a**](docs/PublicAPIApi.md#call_0f0dcb585e5883175b6557c16cf6755a) | **GET** /api/v1/alerts | List alert templates
*PublicAPIApi* | [**call_100b0cf8c5207b35697ff10370fd5fe1**](docs/PublicAPIApi.md#call_100b0cf8c5207b35697ff10370fd5fe1) | **PUT** /api/v1/compensation/planning_cycles/{id} | Update compensation planning cycle
*PublicAPIApi* | [**call_10d66d8561dd7dac50ff9c21ef63d83b**](docs/PublicAPIApi.md#call_10d66d8561dd7dac50ff9c21ef63d83b) | **GET** /api/v1/meta/timezones/by-zip/{zip} | Get timezone by ZIP code
*PublicAPIApi* | [**call_12c40475623893cf0434b3ae69e36975**](docs/PublicAPIApi.md#call_12c40475623893cf0434b3ae69e36975) | **GET** /api/v1/pay-grades-and-bands/review | Get levels and bands review data
*PublicAPIApi* | [**call_14e66bfb5f075043221ce1e843c97493**](docs/PublicAPIApi.md#call_14e66bfb5f075043221ce1e843c97493) | **GET** /api/v1/alert-configurations/{id} | Get an alert configuration
*PublicAPIApi* | [**call_19c7e26a1347ae7eb22919e9b0595c19**](docs/PublicAPIApi.md#call_19c7e26a1347ae7eb22919e9b0595c19) | **POST** /api/v1/new-hire-packets/{id}/cancel | Cancel new hire packet
*PublicAPIApi* | [**call_1ab0279d46023eb951a434f24df885f1**](docs/PublicAPIApi.md#call_1ab0279d46023eb951a434f24df885f1) | **PUT** /api/v1/new-hire-packets/{id} | Update new hire packet
*PublicAPIApi* | [**call_1d1fc0f164cb51973a0206b8e2fb2d2d**](docs/PublicAPIApi.md#call_1d1fc0f164cb51973a0206b8e2fb2d2d) | **POST** /api/v1/compensation/planning_cycles/{id}/budgets/import | Import budget breakdown
*PublicAPIApi* | [**call_1d64402ee192568adbd5e3179a91e6e2**](docs/PublicAPIApi.md#call_1d64402ee192568adbd5e3179a91e6e2) | **PUT** /api/v1/compensation/planning_cycles/{id}/budgets/breakdown | Save budget breakdown
*PublicAPIApi* | [**call_22932a81ba129f22114ccdef397af933**](docs/PublicAPIApi.md#call_22932a81ba129f22114ccdef397af933) | **POST** /api/v1/pay-grades-and-bands/publish | Publish draft compensation level groups
*PublicAPIApi* | [**call_22ad75be25455279e2987c80851af5fc**](docs/PublicAPIApi.md#call_22ad75be25455279e2987c80851af5fc) | **DELETE** /api/v1/compensation/planning_cycles/{id} | Delete compensation planning cycle
*PublicAPIApi* | [**call_288aa996aba16d7a495c62321ea999a9**](docs/PublicAPIApi.md#call_288aa996aba16d7a495c62321ea999a9) | **POST** /api/v1/employees/{employeeId}/onboarding-experiences | Create employee onboarding experience
*PublicAPIApi* | [**call_2a0b847ceec3a4f9bfe20cf27e10e81a**](docs/PublicAPIApi.md#call_2a0b847ceec3a4f9bfe20cf27e10e81a) | **PUT** /api/v1/pay-grades-and-bands/job-titles | Update job title level assignments
*PublicAPIApi* | [**call_329acecaa6df729733d0752aa9f6b204**](docs/PublicAPIApi.md#call_329acecaa6df729733d0752aa9f6b204) | **GET** /api/v1/compensation/planning_cycles/{id}/worksheet | Get compensation planning cycle worksheet
*PublicAPIApi* | [**call_3958585c861325ea7a2cd30a8c74f042**](docs/PublicAPIApi.md#call_3958585c861325ea7a2cd30a8c74f042) | **POST** /api/v1/compensation/planning_cycles/{id}/employees | Add employees to cycle
*PublicAPIApi* | [**call_3a19f07aa737dc826ba43b9a1c1cd257**](docs/PublicAPIApi.md#call_3a19f07aa737dc826ba43b9a1c1cd257) | **PUT** /api/v1/compensation/planning_cycles/{id}/launch | Launch compensation planning cycle
*PublicAPIApi* | [**call_3af7d1ac36c35008b8ebb93fecbdb35b**](docs/PublicAPIApi.md#call_3af7d1ac36c35008b8ebb93fecbdb35b) | **GET** /api/v1/pay-grades-and-bands/job-titles-with-employees | List job titles with employees
*PublicAPIApi* | [**call_432e469fe5959a6ccd765d02018e7db4**](docs/PublicAPIApi.md#call_432e469fe5959a6ccd765d02018e7db4) | **PUT** /api/v1/pay-grades-and-bands/levels | Save compensation level groups and levels
*PublicAPIApi* | [**call_4acdbb25aa278f9f94b44b42ef9f1b27**](docs/PublicAPIApi.md#call_4acdbb25aa278f9f94b44b42ef9f1b27) | **GET** /api/v1/pay-grades-and-bands/job-titles | Get job titles and level assignments
*PublicAPIApi* | [**call_4e886b18264480611f380805301c49c4**](docs/PublicAPIApi.md#call_4e886b18264480611f380805301c49c4) | **GET** /api/v1/compensation/planning_cycles/{id}/approvals | Get compensation planning approval flows
*PublicAPIApi* | [**call_593d5bff120edf2a218a92022a682728**](docs/PublicAPIApi.md#call_593d5bff120edf2a218a92022a682728) | **GET** /api/v1/compensation/planning_cycles/{id}/worksheet/export | Export compensation planning cycle worksheet to CSV
*PublicAPIApi* | [**call_5c2b55158b0950b1e9211655666645b6**](docs/PublicAPIApi.md#call_5c2b55158b0950b1e9211655666645b6) | **GET** /api/v1/compensation/planning_cycles/{id} | Get compensation planning cycle details
*PublicAPIApi* | [**call_5c4aab35a34f5760ec044104b5232bf5**](docs/PublicAPIApi.md#call_5c4aab35a34f5760ec044104b5232bf5) | **POST** /api/v1/compensation/planning_cycles/{id}/approvals/final_approver/{employeeId} | Set final approver
*PublicAPIApi* | [**call_5c5fb0f1211ae1c9451753f92f1053b6**](docs/PublicAPIApi.md#call_5c5fb0f1211ae1c9451753f92f1053b6) | **GET** /api/v1/meta/timezones | List timezones
*PublicAPIApi* | [**call_696f0a229cdde60b733568e3c4d043d9**](docs/PublicAPIApi.md#call_696f0a229cdde60b733568e3c4d043d9) | **GET** /api/v1/new-hire-packets/{id} | Get new hire packet by id
*PublicAPIApi* | [**call_6d0a073cbf3e97fe0409de42c68fe779**](docs/PublicAPIApi.md#call_6d0a073cbf3e97fe0409de42c68fe779) | **GET** /api/v1/alert-configurations | List alert configurations
*PublicAPIApi* | [**call_6fbb2fe60e374d2204f1222252105945**](docs/PublicAPIApi.md#call_6fbb2fe60e374d2204f1222252105945) | **GET** /api/v1/pay-grades-and-bands/status | Get levels and bands status
*PublicAPIApi* | [**call_7efceaee2c010f88244dd01ee81e6e7b**](docs/PublicAPIApi.md#call_7efceaee2c010f88244dd01ee81e6e7b) | **GET** /api/v1/compensation/planning_cycles/{id}/budgets | Get compensation planning cycle budgets
*PublicAPIApi* | [**call_847dd061d1d1859e7ce8cb3adfc9faf2**](docs/PublicAPIApi.md#call_847dd061d1d1859e7ce8cb3adfc9faf2) | **GET** /api/v1/employees/{employeeId}/onboarding-experiences/{onboardingExperienceId} | Get employee onboarding experience by id
*PublicAPIApi* | [**call_89a5068111ec499135c7d6e9a53d5a30**](docs/PublicAPIApi.md#call_89a5068111ec499135c7d6e9a53d5a30) | **DELETE** /api/v1/compensation/planning_cycles/{id}/employees | Remove employees from cycle
*PublicAPIApi* | [**call_99b887959832c80eead3a176acc0c2d4**](docs/PublicAPIApi.md#call_99b887959832c80eead3a176acc0c2d4) | **GET** /api/v1/pay-grades-and-bands/status-counts | Get compensation level group status counts
*PublicAPIApi* | [**call_9bc279d788f6e86b4cd8b2e0d3de91b1**](docs/PublicAPIApi.md#call_9bc279d788f6e86b4cd8b2e0d3de91b1) | **GET** /api/v1/compensation/planning_cycles/{id}/summary | Get compensation planning cycle summary
*PublicAPIApi* | [**call_9f398e2652ea47a6dc5121ce5184222a**](docs/PublicAPIApi.md#call_9f398e2652ea47a6dc5121ce5184222a) | **GET** /api/v1/compensation/tools | List available compensation tools
*PublicAPIApi* | [**cdd8659ca89fb38042fd56feab507edf**](docs/PublicAPIApi.md#cdd8659ca89fb38042fd56feab507edf) | **POST** /api/v1/pay-grades-and-bands/import | Import levels and bands from CSV
*PublicAPIApi* | [**cf87b8e09a001b6fb81dfce6c20ab9e3**](docs/PublicAPIApi.md#cf87b8e09a001b6fb81dfce6c20ab9e3) | **PUT** /api/v1/compensation/planning_cycles/{id}/approvals/{templateId} | Update approval flow
*PublicAPIApi* | [**cfacff2b34cf1e65ccd1ab188c5e1d12**](docs/PublicAPIApi.md#cfacff2b34cf1e65ccd1ab188c5e1d12) | **GET** /api/v1/pay-grades-and-bands | Get published levels and bands
*PublicAPIApi* | [**check_total_rewards_profile**](docs/PublicAPIApi.md#check_total_rewards_profile) | **GET** /api/v1/compensation/total_rewards/{employeeId} | Check Total Rewards Profile Availability
*PublicAPIApi* | [**close_goal**](docs/PublicAPIApi.md#close_goal) | **POST** /api/v1/performance/employees/{employeeId}/goals/{goalId}/close | Close Goal
*PublicAPIApi* | [**create_application_comment**](docs/PublicAPIApi.md#create_application_comment) | **POST** /api/v1/applicant_tracking/applications/{applicationId}/comments | Create Job Application Comment
*PublicAPIApi* | [**create_break**](docs/PublicAPIApi.md#create_break) | **POST** /api/v1/time-tracking/break-policies/{id}/breaks | Create Break
*PublicAPIApi* | [**create_break_policy**](docs/PublicAPIApi.md#create_break_policy) | **POST** /api/v1/time-tracking/break-policies | Create Break Policy
*PublicAPIApi* | [**create_candidate**](docs/PublicAPIApi.md#create_candidate) | **POST** /api/v1/applicant_tracking/application | Create Candidate
*PublicAPIApi* | [**create_company_file_category**](docs/PublicAPIApi.md#create_company_file_category) | **POST** /api/v1/files/categories | Create Company File Category
*PublicAPIApi* | [**create_compensation_benchmark**](docs/PublicAPIApi.md#create_compensation_benchmark) | **POST** /api/v1/compensation/benchmarks | Create Compensation Benchmark
*PublicAPIApi* | [**create_compensation_benchmark_source**](docs/PublicAPIApi.md#create_compensation_benchmark_source) | **POST** /api/v1/compensation/benchmarks/sources | Create Compensation Benchmark Source
*PublicAPIApi* | [**create_employee**](docs/PublicAPIApi.md#create_employee) | **POST** /api/v1/employees | Create Employee
*PublicAPIApi* | [**create_employee_dependent**](docs/PublicAPIApi.md#create_employee_dependent) | **POST** /api/v1/employeedependents | Create Employee Dependent
*PublicAPIApi* | [**create_employee_file_category**](docs/PublicAPIApi.md#create_employee_file_category) | **POST** /api/v1/employees/files/categories | Create Employee File Category
*PublicAPIApi* | [**create_employee_training_record**](docs/PublicAPIApi.md#create_employee_training_record) | **POST** /api/v1/training/record/employee/{employeeId} | Create Employee Training Record
*PublicAPIApi* | [**create_goal**](docs/PublicAPIApi.md#create_goal) | **POST** /api/v1/performance/employees/{employeeId}/goals | Create Goal
*PublicAPIApi* | [**create_goal_comment**](docs/PublicAPIApi.md#create_goal_comment) | **POST** /api/v1/performance/employees/{employeeId}/goals/{goalId}/comments | Create Goal Comment
*PublicAPIApi* | [**create_job_opening**](docs/PublicAPIApi.md#create_job_opening) | **POST** /api/v1/applicant_tracking/job_opening | Create Job Opening
*PublicAPIApi* | [**create_location**](docs/PublicAPIApi.md#create_location) | **POST** /api/v1/hris/org/locations | Create a job location
*PublicAPIApi* | [**create_or_update_time_tracking_hour_records**](docs/PublicAPIApi.md#create_or_update_time_tracking_hour_records) | **POST** /api/v1/timetracking/record | Create or Update Hour Records
*PublicAPIApi* | [**create_or_update_timesheet_clock_entries**](docs/PublicAPIApi.md#create_or_update_timesheet_clock_entries) | **POST** /api/v1/time_tracking/clock_entries/store | Create or Update Timesheet Clock Entries
*PublicAPIApi* | [**create_or_update_timesheet_hour_entries**](docs/PublicAPIApi.md#create_or_update_timesheet_hour_entries) | **POST** /api/v1/time_tracking/hour_entries/store | Create or Update Timesheet Hour Entries
*PublicAPIApi* | [**create_project**](docs/PublicAPIApi.md#create_project) | **POST** /api/v1/time-tracking/projects | Create Time Tracking Project
*PublicAPIApi* | [**create_project_task**](docs/PublicAPIApi.md#create_project_task) | **POST** /api/v1/time-tracking/projects/{projectId}/tasks | Create Time Tracking Project Task
*PublicAPIApi* | [**create_table_row**](docs/PublicAPIApi.md#create_table_row) | **POST** /api/v1/employees/{id}/tables/{table} | Create Table Row
*PublicAPIApi* | [**create_table_row_v11**](docs/PublicAPIApi.md#create_table_row_v11) | **POST** /api/v1_1/employees/{id}/tables/{table} | Create Table Row v1.1
*PublicAPIApi* | [**create_time_off_history**](docs/PublicAPIApi.md#create_time_off_history) | **PUT** /api/v1/employees/{employeeId}/time_off/history | Create Time Off History Item
*PublicAPIApi* | [**create_time_off_request**](docs/PublicAPIApi.md#create_time_off_request) | **PUT** /api/v1/employees/{employeeId}/time_off/request | Create Time Off Request
*PublicAPIApi* | [**create_time_tracking_hour_record**](docs/PublicAPIApi.md#create_time_tracking_hour_record) | **POST** /api/v1/timetracking/add | Create Hour Record
*PublicAPIApi* | [**create_time_tracking_project**](docs/PublicAPIApi.md#create_time_tracking_project) | **POST** /api/v1/time_tracking/projects | Create Time Tracking Project
*PublicAPIApi* | [**create_timesheet_clock_in_entry**](docs/PublicAPIApi.md#create_timesheet_clock_in_entry) | **POST** /api/v1/time_tracking/employees/{employeeId}/clock_in | Create Timesheet Clock-In Entry
*PublicAPIApi* | [**create_timesheet_clock_out_entry**](docs/PublicAPIApi.md#create_timesheet_clock_out_entry) | **POST** /api/v1/time_tracking/employees/{employeeId}/clock_out | Create Timesheet Clock-Out Entry
*PublicAPIApi* | [**create_training_category**](docs/PublicAPIApi.md#create_training_category) | **POST** /api/v1/training/category | Create Training Category
*PublicAPIApi* | [**create_training_type**](docs/PublicAPIApi.md#create_training_type) | **POST** /api/v1/training/type | Create Training Type
*PublicAPIApi* | [**create_webhook**](docs/PublicAPIApi.md#create_webhook) | **POST** /api/v1/webhooks | Create Webhook
*PublicAPIApi* | [**d6987e300672a00c7cfe59afebb64156**](docs/PublicAPIApi.md#d6987e300672a00c7cfe59afebb64156) | **GET** /api/v1/compensation/planning_cycles/{id}/change_comm | Get change communication letter details
*PublicAPIApi* | [**dacd313af2106213fc4696175941ce65**](docs/PublicAPIApi.md#dacd313af2106213fc4696175941ce65) | **PUT** /api/v1/compensation/planning_cycles/{id}/budgets/guidelines | Save budget guidelines
*PublicAPIApi* | [**db49fb29f9f04d59afad7c01ce860418**](docs/PublicAPIApi.md#db49fb29f9f04d59afad7c01ce860418) | **GET** /api/v1/compensation/equity/settings | Get company equity settings
*PublicAPIApi* | [**db8c61787c931b69afbf9e501be85256**](docs/PublicAPIApi.md#db8c61787c931b69afbf9e501be85256) | **GET** /api/v1/pay-grades-and-bands/levels | List compensation level groups and levels
*PublicAPIApi* | [**delete_break**](docs/PublicAPIApi.md#delete_break) | **DELETE** /api/v1/time-tracking/breaks/{id} | Delete Break
*PublicAPIApi* | [**delete_break_policy**](docs/PublicAPIApi.md#delete_break_policy) | **DELETE** /api/v1/time-tracking/break-policies/{id} | Delete Break Policy
*PublicAPIApi* | [**delete_company_file**](docs/PublicAPIApi.md#delete_company_file) | **DELETE** /api/v1/files/{fileId} | Delete Company File
*PublicAPIApi* | [**delete_compensation_benchmark**](docs/PublicAPIApi.md#delete_compensation_benchmark) | **DELETE** /api/v1/compensation/benchmarks/{id} | Delete Compensation Benchmark
*PublicAPIApi* | [**delete_compensation_benchmark_source**](docs/PublicAPIApi.md#delete_compensation_benchmark_source) | **DELETE** /api/v1/compensation/benchmarks/sources | Delete Compensation Benchmark Source
*PublicAPIApi* | [**delete_employee**](docs/PublicAPIApi.md#delete_employee) | **DELETE** /api/v1/employees/{id} | Delete employee
*PublicAPIApi* | [**delete_employee_file**](docs/PublicAPIApi.md#delete_employee_file) | **DELETE** /api/v1/employees/{id}/files/{fileId} | Delete Employee File
*PublicAPIApi* | [**delete_employee_table_row**](docs/PublicAPIApi.md#delete_employee_table_row) | **DELETE** /api/v1/employees/{id}/tables/{table}/{rowId} | Delete Employee Table Row
*PublicAPIApi* | [**delete_employee_training_record**](docs/PublicAPIApi.md#delete_employee_training_record) | **DELETE** /api/v1/training/record/{employeeTrainingRecordId} | Delete Employee Training Record
*PublicAPIApi* | [**delete_goal**](docs/PublicAPIApi.md#delete_goal) | **DELETE** /api/v1/performance/employees/{employeeId}/goals/{goalId} | Delete Goal
*PublicAPIApi* | [**delete_goal_comment**](docs/PublicAPIApi.md#delete_goal_comment) | **DELETE** /api/v1/performance/employees/{employeeId}/goals/{goalId}/comments/{commentId} | Delete Goal Comment
*PublicAPIApi* | [**delete_location**](docs/PublicAPIApi.md#delete_location) | **DELETE** /api/v1/hris/org/locations/{id} | Delete a job location
*PublicAPIApi* | [**delete_project**](docs/PublicAPIApi.md#delete_project) | **DELETE** /api/v1/time-tracking/projects/{id} | Delete Time Tracking Project
*PublicAPIApi* | [**delete_task**](docs/PublicAPIApi.md#delete_task) | **DELETE** /api/v1/time-tracking/tasks/{id} | Delete Time Tracking Task
*PublicAPIApi* | [**delete_time_tracking_hour_record**](docs/PublicAPIApi.md#delete_time_tracking_hour_record) | **DELETE** /api/v1/timetracking/delete/{id} | Delete Hour Record
*PublicAPIApi* | [**delete_timesheet_clock_entries_via_post**](docs/PublicAPIApi.md#delete_timesheet_clock_entries_via_post) | **POST** /api/v1/time_tracking/clock_entries/delete | Delete Timesheet Clock Entries
*PublicAPIApi* | [**delete_timesheet_hour_entries_via_post**](docs/PublicAPIApi.md#delete_timesheet_hour_entries_via_post) | **POST** /api/v1/time_tracking/hour_entries/delete | Delete Timesheet Hour Entries
*PublicAPIApi* | [**delete_training_category**](docs/PublicAPIApi.md#delete_training_category) | **DELETE** /api/v1/training/category/{trainingCategoryId} | Delete Training Category
*PublicAPIApi* | [**delete_training_type**](docs/PublicAPIApi.md#delete_training_type) | **DELETE** /api/v1/training/type/{trainingTypeId} | Delete Training Type
*PublicAPIApi* | [**delete_webhook**](docs/PublicAPIApi.md#delete_webhook) | **DELETE** /api/v1/webhooks/{id} | Delete Webhook
*PublicAPIApi* | [**e2ac4e1535f296cb8901f209e04caa83**](docs/PublicAPIApi.md#e2ac4e1535f296cb8901f209e04caa83) | **POST** /api/v1/compensation/planning_cycles | Create compensation planning cycle
*PublicAPIApi* | [**eb42aa2fa339ba5c08b147fc13c6a79e**](docs/PublicAPIApi.md#eb42aa2fa339ba5c08b147fc13c6a79e) | **PUT** /api/v1/alert-configurations/{id} | Update an alert configuration
*PublicAPIApi* | [**ec1ba8e76f33960b018d0d7518fe97b5**](docs/PublicAPIApi.md#ec1ba8e76f33960b018d0d7518fe97b5) | **POST** /api/v1/new-hire-packets | Create new hire packet
*PublicAPIApi* | [**ef7619b0ee4c8dc079aaea870cfbe81b**](docs/PublicAPIApi.md#ef7619b0ee4c8dc079aaea870cfbe81b) | **DELETE** /api/v1/compensation/planning_cycles/{id}/admins/{employeeId} | Remove cycle admin
*PublicAPIApi* | [**export_compensation_benchmark_details**](docs/PublicAPIApi.md#export_compensation_benchmark_details) | **GET** /api/v1/compensation/benchmarks/details/export | Export Compensation Benchmark Details
*PublicAPIApi* | [**f3883a522dadbe9e11b34f8b656e3adb**](docs/PublicAPIApi.md#f3883a522dadbe9e11b34f8b656e3adb) | **POST** /api/v1/compensation/planning_cycles/{id}/recommendations | Save recommendations
*PublicAPIApi* | [**f44b802c30cdea2b9076b3f82f99c74d**](docs/PublicAPIApi.md#f44b802c30cdea2b9076b3f82f99c74d) | **GET** /api/v1/new-hire-packets | List new hire packets
*PublicAPIApi* | [**f49b0f1f2fb1ef2c408ba12916ee9baa**](docs/PublicAPIApi.md#f49b0f1f2fb1ef2c408ba12916ee9baa) | **POST** /api/v1/new-hire-packets/{id}/send | Send new hire packet
*PublicAPIApi* | [**f4b431363af6573af46750f32632e88b**](docs/PublicAPIApi.md#f4b431363af6573af46750f32632e88b) | **PUT** /api/v1/compensation/planning_cycles/{id}/complete | Complete compensation planning cycle
*PublicAPIApi* | [**fb29d4d4790104b6892a4b6d6db67e19**](docs/PublicAPIApi.md#fb29d4d4790104b6892a4b6d6db67e19) | **GET** /api/v1/pay-grades-and-bands/pay-bands | Get pay bands for levels
*PublicAPIApi* | [**get_alignable_goal_options**](docs/PublicAPIApi.md#get_alignable_goal_options) | **GET** /api/v1/performance/employees/{employeeId}/goals/alignmentOptions | Get Alignable Goal Options
*PublicAPIApi* | [**get_all_currency_types**](docs/PublicAPIApi.md#get_all_currency_types) | **GET** /api/v1/meta/currency/types | Get all currency types
*PublicAPIApi* | [**get_all_provinces**](docs/PublicAPIApi.md#get_all_provinces) | **GET** /api/v1/meta/provinces | Get All Provinces
*PublicAPIApi* | [**get_application_details**](docs/PublicAPIApi.md#get_application_details) | **GET** /api/v1/applicant_tracking/applications/{applicationId} | Get Job Application Details
*PublicAPIApi* | [**get_applications**](docs/PublicAPIApi.md#get_applications) | **GET** /api/v1/applicant_tracking/applications | Get Job Applications
*PublicAPIApi* | [**get_bank_holidays**](docs/PublicAPIApi.md#get_bank_holidays) | **GET** /api/v1/meta/bank-holidays | List bank holidays
*PublicAPIApi* | [**get_break**](docs/PublicAPIApi.md#get_break) | **GET** /api/v1/time-tracking/breaks/{id} | Get Break
*PublicAPIApi* | [**get_break_policy**](docs/PublicAPIApi.md#get_break_policy) | **GET** /api/v1/time-tracking/break-policies/{id} | Get Break Policy
*PublicAPIApi* | [**get_break_policy_suggestions**](docs/PublicAPIApi.md#get_break_policy_suggestions) | **POST** /api/v1/time-tracking/break-policies/suggestions | Get Break Policy Suggestions
*PublicAPIApi* | [**get_changed_employee_ids**](docs/PublicAPIApi.md#get_changed_employee_ids) | **GET** /api/v1/employees/changed | Get Changed Employee IDs
*PublicAPIApi* | [**get_changed_employee_table_data**](docs/PublicAPIApi.md#get_changed_employee_table_data) | **GET** /api/v1/employees/changed/tables/{table} | Get Changed Employee Table Data
*PublicAPIApi* | [**get_company_file**](docs/PublicAPIApi.md#get_company_file) | **GET** /api/v1/files/{fileId} | Get Company File
*PublicAPIApi* | [**get_company_information**](docs/PublicAPIApi.md#get_company_information) | **GET** /api/v1/company_information | Get Company Information
*PublicAPIApi* | [**get_company_locations**](docs/PublicAPIApi.md#get_company_locations) | **GET** /api/v1/applicant_tracking/locations | Get Company Locations
*PublicAPIApi* | [**get_company_profile_integrations**](docs/PublicAPIApi.md#get_company_profile_integrations) | **GET** /api/v1/company-profile-integrations | Get Company Profile Integrations
*PublicAPIApi* | [**get_company_report**](docs/PublicAPIApi.md#get_company_report) | **GET** /api/v1/reports/{id} | Get Company Report
*PublicAPIApi* | [**get_compensation_benchmark_details**](docs/PublicAPIApi.md#get_compensation_benchmark_details) | **GET** /api/v1/compensation/benchmarks/details | Get Compensation Benchmark Details
*PublicAPIApi* | [**get_countries_options**](docs/PublicAPIApi.md#get_countries_options) | **GET** /api/v1/meta/countries/options | Get Countries
*PublicAPIApi* | [**get_currency_conversions**](docs/PublicAPIApi.md#get_currency_conversions) | **GET** /api/v1/meta/currency-conversions | Get currency conversion rates
*PublicAPIApi* | [**get_data_from_dataset_v1**](docs/PublicAPIApi.md#get_data_from_dataset_v1) | **POST** /api/v1/datasets/{datasetName} | Get Data from Dataset (v1)
*PublicAPIApi* | [**get_data_from_dataset_v2**](docs/PublicAPIApi.md#get_data_from_dataset_v2) | **POST** /api/v2/datasets/{datasetName}/data | Get Data from Dataset (v2)
*PublicAPIApi* | [**get_employee**](docs/PublicAPIApi.md#get_employee) | **GET** /api/v1/employees/{id} | Get Employee
*PublicAPIApi* | [**get_employee_dependent**](docs/PublicAPIApi.md#get_employee_dependent) | **GET** /api/v1/employeedependents/{id} | Get Employee Dependent
*PublicAPIApi* | [**get_employee_file**](docs/PublicAPIApi.md#get_employee_file) | **GET** /api/v1/employees/{id}/files/{fileId} | Get Employee File
*PublicAPIApi* | [**get_employee_photo**](docs/PublicAPIApi.md#get_employee_photo) | **GET** /api/v1/employees/{employeeId}/photo/{size} | Get Employee Photo
*PublicAPIApi* | [**get_employee_table_data**](docs/PublicAPIApi.md#get_employee_table_data) | **GET** /api/v1/employees/{id}/tables/{table} | Get Employee Table Data
*PublicAPIApi* | [**get_employee_verification_integration**](docs/PublicAPIApi.md#get_employee_verification_integration) | **GET** /api/v1/employee-verifications/integration | Get employee verification integration status
*PublicAPIApi* | [**get_employees_directory**](docs/PublicAPIApi.md#get_employees_directory) | **GET** /api/v1/employees/directory | Get Employees Directory
*PublicAPIApi* | [**get_field_options_v1**](docs/PublicAPIApi.md#get_field_options_v1) | **POST** /api/v1/datasets/{datasetName}/field-options | Get Field Options (v1)
*PublicAPIApi* | [**get_field_options_v12**](docs/PublicAPIApi.md#get_field_options_v12) | **POST** /api/v1_2/datasets/{datasetName}/field-options | Get Field Options (v1.2)
*PublicAPIApi* | [**get_fields_from_dataset_v1**](docs/PublicAPIApi.md#get_fields_from_dataset_v1) | **GET** /api/v1/datasets/{datasetName}/fields | Get Fields from Dataset (v1)
*PublicAPIApi* | [**get_fields_from_dataset_v12**](docs/PublicAPIApi.md#get_fields_from_dataset_v12) | **GET** /api/v1_2/datasets/{datasetName}/fields | Get Fields from Dataset (v1.2)
*PublicAPIApi* | [**get_goal_aggregate**](docs/PublicAPIApi.md#get_goal_aggregate) | **GET** /api/v1/performance/employees/{employeeId}/goals/{goalId}/aggregate | Get Goal Aggregate
*PublicAPIApi* | [**get_goal_creation_permission**](docs/PublicAPIApi.md#get_goal_creation_permission) | **GET** /api/v1/performance/employees/{employeeId}/goals/canCreateGoals | Get Goal Creation Permission
*PublicAPIApi* | [**get_goals_aggregate_v1**](docs/PublicAPIApi.md#get_goals_aggregate_v1) | **GET** /api/v1/performance/employees/{employeeId}/goals/aggregate | Get Goals Aggregate (v1)
*PublicAPIApi* | [**get_goals_aggregate_v1_1**](docs/PublicAPIApi.md#get_goals_aggregate_v1_1) | **GET** /api/v1_1/performance/employees/{employeeId}/goals/aggregate | Get Goals Aggregate (v1.1)
*PublicAPIApi* | [**get_goals_aggregate_v1_2**](docs/PublicAPIApi.md#get_goals_aggregate_v1_2) | **GET** /api/v1_2/performance/employees/{employeeId}/goals/aggregate | Get Goals Aggregate (v1.2)
*PublicAPIApi* | [**get_goals_filters_v1**](docs/PublicAPIApi.md#get_goals_filters_v1) | **GET** /api/v1/performance/employees/{employeeId}/goals/filters | Get Goal Filters (v1)
*PublicAPIApi* | [**get_goals_filters_v1_1**](docs/PublicAPIApi.md#get_goals_filters_v1_1) | **GET** /api/v1_1/performance/employees/{employeeId}/goals/filters | Get Goal Filters (v1.1)
*PublicAPIApi* | [**get_goals_filters_v1_2**](docs/PublicAPIApi.md#get_goals_filters_v1_2) | **GET** /api/v1_2/performance/employees/{employeeId}/goals/filters | Get Goal Filters (v1.2)
*PublicAPIApi* | [**get_hiring_leads**](docs/PublicAPIApi.md#get_hiring_leads) | **GET** /api/v1/applicant_tracking/hiring_leads | Get Hiring Leads
*PublicAPIApi* | [**get_industries**](docs/PublicAPIApi.md#get_industries) | **GET** /api/v1/meta/industries | Get Industries
*PublicAPIApi* | [**get_job_summaries**](docs/PublicAPIApi.md#get_job_summaries) | **GET** /api/v1/applicant_tracking/jobs | Get Job Summaries
*PublicAPIApi* | [**get_location**](docs/PublicAPIApi.md#get_location) | **GET** /api/v1/hris/org/locations/{id} | Get a job location
*PublicAPIApi* | [**get_locations**](docs/PublicAPIApi.md#get_locations) | **GET** /api/v1/hris/org/locations | List job locations
*PublicAPIApi* | [**get_meta_company**](docs/PublicAPIApi.md#get_meta_company) | **GET** /api/v1/meta/company | Get company properties
*PublicAPIApi* | [**get_meta_country_by_id**](docs/PublicAPIApi.md#get_meta_country_by_id) | **GET** /api/v1/meta/countries/{id} | Get country by ID
*PublicAPIApi* | [**get_post_fields**](docs/PublicAPIApi.md#get_post_fields) | **GET** /api/v1/webhooks/post-fields | Get Webhook Post Fields
*PublicAPIApi* | [**get_project**](docs/PublicAPIApi.md#get_project) | **GET** /api/v1/time-tracking/projects/{projectId} | Get Time Tracking Project
*PublicAPIApi* | [**get_report_by_id**](docs/PublicAPIApi.md#get_report_by_id) | **GET** /api/v1/custom-reports/{reportId} | Get Report by ID
*PublicAPIApi* | [**get_states_by_country_id**](docs/PublicAPIApi.md#get_states_by_country_id) | **GET** /api/v1/meta/provinces/{countryId} | List states and provinces for a country by Country ID
*PublicAPIApi* | [**get_statuses**](docs/PublicAPIApi.md#get_statuses) | **GET** /api/v1/applicant_tracking/statuses | Get Applicant Statuses
*PublicAPIApi* | [**get_task**](docs/PublicAPIApi.md#get_task) | **GET** /api/v1/time-tracking/tasks/{id} | Get Time Tracking Task
*PublicAPIApi* | [**get_time_off_balance**](docs/PublicAPIApi.md#get_time_off_balance) | **GET** /api/v1/employees/{employeeId}/time_off/calculator | Get Time Off Balance
*PublicAPIApi* | [**get_time_tracking_record**](docs/PublicAPIApi.md#get_time_tracking_record) | **GET** /api/v1/timetracking/record/{id} | Get Time Tracking Record
*PublicAPIApi* | [**get_total_rewards_printable_statement**](docs/PublicAPIApi.md#get_total_rewards_printable_statement) | **GET** /api/v1/compensation/total_rewards/{employeeId}/printable | Get Printable Total Rewards Statement
*PublicAPIApi* | [**get_total_rewards_statement**](docs/PublicAPIApi.md#get_total_rewards_statement) | **GET** /api/v1/compensation/total_rewards/{employeeId}/statement | Get Total Rewards Statement
*PublicAPIApi* | [**get_webhook**](docs/PublicAPIApi.md#get_webhook) | **GET** /api/v1/webhooks/{id} | Get Webhook
*PublicAPIApi* | [**import_compensation_benchmarks**](docs/PublicAPIApi.md#import_compensation_benchmarks) | **POST** /api/v1/compensation/benchmarks/import | Import Compensation Benchmarks From CSV
*PublicAPIApi* | [**list_benefit_coverages**](docs/PublicAPIApi.md#list_benefit_coverages) | **GET** /api/v1/benefitcoverages | List Benefit Coverages
*PublicAPIApi* | [**list_benefit_deduction_types**](docs/PublicAPIApi.md#list_benefit_deduction_types) | **GET** /api/v1/benefits/settings/deduction_types/all | List Benefit Deduction Types
*PublicAPIApi* | [**list_break_assessments**](docs/PublicAPIApi.md#list_break_assessments) | **GET** /api/v1/time-tracking/break-assessments | List Break Assessments
*PublicAPIApi* | [**list_break_policies**](docs/PublicAPIApi.md#list_break_policies) | **GET** /api/v1/time-tracking/break-policies | List Break Policies
*PublicAPIApi* | [**list_break_policy_breaks**](docs/PublicAPIApi.md#list_break_policy_breaks) | **GET** /api/v1/time-tracking/break-policies/{id}/breaks | List Breaks for Break Policy
*PublicAPIApi* | [**list_break_policy_employees**](docs/PublicAPIApi.md#list_break_policy_employees) | **GET** /api/v1/time-tracking/break-policies/{id}/employees | List Break Policy Employees
*PublicAPIApi* | [**list_company_benefits**](docs/PublicAPIApi.md#list_company_benefits) | **GET** /api/v1/benefit/company_benefit | List Company Benefits
*PublicAPIApi* | [**list_company_files**](docs/PublicAPIApi.md#list_company_files) | **GET** /api/v1/files/view | Get Company Files and Categories
*PublicAPIApi* | [**list_compensation_benchmark_sources**](docs/PublicAPIApi.md#list_compensation_benchmark_sources) | **GET** /api/v1/compensation/benchmarks/sources | List Compensation Benchmark Sources
*PublicAPIApi* | [**list_compensation_benchmarks**](docs/PublicAPIApi.md#list_compensation_benchmarks) | **GET** /api/v1/compensation/benchmarks | List Compensation Benchmarks
*PublicAPIApi* | [**list_datasets_v1**](docs/PublicAPIApi.md#list_datasets_v1) | **GET** /api/v1/datasets | List Datasets (v1)
*PublicAPIApi* | [**list_datasets_v12**](docs/PublicAPIApi.md#list_datasets_v12) | **GET** /api/v1_2/datasets | List Datasets (v1.2)
*PublicAPIApi* | [**list_employee_benefits**](docs/PublicAPIApi.md#list_employee_benefits) | **GET** /api/v1/benefit/employee_benefit | List Employee Benefits
*PublicAPIApi* | [**list_employee_break_availabilities**](docs/PublicAPIApi.md#list_employee_break_availabilities) | **GET** /api/v1/time-tracking/employees/{id}/break-availabilities | List Employee Break Availabilities
*PublicAPIApi* | [**list_employee_break_policies**](docs/PublicAPIApi.md#list_employee_break_policies) | **GET** /api/v1/time-tracking/employees/{id}/break-policies | List Employee Break Policies
*PublicAPIApi* | [**list_employee_dependents**](docs/PublicAPIApi.md#list_employee_dependents) | **GET** /api/v1/employeedependents | List Employee Dependents
*PublicAPIApi* | [**list_employee_files**](docs/PublicAPIApi.md#list_employee_files) | **GET** /api/v1/employees/{id}/files/view | List Employee Files
*PublicAPIApi* | [**list_employee_time_off_policies**](docs/PublicAPIApi.md#list_employee_time_off_policies) | **GET** /api/v1/employees/{employeeId}/time_off/policies | List Employee Time Off Policies
*PublicAPIApi* | [**list_employee_time_off_policies_v1_1**](docs/PublicAPIApi.md#list_employee_time_off_policies_v1_1) | **GET** /api/v1_1/employees/{employeeId}/time_off/policies | List Employee Time Off Policies v1.1
*PublicAPIApi* | [**list_employee_trainings**](docs/PublicAPIApi.md#list_employee_trainings) | **GET** /api/v1/training/record/employee/{employeeId} | List Employee Training Records
*PublicAPIApi* | [**list_employee_verifications_by_employee**](docs/PublicAPIApi.md#list_employee_verifications_by_employee) | **GET** /api/v1/employee-verifications/employees/{employeeId} | List employee verification records for an employee
*PublicAPIApi* | [**list_employees**](docs/PublicAPIApi.md#list_employees) | **GET** /api/v1/employees | List Employees
*PublicAPIApi* | [**list_fields**](docs/PublicAPIApi.md#list_fields) | **GET** /api/v1/meta/fields | List Fields
*PublicAPIApi* | [**list_goal_comments**](docs/PublicAPIApi.md#list_goal_comments) | **GET** /api/v1/performance/employees/{employeeId}/goals/{goalId}/comments | List Goal Comments
*PublicAPIApi* | [**list_goal_share_options**](docs/PublicAPIApi.md#list_goal_share_options) | **GET** /api/v1/performance/employees/{employeeId}/goals/shareOptions | List Goal Sharing Options
*PublicAPIApi* | [**list_goals**](docs/PublicAPIApi.md#list_goals) | **GET** /api/v1/performance/employees/{employeeId}/goals | List Goals
*PublicAPIApi* | [**list_list_fields**](docs/PublicAPIApi.md#list_list_fields) | **GET** /api/v1/meta/lists | List List Fields
*PublicAPIApi* | [**list_member_benefit_events**](docs/PublicAPIApi.md#list_member_benefit_events) | **GET** /api/v1/benefit/member_benefit | List Member Benefit Events
*PublicAPIApi* | [**list_member_benefits**](docs/PublicAPIApi.md#list_member_benefits) | **GET** /api/v1/benefits/member-benefits | List Member Benefits
*PublicAPIApi* | [**list_monitor_fields**](docs/PublicAPIApi.md#list_monitor_fields) | **GET** /api/v1/webhooks/monitor_fields | List Monitor Fields
*PublicAPIApi* | [**list_project_tasks**](docs/PublicAPIApi.md#list_project_tasks) | **GET** /api/v1/time-tracking/projects/{projectId}/tasks | List Time Tracking Project Tasks
*PublicAPIApi* | [**list_projects**](docs/PublicAPIApi.md#list_projects) | **GET** /api/v1/time-tracking/projects | List Time Tracking Projects
*PublicAPIApi* | [**list_reports**](docs/PublicAPIApi.md#list_reports) | **GET** /api/v1/custom-reports | List Reports
*PublicAPIApi* | [**list_tabular_fields**](docs/PublicAPIApi.md#list_tabular_fields) | **GET** /api/v1/meta/tables | List Tabular Fields
*PublicAPIApi* | [**list_time_off_policies**](docs/PublicAPIApi.md#list_time_off_policies) | **GET** /api/v1/meta/time_off/policies | List Time Off Policies
*PublicAPIApi* | [**list_time_off_requests**](docs/PublicAPIApi.md#list_time_off_requests) | **GET** /api/v1/time_off/requests | List Time Off Requests
*PublicAPIApi* | [**list_time_off_types**](docs/PublicAPIApi.md#list_time_off_types) | **GET** /api/v1/meta/time_off/types | List Time Off Types
*PublicAPIApi* | [**list_timesheet_entries**](docs/PublicAPIApi.md#list_timesheet_entries) | **GET** /api/v1/time_tracking/timesheet_entries | List Timesheet Entries
*PublicAPIApi* | [**list_training_categories**](docs/PublicAPIApi.md#list_training_categories) | **GET** /api/v1/training/category | List Training Categories
*PublicAPIApi* | [**list_training_types**](docs/PublicAPIApi.md#list_training_types) | **GET** /api/v1/training/type | List Training Types
*PublicAPIApi* | [**list_users**](docs/PublicAPIApi.md#list_users) | **GET** /api/v1/meta/users | List Users
*PublicAPIApi* | [**list_webhook_logs**](docs/PublicAPIApi.md#list_webhook_logs) | **GET** /api/v1/webhooks/{id}/log | List Webhook Logs
*PublicAPIApi* | [**list_webhooks**](docs/PublicAPIApi.md#list_webhooks) | **GET** /api/v1/webhooks | List Webhooks
*PublicAPIApi* | [**list_whos_out**](docs/PublicAPIApi.md#list_whos_out) | **GET** /api/v1/time_off/whos_out | List Who’s Out
*PublicAPIApi* | [**login**](docs/PublicAPIApi.md#login) | **POST** /api/v1/login | Login
*PublicAPIApi* | [**patch_company_profile_company_information**](docs/PublicAPIApi.md#patch_company_profile_company_information) | **PATCH** /api/v1/company-profile-data/company-information | Update company information (phone, address, legal name)
*PublicAPIApi* | [**put_company_industry_codes**](docs/PublicAPIApi.md#put_company_industry_codes) | **PUT** /api/v1/company-profile-data/industry-codes | Update Company Industry Codes
*PublicAPIApi* | [**put_company_profile_display_name**](docs/PublicAPIApi.md#put_company_profile_display_name) | **PUT** /api/v1/company-profile-data/display-name | Update company display name
*PublicAPIApi* | [**remove_total_rewards_custom_disclaimer**](docs/PublicAPIApi.md#remove_total_rewards_custom_disclaimer) | **DELETE** /api/v1/compensation/total_rewards/custom_disclaimer | Remove Total Rewards Custom Disclaimer
*PublicAPIApi* | [**remove_total_rewards_employees**](docs/PublicAPIApi.md#remove_total_rewards_employees) | **DELETE** /api/v1/compensation/total_rewards/employees | Remove Employees from Total Rewards
*PublicAPIApi* | [**reopen_goal**](docs/PublicAPIApi.md#reopen_goal) | **POST** /api/v1/performance/employees/{employeeId}/goals/{goalId}/reopen | Reopen Goal
*PublicAPIApi* | [**replace_breaks_for_break_policy**](docs/PublicAPIApi.md#replace_breaks_for_break_policy) | **PUT** /api/v1/time-tracking/break-policies/{id}/breaks | Replace Breaks for Break Policy
*PublicAPIApi* | [**request_custom_report**](docs/PublicAPIApi.md#request_custom_report) | **POST** /api/v1/reports/custom | Request Custom Report
*PublicAPIApi* | [**scheduling_create_schedule**](docs/PublicAPIApi.md#scheduling_create_schedule) | **POST** /api/v1/scheduling/schedules | Create Schedule
*PublicAPIApi* | [**scheduling_create_shift**](docs/PublicAPIApi.md#scheduling_create_shift) | **POST** /api/v1/scheduling/shifts | Create Shift
*PublicAPIApi* | [**scheduling_delete_schedule**](docs/PublicAPIApi.md#scheduling_delete_schedule) | **DELETE** /api/v1/scheduling/schedules/{id} | Delete Schedule
*PublicAPIApi* | [**scheduling_delete_shift**](docs/PublicAPIApi.md#scheduling_delete_shift) | **DELETE** /api/v1/scheduling/shifts/{id} | Delete Shift
*PublicAPIApi* | [**scheduling_get_schedule**](docs/PublicAPIApi.md#scheduling_get_schedule) | **GET** /api/v1/scheduling/schedules/{id} | Get Schedule
*PublicAPIApi* | [**scheduling_get_schedule_pdf**](docs/PublicAPIApi.md#scheduling_get_schedule_pdf) | **GET** /api/v1/scheduling/schedules/{id}/pdf | Get Schedule PDF
*PublicAPIApi* | [**scheduling_get_shift**](docs/PublicAPIApi.md#scheduling_get_shift) | **GET** /api/v1/scheduling/shifts/{id} | Get Shift
*PublicAPIApi* | [**scheduling_list_schedules**](docs/PublicAPIApi.md#scheduling_list_schedules) | **GET** /api/v1/scheduling/schedules | List Schedules
*PublicAPIApi* | [**scheduling_list_shifts**](docs/PublicAPIApi.md#scheduling_list_shifts) | **GET** /api/v1/scheduling/shifts | List Shifts
*PublicAPIApi* | [**scheduling_list_timezones**](docs/PublicAPIApi.md#scheduling_list_timezones) | **GET** /api/v1/scheduling/timezones | List Timezones
*PublicAPIApi* | [**scheduling_publish_shifts**](docs/PublicAPIApi.md#scheduling_publish_shifts) | **POST** /api/v1/scheduling/shifts/publish | Publish Shifts
*PublicAPIApi* | [**scheduling_update_schedule**](docs/PublicAPIApi.md#scheduling_update_schedule) | **PATCH** /api/v1/scheduling/schedules/{id} | Update Schedule
*PublicAPIApi* | [**scheduling_update_shift**](docs/PublicAPIApi.md#scheduling_update_shift) | **PATCH** /api/v1/scheduling/shifts/{id} | Update Shift
*PublicAPIApi* | [**send_employee_verification_lifecycle_email_by_user**](docs/PublicAPIApi.md#send_employee_verification_lifecycle_email_by_user) | **POST** /api/v1/employee-verifications/users/{userId}/send-email | Send employee verification lifecycle email by user and email type
*PublicAPIApi* | [**set_break_policy_employees**](docs/PublicAPIApi.md#set_break_policy_employees) | **PUT** /api/v1/time-tracking/break-policies/{id}/assign | Set Employees for Break Policy
*PublicAPIApi* | [**set_total_rewards_custom_disclaimer**](docs/PublicAPIApi.md#set_total_rewards_custom_disclaimer) | **PUT** /api/v1/compensation/total_rewards/custom_disclaimer | Set Total Rewards Custom Disclaimer
*PublicAPIApi* | [**set_total_rewards_onboarding_step**](docs/PublicAPIApi.md#set_total_rewards_onboarding_step) | **PUT** /api/v1/compensation/total_rewards/onboarding/{stepName} | Set Total Rewards Onboarding Step Status
*PublicAPIApi* | [**sync_break_policy**](docs/PublicAPIApi.md#sync_break_policy) | **PUT** /api/v1/time-tracking/break-policies/{id}/sync | Sync Break Policy
*PublicAPIApi* | [**unassign_employees_from_break_policy**](docs/PublicAPIApi.md#unassign_employees_from_break_policy) | **POST** /api/v1/time-tracking/break-policies/{id}/unassign | Unassign Employees from Break Policy
*PublicAPIApi* | [**update_applicant_status**](docs/PublicAPIApi.md#update_applicant_status) | **POST** /api/v1/applicant_tracking/applications/{applicationId}/status | Update Applicant Status
*PublicAPIApi* | [**update_break**](docs/PublicAPIApi.md#update_break) | **PATCH** /api/v1/time-tracking/breaks/{id} | Update Break
*PublicAPIApi* | [**update_break_policy**](docs/PublicAPIApi.md#update_break_policy) | **PATCH** /api/v1/time-tracking/break-policies/{id} | Update Break Policy
*PublicAPIApi* | [**update_company_file**](docs/PublicAPIApi.md#update_company_file) | **POST** /api/v1/files/{fileId} | Update Company File
*PublicAPIApi* | [**update_compensation_benchmark**](docs/PublicAPIApi.md#update_compensation_benchmark) | **PUT** /api/v1/compensation/benchmarks | Update Compensation Benchmark
*PublicAPIApi* | [**update_compensation_benchmark_sources**](docs/PublicAPIApi.md#update_compensation_benchmark_sources) | **PUT** /api/v1/compensation/benchmarks/sources | Update Compensation Benchmark Sources
*PublicAPIApi* | [**update_employee**](docs/PublicAPIApi.md#update_employee) | **POST** /api/v1/employees/{id} | Update Employee
*PublicAPIApi* | [**update_employee_dependent**](docs/PublicAPIApi.md#update_employee_dependent) | **PUT** /api/v1/employeedependents/{id} | Update Employee Dependent
*PublicAPIApi* | [**update_employee_file**](docs/PublicAPIApi.md#update_employee_file) | **POST** /api/v1/employees/{id}/files/{fileId} | Update Employee File
*PublicAPIApi* | [**update_employee_training_record**](docs/PublicAPIApi.md#update_employee_training_record) | **PUT** /api/v1/training/record/{employeeTrainingRecordId} | Update Employee Training Record
*PublicAPIApi* | [**update_employee_verification**](docs/PublicAPIApi.md#update_employee_verification) | **PUT** /api/v1/employee-verifications/employees/{employeeId}/{verificationId} | Update an employee verification record
*PublicAPIApi* | [**update_employee_verification_integration**](docs/PublicAPIApi.md#update_employee_verification_integration) | **PUT** /api/v1/employee-verifications/integration | Enable or disable the employee verification integration
*PublicAPIApi* | [**update_goal_comment**](docs/PublicAPIApi.md#update_goal_comment) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId}/comments/{commentId} | Update Goal Comment
*PublicAPIApi* | [**update_goal_milestone_progress**](docs/PublicAPIApi.md#update_goal_milestone_progress) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId}/milestones/{milestoneId}/progress | Update Milestone Progress
*PublicAPIApi* | [**update_goal_progress**](docs/PublicAPIApi.md#update_goal_progress) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId}/progress | Update Goal Progress
*PublicAPIApi* | [**update_goal_sharing**](docs/PublicAPIApi.md#update_goal_sharing) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId}/sharedWith | Update Goal Sharing
*PublicAPIApi* | [**update_goal_v1**](docs/PublicAPIApi.md#update_goal_v1) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId} | Update Goal (v1)
*PublicAPIApi* | [**update_goal_v1_1**](docs/PublicAPIApi.md#update_goal_v1_1) | **PUT** /api/v1_1/performance/employees/{employeeId}/goals/{goalId} | Update Goal (v1.1)
*PublicAPIApi* | [**update_list_field_values**](docs/PublicAPIApi.md#update_list_field_values) | **PUT** /api/v1/meta/lists/{listFieldId} | Update List Field Values
*PublicAPIApi* | [**update_location**](docs/PublicAPIApi.md#update_location) | **PUT** /api/v1/hris/org/locations/{id} | Update a job location
*PublicAPIApi* | [**update_new_hire_packet_gtky_answer_visibility**](docs/PublicAPIApi.md#update_new_hire_packet_gtky_answer_visibility) | **PUT** /api/v1/new-hire-packets/{id}/question-visibility | Update GTKY answer visibility for a new hire packet
*PublicAPIApi* | [**update_project**](docs/PublicAPIApi.md#update_project) | **PATCH** /api/v1/time-tracking/projects/{id} | Update Time Tracking Project
*PublicAPIApi* | [**update_table_row**](docs/PublicAPIApi.md#update_table_row) | **POST** /api/v1/employees/{id}/tables/{table}/{rowId} | Update Table Row
*PublicAPIApi* | [**update_table_row_v11**](docs/PublicAPIApi.md#update_table_row_v11) | **POST** /api/v1_1/employees/{id}/tables/{table}/{rowId} | Update Table Row v1.1
*PublicAPIApi* | [**update_task**](docs/PublicAPIApi.md#update_task) | **PATCH** /api/v1/time-tracking/tasks/{id} | Update Time Tracking Task
*PublicAPIApi* | [**update_time_off_request_status**](docs/PublicAPIApi.md#update_time_off_request_status) | **PUT** /api/v1/time_off/requests/{requestId}/status | Update Time Off Request Status
*PublicAPIApi* | [**update_time_tracking_record**](docs/PublicAPIApi.md#update_time_tracking_record) | **PUT** /api/v1/timetracking/adjust | Update Hour Record
*PublicAPIApi* | [**update_training_category**](docs/PublicAPIApi.md#update_training_category) | **PUT** /api/v1/training/category/{trainingCategoryId} | Update Training Category
*PublicAPIApi* | [**update_training_type**](docs/PublicAPIApi.md#update_training_type) | **PUT** /api/v1/training/type/{trainingTypeId} | Update Training Type
*PublicAPIApi* | [**update_webhook**](docs/PublicAPIApi.md#update_webhook) | **PUT** /api/v1/webhooks/{id} | Update Webhook
*PublicAPIApi* | [**upload_company_file**](docs/PublicAPIApi.md#upload_company_file) | **POST** /api/v1/files | Upload Company File
*PublicAPIApi* | [**upload_employee_file**](docs/PublicAPIApi.md#upload_employee_file) | **POST** /api/v1/employees/{id}/files | Upload Employee File
*PublicAPIApi* | [**upload_employee_photo**](docs/PublicAPIApi.md#upload_employee_photo) | **POST** /api/v1/employees/{employeeId}/photo | Upload Employee Photo
*ReportsApi* | [**get_company_report**](docs/ReportsApi.md#get_company_report) | **GET** /api/v1/reports/{id} | Get Company Report
*ReportsApi* | [**request_custom_report**](docs/ReportsApi.md#request_custom_report) | **POST** /api/v1/reports/custom | Request Custom Report
*SchedulingApi* | [**scheduling_create_schedule**](docs/SchedulingApi.md#scheduling_create_schedule) | **POST** /api/v1/scheduling/schedules | Create Schedule
*SchedulingApi* | [**scheduling_create_shift**](docs/SchedulingApi.md#scheduling_create_shift) | **POST** /api/v1/scheduling/shifts | Create Shift
*SchedulingApi* | [**scheduling_delete_schedule**](docs/SchedulingApi.md#scheduling_delete_schedule) | **DELETE** /api/v1/scheduling/schedules/{id} | Delete Schedule
*SchedulingApi* | [**scheduling_delete_shift**](docs/SchedulingApi.md#scheduling_delete_shift) | **DELETE** /api/v1/scheduling/shifts/{id} | Delete Shift
*SchedulingApi* | [**scheduling_get_schedule**](docs/SchedulingApi.md#scheduling_get_schedule) | **GET** /api/v1/scheduling/schedules/{id} | Get Schedule
*SchedulingApi* | [**scheduling_get_schedule_pdf**](docs/SchedulingApi.md#scheduling_get_schedule_pdf) | **GET** /api/v1/scheduling/schedules/{id}/pdf | Get Schedule PDF
*SchedulingApi* | [**scheduling_get_shift**](docs/SchedulingApi.md#scheduling_get_shift) | **GET** /api/v1/scheduling/shifts/{id} | Get Shift
*SchedulingApi* | [**scheduling_list_schedules**](docs/SchedulingApi.md#scheduling_list_schedules) | **GET** /api/v1/scheduling/schedules | List Schedules
*SchedulingApi* | [**scheduling_list_shifts**](docs/SchedulingApi.md#scheduling_list_shifts) | **GET** /api/v1/scheduling/shifts | List Shifts
*SchedulingApi* | [**scheduling_list_timezones**](docs/SchedulingApi.md#scheduling_list_timezones) | **GET** /api/v1/scheduling/timezones | List Timezones
*SchedulingApi* | [**scheduling_publish_shifts**](docs/SchedulingApi.md#scheduling_publish_shifts) | **POST** /api/v1/scheduling/shifts/publish | Publish Shifts
*SchedulingApi* | [**scheduling_update_schedule**](docs/SchedulingApi.md#scheduling_update_schedule) | **PATCH** /api/v1/scheduling/schedules/{id} | Update Schedule
*SchedulingApi* | [**scheduling_update_shift**](docs/SchedulingApi.md#scheduling_update_shift) | **PATCH** /api/v1/scheduling/shifts/{id} | Update Shift
*TabularDataApi* | [**create_table_row**](docs/TabularDataApi.md#create_table_row) | **POST** /api/v1/employees/{id}/tables/{table} | Create Table Row
*TabularDataApi* | [**create_table_row_v11**](docs/TabularDataApi.md#create_table_row_v11) | **POST** /api/v1_1/employees/{id}/tables/{table} | Create Table Row v1.1
*TabularDataApi* | [**delete_employee_table_row**](docs/TabularDataApi.md#delete_employee_table_row) | **DELETE** /api/v1/employees/{id}/tables/{table}/{rowId} | Delete Employee Table Row
*TabularDataApi* | [**get_changed_employee_table_data**](docs/TabularDataApi.md#get_changed_employee_table_data) | **GET** /api/v1/employees/changed/tables/{table} | Get Changed Employee Table Data
*TabularDataApi* | [**get_employee_table_data**](docs/TabularDataApi.md#get_employee_table_data) | **GET** /api/v1/employees/{id}/tables/{table} | Get Employee Table Data
*TabularDataApi* | [**update_table_row**](docs/TabularDataApi.md#update_table_row) | **POST** /api/v1/employees/{id}/tables/{table}/{rowId} | Update Table Row
*TabularDataApi* | [**update_table_row_v11**](docs/TabularDataApi.md#update_table_row_v11) | **POST** /api/v1_1/employees/{id}/tables/{table}/{rowId} | Update Table Row v1.1
*TimeOffApi* | [**adjust_time_off_balance**](docs/TimeOffApi.md#adjust_time_off_balance) | **PUT** /api/v1/employees/{employeeId}/time_off/balance_adjustment | Adjust Time Off Balance
*TimeOffApi* | [**assign_time_off_policies**](docs/TimeOffApi.md#assign_time_off_policies) | **PUT** /api/v1/employees/{employeeId}/time_off/policies | Assign Time Off Policies
*TimeOffApi* | [**assign_time_off_policies_v1_1**](docs/TimeOffApi.md#assign_time_off_policies_v1_1) | **PUT** /api/v1_1/employees/{employeeId}/time_off/policies | Assign Time Off Policies v1.1
*TimeOffApi* | [**create_time_off_history**](docs/TimeOffApi.md#create_time_off_history) | **PUT** /api/v1/employees/{employeeId}/time_off/history | Create Time Off History Item
*TimeOffApi* | [**create_time_off_request**](docs/TimeOffApi.md#create_time_off_request) | **PUT** /api/v1/employees/{employeeId}/time_off/request | Create Time Off Request
*TimeOffApi* | [**get_time_off_balance**](docs/TimeOffApi.md#get_time_off_balance) | **GET** /api/v1/employees/{employeeId}/time_off/calculator | Get Time Off Balance
*TimeOffApi* | [**list_employee_time_off_policies**](docs/TimeOffApi.md#list_employee_time_off_policies) | **GET** /api/v1/employees/{employeeId}/time_off/policies | List Employee Time Off Policies
*TimeOffApi* | [**list_employee_time_off_policies_v1_1**](docs/TimeOffApi.md#list_employee_time_off_policies_v1_1) | **GET** /api/v1_1/employees/{employeeId}/time_off/policies | List Employee Time Off Policies v1.1
*TimeOffApi* | [**list_time_off_policies**](docs/TimeOffApi.md#list_time_off_policies) | **GET** /api/v1/meta/time_off/policies | List Time Off Policies
*TimeOffApi* | [**list_time_off_requests**](docs/TimeOffApi.md#list_time_off_requests) | **GET** /api/v1/time_off/requests | List Time Off Requests
*TimeOffApi* | [**list_time_off_types**](docs/TimeOffApi.md#list_time_off_types) | **GET** /api/v1/meta/time_off/types | List Time Off Types
*TimeOffApi* | [**list_whos_out**](docs/TimeOffApi.md#list_whos_out) | **GET** /api/v1/time_off/whos_out | List Who’s Out
*TimeOffApi* | [**update_time_off_request_status**](docs/TimeOffApi.md#update_time_off_request_status) | **PUT** /api/v1/time_off/requests/{requestId}/status | Update Time Off Request Status
*TimeTrackingApi* | [**assign_employees_to_break_policy**](docs/TimeTrackingApi.md#assign_employees_to_break_policy) | **POST** /api/v1/time-tracking/break-policies/{id}/assign | Assign Employees to Break Policy
*TimeTrackingApi* | [**create_break**](docs/TimeTrackingApi.md#create_break) | **POST** /api/v1/time-tracking/break-policies/{id}/breaks | Create Break
*TimeTrackingApi* | [**create_break_policy**](docs/TimeTrackingApi.md#create_break_policy) | **POST** /api/v1/time-tracking/break-policies | Create Break Policy
*TimeTrackingApi* | [**create_or_update_timesheet_clock_entries**](docs/TimeTrackingApi.md#create_or_update_timesheet_clock_entries) | **POST** /api/v1/time_tracking/clock_entries/store | Create or Update Timesheet Clock Entries
*TimeTrackingApi* | [**create_or_update_timesheet_hour_entries**](docs/TimeTrackingApi.md#create_or_update_timesheet_hour_entries) | **POST** /api/v1/time_tracking/hour_entries/store | Create or Update Timesheet Hour Entries
*TimeTrackingApi* | [**create_project**](docs/TimeTrackingApi.md#create_project) | **POST** /api/v1/time-tracking/projects | Create Time Tracking Project
*TimeTrackingApi* | [**create_project_task**](docs/TimeTrackingApi.md#create_project_task) | **POST** /api/v1/time-tracking/projects/{projectId}/tasks | Create Time Tracking Project Task
*TimeTrackingApi* | [**create_time_tracking_project**](docs/TimeTrackingApi.md#create_time_tracking_project) | **POST** /api/v1/time_tracking/projects | Create Time Tracking Project
*TimeTrackingApi* | [**create_timesheet_clock_in_entry**](docs/TimeTrackingApi.md#create_timesheet_clock_in_entry) | **POST** /api/v1/time_tracking/employees/{employeeId}/clock_in | Create Timesheet Clock-In Entry
*TimeTrackingApi* | [**create_timesheet_clock_out_entry**](docs/TimeTrackingApi.md#create_timesheet_clock_out_entry) | **POST** /api/v1/time_tracking/employees/{employeeId}/clock_out | Create Timesheet Clock-Out Entry
*TimeTrackingApi* | [**delete_break**](docs/TimeTrackingApi.md#delete_break) | **DELETE** /api/v1/time-tracking/breaks/{id} | Delete Break
*TimeTrackingApi* | [**delete_break_policy**](docs/TimeTrackingApi.md#delete_break_policy) | **DELETE** /api/v1/time-tracking/break-policies/{id} | Delete Break Policy
*TimeTrackingApi* | [**delete_project**](docs/TimeTrackingApi.md#delete_project) | **DELETE** /api/v1/time-tracking/projects/{id} | Delete Time Tracking Project
*TimeTrackingApi* | [**delete_task**](docs/TimeTrackingApi.md#delete_task) | **DELETE** /api/v1/time-tracking/tasks/{id} | Delete Time Tracking Task
*TimeTrackingApi* | [**delete_timesheet_clock_entries_via_post**](docs/TimeTrackingApi.md#delete_timesheet_clock_entries_via_post) | **POST** /api/v1/time_tracking/clock_entries/delete | Delete Timesheet Clock Entries
*TimeTrackingApi* | [**delete_timesheet_hour_entries_via_post**](docs/TimeTrackingApi.md#delete_timesheet_hour_entries_via_post) | **POST** /api/v1/time_tracking/hour_entries/delete | Delete Timesheet Hour Entries
*TimeTrackingApi* | [**get_break**](docs/TimeTrackingApi.md#get_break) | **GET** /api/v1/time-tracking/breaks/{id} | Get Break
*TimeTrackingApi* | [**get_break_policy**](docs/TimeTrackingApi.md#get_break_policy) | **GET** /api/v1/time-tracking/break-policies/{id} | Get Break Policy
*TimeTrackingApi* | [**get_break_policy_suggestions**](docs/TimeTrackingApi.md#get_break_policy_suggestions) | **POST** /api/v1/time-tracking/break-policies/suggestions | Get Break Policy Suggestions
*TimeTrackingApi* | [**get_project**](docs/TimeTrackingApi.md#get_project) | **GET** /api/v1/time-tracking/projects/{projectId} | Get Time Tracking Project
*TimeTrackingApi* | [**get_task**](docs/TimeTrackingApi.md#get_task) | **GET** /api/v1/time-tracking/tasks/{id} | Get Time Tracking Task
*TimeTrackingApi* | [**list_break_assessments**](docs/TimeTrackingApi.md#list_break_assessments) | **GET** /api/v1/time-tracking/break-assessments | List Break Assessments
*TimeTrackingApi* | [**list_break_policies**](docs/TimeTrackingApi.md#list_break_policies) | **GET** /api/v1/time-tracking/break-policies | List Break Policies
*TimeTrackingApi* | [**list_break_policy_breaks**](docs/TimeTrackingApi.md#list_break_policy_breaks) | **GET** /api/v1/time-tracking/break-policies/{id}/breaks | List Breaks for Break Policy
*TimeTrackingApi* | [**list_break_policy_employees**](docs/TimeTrackingApi.md#list_break_policy_employees) | **GET** /api/v1/time-tracking/break-policies/{id}/employees | List Break Policy Employees
*TimeTrackingApi* | [**list_employee_break_availabilities**](docs/TimeTrackingApi.md#list_employee_break_availabilities) | **GET** /api/v1/time-tracking/employees/{id}/break-availabilities | List Employee Break Availabilities
*TimeTrackingApi* | [**list_employee_break_policies**](docs/TimeTrackingApi.md#list_employee_break_policies) | **GET** /api/v1/time-tracking/employees/{id}/break-policies | List Employee Break Policies
*TimeTrackingApi* | [**list_project_tasks**](docs/TimeTrackingApi.md#list_project_tasks) | **GET** /api/v1/time-tracking/projects/{projectId}/tasks | List Time Tracking Project Tasks
*TimeTrackingApi* | [**list_projects**](docs/TimeTrackingApi.md#list_projects) | **GET** /api/v1/time-tracking/projects | List Time Tracking Projects
*TimeTrackingApi* | [**list_timesheet_entries**](docs/TimeTrackingApi.md#list_timesheet_entries) | **GET** /api/v1/time_tracking/timesheet_entries | List Timesheet Entries
*TimeTrackingApi* | [**replace_breaks_for_break_policy**](docs/TimeTrackingApi.md#replace_breaks_for_break_policy) | **PUT** /api/v1/time-tracking/break-policies/{id}/breaks | Replace Breaks for Break Policy
*TimeTrackingApi* | [**set_break_policy_employees**](docs/TimeTrackingApi.md#set_break_policy_employees) | **PUT** /api/v1/time-tracking/break-policies/{id}/assign | Set Employees for Break Policy
*TimeTrackingApi* | [**sync_break_policy**](docs/TimeTrackingApi.md#sync_break_policy) | **PUT** /api/v1/time-tracking/break-policies/{id}/sync | Sync Break Policy
*TimeTrackingApi* | [**unassign_employees_from_break_policy**](docs/TimeTrackingApi.md#unassign_employees_from_break_policy) | **POST** /api/v1/time-tracking/break-policies/{id}/unassign | Unassign Employees from Break Policy
*TimeTrackingApi* | [**update_break**](docs/TimeTrackingApi.md#update_break) | **PATCH** /api/v1/time-tracking/breaks/{id} | Update Break
*TimeTrackingApi* | [**update_break_policy**](docs/TimeTrackingApi.md#update_break_policy) | **PATCH** /api/v1/time-tracking/break-policies/{id} | Update Break Policy
*TimeTrackingApi* | [**update_project**](docs/TimeTrackingApi.md#update_project) | **PATCH** /api/v1/time-tracking/projects/{id} | Update Time Tracking Project
*TimeTrackingApi* | [**update_task**](docs/TimeTrackingApi.md#update_task) | **PATCH** /api/v1/time-tracking/tasks/{id} | Update Time Tracking Task
*TotalRewardsApi* | [**add_total_rewards_employees**](docs/TotalRewardsApi.md#add_total_rewards_employees) | **POST** /api/v1/compensation/total_rewards/employees | Add Employees to Total Rewards
*TotalRewardsApi* | [**check_total_rewards_profile**](docs/TotalRewardsApi.md#check_total_rewards_profile) | **GET** /api/v1/compensation/total_rewards/{employeeId} | Check Total Rewards Profile Availability
*TotalRewardsApi* | [**get_total_rewards_printable_statement**](docs/TotalRewardsApi.md#get_total_rewards_printable_statement) | **GET** /api/v1/compensation/total_rewards/{employeeId}/printable | Get Printable Total Rewards Statement
*TotalRewardsApi* | [**get_total_rewards_statement**](docs/TotalRewardsApi.md#get_total_rewards_statement) | **GET** /api/v1/compensation/total_rewards/{employeeId}/statement | Get Total Rewards Statement
*TotalRewardsApi* | [**remove_total_rewards_custom_disclaimer**](docs/TotalRewardsApi.md#remove_total_rewards_custom_disclaimer) | **DELETE** /api/v1/compensation/total_rewards/custom_disclaimer | Remove Total Rewards Custom Disclaimer
*TotalRewardsApi* | [**remove_total_rewards_employees**](docs/TotalRewardsApi.md#remove_total_rewards_employees) | **DELETE** /api/v1/compensation/total_rewards/employees | Remove Employees from Total Rewards
*TotalRewardsApi* | [**set_total_rewards_custom_disclaimer**](docs/TotalRewardsApi.md#set_total_rewards_custom_disclaimer) | **PUT** /api/v1/compensation/total_rewards/custom_disclaimer | Set Total Rewards Custom Disclaimer
*TotalRewardsApi* | [**set_total_rewards_onboarding_step**](docs/TotalRewardsApi.md#set_total_rewards_onboarding_step) | **PUT** /api/v1/compensation/total_rewards/onboarding/{stepName} | Set Total Rewards Onboarding Step Status
*TrainingApi* | [**create_employee_training_record**](docs/TrainingApi.md#create_employee_training_record) | **POST** /api/v1/training/record/employee/{employeeId} | Create Employee Training Record
*TrainingApi* | [**create_training_category**](docs/TrainingApi.md#create_training_category) | **POST** /api/v1/training/category | Create Training Category
*TrainingApi* | [**create_training_type**](docs/TrainingApi.md#create_training_type) | **POST** /api/v1/training/type | Create Training Type
*TrainingApi* | [**delete_employee_training_record**](docs/TrainingApi.md#delete_employee_training_record) | **DELETE** /api/v1/training/record/{employeeTrainingRecordId} | Delete Employee Training Record
*TrainingApi* | [**delete_training_category**](docs/TrainingApi.md#delete_training_category) | **DELETE** /api/v1/training/category/{trainingCategoryId} | Delete Training Category
*TrainingApi* | [**delete_training_type**](docs/TrainingApi.md#delete_training_type) | **DELETE** /api/v1/training/type/{trainingTypeId} | Delete Training Type
*TrainingApi* | [**list_employee_trainings**](docs/TrainingApi.md#list_employee_trainings) | **GET** /api/v1/training/record/employee/{employeeId} | List Employee Training Records
*TrainingApi* | [**list_training_categories**](docs/TrainingApi.md#list_training_categories) | **GET** /api/v1/training/category | List Training Categories
*TrainingApi* | [**list_training_types**](docs/TrainingApi.md#list_training_types) | **GET** /api/v1/training/type | List Training Types
*TrainingApi* | [**update_employee_training_record**](docs/TrainingApi.md#update_employee_training_record) | **PUT** /api/v1/training/record/{employeeTrainingRecordId} | Update Employee Training Record
*TrainingApi* | [**update_training_category**](docs/TrainingApi.md#update_training_category) | **PUT** /api/v1/training/category/{trainingCategoryId} | Update Training Category
*TrainingApi* | [**update_training_type**](docs/TrainingApi.md#update_training_type) | **PUT** /api/v1/training/type/{trainingTypeId} | Update Training Type
*WebhooksApi* | [**create_webhook**](docs/WebhooksApi.md#create_webhook) | **POST** /api/v1/webhooks | Create Webhook
*WebhooksApi* | [**delete_webhook**](docs/WebhooksApi.md#delete_webhook) | **DELETE** /api/v1/webhooks/{id} | Delete Webhook
*WebhooksApi* | [**get_post_fields**](docs/WebhooksApi.md#get_post_fields) | **GET** /api/v1/webhooks/post-fields | Get Webhook Post Fields
*WebhooksApi* | [**get_webhook**](docs/WebhooksApi.md#get_webhook) | **GET** /api/v1/webhooks/{id} | Get Webhook
*WebhooksApi* | [**list_monitor_fields**](docs/WebhooksApi.md#list_monitor_fields) | **GET** /api/v1/webhooks/monitor_fields | List Monitor Fields
*WebhooksApi* | [**list_webhook_logs**](docs/WebhooksApi.md#list_webhook_logs) | **GET** /api/v1/webhooks/{id}/log | List Webhook Logs
*WebhooksApi* | [**list_webhooks**](docs/WebhooksApi.md#list_webhooks) | **GET** /api/v1/webhooks | List Webhooks
*WebhooksApi* | [**update_webhook**](docs/WebhooksApi.md#update_webhook) | **PUT** /api/v1/webhooks/{id} | Update Webhook


## Models

- [A05b6d5f564f805d688ff2c1e37c3990Request](docs/A05b6d5f564f805d688ff2c1e37c3990Request.md)
- [Ad7871529b2a9c6612f8dd3c62192c08Request](docs/Ad7871529b2a9c6612f8dd3c62192c08Request.md)
- [AddCycleAdminsResponse](docs/AddCycleAdminsResponse.md)
- [AddCycleAdminsResponseAddedInner](docs/AddCycleAdminsResponseAddedInner.md)
- [AddCycleAdminsResponseSkippedInner](docs/AddCycleAdminsResponseSkippedInner.md)
- [AddTotalRewardsEmployeesRequest](docs/AddTotalRewardsEmployeesRequest.md)
- [AdjustTimeOffBalance](docs/AdjustTimeOffBalance.md)
- [AdjustTimeTrackingRequestSchema](docs/AdjustTimeTrackingRequestSchema.md)
- [AlertTemplateListResponse](docs/AlertTemplateListResponse.md)
- [AlertTemplateListResponseAlertsInner](docs/AlertTemplateListResponseAlertsInner.md)
- [AlignmentOptionsResponse](docs/AlignmentOptionsResponse.md)
- [AlignmentOptionsResponseAlignsWithOptionsInner](docs/AlignmentOptionsResponseAlignsWithOptionsInner.md)
- [ApplicantStatus](docs/ApplicantStatus.md)
- [ApplicationDetails](docs/ApplicationDetails.md)
- [ApplicationDetailsApplicant](docs/ApplicationDetailsApplicant.md)
- [ApplicationDetailsAttachmentsInner](docs/ApplicationDetailsAttachmentsInner.md)
- [ApplicationDetailsJob](docs/ApplicationDetailsJob.md)
- [ApplicationDetailsJobTitle](docs/ApplicationDetailsJobTitle.md)
- [ApplicationDetailsQuestionsAndAnswersInner](docs/ApplicationDetailsQuestionsAndAnswersInner.md)
- [ApplicationDetailsQuestionsAndAnswersInnerAnswer](docs/ApplicationDetailsQuestionsAndAnswersInnerAnswer.md)
- [ApplicationDetailsQuestionsAndAnswersInnerQuestion](docs/ApplicationDetailsQuestionsAndAnswersInnerQuestion.md)
- [ApplicationDetailsStatus](docs/ApplicationDetailsStatus.md)
- [ApplicationsList](docs/ApplicationsList.md)
- [ApplicationsListApplicationsInner](docs/ApplicationsListApplicationsInner.md)
- [ApplicationsListApplicationsInnerApplicant](docs/ApplicationsListApplicationsInnerApplicant.md)
- [ApplicationsListApplicationsInnerJob](docs/ApplicationsListApplicationsInnerJob.md)
- [ApplicationsListApplicationsInnerJobTitle](docs/ApplicationsListApplicationsInnerJobTitle.md)
- [ApplicationsListApplicationsInnerStatus](docs/ApplicationsListApplicationsInnerStatus.md)
- [AssignEmployeesToBreakPolicyRequest](docs/AssignEmployeesToBreakPolicyRequest.md)
- [AssignTimeOffPoliciesRequestInner](docs/AssignTimeOffPoliciesRequestInner.md)
- [AssignedTimeOffPolicy](docs/AssignedTimeOffPolicy.md)
- [AssignedTimeOffPolicyV11](docs/AssignedTimeOffPolicyV11.md)
- [AvailableAction](docs/AvailableAction.md)
- [BadRequestV1](docs/BadRequestV1.md)
- [BadRequestV1Error](docs/BadRequestV1Error.md)
- [BankHoliday](docs/BankHoliday.md)
- [BenefitCoveragesResponse](docs/BenefitCoveragesResponse.md)
- [BenefitCoveragesResponseBenefitCoveragesInner](docs/BenefitCoveragesResponseBenefitCoveragesInner.md)
- [BenefitDeductionSubType](docs/BenefitDeductionSubType.md)
- [BenefitDeductionType](docs/BenefitDeductionType.md)
- [BenefitDeductionTypeId](docs/BenefitDeductionTypeId.md)
- [BudgetBreakdownImportResponse](docs/BudgetBreakdownImportResponse.md)
- [BudgetGuidelinesView](docs/BudgetGuidelinesView.md)
- [BudgetGuidelinesWarnings](docs/BudgetGuidelinesWarnings.md)
- [C79f9c5950f983e59d2626faa30c00a1Request](docs/C79f9c5950f983e59d2626faa30c00a1Request.md)
- [C7c32ed5278ac67e2e518bf7484a75dcRequest](docs/C7c32ed5278ac67e2e518bf7484a75dcRequest.md)
- [CanCreateGoalsResponse](docs/CanCreateGoalsResponse.md)
- [Cf87b8e09a001b6fb81dfce6c20ab9e3Request](docs/Cf87b8e09a001b6fb81dfce6c20ab9e3Request.md)
- [ChangedEmployeeIdsResponse](docs/ChangedEmployeeIdsResponse.md)
- [ChangedEmployeeIdsResponseEmployeesValue](docs/ChangedEmployeeIdsResponseEmployeesValue.md)
- [ChangedEmployeeTableDataResponse](docs/ChangedEmployeeTableDataResponse.md)
- [ChangedEmployeeTableDataResponseEmployeesValue](docs/ChangedEmployeeTableDataResponseEmployeesValue.md)
- [ChangedEmployeeTableDataResponseEmployeesValueRowsInnerValue](docs/ChangedEmployeeTableDataResponseEmployeesValueRowsInnerValue.md)
- [ChangedEmployeeTableDataResponseEmployeesValueRowsInnerValueAnyOfInner](docs/ChangedEmployeeTableDataResponseEmployeesValueRowsInnerValueAnyOfInner.md)
- [ClockEntriesSchema](docs/ClockEntriesSchema.md)
- [ClockEntryIdsSchema](docs/ClockEntryIdsSchema.md)
- [ClockEntrySchema](docs/ClockEntrySchema.md)
- [ClockInRequestSchema](docs/ClockInRequestSchema.md)
- [ClockOutRequestSchema](docs/ClockOutRequestSchema.md)
- [CloseGoalRequest](docs/CloseGoalRequest.md)
- [CompanyAlertDataObject](docs/CompanyAlertDataObject.md)
- [CompanyBenefitSummary](docs/CompanyBenefitSummary.md)
- [CompanyBenefitsListResponse](docs/CompanyBenefitsListResponse.md)
- [CompanyDeletedWebhookPayload](docs/CompanyDeletedWebhookPayload.md)
- [CompanyFileUpdate](docs/CompanyFileUpdate.md)
- [CompanyFilesResponse](docs/CompanyFilesResponse.md)
- [CompanyFilesResponseCategoriesInner](docs/CompanyFilesResponseCategoriesInner.md)
- [CompanyFilesResponseCategoriesInnerFilesInner](docs/CompanyFilesResponseCategoriesInnerFilesInner.md)
- [CompanyIndustryDataObject](docs/CompanyIndustryDataObject.md)
- [CompanyInformation](docs/CompanyInformation.md)
- [CompanyInformationAddress](docs/CompanyInformationAddress.md)
- [CompanyIntegrationsUpdatedWebhookPayload](docs/CompanyIntegrationsUpdatedWebhookPayload.md)
- [CompanyIntegrationsUpdatedWebhookPayloadData](docs/CompanyIntegrationsUpdatedWebhookPayloadData.md)
- [CompanyProfileData](docs/CompanyProfileData.md)
- [CompanyProfileDataAddress](docs/CompanyProfileDataAddress.md)
- [CompanyProfileIntegrations](docs/CompanyProfileIntegrations.md)
- [CompanyUpdatedWebhookPayload](docs/CompanyUpdatedWebhookPayload.md)
- [CompensationBenchmarkDetailEmployee](docs/CompensationBenchmarkDetailEmployee.md)
- [CompensationBenchmarkDetailEmployeeJobTitle](docs/CompensationBenchmarkDetailEmployeeJobTitle.md)
- [CompensationBenchmarkDetailEmployeeSalary](docs/CompensationBenchmarkDetailEmployeeSalary.md)
- [CompensationBenchmarkDetails](docs/CompensationBenchmarkDetails.md)
- [CompensationBenchmarkDetailsBenchmarkValuesInner](docs/CompensationBenchmarkDetailsBenchmarkValuesInner.md)
- [CompensationBenchmarkJobLocationEmployee](docs/CompensationBenchmarkJobLocationEmployee.md)
- [CompensationBenchmarkJobLocationEmployeeSalary](docs/CompensationBenchmarkJobLocationEmployeeSalary.md)
- [CompensationBenchmarkJobLocationPair](docs/CompensationBenchmarkJobLocationPair.md)
- [CompensationBenchmarkJobLocationPairJobDetails](docs/CompensationBenchmarkJobLocationPairJobDetails.md)
- [CompensationBenchmarkOverview](docs/CompensationBenchmarkOverview.md)
- [CompensationBenchmarkOverviewValues](docs/CompensationBenchmarkOverviewValues.md)
- [CompensationBenchmarkSource](docs/CompensationBenchmarkSource.md)
- [CompensationBenchmarkingColumnMap](docs/CompensationBenchmarkingColumnMap.md)
- [CompensationBenchmarksList](docs/CompensationBenchmarksList.md)
- [CompensationEquitySettingsResponse](docs/CompensationEquitySettingsResponse.md)
- [CompensationEquitySettingsResponseCompanyValuation](docs/CompensationEquitySettingsResponseCompanyValuation.md)
- [CompensationEquitySettingsResponseDisclaimers](docs/CompensationEquitySettingsResponseDisclaimers.md)
- [CompensationEquitySettingsResponseOutstandingShares](docs/CompensationEquitySettingsResponseOutstandingShares.md)
- [CompensationEquitySettingsResponsePricePerShare](docs/CompensationEquitySettingsResponsePricePerShare.md)
- [CompensationEquitySettingsResponseSliderMin](docs/CompensationEquitySettingsResponseSliderMin.md)
- [CompensationEquitySettingsResponseVestingConditions](docs/CompensationEquitySettingsResponseVestingConditions.md)
- [CompensationEquitySettingsUpdateRequest](docs/CompensationEquitySettingsUpdateRequest.md)
- [CompensationPlanningCycleAdminsResponse](docs/CompensationPlanningCycleAdminsResponse.md)
- [CompensationPlanningCycleAdminsResponseAdminsInner](docs/CompensationPlanningCycleAdminsResponseAdminsInner.md)
- [CompensationPlanningCycleCompleteResponse](docs/CompensationPlanningCycleCompleteResponse.md)
- [CompensationPlanningCycleCompleteResponseErrorsInner](docs/CompensationPlanningCycleCompleteResponseErrorsInner.md)
- [CompensationToolsDataObject](docs/CompensationToolsDataObject.md)
- [CompensationToolsResponse](docs/CompensationToolsResponse.md)
- [CompensationUpsellData](docs/CompensationUpsellData.md)
- [CompletedQuestionsAndResponseDataObject](docs/CompletedQuestionsAndResponseDataObject.md)
- [ConversionRateDataObject](docs/ConversionRateDataObject.md)
- [CountriesOptionsResponse](docs/CountriesOptionsResponse.md)
- [Country](docs/Country.md)
- [CountrySchema](docs/CountrySchema.md)
- [CreateApplicationCommentRequest](docs/CreateApplicationCommentRequest.md)
- [CreateCandidateResponse](docs/CreateCandidateResponse.md)
- [CreateCommentResponse](docs/CreateCommentResponse.md)
- [CreateCompensationBenchmarkRequest](docs/CreateCompensationBenchmarkRequest.md)
- [CreateCompensationBenchmarkSourceRequest](docs/CreateCompensationBenchmarkSourceRequest.md)
- [CreateEmployeeTrainingRecordRequest](docs/CreateEmployeeTrainingRecordRequest.md)
- [CreateEmployeeTrainingRecordRequestCost](docs/CreateEmployeeTrainingRecordRequestCost.md)
- [CreateGoalCommentRequest](docs/CreateGoalCommentRequest.md)
- [CreateGoalRequest](docs/CreateGoalRequest.md)
- [CreateGoalRequestMilestonesInner](docs/CreateGoalRequestMilestonesInner.md)
- [CreateJobOpeningResponse](docs/CreateJobOpeningResponse.md)
- [CreateLocationRequest](docs/CreateLocationRequest.md)
- [CreateLocationRequestAddress](docs/CreateLocationRequestAddress.md)
- [CreateTrainingCategoryRequest](docs/CreateTrainingCategoryRequest.md)
- [CreateTrainingTypeRequest](docs/CreateTrainingTypeRequest.md)
- [CreateTrainingTypeRequestCategory](docs/CreateTrainingTypeRequestCategory.md)
- [CreateWebhookBadRequestResponse](docs/CreateWebhookBadRequestResponse.md)
- [CreatedCompensationBenchmark](docs/CreatedCompensationBenchmark.md)
- [CreatedCompensationBenchmarkSavedBenchmark](docs/CreatedCompensationBenchmarkSavedBenchmark.md)
- [CreatedCompensationBenchmarkSource](docs/CreatedCompensationBenchmarkSource.md)
- [CreatedTimeOffRequest](docs/CreatedTimeOffRequest.md)
- [CreatedTimeOffRequestAmount](docs/CreatedTimeOffRequestAmount.md)
- [CreatedTimeOffRequestNotes](docs/CreatedTimeOffRequestNotes.md)
- [CreatedTimeOffRequestStatus](docs/CreatedTimeOffRequestStatus.md)
- [CreatedTimeOffRequestType](docs/CreatedTimeOffRequestType.md)
- [CurrencyConversionsResponse](docs/CurrencyConversionsResponse.md)
- [CursorPagedResponseMetadata](docs/CursorPagedResponseMetadata.md)
- [CursorPagesResponse](docs/CursorPagesResponse.md)
- [CursorPaginationQueryObject](docs/CursorPaginationQueryObject.md)
- [Dacd313af2106213fc4696175941ce65Request](docs/Dacd313af2106213fc4696175941ce65Request.md)
- [DataRequest](docs/DataRequest.md)
- [DataRequestAggregations](docs/DataRequestAggregations.md)
- [DataRequestFilters](docs/DataRequestFilters.md)
- [DataRequestFiltersFiltersInner](docs/DataRequestFiltersFiltersInner.md)
- [DataRequestSortByInner](docs/DataRequestSortByInner.md)
- [DatasetDataResponseV2](docs/DatasetDataResponseV2.md)
- [DatasetDataResponseV2DataInner](docs/DatasetDataResponseV2DataInner.md)
- [DatasetDataResponseV2DataInnerFieldsValue](docs/DatasetDataResponseV2DataInnerFieldsValue.md)
- [DatasetDataResponseV2Links](docs/DatasetDataResponseV2Links.md)
- [DatasetDataResponseV2Meta](docs/DatasetDataResponseV2Meta.md)
- [DatasetFieldsResponse](docs/DatasetFieldsResponse.md)
- [DatasetResponseV1](docs/DatasetResponseV1.md)
- [DatasetV1](docs/DatasetV1.md)
- [DatasetsResponseV12](docs/DatasetsResponseV12.md)
- [DatasetsResponseV12DatasetsInner](docs/DatasetsResponseV12DatasetsInner.md)
- [DeleteCompensationBenchmarkSourceRequest](docs/DeleteCompensationBenchmarkSourceRequest.md)
- [DeleteCompensationBenchmarkSourceResponse](docs/DeleteCompensationBenchmarkSourceResponse.md)
- [DetailsAndCurrencyRequestDataObject](docs/DetailsAndCurrencyRequestDataObject.md)
- [Ec1ba8e76f33960b018d0d7518fe97b5Request](docs/Ec1ba8e76f33960b018d0d7518fe97b5Request.md)
- [Employee](docs/Employee.md)
- [EmployeeBenefitFilters](docs/EmployeeBenefitFilters.md)
- [EmployeeBenefitFiltersFilters](docs/EmployeeBenefitFiltersFilters.md)
- [EmployeeBenefitsListResponse](docs/EmployeeBenefitsListResponse.md)
- [EmployeeBenefitsListResponseEmployeeBenefitsInner](docs/EmployeeBenefitsListResponseEmployeeBenefitsInner.md)
- [EmployeeBenefitsListResponseEmployeeBenefitsInnerEmployeeBenefitInner](docs/EmployeeBenefitsListResponseEmployeeBenefitsInnerEmployeeBenefitInner.md)
- [EmployeeCreatedWebhookPayload](docs/EmployeeCreatedWebhookPayload.md)
- [EmployeeCreatedWebhookPayloadData](docs/EmployeeCreatedWebhookPayloadData.md)
- [EmployeeCursorPaginationQueryObject](docs/EmployeeCursorPaginationQueryObject.md)
- [EmployeeDeletedWebhookPayload](docs/EmployeeDeletedWebhookPayload.md)
- [EmployeeDeletedWebhookPayloadData](docs/EmployeeDeletedWebhookPayloadData.md)
- [EmployeeDependent](docs/EmployeeDependent.md)
- [EmployeeDependentsResponse](docs/EmployeeDependentsResponse.md)
- [EmployeeDependentsResponseEmployeeDependentsInner](docs/EmployeeDependentsResponseEmployeeDependentsInner.md)
- [EmployeeFileUpdate](docs/EmployeeFileUpdate.md)
- [EmployeeOptionalField](docs/EmployeeOptionalField.md)
- [EmployeePhotoJsonResponse](docs/EmployeePhotoJsonResponse.md)
- [EmployeeResponse](docs/EmployeeResponse.md)
- [EmployeeResponseAggregationsInner](docs/EmployeeResponseAggregationsInner.md)
- [EmployeeStringCodeErrorResponseV1](docs/EmployeeStringCodeErrorResponseV1.md)
- [EmployeeStringCodeErrorResponseV1Error](docs/EmployeeStringCodeErrorResponseV1Error.md)
- [EmployeeTableRow](docs/EmployeeTableRow.md)
- [EmployeeTimeOffPolicyAssignment](docs/EmployeeTimeOffPolicyAssignment.md)
- [EmployeeTimeOffPolicyAssignmentV11](docs/EmployeeTimeOffPolicyAssignmentV11.md)
- [EmployeeTimeOffRequestApproverResponseInner](docs/EmployeeTimeOffRequestApproverResponseInner.md)
- [EmployeeTimesheetEntryTransformer](docs/EmployeeTimesheetEntryTransformer.md)
- [EmployeeUpdatedWebhookPayload](docs/EmployeeUpdatedWebhookPayload.md)
- [EmployeeUpdatedWebhookPayloadData](docs/EmployeeUpdatedWebhookPayloadData.md)
- [EmployeeValue](docs/EmployeeValue.md)
- [EmployeeValueAnyOfInner](docs/EmployeeValueAnyOfInner.md)
- [EmployeeVerificationIntegration](docs/EmployeeVerificationIntegration.md)
- [EmployeeVerificationIntegrationResponse](docs/EmployeeVerificationIntegrationResponse.md)
- [EmployeeVerificationLifecycleEmailAcceptedResponse](docs/EmployeeVerificationLifecycleEmailAcceptedResponse.md)
- [EmployeeVerificationPublicApiRecord](docs/EmployeeVerificationPublicApiRecord.md)
- [EmployeeVerificationUpdateResponse](docs/EmployeeVerificationUpdateResponse.md)
- [EmployeeVerificationsListResponse](docs/EmployeeVerificationsListResponse.md)
- [EmployeesDirectoryJsonResponse](docs/EmployeesDirectoryJsonResponse.md)
- [EmployeesDirectoryJsonResponseFieldsInner](docs/EmployeesDirectoryJsonResponseFieldsInner.md)
- [EmployeesDirectoryXmlResponse](docs/EmployeesDirectoryXmlResponse.md)
- [EmployeesDirectoryXmlResponseEmployees](docs/EmployeesDirectoryXmlResponseEmployees.md)
- [EmployeesDirectoryXmlResponseEmployeesEmployeeInner](docs/EmployeesDirectoryXmlResponseEmployeesEmployeeInner.md)
- [EmployeesDirectoryXmlResponseEmployeesEmployeeInnerFieldInner](docs/EmployeesDirectoryXmlResponseEmployeesEmployeeInnerFieldInner.md)
- [EmployeesDirectoryXmlResponseFieldset](docs/EmployeesDirectoryXmlResponseFieldset.md)
- [EmployeesDirectoryXmlResponseFieldsetFieldInner](docs/EmployeesDirectoryXmlResponseFieldsetFieldInner.md)
- [ErrorResponse](docs/ErrorResponse.md)
- [ErrorResponseError](docs/ErrorResponseError.md)
- [F3883a522dadbe9e11b34f8b656e3adbRequest](docs/F3883a522dadbe9e11b34f8b656e3adbRequest.md)
- [Field1](docs/Field1.md)
- [Field1Id](docs/Field1Id.md)
- [FieldOptionsRequestSchema](docs/FieldOptionsRequestSchema.md)
- [FieldOptionsRequestSchemaDependentFieldsValueInner](docs/FieldOptionsRequestSchemaDependentFieldsValueInner.md)
- [FieldOptionsTransformer](docs/FieldOptionsTransformer.md)
- [FieldOptionsTransformerId](docs/FieldOptionsTransformerId.md)
- [ForbiddenV1](docs/ForbiddenV1.md)
- [ForbiddenV1Error](docs/ForbiddenV1Error.md)
- [GetBreakPolicySuggestionsRequest](docs/GetBreakPolicySuggestionsRequest.md)
- [GetCompanyReportResponse](docs/GetCompanyReportResponse.md)
- [GetCompanyReportResponseEmployeesInner](docs/GetCompanyReportResponseEmployeesInner.md)
- [GetDataFromDatasetV2Request](docs/GetDataFromDatasetV2Request.md)
- [GetEmployeeResponse](docs/GetEmployeeResponse.md)
- [GetEmployeesEmployeeBaseResponse](docs/GetEmployeesEmployeeBaseResponse.md)
- [GetEmployeesEmployeeResponse](docs/GetEmployeesEmployeeResponse.md)
- [GetEmployeesEmployeeResponseAllOfOvertimeRate](docs/GetEmployeesEmployeeResponseAllOfOvertimeRate.md)
- [GetEmployeesEmployeeResponseAllOfPayRate](docs/GetEmployeesEmployeeResponseAllOfPayRate.md)
- [GetEmployeesEmployeeResponseAllOfTeams](docs/GetEmployeesEmployeeResponseAllOfTeams.md)
- [GetEmployeesFilterRequestObject](docs/GetEmployeesFilterRequestObject.md)
- [GetEmployeesResponseObject](docs/GetEmployeesResponseObject.md)
- [GetEmployeesResponseObjectLinks](docs/GetEmployeesResponseObjectLinks.md)
- [GetEmployeesResponseObjectLinksNext](docs/GetEmployeesResponseObjectLinksNext.md)
- [GetEmployeesResponseObjectLinksPrev](docs/GetEmployeesResponseObjectLinksPrev.md)
- [GetEmployeesResponseObjectLinksSelf](docs/GetEmployeesResponseObjectLinksSelf.md)
- [GoalAggregate](docs/GoalAggregate.md)
- [GoalAggregateAlignsWithOptionsInner](docs/GoalAggregateAlignsWithOptionsInner.md)
- [GoalAggregateCommentsInner](docs/GoalAggregateCommentsInner.md)
- [GoalAggregatePersonsInner](docs/GoalAggregatePersonsInner.md)
- [GoalCommentResponse](docs/GoalCommentResponse.md)
- [GoalCommentsResponse](docs/GoalCommentsResponse.md)
- [GoalCommentsResponseCommentsInner](docs/GoalCommentsResponseCommentsInner.md)
- [GoalFiltersV1](docs/GoalFiltersV1.md)
- [GoalFiltersV11](docs/GoalFiltersV11.md)
- [GoalFiltersV11FiltersInner](docs/GoalFiltersV11FiltersInner.md)
- [GoalFiltersV11FiltersInnerActions](docs/GoalFiltersV11FiltersInnerActions.md)
- [GoalFiltersV1FiltersInner](docs/GoalFiltersV1FiltersInner.md)
- [GoalResponse](docs/GoalResponse.md)
- [GoalsAggregateV1](docs/GoalsAggregateV1.md)
- [GoalsAggregateV11](docs/GoalsAggregateV11.md)
- [GoalsAggregateV11CommentsInner](docs/GoalsAggregateV11CommentsInner.md)
- [GoalsAggregateV12](docs/GoalsAggregateV12.md)
- [GoalsAggregateV12CommentsInner](docs/GoalsAggregateV12CommentsInner.md)
- [GoalsAggregateV1CommentsInner](docs/GoalsAggregateV1CommentsInner.md)
- [GoalsAggregateV1PersonsInner](docs/GoalsAggregateV1PersonsInner.md)
- [GoalsList](docs/GoalsList.md)
- [HiringLead](docs/HiringLead.md)
- [HourEntriesRequestSchema](docs/HourEntriesRequestSchema.md)
- [HourEntryIdsSchema](docs/HourEntryIdsSchema.md)
- [HourEntrySchema](docs/HourEntrySchema.md)
- [ImportCompensationBenchmarksResponse](docs/ImportCompensationBenchmarksResponse.md)
- [Industry](docs/Industry.md)
- [InlineObjectInner](docs/InlineObjectInner.md)
- [JobSummary](docs/JobSummary.md)
- [JobSummaryStatus](docs/JobSummaryStatus.md)
- [JsonEmployeeFiles](docs/JsonEmployeeFiles.md)
- [JsonEmployeeFilesCategoriesInner](docs/JsonEmployeeFilesCategoriesInner.md)
- [JsonEmployeeFilesCategoriesInnerFilesInner](docs/JsonEmployeeFilesCategoriesInnerFilesInner.md)
- [JsonEmployeeFilesEmployee](docs/JsonEmployeeFilesEmployee.md)
- [LevelsAndBandsColumnMap](docs/LevelsAndBandsColumnMap.md)
- [LevelsAndBandsEmployee](docs/LevelsAndBandsEmployee.md)
- [LevelsAndBandsErrorWarningIdentifier](docs/LevelsAndBandsErrorWarningIdentifier.md)
- [LevelsAndBandsGroup](docs/LevelsAndBandsGroup.md)
- [LevelsAndBandsGroupStatusCounts](docs/LevelsAndBandsGroupStatusCounts.md)
- [LevelsAndBandsJobTitle](docs/LevelsAndBandsJobTitle.md)
- [LevelsAndBandsJobTitleAssignment](docs/LevelsAndBandsJobTitleAssignment.md)
- [LevelsAndBandsJobTitleAssignmentsRequest](docs/LevelsAndBandsJobTitleAssignmentsRequest.md)
- [LevelsAndBandsJobTitleWithEmployees](docs/LevelsAndBandsJobTitleWithEmployees.md)
- [LevelsAndBandsJobTitlesStatus](docs/LevelsAndBandsJobTitlesStatus.md)
- [LevelsAndBandsLevel](docs/LevelsAndBandsLevel.md)
- [LevelsAndBandsLevelsAndBands](docs/LevelsAndBandsLevelsAndBands.md)
- [LevelsAndBandsLevelsAndBandsStatus](docs/LevelsAndBandsLevelsAndBandsStatus.md)
- [LevelsAndBandsPayBand](docs/LevelsAndBandsPayBand.md)
- [LevelsAndBandsStepStatus](docs/LevelsAndBandsStepStatus.md)
- [LevelsAndBandsUploadResponse](docs/LevelsAndBandsUploadResponse.md)
- [ListFieldDetail](docs/ListFieldDetail.md)
- [ListFieldOption](docs/ListFieldOption.md)
- [ListFieldValues](docs/ListFieldValues.md)
- [ListFieldValuesOptionsInner](docs/ListFieldValuesOptionsInner.md)
- [ListFieldValuesXml](docs/ListFieldValuesXml.md)
- [ListFieldValuesXmlOptionInner](docs/ListFieldValuesXmlOptionInner.md)
- [ListUsersResponseValue](docs/ListUsersResponseValue.md)
- [ListUsersXmlResponse](docs/ListUsersXmlResponse.md)
- [ListUsersXmlResponseUserInner](docs/ListUsersXmlResponseUserInner.md)
- [Location](docs/Location.md)
- [LocationResponseObject](docs/LocationResponseObject.md)
- [LocationResponseObjectAddress](docs/LocationResponseObjectAddress.md)
- [LocationResponseObjectAddressCountry](docs/LocationResponseObjectAddressCountry.md)
- [LocationResponseObjectAddressState](docs/LocationResponseObjectAddressState.md)
- [LoginFailureResponse](docs/LoginFailureResponse.md)
- [LoginFailureXmlResponse](docs/LoginFailureXmlResponse.md)
- [LoginResponse](docs/LoginResponse.md)
- [LoginXmlResponse](docs/LoginXmlResponse.md)
- [MemberBenefitEvent](docs/MemberBenefitEvent.md)
- [MemberBenefitEventCoveragesInner](docs/MemberBenefitEventCoveragesInner.md)
- [MemberBenefitEventCoveragesInnerEventsInner](docs/MemberBenefitEventCoveragesInnerEventsInner.md)
- [MemberBenefitEventsResponse](docs/MemberBenefitEventsResponse.md)
- [MemberBenefitsGetPermissionDeniedResponse](docs/MemberBenefitsGetPermissionDeniedResponse.md)
- [MemberBenefitsGetSuccessResponse](docs/MemberBenefitsGetSuccessResponse.md)
- [MemberBenefitsGetSuccessResponseDataInner](docs/MemberBenefitsGetSuccessResponseDataInner.md)
- [MemberBenefitsGetSuccessResponseDataInnerPlansInner](docs/MemberBenefitsGetSuccessResponseDataInnerPlansInner.md)
- [MemberBenefitsGetSuccessResponseDataInnerPlansInnerDateRangesInner](docs/MemberBenefitsGetSuccessResponseDataInnerPlansInnerDateRangesInner.md)
- [MemberBenefitsGetSuccessResponseLinks](docs/MemberBenefitsGetSuccessResponseLinks.md)
- [MemberBenefitsGetSuccessResponseLinksNext](docs/MemberBenefitsGetSuccessResponseLinksNext.md)
- [MemberBenefitsGetSuccessResponseLinksPrev](docs/MemberBenefitsGetSuccessResponseLinksPrev.md)
- [MemberBenefitsGetSuccessResponseMeta](docs/MemberBenefitsGetSuccessResponseMeta.md)
- [MemberBenefitsGetValidationErrorResponse](docs/MemberBenefitsGetValidationErrorResponse.md)
- [MetaCompanyPropertiesResponse](docs/MetaCompanyPropertiesResponse.md)
- [MetaCurrencyTypeItem](docs/MetaCurrencyTypeItem.md)
- [Model1d1fc0f164cb51973a0206b8e2fb2d2dRequest](docs/Model1d1fc0f164cb51973a0206b8e2fb2d2dRequest.md)
- [Model1d1fc0f164cb51973a0206b8e2fb2d2dRequestBudgetBreakdownInner](docs/Model1d1fc0f164cb51973a0206b8e2fb2d2dRequestBudgetBreakdownInner.md)
- [Model1d64402ee192568adbd5e3179a91e6e2RequestInner](docs/Model1d64402ee192568adbd5e3179a91e6e2RequestInner.md)
- [Model1d64402ee192568adbd5e3179a91e6e2RequestInnerBudgetAllocations](docs/Model1d64402ee192568adbd5e3179a91e6e2RequestInnerBudgetAllocations.md)
- [Model288aa996aba16d7a495c62321ea999a9Request](docs/Model288aa996aba16d7a495c62321ea999a9Request.md)
- [Model288aa996aba16d7a495c62321ea999a9RequestSentDateTime](docs/Model288aa996aba16d7a495c62321ea999a9RequestSentDateTime.md)
- [Model3958585c861325ea7a2cd30a8c74f042Request](docs/Model3958585c861325ea7a2cd30a8c74f042Request.md)
- [Model89a5068111ec499135c7d6e9a53d5a30Request](docs/Model89a5068111ec499135c7d6e9a53d5a30Request.md)
- [ModelField](docs/ModelField.md)
- [MonitorFieldList](docs/MonitorFieldList.md)
- [MonitorFieldListFieldsInner](docs/MonitorFieldListFieldsInner.md)
- [NewHirePacketGtkyAnswerVisibilityItem](docs/NewHirePacketGtkyAnswerVisibilityItem.md)
- [NewHirePacketGtkyAnswerVisibilityRequest](docs/NewHirePacketGtkyAnswerVisibilityRequest.md)
- [NewHirePacketGtkyAnswerVisibilityResponse](docs/NewHirePacketGtkyAnswerVisibilityResponse.md)
- [NewHirePacketPublicApi](docs/NewHirePacketPublicApi.md)
- [NewHirePacketPublicApiWritableBody](docs/NewHirePacketPublicApiWritableBody.md)
- [NewHirePacketsListResponse](docs/NewHirePacketsListResponse.md)
- [NewHireWidgetItem](docs/NewHireWidgetItem.md)
- [NewHireWidgetResponse](docs/NewHireWidgetResponse.md)
- [NewWebHook](docs/NewWebHook.md)
- [OnboardingExperiencePublicApi](docs/OnboardingExperiencePublicApi.md)
- [OnboardingExperiencesListResponse](docs/OnboardingExperiencesListResponse.md)
- [PagedLocationResponse](docs/PagedLocationResponse.md)
- [PagedResponse](docs/PagedResponse.md)
- [Pagination](docs/Pagination.md)
- [PaginationMetaData](docs/PaginationMetaData.md)
- [PatchCompanyProfileCompanyInformationRequest](docs/PatchCompanyProfileCompanyInformationRequest.md)
- [PatchCompanyProfileCompanyInformationRequestAddress](docs/PatchCompanyProfileCompanyInformationRequestAddress.md)
- [PayGradesAndBandsPublishResponse](docs/PayGradesAndBandsPublishResponse.md)
- [PayGradesAndBandsSaveLevelsResponse](docs/PayGradesAndBandsSaveLevelsResponse.md)
- [PayGradesAndBandsUpdateJobTitlesResponse](docs/PayGradesAndBandsUpdateJobTitlesResponse.md)
- [PayGradesAndBandsUpdatePayBandsResponse](docs/PayGradesAndBandsUpdatePayBandsResponse.md)
- [PersonInfoApiTransformer](docs/PersonInfoApiTransformer.md)
- [PostNewEmployee](docs/PostNewEmployee.md)
- [ProblemDetailsResponse](docs/ProblemDetailsResponse.md)
- [ProjectCreateRequestSchema](docs/ProjectCreateRequestSchema.md)
- [ProjectCreateTimeTrackingProjectTaskV1](docs/ProjectCreateTimeTrackingProjectTaskV1.md)
- [ProjectCreateTimeTrackingProjectV1](docs/ProjectCreateTimeTrackingProjectV1.md)
- [ProjectCreateTimeTrackingProjectV1TasksInner](docs/ProjectCreateTimeTrackingProjectV1TasksInner.md)
- [ProjectInfoApiTransformer](docs/ProjectInfoApiTransformer.md)
- [ProjectInfoApiTransformerProject](docs/ProjectInfoApiTransformerProject.md)
- [ProjectPaginatedResponseDataV1](docs/ProjectPaginatedResponseDataV1.md)
- [ProjectPaginatedResponseDataV1Links](docs/ProjectPaginatedResponseDataV1Links.md)
- [ProjectPaginatedResponseDataV1LinksNext](docs/ProjectPaginatedResponseDataV1LinksNext.md)
- [ProjectPaginatedResponseDataV1LinksPrev](docs/ProjectPaginatedResponseDataV1LinksPrev.md)
- [ProjectPaginatedResponseDataV1Meta](docs/ProjectPaginatedResponseDataV1Meta.md)
- [ProjectPaginatedTasksResponseV1](docs/ProjectPaginatedTasksResponseV1.md)
- [ProjectPaginatedTasksResponseV1Links](docs/ProjectPaginatedTasksResponseV1Links.md)
- [ProjectPaginatedTasksResponseV1Meta](docs/ProjectPaginatedTasksResponseV1Meta.md)
- [ProjectPaginatedTimeTrackingProjectsResponseV1](docs/ProjectPaginatedTimeTrackingProjectsResponseV1.md)
- [ProjectTimeTrackingProjectV1](docs/ProjectTimeTrackingProjectV1.md)
- [ProjectTimeTrackingTaskV1](docs/ProjectTimeTrackingTaskV1.md)
- [ProjectUpdateTimeTrackingProjectTaskV1](docs/ProjectUpdateTimeTrackingProjectTaskV1.md)
- [ProjectUpdateTimeTrackingProjectV1](docs/ProjectUpdateTimeTrackingProjectV1.md)
- [ProvinceItem](docs/ProvinceItem.md)
- [PutCompanyIndustryCodesRequest](docs/PutCompanyIndustryCodesRequest.md)
- [PutCompanyProfileDisplayNameRequest](docs/PutCompanyProfileDisplayNameRequest.md)
- [RemoveCycleAdminSelfResponse](docs/RemoveCycleAdminSelfResponse.md)
- [RemoveTotalRewardsEmployeesRequest](docs/RemoveTotalRewardsEmployeesRequest.md)
- [Report](docs/Report.md)
- [ReportsResponse](docs/ReportsResponse.md)
- [Request](docs/Request.md)
- [RequestCustomReport](docs/RequestCustomReport.md)
- [RequestCustomReportFilters](docs/RequestCustomReportFilters.md)
- [RequestCustomReportFiltersLastChanged](docs/RequestCustomReportFiltersLastChanged.md)
- [RequestCustomReportResponse](docs/RequestCustomReportResponse.md)
- [RequestCustomReportResponseEmployeesInner](docs/RequestCustomReportResponseEmployeesInner.md)
- [RequestCustomReportResponseFieldsInner](docs/RequestCustomReportResponseFieldsInner.md)
- [SaveChangeCommTemplateResponse](docs/SaveChangeCommTemplateResponse.md)
- [SchedulingCreateScheduleRequestV1](docs/SchedulingCreateScheduleRequestV1.md)
- [SchedulingCreateSchedulingShiftRequestV1](docs/SchedulingCreateSchedulingShiftRequestV1.md)
- [SchedulingPublishShiftsFailureV1](docs/SchedulingPublishShiftsFailureV1.md)
- [SchedulingPublishShiftsRequest](docs/SchedulingPublishShiftsRequest.md)
- [SchedulingPublishShiftsResultV1](docs/SchedulingPublishShiftsResultV1.md)
- [SchedulingScheduleListResponseV1](docs/SchedulingScheduleListResponseV1.md)
- [SchedulingScheduleListResponseV1Links](docs/SchedulingScheduleListResponseV1Links.md)
- [SchedulingScheduleListResponseV1Meta](docs/SchedulingScheduleListResponseV1Meta.md)
- [SchedulingScheduleV1](docs/SchedulingScheduleV1.md)
- [SchedulingSchedulingShiftV1](docs/SchedulingSchedulingShiftV1.md)
- [SchedulingShiftListResponseV1](docs/SchedulingShiftListResponseV1.md)
- [SchedulingShiftListResponseV1Links](docs/SchedulingShiftListResponseV1Links.md)
- [SchedulingShiftListResponseV1LinksNext](docs/SchedulingShiftListResponseV1LinksNext.md)
- [SchedulingShiftListResponseV1LinksPrev](docs/SchedulingShiftListResponseV1LinksPrev.md)
- [SchedulingShiftListResponseV1Meta](docs/SchedulingShiftListResponseV1Meta.md)
- [SchedulingTimezoneListResponseV1](docs/SchedulingTimezoneListResponseV1.md)
- [SchedulingTimezoneListResponseV1Meta](docs/SchedulingTimezoneListResponseV1Meta.md)
- [SchedulingTimezoneV1](docs/SchedulingTimezoneV1.md)
- [SchedulingUpdateScheduleRequestV1](docs/SchedulingUpdateScheduleRequestV1.md)
- [SchedulingUpdateSchedulingShiftRequestV1](docs/SchedulingUpdateSchedulingShiftRequestV1.md)
- [SendEmployeeVerificationLifecycleEmailByUserRequest](docs/SendEmployeeVerificationLifecycleEmailByUserRequest.md)
- [SendRecommendationsResponse](docs/SendRecommendationsResponse.md)
- [SetBreakPolicyEmployeesRequest](docs/SetBreakPolicyEmployeesRequest.md)
- [SetTotalRewardsCustomDisclaimerRequest](docs/SetTotalRewardsCustomDisclaimerRequest.md)
- [SetTotalRewardsOnboardingStepRequest](docs/SetTotalRewardsOnboardingStepRequest.md)
- [ShareOptionsResponse](docs/ShareOptionsResponse.md)
- [State](docs/State.md)
- [StateProvinceResponseSchema](docs/StateProvinceResponseSchema.md)
- [StateProvinceSchema](docs/StateProvinceSchema.md)
- [TableRowDeleteResponse](docs/TableRowDeleteResponse.md)
- [TableRowUpdate](docs/TableRowUpdate.md)
- [TabularField](docs/TabularField.md)
- [TabularFieldFieldsInner](docs/TabularFieldFieldsInner.md)
- [TaskCreateSchema](docs/TaskCreateSchema.md)
- [TimeOffBalanceEntry](docs/TimeOffBalanceEntry.md)
- [TimeOffHistory](docs/TimeOffHistory.md)
- [TimeOffPolicy](docs/TimeOffPolicy.md)
- [TimeOffRequest](docs/TimeOffRequest.md)
- [TimeOffRequest1](docs/TimeOffRequest1.md)
- [TimeOffRequest1Actions](docs/TimeOffRequest1Actions.md)
- [TimeOffRequest1Amount](docs/TimeOffRequest1Amount.md)
- [TimeOffRequest1Notes](docs/TimeOffRequest1Notes.md)
- [TimeOffRequest1Status](docs/TimeOffRequest1Status.md)
- [TimeOffRequest1Type](docs/TimeOffRequest1Type.md)
- [TimeOffRequestDatesInner](docs/TimeOffRequestDatesInner.md)
- [TimeOffRequestNotesInner](docs/TimeOffRequestNotesInner.md)
- [TimeOffTypesAndDefaultHours](docs/TimeOffTypesAndDefaultHours.md)
- [TimeOffTypesAndDefaultHoursDefaultHoursInner](docs/TimeOffTypesAndDefaultHoursDefaultHoursInner.md)
- [TimeOffTypesAndDefaultHoursTimeOffTypesInner](docs/TimeOffTypesAndDefaultHoursTimeOffTypesInner.md)
- [TimeTrackingBreakPolicyEmployeeCollectionV1Inner](docs/TimeTrackingBreakPolicyEmployeeCollectionV1Inner.md)
- [TimeTrackingBreakPolicySuggestionsResponseV1](docs/TimeTrackingBreakPolicySuggestionsResponseV1.md)
- [TimeTrackingBreakPolicySuggestionsResponseV1SuggestedPoliciesInner](docs/TimeTrackingBreakPolicySuggestionsResponseV1SuggestedPoliciesInner.md)
- [TimeTrackingBreakPolicySuggestionsResponseV1SuggestedPoliciesInnerBreaksInner](docs/TimeTrackingBreakPolicySuggestionsResponseV1SuggestedPoliciesInnerBreaksInner.md)
- [TimeTrackingBulkResponseSchema](docs/TimeTrackingBulkResponseSchema.md)
- [TimeTrackingBulkResponseSchemaResponse](docs/TimeTrackingBulkResponseSchemaResponse.md)
- [TimeTrackingCreateOrUpdateTimeTrackingBreakWithoutPolicyV1](docs/TimeTrackingCreateOrUpdateTimeTrackingBreakWithoutPolicyV1.md)
- [TimeTrackingCreateTimeTrackingBreakPolicyV1](docs/TimeTrackingCreateTimeTrackingBreakPolicyV1.md)
- [TimeTrackingCreateTimeTrackingBreakV1](docs/TimeTrackingCreateTimeTrackingBreakV1.md)
- [TimeTrackingDeleteResponseSchema](docs/TimeTrackingDeleteResponseSchema.md)
- [TimeTrackingIdResponseSchema](docs/TimeTrackingIdResponseSchema.md)
- [TimeTrackingOffsetPaginatedResponseDataV1](docs/TimeTrackingOffsetPaginatedResponseDataV1.md)
- [TimeTrackingOffsetPaginatedResponseDataV1Links](docs/TimeTrackingOffsetPaginatedResponseDataV1Links.md)
- [TimeTrackingOffsetPaginatedResponseDataV1Meta](docs/TimeTrackingOffsetPaginatedResponseDataV1Meta.md)
- [TimeTrackingPaginatedBreakAssessmentsResponseV1](docs/TimeTrackingPaginatedBreakAssessmentsResponseV1.md)
- [TimeTrackingPaginatedBreakPoliciesResponseV1](docs/TimeTrackingPaginatedBreakPoliciesResponseV1.md)
- [TimeTrackingPaginatedBreakPolicyEmployeesResponseV1](docs/TimeTrackingPaginatedBreakPolicyEmployeesResponseV1.md)
- [TimeTrackingPaginatedBreaksResponseV1](docs/TimeTrackingPaginatedBreaksResponseV1.md)
- [TimeTrackingProjectWithTasksAndEmployeeIds](docs/TimeTrackingProjectWithTasksAndEmployeeIds.md)
- [TimeTrackingRecord](docs/TimeTrackingRecord.md)
- [TimeTrackingRecordSchema](docs/TimeTrackingRecordSchema.md)
- [TimeTrackingSyncTimeTrackingBreakPolicyV1](docs/TimeTrackingSyncTimeTrackingBreakPolicyV1.md)
- [TimeTrackingTask](docs/TimeTrackingTask.md)
- [TimeTrackingTimeTrackingBreakAssessmentV1](docs/TimeTrackingTimeTrackingBreakAssessmentV1.md)
- [TimeTrackingTimeTrackingBreakAssessmentViolationV1](docs/TimeTrackingTimeTrackingBreakAssessmentViolationV1.md)
- [TimeTrackingTimeTrackingBreakAvailabilityV1](docs/TimeTrackingTimeTrackingBreakAvailabilityV1.md)
- [TimeTrackingTimeTrackingBreakPolicyV1](docs/TimeTrackingTimeTrackingBreakPolicyV1.md)
- [TimeTrackingTimeTrackingBreakPolicyWithRelationsV1](docs/TimeTrackingTimeTrackingBreakPolicyWithRelationsV1.md)
- [TimeTrackingTimeTrackingBreakV1](docs/TimeTrackingTimeTrackingBreakV1.md)
- [TimeTrackingUpdateTimeTrackingBreakPolicyV1](docs/TimeTrackingUpdateTimeTrackingBreakPolicyV1.md)
- [TimeTrackingUpdateTimeTrackingBreakV1](docs/TimeTrackingUpdateTimeTrackingBreakV1.md)
- [TimesheetEntryInfoApiTransformer](docs/TimesheetEntryInfoApiTransformer.md)
- [TimezoneListResponse](docs/TimezoneListResponse.md)
- [TimezoneResource](docs/TimezoneResource.md)
- [TotalRewardsBenefitDetailsValues](docs/TotalRewardsBenefitDetailsValues.md)
- [TotalRewardsBenefitSectionValues](docs/TotalRewardsBenefitSectionValues.md)
- [TotalRewardsCalendarSectionValues](docs/TotalRewardsCalendarSectionValues.md)
- [TotalRewardsCompSummaryValues](docs/TotalRewardsCompSummaryValues.md)
- [TotalRewardsCustomDisclaimerInfo](docs/TotalRewardsCustomDisclaimerInfo.md)
- [TotalRewardsEmployeeStatement](docs/TotalRewardsEmployeeStatement.md)
- [TotalRewardsEquityDetailsValues](docs/TotalRewardsEquityDetailsValues.md)
- [TotalRewardsEquityEstimatedValuationValues](docs/TotalRewardsEquityEstimatedValuationValues.md)
- [TotalRewardsEquityGrowthChartItem](docs/TotalRewardsEquityGrowthChartItem.md)
- [TotalRewardsEquityGrowthEstimation](docs/TotalRewardsEquityGrowthEstimation.md)
- [TotalRewardsEquitySectionValues](docs/TotalRewardsEquitySectionValues.md)
- [TotalRewardsExtraPayDetailsValues](docs/TotalRewardsExtraPayDetailsValues.md)
- [TotalRewardsExtraPaySectionValues](docs/TotalRewardsExtraPaySectionValues.md)
- [TotalRewardsHolidayValue](docs/TotalRewardsHolidayValue.md)
- [TotalRewardsOnboardingStep](docs/TotalRewardsOnboardingStep.md)
- [TotalRewardsOverviewSectionValues](docs/TotalRewardsOverviewSectionValues.md)
- [TotalRewardsTimeOffPolicyValue](docs/TotalRewardsTimeOffPolicyValue.md)
- [TotalRewardsTimelineItem](docs/TotalRewardsTimelineItem.md)
- [TotalRewardsTimelineItemLabel](docs/TotalRewardsTimelineItemLabel.md)
- [TotalRewardsTimelineSectionValues](docs/TotalRewardsTimelineSectionValues.md)
- [TrainingCategory](docs/TrainingCategory.md)
- [TrainingRecord](docs/TrainingRecord.md)
- [TrainingRecordMap](docs/TrainingRecordMap.md)
- [TrainingRecordType](docs/TrainingRecordType.md)
- [TrainingType](docs/TrainingType.md)
- [TrainingTypeCategory](docs/TrainingTypeCategory.md)
- [TransformedApiEmployeeGoalDetails](docs/TransformedApiEmployeeGoalDetails.md)
- [TransformedApiEmployeeGoalDetailsGoal](docs/TransformedApiEmployeeGoalDetailsGoal.md)
- [TransformedApiGoal](docs/TransformedApiGoal.md)
- [TransformedApiGoalMilestonesInner](docs/TransformedApiGoalMilestonesInner.md)
- [UnassignEmployeesFromBreakPolicyRequest](docs/UnassignEmployeesFromBreakPolicyRequest.md)
- [UpdateApplicantStatusRequest](docs/UpdateApplicantStatusRequest.md)
- [UpdateApplicantStatusResponse](docs/UpdateApplicantStatusResponse.md)
- [UpdateCompanyIndustryCodes400Response](docs/UpdateCompanyIndustryCodes400Response.md)
- [UpdateCompanyIndustryCodes403Response](docs/UpdateCompanyIndustryCodes403Response.md)
- [UpdateCompanyIndustryCodes404Response](docs/UpdateCompanyIndustryCodes404Response.md)
- [UpdateCompanyIndustryCodes500Response](docs/UpdateCompanyIndustryCodes500Response.md)
- [UpdateCompanyIndustryCodesResponse](docs/UpdateCompanyIndustryCodesResponse.md)
- [UpdateCompanyNameBadRequestResponse](docs/UpdateCompanyNameBadRequestResponse.md)
- [UpdateCompanyNameBadRequestResponseError](docs/UpdateCompanyNameBadRequestResponseError.md)
- [UpdateCompanyNameForbiddenResponse](docs/UpdateCompanyNameForbiddenResponse.md)
- [UpdateCompanyNameForbiddenResponseError](docs/UpdateCompanyNameForbiddenResponseError.md)
- [UpdateCompanyNameInternalErrorResponse](docs/UpdateCompanyNameInternalErrorResponse.md)
- [UpdateCompanyNameSuccessResponse](docs/UpdateCompanyNameSuccessResponse.md)
- [UpdateCompensationBenchmarkRequest](docs/UpdateCompensationBenchmarkRequest.md)
- [UpdateCompensationBenchmarkSourceItem](docs/UpdateCompensationBenchmarkSourceItem.md)
- [UpdateCompensationBenchmarkSourcesRequest](docs/UpdateCompensationBenchmarkSourcesRequest.md)
- [UpdateCompensationBenchmarkSourcesResponse](docs/UpdateCompensationBenchmarkSourcesResponse.md)
- [UpdateEmployeeTrainingRecordRequest](docs/UpdateEmployeeTrainingRecordRequest.md)
- [UpdateEmployeeVerificationIntegrationRequest](docs/UpdateEmployeeVerificationIntegrationRequest.md)
- [UpdateEmployeeVerificationRequest](docs/UpdateEmployeeVerificationRequest.md)
- [UpdateGoalCommentRequest](docs/UpdateGoalCommentRequest.md)
- [UpdateGoalMilestoneProgressRequest](docs/UpdateGoalMilestoneProgressRequest.md)
- [UpdateGoalProgressRequest](docs/UpdateGoalProgressRequest.md)
- [UpdateGoalSharingRequest](docs/UpdateGoalSharingRequest.md)
- [UpdateGoalV1](docs/UpdateGoalV1.md)
- [UpdateGoalV11Request](docs/UpdateGoalV11Request.md)
- [UpdateGoalV11RequestMilestonesInner](docs/UpdateGoalV11RequestMilestonesInner.md)
- [UpdateLocationRequest](docs/UpdateLocationRequest.md)
- [UpdateLocationRequestAddress](docs/UpdateLocationRequestAddress.md)
- [UpdateTrainingCategoryRequest](docs/UpdateTrainingCategoryRequest.md)
- [UpdateTrainingTypeRequest](docs/UpdateTrainingTypeRequest.md)
- [UpdateTrainingTypeRequestCategory](docs/UpdateTrainingTypeRequestCategory.md)
- [UpdateWebhookBadRequestResponse](docs/UpdateWebhookBadRequestResponse.md)
- [UpdatedCompensationBenchmark](docs/UpdatedCompensationBenchmark.md)
- [UpdatedCompensationBenchmarkSavedBenchmark](docs/UpdatedCompensationBenchmarkSavedBenchmark.md)
- [UploadEmployeePhotoRequest1](docs/UploadEmployeePhotoRequest1.md)
- [UserPermissionData](docs/UserPermissionData.md)
- [WebHookPostFieldDataObject](docs/WebHookPostFieldDataObject.md)
- [WebHookPostFieldPageDataObject](docs/WebHookPostFieldPageDataObject.md)
- [WebHookPostFieldResponseObject](docs/WebHookPostFieldResponseObject.md)
- [WebHookPostFieldTableDataObject](docs/WebHookPostFieldTableDataObject.md)
- [WebHookResponse](docs/WebHookResponse.md)
- [Webhook](docs/Webhook.md)
- [WebhookBadRequest](docs/WebhookBadRequest.md)
- [WebhookBadRequestErrorsInner](docs/WebhookBadRequestErrorsInner.md)
- [WebhookError](docs/WebhookError.md)
- [WebhookErrorErrors](docs/WebhookErrorErrors.md)
- [WebhookEventType](docs/WebhookEventType.md)
- [WebhookLogEntry](docs/WebhookLogEntry.md)
- [WebhookLogListResponse](docs/WebhookLogListResponse.md)
- [WebhookLogRateLimitResponse](docs/WebhookLogRateLimitResponse.md)
- [WebhookLogRateLimitResponseError](docs/WebhookLogRateLimitResponseError.md)
- [WebhookSubErrorProperty](docs/WebhookSubErrorProperty.md)
- [WebhookSubErrorPropertyMonitorFieldsInner](docs/WebhookSubErrorPropertyMonitorFieldsInner.md)
- [WebhookSubErrorPropertyMonitorFieldsInnerId](docs/WebhookSubErrorPropertyMonitorFieldsInnerId.md)
- [WebhookSubErrorPropertyUnknownFieldsInner](docs/WebhookSubErrorPropertyUnknownFieldsInner.md)
- [WebhookSubErrorPropertyUnknownFieldsInnerId](docs/WebhookSubErrorPropertyUnknownFieldsInnerId.md)
- [WebhooksList](docs/WebhooksList.md)
- [WebhooksListWebhooksInner](docs/WebhooksListWebhooksInner.md)
- [WhosOutEntry](docs/WhosOutEntry.md)
- [XmlEmployeeFiles](docs/XmlEmployeeFiles.md)
- [XmlEmployeeFilesCategoryInner](docs/XmlEmployeeFilesCategoryInner.md)
- [XmlEmployeeFilesCategoryInnerFileInner](docs/XmlEmployeeFilesCategoryInnerFileInner.md)


## Exceptions

- [Exceptions](docs/Exceptions/Exceptions.md) - Information about exceptions, potential causes, and debugging tips

## Troubleshooting

### Common Errors

#### Authentication Errors (401)

**Symptom:** `AuthenticationFailedException` on every request.

**Solutions:**
- **API key:** Verify your key is correct and not disabled. The SDK sends it as HTTP Basic auth with `"x"` as the password — this is handled automatically.
- **OAuth:** Check that your access token hasn't expired. Use `with_oauth_refresh()` for automatic token renewal.
- **Company subdomain:** Ensure `for_company()` matches your BambooHR subdomain exactly (e.g., if your URL is `acme.bamboohr.com`, use `"acme"`).

#### Permission Errors (403)

**Symptom:** `PermissionDeniedException` for specific endpoints.

**Solutions:**
- Verify the API key or OAuth token has access to the requested resource.
- Contact your BambooHR administrator to review API access permissions.
- Check if IP restrictions are in place for API access.

#### Rate Limiting (429)

**Symptom:** `RateLimitExceededException` during batch operations.

**Solutions:**
- The SDK automatically retries on 429 responses with exponential backoff. Increase retries:
  ```python
  client = BambooHRClient().with_retries(5).for_company("acme").build()
  ```
- Add delays between batch requests: `time.sleep(0.1)` between calls.
- Check the `Retry-After` response header for server guidance.

### Network Troubleshooting

#### Connection Timeouts

**Symptom:** Requests hang or fail with timeout errors.

**Solutions:**
- Configure a timeout:
  ```python
  client = BambooHRClient().with_timeout(30.0).for_company("acme").build()
  ```
- Check your network connection and firewall settings.
- Verify that `*.bamboohr.com` is accessible from your network.

#### SSL/TLS Errors

**Symptom:** SSL certificate verification failures.

**Solutions:**
- Ensure your Python installation has up-to-date CA certificates: `pip install --upgrade certifi`
- If behind a corporate proxy, your IT team may need to add the proxy's CA certificate to your trust store.
- **Do not** disable SSL verification in production.

#### Proxy Configuration

If you're behind a corporate proxy, configure it via environment variables:

```bash
export HTTPS_PROXY=https://proxy.example.com:8080
```

### Enabling Debug Logging

Enable detailed request/response logging to diagnose issues:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
logging.getLogger("bamboohr_sdk").setLevel(logging.DEBUG)
```

This will log request URLs, response status codes, retry attempts, and token refresh events. Sensitive data (API keys, tokens, Authorization headers) is automatically redacted.

### Getting Help

When reporting issues, include:
- The **request ID** from the exception (`e.request_id`) — this helps BambooHR support trace the request.
- The **HTTP status code** and error message.
- The **SDK version** (`pip show bamboohr-sdk`).
- Debug log output (sensitive data is auto-redacted).

## Project Structure

```
bhr-api-python/
├── bamboohr_sdk/               # Main package
│   ├── api/                    # Auto-generated API classes
│   ├── models/                 # Auto-generated data models
│   ├── client/                 # Custom API client & auth
│   │   ├── auth/               # TokenManager, RefreshProvider
│   │   ├── middleware/         # OAuth2, RequestId middleware
│   │   └── logger/             # SecureLogger
│   ├── api_helper.py           # Retry logic & logging utilities
│   └── api_error_helper.py     # Error catalog & exception factory
├── test/                       # Auto-generated API test stubs
├── tests/                      # Custom hand-written tests
├── docs/                       # Auto-generated API documentation
├── templates-python/           # Custom openapi-generator templates
├── scripts/                    # Post-generation scripts
├── examples/                   # Usage examples
└── pyproject.toml              # Project configuration
```

## Development Setup

```bash
# Clone the repository
git clone https://github.com/BambooHR/bhr-api-python.git
cd bhr-api-python

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install with dev dependencies
pip install -e ".[dev]"
```

### Linting & Formatting

```bash
# Check linting
ruff check bamboohr_sdk/ tests/

# Auto-fix linting issues
ruff check --fix bamboohr_sdk/ tests/

# Format code
ruff format bamboohr_sdk/ tests/
```

### Type Checking

```bash
mypy bamboohr_sdk/
```

### Testing

```bash
pytest
```

### Protecting Implemented Tests

The `test/` directory contains auto-generated API test stubs created by `make generate`.
These stubs are overwritten on each regeneration. Once you implement real test logic in a
test file, add it to `.openapi-generator-ignore` to prevent it from being overwritten:

```
# .openapi-generator-ignore
test/test_employees_api.py
test/test_time_tracking_api.py
```

This ensures your implemented tests survive regeneration while new API test stubs are still
generated for any newly added APIs.

## Generating the SDK

This requires access to the internal BambooHR OpenAPI spec. The path to the spec file is
specified by the `OPENAPI_SPEC_PATH` environment variable.

```bash
make generate
```

### Manual changes to the auto-generated code

If you need to make manual changes to the auto-generated code, update the corresponding template in the `templates-python` directory and run `make generate` to regenerate the SDK. We have customized several templates to add SDK-specific features.

The following templates in `templates-python/` have been modified from the OpenAPI Generator defaults:

| Template | Modifications | Rationale |
|----------|--------------|-----------|
| `api.mustache` | Custom retry logic, secure logging, request ID extraction, void endpoint handling | Production-ready API calls with automatic retries and debugging support |
| `api_client.mustache` | HTTPS enforcement, custom User-Agent header, middleware pipeline | Security (HTTPS-only) and observability (request tracing) |
| `configuration.mustache` | HTTPS URL enforcement, retry configuration, custom defaults | Prevent accidental plaintext HTTP, sane retry defaults |
| `exceptions.mustache` | Status-specific exception hierarchy, `potential_causes()`/`debugging_tips()` methods, request ID support | Developer-friendly error handling with built-in troubleshooting |
| `README.mustache` | Complete custom README with troubleshooting and manual change tracking | Developer experience and onboarding |
| `api_test.mustache` | Test stub customizations | Consistent test structure |

Nearly all files under `bamboohr_sdk/api/`, `bamboohr_sdk/models/`, `test/`, and `docs/` are generated by the `make generate` command, with the following exceptions protected via `.openapi-generator-ignore`:

| File/Directory | Purpose | Why it's protected |
|---------------|---------|-------------------|
| `bamboohr_sdk/client/` | Fluent API client, auth builder, token manager, OAuth2 middleware, secure logger | Core SDK experience — all auth, retry, and logging logic lives here |
| `bamboohr_sdk/api_helper.py` | Retry logic with exponential backoff, secure request/response logging | Heavily customized from generator default — handles retry strategy and log redaction |
| `bamboohr_sdk/api_error_helper.py` | Error catalog mapping HTTP status codes to exception classes with causes/tips | Hand-written error metadata — regenerate exception classes via `scripts/generate_exceptions.py` |
| `bamboohr_sdk/api/manual_api.py` | Hand-written API class for endpoints not covered by the OpenAPI spec | Supplements auto-generated APIs |
| `tests/` | Hand-written unit and integration tests | Protected separately from auto-generated `test/` stubs |
| `examples/` | Usage examples and getting started code | Documentation — not generated |

Custom descriptions for some API docs are added in the `scripts/post_generate.py` script, which is run as part of the `make generate` command.

*Note: regeneration will not force an overwrite of tests in the `test/` directory, unless tests are deleted first.*

### Generating Error Documentation

The error documentation is automatically generated from the error messages defined in `api_error_helper.py`. To update the documentation when error messages are added or modified, run:

```bash
make generate-error-docs
```

Note that this script will also run as part of the `make generate` command.

This will:

1. Regenerate exception classes in `bamboohr_sdk/exceptions.py`
2. Regenerate the `docs/Exceptions/Exceptions.md` file with the latest error information
3. Generate exception documentation in `docs/Exceptions/Classes/`

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines, and the [Releasing](CONTRIBUTING.md#releasing) section for the publish-to-PyPI procedure.

## Data Handling

This SDK is a thin HTTP client for the BambooHR API. All data transits directly between your application and the BambooHR API over HTTPS — the SDK does not send telemetry, analytics, or data to any other destination.

- **Authentication**: API keys and OAuth tokens are sent in request headers to `https://{subdomain}.bamboohr.com`. Credentials are automatically redacted from debug log output.
- **API data**: Requests and responses may include HR data such as employee records, payroll, time off, benefits, and related information. See the [API documentation](https://documentation.bamboohr.com/docs/getting-started) for details on specific endpoints and data types.
- **Logging**: The SDK's debug logger redacts sensitive headers (Authorization, API keys) by default. No request or response bodies are logged unless you explicitly enable verbose logging in your application.

## Support

If you encounter any issues or need assistance with this SDK, please contact us through one of these channels:

- **Documentation**: Refer to the [official documentation](https://documentation.bamboohr.com/docs/getting-started)
- **Community**: Check existing issues and discussions for similar problems
- **Issue Tracker**: Submit bugs and feature requests through our [GitHub issue tracker](https://github.com/BambooHR/bhr-api-python/issues)

## About this package

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: `1.0`
- Package version: `1.0.0`
- Generator version: `7.16.0`
- Build package: `org.openapitools.codegen.languages.PythonClientCodegen`

## Terms

Use of the BambooHR API is subject to the [BambooHR Developer Terms of Service](https://www.bamboohr.com/legal/developer-terms-of-service).

## License

[MIT](LICENSE)
