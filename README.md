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
*AccountInformationApi* | [**call_5c5fb0f1211ae1c9451753f92f1053b6**](docs/AccountInformationApi.md#call_5c5fb0f1211ae1c9451753f92f1053b6) | **GET** /api/v1/meta/timezones | List timezones
*AccountInformationApi* | [**get_countries_options**](docs/AccountInformationApi.md#get_countries_options) | **GET** /api/v1/meta/countries/options | Get Countries
*AccountInformationApi* | [**get_states_by_country_id**](docs/AccountInformationApi.md#get_states_by_country_id) | **GET** /api/v1/meta/provinces/{countryId} | Get States by Country ID
*AccountInformationApi* | [**list_fields**](docs/AccountInformationApi.md#list_fields) | **GET** /api/v1/meta/fields | List Fields
*AccountInformationApi* | [**list_list_fields**](docs/AccountInformationApi.md#list_list_fields) | **GET** /api/v1/meta/lists | List List Fields
*AccountInformationApi* | [**list_tabular_fields**](docs/AccountInformationApi.md#list_tabular_fields) | **GET** /api/v1/meta/tables | List Tabular Fields
*AccountInformationApi* | [**list_users**](docs/AccountInformationApi.md#list_users) | **GET** /api/v1/meta/users | List Users
*AccountInformationApi* | [**update_list_field_values**](docs/AccountInformationApi.md#update_list_field_values) | **PUT** /api/v1/meta/lists/{listFieldId} | Update List Field Values
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
*BenefitsApi* | [**get_member_benefits**](docs/BenefitsApi.md#get_member_benefits) | **GET** /api/v1/benefits/member-benefits | Get Member Benefits
*BenefitsApi* | [**list_benefit_coverages**](docs/BenefitsApi.md#list_benefit_coverages) | **GET** /api/v1/benefitcoverages | List Benefit Coverages
*BenefitsApi* | [**list_benefit_deduction_types**](docs/BenefitsApi.md#list_benefit_deduction_types) | **GET** /api/v1/benefits/settings/deduction_types/all | List Benefit Deduction Types
*BenefitsApi* | [**list_company_benefits**](docs/BenefitsApi.md#list_company_benefits) | **GET** /api/v1/benefit/company_benefit | List Company Benefits
*BenefitsApi* | [**list_employee_benefits**](docs/BenefitsApi.md#list_employee_benefits) | **GET** /api/v1/benefit/employee_benefit | List Employee Benefits
*BenefitsApi* | [**list_employee_dependents**](docs/BenefitsApi.md#list_employee_dependents) | **GET** /api/v1/employeedependents | List Employee Dependents
*BenefitsApi* | [**list_member_benefit_events**](docs/BenefitsApi.md#list_member_benefit_events) | **GET** /api/v1/benefit/member_benefit | List Member Benefit Events
*BenefitsApi* | [**update_employee_dependent**](docs/BenefitsApi.md#update_employee_dependent) | **PUT** /api/v1/employeedependents/{id} | Update Employee Dependent
*CompanyFilesApi* | [**add_company_file_category**](docs/CompanyFilesApi.md#add_company_file_category) | **POST** /api/v1/files/categories | Create Company File Category
*CompanyFilesApi* | [**delete_company_file**](docs/CompanyFilesApi.md#delete_company_file) | **DELETE** /api/v1/files/{fileId} | Delete Company File
*CompanyFilesApi* | [**get_company_file**](docs/CompanyFilesApi.md#get_company_file) | **GET** /api/v1/files/{fileId} | Get Company File
*CompanyFilesApi* | [**list_company_files**](docs/CompanyFilesApi.md#list_company_files) | **GET** /api/v1/files/view | Get Company Files and Categories
*CompanyFilesApi* | [**update_company_file**](docs/CompanyFilesApi.md#update_company_file) | **POST** /api/v1/files/{fileId} | Update Company File
*CompanyFilesApi* | [**upload_company_file**](docs/CompanyFilesApi.md#upload_company_file) | **POST** /api/v1/files | Upload Company File
*CompanyProfileApi* | [**get_company_profile_integrations**](docs/CompanyProfileApi.md#get_company_profile_integrations) | **GET** /api/v1/company-profile-integrations | Get Company Profile Integrations
*CustomReportsApi* | [**get_by_report_id**](docs/CustomReportsApi.md#get_by_report_id) | **GET** /api/v1/custom-reports/{reportId} | Get Report by ID
*CustomReportsApi* | [**list_reports**](docs/CustomReportsApi.md#list_reports) | **GET** /api/v1/custom-reports | List Reports
*DatasetsApi* | [**get_data_from_dataset**](docs/DatasetsApi.md#get_data_from_dataset) | **POST** /api/v1/datasets/{datasetName} | Get Data from Dataset
*DatasetsApi* | [**get_datasets**](docs/DatasetsApi.md#get_datasets) | **GET** /api/v1/datasets | Get Datasets
*DatasetsApi* | [**get_datasets_v12**](docs/DatasetsApi.md#get_datasets_v12) | **GET** /api/v1_2/datasets | Get Datasets v1.2
*DatasetsApi* | [**get_field_options**](docs/DatasetsApi.md#get_field_options) | **POST** /api/v1/datasets/{datasetName}/field-options | Get Field Options
*DatasetsApi* | [**get_field_options_v12**](docs/DatasetsApi.md#get_field_options_v12) | **POST** /api/v1_2/datasets/{datasetName}/field-options | Get Field Options v1.2
*DatasetsApi* | [**get_fields_from_dataset**](docs/DatasetsApi.md#get_fields_from_dataset) | **GET** /api/v1/datasets/{datasetName}/fields | Get Fields from Dataset
*DatasetsApi* | [**get_fields_from_dataset_v12**](docs/DatasetsApi.md#get_fields_from_dataset_v12) | **GET** /api/v1_2/datasets/{datasetName}/fields | Get Fields from Dataset v1.2
*EmployeeFilesApi* | [**add_employee_file_category**](docs/EmployeeFilesApi.md#add_employee_file_category) | **POST** /api/v1/employees/files/categories | Create Employee File Category
*EmployeeFilesApi* | [**delete_employee_file**](docs/EmployeeFilesApi.md#delete_employee_file) | **DELETE** /api/v1/employees/{id}/files/{fileId} | Delete Employee File
*EmployeeFilesApi* | [**get_employee_file**](docs/EmployeeFilesApi.md#get_employee_file) | **GET** /api/v1/employees/{id}/files/{fileId} | Get Employee File
*EmployeeFilesApi* | [**list_employee_files**](docs/EmployeeFilesApi.md#list_employee_files) | **GET** /api/v1/employees/{id}/files/view | List Employee Files
*EmployeeFilesApi* | [**update_employee_file**](docs/EmployeeFilesApi.md#update_employee_file) | **POST** /api/v1/employees/{id}/files/{fileId} | Update Employee File
*EmployeeFilesApi* | [**upload_employee_file**](docs/EmployeeFilesApi.md#upload_employee_file) | **POST** /api/v1/employees/{id}/files | Upload Employee File
*EmployeesApi* | [**create_employee**](docs/EmployeesApi.md#create_employee) | **POST** /api/v1/employees | Create Employee
*EmployeesApi* | [**get_company_information**](docs/EmployeesApi.md#get_company_information) | **GET** /api/v1/company_information | Get Company Information
*EmployeesApi* | [**get_employee**](docs/EmployeesApi.md#get_employee) | **GET** /api/v1/employees/{id} | Get Employee
*EmployeesApi* | [**get_employees_directory**](docs/EmployeesApi.md#get_employees_directory) | **GET** /api/v1/employees/directory | Get Employee Directory
*EmployeesApi* | [**list_employees**](docs/EmployeesApi.md#list_employees) | **GET** /api/v1/employees | List Employees
*EmployeesApi* | [**update_employee**](docs/EmployeesApi.md#update_employee) | **POST** /api/v1/employees/{id} | Update Employee
*GoalsApi* | [**delete_goal**](docs/GoalsApi.md#delete_goal) | **DELETE** /api/v1/performance/employees/{employeeId}/goals/{goalId} | Delete Goal
*GoalsApi* | [**delete_goal_comment**](docs/GoalsApi.md#delete_goal_comment) | **DELETE** /api/v1/performance/employees/{employeeId}/goals/{goalId}/comments/{commentId} | Delete Goal Comment
*GoalsApi* | [**get_can_create_goal**](docs/GoalsApi.md#get_can_create_goal) | **GET** /api/v1/performance/employees/{employeeId}/goals/canCreateGoals | Check Goal Creation Permission
*GoalsApi* | [**get_goal_aggregate**](docs/GoalsApi.md#get_goal_aggregate) | **GET** /api/v1/performance/employees/{employeeId}/goals/{goalId}/aggregate | Get Goal Aggregate
*GoalsApi* | [**get_goal_comments**](docs/GoalsApi.md#get_goal_comments) | **GET** /api/v1/performance/employees/{employeeId}/goals/{goalId}/comments | Get Goal Comments
*GoalsApi* | [**get_goals**](docs/GoalsApi.md#get_goals) | **GET** /api/v1/performance/employees/{employeeId}/goals | Get Goals
*GoalsApi* | [**get_goals_aggregate_v1**](docs/GoalsApi.md#get_goals_aggregate_v1) | **GET** /api/v1/performance/employees/{employeeId}/goals/aggregate | Get Goals Aggregate
*GoalsApi* | [**get_goals_aggregate_v1_1**](docs/GoalsApi.md#get_goals_aggregate_v1_1) | **GET** /api/v1_1/performance/employees/{employeeId}/goals/aggregate | Get Goals Aggregate v1.1
*GoalsApi* | [**get_goals_aggregate_v1_2**](docs/GoalsApi.md#get_goals_aggregate_v1_2) | **GET** /api/v1_2/performance/employees/{employeeId}/goals/aggregate | Get Goals Aggregate v1.2
*GoalsApi* | [**get_goals_alignment_options**](docs/GoalsApi.md#get_goals_alignment_options) | **GET** /api/v1/performance/employees/{employeeId}/goals/alignmentOptions | Get Alignable Goal Options
*GoalsApi* | [**get_goals_filters_v1**](docs/GoalsApi.md#get_goals_filters_v1) | **GET** /api/v1/performance/employees/{employeeId}/goals/filters | Get Goal Filters
*GoalsApi* | [**get_goals_filters_v1_1**](docs/GoalsApi.md#get_goals_filters_v1_1) | **GET** /api/v1_1/performance/employees/{employeeId}/goals/filters | Get Goal Filters v1.1
*GoalsApi* | [**get_goals_filters_v1_2**](docs/GoalsApi.md#get_goals_filters_v1_2) | **GET** /api/v1_2/performance/employees/{employeeId}/goals/filters | Get Goal Status Counts v1.2
*GoalsApi* | [**get_goals_share_options**](docs/GoalsApi.md#get_goals_share_options) | **GET** /api/v1/performance/employees/{employeeId}/goals/shareOptions | Get Available Goal Sharing Options
*GoalsApi* | [**post_close_goal**](docs/GoalsApi.md#post_close_goal) | **POST** /api/v1/performance/employees/{employeeId}/goals/{goalId}/close | Close Goal
*GoalsApi* | [**post_goal**](docs/GoalsApi.md#post_goal) | **POST** /api/v1/performance/employees/{employeeId}/goals | Create Goal
*GoalsApi* | [**post_goal_comment**](docs/GoalsApi.md#post_goal_comment) | **POST** /api/v1/performance/employees/{employeeId}/goals/{goalId}/comments | Create Goal Comment
*GoalsApi* | [**post_reopen_goal**](docs/GoalsApi.md#post_reopen_goal) | **POST** /api/v1/performance/employees/{employeeId}/goals/{goalId}/reopen | Reopen Goal
*GoalsApi* | [**put_goal_comment**](docs/GoalsApi.md#put_goal_comment) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId}/comments/{commentId} | Update Goal Comment
*GoalsApi* | [**put_goal_milestone_progress**](docs/GoalsApi.md#put_goal_milestone_progress) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId}/milestones/{milestoneId}/progress | Update Milestone Progress
*GoalsApi* | [**put_goal_progress**](docs/GoalsApi.md#put_goal_progress) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId}/progress | Update Goal Progress
*GoalsApi* | [**put_goal_shared_with**](docs/GoalsApi.md#put_goal_shared_with) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId}/sharedWith | Update Goal Sharing
*GoalsApi* | [**put_goal_v1**](docs/GoalsApi.md#put_goal_v1) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId} | Update Goal
*GoalsApi* | [**put_goal_v1_1**](docs/GoalsApi.md#put_goal_v1_1) | **PUT** /api/v1_1/performance/employees/{employeeId}/goals/{goalId} | Update Goal v1.1
*HoursApi* | [**create_or_update_time_tracking_hour_records**](docs/HoursApi.md#create_or_update_time_tracking_hour_records) | **POST** /api/v1/timetracking/record | Create or Update Hour Records
*HoursApi* | [**create_time_tracking_hour_record**](docs/HoursApi.md#create_time_tracking_hour_record) | **POST** /api/v1/timetracking/add | Create Hour Record
*HoursApi* | [**delete_time_tracking_hour_record**](docs/HoursApi.md#delete_time_tracking_hour_record) | **DELETE** /api/v1/timetracking/delete/{id} | Delete Hour Record
*HoursApi* | [**get_time_tracking_record**](docs/HoursApi.md#get_time_tracking_record) | **GET** /api/v1/timetracking/record/{id} | Get Time Tracking Record
*HoursApi* | [**update_time_tracking_record**](docs/HoursApi.md#update_time_tracking_record) | **PUT** /api/v1/timetracking/adjust | Update Hour Record
*LastChangeInformationApi* | [**get_changed_employee_ids**](docs/LastChangeInformationApi.md#get_changed_employee_ids) | **GET** /api/v1/employees/changed | Get Changed Employee IDs
*LoginApi* | [**login**](docs/LoginApi.md#login) | **POST** /api/v1/login | Login
*PhotosApi* | [**get_employee_photo**](docs/PhotosApi.md#get_employee_photo) | **GET** /api/v1/employees/{employeeId}/photo/{size} | Get Employee Photo
*PhotosApi* | [**upload_employee_photo**](docs/PhotosApi.md#upload_employee_photo) | **POST** /api/v1/employees/{employeeId}/photo | Upload Employee Photo
*PublicAPIApi* | [**add_company_file_category**](docs/PublicAPIApi.md#add_company_file_category) | **POST** /api/v1/files/categories | Create Company File Category
*PublicAPIApi* | [**add_employee_file_category**](docs/PublicAPIApi.md#add_employee_file_category) | **POST** /api/v1/employees/files/categories | Create Employee File Category
*PublicAPIApi* | [**adjust_time_off_balance**](docs/PublicAPIApi.md#adjust_time_off_balance) | **PUT** /api/v1/employees/{employeeId}/time_off/balance_adjustment | Adjust Time Off Balance
*PublicAPIApi* | [**assign_employees_to_break_policy**](docs/PublicAPIApi.md#assign_employees_to_break_policy) | **POST** /api/v1/time-tracking/break-policies/{id}/assign | Assign Employees to Break Policy
*PublicAPIApi* | [**assign_time_off_policies**](docs/PublicAPIApi.md#assign_time_off_policies) | **PUT** /api/v1/employees/{employeeId}/time_off/policies | Assign Time Off Policies
*PublicAPIApi* | [**assign_time_off_policies_v1_1**](docs/PublicAPIApi.md#assign_time_off_policies_v1_1) | **PUT** /api/v1_1/employees/{employeeId}/time_off/policies | Assign Time Off Policies v1.1
*PublicAPIApi* | [**call_5c5fb0f1211ae1c9451753f92f1053b6**](docs/PublicAPIApi.md#call_5c5fb0f1211ae1c9451753f92f1053b6) | **GET** /api/v1/meta/timezones | List timezones
*PublicAPIApi* | [**create_application_comment**](docs/PublicAPIApi.md#create_application_comment) | **POST** /api/v1/applicant_tracking/applications/{applicationId}/comments | Create Job Application Comment
*PublicAPIApi* | [**create_break**](docs/PublicAPIApi.md#create_break) | **POST** /api/v1/time-tracking/break-policies/{id}/breaks | Create Break
*PublicAPIApi* | [**create_break_policy**](docs/PublicAPIApi.md#create_break_policy) | **POST** /api/v1/time-tracking/break-policies | Create Break Policy
*PublicAPIApi* | [**create_candidate**](docs/PublicAPIApi.md#create_candidate) | **POST** /api/v1/applicant_tracking/application | Create Candidate
*PublicAPIApi* | [**create_employee**](docs/PublicAPIApi.md#create_employee) | **POST** /api/v1/employees | Create Employee
*PublicAPIApi* | [**create_employee_dependent**](docs/PublicAPIApi.md#create_employee_dependent) | **POST** /api/v1/employeedependents | Create Employee Dependent
*PublicAPIApi* | [**create_employee_training_record**](docs/PublicAPIApi.md#create_employee_training_record) | **POST** /api/v1/training/record/employee/{employeeId} | Create Employee Training Record
*PublicAPIApi* | [**create_job_opening**](docs/PublicAPIApi.md#create_job_opening) | **POST** /api/v1/applicant_tracking/job_opening | Create Job Opening
*PublicAPIApi* | [**create_or_update_time_tracking_hour_records**](docs/PublicAPIApi.md#create_or_update_time_tracking_hour_records) | **POST** /api/v1/timetracking/record | Create or Update Hour Records
*PublicAPIApi* | [**create_or_update_timesheet_clock_entries**](docs/PublicAPIApi.md#create_or_update_timesheet_clock_entries) | **POST** /api/v1/time_tracking/clock_entries/store | Create or Update Timesheet Clock Entries
*PublicAPIApi* | [**create_or_update_timesheet_hour_entries**](docs/PublicAPIApi.md#create_or_update_timesheet_hour_entries) | **POST** /api/v1/time_tracking/hour_entries/store | Create or Update Timesheet Hour Entries
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
*PublicAPIApi* | [**delete_break**](docs/PublicAPIApi.md#delete_break) | **DELETE** /api/v1/time-tracking/breaks/{id} | Delete Break
*PublicAPIApi* | [**delete_break_policy**](docs/PublicAPIApi.md#delete_break_policy) | **DELETE** /api/v1/time-tracking/break-policies/{id} | Delete Break Policy
*PublicAPIApi* | [**delete_company_file**](docs/PublicAPIApi.md#delete_company_file) | **DELETE** /api/v1/files/{fileId} | Delete Company File
*PublicAPIApi* | [**delete_employee_file**](docs/PublicAPIApi.md#delete_employee_file) | **DELETE** /api/v1/employees/{id}/files/{fileId} | Delete Employee File
*PublicAPIApi* | [**delete_employee_table_row**](docs/PublicAPIApi.md#delete_employee_table_row) | **DELETE** /api/v1/employees/{id}/tables/{table}/{rowId} | Delete Employee Table Row
*PublicAPIApi* | [**delete_employee_training_record**](docs/PublicAPIApi.md#delete_employee_training_record) | **DELETE** /api/v1/training/record/{employeeTrainingRecordId} | Delete Employee Training Record
*PublicAPIApi* | [**delete_goal**](docs/PublicAPIApi.md#delete_goal) | **DELETE** /api/v1/performance/employees/{employeeId}/goals/{goalId} | Delete Goal
*PublicAPIApi* | [**delete_goal_comment**](docs/PublicAPIApi.md#delete_goal_comment) | **DELETE** /api/v1/performance/employees/{employeeId}/goals/{goalId}/comments/{commentId} | Delete Goal Comment
*PublicAPIApi* | [**delete_time_tracking_hour_record**](docs/PublicAPIApi.md#delete_time_tracking_hour_record) | **DELETE** /api/v1/timetracking/delete/{id} | Delete Hour Record
*PublicAPIApi* | [**delete_timesheet_clock_entries_via_post**](docs/PublicAPIApi.md#delete_timesheet_clock_entries_via_post) | **POST** /api/v1/time_tracking/clock_entries/delete | Delete Timesheet Clock Entries
*PublicAPIApi* | [**delete_timesheet_hour_entries_via_post**](docs/PublicAPIApi.md#delete_timesheet_hour_entries_via_post) | **POST** /api/v1/time_tracking/hour_entries/delete | Delete Timesheet Hour Entries
*PublicAPIApi* | [**delete_training_category**](docs/PublicAPIApi.md#delete_training_category) | **DELETE** /api/v1/training/category/{trainingCategoryId} | Delete Training Category
*PublicAPIApi* | [**delete_training_type**](docs/PublicAPIApi.md#delete_training_type) | **DELETE** /api/v1/training/type/{trainingTypeId} | Delete Training Type
*PublicAPIApi* | [**delete_webhook**](docs/PublicAPIApi.md#delete_webhook) | **DELETE** /api/v1/webhooks/{id} | Delete Webhook
*PublicAPIApi* | [**get_application_details**](docs/PublicAPIApi.md#get_application_details) | **GET** /api/v1/applicant_tracking/applications/{applicationId} | Get Job Application Details
*PublicAPIApi* | [**get_applications**](docs/PublicAPIApi.md#get_applications) | **GET** /api/v1/applicant_tracking/applications | Get Job Applications
*PublicAPIApi* | [**get_break**](docs/PublicAPIApi.md#get_break) | **GET** /api/v1/time-tracking/breaks/{id} | Get Break
*PublicAPIApi* | [**get_break_policy**](docs/PublicAPIApi.md#get_break_policy) | **GET** /api/v1/time-tracking/break-policies/{id} | Get Break Policy
*PublicAPIApi* | [**get_by_report_id**](docs/PublicAPIApi.md#get_by_report_id) | **GET** /api/v1/custom-reports/{reportId} | Get Report by ID
*PublicAPIApi* | [**get_can_create_goal**](docs/PublicAPIApi.md#get_can_create_goal) | **GET** /api/v1/performance/employees/{employeeId}/goals/canCreateGoals | Check Goal Creation Permission
*PublicAPIApi* | [**get_changed_employee_ids**](docs/PublicAPIApi.md#get_changed_employee_ids) | **GET** /api/v1/employees/changed | Get Changed Employee IDs
*PublicAPIApi* | [**get_changed_employee_table_data**](docs/PublicAPIApi.md#get_changed_employee_table_data) | **GET** /api/v1/employees/changed/tables/{table} | Get Changed Employee Table Data
*PublicAPIApi* | [**get_company_file**](docs/PublicAPIApi.md#get_company_file) | **GET** /api/v1/files/{fileId} | Get Company File
*PublicAPIApi* | [**get_company_information**](docs/PublicAPIApi.md#get_company_information) | **GET** /api/v1/company_information | Get Company Information
*PublicAPIApi* | [**get_company_locations**](docs/PublicAPIApi.md#get_company_locations) | **GET** /api/v1/applicant_tracking/locations | Get Company Locations
*PublicAPIApi* | [**get_company_profile_integrations**](docs/PublicAPIApi.md#get_company_profile_integrations) | **GET** /api/v1/company-profile-integrations | Get Company Profile Integrations
*PublicAPIApi* | [**get_company_report**](docs/PublicAPIApi.md#get_company_report) | **GET** /api/v1/reports/{id} | Get Company Report
*PublicAPIApi* | [**get_countries_options**](docs/PublicAPIApi.md#get_countries_options) | **GET** /api/v1/meta/countries/options | Get Countries
*PublicAPIApi* | [**get_data_from_dataset**](docs/PublicAPIApi.md#get_data_from_dataset) | **POST** /api/v1/datasets/{datasetName} | Get Data from Dataset
*PublicAPIApi* | [**get_datasets**](docs/PublicAPIApi.md#get_datasets) | **GET** /api/v1/datasets | Get Datasets
*PublicAPIApi* | [**get_datasets_v12**](docs/PublicAPIApi.md#get_datasets_v12) | **GET** /api/v1_2/datasets | Get Datasets v1.2
*PublicAPIApi* | [**get_employee**](docs/PublicAPIApi.md#get_employee) | **GET** /api/v1/employees/{id} | Get Employee
*PublicAPIApi* | [**get_employee_dependent**](docs/PublicAPIApi.md#get_employee_dependent) | **GET** /api/v1/employeedependents/{id} | Get Employee Dependent
*PublicAPIApi* | [**get_employee_file**](docs/PublicAPIApi.md#get_employee_file) | **GET** /api/v1/employees/{id}/files/{fileId} | Get Employee File
*PublicAPIApi* | [**get_employee_photo**](docs/PublicAPIApi.md#get_employee_photo) | **GET** /api/v1/employees/{employeeId}/photo/{size} | Get Employee Photo
*PublicAPIApi* | [**get_employee_table_data**](docs/PublicAPIApi.md#get_employee_table_data) | **GET** /api/v1/employees/{id}/tables/{table} | Get Employee Table Data
*PublicAPIApi* | [**get_employees_directory**](docs/PublicAPIApi.md#get_employees_directory) | **GET** /api/v1/employees/directory | Get Employee Directory
*PublicAPIApi* | [**get_field_options**](docs/PublicAPIApi.md#get_field_options) | **POST** /api/v1/datasets/{datasetName}/field-options | Get Field Options
*PublicAPIApi* | [**get_field_options_v12**](docs/PublicAPIApi.md#get_field_options_v12) | **POST** /api/v1_2/datasets/{datasetName}/field-options | Get Field Options v1.2
*PublicAPIApi* | [**get_fields_from_dataset**](docs/PublicAPIApi.md#get_fields_from_dataset) | **GET** /api/v1/datasets/{datasetName}/fields | Get Fields from Dataset
*PublicAPIApi* | [**get_fields_from_dataset_v12**](docs/PublicAPIApi.md#get_fields_from_dataset_v12) | **GET** /api/v1_2/datasets/{datasetName}/fields | Get Fields from Dataset v1.2
*PublicAPIApi* | [**get_goal_aggregate**](docs/PublicAPIApi.md#get_goal_aggregate) | **GET** /api/v1/performance/employees/{employeeId}/goals/{goalId}/aggregate | Get Goal Aggregate
*PublicAPIApi* | [**get_goal_comments**](docs/PublicAPIApi.md#get_goal_comments) | **GET** /api/v1/performance/employees/{employeeId}/goals/{goalId}/comments | Get Goal Comments
*PublicAPIApi* | [**get_goals**](docs/PublicAPIApi.md#get_goals) | **GET** /api/v1/performance/employees/{employeeId}/goals | Get Goals
*PublicAPIApi* | [**get_goals_aggregate_v1**](docs/PublicAPIApi.md#get_goals_aggregate_v1) | **GET** /api/v1/performance/employees/{employeeId}/goals/aggregate | Get Goals Aggregate
*PublicAPIApi* | [**get_goals_aggregate_v1_1**](docs/PublicAPIApi.md#get_goals_aggregate_v1_1) | **GET** /api/v1_1/performance/employees/{employeeId}/goals/aggregate | Get Goals Aggregate v1.1
*PublicAPIApi* | [**get_goals_aggregate_v1_2**](docs/PublicAPIApi.md#get_goals_aggregate_v1_2) | **GET** /api/v1_2/performance/employees/{employeeId}/goals/aggregate | Get Goals Aggregate v1.2
*PublicAPIApi* | [**get_goals_alignment_options**](docs/PublicAPIApi.md#get_goals_alignment_options) | **GET** /api/v1/performance/employees/{employeeId}/goals/alignmentOptions | Get Alignable Goal Options
*PublicAPIApi* | [**get_goals_filters_v1**](docs/PublicAPIApi.md#get_goals_filters_v1) | **GET** /api/v1/performance/employees/{employeeId}/goals/filters | Get Goal Filters
*PublicAPIApi* | [**get_goals_filters_v1_1**](docs/PublicAPIApi.md#get_goals_filters_v1_1) | **GET** /api/v1_1/performance/employees/{employeeId}/goals/filters | Get Goal Filters v1.1
*PublicAPIApi* | [**get_goals_filters_v1_2**](docs/PublicAPIApi.md#get_goals_filters_v1_2) | **GET** /api/v1_2/performance/employees/{employeeId}/goals/filters | Get Goal Status Counts v1.2
*PublicAPIApi* | [**get_goals_share_options**](docs/PublicAPIApi.md#get_goals_share_options) | **GET** /api/v1/performance/employees/{employeeId}/goals/shareOptions | Get Available Goal Sharing Options
*PublicAPIApi* | [**get_hiring_leads**](docs/PublicAPIApi.md#get_hiring_leads) | **GET** /api/v1/applicant_tracking/hiring_leads | Get Hiring Leads
*PublicAPIApi* | [**get_job_summaries**](docs/PublicAPIApi.md#get_job_summaries) | **GET** /api/v1/applicant_tracking/jobs | Get Job Summaries
*PublicAPIApi* | [**get_member_benefits**](docs/PublicAPIApi.md#get_member_benefits) | **GET** /api/v1/benefits/member-benefits | Get Member Benefits
*PublicAPIApi* | [**get_monitor_fields**](docs/PublicAPIApi.md#get_monitor_fields) | **GET** /api/v1/webhooks/monitor_fields | Get Monitor Fields
*PublicAPIApi* | [**get_post_fields**](docs/PublicAPIApi.md#get_post_fields) | **GET** /api/v1/webhooks/post-fields | Get Post Fields
*PublicAPIApi* | [**get_states_by_country_id**](docs/PublicAPIApi.md#get_states_by_country_id) | **GET** /api/v1/meta/provinces/{countryId} | Get States by Country ID
*PublicAPIApi* | [**get_statuses**](docs/PublicAPIApi.md#get_statuses) | **GET** /api/v1/applicant_tracking/statuses | Get Applicant Statuses
*PublicAPIApi* | [**get_time_off_balance**](docs/PublicAPIApi.md#get_time_off_balance) | **GET** /api/v1/employees/{employeeId}/time_off/calculator | Get Time Off Balance
*PublicAPIApi* | [**get_time_tracking_record**](docs/PublicAPIApi.md#get_time_tracking_record) | **GET** /api/v1/timetracking/record/{id} | Get Time Tracking Record
*PublicAPIApi* | [**get_webhook**](docs/PublicAPIApi.md#get_webhook) | **GET** /api/v1/webhooks/{id} | Get Webhook
*PublicAPIApi* | [**get_webhook_logs**](docs/PublicAPIApi.md#get_webhook_logs) | **GET** /api/v1/webhooks/{id}/log | Get Webhook Logs
*PublicAPIApi* | [**list_benefit_coverages**](docs/PublicAPIApi.md#list_benefit_coverages) | **GET** /api/v1/benefitcoverages | List Benefit Coverages
*PublicAPIApi* | [**list_benefit_deduction_types**](docs/PublicAPIApi.md#list_benefit_deduction_types) | **GET** /api/v1/benefits/settings/deduction_types/all | List Benefit Deduction Types
*PublicAPIApi* | [**list_break_assessments**](docs/PublicAPIApi.md#list_break_assessments) | **GET** /api/v1/time-tracking/break-assessments | List Break Assessments
*PublicAPIApi* | [**list_break_policies**](docs/PublicAPIApi.md#list_break_policies) | **GET** /api/v1/time-tracking/break-policies | List Break Policies
*PublicAPIApi* | [**list_break_policy_breaks**](docs/PublicAPIApi.md#list_break_policy_breaks) | **GET** /api/v1/time-tracking/break-policies/{id}/breaks | List Breaks for Break Policy
*PublicAPIApi* | [**list_break_policy_employees**](docs/PublicAPIApi.md#list_break_policy_employees) | **GET** /api/v1/time-tracking/break-policies/{id}/employees | List Break Policy Employees
*PublicAPIApi* | [**list_company_benefits**](docs/PublicAPIApi.md#list_company_benefits) | **GET** /api/v1/benefit/company_benefit | List Company Benefits
*PublicAPIApi* | [**list_company_files**](docs/PublicAPIApi.md#list_company_files) | **GET** /api/v1/files/view | Get Company Files and Categories
*PublicAPIApi* | [**list_employee_benefits**](docs/PublicAPIApi.md#list_employee_benefits) | **GET** /api/v1/benefit/employee_benefit | List Employee Benefits
*PublicAPIApi* | [**list_employee_break_availabilities**](docs/PublicAPIApi.md#list_employee_break_availabilities) | **GET** /api/v1/time-tracking/employees/{id}/break-availabilities | List Employee Break Availabilities
*PublicAPIApi* | [**list_employee_break_policies**](docs/PublicAPIApi.md#list_employee_break_policies) | **GET** /api/v1/time-tracking/employees/{id}/break-policies | List Employee Break Policies
*PublicAPIApi* | [**list_employee_dependents**](docs/PublicAPIApi.md#list_employee_dependents) | **GET** /api/v1/employeedependents | List Employee Dependents
*PublicAPIApi* | [**list_employee_files**](docs/PublicAPIApi.md#list_employee_files) | **GET** /api/v1/employees/{id}/files/view | List Employee Files
*PublicAPIApi* | [**list_employee_time_off_policies**](docs/PublicAPIApi.md#list_employee_time_off_policies) | **GET** /api/v1/employees/{employeeId}/time_off/policies | List Employee Time Off Policies
*PublicAPIApi* | [**list_employee_time_off_policies_v1_1**](docs/PublicAPIApi.md#list_employee_time_off_policies_v1_1) | **GET** /api/v1_1/employees/{employeeId}/time_off/policies | List Employee Time Off Policies v1.1
*PublicAPIApi* | [**list_employee_trainings**](docs/PublicAPIApi.md#list_employee_trainings) | **GET** /api/v1/training/record/employee/{employeeId} | List Employee Training Records
*PublicAPIApi* | [**list_employees**](docs/PublicAPIApi.md#list_employees) | **GET** /api/v1/employees | List Employees
*PublicAPIApi* | [**list_fields**](docs/PublicAPIApi.md#list_fields) | **GET** /api/v1/meta/fields | List Fields
*PublicAPIApi* | [**list_list_fields**](docs/PublicAPIApi.md#list_list_fields) | **GET** /api/v1/meta/lists | List List Fields
*PublicAPIApi* | [**list_member_benefit_events**](docs/PublicAPIApi.md#list_member_benefit_events) | **GET** /api/v1/benefit/member_benefit | List Member Benefit Events
*PublicAPIApi* | [**list_reports**](docs/PublicAPIApi.md#list_reports) | **GET** /api/v1/custom-reports | List Reports
*PublicAPIApi* | [**list_tabular_fields**](docs/PublicAPIApi.md#list_tabular_fields) | **GET** /api/v1/meta/tables | List Tabular Fields
*PublicAPIApi* | [**list_time_off_policies**](docs/PublicAPIApi.md#list_time_off_policies) | **GET** /api/v1/meta/time_off/policies | List Time Off Policies
*PublicAPIApi* | [**list_time_off_requests**](docs/PublicAPIApi.md#list_time_off_requests) | **GET** /api/v1/time_off/requests | List Time Off Requests
*PublicAPIApi* | [**list_time_off_types**](docs/PublicAPIApi.md#list_time_off_types) | **GET** /api/v1/meta/time_off/types | List Time Off Types
*PublicAPIApi* | [**list_timesheet_entries**](docs/PublicAPIApi.md#list_timesheet_entries) | **GET** /api/v1/time_tracking/timesheet_entries | List Timesheet Entries
*PublicAPIApi* | [**list_training_categories**](docs/PublicAPIApi.md#list_training_categories) | **GET** /api/v1/training/category | List Training Categories
*PublicAPIApi* | [**list_training_types**](docs/PublicAPIApi.md#list_training_types) | **GET** /api/v1/training/type | List Training Types
*PublicAPIApi* | [**list_users**](docs/PublicAPIApi.md#list_users) | **GET** /api/v1/meta/users | List Users
*PublicAPIApi* | [**list_webhooks**](docs/PublicAPIApi.md#list_webhooks) | **GET** /api/v1/webhooks | List Webhooks
*PublicAPIApi* | [**list_whos_out**](docs/PublicAPIApi.md#list_whos_out) | **GET** /api/v1/time_off/whos_out | List Who’s Out
*PublicAPIApi* | [**login**](docs/PublicAPIApi.md#login) | **POST** /api/v1/login | Login
*PublicAPIApi* | [**post_close_goal**](docs/PublicAPIApi.md#post_close_goal) | **POST** /api/v1/performance/employees/{employeeId}/goals/{goalId}/close | Close Goal
*PublicAPIApi* | [**post_goal**](docs/PublicAPIApi.md#post_goal) | **POST** /api/v1/performance/employees/{employeeId}/goals | Create Goal
*PublicAPIApi* | [**post_goal_comment**](docs/PublicAPIApi.md#post_goal_comment) | **POST** /api/v1/performance/employees/{employeeId}/goals/{goalId}/comments | Create Goal Comment
*PublicAPIApi* | [**post_reopen_goal**](docs/PublicAPIApi.md#post_reopen_goal) | **POST** /api/v1/performance/employees/{employeeId}/goals/{goalId}/reopen | Reopen Goal
*PublicAPIApi* | [**put_goal_comment**](docs/PublicAPIApi.md#put_goal_comment) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId}/comments/{commentId} | Update Goal Comment
*PublicAPIApi* | [**put_goal_milestone_progress**](docs/PublicAPIApi.md#put_goal_milestone_progress) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId}/milestones/{milestoneId}/progress | Update Milestone Progress
*PublicAPIApi* | [**put_goal_progress**](docs/PublicAPIApi.md#put_goal_progress) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId}/progress | Update Goal Progress
*PublicAPIApi* | [**put_goal_shared_with**](docs/PublicAPIApi.md#put_goal_shared_with) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId}/sharedWith | Update Goal Sharing
*PublicAPIApi* | [**put_goal_v1**](docs/PublicAPIApi.md#put_goal_v1) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId} | Update Goal
*PublicAPIApi* | [**put_goal_v1_1**](docs/PublicAPIApi.md#put_goal_v1_1) | **PUT** /api/v1_1/performance/employees/{employeeId}/goals/{goalId} | Update Goal v1.1
*PublicAPIApi* | [**replace_breaks_for_break_policy**](docs/PublicAPIApi.md#replace_breaks_for_break_policy) | **PUT** /api/v1/time-tracking/break-policies/{id}/breaks | Replace Breaks for Break Policy
*PublicAPIApi* | [**request_custom_report**](docs/PublicAPIApi.md#request_custom_report) | **POST** /api/v1/reports/custom | Request Custom Report
*PublicAPIApi* | [**set_break_policy_employees**](docs/PublicAPIApi.md#set_break_policy_employees) | **PUT** /api/v1/time-tracking/break-policies/{id}/assign | Set Employees for Break Policy
*PublicAPIApi* | [**sync_break_policy**](docs/PublicAPIApi.md#sync_break_policy) | **PUT** /api/v1/time-tracking/break-policies/{id}/sync | Sync Break Policy
*PublicAPIApi* | [**unassign_employees_from_break_policy**](docs/PublicAPIApi.md#unassign_employees_from_break_policy) | **POST** /api/v1/time-tracking/break-policies/{id}/unassign | Unassign Employees from Break Policy
*PublicAPIApi* | [**update_applicant_status**](docs/PublicAPIApi.md#update_applicant_status) | **POST** /api/v1/applicant_tracking/applications/{applicationId}/status | Update Applicant Status
*PublicAPIApi* | [**update_break**](docs/PublicAPIApi.md#update_break) | **PATCH** /api/v1/time-tracking/breaks/{id} | Update Break
*PublicAPIApi* | [**update_break_policy**](docs/PublicAPIApi.md#update_break_policy) | **PATCH** /api/v1/time-tracking/break-policies/{id} | Update Break Policy
*PublicAPIApi* | [**update_company_file**](docs/PublicAPIApi.md#update_company_file) | **POST** /api/v1/files/{fileId} | Update Company File
*PublicAPIApi* | [**update_employee**](docs/PublicAPIApi.md#update_employee) | **POST** /api/v1/employees/{id} | Update Employee
*PublicAPIApi* | [**update_employee_dependent**](docs/PublicAPIApi.md#update_employee_dependent) | **PUT** /api/v1/employeedependents/{id} | Update Employee Dependent
*PublicAPIApi* | [**update_employee_file**](docs/PublicAPIApi.md#update_employee_file) | **POST** /api/v1/employees/{id}/files/{fileId} | Update Employee File
*PublicAPIApi* | [**update_employee_training_record**](docs/PublicAPIApi.md#update_employee_training_record) | **PUT** /api/v1/training/record/{employeeTrainingRecordId} | Update Employee Training Record
*PublicAPIApi* | [**update_list_field_values**](docs/PublicAPIApi.md#update_list_field_values) | **PUT** /api/v1/meta/lists/{listFieldId} | Update List Field Values
*PublicAPIApi* | [**update_table_row**](docs/PublicAPIApi.md#update_table_row) | **POST** /api/v1/employees/{id}/tables/{table}/{rowId} | Update Table Row
*PublicAPIApi* | [**update_table_row_v11**](docs/PublicAPIApi.md#update_table_row_v11) | **POST** /api/v1_1/employees/{id}/tables/{table}/{rowId} | Update Table Row v1.1
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
*TimeTrackingApi* | [**create_time_tracking_project**](docs/TimeTrackingApi.md#create_time_tracking_project) | **POST** /api/v1/time_tracking/projects | Create Time Tracking Project
*TimeTrackingApi* | [**create_timesheet_clock_in_entry**](docs/TimeTrackingApi.md#create_timesheet_clock_in_entry) | **POST** /api/v1/time_tracking/employees/{employeeId}/clock_in | Create Timesheet Clock-In Entry
*TimeTrackingApi* | [**create_timesheet_clock_out_entry**](docs/TimeTrackingApi.md#create_timesheet_clock_out_entry) | **POST** /api/v1/time_tracking/employees/{employeeId}/clock_out | Create Timesheet Clock-Out Entry
*TimeTrackingApi* | [**delete_break**](docs/TimeTrackingApi.md#delete_break) | **DELETE** /api/v1/time-tracking/breaks/{id} | Delete Break
*TimeTrackingApi* | [**delete_break_policy**](docs/TimeTrackingApi.md#delete_break_policy) | **DELETE** /api/v1/time-tracking/break-policies/{id} | Delete Break Policy
*TimeTrackingApi* | [**delete_timesheet_clock_entries_via_post**](docs/TimeTrackingApi.md#delete_timesheet_clock_entries_via_post) | **POST** /api/v1/time_tracking/clock_entries/delete | Delete Timesheet Clock Entries
*TimeTrackingApi* | [**delete_timesheet_hour_entries_via_post**](docs/TimeTrackingApi.md#delete_timesheet_hour_entries_via_post) | **POST** /api/v1/time_tracking/hour_entries/delete | Delete Timesheet Hour Entries
*TimeTrackingApi* | [**get_break**](docs/TimeTrackingApi.md#get_break) | **GET** /api/v1/time-tracking/breaks/{id} | Get Break
*TimeTrackingApi* | [**get_break_policy**](docs/TimeTrackingApi.md#get_break_policy) | **GET** /api/v1/time-tracking/break-policies/{id} | Get Break Policy
*TimeTrackingApi* | [**list_break_assessments**](docs/TimeTrackingApi.md#list_break_assessments) | **GET** /api/v1/time-tracking/break-assessments | List Break Assessments
*TimeTrackingApi* | [**list_break_policies**](docs/TimeTrackingApi.md#list_break_policies) | **GET** /api/v1/time-tracking/break-policies | List Break Policies
*TimeTrackingApi* | [**list_break_policy_breaks**](docs/TimeTrackingApi.md#list_break_policy_breaks) | **GET** /api/v1/time-tracking/break-policies/{id}/breaks | List Breaks for Break Policy
*TimeTrackingApi* | [**list_break_policy_employees**](docs/TimeTrackingApi.md#list_break_policy_employees) | **GET** /api/v1/time-tracking/break-policies/{id}/employees | List Break Policy Employees
*TimeTrackingApi* | [**list_employee_break_availabilities**](docs/TimeTrackingApi.md#list_employee_break_availabilities) | **GET** /api/v1/time-tracking/employees/{id}/break-availabilities | List Employee Break Availabilities
*TimeTrackingApi* | [**list_employee_break_policies**](docs/TimeTrackingApi.md#list_employee_break_policies) | **GET** /api/v1/time-tracking/employees/{id}/break-policies | List Employee Break Policies
*TimeTrackingApi* | [**list_timesheet_entries**](docs/TimeTrackingApi.md#list_timesheet_entries) | **GET** /api/v1/time_tracking/timesheet_entries | List Timesheet Entries
*TimeTrackingApi* | [**replace_breaks_for_break_policy**](docs/TimeTrackingApi.md#replace_breaks_for_break_policy) | **PUT** /api/v1/time-tracking/break-policies/{id}/breaks | Replace Breaks for Break Policy
*TimeTrackingApi* | [**set_break_policy_employees**](docs/TimeTrackingApi.md#set_break_policy_employees) | **PUT** /api/v1/time-tracking/break-policies/{id}/assign | Set Employees for Break Policy
*TimeTrackingApi* | [**sync_break_policy**](docs/TimeTrackingApi.md#sync_break_policy) | **PUT** /api/v1/time-tracking/break-policies/{id}/sync | Sync Break Policy
*TimeTrackingApi* | [**unassign_employees_from_break_policy**](docs/TimeTrackingApi.md#unassign_employees_from_break_policy) | **POST** /api/v1/time-tracking/break-policies/{id}/unassign | Unassign Employees from Break Policy
*TimeTrackingApi* | [**update_break**](docs/TimeTrackingApi.md#update_break) | **PATCH** /api/v1/time-tracking/breaks/{id} | Update Break
*TimeTrackingApi* | [**update_break_policy**](docs/TimeTrackingApi.md#update_break_policy) | **PATCH** /api/v1/time-tracking/break-policies/{id} | Update Break Policy
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
*WebhooksApi* | [**get_monitor_fields**](docs/WebhooksApi.md#get_monitor_fields) | **GET** /api/v1/webhooks/monitor_fields | Get Monitor Fields
*WebhooksApi* | [**get_post_fields**](docs/WebhooksApi.md#get_post_fields) | **GET** /api/v1/webhooks/post-fields | Get Post Fields
*WebhooksApi* | [**get_webhook**](docs/WebhooksApi.md#get_webhook) | **GET** /api/v1/webhooks/{id} | Get Webhook
*WebhooksApi* | [**get_webhook_logs**](docs/WebhooksApi.md#get_webhook_logs) | **GET** /api/v1/webhooks/{id}/log | Get Webhook Logs
*WebhooksApi* | [**list_webhooks**](docs/WebhooksApi.md#list_webhooks) | **GET** /api/v1/webhooks | List Webhooks
*WebhooksApi* | [**update_webhook**](docs/WebhooksApi.md#update_webhook) | **PUT** /api/v1/webhooks/{id} | Update Webhook


## Models

- [AdjustTimeOffBalance](docs/AdjustTimeOffBalance.md)
- [AdjustTimeTrackingRequestSchema](docs/AdjustTimeTrackingRequestSchema.md)
- [AlignmentOptionsResponse](docs/AlignmentOptionsResponse.md)
- [AlignmentOptionsResponseAlignsWithOptionsInner](docs/AlignmentOptionsResponseAlignsWithOptionsInner.md)
- [ApplicantStatus](docs/ApplicantStatus.md)
- [ApplicationDetails](docs/ApplicationDetails.md)
- [ApplicationDetailsApplicant](docs/ApplicationDetailsApplicant.md)
- [ApplicationDetailsApplicantAddress](docs/ApplicationDetailsApplicantAddress.md)
- [ApplicationDetailsApplicantEducation](docs/ApplicationDetailsApplicantEducation.md)
- [ApplicationDetailsApplicantEducationLevel](docs/ApplicationDetailsApplicantEducationLevel.md)
- [ApplicationDetailsAttachmentsInner](docs/ApplicationDetailsAttachmentsInner.md)
- [ApplicationDetailsJob](docs/ApplicationDetailsJob.md)
- [ApplicationDetailsJobHiringLead](docs/ApplicationDetailsJobHiringLead.md)
- [ApplicationDetailsJobHiringLeadJobTitle](docs/ApplicationDetailsJobHiringLeadJobTitle.md)
- [ApplicationDetailsJobTitle](docs/ApplicationDetailsJobTitle.md)
- [ApplicationDetailsQuestionsAndAnswersInner](docs/ApplicationDetailsQuestionsAndAnswersInner.md)
- [ApplicationDetailsQuestionsAndAnswersInnerAnswer](docs/ApplicationDetailsQuestionsAndAnswersInnerAnswer.md)
- [ApplicationDetailsQuestionsAndAnswersInnerQuestion](docs/ApplicationDetailsQuestionsAndAnswersInnerQuestion.md)
- [ApplicationDetailsStatus](docs/ApplicationDetailsStatus.md)
- [ApplicationDetailsStatusChangedByUser](docs/ApplicationDetailsStatusChangedByUser.md)
- [ApplicationDetailsStatusChangedByUserJobTitle](docs/ApplicationDetailsStatusChangedByUserJobTitle.md)
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
- [BadRequest](docs/BadRequest.md)
- [BadRequestError](docs/BadRequestError.md)
- [BenefitCoveragesResponse](docs/BenefitCoveragesResponse.md)
- [BenefitCoveragesResponseBenefitCoveragesInner](docs/BenefitCoveragesResponseBenefitCoveragesInner.md)
- [BenefitDeductionSubType](docs/BenefitDeductionSubType.md)
- [BenefitDeductionType](docs/BenefitDeductionType.md)
- [BenefitDeductionTypeId](docs/BenefitDeductionTypeId.md)
- [CanCreateGoalsResponse](docs/CanCreateGoalsResponse.md)
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
- [CompanyBenefitSummary](docs/CompanyBenefitSummary.md)
- [CompanyBenefitsListResponse](docs/CompanyBenefitsListResponse.md)
- [CompanyDeletedWebhookPayload](docs/CompanyDeletedWebhookPayload.md)
- [CompanyFileUpdate](docs/CompanyFileUpdate.md)
- [CompanyFilesResponse](docs/CompanyFilesResponse.md)
- [CompanyFilesResponseCategoriesInner](docs/CompanyFilesResponseCategoriesInner.md)
- [CompanyFilesResponseCategoriesInnerFilesInner](docs/CompanyFilesResponseCategoriesInnerFilesInner.md)
- [CompanyInformation](docs/CompanyInformation.md)
- [CompanyInformationAddress](docs/CompanyInformationAddress.md)
- [CompanyIntegrationsUpdatedWebhookPayload](docs/CompanyIntegrationsUpdatedWebhookPayload.md)
- [CompanyIntegrationsUpdatedWebhookPayloadData](docs/CompanyIntegrationsUpdatedWebhookPayloadData.md)
- [CompanyProfileIntegrations](docs/CompanyProfileIntegrations.md)
- [CompanyUpdatedWebhookPayload](docs/CompanyUpdatedWebhookPayload.md)
- [Country](docs/Country.md)
- [CountrySchema](docs/CountrySchema.md)
- [CreateApplicationCommentRequest](docs/CreateApplicationCommentRequest.md)
- [CreateCandidateResponse](docs/CreateCandidateResponse.md)
- [CreateCommentResponse](docs/CreateCommentResponse.md)
- [CreateEmployeeTrainingRecordRequest](docs/CreateEmployeeTrainingRecordRequest.md)
- [CreateEmployeeTrainingRecordRequestCost](docs/CreateEmployeeTrainingRecordRequestCost.md)
- [CreateJobOpeningResponse](docs/CreateJobOpeningResponse.md)
- [CreateTrainingCategoryRequest](docs/CreateTrainingCategoryRequest.md)
- [CreateTrainingTypeRequest](docs/CreateTrainingTypeRequest.md)
- [CreateTrainingTypeRequestCategory](docs/CreateTrainingTypeRequestCategory.md)
- [CreateTrainingTypeRequestDueFromHireDate](docs/CreateTrainingTypeRequestDueFromHireDate.md)
- [CreateTrainingTypeRequestDueFromHireDateOneOf](docs/CreateTrainingTypeRequestDueFromHireDateOneOf.md)
- [CreateWebhookBadRequestResponse](docs/CreateWebhookBadRequestResponse.md)
- [CursorPagedResponseMetadata](docs/CursorPagedResponseMetadata.md)
- [CursorPagesResponse](docs/CursorPagesResponse.md)
- [CursorPaginationQueryObject](docs/CursorPaginationQueryObject.md)
- [DataRequest](docs/DataRequest.md)
- [DataRequestAggregationsInner](docs/DataRequestAggregationsInner.md)
- [DataRequestFilters](docs/DataRequestFilters.md)
- [DataRequestFiltersFiltersInner](docs/DataRequestFiltersFiltersInner.md)
- [DataRequestSortByInner](docs/DataRequestSortByInner.md)
- [Dataset](docs/Dataset.md)
- [DatasetFieldsResponse](docs/DatasetFieldsResponse.md)
- [DatasetResponse](docs/DatasetResponse.md)
- [DatasetsResponse](docs/DatasetsResponse.md)
- [DatasetsResponseDatasetsInner](docs/DatasetsResponseDatasetsInner.md)
- [Employee](docs/Employee.md)
- [EmployeeBenefitFilters](docs/EmployeeBenefitFilters.md)
- [EmployeeBenefitFiltersFilters](docs/EmployeeBenefitFiltersFilters.md)
- [EmployeeBenefitsListResponse](docs/EmployeeBenefitsListResponse.md)
- [EmployeeBenefitsListResponseEmployeeBenefitsInner](docs/EmployeeBenefitsListResponseEmployeeBenefitsInner.md)
- [EmployeeBenefitsListResponseEmployeeBenefitsInnerEmployeeBenefitInner](docs/EmployeeBenefitsListResponseEmployeeBenefitsInnerEmployeeBenefitInner.md)
- [EmployeeCreatedWebhookPayload](docs/EmployeeCreatedWebhookPayload.md)
- [EmployeeCreatedWebhookPayloadData](docs/EmployeeCreatedWebhookPayloadData.md)
- [EmployeeDeletedWebhookPayload](docs/EmployeeDeletedWebhookPayload.md)
- [EmployeeDeletedWebhookPayloadData](docs/EmployeeDeletedWebhookPayloadData.md)
- [EmployeeDependent](docs/EmployeeDependent.md)
- [EmployeeDependentsResponse](docs/EmployeeDependentsResponse.md)
- [EmployeeDependentsResponseEmployeeDependentsInner](docs/EmployeeDependentsResponseEmployeeDependentsInner.md)
- [EmployeeFileUpdate](docs/EmployeeFileUpdate.md)
- [EmployeeResponse](docs/EmployeeResponse.md)
- [EmployeeResponseAggregationsInner](docs/EmployeeResponseAggregationsInner.md)
- [EmployeeTableRow](docs/EmployeeTableRow.md)
- [EmployeeTableRowValue](docs/EmployeeTableRowValue.md)
- [EmployeeTableRowValueAnyOfInner](docs/EmployeeTableRowValueAnyOfInner.md)
- [EmployeeTimeOffPolicyAssignment](docs/EmployeeTimeOffPolicyAssignment.md)
- [EmployeeTimeOffPolicyAssignmentV11](docs/EmployeeTimeOffPolicyAssignmentV11.md)
- [EmployeeTimesheetEntryTransformer](docs/EmployeeTimesheetEntryTransformer.md)
- [EmployeeUpdatedWebhookPayload](docs/EmployeeUpdatedWebhookPayload.md)
- [EmployeeUpdatedWebhookPayloadData](docs/EmployeeUpdatedWebhookPayloadData.md)
- [EmployeeValue](docs/EmployeeValue.md)
- [EmployeeValueAnyOfInner](docs/EmployeeValueAnyOfInner.md)
- [Field1](docs/Field1.md)
- [Field1Id](docs/Field1Id.md)
- [FieldList](docs/FieldList.md)
- [FieldListFieldsInner](docs/FieldListFieldsInner.md)
- [FieldOptionsRequestSchema](docs/FieldOptionsRequestSchema.md)
- [FieldOptionsRequestSchemaDependentFieldsValueInner](docs/FieldOptionsRequestSchemaDependentFieldsValueInner.md)
- [FieldOptionsTransformer](docs/FieldOptionsTransformer.md)
- [Forbidden](docs/Forbidden.md)
- [GetCompanyReportResponse](docs/GetCompanyReportResponse.md)
- [GetEmployeesEmployeeResponse](docs/GetEmployeesEmployeeResponse.md)
- [GetEmployeesFilterRequestObject](docs/GetEmployeesFilterRequestObject.md)
- [GetEmployeesResponseObject](docs/GetEmployeesResponseObject.md)
- [GetEmployeesResponseObjectLinks](docs/GetEmployeesResponseObjectLinks.md)
- [GetEmployeesResponseObjectLinksNext](docs/GetEmployeesResponseObjectLinksNext.md)
- [GetEmployeesResponseObjectLinksPrev](docs/GetEmployeesResponseObjectLinksPrev.md)
- [GetEmployeesResponseObjectLinksSelf](docs/GetEmployeesResponseObjectLinksSelf.md)
- [Goal](docs/Goal.md)
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
- [InvalidRequest](docs/InvalidRequest.md)
- [InvalidRequestError](docs/InvalidRequestError.md)
- [JobSummary](docs/JobSummary.md)
- [JobSummaryDepartment](docs/JobSummaryDepartment.md)
- [JobSummaryHiringLead](docs/JobSummaryHiringLead.md)
- [JobSummaryLocation](docs/JobSummaryLocation.md)
- [JobSummaryStatus](docs/JobSummaryStatus.md)
- [JsonDirectoryEmployee](docs/JsonDirectoryEmployee.md)
- [JsonDirectoryEmployeeFieldsInner](docs/JsonDirectoryEmployeeFieldsInner.md)
- [JsonEmployeeFiles](docs/JsonEmployeeFiles.md)
- [JsonEmployeeFilesCategoriesInner](docs/JsonEmployeeFilesCategoriesInner.md)
- [JsonEmployeeFilesCategoriesInnerFilesInner](docs/JsonEmployeeFilesCategoriesInnerFilesInner.md)
- [JsonEmployeeFilesEmployee](docs/JsonEmployeeFilesEmployee.md)
- [ListFieldDetail](docs/ListFieldDetail.md)
- [ListFieldOption](docs/ListFieldOption.md)
- [ListFieldValues](docs/ListFieldValues.md)
- [ListFieldValuesOptionsInner](docs/ListFieldValuesOptionsInner.md)
- [ListUsersResponseValue](docs/ListUsersResponseValue.md)
- [ListUsersXmlResponse](docs/ListUsersXmlResponse.md)
- [ListUsersXmlResponseUserInner](docs/ListUsersXmlResponseUserInner.md)
- [Location](docs/Location.md)
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
- [ModelField](docs/ModelField.md)
- [NewWebHook](docs/NewWebHook.md)
- [PagedResponse](docs/PagedResponse.md)
- [Pagination](docs/Pagination.md)
- [PaginationMetaData](docs/PaginationMetaData.md)
- [PersonInfoApiTransformer](docs/PersonInfoApiTransformer.md)
- [PostGoalCommentRequest](docs/PostGoalCommentRequest.md)
- [PostGoalRequest](docs/PostGoalRequest.md)
- [PostGoalRequestMilestonesInner](docs/PostGoalRequestMilestonesInner.md)
- [PostNewEmployee](docs/PostNewEmployee.md)
- [ProblemDetailsResponse](docs/ProblemDetailsResponse.md)
- [ProjectCreateRequestSchema](docs/ProjectCreateRequestSchema.md)
- [ProjectInfoApiTransformer](docs/ProjectInfoApiTransformer.md)
- [ProjectInfoApiTransformerProject](docs/ProjectInfoApiTransformerProject.md)
- [ProjectInfoApiTransformerTask](docs/ProjectInfoApiTransformerTask.md)
- [PutGoalCommentRequest](docs/PutGoalCommentRequest.md)
- [PutGoalMilestoneProgressRequest](docs/PutGoalMilestoneProgressRequest.md)
- [PutGoalProgressRequest](docs/PutGoalProgressRequest.md)
- [PutGoalSharedWithRequest](docs/PutGoalSharedWithRequest.md)
- [PutGoalV11Request](docs/PutGoalV11Request.md)
- [PutGoalV11RequestMilestonesInner](docs/PutGoalV11RequestMilestonesInner.md)
- [Report](docs/Report.md)
- [ReportsResponse](docs/ReportsResponse.md)
- [Request](docs/Request.md)
- [RequestCustomReport](docs/RequestCustomReport.md)
- [RequestCustomReportFilters](docs/RequestCustomReportFilters.md)
- [RequestCustomReportFiltersLastChanged](docs/RequestCustomReportFiltersLastChanged.md)
- [RequestCustomReportResponse](docs/RequestCustomReportResponse.md)
- [RequestCustomReportResponseEmployeesInner](docs/RequestCustomReportResponseEmployeesInner.md)
- [RequestCustomReportResponseFieldsInner](docs/RequestCustomReportResponseFieldsInner.md)
- [SetBreakPolicyEmployeesRequest](docs/SetBreakPolicyEmployeesRequest.md)
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
- [TimeTrackingBulkResponseSchema](docs/TimeTrackingBulkResponseSchema.md)
- [TimeTrackingBulkResponseSchemaResponse](docs/TimeTrackingBulkResponseSchemaResponse.md)
- [TimeTrackingCreateOrUpdateTimeTrackingBreakWithoutPolicyV1](docs/TimeTrackingCreateOrUpdateTimeTrackingBreakWithoutPolicyV1.md)
- [TimeTrackingCreateTimeTrackingBreakPolicyV1](docs/TimeTrackingCreateTimeTrackingBreakPolicyV1.md)
- [TimeTrackingCreateTimeTrackingBreakV1](docs/TimeTrackingCreateTimeTrackingBreakV1.md)
- [TimeTrackingDeleteResponseSchema](docs/TimeTrackingDeleteResponseSchema.md)
- [TimeTrackingIdResponseSchema](docs/TimeTrackingIdResponseSchema.md)
- [TimeTrackingOffsetPaginatedResponseDataV1](docs/TimeTrackingOffsetPaginatedResponseDataV1.md)
- [TimeTrackingOffsetPaginatedResponseDataV1Links](docs/TimeTrackingOffsetPaginatedResponseDataV1Links.md)
- [TimeTrackingOffsetPaginatedResponseDataV1LinksNext](docs/TimeTrackingOffsetPaginatedResponseDataV1LinksNext.md)
- [TimeTrackingOffsetPaginatedResponseDataV1LinksPrev](docs/TimeTrackingOffsetPaginatedResponseDataV1LinksPrev.md)
- [TimeTrackingOffsetPaginatedResponseDataV1Meta](docs/TimeTrackingOffsetPaginatedResponseDataV1Meta.md)
- [TimeTrackingPaginatedBreakAssessmentsResponseV1](docs/TimeTrackingPaginatedBreakAssessmentsResponseV1.md)
- [TimeTrackingPaginatedBreakPoliciesResponseV1](docs/TimeTrackingPaginatedBreakPoliciesResponseV1.md)
- [TimeTrackingPaginatedBreakPolicyEmployeesResponseV1](docs/TimeTrackingPaginatedBreakPolicyEmployeesResponseV1.md)
- [TimeTrackingPaginatedBreaksResponseV1](docs/TimeTrackingPaginatedBreaksResponseV1.md)
- [TimeTrackingProjectWithTasksAndEmployeeIds](docs/TimeTrackingProjectWithTasksAndEmployeeIds.md)
- [TimeTrackingRecord](docs/TimeTrackingRecord.md)
- [TimeTrackingRecordSchema](docs/TimeTrackingRecordSchema.md)
- [TimeTrackingRecordSchemaProject](docs/TimeTrackingRecordSchemaProject.md)
- [TimeTrackingRecordSchemaProjectTask](docs/TimeTrackingRecordSchemaProjectTask.md)
- [TimeTrackingRecordSchemaShiftDifferential](docs/TimeTrackingRecordSchemaShiftDifferential.md)
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
- [TimesheetEntryInfoApiTransformerBreakInfo](docs/TimesheetEntryInfoApiTransformerBreakInfo.md)
- [TimezoneListResponse](docs/TimezoneListResponse.md)
- [TimezoneResource](docs/TimezoneResource.md)
- [TrainingCategory](docs/TrainingCategory.md)
- [TrainingRecord](docs/TrainingRecord.md)
- [TrainingRecordMap](docs/TrainingRecordMap.md)
- [TrainingRecordType](docs/TrainingRecordType.md)
- [TrainingType](docs/TrainingType.md)
- [TrainingTypeCategory](docs/TrainingTypeCategory.md)
- [TrainingTypeDueFromHireDate](docs/TrainingTypeDueFromHireDate.md)
- [TrainingTypeDueFromHireDateOneOf](docs/TrainingTypeDueFromHireDateOneOf.md)
- [TransformedApiEmployeeGoalDetails](docs/TransformedApiEmployeeGoalDetails.md)
- [TransformedApiEmployeeGoalDetailsGoal](docs/TransformedApiEmployeeGoalDetailsGoal.md)
- [TransformedApiGoal](docs/TransformedApiGoal.md)
- [TransformedApiGoalActions](docs/TransformedApiGoalActions.md)
- [TransformedApiGoalMilestonesInner](docs/TransformedApiGoalMilestonesInner.md)
- [UnassignEmployeesFromBreakPolicyRequest](docs/UnassignEmployeesFromBreakPolicyRequest.md)
- [UpdateApplicantStatusRequest](docs/UpdateApplicantStatusRequest.md)
- [UpdateApplicantStatusResponse](docs/UpdateApplicantStatusResponse.md)
- [UpdateEmployeeTrainingRecordRequest](docs/UpdateEmployeeTrainingRecordRequest.md)
- [UpdateTrainingCategoryRequest](docs/UpdateTrainingCategoryRequest.md)
- [UpdateTrainingTypeRequest](docs/UpdateTrainingTypeRequest.md)
- [UpdateTrainingTypeRequestCategory](docs/UpdateTrainingTypeRequestCategory.md)
- [UpdateWebhookBadRequestResponse](docs/UpdateWebhookBadRequestResponse.md)
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
- [XmlDirectoryEmployee](docs/XmlDirectoryEmployee.md)
- [XmlDirectoryEmployeeEmployees](docs/XmlDirectoryEmployeeEmployees.md)
- [XmlDirectoryEmployeeEmployeesEmployeeInner](docs/XmlDirectoryEmployeeEmployeesEmployeeInner.md)
- [XmlDirectoryEmployeeEmployeesEmployeeInnerFieldInner](docs/XmlDirectoryEmployeeEmployeesEmployeeInnerFieldInner.md)
- [XmlDirectoryEmployeeFieldset](docs/XmlDirectoryEmployeeFieldset.md)
- [XmlDirectoryEmployeeFieldsetFieldInner](docs/XmlDirectoryEmployeeFieldsetFieldInner.md)
- [XmlEmployeeFiles](docs/XmlEmployeeFiles.md)
- [XmlEmployeeFilesCategoryInner](docs/XmlEmployeeFilesCategoryInner.md)
- [XmlEmployeeFilesCategoryInnerFileInner](docs/XmlEmployeeFilesCategoryInnerFileInner.md)


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

If you need to make changes to generated code, update the corresponding template in
`templates-python/` and run `make generate` to regenerate. To update the README, edit
`templates-python/README.mustache` and regenerate — do not edit `README.md` directly.

The following files are **not** auto-generated and are protected from regeneration:

- `bamboohr_sdk/client/` — custom API client and authentication
- `bamboohr_sdk/api_helper.py` — retry logic and logging
- `bamboohr_sdk/api_error_helper.py` — error catalog and exception factory
- `bamboohr_sdk/api/manual_api.py` — hand-written API for custom requests
- `tests/` — hand-written tests
- `examples/` — usage examples

## Contributing

Contributions are welcome. Please open an issue before submitting a pull request for significant changes. Ensure all tests pass and type-checking is clean before opening a PR.

```bash
pytest
mypy bamboohr_sdk/
ruff check bamboohr_sdk/ tests/
```

## Support

- **API documentation:** [documentation.bamboohr.com](https://documentation.bamboohr.com/docs/getting-started)
- **Issues:** [GitHub Issues](https://github.com/BambooHR/bhr-api-python/issues)
- **BambooHR support:** [support.bamboohr.com](https://support.bamboohr.com)

## License

MIT
