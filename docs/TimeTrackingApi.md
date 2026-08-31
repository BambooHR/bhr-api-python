# bamboohr_sdk.TimeTrackingApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_timesheet**](TimeTrackingApi.md#approve_timesheet) | **POST** /api/v1/time-tracking/timesheet-approvals | Approve Timesheet
[**bulk_upsert_time_tracking_employee_enrollments**](TimeTrackingApi.md#bulk_upsert_time_tracking_employee_enrollments) | **POST** /api/v1/time-tracking/employees/bulk-upsert | Bulk Upsert Employee Enrollments
[**clock_in**](TimeTrackingApi.md#clock_in) | **POST** /api/v1/time-tracking/clock-ins | Clock In
[**clock_out**](TimeTrackingApi.md#clock_out) | **POST** /api/v1/time-tracking/clock-outs | Clock Out
[**create_clock_entry**](TimeTrackingApi.md#create_clock_entry) | **POST** /api/v1/time-tracking/clock-entries | Create Clock Entry
[**create_hour_entry**](TimeTrackingApi.md#create_hour_entry) | **POST** /api/v1/time-tracking/hour-entries | Create Hour Entry
[**create_or_update_timesheet_clock_entries**](TimeTrackingApi.md#create_or_update_timesheet_clock_entries) | **POST** /api/v1/time_tracking/clock_entries/store | Create or Update Timesheet Clock Entries
[**create_or_update_timesheet_hour_entries**](TimeTrackingApi.md#create_or_update_timesheet_hour_entries) | **POST** /api/v1/time_tracking/hour_entries/store | Create or Update Timesheet Hour Entries
[**create_project_task**](TimeTrackingApi.md#create_project_task) | **POST** /api/v1/time-tracking/projects/{projectId}/tasks | Create Time Tracking Project Task
[**create_shift_differential**](TimeTrackingApi.md#create_shift_differential) | **POST** /api/v1/time-tracking/shift-differentials | Create Time Tracking Shift Differential
[**create_time_tracking_configuration**](TimeTrackingApi.md#create_time_tracking_configuration) | **POST** /api/v1/time-tracking/configurations | Create Configuration
[**create_time_tracking_project**](TimeTrackingApi.md#create_time_tracking_project) | **POST** /api/v1/time-tracking/projects | Create Time Tracking Project
[**create_time_tracking_project_legacy**](TimeTrackingApi.md#create_time_tracking_project_legacy) | **POST** /api/v1/time_tracking/projects | Create Time Tracking Project (Legacy)
[**create_timesheet_clock_in_entry**](TimeTrackingApi.md#create_timesheet_clock_in_entry) | **POST** /api/v1/time_tracking/employees/{employeeId}/clock_in | Create Timesheet Clock-In Entry
[**create_timesheet_clock_out_entry**](TimeTrackingApi.md#create_timesheet_clock_out_entry) | **POST** /api/v1/time_tracking/employees/{employeeId}/clock_out | Create Timesheet Clock-Out Entry
[**delete_clock_entry**](TimeTrackingApi.md#delete_clock_entry) | **DELETE** /api/v1/time-tracking/clock-entries/{id} | Delete Clock Entry
[**delete_hour_entry**](TimeTrackingApi.md#delete_hour_entry) | **DELETE** /api/v1/time-tracking/hour-entries/{id} | Delete Hour Entry
[**delete_project**](TimeTrackingApi.md#delete_project) | **DELETE** /api/v1/time-tracking/projects/{id} | Delete Time Tracking Project
[**delete_shift_differential**](TimeTrackingApi.md#delete_shift_differential) | **DELETE** /api/v1/time-tracking/shift-differentials/{id} | Delete Time Tracking Shift Differential
[**delete_task**](TimeTrackingApi.md#delete_task) | **DELETE** /api/v1/time-tracking/tasks/{id} | Delete Time Tracking Task
[**delete_time_tracking_configuration**](TimeTrackingApi.md#delete_time_tracking_configuration) | **DELETE** /api/v1/time-tracking/configurations/{id} | Delete Configuration
[**delete_time_tracking_kiosk**](TimeTrackingApi.md#delete_time_tracking_kiosk) | **DELETE** /api/v1/time-tracking/kiosks/{id} | Delete Time Tracking Kiosk
[**delete_timesheet_clock_entries_via_post**](TimeTrackingApi.md#delete_timesheet_clock_entries_via_post) | **POST** /api/v1/time_tracking/clock_entries/delete | Delete Timesheet Clock Entries
[**delete_timesheet_hour_entries_via_post**](TimeTrackingApi.md#delete_timesheet_hour_entries_via_post) | **POST** /api/v1/time_tracking/hour_entries/delete | Delete Timesheet Hour Entries
[**get_clock_entry**](TimeTrackingApi.md#get_clock_entry) | **GET** /api/v1/time-tracking/clock-entries/{id} | Get Clock Entry
[**get_hour_entry**](TimeTrackingApi.md#get_hour_entry) | **GET** /api/v1/time-tracking/hour-entries/{id} | Get Hour Entry
[**get_project**](TimeTrackingApi.md#get_project) | **GET** /api/v1/time-tracking/projects/{id} | Get Time Tracking Project
[**get_shift_differential**](TimeTrackingApi.md#get_shift_differential) | **GET** /api/v1/time-tracking/shift-differentials/{id} | Get Time Tracking Shift Differential
[**get_task**](TimeTrackingApi.md#get_task) | **GET** /api/v1/time-tracking/tasks/{id} | Get Time Tracking Task
[**get_time_tracking_configuration**](TimeTrackingApi.md#get_time_tracking_configuration) | **GET** /api/v1/time-tracking/configurations/{id} | Get Configuration
[**get_time_tracking_employee_enrollment**](TimeTrackingApi.md#get_time_tracking_employee_enrollment) | **GET** /api/v1/time-tracking/employees/{employeeId} | Get Employee Enrollment
[**get_time_tracking_kiosk**](TimeTrackingApi.md#get_time_tracking_kiosk) | **GET** /api/v1/time-tracking/kiosks/{id} | Get Time Tracking Kiosk
[**get_time_tracking_time_clock**](TimeTrackingApi.md#get_time_tracking_time_clock) | **GET** /api/v1/time-tracking/time-clocks/{id} | Get Time Tracking Time Clock
[**get_timesheet**](TimeTrackingApi.md#get_timesheet) | **GET** /api/v1/time-tracking/timesheets/{id} | Get Timesheet
[**get_timesheet_summary**](TimeTrackingApi.md#get_timesheet_summary) | **GET** /api/v1/time-tracking/timesheets/{id}/summary | Get Timesheet Summary
[**list_clock_entries**](TimeTrackingApi.md#list_clock_entries) | **GET** /api/v1/time-tracking/clock-entries | List Clock Entries
[**list_hour_entries**](TimeTrackingApi.md#list_hour_entries) | **GET** /api/v1/time-tracking/hour-entries | List Hour Entries
[**list_project_tasks**](TimeTrackingApi.md#list_project_tasks) | **GET** /api/v1/time-tracking/projects/{projectId}/tasks | List Time Tracking Project Tasks
[**list_projects**](TimeTrackingApi.md#list_projects) | **GET** /api/v1/time-tracking/projects | List Time Tracking Projects
[**list_shift_differentials**](TimeTrackingApi.md#list_shift_differentials) | **GET** /api/v1/time-tracking/shift-differentials | List Time Tracking Shift Differentials
[**list_time_tracking_configurations**](TimeTrackingApi.md#list_time_tracking_configurations) | **GET** /api/v1/time-tracking/configurations | List Configurations
[**list_time_tracking_employees**](TimeTrackingApi.md#list_time_tracking_employees) | **GET** /api/v1/time-tracking/employees | List Enrolled Employees
[**list_time_tracking_kiosks**](TimeTrackingApi.md#list_time_tracking_kiosks) | **GET** /api/v1/time-tracking/kiosks | List Time Tracking Kiosks
[**list_time_tracking_time_clocks**](TimeTrackingApi.md#list_time_tracking_time_clocks) | **GET** /api/v1/time-tracking/time-clocks | List Time Tracking Time Clocks
[**list_timesheet_entries**](TimeTrackingApi.md#list_timesheet_entries) | **GET** /api/v1/time_tracking/timesheet_entries | List Timesheet Entries
[**list_timesheets**](TimeTrackingApi.md#list_timesheets) | **GET** /api/v1/time-tracking/timesheets | List Timesheets
[**update_clock_entry**](TimeTrackingApi.md#update_clock_entry) | **PATCH** /api/v1/time-tracking/clock-entries/{id} | Update Clock Entry
[**update_hour_entry**](TimeTrackingApi.md#update_hour_entry) | **PATCH** /api/v1/time-tracking/hour-entries/{id} | Update Hour Entry
[**update_project**](TimeTrackingApi.md#update_project) | **PATCH** /api/v1/time-tracking/projects/{id} | Update Time Tracking Project
[**update_shift_differential**](TimeTrackingApi.md#update_shift_differential) | **PATCH** /api/v1/time-tracking/shift-differentials/{id} | Update Time Tracking Shift Differential
[**update_task**](TimeTrackingApi.md#update_task) | **PATCH** /api/v1/time-tracking/tasks/{id} | Update Time Tracking Task
[**update_time_tracking_configuration**](TimeTrackingApi.md#update_time_tracking_configuration) | **PATCH** /api/v1/time-tracking/configurations/{id} | Update Configuration
[**update_time_tracking_employee_enrollment**](TimeTrackingApi.md#update_time_tracking_employee_enrollment) | **PATCH** /api/v1/time-tracking/employees/{employeeId} | Update Employee Enrollment
[**update_time_tracking_kiosk**](TimeTrackingApi.md#update_time_tracking_kiosk) | **PATCH** /api/v1/time-tracking/kiosks/{id} | Update Time Tracking Kiosk
[**update_time_tracking_time_clock**](TimeTrackingApi.md#update_time_tracking_time_clock) | **PATCH** /api/v1/time-tracking/time-clocks/{id} | Update Time Tracking Time Clock


# **approve_timesheet**
> TimeTrackingTimesheetV1 approve_timesheet(approve_timesheet_request)

Approve Timesheet

Approves a timesheet (process resource). Only a timesheet whose derived `status` is `PENDING_APPROVAL` can be approved; approving an already-approved or not-yet-open timesheet returns 409. Returns the updated timesheet with `status` `APPROVED`.

OAuth Scopes: time_tracking:timesheets.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.approve_timesheet_request import ApproveTimesheetRequest
from bamboohr_sdk.models.time_tracking_timesheet_v1 import TimeTrackingTimesheetV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    approve_timesheet_request = bamboohr_sdk.ApproveTimesheetRequest() # ApproveTimesheetRequest | 

    try:
        # Approve Timesheet
        api_response = api_instance.approve_timesheet(approve_timesheet_request)
        print("The response of TimeTrackingApi->approve_timesheet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->approve_timesheet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **approve_timesheet_request** | [**ApproveTimesheetRequest**](ApproveTimesheetRequest.md)|  | 

### Return type

[**TimeTrackingTimesheetV1**](TimeTrackingTimesheetV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully approved the timesheet. |  -  |
**400** | Malformed request body (e.g. missing timesheetId or lastChangedAt). |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | Timesheet not found. |  -  |
**409** | Timesheet is already approved, its approval window has not opened (status is not PENDING_APPROVAL), or it changed after the provided lastChangedAt. |  -  |
**422** | The provided timesheetId is not a valid positive integer, or lastChangedAt is not a valid ISO 8601 UTC timestamp. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_upsert_time_tracking_employee_enrollments**
> TimeTrackingBulkUpsertEmployeeTimeTrackingDataAcceptedV1 bulk_upsert_time_tracking_employee_enrollments(time_tracking_bulk_upsert_employee_time_tracking_data_record_v1, idempotency_key=idempotency_key, atomic=atomic)

Bulk Upsert Employee Enrollments

Bulk enables, disables, or reassigns employee enrollments. The body is a top-level JSON array of between 1 and 1000 upsert records; each record requires `employeeId` and applies the same merge-patch semantics as the single-employee PATCH. Request-level validation (payload shape, record cap, missing `employeeId`) runs synchronously; the records themselves are applied asynchronously, so the response is 202 with a `requestId` for log correlation rather than the resulting enrollments. Confirm the final state by reading the enrollments back through `GET /api/v1/time-tracking/employees`. Per-record processing errors, such as an unknown `employeeId` or `configurationId`, do not surface in the response. Send `atomic=true` to commit the whole batch as one unit instead, in which case any per-record failure aborts the batch and returns 422 with nothing applied.

OAuth Scopes: time_tracking:employees.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_bulk_upsert_employee_time_tracking_data_accepted_v1 import TimeTrackingBulkUpsertEmployeeTimeTrackingDataAcceptedV1
from bamboohr_sdk.models.time_tracking_bulk_upsert_employee_time_tracking_data_record_v1 import TimeTrackingBulkUpsertEmployeeTimeTrackingDataRecordV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    time_tracking_bulk_upsert_employee_time_tracking_data_record_v1 = [bamboohr_sdk.TimeTrackingBulkUpsertEmployeeTimeTrackingDataRecordV1()] # List[TimeTrackingBulkUpsertEmployeeTimeTrackingDataRecordV1] | 
    idempotency_key = 'idempotency_key_example' # str | Optional client-supplied key for safe retries. Replaying the same key with the same body and the same `atomic` mode returns the original response; reusing it with either changed is a conflict. (optional)
    atomic = False # bool | When true, the whole batch is committed as a single transaction and any per-record failure returns 422 with nothing applied. Defaults to false, which keeps the successful records and silently drops the failing ones. (optional) (default to False)

    try:
        # Bulk Upsert Employee Enrollments
        api_response = api_instance.bulk_upsert_time_tracking_employee_enrollments(time_tracking_bulk_upsert_employee_time_tracking_data_record_v1, idempotency_key=idempotency_key, atomic=atomic)
        print("The response of TimeTrackingApi->bulk_upsert_time_tracking_employee_enrollments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->bulk_upsert_time_tracking_employee_enrollments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_tracking_bulk_upsert_employee_time_tracking_data_record_v1** | [**List[TimeTrackingBulkUpsertEmployeeTimeTrackingDataRecordV1]**](TimeTrackingBulkUpsertEmployeeTimeTrackingDataRecordV1.md)|  | 
 **idempotency_key** | **str**| Optional client-supplied key for safe retries. Replaying the same key with the same body and the same &#x60;atomic&#x60; mode returns the original response; reusing it with either changed is a conflict. | [optional] 
 **atomic** | **bool**| When true, the whole batch is committed as a single transaction and any per-record failure returns 422 with nothing applied. Defaults to false, which keeps the successful records and silently drops the failing ones. | [optional] [default to False]

### Return type

[**TimeTrackingBulkUpsertEmployeeTimeTrackingDataAcceptedV1**](TimeTrackingBulkUpsertEmployeeTimeTrackingDataAcceptedV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The batch has been accepted. |  -  |
**400** | Malformed request body (not an array, or a record that does not name an employee). |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**409** | Conflict. The Idempotency-Key was reused with a different request, either a different body or a different &#x60;atomic&#x60; mode. |  -  |
**422** | Validation error (an empty batch, more than the maximum number of records, an unusable record field, an invalid &#x60;atomic&#x60; value, or, in atomic mode, any per-record failure). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clock_in**
> TimeTrackingClockEntryV1 clock_in(time_tracking_create_clock_in_v1)

Clock In

Clocks an employee in at the current server time, creating an open clock entry (`end: null`). Proxy clock-in for a different employee requires `time_tracking:timesheets.write` scope plus permission to manage the target employee's time.

OAuth Scopes: time_tracking:timesheets.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_clock_entry_v1 import TimeTrackingClockEntryV1
from bamboohr_sdk.models.time_tracking_create_clock_in_v1 import TimeTrackingCreateClockInV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    time_tracking_create_clock_in_v1 = bamboohr_sdk.TimeTrackingCreateClockInV1() # TimeTrackingCreateClockInV1 | 

    try:
        # Clock In
        api_response = api_instance.clock_in(time_tracking_create_clock_in_v1)
        print("The response of TimeTrackingApi->clock_in:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->clock_in: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_tracking_create_clock_in_v1** | [**TimeTrackingCreateClockInV1**](TimeTrackingCreateClockInV1.md)|  | 

### Return type

[**TimeTrackingClockEntryV1**](TimeTrackingClockEntryV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully clocked in. Returns the new open clock entry. |  -  |
**400** | Malformed request body. |  -  |
**401** | Unauthorized. |  -  |
**403** | Insufficient permissions. |  -  |
**409** | Employee is already clocked in, or the resolved timesheet type is not CLOCK. |  -  |
**422** | Validation error (invalid timezone, accuracy &gt; 10000 meters, or missing required fields). |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clock_out**
> TimeTrackingClockEntryV1 clock_out(time_tracking_create_clock_out_v1)

Clock Out

Clocks an employee out at the current server time, closing the employee's open clock entry (`end` set, `endSource: USER`). Proxy clock-out for a different employee requires `time_tracking:timesheets.write` scope plus permission to manage the target employee's time.

OAuth Scopes: time_tracking:timesheets.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_clock_entry_v1 import TimeTrackingClockEntryV1
from bamboohr_sdk.models.time_tracking_create_clock_out_v1 import TimeTrackingCreateClockOutV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    time_tracking_create_clock_out_v1 = bamboohr_sdk.TimeTrackingCreateClockOutV1() # TimeTrackingCreateClockOutV1 | 

    try:
        # Clock Out
        api_response = api_instance.clock_out(time_tracking_create_clock_out_v1)
        print("The response of TimeTrackingApi->clock_out:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->clock_out: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_tracking_create_clock_out_v1** | [**TimeTrackingCreateClockOutV1**](TimeTrackingCreateClockOutV1.md)|  | 

### Return type

[**TimeTrackingClockEntryV1**](TimeTrackingClockEntryV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully clocked out. Returns the closed clock entry. |  -  |
**400** | Malformed request body. |  -  |
**401** | Unauthorized. |  -  |
**403** | Insufficient permissions. |  -  |
**404** | No active clock entry found for the employee. |  -  |
**409** | The employee is already clocked out, or the resolved timesheet type is not CLOCK. |  -  |
**422** | Validation error (accuracy &gt; 10000 meters, or missing required fields). |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_clock_entry**
> TimeTrackingClockEntryV1 create_clock_entry(clock_entry_create_clock_entry_v1)

Create Clock Entry

Manually creates a time tracking clock entry (corrections, retroactive entry). Distinct from the real-time clock-in process resource. The parent daily entry and timesheet are resolved (and created if needed) from `start` + `timezone`; the entry is rejected with 409 when the resolved timesheet's type does not accept clock entries. Geolocation is persisted only when the employee's configuration has it enabled.

OAuth Scopes: time_tracking:timesheets.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.clock_entry_create_clock_entry_v1 import ClockEntryCreateClockEntryV1
from bamboohr_sdk.models.time_tracking_clock_entry_v1 import TimeTrackingClockEntryV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    clock_entry_create_clock_entry_v1 = bamboohr_sdk.ClockEntryCreateClockEntryV1() # ClockEntryCreateClockEntryV1 | 

    try:
        # Create Clock Entry
        api_response = api_instance.create_clock_entry(clock_entry_create_clock_entry_v1)
        print("The response of TimeTrackingApi->create_clock_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->create_clock_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clock_entry_create_clock_entry_v1** | [**ClockEntryCreateClockEntryV1**](ClockEntryCreateClockEntryV1.md)|  | 

### Return type

[**TimeTrackingClockEntryV1**](TimeTrackingClockEntryV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Clock entry created successfully. |  -  |
**400** | Malformed request body. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | No timesheet covering the requested date exists for the employee, or the employee does not exist. |  -  |
**409** | Conflict. An overlapping entry exists, or the resolved timesheet&#39;s type is SINGLE or HOUR (clock entries not accepted). |  -  |
**422** | Validation error (e.g., missing required fields, end before start, invalid timezone, accuracy greater than 10000). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_hour_entry**
> TimeTrackingHourEntryV1 create_hour_entry(hour_entry_create_hour_entry_v1)

Create Hour Entry

Creates a new time tracking hour entry.

OAuth Scopes: time_tracking:timesheets.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.hour_entry_create_hour_entry_v1 import HourEntryCreateHourEntryV1
from bamboohr_sdk.models.time_tracking_hour_entry_v1 import TimeTrackingHourEntryV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    hour_entry_create_hour_entry_v1 = bamboohr_sdk.HourEntryCreateHourEntryV1() # HourEntryCreateHourEntryV1 | 

    try:
        # Create Hour Entry
        api_response = api_instance.create_hour_entry(hour_entry_create_hour_entry_v1)
        print("The response of TimeTrackingApi->create_hour_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->create_hour_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hour_entry_create_hour_entry_v1** | [**HourEntryCreateHourEntryV1**](HourEntryCreateHourEntryV1.md)|  | 

### Return type

[**TimeTrackingHourEntryV1**](TimeTrackingHourEntryV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Hour entry created successfully. |  -  |
**400** | Malformed request body. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | No timesheet covering the requested date exists for the employee, or the employee does not exist. |  -  |
**409** | Conflict. Invalid timesheet type or an entry already exists for the date on a single-entry timesheet. |  -  |
**422** | Validation error (e.g., missing required fields, invalid date, hours less than or equal to zero). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_timesheet_clock_entries**
> List[TimesheetEntryInfoApiTransformer] create_or_update_timesheet_clock_entries(clock_entries_schema)

Create or Update Timesheet Clock Entries

Creates or updates timesheet clock entries in bulk. Entries with an existing ID are updated; entries without an ID are created.

OAuth Scopes: time_tracking.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.clock_entries_schema import ClockEntriesSchema
from bamboohr_sdk.models.timesheet_entry_info_api_transformer import TimesheetEntryInfoApiTransformer
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    clock_entries_schema = bamboohr_sdk.ClockEntriesSchema() # ClockEntriesSchema | 

    try:
        # Create or Update Timesheet Clock Entries
        api_response = api_instance.create_or_update_timesheet_clock_entries(clock_entries_schema)
        print("The response of TimeTrackingApi->create_or_update_timesheet_clock_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->create_or_update_timesheet_clock_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clock_entries_schema** | [**ClockEntriesSchema**](ClockEntriesSchema.md)|  | 

### Return type

[**List[TimesheetEntryInfoApiTransformer]**](TimesheetEntryInfoApiTransformer.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Entries created or updated successfully. Returns the resulting clock entry details. |  -  |
**400** | Bad request parameters - invalid data, clock times, project, task, or note. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Forbidden. Insufficient user permissions or API access is not turned on. |  -  |
**404** | Employee or timesheet entry not found. |  -  |
**406** | Entry is beyond the end of the current period. |  -  |
**409** | Conflicting entries exist, or timesheet type conflict. |  -  |
**412** | Precondition failed - invalid company configuration or timezone. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_timesheet_hour_entries**
> List[TimesheetEntryInfoApiTransformer] create_or_update_timesheet_hour_entries(hour_entries_request_schema)

Create or Update Timesheet Hour Entries

Creates or updates timesheet hour entries in bulk. Entries with an existing ID are updated; entries without an ID are created.

OAuth Scopes: time_tracking.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.hour_entries_request_schema import HourEntriesRequestSchema
from bamboohr_sdk.models.timesheet_entry_info_api_transformer import TimesheetEntryInfoApiTransformer
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    hour_entries_request_schema = bamboohr_sdk.HourEntriesRequestSchema() # HourEntriesRequestSchema | 

    try:
        # Create or Update Timesheet Hour Entries
        api_response = api_instance.create_or_update_timesheet_hour_entries(hour_entries_request_schema)
        print("The response of TimeTrackingApi->create_or_update_timesheet_hour_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->create_or_update_timesheet_hour_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hour_entries_request_schema** | [**HourEntriesRequestSchema**](HourEntriesRequestSchema.md)|  | 

### Return type

[**List[TimesheetEntryInfoApiTransformer]**](TimesheetEntryInfoApiTransformer.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Entries created or updated successfully. Returns the resulting hour entry details. |  -  |
**400** | Bad request parameters - invalid hours, project, task, or note. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Forbidden. Insufficient user permissions or API access is not turned on. |  -  |
**404** | Employee or timesheet entry not found. |  -  |
**406** | Request not acceptable. |  -  |
**409** | Timesheet type conflict. |  -  |
**412** | Precondition failed - invalid company configuration or timezone. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_task**
> ProjectTimeTrackingTaskV1 create_project_task(project_id, project_create_time_tracking_project_task_v1)

Create Time Tracking Project Task

Creates a new task on the specified time tracking project.

OAuth Scopes: time_tracking:project.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.project_create_time_tracking_project_task_v1 import ProjectCreateTimeTrackingProjectTaskV1
from bamboohr_sdk.models.project_time_tracking_task_v1 import ProjectTimeTrackingTaskV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    project_id = 'project_id_example' # str | The project ID.
    project_create_time_tracking_project_task_v1 = bamboohr_sdk.ProjectCreateTimeTrackingProjectTaskV1() # ProjectCreateTimeTrackingProjectTaskV1 | 

    try:
        # Create Time Tracking Project Task
        api_response = api_instance.create_project_task(project_id, project_create_time_tracking_project_task_v1)
        print("The response of TimeTrackingApi->create_project_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->create_project_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The project ID. | 
 **project_create_time_tracking_project_task_v1** | [**ProjectCreateTimeTrackingProjectTaskV1**](ProjectCreateTimeTrackingProjectTaskV1.md)|  | 

### Return type

[**ProjectTimeTrackingTaskV1**](ProjectTimeTrackingTaskV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Task created. |  -  |
**403** | Forbidden. |  -  |
**404** | Project not found. |  -  |
**409** | Duplicate task name within the project. |  -  |
**422** | Validation error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_shift_differential**
> ShiftDifferentialTimeTrackingShiftDifferentialV1 create_shift_differential(shift_differential_create_time_tracking_shift_differential_v1)

Create Time Tracking Shift Differential

Creates a new time tracking shift differential.

OAuth Scopes: time_tracking:shift_differentials.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.shift_differential_create_time_tracking_shift_differential_v1 import ShiftDifferentialCreateTimeTrackingShiftDifferentialV1
from bamboohr_sdk.models.shift_differential_time_tracking_shift_differential_v1 import ShiftDifferentialTimeTrackingShiftDifferentialV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    shift_differential_create_time_tracking_shift_differential_v1 = bamboohr_sdk.ShiftDifferentialCreateTimeTrackingShiftDifferentialV1() # ShiftDifferentialCreateTimeTrackingShiftDifferentialV1 | 

    try:
        # Create Time Tracking Shift Differential
        api_response = api_instance.create_shift_differential(shift_differential_create_time_tracking_shift_differential_v1)
        print("The response of TimeTrackingApi->create_shift_differential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->create_shift_differential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shift_differential_create_time_tracking_shift_differential_v1** | [**ShiftDifferentialCreateTimeTrackingShiftDifferentialV1**](ShiftDifferentialCreateTimeTrackingShiftDifferentialV1.md)|  | 

### Return type

[**ShiftDifferentialTimeTrackingShiftDifferentialV1**](ShiftDifferentialTimeTrackingShiftDifferentialV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Shift differential created successfully. |  -  |
**400** | Malformed request body. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**409** | Conflict. A shift differential with the provided name already exists. |  -  |
**422** | Validation error (e.g., missing &#x60;name&#x60;, invalid &#x60;rate&#x60;, empty &#x60;times&#x60; array). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_time_tracking_configuration**
> TimeTrackingTimeTrackingConfigurationV1 create_time_tracking_configuration(time_tracking_create_time_tracking_configuration_v1, idempotency_key=idempotency_key)

Create Configuration

Creates a new GROUP time tracking configuration together with its approval workflow. The type is forced to GROUP server-side; the GLOBAL configuration is auto-managed and cannot be created via this endpoint. Accepts an optional Idempotency-Key header for safe retries.

OAuth Scopes: time_tracking:configurations.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_create_time_tracking_configuration_v1 import TimeTrackingCreateTimeTrackingConfigurationV1
from bamboohr_sdk.models.time_tracking_time_tracking_configuration_v1 import TimeTrackingTimeTrackingConfigurationV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    time_tracking_create_time_tracking_configuration_v1 = bamboohr_sdk.TimeTrackingCreateTimeTrackingConfigurationV1() # TimeTrackingCreateTimeTrackingConfigurationV1 | 
    idempotency_key = 'idempotency_key_example' # str | Optional client-supplied key for safe retries (UUID recommended). Replaying the same key returns the original response; reusing it with a different body returns 409. (optional)

    try:
        # Create Configuration
        api_response = api_instance.create_time_tracking_configuration(time_tracking_create_time_tracking_configuration_v1, idempotency_key=idempotency_key)
        print("The response of TimeTrackingApi->create_time_tracking_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->create_time_tracking_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_tracking_create_time_tracking_configuration_v1** | [**TimeTrackingCreateTimeTrackingConfigurationV1**](TimeTrackingCreateTimeTrackingConfigurationV1.md)|  | 
 **idempotency_key** | **str**| Optional client-supplied key for safe retries (UUID recommended). Replaying the same key returns the original response; reusing it with a different body returns 409. | [optional] 

### Return type

[**TimeTrackingTimeTrackingConfigurationV1**](TimeTrackingTimeTrackingConfigurationV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Configuration created successfully. |  -  |
**400** | Malformed request body. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**409** | Conflict. A configuration with this name already exists, or the Idempotency-Key was reused with a different body. |  -  |
**422** | Validation error (e.g., missing required field, missing approverUserId when required, overtime fields set while customOvertimeEnabled is false, an overtime threshold outside its allowed range, or attempting to create a GLOBAL configuration). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_time_tracking_project**
> ProjectTimeTrackingProjectV1 create_time_tracking_project(project_create_time_tracking_project_v1)

Create Time Tracking Project

Creates a time tracking project. If a deleted project with the same name exists, that project is restored and updated with the supplied values instead of a new project being created; the response returns the restored project's existing ID. `hasTasks` in the response is set automatically based on whether `tasks` were supplied and cannot be set directly on create. Created tasks are not embedded; retrieve them with **List Time Tracking Project Tasks** (`list-project-tasks`).

OAuth Scopes: time_tracking:project.write

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.project_create_time_tracking_project_v1 import ProjectCreateTimeTrackingProjectV1
from bamboohr_sdk.models.project_time_tracking_project_v1 import ProjectTimeTrackingProjectV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    project_create_time_tracking_project_v1 = bamboohr_sdk.ProjectCreateTimeTrackingProjectV1() # ProjectCreateTimeTrackingProjectV1 | 

    try:
        # Create Time Tracking Project
        api_response = api_instance.create_time_tracking_project(project_create_time_tracking_project_v1)
        print("The response of TimeTrackingApi->create_time_tracking_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->create_time_tracking_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_create_time_tracking_project_v1** | [**ProjectCreateTimeTrackingProjectV1**](ProjectCreateTimeTrackingProjectV1.md)|  | 

### Return type

[**ProjectTimeTrackingProjectV1**](ProjectTimeTrackingProjectV1.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created or restored project resource. Created tasks are not embedded. |  -  |
**401** | Unauthorized. The response body is not JSON. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**409** | Conflict. A project with this name already exists. Name comparison is case-insensitive and ignores surrounding whitespace. |  -  |
**422** | Validation error (e.g. missing &#x60;name&#x60;, invalid &#x60;employeeIds&#x60;, name too long). |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_time_tracking_project_legacy**
> TimeTrackingProjectWithTasksAndEmployeeIds create_time_tracking_project_legacy(project_create_request_schema)

Create Time Tracking Project (Legacy)

Deprecated. Use **Create Time Tracking Project** instead (`create-time-tracking-project`).

Creates a time tracking project using the legacy contract and returns the project with its tasks. If a deleted project with the same name exists, that project is restored and updated with the supplied values instead of a new project being created; the response returns the restored project's existing ID.

OAuth Scopes: time_tracking.write

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.project_create_request_schema import ProjectCreateRequestSchema
from bamboohr_sdk.models.time_tracking_project_with_tasks_and_employee_ids import TimeTrackingProjectWithTasksAndEmployeeIds
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    project_create_request_schema = bamboohr_sdk.ProjectCreateRequestSchema() # ProjectCreateRequestSchema | 

    try:
        # Create Time Tracking Project (Legacy)
        api_response = api_instance.create_time_tracking_project_legacy(project_create_request_schema)
        print("The response of TimeTrackingApi->create_time_tracking_project_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->create_time_tracking_project_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_create_request_schema** | [**ProjectCreateRequestSchema**](ProjectCreateRequestSchema.md)|  | 

### Return type

[**TimeTrackingProjectWithTasksAndEmployeeIds**](TimeTrackingProjectWithTasksAndEmployeeIds.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created or restored project with its tasks. The &#x60;employeeIds&#x60; field is present only when one or more employees are individually assigned. |  -  |
**400** | Invalid or missing request data, duplicate project or task name, or another project validation failure. |  -  |
**401** | Unauthorized. The response body is not JSON. |  -  |
**403** | Forbidden. Insufficient user permissions or API access is not turned on. |  -  |
**404** | Not found. A referenced record could not be resolved. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_timesheet_clock_in_entry**
> TimesheetEntryInfoApiTransformer create_timesheet_clock_in_entry(employee_id, clock_in_request_schema=clock_in_request_schema)

Create Timesheet Clock-In Entry

Clocks in an employee at the current server time. To record a historical clock-in, provide a `date`, `start` (HH:MM, 24-hour format), and `timezone`. You can optionally associate the entry with `projectId`, `taskId` (requires `projectId`), `breakId`, and a `note`.

OAuth Scopes: time_tracking.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.clock_in_request_schema import ClockInRequestSchema
from bamboohr_sdk.models.timesheet_entry_info_api_transformer import TimesheetEntryInfoApiTransformer
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    employee_id = 56 # int | The internal employee ID of the employee to clock in.
    clock_in_request_schema = bamboohr_sdk.ClockInRequestSchema() # ClockInRequestSchema |  (optional)

    try:
        # Create Timesheet Clock-In Entry
        api_response = api_instance.create_timesheet_clock_in_entry(employee_id, clock_in_request_schema=clock_in_request_schema)
        print("The response of TimeTrackingApi->create_timesheet_clock_in_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->create_timesheet_clock_in_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| The internal employee ID of the employee to clock in. | 
 **clock_in_request_schema** | [**ClockInRequestSchema**](ClockInRequestSchema.md)|  | [optional] 

### Return type

[**TimesheetEntryInfoApiTransformer**](TimesheetEntryInfoApiTransformer.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The employee was successfully clocked in. Returns the new clock entry details. |  -  |
**400** | Bad request parameters - invalid date, time, timezone, project, task, or note. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Forbidden. Insufficient user permissions or API access is not turned on. |  -  |
**404** | Employee not found. |  -  |
**406** | A future clock entry exists; cannot clock in until it is resolved. |  -  |
**409** | The employee is already clocked in, or timesheet type conflict. |  -  |
**412** | Precondition failed - invalid company configuration, invalid timezone, or employee is not configured for time tracking. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_timesheet_clock_out_entry**
> TimesheetEntryInfoApiTransformer create_timesheet_clock_out_entry(employee_id, clock_out_request_schema=clock_out_request_schema)

Create Timesheet Clock-Out Entry

Clocks out a currently clocked-in employee at the current server time. To record a historical clock-out, provide a `date`, `end` (HH:MM, 24-hour format), and `timezone`.

OAuth Scopes: time_tracking.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.clock_out_request_schema import ClockOutRequestSchema
from bamboohr_sdk.models.timesheet_entry_info_api_transformer import TimesheetEntryInfoApiTransformer
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    employee_id = 56 # int | The internal employee ID of the employee to clock out.
    clock_out_request_schema = bamboohr_sdk.ClockOutRequestSchema() # ClockOutRequestSchema |  (optional)

    try:
        # Create Timesheet Clock-Out Entry
        api_response = api_instance.create_timesheet_clock_out_entry(employee_id, clock_out_request_schema=clock_out_request_schema)
        print("The response of TimeTrackingApi->create_timesheet_clock_out_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->create_timesheet_clock_out_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| The internal employee ID of the employee to clock out. | 
 **clock_out_request_schema** | [**ClockOutRequestSchema**](ClockOutRequestSchema.md)|  | [optional] 

### Return type

[**TimesheetEntryInfoApiTransformer**](TimesheetEntryInfoApiTransformer.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The employee was successfully clocked out. Returns the completed clock entry details. |  -  |
**400** | Bad request parameters - invalid date, time, or timezone. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Forbidden. Insufficient user permissions or API access is not turned on. |  -  |
**404** | Employee not found, or the clock entry has already been removed. |  -  |
**409** | The employee is not currently clocked in (already clocked out), or a timesheet type conflict. |  -  |
**412** | Precondition failed - invalid company configuration, invalid timezone, no open clock entries, or employee is not configured for time tracking. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_clock_entry**
> delete_clock_entry(id)

Delete Clock Entry

Deletes a time tracking clock entry by its ID.

OAuth Scopes: time_tracking:timesheets.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 56 # int | The clock entry ID.

    try:
        # Delete Clock Entry
        api_instance.delete_clock_entry(id)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->delete_clock_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The clock entry ID. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The clock entry was deleted, or did not exist (DELETE is idempotent). |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**409** | Conflict. The clock entry belongs to an approved timesheet or is still open. |  -  |
**422** | The provided clock entry ID is not a valid positive integer. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_hour_entry**
> delete_hour_entry(id)

Delete Hour Entry

Deletes a time tracking hour entry by its ID.

OAuth Scopes: time_tracking:timesheets.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 56 # int | The hour entry ID.

    try:
        # Delete Hour Entry
        api_instance.delete_hour_entry(id)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->delete_hour_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The hour entry ID. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The hour entry was deleted, or did not exist (DELETE is idempotent). |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**409** | Conflict. The hour entry belongs to an approved timesheet. |  -  |
**422** | The provided hour entry ID is not a valid positive integer. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(id)

Delete Time Tracking Project

Deletes a time tracking project by its ID.

OAuth Scopes: time_tracking:project.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 56 # int | The project ID.

    try:
        # Delete Time Tracking Project
        api_instance.delete_project(id)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->delete_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project ID. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Project deleted successfully. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | Project not found. |  -  |
**422** | The provided project ID is not a valid integer. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shift_differential**
> delete_shift_differential(id)

Delete Time Tracking Shift Differential

Deletes a time tracking shift differential by its ID.

OAuth Scopes: time_tracking:shift_differentials.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 56 # int | The shift differential ID.

    try:
        # Delete Time Tracking Shift Differential
        api_instance.delete_shift_differential(id)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->delete_shift_differential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The shift differential ID. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Shift differential deleted successfully. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**422** | The provided shift differential ID is not a valid integer. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task**
> delete_task(id)

Delete Time Tracking Task

Deletes a time tracking task by its ID.

OAuth Scopes: time_tracking:project.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 56 # int | The task ID.

    try:
        # Delete Time Tracking Task
        api_instance.delete_task(id)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->delete_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The task ID. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The task was deleted successfully. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | Task not found. |  -  |
**422** | The provided &#x60;id&#x60; is not a valid integer. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_time_tracking_configuration**
> delete_time_tracking_configuration(id)

Delete Configuration

Soft-deletes an empty GROUP time tracking configuration. A configuration that still has enrolled employees cannot be deleted, because un-enrolling employees is governed by the employee enrollment permissions rather than the configuration permissions; move or un-enroll its employees first. Open timesheets stay on the previously-applicable rules until the next pay period boundary. The GLOBAL configuration is auto-managed and cannot be deleted. Deletion is idempotent: an ID that does not exist, or a configuration that was already deleted, also returns 204.

OAuth Scopes: time_tracking:configurations.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 56 # int | The time tracking configuration ID.

    try:
        # Delete Configuration
        api_instance.delete_time_tracking_configuration(id)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->delete_time_tracking_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The time tracking configuration ID. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The configuration was deleted, or no configuration with that ID exists. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**422** | The GLOBAL configuration cannot be deleted, the configuration still has enrolled employees, or the provided configuration ID is not a valid positive integer. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_time_tracking_kiosk**
> delete_time_tracking_kiosk(id)

Delete Time Tracking Kiosk

Soft-deletes a time tracking kiosk. Deletion is idempotent (REST API Standard 3.3): a 204 is returned whether or not the kiosk currently exists, so deleting a missing or already-deleted kiosk also returns 204. Once deleted, a kiosk is absent from List Kiosks and returns 404 on Get Kiosk.

OAuth Scopes: time_tracking:kiosks.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 'id_example' # str | The time tracking kiosk ID.

    try:
        # Delete Time Tracking Kiosk
        api_instance.delete_time_tracking_kiosk(id)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->delete_time_tracking_kiosk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The time tracking kiosk ID. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Kiosk deleted. Also returned when the kiosk does not exist or was already deleted. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions or read-only scope. |  -  |
**422** | The provided kiosk ID is not a valid UUID. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_timesheet_clock_entries_via_post**
> delete_timesheet_clock_entries_via_post(clock_entry_ids_schema)

Delete Timesheet Clock Entries

Deletes one or more timesheet clock entries by their IDs. Delete operations are idempotent; deleting already-removed entries does not require client retries.

OAuth Scopes: time_tracking.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.clock_entry_ids_schema import ClockEntryIdsSchema
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    clock_entry_ids_schema = bamboohr_sdk.ClockEntryIdsSchema() # ClockEntryIdsSchema | 

    try:
        # Delete Timesheet Clock Entries
        api_instance.delete_timesheet_clock_entries_via_post(clock_entry_ids_schema)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->delete_timesheet_clock_entries_via_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clock_entry_ids_schema** | [**ClockEntryIdsSchema**](ClockEntryIdsSchema.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Entries deleted successfully. No content returned. |  -  |
**400** | Bad request parameters - missing or invalid clockEntryIds. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Forbidden. Insufficient permissions or timesheet already approved. |  -  |
**409** | One or more entries are still clocked in; clock out before deleting. |  -  |
**412** | Precondition failed - invalid company configuration or timezone. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_timesheet_hour_entries_via_post**
> delete_timesheet_hour_entries_via_post(hour_entry_ids_schema)

Delete Timesheet Hour Entries

Deletes one or more timesheet hour entries by their IDs. Delete operations are idempotent; deleting already-removed entries does not require client retries.

OAuth Scopes: time_tracking.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.hour_entry_ids_schema import HourEntryIdsSchema
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    hour_entry_ids_schema = bamboohr_sdk.HourEntryIdsSchema() # HourEntryIdsSchema | 

    try:
        # Delete Timesheet Hour Entries
        api_instance.delete_timesheet_hour_entries_via_post(hour_entry_ids_schema)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->delete_timesheet_hour_entries_via_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hour_entry_ids_schema** | [**HourEntryIdsSchema**](HourEntryIdsSchema.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Entries deleted successfully. No content returned. |  -  |
**400** | Bad request parameters - missing or invalid hourEntryIds. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Forbidden. Insufficient user permissions or API access is not turned on. |  -  |
**404** | Hour entry not found. |  -  |
**409** | Timesheet type conflict. |  -  |
**412** | Precondition failed - invalid time tracking configuration or timezone. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clock_entry**
> TimeTrackingClockEntryV1 get_clock_entry(id)

Get Clock Entry

Retrieves a single clock entry by its ID. `start`/`end` are ISO 8601 with the offset of the entry's `timezone`; `end` and `clockOutLocation` are null while the entry is open. Geolocation is omitted (null) when the configuration has it disabled.

OAuth Scopes: time_tracking:timesheets

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_clock_entry_v1 import TimeTrackingClockEntryV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 56 # int | The clock entry ID.

    try:
        # Get Clock Entry
        api_response = api_instance.get_clock_entry(id)
        print("The response of TimeTrackingApi->get_clock_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->get_clock_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The clock entry ID. | 

### Return type

[**TimeTrackingClockEntryV1**](TimeTrackingClockEntryV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the clock entry. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | Clock entry not found. |  -  |
**422** | The provided clock entry ID is not a valid positive integer. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hour_entry**
> TimeTrackingHourEntryV1 get_hour_entry(id)

Get Hour Entry

Retrieves a single hour entry by its ID.

OAuth Scopes: time_tracking:timesheets

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_hour_entry_v1 import TimeTrackingHourEntryV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 56 # int | The hour entry ID.

    try:
        # Get Hour Entry
        api_response = api_instance.get_hour_entry(id)
        print("The response of TimeTrackingApi->get_hour_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->get_hour_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The hour entry ID. | 

### Return type

[**TimeTrackingHourEntryV1**](TimeTrackingHourEntryV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the hour entry. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | Hour entry not found. |  -  |
**422** | The provided hour entry ID is not a valid positive integer. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> ProjectTimeTrackingProjectV1 get_project(id)

Get Time Tracking Project

Retrieves a single time tracking project by its ID, including the list of employees assigned to it.

OAuth Scopes: time_tracking:project

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.project_time_tracking_project_v1 import ProjectTimeTrackingProjectV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 56 # int | The project ID.

    try:
        # Get Time Tracking Project
        api_response = api_instance.get_project(id)
        print("The response of TimeTrackingApi->get_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->get_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project ID. | 

### Return type

[**ProjectTimeTrackingProjectV1**](ProjectTimeTrackingProjectV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the project. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | Project not found. |  -  |
**422** | The provided &#x60;id&#x60; is not a valid integer. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shift_differential**
> ShiftDifferentialTimeTrackingShiftDifferentialV1 get_shift_differential(id)

Get Time Tracking Shift Differential

Retrieves a single time tracking shift differential by its ID. Archived shift differentials are returned normally; soft-deleted shift differentials return 404.

OAuth Scopes: time_tracking:shift_differentials

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.shift_differential_time_tracking_shift_differential_v1 import ShiftDifferentialTimeTrackingShiftDifferentialV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 56 # int | The shift differential ID.

    try:
        # Get Time Tracking Shift Differential
        api_response = api_instance.get_shift_differential(id)
        print("The response of TimeTrackingApi->get_shift_differential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->get_shift_differential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The shift differential ID. | 

### Return type

[**ShiftDifferentialTimeTrackingShiftDifferentialV1**](ShiftDifferentialTimeTrackingShiftDifferentialV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the shift differential. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | Shift differential not found. |  -  |
**422** | The provided shift differential ID is not a valid integer. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> ProjectTimeTrackingTaskV1 get_task(id)

Get Time Tracking Task

Retrieves a single time tracking task by its ID.

OAuth Scopes: time_tracking:project

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.project_time_tracking_task_v1 import ProjectTimeTrackingTaskV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 56 # int | The task ID.

    try:
        # Get Time Tracking Task
        api_response = api_instance.get_task(id)
        print("The response of TimeTrackingApi->get_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->get_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The task ID. | 

### Return type

[**ProjectTimeTrackingTaskV1**](ProjectTimeTrackingTaskV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the task. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | Task not found. |  -  |
**422** | The provided &#x60;id&#x60; is not a valid integer. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_tracking_configuration**
> TimeTrackingTimeTrackingConfigurationV1 get_time_tracking_configuration(id)

Get Configuration

Retrieves a single time tracking configuration by its ID. Soft-deleted configurations return 404.

OAuth Scopes: time_tracking:configurations

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_time_tracking_configuration_v1 import TimeTrackingTimeTrackingConfigurationV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 56 # int | The configuration ID.

    try:
        # Get Configuration
        api_response = api_instance.get_time_tracking_configuration(id)
        print("The response of TimeTrackingApi->get_time_tracking_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->get_time_tracking_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The configuration ID. | 

### Return type

[**TimeTrackingTimeTrackingConfigurationV1**](TimeTrackingTimeTrackingConfigurationV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the configuration. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | Configuration not found. |  -  |
**422** | The provided configuration ID is not a valid positive integer. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_tracking_employee_enrollment**
> TimeTrackingEmployeeTimeTrackingDataV1 get_time_tracking_employee_enrollment(employee_id)

Get Employee Enrollment

Gets an employee's time tracking enrollment data.

OAuth Scopes: time_tracking:employees

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_employee_time_tracking_data_v1 import TimeTrackingEmployeeTimeTrackingDataV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    employee_id = 56 # int | The employee ID.

    try:
        # Get Employee Enrollment
        api_response = api_instance.get_time_tracking_employee_enrollment(employee_id)
        print("The response of TimeTrackingApi->get_time_tracking_employee_enrollment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->get_time_tracking_employee_enrollment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| The employee ID. | 

### Return type

[**TimeTrackingEmployeeTimeTrackingDataV1**](TimeTrackingEmployeeTimeTrackingDataV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the employee enrollment. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | The employee has no time tracking enrollment record. |  -  |
**422** | The provided employee ID is not a valid positive integer. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_tracking_kiosk**
> TimeTrackingTimeTrackingKioskV1 get_time_tracking_kiosk(id)

Get Time Tracking Kiosk

Retrieves a single time tracking kiosk by its ID. Deleted kiosks return 404.

OAuth Scopes: time_tracking:kiosks

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_time_tracking_kiosk_v1 import TimeTrackingTimeTrackingKioskV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 'id_example' # str | The time tracking kiosk ID.

    try:
        # Get Time Tracking Kiosk
        api_response = api_instance.get_time_tracking_kiosk(id)
        print("The response of TimeTrackingApi->get_time_tracking_kiosk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->get_time_tracking_kiosk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The time tracking kiosk ID. | 

### Return type

[**TimeTrackingTimeTrackingKioskV1**](TimeTrackingTimeTrackingKioskV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the kiosk. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | Kiosk not found. |  -  |
**422** | The provided kiosk ID is not a valid UUID. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_tracking_time_clock**
> TimeTrackingTimeTrackingTimeClockV1 get_time_tracking_time_clock(id)

Get Time Tracking Time Clock

Retrieves a single time tracking time clock by its ID. Device health flags are reported as null while device status is temporarily unavailable.

OAuth Scopes: time_tracking:time_clocks

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_time_tracking_time_clock_v1 import TimeTrackingTimeTrackingTimeClockV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 'id_example' # str | The time tracking time clock ID.

    try:
        # Get Time Tracking Time Clock
        api_response = api_instance.get_time_tracking_time_clock(id)
        print("The response of TimeTrackingApi->get_time_tracking_time_clock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->get_time_tracking_time_clock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The time tracking time clock ID. | 

### Return type

[**TimeTrackingTimeTrackingTimeClockV1**](TimeTrackingTimeTrackingTimeClockV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the time clock. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | Time clock not found, or the company has no time clocks connected. |  -  |
**422** | The provided time clock ID is not a valid UUID. |  -  |
**503** | Time clock data is temporarily unavailable. Retry after the interval given in the Retry-After header. |  * Retry-After - Seconds to wait before retrying the request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timesheet**
> TimeTrackingTimesheetV1 get_timesheet(id)

Get Timesheet

Retrieves a single timesheet by its ID. The `status` is derived at read time (`OPEN`, `PENDING_APPROVAL`, or `APPROVED`) and `type` is returned in `UPPER_SNAKE_CASE` (`SINGLE`, `CLOCK`, `MULTIPLE`, or `HOUR`). Timesheets for pay periods that have not started yet return 404.

OAuth Scopes: time_tracking:timesheets

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_timesheet_v1 import TimeTrackingTimesheetV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 56 # int | The timesheet ID.

    try:
        # Get Timesheet
        api_response = api_instance.get_timesheet(id)
        print("The response of TimeTrackingApi->get_timesheet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->get_timesheet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The timesheet ID. | 

### Return type

[**TimeTrackingTimesheetV1**](TimeTrackingTimesheetV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the timesheet. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | Timesheet not found, or for a future pay period. |  -  |
**422** | The provided timesheet ID is not a valid positive integer. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timesheet_summary**
> TimesheetTimesheetDailySummaryV1 get_timesheet_summary(id)

Get Timesheet Summary

Returns the daily breakdown of hours for a timesheet, including regular, overtime, and double-time hours per day. Every date in the pay period is represented; days with no logged hours return 0.0 in each bucket.

OAuth Scopes: time_tracking:timesheets

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.timesheet_timesheet_daily_summary_v1 import TimesheetTimesheetDailySummaryV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 56 # int | The timesheet ID.

    try:
        # Get Timesheet Summary
        api_response = api_instance.get_timesheet_summary(id)
        print("The response of TimeTrackingApi->get_timesheet_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->get_timesheet_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The timesheet ID. | 

### Return type

[**TimesheetTimesheetDailySummaryV1**](TimesheetTimesheetDailySummaryV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the timesheet summary. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | Timesheet not found, or its pay period has not started yet. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_clock_entries**
> TimeTrackingPaginatedClockEntriesResponseV1 list_clock_entries(filter=filter, sort=sort, page=page, page_size=page_size)

List Clock Entries

Returns a paginated list of time tracking clock entries. Supports OData-style `filter` and `sort` query parameters. Pagination is page-based via `page` and `pageSize` (defaults: page 1, pageSize 50, min 10, max 200). Filterable fields: `timesheetId`, `employeeId`, `start`, `end`. Sortable fields: `start`, `end`, `updatedAt`. Default sort is `start desc`. Geolocation is omitted (null) for entries whose configuration has it disabled.

OAuth Scopes: time_tracking:timesheets

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_paginated_clock_entries_response_v1 import TimeTrackingPaginatedClockEntriesResponseV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    filter = 'filter_example' # str | OData v4 filter expression. Supported operators: `eq`, `ge`, `le`, `and`. Filterable fields: `timesheetId`, `employeeId`, `start`, `end`. Examples: `employeeId eq 40342`, `start ge 2026-03-16T00:00:00Z and start le 2026-03-29T23:59:59Z`, `timesheetId eq 9001`. (optional)
    sort = 'sort_example' # str | Sort expression like `start desc` or `updatedAt asc`. Allowed fields: `start`, `end`, `updatedAt`. Defaults to `start desc`. (optional)
    page = 1 # int | The page number to retrieve. Defaults to 1. (optional) (default to 1)
    page_size = 50 # int | The number of items per page. Defaults to 50, minimum 10, maximum 200. (optional) (default to 50)

    try:
        # List Clock Entries
        api_response = api_instance.list_clock_entries(filter=filter, sort=sort, page=page, page_size=page_size)
        print("The response of TimeTrackingApi->list_clock_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->list_clock_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| OData v4 filter expression. Supported operators: &#x60;eq&#x60;, &#x60;ge&#x60;, &#x60;le&#x60;, &#x60;and&#x60;. Filterable fields: &#x60;timesheetId&#x60;, &#x60;employeeId&#x60;, &#x60;start&#x60;, &#x60;end&#x60;. Examples: &#x60;employeeId eq 40342&#x60;, &#x60;start ge 2026-03-16T00:00:00Z and start le 2026-03-29T23:59:59Z&#x60;, &#x60;timesheetId eq 9001&#x60;. | [optional] 
 **sort** | **str**| Sort expression like &#x60;start desc&#x60; or &#x60;updatedAt asc&#x60;. Allowed fields: &#x60;start&#x60;, &#x60;end&#x60;, &#x60;updatedAt&#x60;. Defaults to &#x60;start desc&#x60;. | [optional] 
 **page** | **int**| The page number to retrieve. Defaults to 1. | [optional] [default to 1]
 **page_size** | **int**| The number of items per page. Defaults to 50, minimum 10, maximum 200. | [optional] [default to 50]

### Return type

[**TimeTrackingPaginatedClockEntriesResponseV1**](TimeTrackingPaginatedClockEntriesResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of clock entries. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**422** | Invalid query parameters. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_hour_entries**
> TimeTrackingPaginatedHourEntriesResponseV1 list_hour_entries(filter=filter, sort=sort, page=page, page_size=page_size)

List Hour Entries

Returns a paginated list of time tracking hour entries. Supports OData-style `filter` and `sort` query parameters. Pagination is page-based via `page` and `pageSize` (defaults: page 1, pageSize 50, min 10, max 200). Filterable fields: `timesheetId`, `employeeId`, `date`. Sortable fields: `date`, `updatedAt`. Default sort is `date desc`.

OAuth Scopes: time_tracking:timesheets

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_paginated_hour_entries_response_v1 import TimeTrackingPaginatedHourEntriesResponseV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    filter = 'filter_example' # str | OData v4 filter expression. Supported operators: `eq`, `ge`, `le`, `and`. Filterable fields: `timesheetId`, `employeeId`, `date`. Examples: `employeeId eq 40342`, `date ge 2025-01-01 and date le 2025-01-31`, `timesheetId eq 9001`. (optional)
    sort = 'sort_example' # str | Sort expression like `date desc` or `updatedAt asc`. Allowed fields: `date`, `updatedAt`. Defaults to `date desc`. (optional)
    page = 1 # int | The page number to retrieve. Defaults to 1. (optional) (default to 1)
    page_size = 50 # int | The number of items per page. Defaults to 50, minimum 10, maximum 200. (optional) (default to 50)

    try:
        # List Hour Entries
        api_response = api_instance.list_hour_entries(filter=filter, sort=sort, page=page, page_size=page_size)
        print("The response of TimeTrackingApi->list_hour_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->list_hour_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| OData v4 filter expression. Supported operators: &#x60;eq&#x60;, &#x60;ge&#x60;, &#x60;le&#x60;, &#x60;and&#x60;. Filterable fields: &#x60;timesheetId&#x60;, &#x60;employeeId&#x60;, &#x60;date&#x60;. Examples: &#x60;employeeId eq 40342&#x60;, &#x60;date ge 2025-01-01 and date le 2025-01-31&#x60;, &#x60;timesheetId eq 9001&#x60;. | [optional] 
 **sort** | **str**| Sort expression like &#x60;date desc&#x60; or &#x60;updatedAt asc&#x60;. Allowed fields: &#x60;date&#x60;, &#x60;updatedAt&#x60;. Defaults to &#x60;date desc&#x60;. | [optional] 
 **page** | **int**| The page number to retrieve. Defaults to 1. | [optional] [default to 1]
 **page_size** | **int**| The number of items per page. Defaults to 50, minimum 10, maximum 200. | [optional] [default to 50]

### Return type

[**TimeTrackingPaginatedHourEntriesResponseV1**](TimeTrackingPaginatedHourEntriesResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of hour entries. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**422** | Invalid query parameters. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_tasks**
> ProjectPaginatedTasksResponseV1 list_project_tasks(project_id, statuses=statuses, page=page, page_size=page_size)

List Time Tracking Project Tasks

Returns a paginated list of tasks for the specified time tracking project. Tasks are filtered by `statuses[]`, which defaults to `active`.

OAuth Scopes: time_tracking:project

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.project_paginated_tasks_response_v1 import ProjectPaginatedTasksResponseV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    project_id = 56 # int | The project ID.
    statuses = ["active"] # List[str] | Statuses to include. Defaults to `active` (excludes deleted tasks). Use both values to include active and deleted tasks. (optional) (default to ["active"])
    page = 1 # int | The page number to retrieve (1-indexed). (optional) (default to 1)
    page_size = 25 # int | The maximum number of items per page. (optional) (default to 25)

    try:
        # List Time Tracking Project Tasks
        api_response = api_instance.list_project_tasks(project_id, statuses=statuses, page=page, page_size=page_size)
        print("The response of TimeTrackingApi->list_project_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->list_project_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The project ID. | 
 **statuses** | [**List[str]**](str.md)| Statuses to include. Defaults to &#x60;active&#x60; (excludes deleted tasks). Use both values to include active and deleted tasks. | [optional] [default to [&quot;active&quot;]]
 **page** | **int**| The page number to retrieve (1-indexed). | [optional] [default to 1]
 **page_size** | **int**| The maximum number of items per page. | [optional] [default to 25]

### Return type

[**ProjectPaginatedTasksResponseV1**](ProjectPaginatedTasksResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved tasks for the project. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | Project not found. |  -  |
**422** | A query parameter is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> ProjectPaginatedTimeTrackingProjectsResponseV1 list_projects(filter=filter, sort=sort, page=page, page_size=page_size)

List Time Tracking Projects

Returns a paginated list of time tracking projects. Supports OData-style `filter` and `sort` query parameters. Pagination is page-based via `page` and `pageSize` (defaults: page 1, pageSize 100, max 500).

OAuth Scopes: time_tracking:project

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.project_paginated_time_tracking_projects_response_v1 import ProjectPaginatedTimeTrackingProjectsResponseV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    filter = 'filter_example' # str | OData v4 filter expression. Filterable fields: `id`, `name`, `billable`, `includeInPayroll`, `allEmployeesAssigned`, `archived`, `createdAt`, `updatedAt`. (optional)
    sort = 'sort_example' # str | Sort expression like `name asc, createdAt desc`. Allowed fields: `name`, `createdAt`, `updatedAt`. (optional)
    page = 1 # int | The starting page for pagination. Defaults to 1. (optional) (default to 1)
    page_size = 100 # int | The number of items per page. Defaults to 100, maximum 500. (optional) (default to 100)

    try:
        # List Time Tracking Projects
        api_response = api_instance.list_projects(filter=filter, sort=sort, page=page, page_size=page_size)
        print("The response of TimeTrackingApi->list_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->list_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| OData v4 filter expression. Filterable fields: &#x60;id&#x60;, &#x60;name&#x60;, &#x60;billable&#x60;, &#x60;includeInPayroll&#x60;, &#x60;allEmployeesAssigned&#x60;, &#x60;archived&#x60;, &#x60;createdAt&#x60;, &#x60;updatedAt&#x60;. | [optional] 
 **sort** | **str**| Sort expression like &#x60;name asc, createdAt desc&#x60;. Allowed fields: &#x60;name&#x60;, &#x60;createdAt&#x60;, &#x60;updatedAt&#x60;. | [optional] 
 **page** | **int**| The starting page for pagination. Defaults to 1. | [optional] [default to 1]
 **page_size** | **int**| The number of items per page. Defaults to 100, maximum 500. | [optional] [default to 100]

### Return type

[**ProjectPaginatedTimeTrackingProjectsResponseV1**](ProjectPaginatedTimeTrackingProjectsResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of projects. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**422** | Invalid query parameters (e.g., invalid &#x60;page&#x60;, &#x60;pageSize&#x60;, &#x60;filter&#x60;, or &#x60;sort&#x60;). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shift_differentials**
> ShiftDifferentialPaginatedTimeTrackingShiftDifferentialsResponseV1 list_shift_differentials(filter=filter, sort=sort, page=page, page_size=page_size)

List Time Tracking Shift Differentials

Returns a paginated list of time tracking shift differentials. Supports OData-style `filter` and `sort` query parameters. Pagination is page-based via `page` and `pageSize` (defaults: page 1, pageSize 20, max 100). Archived rows are excluded by default; include them with `filter=archived eq true`. Soft-deleted rows are never returned.

OAuth Scopes: time_tracking:shift_differentials

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.shift_differential_paginated_time_tracking_shift_differentials_response_v1 import ShiftDifferentialPaginatedTimeTrackingShiftDifferentialsResponseV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    filter = 'filter_example' # str | OData v4 filter expression. Filterable fields: `name`, `rate`, `rateType`, `archived`. (optional)
    sort = 'sort_example' # str | Sort expression like `name asc, createdAt desc`. Allowed fields: `name`, `createdAt`, `updatedAt`. (optional)
    page = 1 # int | The starting page for pagination. Defaults to 1. (optional) (default to 1)
    page_size = 20 # int | The number of items per page. Defaults to 20, maximum 100. (optional) (default to 20)

    try:
        # List Time Tracking Shift Differentials
        api_response = api_instance.list_shift_differentials(filter=filter, sort=sort, page=page, page_size=page_size)
        print("The response of TimeTrackingApi->list_shift_differentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->list_shift_differentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| OData v4 filter expression. Filterable fields: &#x60;name&#x60;, &#x60;rate&#x60;, &#x60;rateType&#x60;, &#x60;archived&#x60;. | [optional] 
 **sort** | **str**| Sort expression like &#x60;name asc, createdAt desc&#x60;. Allowed fields: &#x60;name&#x60;, &#x60;createdAt&#x60;, &#x60;updatedAt&#x60;. | [optional] 
 **page** | **int**| The starting page for pagination. Defaults to 1. | [optional] [default to 1]
 **page_size** | **int**| The number of items per page. Defaults to 20, maximum 100. | [optional] [default to 20]

### Return type

[**ShiftDifferentialPaginatedTimeTrackingShiftDifferentialsResponseV1**](ShiftDifferentialPaginatedTimeTrackingShiftDifferentialsResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of shift differentials. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**422** | Invalid query parameters (e.g., invalid &#x60;page&#x60;, &#x60;pageSize&#x60;, &#x60;filter&#x60;, or &#x60;sort&#x60;). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_time_tracking_configurations**
> TimeTrackingPaginatedTimeTrackingConfigurationsResponseV1 list_time_tracking_configurations(filter=filter, order_by=order_by, select=select, page=page, page_size=page_size)

List Configurations

Returns a paginated list of time tracking configurations. Both GLOBAL and GROUP configurations are returned; soft-deleted configurations are never returned. Supports an OData-style `filter`, an `orderBy` sort expression, and `select` sparse fieldsets. Pagination is page-based via `page` and `pageSize` (defaults: page 1, pageSize 20, max 100).

OAuth Scopes: time_tracking:configurations

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_paginated_time_tracking_configurations_response_v1 import TimeTrackingPaginatedTimeTrackingConfigurationsResponseV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    filter = 'filter_example' # str | OData v4 filter expression. Filterable fields: `name`, `type`, `timesheetType`. Example: `type eq 'GROUP' and timesheetType eq 'CLOCK'`. (optional)
    order_by = 'order_by_example' # str | Sort expression like `name asc, createdAt desc`. Allowed fields: `name`, `createdAt`, `updatedAt`. (optional)
    select = 'select_example' # str | Comma-separated list of properties to return (sparse fieldsets). (optional)
    page = 1 # int | The page to return. Defaults to 1. (optional) (default to 1)
    page_size = 20 # int | The number of items per page. Defaults to 20, maximum 100. (optional) (default to 20)

    try:
        # List Configurations
        api_response = api_instance.list_time_tracking_configurations(filter=filter, order_by=order_by, select=select, page=page, page_size=page_size)
        print("The response of TimeTrackingApi->list_time_tracking_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->list_time_tracking_configurations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| OData v4 filter expression. Filterable fields: &#x60;name&#x60;, &#x60;type&#x60;, &#x60;timesheetType&#x60;. Example: &#x60;type eq &#39;GROUP&#39; and timesheetType eq &#39;CLOCK&#39;&#x60;. | [optional] 
 **order_by** | **str**| Sort expression like &#x60;name asc, createdAt desc&#x60;. Allowed fields: &#x60;name&#x60;, &#x60;createdAt&#x60;, &#x60;updatedAt&#x60;. | [optional] 
 **select** | **str**| Comma-separated list of properties to return (sparse fieldsets). | [optional] 
 **page** | **int**| The page to return. Defaults to 1. | [optional] [default to 1]
 **page_size** | **int**| The number of items per page. Defaults to 20, maximum 100. | [optional] [default to 20]

### Return type

[**TimeTrackingPaginatedTimeTrackingConfigurationsResponseV1**](TimeTrackingPaginatedTimeTrackingConfigurationsResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of time tracking configurations. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**422** | Invalid query parameters (e.g., invalid &#x60;page&#x60;, &#x60;pageSize&#x60;, &#x60;filter&#x60;, &#x60;orderBy&#x60;, or &#x60;select&#x60;). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_time_tracking_employees**
> TimeTrackingPaginatedEmployeeTimeTrackingDataResponseV1 list_time_tracking_employees(filter=filter, order_by=order_by, select=select, page=page, page_size=page_size)

List Enrolled Employees

Returns a paginated list of employee time tracking enrollments. Both enabled and disabled enrollments are returned; narrow with the `enabled` filter. Supports an OData-style `filter`, an `orderBy` sort expression, and `select` sparse fieldsets. Pagination is page-based via `page` and `pageSize` (defaults: page 1, pageSize 20, minimum 10, maximum 100).

OAuth Scopes: time_tracking:employees

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_paginated_employee_time_tracking_data_response_v1 import TimeTrackingPaginatedEmployeeTimeTrackingDataResponseV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    filter = 'filter_example' # str | OData v4 filter expression. Filterable fields: `enabled`, `configurationId`. Example: `enabled eq true and configurationId eq 3`. (optional)
    order_by = 'order_by_example' # str | Sort expression like `employeeId asc, createdAt desc`. Allowed fields: `employeeId`, `enabledOn`, `createdAt`, `updatedAt`. (optional)
    select = 'select_example' # str | Comma-separated list of properties to return (sparse fieldsets). (optional)
    page = 1 # int | The page to return. Defaults to 1. (optional) (default to 1)
    page_size = 20 # int | The number of items per page. Defaults to 20, minimum 10, maximum 100. (optional) (default to 20)

    try:
        # List Enrolled Employees
        api_response = api_instance.list_time_tracking_employees(filter=filter, order_by=order_by, select=select, page=page, page_size=page_size)
        print("The response of TimeTrackingApi->list_time_tracking_employees:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->list_time_tracking_employees: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| OData v4 filter expression. Filterable fields: &#x60;enabled&#x60;, &#x60;configurationId&#x60;. Example: &#x60;enabled eq true and configurationId eq 3&#x60;. | [optional] 
 **order_by** | **str**| Sort expression like &#x60;employeeId asc, createdAt desc&#x60;. Allowed fields: &#x60;employeeId&#x60;, &#x60;enabledOn&#x60;, &#x60;createdAt&#x60;, &#x60;updatedAt&#x60;. | [optional] 
 **select** | **str**| Comma-separated list of properties to return (sparse fieldsets). | [optional] 
 **page** | **int**| The page to return. Defaults to 1. | [optional] [default to 1]
 **page_size** | **int**| The number of items per page. Defaults to 20, minimum 10, maximum 100. | [optional] [default to 20]

### Return type

[**TimeTrackingPaginatedEmployeeTimeTrackingDataResponseV1**](TimeTrackingPaginatedEmployeeTimeTrackingDataResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of employee time tracking enrollments. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**422** | Invalid query parameters (e.g., invalid &#x60;page&#x60;, &#x60;pageSize&#x60;, &#x60;filter&#x60;, &#x60;orderBy&#x60;, or &#x60;select&#x60;). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_time_tracking_kiosks**
> TimeTrackingPaginatedTimeTrackingKiosksResponseV1 list_time_tracking_kiosks(filter=filter, order_by=order_by, select=select, page=page, page_size=page_size)

List Time Tracking Kiosks

Returns a paginated list of time tracking kiosks. Deleted kiosks are never returned. Supports an OData-style `filter`, an `orderBy` sort expression, and `select` sparse fieldsets. Results are sorted by name ascending when `orderBy` is omitted; name ordering is case-insensitive. Pagination is page-based via `page` and `pageSize` (defaults: page 1, pageSize 20, max 100).

OAuth Scopes: time_tracking:kiosks

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_paginated_time_tracking_kiosks_response_v1 import TimeTrackingPaginatedTimeTrackingKiosksResponseV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    filter = 'filter_example' # str | OData v4 filter expression. Filterable fields: `name`, `lastUsed`, `createdAt`, `updatedAt`. Example: `name eq 'Front Desk Kiosk'`. (optional)
    order_by = 'order_by_example' # str | Sort expression like `name asc, createdAt desc`. Allowed fields: `name`, `lastUsed`, `createdAt`, `updatedAt`. Defaults to `name asc`. (optional)
    select = 'select_example' # str | Comma-separated list of properties to return (sparse fieldsets). (optional)
    page = 1 # int | The page to retrieve. Defaults to 1. (optional) (default to 1)
    page_size = 20 # int | The number of kiosks per page. Defaults to 20, minimum 10, maximum 100. (optional) (default to 20)

    try:
        # List Time Tracking Kiosks
        api_response = api_instance.list_time_tracking_kiosks(filter=filter, order_by=order_by, select=select, page=page, page_size=page_size)
        print("The response of TimeTrackingApi->list_time_tracking_kiosks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->list_time_tracking_kiosks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| OData v4 filter expression. Filterable fields: &#x60;name&#x60;, &#x60;lastUsed&#x60;, &#x60;createdAt&#x60;, &#x60;updatedAt&#x60;. Example: &#x60;name eq &#39;Front Desk Kiosk&#39;&#x60;. | [optional] 
 **order_by** | **str**| Sort expression like &#x60;name asc, createdAt desc&#x60;. Allowed fields: &#x60;name&#x60;, &#x60;lastUsed&#x60;, &#x60;createdAt&#x60;, &#x60;updatedAt&#x60;. Defaults to &#x60;name asc&#x60;. | [optional] 
 **select** | **str**| Comma-separated list of properties to return (sparse fieldsets). | [optional] 
 **page** | **int**| The page to retrieve. Defaults to 1. | [optional] [default to 1]
 **page_size** | **int**| The number of kiosks per page. Defaults to 20, minimum 10, maximum 100. | [optional] [default to 20]

### Return type

[**TimeTrackingPaginatedTimeTrackingKiosksResponseV1**](TimeTrackingPaginatedTimeTrackingKiosksResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of kiosks. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**422** | Invalid query parameters (e.g., invalid &#x60;page&#x60;, &#x60;pageSize&#x60;, &#x60;filter&#x60;, &#x60;orderBy&#x60;, or &#x60;select&#x60;). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_time_tracking_time_clocks**
> TimeTrackingPaginatedTimeTrackingTimeClocksResponseV1 list_time_tracking_time_clocks(filter=filter, order_by=order_by, select=select, page=page, page_size=page_size)

List Time Tracking Time Clocks

Returns a paginated list of the company's time tracking time clocks. Supports an OData-style `filter`, an `orderBy` sort expression, and `select` sparse fieldsets. Results are sorted by name ascending when `orderBy` is omitted; name ordering is case-insensitive. Filtering and sorting are applied in memory over the cached GT Connect list (partner ordering is not relied on). A company with no GT Clocks connected returns an empty list, not a 404. Device health flags are reported as null while device status is temporarily unavailable. Pagination is page-based via `page` and `pageSize` (defaults: page 1, pageSize 20, minimum 10, maximum 100).

OAuth Scopes: time_tracking:time_clocks

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_paginated_time_tracking_time_clocks_response_v1 import TimeTrackingPaginatedTimeTrackingTimeClocksResponseV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    filter = 'filter_example' # str | OData v4 filter expression. Filterable fields: `name`, `serialNumber`, `type`, `timezone`. Example: `type eq 'TIME_CLOCK'`. (optional)
    order_by = 'order_by_example' # str | Sort expression like `name asc, serialNumber desc`. Allowed fields: `name`, `serialNumber`, `type`, `timezone`. Defaults to `name asc`. (optional)
    select = 'select_example' # str | Comma-separated list of properties to return (sparse fieldsets). (optional)
    page = 1 # int | The page to retrieve. Defaults to 1. (optional) (default to 1)
    page_size = 20 # int | The number of time clocks per page. Defaults to 20, minimum 10, maximum 100. (optional) (default to 20)

    try:
        # List Time Tracking Time Clocks
        api_response = api_instance.list_time_tracking_time_clocks(filter=filter, order_by=order_by, select=select, page=page, page_size=page_size)
        print("The response of TimeTrackingApi->list_time_tracking_time_clocks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->list_time_tracking_time_clocks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| OData v4 filter expression. Filterable fields: &#x60;name&#x60;, &#x60;serialNumber&#x60;, &#x60;type&#x60;, &#x60;timezone&#x60;. Example: &#x60;type eq &#39;TIME_CLOCK&#39;&#x60;. | [optional] 
 **order_by** | **str**| Sort expression like &#x60;name asc, serialNumber desc&#x60;. Allowed fields: &#x60;name&#x60;, &#x60;serialNumber&#x60;, &#x60;type&#x60;, &#x60;timezone&#x60;. Defaults to &#x60;name asc&#x60;. | [optional] 
 **select** | **str**| Comma-separated list of properties to return (sparse fieldsets). | [optional] 
 **page** | **int**| The page to retrieve. Defaults to 1. | [optional] [default to 1]
 **page_size** | **int**| The number of time clocks per page. Defaults to 20, minimum 10, maximum 100. | [optional] [default to 20]

### Return type

[**TimeTrackingPaginatedTimeTrackingTimeClocksResponseV1**](TimeTrackingPaginatedTimeTrackingTimeClocksResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of time clocks. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**422** | Invalid query parameters (e.g., invalid &#x60;page&#x60;, &#x60;pageSize&#x60;, &#x60;filter&#x60;, &#x60;orderBy&#x60;, or &#x60;select&#x60;). |  -  |
**503** | Time clock data is temporarily unavailable. Retry after the interval given in the Retry-After header. |  * Retry-After - Seconds to wait before retrying the request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_timesheet_entries**
> List[EmployeeTimesheetEntryTransformer] list_timesheet_entries(start, end, employee_ids=employee_ids)

List Timesheet Entries

Returns timesheet entries for all employees, or a filtered subset, within the specified date range. Results include both clock and hour entry types. Dates must fall within the last 365 days and are interpreted in the company timezone.

OAuth Scopes: time_tracking

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.employee_timesheet_entry_transformer import EmployeeTimesheetEntryTransformer
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    start = '2025-01-01' # date | YYYY-MM-DD. Only show timesheet entries on/after the specified start date. Must be within the last 365 days.
    end = '2025-03-01' # date | YYYY-MM-DD. Only show timesheet entries on/before the specified end date. Must be within the last 365 days.
    employee_ids = '1,2,3' # str | A comma-separated list of internal employee IDs. When specified, only entries that match these employee IDs are returned. When omitted, entries for all accessible employees are returned. (optional)

    try:
        # List Timesheet Entries
        api_response = api_instance.list_timesheet_entries(start, end, employee_ids=employee_ids)
        print("The response of TimeTrackingApi->list_timesheet_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->list_timesheet_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| YYYY-MM-DD. Only show timesheet entries on/after the specified start date. Must be within the last 365 days. | 
 **end** | **date**| YYYY-MM-DD. Only show timesheet entries on/before the specified end date. Must be within the last 365 days. | 
 **employee_ids** | **str**| A comma-separated list of internal employee IDs. When specified, only entries that match these employee IDs are returned. When omitted, entries for all accessible employees are returned. | [optional] 

### Return type

[**List[EmployeeTimesheetEntryTransformer]**](EmployeeTimesheetEntryTransformer.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the matching timesheet entries grouped by employee. |  -  |
**400** | Bad request parameters - invalid dates, date range exceeds 365 days, or malformed employeeIds. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_timesheets**
> TimeTrackingPaginatedTimesheetsResponseV1 list_timesheets(filter=filter, sort=sort, page=page, page_size=page_size)

List Timesheets

Returns a paginated list of timesheets. Supports OData-style `filter` (fields: `employeeId`, `status`, `startDate`, `endDate`) and `sort` (fields: `startDate`, `endDate`, `approvedAt`, `updatedAt`; default `startDate desc`). Page-based pagination via `page` (default 1) and `pageSize` (default 50, max 200). Future-period timesheets are always excluded.

OAuth Scopes: time_tracking:timesheets

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_paginated_timesheets_response_v1 import TimeTrackingPaginatedTimesheetsResponseV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    filter = 'filter_example' # str | OData-style filter expression. (optional)
    sort = 'sort_example' # str | Sort expression. Default: startDate desc. (optional)
    page = 1 # int | Page number (1-based). (optional) (default to 1)
    page_size = 50 # int | Records per page (max 200). (optional) (default to 50)

    try:
        # List Timesheets
        api_response = api_instance.list_timesheets(filter=filter, sort=sort, page=page, page_size=page_size)
        print("The response of TimeTrackingApi->list_timesheets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->list_timesheets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| OData-style filter expression. | [optional] 
 **sort** | **str**| Sort expression. Default: startDate desc. | [optional] 
 **page** | **int**| Page number (1-based). | [optional] [default to 1]
 **page_size** | **int**| Records per page (max 200). | [optional] [default to 50]

### Return type

[**TimeTrackingPaginatedTimesheetsResponseV1**](TimeTrackingPaginatedTimesheetsResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the timesheets. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**422** | Invalid query parameters (filter, sort, page, or pageSize). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_clock_entry**
> TimeTrackingClockEntryV1 update_clock_entry(id, time_tracking_update_clock_entry_v1)

Update Clock Entry

Partially updates a time tracking clock entry identified by its ID. Only the fields present in the body are changed. When `start` or `timezone` change, the entry's `date` and `timesheetId` are recomputed server-side and the entry is moved to the matching timesheet. Pass `null` for `clockInLocation` / `clockOutLocation` to clear the stored geolocation.

OAuth Scopes: time_tracking:timesheets.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_clock_entry_v1 import TimeTrackingClockEntryV1
from bamboohr_sdk.models.time_tracking_update_clock_entry_v1 import TimeTrackingUpdateClockEntryV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 56 # int | The clock entry ID.
    time_tracking_update_clock_entry_v1 = bamboohr_sdk.TimeTrackingUpdateClockEntryV1() # TimeTrackingUpdateClockEntryV1 | 

    try:
        # Update Clock Entry
        api_response = api_instance.update_clock_entry(id, time_tracking_update_clock_entry_v1)
        print("The response of TimeTrackingApi->update_clock_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->update_clock_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The clock entry ID. | 
 **time_tracking_update_clock_entry_v1** | [**TimeTrackingUpdateClockEntryV1**](TimeTrackingUpdateClockEntryV1.md)|  | 

### Return type

[**TimeTrackingClockEntryV1**](TimeTrackingClockEntryV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated clock entry. |  -  |
**400** | Malformed request body. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | Clock entry not found. |  -  |
**409** | Conflict. The parent timesheet is already approved, the entry overlaps another, or the timesheet does not accept clock entries. |  -  |
**422** | Validation error (e.g., invalid time range, invalid timezone, accuracy greater than 10000, or a missing updatable field). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hour_entry**
> TimeTrackingHourEntryV1 update_hour_entry(id, hour_entry_patch_hour_entry_v1)

Update Hour Entry

Partially updates a time tracking hour entry identified by its ID. Only the fields present in the body are changed; the rest retain their prior values. Moving the entry to a date in a different pay period updates the returned timesheetId.

OAuth Scopes: time_tracking:timesheets.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.hour_entry_patch_hour_entry_v1 import HourEntryPatchHourEntryV1
from bamboohr_sdk.models.time_tracking_hour_entry_v1 import TimeTrackingHourEntryV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 56 # int | The hour entry ID.
    hour_entry_patch_hour_entry_v1 = bamboohr_sdk.HourEntryPatchHourEntryV1() # HourEntryPatchHourEntryV1 | 

    try:
        # Update Hour Entry
        api_response = api_instance.update_hour_entry(id, hour_entry_patch_hour_entry_v1)
        print("The response of TimeTrackingApi->update_hour_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->update_hour_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The hour entry ID. | 
 **hour_entry_patch_hour_entry_v1** | [**HourEntryPatchHourEntryV1**](HourEntryPatchHourEntryV1.md)|  | 

### Return type

[**TimeTrackingHourEntryV1**](TimeTrackingHourEntryV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hour entry updated successfully. |  -  |
**400** | Malformed request body. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions, or the parent timesheet is already approved. |  -  |
**404** | Hour entry not found, or no timesheet covering the requested date exists for the employee. |  -  |
**409** | Conflict. The destination timesheet type is CLOCK or MULTIPLE, or a single-entry timesheet already has an entry for the date. |  -  |
**422** | Validation error (e.g., hours &lt;&#x3D; 0, malformed date, taskId not under projectId, no fields provided, or employeeId present). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> ProjectTimeTrackingProjectV1 update_project(id, project_update_time_tracking_project_v1)

Update Time Tracking Project

Partially updates a time tracking project identified by its ID. Only fields provided in the request body are updated; omitted fields are left unchanged.

OAuth Scopes: time_tracking:project.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.project_time_tracking_project_v1 import ProjectTimeTrackingProjectV1
from bamboohr_sdk.models.project_update_time_tracking_project_v1 import ProjectUpdateTimeTrackingProjectV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 56 # int | The project ID.
    project_update_time_tracking_project_v1 = bamboohr_sdk.ProjectUpdateTimeTrackingProjectV1() # ProjectUpdateTimeTrackingProjectV1 | 

    try:
        # Update Time Tracking Project
        api_response = api_instance.update_project(id, project_update_time_tracking_project_v1)
        print("The response of TimeTrackingApi->update_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->update_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The project ID. | 
 **project_update_time_tracking_project_v1** | [**ProjectUpdateTimeTrackingProjectV1**](ProjectUpdateTimeTrackingProjectV1.md)|  | 

### Return type

[**ProjectTimeTrackingProjectV1**](ProjectTimeTrackingProjectV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the project. |  -  |
**400** | Malformed request body. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | Project not found. |  -  |
**409** | A project with the supplied name already exists. |  -  |
**422** | Validation error (e.g., invalid &#x60;projectId&#x60;, no fields provided, invalid types, or setting &#x60;hasTasks&#x3D;true&#x60; on a project with no active tasks). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shift_differential**
> ShiftDifferentialTimeTrackingShiftDifferentialV1 update_shift_differential(id, shift_differential_update_time_tracking_shift_differential_v1)

Update Time Tracking Shift Differential

Partially updates a time tracking shift differential identified by its ID.

OAuth Scopes: time_tracking:shift_differentials.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.shift_differential_time_tracking_shift_differential_v1 import ShiftDifferentialTimeTrackingShiftDifferentialV1
from bamboohr_sdk.models.shift_differential_update_time_tracking_shift_differential_v1 import ShiftDifferentialUpdateTimeTrackingShiftDifferentialV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 56 # int | The shift differential ID.
    shift_differential_update_time_tracking_shift_differential_v1 = bamboohr_sdk.ShiftDifferentialUpdateTimeTrackingShiftDifferentialV1() # ShiftDifferentialUpdateTimeTrackingShiftDifferentialV1 | 

    try:
        # Update Time Tracking Shift Differential
        api_response = api_instance.update_shift_differential(id, shift_differential_update_time_tracking_shift_differential_v1)
        print("The response of TimeTrackingApi->update_shift_differential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->update_shift_differential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The shift differential ID. | 
 **shift_differential_update_time_tracking_shift_differential_v1** | [**ShiftDifferentialUpdateTimeTrackingShiftDifferentialV1**](ShiftDifferentialUpdateTimeTrackingShiftDifferentialV1.md)|  | 

### Return type

[**ShiftDifferentialTimeTrackingShiftDifferentialV1**](ShiftDifferentialTimeTrackingShiftDifferentialV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Shift differential updated successfully. |  -  |
**400** | Malformed request body. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | Shift differential not found. |  -  |
**409** | Conflict. A shift differential with the provided name already exists. |  -  |
**422** | Validation error (e.g., invalid &#x60;rate&#x60;, invalid &#x60;times&#x60;, no fields provided). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task**
> ProjectTimeTrackingTaskV1 update_task(id, project_update_time_tracking_project_task_v1)

Update Time Tracking Task

Partially updates a time tracking task identified by its ID. Only fields provided in the request body are updated; at least one field must be provided.

OAuth Scopes: time_tracking:project.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.project_time_tracking_task_v1 import ProjectTimeTrackingTaskV1
from bamboohr_sdk.models.project_update_time_tracking_project_task_v1 import ProjectUpdateTimeTrackingProjectTaskV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 56 # int | The task ID.
    project_update_time_tracking_project_task_v1 = bamboohr_sdk.ProjectUpdateTimeTrackingProjectTaskV1() # ProjectUpdateTimeTrackingProjectTaskV1 | 

    try:
        # Update Time Tracking Task
        api_response = api_instance.update_task(id, project_update_time_tracking_project_task_v1)
        print("The response of TimeTrackingApi->update_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->update_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The task ID. | 
 **project_update_time_tracking_project_task_v1** | [**ProjectUpdateTimeTrackingProjectTaskV1**](ProjectUpdateTimeTrackingProjectTaskV1.md)|  | 

### Return type

[**ProjectTimeTrackingTaskV1**](ProjectTimeTrackingTaskV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task updated. |  -  |
**403** | Forbidden. |  -  |
**404** | Task not found. |  -  |
**409** | Duplicate task name within the project. |  -  |
**422** | Validation error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_time_tracking_configuration**
> TimeTrackingTimeTrackingConfigurationV1 update_time_tracking_configuration(id, time_tracking_update_time_tracking_configuration_v1)

Update Configuration

Updates a time tracking configuration using JSON Merge Patch (RFC 7396) semantics: only the properties present in the body are applied, omitted properties are unchanged, and an explicit null clears a nullable property. Both GLOBAL and GROUP configurations can be updated. Content-Type: application/merge-patch+json is preferred because it names those semantics, but application/json is also accepted.

OAuth Scopes: time_tracking:configurations.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_time_tracking_configuration_v1 import TimeTrackingTimeTrackingConfigurationV1
from bamboohr_sdk.models.time_tracking_update_time_tracking_configuration_v1 import TimeTrackingUpdateTimeTrackingConfigurationV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 56 # int | The time tracking configuration ID.
    time_tracking_update_time_tracking_configuration_v1 = bamboohr_sdk.TimeTrackingUpdateTimeTrackingConfigurationV1() # TimeTrackingUpdateTimeTrackingConfigurationV1 | 

    try:
        # Update Configuration
        api_response = api_instance.update_time_tracking_configuration(id, time_tracking_update_time_tracking_configuration_v1)
        print("The response of TimeTrackingApi->update_time_tracking_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->update_time_tracking_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The time tracking configuration ID. | 
 **time_tracking_update_time_tracking_configuration_v1** | [**TimeTrackingUpdateTimeTrackingConfigurationV1**](TimeTrackingUpdateTimeTrackingConfigurationV1.md)|  | 

### Return type

[**TimeTrackingTimeTrackingConfigurationV1**](TimeTrackingTimeTrackingConfigurationV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated configuration. |  -  |
**400** | Malformed request body. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | Configuration not found, or soft-deleted. |  -  |
**409** | Conflict. Another configuration already uses the new name. |  -  |
**422** | Validation error (e.g., an invalid field value, patching the read-only type or employeeIds, missing approverUserId when setting approverType to SPECIFIC_PERSON, or an overtime threshold set while customOvertimeEnabled is false). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_time_tracking_employee_enrollment**
> TimeTrackingEmployeeTimeTrackingDataV1 update_time_tracking_employee_enrollment(employee_id, time_tracking_update_employee_time_tracking_data_v1)

Update Employee Enrollment

Enables, disables, or reassigns a single employee's enrollment using JSON Merge Patch (RFC 7396) semantics: only the properties present in the body are applied and omitted properties are unchanged. Content-Type must be `application/merge-patch+json`. When the employee has no enrollment record yet and `enabled` is set to true, one is created. `timezone` and `clockInId` are read-only on this API. Reassigning an employee whose time tracking is currently off requires setting `enabled` to true in the same body, and `configurationId` and `enabledOn` cannot be combined with `enabled: false`.

OAuth Scopes: time_tracking:employees.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_employee_time_tracking_data_v1 import TimeTrackingEmployeeTimeTrackingDataV1
from bamboohr_sdk.models.time_tracking_update_employee_time_tracking_data_v1 import TimeTrackingUpdateEmployeeTimeTrackingDataV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    employee_id = 56 # int | The employee ID.
    time_tracking_update_employee_time_tracking_data_v1 = bamboohr_sdk.TimeTrackingUpdateEmployeeTimeTrackingDataV1() # TimeTrackingUpdateEmployeeTimeTrackingDataV1 | 

    try:
        # Update Employee Enrollment
        api_response = api_instance.update_time_tracking_employee_enrollment(employee_id, time_tracking_update_employee_time_tracking_data_v1)
        print("The response of TimeTrackingApi->update_time_tracking_employee_enrollment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->update_time_tracking_employee_enrollment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| The employee ID. | 
 **time_tracking_update_employee_time_tracking_data_v1** | [**TimeTrackingUpdateEmployeeTimeTrackingDataV1**](TimeTrackingUpdateEmployeeTimeTrackingDataV1.md)|  | 

### Return type

[**TimeTrackingEmployeeTimeTrackingDataV1**](TimeTrackingEmployeeTimeTrackingDataV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated employee time tracking enrollment. |  -  |
**400** | Malformed request body. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | The employee does not exist, or has no enrollment record to disable. |  -  |
**415** | Unsupported media type. Content-Type must be application/merge-patch+json. |  -  |
**422** | Validation error (e.g., an unknown configurationId, an invalid enabledOn, an attempt to write a read-only field, or an employee who cannot be enabled). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_time_tracking_kiosk**
> TimeTrackingTimeTrackingKioskV1 update_time_tracking_kiosk(id, time_tracking_update_time_tracking_kiosk_v1)

Update Time Tracking Kiosk

Updates a time tracking kiosk using JSON Merge Patch (RFC 7396) semantics. Only the kiosk `name` is mutable. Content-Type: application/merge-patch+json is preferred because it names those semantics, but application/json is also accepted.

OAuth Scopes: time_tracking:kiosks.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_time_tracking_kiosk_v1 import TimeTrackingTimeTrackingKioskV1
from bamboohr_sdk.models.time_tracking_update_time_tracking_kiosk_v1 import TimeTrackingUpdateTimeTrackingKioskV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 'id_example' # str | The time tracking kiosk ID.
    time_tracking_update_time_tracking_kiosk_v1 = bamboohr_sdk.TimeTrackingUpdateTimeTrackingKioskV1() # TimeTrackingUpdateTimeTrackingKioskV1 | 

    try:
        # Update Time Tracking Kiosk
        api_response = api_instance.update_time_tracking_kiosk(id, time_tracking_update_time_tracking_kiosk_v1)
        print("The response of TimeTrackingApi->update_time_tracking_kiosk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->update_time_tracking_kiosk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The time tracking kiosk ID. | 
 **time_tracking_update_time_tracking_kiosk_v1** | [**TimeTrackingUpdateTimeTrackingKioskV1**](TimeTrackingUpdateTimeTrackingKioskV1.md)|  | 

### Return type

[**TimeTrackingTimeTrackingKioskV1**](TimeTrackingTimeTrackingKioskV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated kiosk. |  -  |
**400** | Malformed request body. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions or read-only scope. |  -  |
**404** | Kiosk not found or soft-deleted. |  -  |
**409** | Conflict. Another active kiosk already uses the provided name. |  -  |
**422** | Validation error (e.g., the ID is not a valid UUID, or &#x60;name&#x60; is empty or longer than 255 characters). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_time_tracking_time_clock**
> TimeTrackingTimeTrackingTimeClockV1 update_time_tracking_time_clock(id, time_tracking_update_time_tracking_time_clock_v1)

Update Time Tracking Time Clock

Updates a time tracking time clock using JSON Merge Patch (RFC 7396) semantics: only the properties present in the body are applied. Only `name` and `timezone` are mutable, and at least one of them must be provided. Both changes are written through to the GT Clocks partner; writes are never served from cache, so a write returns 503 with a Retry-After header when the partner is unreachable. A successful write invalidates the cached device list so the next read reflects the change. Content-Type: application/merge-patch+json is preferred because it names those semantics, but application/json is also accepted.

OAuth Scopes: time_tracking:time_clocks.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_time_tracking_time_clock_v1 import TimeTrackingTimeTrackingTimeClockV1
from bamboohr_sdk.models.time_tracking_update_time_tracking_time_clock_v1 import TimeTrackingUpdateTimeTrackingTimeClockV1
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basic
configuration = bamboohr_sdk.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TimeTrackingApi(api_client)
    id = 'id_example' # str | The time tracking time clock ID.
    time_tracking_update_time_tracking_time_clock_v1 = bamboohr_sdk.TimeTrackingUpdateTimeTrackingTimeClockV1() # TimeTrackingUpdateTimeTrackingTimeClockV1 | 

    try:
        # Update Time Tracking Time Clock
        api_response = api_instance.update_time_tracking_time_clock(id, time_tracking_update_time_tracking_time_clock_v1)
        print("The response of TimeTrackingApi->update_time_tracking_time_clock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->update_time_tracking_time_clock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The time tracking time clock ID. | 
 **time_tracking_update_time_tracking_time_clock_v1** | [**TimeTrackingUpdateTimeTrackingTimeClockV1**](TimeTrackingUpdateTimeTrackingTimeClockV1.md)|  | 

### Return type

[**TimeTrackingTimeTrackingTimeClockV1**](TimeTrackingTimeTrackingTimeClockV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated time clock. |  -  |
**400** | Malformed request body. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | Time clock not found, or the company has no time clocks connected. |  -  |
**422** | Validation error (e.g., an invalid time clock ID, a name outside 1-255 characters, an unknown IANA timezone, or neither name nor timezone provided). |  -  |
**503** | The GT Clocks partner is temporarily unreachable and the write could not be applied. Retry after the interval given in the Retry-After header. |  * Retry-After - Seconds to wait before retrying the request. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

