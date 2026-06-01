# bamboohr_sdk.SchedulingApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scheduling_create_schedule**](SchedulingApi.md#scheduling_create_schedule) | **POST** /api/v1/scheduling/schedules | Create Schedule
[**scheduling_create_shift**](SchedulingApi.md#scheduling_create_shift) | **POST** /api/v1/scheduling/shifts | Create Shift
[**scheduling_delete_schedule**](SchedulingApi.md#scheduling_delete_schedule) | **DELETE** /api/v1/scheduling/schedules/{id} | Delete Schedule
[**scheduling_delete_shift**](SchedulingApi.md#scheduling_delete_shift) | **DELETE** /api/v1/scheduling/shifts/{id} | Delete Shift
[**scheduling_get_schedule**](SchedulingApi.md#scheduling_get_schedule) | **GET** /api/v1/scheduling/schedules/{id} | Get Schedule
[**scheduling_get_schedule_pdf**](SchedulingApi.md#scheduling_get_schedule_pdf) | **GET** /api/v1/scheduling/schedules/{id}/pdf | Get Schedule PDF
[**scheduling_get_shift**](SchedulingApi.md#scheduling_get_shift) | **GET** /api/v1/scheduling/shifts/{id} | Get Shift
[**scheduling_list_schedules**](SchedulingApi.md#scheduling_list_schedules) | **GET** /api/v1/scheduling/schedules | List Schedules
[**scheduling_list_shifts**](SchedulingApi.md#scheduling_list_shifts) | **GET** /api/v1/scheduling/shifts | List Shifts
[**scheduling_list_timezones**](SchedulingApi.md#scheduling_list_timezones) | **GET** /api/v1/scheduling/timezones | List Timezones
[**scheduling_publish_shifts**](SchedulingApi.md#scheduling_publish_shifts) | **POST** /api/v1/scheduling/shifts/publish | Publish Shifts
[**scheduling_update_schedule**](SchedulingApi.md#scheduling_update_schedule) | **PATCH** /api/v1/scheduling/schedules/{id} | Update Schedule
[**scheduling_update_shift**](SchedulingApi.md#scheduling_update_shift) | **PATCH** /api/v1/scheduling/shifts/{id} | Update Shift


# **scheduling_create_schedule**
> SchedulingScheduleV1 scheduling_create_schedule(scheduling_create_schedule_request_v1)

Create Schedule

Creates a new schedule for the company. Rejects duplicate schedule data for the same location and configuration.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.scheduling_create_schedule_request_v1 import SchedulingCreateScheduleRequestV1
from bamboohr_sdk.models.scheduling_schedule_v1 import SchedulingScheduleV1
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
    api_instance = bamboohr_sdk.SchedulingApi(api_client)
    scheduling_create_schedule_request_v1 = bamboohr_sdk.SchedulingCreateScheduleRequestV1() # SchedulingCreateScheduleRequestV1 | 

    try:
        # Create Schedule
        api_response = api_instance.scheduling_create_schedule(scheduling_create_schedule_request_v1)
        print("The response of SchedulingApi->scheduling_create_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulingApi->scheduling_create_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduling_create_schedule_request_v1** | [**SchedulingCreateScheduleRequestV1**](SchedulingCreateScheduleRequestV1.md)|  | 

### Return type

[**SchedulingScheduleV1**](SchedulingScheduleV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Schedule created successfully |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**422** | Unprocessable entity - validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduling_create_shift**
> SchedulingSchedulingShiftV1 scheduling_create_shift(scheduling_create_scheduling_shift_request_v1)

Create Shift

Creates a new shift in the specified schedule.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.scheduling_create_scheduling_shift_request_v1 import SchedulingCreateSchedulingShiftRequestV1
from bamboohr_sdk.models.scheduling_scheduling_shift_v1 import SchedulingSchedulingShiftV1
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
    api_instance = bamboohr_sdk.SchedulingApi(api_client)
    scheduling_create_scheduling_shift_request_v1 = bamboohr_sdk.SchedulingCreateSchedulingShiftRequestV1() # SchedulingCreateSchedulingShiftRequestV1 | 

    try:
        # Create Shift
        api_response = api_instance.scheduling_create_shift(scheduling_create_scheduling_shift_request_v1)
        print("The response of SchedulingApi->scheduling_create_shift:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulingApi->scheduling_create_shift: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduling_create_scheduling_shift_request_v1** | [**SchedulingCreateSchedulingShiftRequestV1**](SchedulingCreateSchedulingShiftRequestV1.md)|  | 

### Return type

[**SchedulingSchedulingShiftV1**](SchedulingSchedulingShiftV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a shift. |  -  |
**403** | Forbidden - user does not have permission. |  -  |
**404** | Not Found - the referenced schedule does not exist. |  -  |
**422** | Invalid request data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduling_delete_schedule**
> scheduling_delete_schedule(id)

Delete Schedule

Deletes a schedule by its UUID. Unworked shifts will be deleted as a result.

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
    api_instance = bamboohr_sdk.SchedulingApi(api_client)
    id = 'id_example' # str | The schedule UUID

    try:
        # Delete Schedule
        api_instance.scheduling_delete_schedule(id)
    except Exception as e:
        print("Exception when calling SchedulingApi->scheduling_delete_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The schedule UUID | 

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
**204** | Schedule deleted successfully |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Schedule not found |  -  |
**422** | Invalid request data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduling_delete_shift**
> scheduling_delete_shift(id, recurrence_edit_option=recurrence_edit_option)

Delete Shift

Deletes a shift by its UUID or composite recurrence ID. Use `recurrenceEditOption` to control the scope to delete one or many consecutive recurring shifts

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
    api_instance = bamboohr_sdk.SchedulingApi(api_client)
    id = 'id_example' # str | The shift UUID, or the projected shift composite ID.
    recurrence_edit_option = instance # str | How should the shift be deleted? Choose 'instance' for deleting a single target shift,    'future' for deleting the target shift and all following shifts that are in the same recurrence,    'all' for deleting all shifts starting from now that are in the same recurrence as the target shift. (optional) (default to instance)

    try:
        # Delete Shift
        api_instance.scheduling_delete_shift(id, recurrence_edit_option=recurrence_edit_option)
    except Exception as e:
        print("Exception when calling SchedulingApi->scheduling_delete_shift: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The shift UUID, or the projected shift composite ID. | 
 **recurrence_edit_option** | **str**| How should the shift be deleted? Choose &#39;instance&#39; for deleting a single target shift,    &#39;future&#39; for deleting the target shift and all following shifts that are in the same recurrence,    &#39;all&#39; for deleting all shifts starting from now that are in the same recurrence as the target shift. | [optional] [default to instance]

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
**204** | Shift deleted successfully. No content returned. |  -  |
**403** | Forbidden - user does not have permission. |  -  |
**404** | Not Found - shift not found. |  -  |
**422** | Invalid request data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduling_get_schedule**
> SchedulingScheduleV1 scheduling_get_schedule(id)

Get Schedule

Retrieves a specific schedule by its UUID. Schedules organize shifts for employees.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.scheduling_schedule_v1 import SchedulingScheduleV1
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
    api_instance = bamboohr_sdk.SchedulingApi(api_client)
    id = 'id_example' # str | The ID of the schedule

    try:
        # Get Schedule
        api_response = api_instance.scheduling_get_schedule(id)
        print("The response of SchedulingApi->scheduling_get_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulingApi->scheduling_get_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the schedule | 

### Return type

[**SchedulingScheduleV1**](SchedulingScheduleV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Schedule retrieved successfully |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Schedule not found. |  -  |
**422** | Unprocessable entity - invalid UUID format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduling_get_schedule_pdf**
> scheduling_get_schedule_pdf(id, start_ymd, end_ymd, group_by=group_by, employee_ids=employee_ids, include_employees_without_shifts=include_employees_without_shifts, include_holidays=include_holidays, include_time_off=include_time_off)

Get Schedule PDF

Generates and streams a PDF of the schedule view for the given schedule and date range.

### Example

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.SchedulingApi(api_client)
    id = 'id_example' # str | The schedule ID
    start_ymd = '2013-10-20' # date | Start date in YYYY-MM-DD format
    end_ymd = '2013-10-20' # date | End date in YYYY-MM-DD format
    group_by = 'group_by_example' # str | Group employees by this field (optional)
    employee_ids = ['employee_ids_example'] # List[Optional[str]] | Filter by employee IDs. Pass the string \"null\" as an element to include open shifts. (optional)
    include_employees_without_shifts = False # bool | Whether to include employees who have no shifts in the date range (optional) (default to False)
    include_holidays = False # bool | Whether to include holidays in the PDF (optional) (default to False)
    include_time_off = False # bool | Whether to include time-off entries in the PDF (optional) (default to False)

    try:
        # Get Schedule PDF
        api_instance.scheduling_get_schedule_pdf(id, start_ymd, end_ymd, group_by=group_by, employee_ids=employee_ids, include_employees_without_shifts=include_employees_without_shifts, include_holidays=include_holidays, include_time_off=include_time_off)
    except Exception as e:
        print("Exception when calling SchedulingApi->scheduling_get_schedule_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The schedule ID | 
 **start_ymd** | **date**| Start date in YYYY-MM-DD format | 
 **end_ymd** | **date**| End date in YYYY-MM-DD format | 
 **group_by** | **str**| Group employees by this field | [optional] 
 **employee_ids** | [**List[Optional[str]]**](str.md)| Filter by employee IDs. Pass the string \&quot;null\&quot; as an element to include open shifts. | [optional] 
 **include_employees_without_shifts** | **bool**| Whether to include employees who have no shifts in the date range | [optional] [default to False]
 **include_holidays** | **bool**| Whether to include holidays in the PDF | [optional] [default to False]
 **include_time_off** | **bool**| Whether to include time-off entries in the PDF | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PDF binary stream |  -  |
**403** | Forbidden |  -  |
**404** | Schedule not found |  -  |
**422** | Invalid parameters |  -  |
**500** | Failed to render PDF |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduling_get_shift**
> SchedulingSchedulingShiftV1 scheduling_get_shift(id)

Get Shift

Retrieves a single shift by its UUID. Returns the full shift object including recurrence settings, assigned employee IDs, and status. Returns 404 if the shift does not exist or has been deleted.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.scheduling_scheduling_shift_v1 import SchedulingSchedulingShiftV1
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
    api_instance = bamboohr_sdk.SchedulingApi(api_client)
    id = 'id_example' # str | The shift uuid

    try:
        # Get Shift
        api_response = api_instance.scheduling_get_shift(id)
        print("The response of SchedulingApi->scheduling_get_shift:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulingApi->scheduling_get_shift: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The shift uuid | 

### Return type

[**SchedulingSchedulingShiftV1**](SchedulingSchedulingShiftV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched a shift |  -  |
**403** | Forbidden - user does not have permission |  -  |
**404** | Not Found - shift not found |  -  |
**422** | Invalid request data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduling_list_schedules**
> SchedulingScheduleListResponseV1 scheduling_list_schedules(filter=filter, sort=sort, page=page, page_size=page_size)

List Schedules

Retrieves a paginated list of all schedules for the company. Supports optional OData-style filtering and sorting.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.scheduling_schedule_list_response_v1 import SchedulingScheduleListResponseV1
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
    api_instance = bamboohr_sdk.SchedulingApi(api_client)
    filter = 'filter_example' # str | OData filter expression applied to schedules. Supported operators: `eq` (equals, use `eq null` to match NULL), `ne` (not equals, use `ne null` to match NOT NULL), `lt` (less than), `le` (less than or equal), `gt` (greater than), `ge` (greater than or equal), `in` (value in list), `and` (combine clauses). Not supported: `or`, `not`, parenthesized grouping. Filterable fields: `id`, `name`, `locationId`, `timezone`, `startOfWeek`, `earlyClockInThreshold`, `createdAt`, `updatedAt`, `deletedAt`. Examples: `name eq 'Default Schedule'`, `deletedAt eq null`, `name eq 'Default Schedule' and locationId in (1, 2)`. (optional)
    sort = 'sort_example' # str | Sorting options. Supported sorts are: name, locationId, timezone, startOfWeek, earlyClockInThreshold, createdAt, updatedAt, deletedAt (optional)
    page = 1 # int | The starting page for pagination (optional) (default to 1)
    page_size = 100 # int | The number of items to be returned (optional) (default to 100)

    try:
        # List Schedules
        api_response = api_instance.scheduling_list_schedules(filter=filter, sort=sort, page=page, page_size=page_size)
        print("The response of SchedulingApi->scheduling_list_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulingApi->scheduling_list_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| OData filter expression applied to schedules. Supported operators: &#x60;eq&#x60; (equals, use &#x60;eq null&#x60; to match NULL), &#x60;ne&#x60; (not equals, use &#x60;ne null&#x60; to match NOT NULL), &#x60;lt&#x60; (less than), &#x60;le&#x60; (less than or equal), &#x60;gt&#x60; (greater than), &#x60;ge&#x60; (greater than or equal), &#x60;in&#x60; (value in list), &#x60;and&#x60; (combine clauses). Not supported: &#x60;or&#x60;, &#x60;not&#x60;, parenthesized grouping. Filterable fields: &#x60;id&#x60;, &#x60;name&#x60;, &#x60;locationId&#x60;, &#x60;timezone&#x60;, &#x60;startOfWeek&#x60;, &#x60;earlyClockInThreshold&#x60;, &#x60;createdAt&#x60;, &#x60;updatedAt&#x60;, &#x60;deletedAt&#x60;. Examples: &#x60;name eq &#39;Default Schedule&#39;&#x60;, &#x60;deletedAt eq null&#x60;, &#x60;name eq &#39;Default Schedule&#39; and locationId in (1, 2)&#x60;. | [optional] 
 **sort** | **str**| Sorting options. Supported sorts are: name, locationId, timezone, startOfWeek, earlyClockInThreshold, createdAt, updatedAt, deletedAt | [optional] 
 **page** | **int**| The starting page for pagination | [optional] [default to 1]
 **page_size** | **int**| The number of items to be returned | [optional] [default to 100]

### Return type

[**SchedulingScheduleListResponseV1**](SchedulingScheduleListResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of schedules |  -  |
**400** | Bad request - invalid filter, sort, or pagination parameters. |  -  |
**403** | Forbidden - insufficient permissions. |  -  |
**422** | Unprocessable entity - invalid filter or sort syntax. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduling_list_shifts**
> SchedulingShiftListResponseV1 scheduling_list_shifts(ids=ids, start=start, end=end, employee_ids=employee_ids, schedule_ids=schedule_ids, statuses=statuses, page=page, page_size=page_size)

List Shifts

Lists shifts matching the given filters. Either provide `ids` (ignores all other filters) or provide `start`, `end`, and at least one of `employeeIds` or `scheduleIds`. The time window must be no longer than 1 month. Defaults to returning planned and published shifts.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.scheduling_shift_list_response_v1 import SchedulingShiftListResponseV1
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
    api_instance = bamboohr_sdk.SchedulingApi(api_client)
    ids = ['ids_example'] # List[str] | Filter by shift IDs. If provided, other filters are ignored. (optional)
    start = '2013-10-20T19:20:30+01:00' # datetime | Start datetime for the shift window (ISO-8601 datetime string). Required if ids not provided. (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime | End datetime for the shift window (ISO-8601 datetime string). Required if ids not provided. (optional)
    employee_ids = ['employee_ids_example'] # List[str] | Filter by employee IDs. Use the string \"null\" as a value to include unassigned shifts (e.g. employeeIds[]=10&employeeIds[]=null). (optional)
    schedule_ids = ['schedule_ids_example'] # List[str] | Filter by schedule IDs. (optional)
    statuses = ["planned","published"] # List[str] | Filter by shift statuses. (optional) (default to ["planned","published"])
    page = 1 # int | The starting page for pagination. (optional) (default to 1)
    page_size = 1000 # int | The number of items to be returned. (optional) (default to 1000)

    try:
        # List Shifts
        api_response = api_instance.scheduling_list_shifts(ids=ids, start=start, end=end, employee_ids=employee_ids, schedule_ids=schedule_ids, statuses=statuses, page=page, page_size=page_size)
        print("The response of SchedulingApi->scheduling_list_shifts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulingApi->scheduling_list_shifts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[str]**](str.md)| Filter by shift IDs. If provided, other filters are ignored. | [optional] 
 **start** | **datetime**| Start datetime for the shift window (ISO-8601 datetime string). Required if ids not provided. | [optional] 
 **end** | **datetime**| End datetime for the shift window (ISO-8601 datetime string). Required if ids not provided. | [optional] 
 **employee_ids** | [**List[str]**](str.md)| Filter by employee IDs. Use the string \&quot;null\&quot; as a value to include unassigned shifts (e.g. employeeIds[]&#x3D;10&amp;employeeIds[]&#x3D;null). | [optional] 
 **schedule_ids** | [**List[str]**](str.md)| Filter by schedule IDs. | [optional] 
 **statuses** | [**List[str]**](str.md)| Filter by shift statuses. | [optional] [default to [&quot;planned&quot;,&quot;published&quot;]]
 **page** | **int**| The starting page for pagination. | [optional] [default to 1]
 **page_size** | **int**| The number of items to be returned. | [optional] [default to 1000]

### Return type

[**SchedulingShiftListResponseV1**](SchedulingShiftListResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Shifts retrieved successfully |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**422** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduling_list_timezones**
> SchedulingTimezoneListResponseV1 scheduling_list_timezones(filter=filter, sort=sort, page=page, page_size=page_size)

List Timezones

Returns a paginated list of timezones available for use when creating or editing schedules. Supports OData-style filtering on the `name` field.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.scheduling_timezone_list_response_v1 import SchedulingTimezoneListResponseV1
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
    api_instance = bamboohr_sdk.SchedulingApi(api_client)
    filter = 'filter_example' # str | OData filter expression applied to the `name` field. Supported operators: `eq` (exact match), `ne` (exclude), `and` (combine clauses). Supported string functions: `contains`, `startswith`, `endswith` (all case-insensitive). Not supported: `or`, `not`, parenthesized grouping. Examples: `name eq 'America/Denver'`, `name ne 'UTC'`, `contains(name, 'America')`, `startswith(name, 'US/')`, `endswith(name, 'York')`. (optional)
    sort = 'sort_example' # str | Sorting options. Supported sort fields: `name` (alphabetical), `offset` (numeric UTC offset). Example: `name asc` or `offset desc` (optional)
    page = 1 # int | The starting page for pagination. Defaults to 1. (optional) (default to 1)
    page_size = 100 # int | The number of items to be returned. Defaults to 100. (optional) (default to 100)

    try:
        # List Timezones
        api_response = api_instance.scheduling_list_timezones(filter=filter, sort=sort, page=page, page_size=page_size)
        print("The response of SchedulingApi->scheduling_list_timezones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulingApi->scheduling_list_timezones: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| OData filter expression applied to the &#x60;name&#x60; field. Supported operators: &#x60;eq&#x60; (exact match), &#x60;ne&#x60; (exclude), &#x60;and&#x60; (combine clauses). Supported string functions: &#x60;contains&#x60;, &#x60;startswith&#x60;, &#x60;endswith&#x60; (all case-insensitive). Not supported: &#x60;or&#x60;, &#x60;not&#x60;, parenthesized grouping. Examples: &#x60;name eq &#39;America/Denver&#39;&#x60;, &#x60;name ne &#39;UTC&#39;&#x60;, &#x60;contains(name, &#39;America&#39;)&#x60;, &#x60;startswith(name, &#39;US/&#39;)&#x60;, &#x60;endswith(name, &#39;York&#39;)&#x60;. | [optional] 
 **sort** | **str**| Sorting options. Supported sort fields: &#x60;name&#x60; (alphabetical), &#x60;offset&#x60; (numeric UTC offset). Example: &#x60;name asc&#x60; or &#x60;offset desc&#x60; | [optional] 
 **page** | **int**| The starting page for pagination. Defaults to 1. | [optional] [default to 1]
 **page_size** | **int**| The number of items to be returned. Defaults to 100. | [optional] [default to 100]

### Return type

[**SchedulingTimezoneListResponseV1**](SchedulingTimezoneListResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of timezones. |  -  |
**403** | Forbidden - insufficient permissions. |  -  |
**422** | Unprocessable entity - invalid filter or pagination parameters. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduling_publish_shifts**
> SchedulingPublishShiftsResultV1 scheduling_publish_shifts(scheduling_publish_shifts_request)

Publish Shifts

Publishes one or more planned shifts, making them visible to employees. Shifts with scheduling conflicts are skipped and reported as failures. Returns 200 if all shifts succeed, 207 if some shifts failed due to conflicts, or 409 if all shifts failed due to conflicts.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.scheduling_publish_shifts_request import SchedulingPublishShiftsRequest
from bamboohr_sdk.models.scheduling_publish_shifts_result_v1 import SchedulingPublishShiftsResultV1
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
    api_instance = bamboohr_sdk.SchedulingApi(api_client)
    scheduling_publish_shifts_request = bamboohr_sdk.SchedulingPublishShiftsRequest() # SchedulingPublishShiftsRequest | 

    try:
        # Publish Shifts
        api_response = api_instance.scheduling_publish_shifts(scheduling_publish_shifts_request)
        print("The response of SchedulingApi->scheduling_publish_shifts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulingApi->scheduling_publish_shifts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduling_publish_shifts_request** | [**SchedulingPublishShiftsRequest**](SchedulingPublishShiftsRequest.md)|  | 

### Return type

[**SchedulingPublishShiftsResultV1**](SchedulingPublishShiftsResultV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All shifts published successfully |  -  |
**207** | Some shifts published successfully, but one or more failed due to conflicts |  -  |
**409** | All shifts failed to publish due to conflicts |  -  |
**403** | Forbidden - user does not have permission |  -  |
**422** | Invalid request data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduling_update_schedule**
> SchedulingScheduleV1 scheduling_update_schedule(id, scheduling_update_schedule_request_v1)

Update Schedule

Partially updates an existing schedule by its UUID. Fields not provided retain their existing values.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.scheduling_schedule_v1 import SchedulingScheduleV1
from bamboohr_sdk.models.scheduling_update_schedule_request_v1 import SchedulingUpdateScheduleRequestV1
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
    api_instance = bamboohr_sdk.SchedulingApi(api_client)
    id = 'id_example' # str | The schedule UUID
    scheduling_update_schedule_request_v1 = bamboohr_sdk.SchedulingUpdateScheduleRequestV1() # SchedulingUpdateScheduleRequestV1 | 

    try:
        # Update Schedule
        api_response = api_instance.scheduling_update_schedule(id, scheduling_update_schedule_request_v1)
        print("The response of SchedulingApi->scheduling_update_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulingApi->scheduling_update_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The schedule UUID | 
 **scheduling_update_schedule_request_v1** | [**SchedulingUpdateScheduleRequestV1**](SchedulingUpdateScheduleRequestV1.md)|  | 

### Return type

[**SchedulingScheduleV1**](SchedulingScheduleV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Schedule updated successfully |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Schedule not found. |  -  |
**422** | Unprocessable entity - validation failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scheduling_update_shift**
> SchedulingSchedulingShiftV1 scheduling_update_shift(id, scheduling_update_scheduling_shift_request_v1)

Update Shift

Updates a shift by its UUID. Fields not provided will retain their existing values. For published shifts, changes are not applied directly — they are stored as pending (`unpublishedChanges`) and take effect when the shift is published. `recurrenceEditOption` is required when the shift already has recurrence settings; ALL and FUTURE edits propagate to published sibling occurrences the same way, staging changes rather than applying them immediately. Sibling shifts may be permanently removed if they no longer conform to changed recurrence fields.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.scheduling_scheduling_shift_v1 import SchedulingSchedulingShiftV1
from bamboohr_sdk.models.scheduling_update_scheduling_shift_request_v1 import SchedulingUpdateSchedulingShiftRequestV1
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
    api_instance = bamboohr_sdk.SchedulingApi(api_client)
    id = 'id_example' # str | The shift uuid
    scheduling_update_scheduling_shift_request_v1 = bamboohr_sdk.SchedulingUpdateSchedulingShiftRequestV1() # SchedulingUpdateSchedulingShiftRequestV1 | 

    try:
        # Update Shift
        api_response = api_instance.scheduling_update_shift(id, scheduling_update_scheduling_shift_request_v1)
        print("The response of SchedulingApi->scheduling_update_shift:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchedulingApi->scheduling_update_shift: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The shift uuid | 
 **scheduling_update_scheduling_shift_request_v1** | [**SchedulingUpdateSchedulingShiftRequestV1**](SchedulingUpdateSchedulingShiftRequestV1.md)|  | 

### Return type

[**SchedulingSchedulingShiftV1**](SchedulingSchedulingShiftV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated a shift |  -  |
**403** | Forbidden - user does not have permission |  -  |
**404** | Not Found - shift not found. |  -  |
**422** | Invalid request data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

