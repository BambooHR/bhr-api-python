# bamboohr_sdk.TimeTrackingApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_edit_timesheet_clock_entries**](TimeTrackingApi.md#add_edit_timesheet_clock_entries) | **POST** /api/v1/time_tracking/clock_entries/store | Create or Update Timesheet Clock Entries
[**add_edit_timesheet_hour_entries**](TimeTrackingApi.md#add_edit_timesheet_hour_entries) | **POST** /api/v1/time_tracking/hour_entries/store | Create or Update Timesheet Hour Entries
[**add_timesheet_clock_in_entry**](TimeTrackingApi.md#add_timesheet_clock_in_entry) | **POST** /api/v1/time_tracking/employees/{employeeId}/clock_in | Create Timesheet Clock-In Entry
[**add_timesheet_clock_out_entry**](TimeTrackingApi.md#add_timesheet_clock_out_entry) | **POST** /api/v1/time_tracking/employees/{employeeId}/clock_out | Create Timesheet Clock-Out Entry
[**create_time_tracking_project**](TimeTrackingApi.md#create_time_tracking_project) | **POST** /api/v1/time_tracking/projects | Create Time Tracking Project
[**delete_timesheet_clock_entries_via_post**](TimeTrackingApi.md#delete_timesheet_clock_entries_via_post) | **POST** /api/v1/time_tracking/clock_entries/delete | Delete Timesheet Clock Entries
[**delete_timesheet_hour_entries_via_post**](TimeTrackingApi.md#delete_timesheet_hour_entries_via_post) | **POST** /api/v1/time_tracking/hour_entries/delete | Delete Timesheet Hour Entries
[**get_timesheet_entries**](TimeTrackingApi.md#get_timesheet_entries) | **GET** /api/v1/time_tracking/timesheet_entries | Get Timesheet Entries
[**time_tracking_assign_employees_to_break_policy**](TimeTrackingApi.md#time_tracking_assign_employees_to_break_policy) | **POST** /api/v1/time-tracking/break-policies/{id}/assign | Assign Employees to Break Policy
[**time_tracking_create_break**](TimeTrackingApi.md#time_tracking_create_break) | **POST** /api/v1/time-tracking/break-policies/{id}/breaks | Create Break
[**time_tracking_create_break_policy**](TimeTrackingApi.md#time_tracking_create_break_policy) | **POST** /api/v1/time-tracking/break-policies | Create Break Policy
[**time_tracking_delete_break**](TimeTrackingApi.md#time_tracking_delete_break) | **DELETE** /api/v1/time-tracking/breaks/{id} | Delete Break
[**time_tracking_delete_break_policy**](TimeTrackingApi.md#time_tracking_delete_break_policy) | **DELETE** /api/v1/time-tracking/break-policies/{id} | Delete Break Policy
[**time_tracking_get_break**](TimeTrackingApi.md#time_tracking_get_break) | **GET** /api/v1/time-tracking/breaks/{id} | Get Break
[**time_tracking_get_break_policy**](TimeTrackingApi.md#time_tracking_get_break_policy) | **GET** /api/v1/time-tracking/break-policies/{id} | Get Break Policy
[**time_tracking_list_break_assessments**](TimeTrackingApi.md#time_tracking_list_break_assessments) | **GET** /api/v1/time-tracking/break-assessments | List Break Assessments
[**time_tracking_list_break_policies**](TimeTrackingApi.md#time_tracking_list_break_policies) | **GET** /api/v1/time-tracking/break-policies | List Break Policies
[**time_tracking_list_break_policy_breaks**](TimeTrackingApi.md#time_tracking_list_break_policy_breaks) | **GET** /api/v1/time-tracking/break-policies/{id}/breaks | List Breaks for Break Policy
[**time_tracking_list_break_policy_employees**](TimeTrackingApi.md#time_tracking_list_break_policy_employees) | **GET** /api/v1/time-tracking/break-policies/{id}/employees | List Break Policy Employees
[**time_tracking_list_employee_break_availabilities**](TimeTrackingApi.md#time_tracking_list_employee_break_availabilities) | **GET** /api/v1/time-tracking/employees/{id}/break-availabilities | List Employee Break Availability
[**time_tracking_list_employee_break_policies**](TimeTrackingApi.md#time_tracking_list_employee_break_policies) | **GET** /api/v1/time-tracking/employees/{id}/break-policies | List Employee Break Policies
[**time_tracking_replace_breaks_for_break_policy**](TimeTrackingApi.md#time_tracking_replace_breaks_for_break_policy) | **PUT** /api/v1/time-tracking/break-policies/{id}/breaks | Replace Breaks for Break Policy
[**time_tracking_set_break_policy_employees**](TimeTrackingApi.md#time_tracking_set_break_policy_employees) | **PUT** /api/v1/time-tracking/break-policies/{id}/assign | Set Employees for Break Policy
[**time_tracking_sync_break_policy**](TimeTrackingApi.md#time_tracking_sync_break_policy) | **PUT** /api/v1/time-tracking/break-policies/{id}/sync | Sync Break Policy
[**time_tracking_unassign_employees_from_break_policy**](TimeTrackingApi.md#time_tracking_unassign_employees_from_break_policy) | **POST** /api/v1/time-tracking/break-policies/{id}/unassign | Unassign Employees from Break Policy
[**time_tracking_update_break**](TimeTrackingApi.md#time_tracking_update_break) | **PATCH** /api/v1/time-tracking/breaks/{id} | Update Break
[**time_tracking_update_break_policy**](TimeTrackingApi.md#time_tracking_update_break_policy) | **PATCH** /api/v1/time-tracking/break-policies/{id} | Update Break Policy


# **add_edit_timesheet_clock_entries**
> List[TimesheetEntryInfoApiTransformer] add_edit_timesheet_clock_entries(clock_entries_schema=clock_entries_schema)

Create or Update Timesheet Clock Entries

Add or edit timesheet clock entries.

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
    clock_entries_schema = bamboohr_sdk.ClockEntriesSchema() # ClockEntriesSchema |  (optional)

    try:
        # Create or Update Timesheet Clock Entries
        api_response = api_instance.add_edit_timesheet_clock_entries(clock_entries_schema=clock_entries_schema)
        print("The response of TimeTrackingApi->add_edit_timesheet_clock_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->add_edit_timesheet_clock_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clock_entries_schema** | [**ClockEntriesSchema**](ClockEntriesSchema.md)|  | [optional] 

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
**201** | Success. |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Forbidden. Insufficient user permissions or API access is not turned on. |  -  |
**406** | Request not acceptable. |  -  |
**409** | There was a conflict with the request. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_edit_timesheet_hour_entries**
> List[TimesheetEntryInfoApiTransformer] add_edit_timesheet_hour_entries(hour_entries_request_schema=hour_entries_request_schema)

Create or Update Timesheet Hour Entries

Add or edit timesheet hour entries.

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
    hour_entries_request_schema = bamboohr_sdk.HourEntriesRequestSchema() # HourEntriesRequestSchema |  (optional)

    try:
        # Create or Update Timesheet Hour Entries
        api_response = api_instance.add_edit_timesheet_hour_entries(hour_entries_request_schema=hour_entries_request_schema)
        print("The response of TimeTrackingApi->add_edit_timesheet_hour_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->add_edit_timesheet_hour_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hour_entries_request_schema** | [**HourEntriesRequestSchema**](HourEntriesRequestSchema.md)|  | [optional] 

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
**201** | Success. |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Forbidden. Insufficient user permissions or API access is not turned on. |  -  |
**406** | Request not acceptable. |  -  |
**409** | There was a conflict with the request. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_timesheet_clock_in_entry**
> TimesheetEntryInfoApiTransformer add_timesheet_clock_in_entry(employee_id, clock_in_request_schema=clock_in_request_schema)

Create Timesheet Clock-In Entry

Clock in an employee.

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
        api_response = api_instance.add_timesheet_clock_in_entry(employee_id, clock_in_request_schema=clock_in_request_schema)
        print("The response of TimeTrackingApi->add_timesheet_clock_in_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->add_timesheet_clock_in_entry: %s\n" % e)
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
**200** | Success. |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Forbidden. Insufficient user permissions or API access is not turned on. |  -  |
**406** | Request not acceptable. |  -  |
**409** | There was a conflict with the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_timesheet_clock_out_entry**
> TimesheetEntryInfoApiTransformer add_timesheet_clock_out_entry(employee_id, clock_out_request_schema=clock_out_request_schema)

Create Timesheet Clock-Out Entry

Clock out an employee.

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
        api_response = api_instance.add_timesheet_clock_out_entry(employee_id, clock_out_request_schema=clock_out_request_schema)
        print("The response of TimeTrackingApi->add_timesheet_clock_out_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->add_timesheet_clock_out_entry: %s\n" % e)
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
**200** | Success. |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Forbidden. Insufficient user permissions or API access is not turned on. |  -  |
**406** | Request not acceptable. |  -  |
**409** | There was a conflict with the request. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_time_tracking_project**
> TimeTrackingProjectWithTasksAndEmployeeIds create_time_tracking_project(project_create_request_schema=project_create_request_schema)

Create Time Tracking Project

Create a time tracking project with optional tasks.

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
    project_create_request_schema = bamboohr_sdk.ProjectCreateRequestSchema() # ProjectCreateRequestSchema |  (optional)

    try:
        # Create Time Tracking Project
        api_response = api_instance.create_time_tracking_project(project_create_request_schema=project_create_request_schema)
        print("The response of TimeTrackingApi->create_time_tracking_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->create_time_tracking_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_create_request_schema** | [**ProjectCreateRequestSchema**](ProjectCreateRequestSchema.md)|  | [optional] 

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
**201** | Success. |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Forbidden. Insufficient user permissions or API access is not turned on. |  -  |
**406** | Request not acceptable. |  -  |
**409** | There was a conflict with the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_timesheet_clock_entries_via_post**
> delete_timesheet_clock_entries_via_post(clock_entry_ids_schema)

Delete Timesheet Clock Entries

Delete timesheet clock entries.

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
**204** | Successful deletion will return a 204, no content. |  -  |
**400** | Invalid information passed in. |  -  |
**403** | Missing permissions or timesheet already approved. |  -  |
**404** | Id not found. |  -  |
**409** | If clock timesheet, may still be clocked in. Have to clock out first. |  -  |
**412** | Invalid company configuration or timezone. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_timesheet_hour_entries_via_post**
> delete_timesheet_hour_entries_via_post(hour_entry_ids_schema=hour_entry_ids_schema)

Delete Timesheet Hour Entries

Delete timesheet hour entries.

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
    hour_entry_ids_schema = bamboohr_sdk.HourEntryIdsSchema() # HourEntryIdsSchema |  (optional)

    try:
        # Delete Timesheet Hour Entries
        api_instance.delete_timesheet_hour_entries_via_post(hour_entry_ids_schema=hour_entry_ids_schema)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->delete_timesheet_hour_entries_via_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hour_entry_ids_schema** | [**HourEntryIdsSchema**](HourEntryIdsSchema.md)|  | [optional] 

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
**204** | Success. No content returned. |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Forbidden. Insufficient user permissions or API access is not turned on. |  -  |
**406** | Request not acceptable. |  -  |
**409** | There was a conflict with the request. |  -  |
**412** | Invalid time tracking configuration or timezone. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timesheet_entries**
> List[EmployeeTimesheetEntryTransformer] get_timesheet_entries(start, end, employee_ids=employee_ids)

Get Timesheet Entries

Get all timesheet entries for a given period of time.

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
    employee_ids = '1,2,3' # str | A comma separated list of employee IDs. When specified, only entries that match these employee IDs are returned. (optional)

    try:
        # Get Timesheet Entries
        api_response = api_instance.get_timesheet_entries(start, end, employee_ids=employee_ids)
        print("The response of TimeTrackingApi->get_timesheet_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->get_timesheet_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| YYYY-MM-DD. Only show timesheet entries on/after the specified start date. Must be within the last 365 days. | 
 **end** | **date**| YYYY-MM-DD. Only show timesheet entries on/before the specified end date. Must be within the last 365 days. | 
 **employee_ids** | **str**| A comma separated list of employee IDs. When specified, only entries that match these employee IDs are returned. | [optional] 

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
**200** | Success. |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_tracking_assign_employees_to_break_policy**
> time_tracking_assign_employees_to_break_policy(id, time_tracking_assign_employees_to_break_policy_request)

Assign Employees to Break Policy

Assigns employees to a break policy. Adds the specified employees to the policy without removing existing assignments.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_assign_employees_to_break_policy_request import TimeTrackingAssignEmployeesToBreakPolicyRequest
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
    time_tracking_assign_employees_to_break_policy_request = bamboohr_sdk.TimeTrackingAssignEmployeesToBreakPolicyRequest() # TimeTrackingAssignEmployeesToBreakPolicyRequest | 

    try:
        # Assign Employees to Break Policy
        api_instance.time_tracking_assign_employees_to_break_policy(id, time_tracking_assign_employees_to_break_policy_request)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->time_tracking_assign_employees_to_break_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 
 **time_tracking_assign_employees_to_break_policy_request** | [**TimeTrackingAssignEmployeesToBreakPolicyRequest**](TimeTrackingAssignEmployeesToBreakPolicyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Employees successfully assigned to the break policy |  -  |
**400** | Bad request - invalid data provided |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Break policy not found |  -  |
**422** | Unprocessable entity - validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_tracking_create_break**
> TimeTrackingTimeTrackingBreakV1 time_tracking_create_break(id, time_tracking_create_time_tracking_break_v1)

Create Break

Create a break for the provided break policy.

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
        api_response = api_instance.time_tracking_create_break(id, time_tracking_create_time_tracking_break_v1)
        print("The response of TimeTrackingApi->time_tracking_create_break:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->time_tracking_create_break: %s\n" % e)
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

# **time_tracking_create_break_policy**
> TimeTrackingTimeTrackingBreakPolicyWithRelationsV1 time_tracking_create_break_policy(time_tracking_create_time_tracking_break_policy_v1)

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
        api_response = api_instance.time_tracking_create_break_policy(time_tracking_create_time_tracking_break_policy_v1)
        print("The response of TimeTrackingApi->time_tracking_create_break_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->time_tracking_create_break_policy: %s\n" % e)
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

# **time_tracking_delete_break**
> time_tracking_delete_break(id)

Delete Break

Delete a break by ID.

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
        api_instance.time_tracking_delete_break(id)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->time_tracking_delete_break: %s\n" % e)
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

# **time_tracking_delete_break_policy**
> time_tracking_delete_break_policy(id)

Delete Break Policy

Delete a break policy by ID.

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
        api_instance.time_tracking_delete_break_policy(id)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->time_tracking_delete_break_policy: %s\n" % e)
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

# **time_tracking_get_break**
> TimeTrackingTimeTrackingBreakV1 time_tracking_get_break(id)

Get Break

Get a break by ID.

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
        api_response = api_instance.time_tracking_get_break(id)
        print("The response of TimeTrackingApi->time_tracking_get_break:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->time_tracking_get_break: %s\n" % e)
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
**200** | Successful |  -  |
**403** | Forbidden |  -  |
**404** | Break not found. |  -  |
**422** | Invalid uuid format |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_tracking_get_break_policy**
> TimeTrackingTimeTrackingBreakPolicyV1 time_tracking_get_break_policy(id, include_counts=include_counts)

Get Break Policy

Get a break policy by ID.

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
        api_response = api_instance.time_tracking_get_break_policy(id, include_counts=include_counts)
        print("The response of TimeTrackingApi->time_tracking_get_break_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->time_tracking_get_break_policy: %s\n" % e)
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

# **time_tracking_list_break_assessments**
> TimeTrackingPaginatedBreakAssessmentsResponseV1 time_tracking_list_break_assessments(offset=offset, limit=limit, filter=filter)

List Break Assessments

Retrieves a list of time tracking break assessments, with optional filtering and pagination.

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
    offset = 0 # int | The offset of items to retrieve (optional) (default to 0)
    limit = 100 # int | The maximum items to retrieve (optional) (default to 100)
    filter = '' # str | Filter by an OData (Open Data Protocol) v4 specification (optional) (default to '')

    try:
        # List Break Assessments
        api_response = api_instance.time_tracking_list_break_assessments(offset=offset, limit=limit, filter=filter)
        print("The response of TimeTrackingApi->time_tracking_list_break_assessments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->time_tracking_list_break_assessments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The offset of items to retrieve | [optional] [default to 0]
 **limit** | **int**| The maximum items to retrieve | [optional] [default to 100]
 **filter** | **str**| Filter by an OData (Open Data Protocol) v4 specification | [optional] [default to &#39;&#39;]

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

# **time_tracking_list_break_policies**
> TimeTrackingPaginatedBreakPoliciesResponseV1 time_tracking_list_break_policies(offset=offset, limit=limit, filter=filter, include_counts=include_counts)

List Break Policies

Lists all break policies, with optional filtering.

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
        api_response = api_instance.time_tracking_list_break_policies(offset=offset, limit=limit, filter=filter, include_counts=include_counts)
        print("The response of TimeTrackingApi->time_tracking_list_break_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->time_tracking_list_break_policies: %s\n" % e)
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

# **time_tracking_list_break_policy_breaks**
> TimeTrackingPaginatedBreaksResponseV1 time_tracking_list_break_policy_breaks(id, offset=offset, limit=limit, filter=filter)

List Breaks for Break Policy

List breaks for a specific break policy.

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
        api_response = api_instance.time_tracking_list_break_policy_breaks(id, offset=offset, limit=limit, filter=filter)
        print("The response of TimeTrackingApi->time_tracking_list_break_policy_breaks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->time_tracking_list_break_policy_breaks: %s\n" % e)
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

# **time_tracking_list_break_policy_employees**
> TimeTrackingPaginatedBreakPolicyEmployeesResponseV1 time_tracking_list_break_policy_employees(id, offset=offset, limit=limit)

List Break Policy Employees

Retrieves employees assigned to a specific break policy.

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
        api_response = api_instance.time_tracking_list_break_policy_employees(id, offset=offset, limit=limit)
        print("The response of TimeTrackingApi->time_tracking_list_break_policy_employees:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->time_tracking_list_break_policy_employees: %s\n" % e)
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

# **time_tracking_list_employee_break_availabilities**
> List[TimeTrackingTimeTrackingBreakAvailabilityV1] time_tracking_list_employee_break_availabilities(id, effective=effective)

List Employee Break Availability

Retrieves break availability information for an employee.

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
        # List Employee Break Availability
        api_response = api_instance.time_tracking_list_employee_break_availabilities(id, effective=effective)
        print("The response of TimeTrackingApi->time_tracking_list_employee_break_availabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->time_tracking_list_employee_break_availabilities: %s\n" % e)
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
**403** | Forbidden |  -  |
**422** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_tracking_list_employee_break_policies**
> TimeTrackingPaginatedBreakPoliciesResponseV1 time_tracking_list_employee_break_policies(id, offset=offset, limit=limit)

List Employee Break Policies

Retrieves break policies assigned to a specific employee.

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
        api_response = api_instance.time_tracking_list_employee_break_policies(id, offset=offset, limit=limit)
        print("The response of TimeTrackingApi->time_tracking_list_employee_break_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->time_tracking_list_employee_break_policies: %s\n" % e)
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

# **time_tracking_replace_breaks_for_break_policy**
> List[TimeTrackingTimeTrackingBreakV1] time_tracking_replace_breaks_for_break_policy(id, time_tracking_create_or_update_time_tracking_break_without_policy_v1)

Replace Breaks for Break Policy

Replace all breaks for a break policy. Breaks with an ID will be updated, breaks without an ID will be created. Existing breaks not in the request will be soft deleted.

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
        api_response = api_instance.time_tracking_replace_breaks_for_break_policy(id, time_tracking_create_or_update_time_tracking_break_without_policy_v1)
        print("The response of TimeTrackingApi->time_tracking_replace_breaks_for_break_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->time_tracking_replace_breaks_for_break_policy: %s\n" % e)
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

# **time_tracking_set_break_policy_employees**
> time_tracking_set_break_policy_employees(id, time_tracking_set_break_policy_employees_request)

Set Employees for Break Policy

Sets the employee assignments for a break policy. This replaces all existing assignments with the provided list.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_set_break_policy_employees_request import TimeTrackingSetBreakPolicyEmployeesRequest
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
    time_tracking_set_break_policy_employees_request = bamboohr_sdk.TimeTrackingSetBreakPolicyEmployeesRequest() # TimeTrackingSetBreakPolicyEmployeesRequest | 

    try:
        # Set Employees for Break Policy
        api_instance.time_tracking_set_break_policy_employees(id, time_tracking_set_break_policy_employees_request)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->time_tracking_set_break_policy_employees: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 
 **time_tracking_set_break_policy_employees_request** | [**TimeTrackingSetBreakPolicyEmployeesRequest**](TimeTrackingSetBreakPolicyEmployeesRequest.md)|  | 

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
**403** | Forbidden |  -  |
**404** | Break policy not found |  -  |
**422** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_tracking_sync_break_policy**
> TimeTrackingTimeTrackingBreakPolicyWithRelationsV1 time_tracking_sync_break_policy(id, time_tracking_sync_time_tracking_break_policy_v1)

Sync Break Policy

Sync a break policy by ID. This will synchronize the break policy with the provided data, replacing existing data, including related data (breaks and assignments).

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
        api_response = api_instance.time_tracking_sync_break_policy(id, time_tracking_sync_time_tracking_break_policy_v1)
        print("The response of TimeTrackingApi->time_tracking_sync_break_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->time_tracking_sync_break_policy: %s\n" % e)
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

# **time_tracking_unassign_employees_from_break_policy**
> time_tracking_unassign_employees_from_break_policy(id, time_tracking_unassign_employees_from_break_policy_request)

Unassign Employees from Break Policy

Unassigns the specified employees from a break policy. Removes employee assignments from the policy without affecting the policy itself or other assigned employees. Employees can only be unassigned from policies that are not assigned to all employees.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_unassign_employees_from_break_policy_request import TimeTrackingUnassignEmployeesFromBreakPolicyRequest
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
    time_tracking_unassign_employees_from_break_policy_request = bamboohr_sdk.TimeTrackingUnassignEmployeesFromBreakPolicyRequest() # TimeTrackingUnassignEmployeesFromBreakPolicyRequest | 

    try:
        # Unassign Employees from Break Policy
        api_instance.time_tracking_unassign_employees_from_break_policy(id, time_tracking_unassign_employees_from_break_policy_request)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->time_tracking_unassign_employees_from_break_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 
 **time_tracking_unassign_employees_from_break_policy_request** | [**TimeTrackingUnassignEmployeesFromBreakPolicyRequest**](TimeTrackingUnassignEmployeesFromBreakPolicyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

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

# **time_tracking_update_break**
> TimeTrackingTimeTrackingBreakV1 time_tracking_update_break(id, time_tracking_update_time_tracking_break_v1)

Update Break

Update a break by ID.

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
        api_response = api_instance.time_tracking_update_break(id, time_tracking_update_time_tracking_break_v1)
        print("The response of TimeTrackingApi->time_tracking_update_break:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->time_tracking_update_break: %s\n" % e)
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

# **time_tracking_update_break_policy**
> TimeTrackingTimeTrackingBreakPolicyV1 time_tracking_update_break_policy(id, time_tracking_update_time_tracking_break_policy_v1)

Update Break Policy

Update a break policy by ID.

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
        api_response = api_instance.time_tracking_update_break_policy(id, time_tracking_update_time_tracking_break_policy_v1)
        print("The response of TimeTrackingApi->time_tracking_update_break_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeTrackingApi->time_tracking_update_break_policy: %s\n" % e)
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

