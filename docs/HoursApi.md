# bamboohr_sdk.HoursApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_time_tracking_hour_records**](HoursApi.md#create_or_update_time_tracking_hour_records) | **POST** /api/v1/timetracking/record | Create or Update Hour Records
[**create_time_tracking_hour_record**](HoursApi.md#create_time_tracking_hour_record) | **POST** /api/v1/timetracking/add | Create Hour Record
[**delete_time_tracking_hour_record**](HoursApi.md#delete_time_tracking_hour_record) | **DELETE** /api/v1/timetracking/delete/{id} | Delete Hour Record
[**get_time_tracking_record**](HoursApi.md#get_time_tracking_record) | **GET** /api/v1/timetracking/record/{id} | Get Time Tracking Record
[**update_time_tracking_record**](HoursApi.md#update_time_tracking_record) | **PUT** /api/v1/timetracking/adjust | Update Hour Record


# **create_or_update_time_tracking_hour_records**
> TimeTrackingBulkResponseSchema create_or_update_time_tracking_hour_records(time_tracking_record)

Create or Update Hour Records

Bulk add/edit hour records. The endpoint can return HTTP 201 even when individual items fail validation; inspect each item's `success` flag and per-item `response.message` for partial failures.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_bulk_response_schema import TimeTrackingBulkResponseSchema
from bamboohr_sdk.models.time_tracking_record import TimeTrackingRecord
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
    api_instance = bamboohr_sdk.HoursApi(api_client)
    time_tracking_record = [bamboohr_sdk.TimeTrackingRecord()] # List[TimeTrackingRecord] | 

    try:
        # Create or Update Hour Records
        api_response = api_instance.create_or_update_time_tracking_hour_records(time_tracking_record)
        print("The response of HoursApi->create_or_update_time_tracking_hour_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HoursApi->create_or_update_time_tracking_hour_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_tracking_record** | [**List[TimeTrackingRecord]**](TimeTrackingRecord.md)|  | 

### Return type

[**TimeTrackingBulkResponseSchema**](TimeTrackingBulkResponseSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns an array of per-item results. Each item has a &#x60;success&#x60; boolean and a &#x60;response&#x60; object containing the resulting &#x60;id&#x60; on success, or a &#x60;message&#x60; describing the failure. Note: HTTP 201 is returned even when individual items fail; inspect each item&#39;s &#x60;success&#x60; field for partial failures. |  -  |
**403** | Forbidden. Insufficient user permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_time_tracking_hour_record**
> TimeTrackingIdResponseSchema create_time_tracking_hour_record(time_tracking_record)

Create Hour Record

Adds a single hour record. Use this endpoint when creating one record at a time. For bulk imports, use create-or-update-time-tracking-hour-records.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_id_response_schema import TimeTrackingIdResponseSchema
from bamboohr_sdk.models.time_tracking_record import TimeTrackingRecord
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
    api_instance = bamboohr_sdk.HoursApi(api_client)
    time_tracking_record = bamboohr_sdk.TimeTrackingRecord() # TimeTrackingRecord | 

    try:
        # Create Hour Record
        api_response = api_instance.create_time_tracking_hour_record(time_tracking_record)
        print("The response of HoursApi->create_time_tracking_hour_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HoursApi->create_time_tracking_hour_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_tracking_record** | [**TimeTrackingRecord**](TimeTrackingRecord.md)|  | 

### Return type

[**TimeTrackingIdResponseSchema**](TimeTrackingIdResponseSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Record created. Returns the new time tracking ID. |  -  |
**400** | If any required field is missing, referenced IDs are invalid, or the posted JSON is invalid. |  -  |
**403** | Forbidden. Insufficient user permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_time_tracking_hour_record**
> TimeTrackingDeleteResponseSchema delete_time_tracking_hour_record(id)

Delete Hour Record

Deletes an hour record by `timeTrackingId` (`id` path parameter). This removes all stored revisions associated with that logical time tracking record. Not-found and invalid-id cases are currently returned as a 400 invalid-argument response for backward compatibility.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_delete_response_schema import TimeTrackingDeleteResponseSchema
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
    api_instance = bamboohr_sdk.HoursApi(api_client)
    id = 'id_example' # str | The time tracking id is the id that was used to track the record up to 36 characters in length. (i.e. UUID).

    try:
        # Delete Hour Record
        api_response = api_instance.delete_time_tracking_hour_record(id)
        print("The response of HoursApi->delete_time_tracking_hour_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HoursApi->delete_time_tracking_hour_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The time tracking id is the id that was used to track the record up to 36 characters in length. (i.e. UUID). | 

### Return type

[**TimeTrackingDeleteResponseSchema**](TimeTrackingDeleteResponseSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Record removed. |  -  |
**400** | If the time tracking ID cannot be found. |  -  |
**403** | Forbidden. Insufficient permissions to delete this record. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_tracking_record**
> TimeTrackingRecordSchema get_time_tracking_record(id)

Get Time Tracking Record

Retrieves a single time tracking hour record by its ID. Returns the full record details including hours, date, employee, project, task, and shift differential information. The `project` and `shiftDifferential` fields are null when not applicable. For historical compatibility, missing records may surface as an empty/null payload rather than a strict not-found response.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_record_schema import TimeTrackingRecordSchema
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
    api_instance = bamboohr_sdk.HoursApi(api_client)
    id = 'id_example' # str | The time tracking record ID used to originally create the record.

    try:
        # Get Time Tracking Record
        api_response = api_instance.get_time_tracking_record(id)
        print("The response of HoursApi->get_time_tracking_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HoursApi->get_time_tracking_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The time tracking record ID used to originally create the record. | 

### Return type

[**TimeTrackingRecordSchema**](TimeTrackingRecordSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the time tracking record. |  -  |
**400** | Invalid or missing argument. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Forbidden. Insufficient permissions to view this record. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_time_tracking_record**
> TimeTrackingIdResponseSchema update_time_tracking_record(adjust_time_tracking_request_schema)

Update Hour Record

Edits an existing hour record by `timeTrackingId`.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.adjust_time_tracking_request_schema import AdjustTimeTrackingRequestSchema
from bamboohr_sdk.models.time_tracking_id_response_schema import TimeTrackingIdResponseSchema
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
    api_instance = bamboohr_sdk.HoursApi(api_client)
    adjust_time_tracking_request_schema = bamboohr_sdk.AdjustTimeTrackingRequestSchema() # AdjustTimeTrackingRequestSchema | 

    try:
        # Update Hour Record
        api_response = api_instance.update_time_tracking_record(adjust_time_tracking_request_schema)
        print("The response of HoursApi->update_time_tracking_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HoursApi->update_time_tracking_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adjust_time_tracking_request_schema** | [**AdjustTimeTrackingRequestSchema**](AdjustTimeTrackingRequestSchema.md)|  | 

### Return type

[**TimeTrackingIdResponseSchema**](TimeTrackingIdResponseSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Record updated. Returns the time tracking ID. |  -  |
**400** | If any required field is missing, referenced IDs are invalid, or the posted JSON is invalid. |  -  |
**403** | Forbidden. Insufficient user permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

