# bamboohr_sdk.TimeTrackingApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_employees_to_break_policy**](TimeTrackingApi.md#assign_employees_to_break_policy) | **POST** /api/v1/time-tracking/break-policies/{id}/assign | Assign Employees to Break Policy
[**create_break**](TimeTrackingApi.md#create_break) | **POST** /api/v1/time-tracking/break-policies/{id}/breaks | Create Break
[**create_break_policy**](TimeTrackingApi.md#create_break_policy) | **POST** /api/v1/time-tracking/break-policies | Create Break Policy
[**create_or_update_timesheet_clock_entries**](TimeTrackingApi.md#create_or_update_timesheet_clock_entries) | **POST** /api/v1/time_tracking/clock_entries/store | Create or Update Timesheet Clock Entries
[**create_or_update_timesheet_hour_entries**](TimeTrackingApi.md#create_or_update_timesheet_hour_entries) | **POST** /api/v1/time_tracking/hour_entries/store | Create or Update Timesheet Hour Entries
[**create_time_tracking_project**](TimeTrackingApi.md#create_time_tracking_project) | **POST** /api/v1/time_tracking/projects | Create Time Tracking Project
[**create_timesheet_clock_in_entry**](TimeTrackingApi.md#create_timesheet_clock_in_entry) | **POST** /api/v1/time_tracking/employees/{employeeId}/clock_in | Create Timesheet Clock-In Entry
[**create_timesheet_clock_out_entry**](TimeTrackingApi.md#create_timesheet_clock_out_entry) | **POST** /api/v1/time_tracking/employees/{employeeId}/clock_out | Create Timesheet Clock-Out Entry
[**delete_break**](TimeTrackingApi.md#delete_break) | **DELETE** /api/v1/time-tracking/breaks/{id} | Delete Break
[**delete_break_policy**](TimeTrackingApi.md#delete_break_policy) | **DELETE** /api/v1/time-tracking/break-policies/{id} | Delete Break Policy
[**delete_timesheet_clock_entries_via_post**](TimeTrackingApi.md#delete_timesheet_clock_entries_via_post) | **POST** /api/v1/time_tracking/clock_entries/delete | Delete Timesheet Clock Entries
[**delete_timesheet_hour_entries_via_post**](TimeTrackingApi.md#delete_timesheet_hour_entries_via_post) | **POST** /api/v1/time_tracking/hour_entries/delete | Delete Timesheet Hour Entries
[**get_break**](TimeTrackingApi.md#get_break) | **GET** /api/v1/time-tracking/breaks/{id} | Get Break
[**get_break_policy**](TimeTrackingApi.md#get_break_policy) | **GET** /api/v1/time-tracking/break-policies/{id} | Get Break Policy
[**list_break_assessments**](TimeTrackingApi.md#list_break_assessments) | **GET** /api/v1/time-tracking/break-assessments | List Break Assessments
[**list_break_policies**](TimeTrackingApi.md#list_break_policies) | **GET** /api/v1/time-tracking/break-policies | List Break Policies
[**list_break_policy_breaks**](TimeTrackingApi.md#list_break_policy_breaks) | **GET** /api/v1/time-tracking/break-policies/{id}/breaks | List Breaks for Break Policy
[**list_break_policy_employees**](TimeTrackingApi.md#list_break_policy_employees) | **GET** /api/v1/time-tracking/break-policies/{id}/employees | List Break Policy Employees
[**list_employee_break_availabilities**](TimeTrackingApi.md#list_employee_break_availabilities) | **GET** /api/v1/time-tracking/employees/{id}/break-availabilities | List Employee Break Availabilities
[**list_employee_break_policies**](TimeTrackingApi.md#list_employee_break_policies) | **GET** /api/v1/time-tracking/employees/{id}/break-policies | List Employee Break Policies
[**list_timesheet_entries**](TimeTrackingApi.md#list_timesheet_entries) | **GET** /api/v1/time_tracking/timesheet_entries | List Timesheet Entries
[**replace_breaks_for_break_policy**](TimeTrackingApi.md#replace_breaks_for_break_policy) | **PUT** /api/v1/time-tracking/break-policies/{id}/breaks | Replace Breaks for Break Policy
[**set_break_policy_employees**](TimeTrackingApi.md#set_break_policy_employees) | **PUT** /api/v1/time-tracking/break-policies/{id}/assign | Set Employees for Break Policy
[**sync_break_policy**](TimeTrackingApi.md#sync_break_policy) | **PUT** /api/v1/time-tracking/break-policies/{id}/sync | Sync Break Policy
[**unassign_employees_from_break_policy**](TimeTrackingApi.md#unassign_employees_from_break_policy) | **POST** /api/v1/time-tracking/break-policies/{id}/unassign | Unassign Employees from Break Policy
[**update_break**](TimeTrackingApi.md#update_break) | **PATCH** /api/v1/time-tracking/breaks/{id} | Update Break
[**update_break_policy**](TimeTrackingApi.md#update_break_policy) | **PATCH** /api/v1/time-tracking/break-policies/{id} | Update Break Policy


# **assign_employees_to_break_policy**
> assign_employees_to_break_policy(id, assign_employees_to_break_policy_request)

Assign Employees to Break Policy

Assigns employees to a break policy. Adds the specified employees to the policy without removing existing assignments.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.assign_employees_to_break_policy_request import AssignEmployeesToBreakPolicyRequest
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
    id = 'id_example' # str | The break policy ID.
    assign_employees_to_break_policy_request = bamboohr_sdk.AssignEmployeesToBreakPolicyRequest() # AssignEmployeesToBreakPolicyRequest | 

    try:
        # Assign Employees to Break Policy
        api_instance.assign_employees_to_break_policy(id, assign_employees_to_break_policy_request)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->assign_employees_to_break_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 
 **assign_employees_to_break_policy_request** | [**AssignEmployeesToBreakPolicyRequest**](AssignEmployeesToBreakPolicyRequest.md)|  | 

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
**204** | Employees successfully assigned to the break policy |  -  |
**400** | Bad request - invalid data provided (for example: missing &#x60;employeeIds&#x60;, invalid IDs, or policy assignment constraints). |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Break policy not found |  -  |
**422** | Unprocessable entity - validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_break**
> TimeTrackingTimeTrackingBreakV1 create_break(id, time_tracking_create_time_tracking_break_v1)

Create Break

Creates a new break and associates it with the specified break policy.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_create_time_tracking_break_v1 import TimeTrackingCreateTimeTrackingBreakV1
from bamboohr_sdk.models.time_tracking_time_tracking_break_v1 import TimeTrackingTimeTrackingBreakV1
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
    id = 'id_example' # str | The break policy ID.
    time_tracking_create_time_tracking_break_v1 = bamboohr_sdk.TimeTrackingCreateTimeTrackingBreakV1() # TimeTrackingCreateTimeTrackingBreakV1 | 

    try:
        # Create Break
        api_response = api_instance.create_break(id, time_tracking_create_time_tracking_break_v1)
        print("The response of TimeTrackingApi->create_break:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->create_break: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 
 **time_tracking_create_time_tracking_break_v1** | [**TimeTrackingCreateTimeTrackingBreakV1**](TimeTrackingCreateTimeTrackingBreakV1.md)|  | 

### Return type

[**TimeTrackingTimeTrackingBreakV1**](TimeTrackingTimeTrackingBreakV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a break |  -  |
**422** | Invalid request data |  -  |
**403** | Forbidden - user does not have permission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_break_policy**
> TimeTrackingTimeTrackingBreakPolicyWithRelationsV1 create_break_policy(time_tracking_create_time_tracking_break_policy_v1)

Create Break Policy

Create a break policy. Breaks and assignments can be optionally included and created at the same time.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_create_time_tracking_break_policy_v1 import TimeTrackingCreateTimeTrackingBreakPolicyV1
from bamboohr_sdk.models.time_tracking_time_tracking_break_policy_with_relations_v1 import TimeTrackingTimeTrackingBreakPolicyWithRelationsV1
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
    time_tracking_create_time_tracking_break_policy_v1 = bamboohr_sdk.TimeTrackingCreateTimeTrackingBreakPolicyV1() # TimeTrackingCreateTimeTrackingBreakPolicyV1 | 

    try:
        # Create Break Policy
        api_response = api_instance.create_break_policy(time_tracking_create_time_tracking_break_policy_v1)
        print("The response of TimeTrackingApi->create_break_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->create_break_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_tracking_create_time_tracking_break_policy_v1** | [**TimeTrackingCreateTimeTrackingBreakPolicyV1**](TimeTrackingCreateTimeTrackingBreakPolicyV1.md)|  | 

### Return type

[**TimeTrackingTimeTrackingBreakPolicyWithRelationsV1**](TimeTrackingTimeTrackingBreakPolicyWithRelationsV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a break policy |  -  |
**403** | Forbidden |  -  |
**422** | Invalid request data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_timesheet_clock_entries**
> List[TimesheetEntryInfoApiTransformer] create_or_update_timesheet_clock_entries(clock_entries_schema)

Create or Update Timesheet Clock Entries

Creates or updates timesheet clock entries in bulk. Entries with an existing ID are updated; entries without an ID are created.

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

# **create_time_tracking_project**
> TimeTrackingProjectWithTasksAndEmployeeIds create_time_tracking_project(project_create_request_schema)

Create Time Tracking Project

Creates a new time tracking project. Returns the created project with its ID and tasks. When `allowAllEmployees` is false, the response also includes the `employeeIds` array of employees who have access.

By default, all employees can log time to the project (`allowAllEmployees` defaults to true) and the project is billable (`billable` defaults to true). Set `hasTasks` to true to enable task-level tracking and provide a `tasks` array — at least one task is required when `hasTasks` is true. Project and task names must be unique and may not exceed 50 characters. When `allowAllEmployees` is false, provide `employeeIds` to restrict access to specific employees.

### Example

* Basic Authentication (basic):
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
    project_create_request_schema = bamboohr_sdk.ProjectCreateRequestSchema() # ProjectCreateRequestSchema | 

    try:
        # Create Time Tracking Project
        api_response = api_instance.create_time_tracking_project(project_create_request_schema)
        print("The response of TimeTrackingApi->create_time_tracking_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->create_time_tracking_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_create_request_schema** | [**ProjectCreateRequestSchema**](ProjectCreateRequestSchema.md)|  | 

### Return type

[**TimeTrackingProjectWithTasksAndEmployeeIds**](TimeTrackingProjectWithTasksAndEmployeeIds.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Project created successfully. Returns the new project with tasks. The &#x60;employeeIds&#x60; field is included only when &#x60;allowAllEmployees&#x60; is false. |  -  |
**400** | Bad request parameters - invalid or missing required fields. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Forbidden. Insufficient user permissions or API access is not turned on. |  -  |
**406** | Request not acceptable. |  -  |
**409** | There was a conflict with the request. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_timesheet_clock_in_entry**
> TimesheetEntryInfoApiTransformer create_timesheet_clock_in_entry(employee_id, clock_in_request_schema=clock_in_request_schema)

Create Timesheet Clock-In Entry

Clocks in an employee at the current server time. To record a historical clock-in, provide a `date`, `start` (HH:MM, 24-hour format), and `timezone`. You can optionally associate the entry with `projectId`, `taskId` (requires `projectId`), `breakId`, and a `note`.

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
    employee_id = 56 # int | ID of the employee to clock in.
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
 **employee_id** | **int**| ID of the employee to clock in. | 
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
    employee_id = 56 # int | ID of the employee to clock out.
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
 **employee_id** | **int**| ID of the employee to clock out. | 
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

# **delete_break**
> delete_break(id)

Delete Break

Deletes a time tracking break by its UUID. The break is soft-deleted and removed from any break policies it was associated with.

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
    id = 'id_example' # str | The break ID.

    try:
        # Delete Break
        api_instance.delete_break(id)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->delete_break: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break ID. | 

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
**204** | Break deleted successfully |  -  |
**400** | Invalid ID format |  -  |
**403** | Forbidden |  -  |
**404** | Break not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_break_policy**
> delete_break_policy(id)

Delete Break Policy

Deletes a break policy by its UUID. Associated breaks and employee assignments are also removed.

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
    id = 'id_example' # str | The break policy ID.

    try:
        # Delete Break Policy
        api_instance.delete_break_policy(id)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->delete_break_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 

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
**204** | Break policy deleted successfully |  -  |
**400** | Invalid uuid format |  -  |
**403** | Forbidden |  -  |
**404** | Break policy not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_timesheet_clock_entries_via_post**
> delete_timesheet_clock_entries_via_post(clock_entry_ids_schema)

Delete Timesheet Clock Entries

Deletes one or more timesheet clock entries by their IDs. Delete operations are idempotent; deleting already-removed entries does not require client retries.

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

# **get_break**
> TimeTrackingTimeTrackingBreakV1 get_break(id)

Get Break

Retrieves a single time tracking break by its UUID. Returns the full break details including name, duration, paid status, and availability configuration.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_time_tracking_break_v1 import TimeTrackingTimeTrackingBreakV1
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
    id = 'id_example' # str | The break ID.

    try:
        # Get Break
        api_response = api_instance.get_break(id)
        print("The response of TimeTrackingApi->get_break:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->get_break: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break ID. | 

### Return type

[**TimeTrackingTimeTrackingBreakV1**](TimeTrackingTimeTrackingBreakV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the break. |  -  |
**403** | Forbidden |  -  |
**404** | Break not found. |  -  |
**422** | The provided &#x60;id&#x60; is not a valid UUID. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_break_policy**
> TimeTrackingTimeTrackingBreakPolicyV1 get_break_policy(id, include_counts=include_counts)

Get Break Policy

Retrieves a single break policy by its UUID. When includeCounts is enabled, the response includes the number of associated employees and breaks.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_time_tracking_break_policy_v1 import TimeTrackingTimeTrackingBreakPolicyV1
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
    id = 'id_example' # str | The break policy ID.
    include_counts = False # bool | Include employee and break counts (optional) (default to False)

    try:
        # Get Break Policy
        api_response = api_instance.get_break_policy(id, include_counts=include_counts)
        print("The response of TimeTrackingApi->get_break_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->get_break_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 
 **include_counts** | **bool**| Include employee and break counts | [optional] [default to False]

### Return type

[**TimeTrackingTimeTrackingBreakPolicyV1**](TimeTrackingTimeTrackingBreakPolicyV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Break policy retrieved successfully |  -  |
**403** | Forbidden |  -  |
**404** | Break policy not found |  -  |
**422** | Invalid input |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_break_assessments**
> TimeTrackingPaginatedBreakAssessmentsResponseV1 list_break_assessments(offset=offset, limit=limit, filter=filter)

List Break Assessments

Returns a paginated list of break assessments. A break assessment records whether an employee complied with their assigned break policy for a given day, along with any violations. Use the `filter` parameter to scope results by employee, date, result, or other fields. Use `offset` and `limit` for pagination; `limit` defaults to 100 and may not exceed 500.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_paginated_break_assessments_response_v1 import TimeTrackingPaginatedBreakAssessmentsResponseV1
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
    offset = 0 # int | Number of items to skip before returning results. Defaults to 0. (optional) (default to 0)
    limit = 100 # int | Maximum number of items to return. Defaults to 100. Maximum is 500. (optional) (default to 100)
    filter = '' # str | OData v4 filter expression. Filterable fields: `id`, `breakId`, `employeeId`, `employeeTimesheetId`, `date`, `result`, `availableYmdt`, `unavailableYmdt`, `createdAt`, `updatedAt`, `expectedDuration`, `recordedDuration`, `durationDifference`. (optional) (default to '')

    try:
        # List Break Assessments
        api_response = api_instance.list_break_assessments(offset=offset, limit=limit, filter=filter)
        print("The response of TimeTrackingApi->list_break_assessments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->list_break_assessments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Number of items to skip before returning results. Defaults to 0. | [optional] [default to 0]
 **limit** | **int**| Maximum number of items to return. Defaults to 100. Maximum is 500. | [optional] [default to 100]
 **filter** | **str**| OData v4 filter expression. Filterable fields: &#x60;id&#x60;, &#x60;breakId&#x60;, &#x60;employeeId&#x60;, &#x60;employeeTimesheetId&#x60;, &#x60;date&#x60;, &#x60;result&#x60;, &#x60;availableYmdt&#x60;, &#x60;unavailableYmdt&#x60;, &#x60;createdAt&#x60;, &#x60;updatedAt&#x60;, &#x60;expectedDuration&#x60;, &#x60;recordedDuration&#x60;, &#x60;durationDifference&#x60;. | [optional] [default to &#39;&#39;]

### Return type

[**TimeTrackingPaginatedBreakAssessmentsResponseV1**](TimeTrackingPaginatedBreakAssessmentsResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of paginated break assessments |  -  |
**403** | Forbidden |  -  |
**422** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_break_policies**
> TimeTrackingPaginatedBreakPoliciesResponseV1 list_break_policies(offset=offset, limit=limit, filter=filter, include_counts=include_counts)

List Break Policies

Returns a paginated list of all break policies. Supports OData v4 filtering. Use includeCounts to include employee and break counts per policy.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_paginated_break_policies_response_v1 import TimeTrackingPaginatedBreakPoliciesResponseV1
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
    offset = 0 # int | The offset of items to retrieve (optional) (default to 0)
    limit = 100 # int | The maximum items to retrieve (optional) (default to 100)
    filter = '' # str | Filter by an OData (Open Data Protocol) v4 specification (optional) (default to '')
    include_counts = False # bool | Include employee and break counts (optional) (default to False)

    try:
        # List Break Policies
        api_response = api_instance.list_break_policies(offset=offset, limit=limit, filter=filter, include_counts=include_counts)
        print("The response of TimeTrackingApi->list_break_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->list_break_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The offset of items to retrieve | [optional] [default to 0]
 **limit** | **int**| The maximum items to retrieve | [optional] [default to 100]
 **filter** | **str**| Filter by an OData (Open Data Protocol) v4 specification | [optional] [default to &#39;&#39;]
 **include_counts** | **bool**| Include employee and break counts | [optional] [default to False]

### Return type

[**TimeTrackingPaginatedBreakPoliciesResponseV1**](TimeTrackingPaginatedBreakPoliciesResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved break policies |  -  |
**403** | Forbidden |  -  |
**422** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_break_policy_breaks**
> TimeTrackingPaginatedBreaksResponseV1 list_break_policy_breaks(id, offset=offset, limit=limit, filter=filter)

List Breaks for Break Policy

Returns a paginated list of breaks belonging to the specified break policy. Supports OData v4 filtering.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_paginated_breaks_response_v1 import TimeTrackingPaginatedBreaksResponseV1
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
    id = 'id_example' # str | The break policy ID.
    offset = 0 # int | The offset of items to retrieve (optional) (default to 0)
    limit = 100 # int | The maximum items to retrieve (optional) (default to 100)
    filter = '' # str | Filter by an OData (Open Data Protocol) v4 specification (optional) (default to '')

    try:
        # List Breaks for Break Policy
        api_response = api_instance.list_break_policy_breaks(id, offset=offset, limit=limit, filter=filter)
        print("The response of TimeTrackingApi->list_break_policy_breaks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->list_break_policy_breaks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 
 **offset** | **int**| The offset of items to retrieve | [optional] [default to 0]
 **limit** | **int**| The maximum items to retrieve | [optional] [default to 100]
 **filter** | **str**| Filter by an OData (Open Data Protocol) v4 specification | [optional] [default to &#39;&#39;]

### Return type

[**TimeTrackingPaginatedBreaksResponseV1**](TimeTrackingPaginatedBreaksResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved breaks for the specified break policy |  -  |
**403** | Forbidden |  -  |
**422** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_break_policy_employees**
> TimeTrackingPaginatedBreakPolicyEmployeesResponseV1 list_break_policy_employees(id, offset=offset, limit=limit)

List Break Policy Employees

Retrieves employees assigned to a specific break policy. If a policy has no assignments, returns HTTP 200 with an empty `data` array.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_paginated_break_policy_employees_response_v1 import TimeTrackingPaginatedBreakPolicyEmployeesResponseV1
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
    id = 'id_example' # str | The break policy ID.
    offset = 0 # int | The offset of items to retrieve (optional) (default to 0)
    limit = 100 # int | The maximum items to retrieve (optional) (default to 100)

    try:
        # List Break Policy Employees
        api_response = api_instance.list_break_policy_employees(id, offset=offset, limit=limit)
        print("The response of TimeTrackingApi->list_break_policy_employees:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->list_break_policy_employees: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 
 **offset** | **int**| The offset of items to retrieve | [optional] [default to 0]
 **limit** | **int**| The maximum items to retrieve | [optional] [default to 100]

### Return type

[**TimeTrackingPaginatedBreakPolicyEmployeesResponseV1**](TimeTrackingPaginatedBreakPolicyEmployeesResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of employees assigned to a break policy |  -  |
**403** | Forbidden |  -  |
**422** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_employee_break_availabilities**
> List[TimeTrackingTimeTrackingBreakAvailabilityV1] list_employee_break_availabilities(id, effective=effective)

List Employee Break Availabilities

Retrieves break availability information for an employee. Requires permission to view the target employee in addition to time-tracking-break access.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_time_tracking_break_availability_v1 import TimeTrackingTimeTrackingBreakAvailabilityV1
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
    id = 56 # int | The employee ID.
    effective = '2025-12-15T14:30:00' # str | The employee's local time that should be used to calculate availability. Defaults to the current time. Must be in Y-m-d\\TH:i:s format (no timezone offset). (optional)

    try:
        # List Employee Break Availabilities
        api_response = api_instance.list_employee_break_availabilities(id, effective=effective)
        print("The response of TimeTrackingApi->list_employee_break_availabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->list_employee_break_availabilities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The employee ID. | 
 **effective** | **str**| The employee&#39;s local time that should be used to calculate availability. Defaults to the current time. Must be in Y-m-d\\TH:i:s format (no timezone offset). | [optional] 

### Return type

[**List[TimeTrackingTimeTrackingBreakAvailabilityV1]**](TimeTrackingTimeTrackingBreakAvailabilityV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved break availabilities for the specified employee |  -  |
**403** | Forbidden - insufficient permissions to view this employee or break settings. |  -  |
**422** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_employee_break_policies**
> TimeTrackingPaginatedBreakPoliciesResponseV1 list_employee_break_policies(id, offset=offset, limit=limit)

List Employee Break Policies

Retrieves break policies assigned to a specific employee. Requires permission to view the target employee.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_paginated_break_policies_response_v1 import TimeTrackingPaginatedBreakPoliciesResponseV1
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
    id = 56 # int | The employee ID.
    offset = 0 # int | The number of items to skip before starting to collect the result set. Minimum 0. Defaults to 0. (optional) (default to 0)
    limit = 100 # int | The maximum number of items to return. Must be between 0 and 500. Defaults to 100. (optional) (default to 100)

    try:
        # List Employee Break Policies
        api_response = api_instance.list_employee_break_policies(id, offset=offset, limit=limit)
        print("The response of TimeTrackingApi->list_employee_break_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->list_employee_break_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The employee ID. | 
 **offset** | **int**| The number of items to skip before starting to collect the result set. Minimum 0. Defaults to 0. | [optional] [default to 0]
 **limit** | **int**| The maximum number of items to return. Must be between 0 and 500. Defaults to 100. | [optional] [default to 100]

### Return type

[**TimeTrackingPaginatedBreakPoliciesResponseV1**](TimeTrackingPaginatedBreakPoliciesResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of break policies |  -  |
**403** | Forbidden |  -  |
**422** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_timesheet_entries**
> List[EmployeeTimesheetEntryTransformer] list_timesheet_entries(start, end, employee_ids=employee_ids)

List Timesheet Entries

Returns timesheet entries for all employees, or a filtered subset, within the specified date range. Results include both clock and hour entry types. Dates must fall within the last 365 days and are interpreted in the company timezone.

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
    employee_ids = '1,2,3' # str | A comma separated list of employee IDs. When specified, only entries that match these employee IDs are returned. When omitted, entries for all accessible employees are returned. (optional)

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
 **employee_ids** | **str**| A comma separated list of employee IDs. When specified, only entries that match these employee IDs are returned. When omitted, entries for all accessible employees are returned. | [optional] 

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

# **replace_breaks_for_break_policy**
> List[TimeTrackingTimeTrackingBreakV1] replace_breaks_for_break_policy(id, time_tracking_create_or_update_time_tracking_break_without_policy_v1)

Replace Breaks for Break Policy

Replace all breaks for a break policy. Breaks with an ID will be updated, breaks without an ID will be created. Existing breaks not in the request will be soft-deleted.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_create_or_update_time_tracking_break_without_policy_v1 import TimeTrackingCreateOrUpdateTimeTrackingBreakWithoutPolicyV1
from bamboohr_sdk.models.time_tracking_time_tracking_break_v1 import TimeTrackingTimeTrackingBreakV1
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
    id = 'id_example' # str | The break policy ID.
    time_tracking_create_or_update_time_tracking_break_without_policy_v1 = [bamboohr_sdk.TimeTrackingCreateOrUpdateTimeTrackingBreakWithoutPolicyV1()] # List[TimeTrackingCreateOrUpdateTimeTrackingBreakWithoutPolicyV1] | 

    try:
        # Replace Breaks for Break Policy
        api_response = api_instance.replace_breaks_for_break_policy(id, time_tracking_create_or_update_time_tracking_break_without_policy_v1)
        print("The response of TimeTrackingApi->replace_breaks_for_break_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->replace_breaks_for_break_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 
 **time_tracking_create_or_update_time_tracking_break_without_policy_v1** | [**List[TimeTrackingCreateOrUpdateTimeTrackingBreakWithoutPolicyV1]**](TimeTrackingCreateOrUpdateTimeTrackingBreakWithoutPolicyV1.md)|  | 

### Return type

[**List[TimeTrackingTimeTrackingBreakV1]**](TimeTrackingTimeTrackingBreakV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully replaced breaks for the policy |  -  |
**400** | Bad request - validation errors |  -  |
**403** | Insufficient permissions |  -  |
**404** | Break policy not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_break_policy_employees**
> set_break_policy_employees(id, set_break_policy_employees_request)

Set Employees for Break Policy

Sets the employee assignments for a break policy. This replaces all existing assignments with the provided list.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.set_break_policy_employees_request import SetBreakPolicyEmployeesRequest
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
    id = 'id_example' # str | The break policy ID.
    set_break_policy_employees_request = bamboohr_sdk.SetBreakPolicyEmployeesRequest() # SetBreakPolicyEmployeesRequest | 

    try:
        # Set Employees for Break Policy
        api_instance.set_break_policy_employees(id, set_break_policy_employees_request)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->set_break_policy_employees: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 
 **set_break_policy_employees_request** | [**SetBreakPolicyEmployeesRequest**](SetBreakPolicyEmployeesRequest.md)|  | 

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
**204** | Employees assigned successfully |  -  |
**400** | Invalid data provided. |  -  |
**403** | Forbidden |  -  |
**404** | Break policy not found |  -  |
**422** | Unprocessable entity. The provided &#x60;id&#x60; is not a valid UUID, or &#x60;employeeIds&#x60; is not an array of positive integers. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_break_policy**
> TimeTrackingTimeTrackingBreakPolicyWithRelationsV1 sync_break_policy(id, time_tracking_sync_time_tracking_break_policy_v1)

Sync Break Policy

Performs a full replacement of a break policy and its related data (breaks and employee assignments). Unlike the partial update endpoint, this replaces the entire policy state with the provided payload, removing any breaks or assignments not included in the request.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_sync_time_tracking_break_policy_v1 import TimeTrackingSyncTimeTrackingBreakPolicyV1
from bamboohr_sdk.models.time_tracking_time_tracking_break_policy_with_relations_v1 import TimeTrackingTimeTrackingBreakPolicyWithRelationsV1
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
    id = 'id_example' # str | The break policy ID.
    time_tracking_sync_time_tracking_break_policy_v1 = bamboohr_sdk.TimeTrackingSyncTimeTrackingBreakPolicyV1() # TimeTrackingSyncTimeTrackingBreakPolicyV1 | 

    try:
        # Sync Break Policy
        api_response = api_instance.sync_break_policy(id, time_tracking_sync_time_tracking_break_policy_v1)
        print("The response of TimeTrackingApi->sync_break_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->sync_break_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 
 **time_tracking_sync_time_tracking_break_policy_v1** | [**TimeTrackingSyncTimeTrackingBreakPolicyV1**](TimeTrackingSyncTimeTrackingBreakPolicyV1.md)|  | 

### Return type

[**TimeTrackingTimeTrackingBreakPolicyWithRelationsV1**](TimeTrackingTimeTrackingBreakPolicyWithRelationsV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Break policy synced successfully |  -  |
**403** | Forbidden |  -  |
**404** | Break policy not found |  -  |
**422** | Invalid data provided |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_employees_from_break_policy**
> unassign_employees_from_break_policy(id, unassign_employees_from_break_policy_request)

Unassign Employees from Break Policy

Unassigns the specified employees from a break policy. Removes employee assignments from the policy without affecting the policy itself or other assigned employees. Employees can only be unassigned from policies that are not assigned to all employees.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.unassign_employees_from_break_policy_request import UnassignEmployeesFromBreakPolicyRequest
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
    id = 'id_example' # str | The break policy ID.
    unassign_employees_from_break_policy_request = bamboohr_sdk.UnassignEmployeesFromBreakPolicyRequest() # UnassignEmployeesFromBreakPolicyRequest | 

    try:
        # Unassign Employees from Break Policy
        api_instance.unassign_employees_from_break_policy(id, unassign_employees_from_break_policy_request)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->unassign_employees_from_break_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 
 **unassign_employees_from_break_policy_request** | [**UnassignEmployeesFromBreakPolicyRequest**](UnassignEmployeesFromBreakPolicyRequest.md)|  | 

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
**204** | Employees successfully unassigned from break policy |  -  |
**400** | Bad request - Invalid data or policy is assigned to all employees |  -  |
**403** | Forbidden |  -  |
**404** | Break policy not found |  -  |
**422** | Unprocessable entity - validation failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_break**
> TimeTrackingTimeTrackingBreakV1 update_break(id, time_tracking_update_time_tracking_break_v1)

Update Break

Partially updates a time tracking break identified by its UUID. Only fields provided in the request body are updated. Returns the updated break on success.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_time_tracking_break_v1 import TimeTrackingTimeTrackingBreakV1
from bamboohr_sdk.models.time_tracking_update_time_tracking_break_v1 import TimeTrackingUpdateTimeTrackingBreakV1
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
    id = 'id_example' # str | The break ID.
    time_tracking_update_time_tracking_break_v1 = bamboohr_sdk.TimeTrackingUpdateTimeTrackingBreakV1() # TimeTrackingUpdateTimeTrackingBreakV1 | 

    try:
        # Update Break
        api_response = api_instance.update_break(id, time_tracking_update_time_tracking_break_v1)
        print("The response of TimeTrackingApi->update_break:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->update_break: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break ID. | 
 **time_tracking_update_time_tracking_break_v1** | [**TimeTrackingUpdateTimeTrackingBreakV1**](TimeTrackingUpdateTimeTrackingBreakV1.md)|  | 

### Return type

[**TimeTrackingTimeTrackingBreakV1**](TimeTrackingTimeTrackingBreakV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated break |  -  |
**403** | Forbidden |  -  |
**422** | Invalid request data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_break_policy**
> TimeTrackingTimeTrackingBreakPolicyV1 update_break_policy(id, time_tracking_update_time_tracking_break_policy_v1)

Update Break Policy

Partially updates a break policy identified by its UUID. Only fields provided in the request body are updated. Returns the updated break policy on success.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_time_tracking_break_policy_v1 import TimeTrackingTimeTrackingBreakPolicyV1
from bamboohr_sdk.models.time_tracking_update_time_tracking_break_policy_v1 import TimeTrackingUpdateTimeTrackingBreakPolicyV1
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
    id = 'id_example' # str | The break policy ID.
    time_tracking_update_time_tracking_break_policy_v1 = bamboohr_sdk.TimeTrackingUpdateTimeTrackingBreakPolicyV1() # TimeTrackingUpdateTimeTrackingBreakPolicyV1 | 

    try:
        # Update Break Policy
        api_response = api_instance.update_break_policy(id, time_tracking_update_time_tracking_break_policy_v1)
        print("The response of TimeTrackingApi->update_break_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->update_break_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 
 **time_tracking_update_time_tracking_break_policy_v1** | [**TimeTrackingUpdateTimeTrackingBreakPolicyV1**](TimeTrackingUpdateTimeTrackingBreakPolicyV1.md)|  | 

### Return type

[**TimeTrackingTimeTrackingBreakPolicyV1**](TimeTrackingTimeTrackingBreakPolicyV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Break policy updated successfully |  -  |
**403** | Forbidden |  -  |
**404** | Break policy not found |  -  |
**422** | Invalid uuid format |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

