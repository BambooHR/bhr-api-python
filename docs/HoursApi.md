# bamboohr_sdk.HoursApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_time_tracking_bulk**](HoursApi.md#add_time_tracking_bulk) | **POST** /api/v1/timetracking/record | Create or Update Hour Records
[**add_time_tracking_hour_record**](HoursApi.md#add_time_tracking_hour_record) | **POST** /api/v1/timetracking/add | Create Hour Record
[**delete_time_tracking_by_id**](HoursApi.md#delete_time_tracking_by_id) | **DELETE** /api/v1/timetracking/delete/{id} | Delete Hour Record
[**edit_time_tracking_record**](HoursApi.md#edit_time_tracking_record) | **PUT** /api/v1/timetracking/adjust | Update Hour Record
[**get_time_tracking_record**](HoursApi.md#get_time_tracking_record) | **GET** /api/v1/timetracking/record/{id} | Get Hour Record


# **add_time_tracking_bulk**
> TimeTrackingBulkResponseSchema add_time_tracking_bulk(time_tracking_record)

Create or Update Hour Records

Bulk add/edit hour records

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
        api_response = api_instance.add_time_tracking_bulk(time_tracking_record)
        print("The response of HoursApi->add_time_tracking_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HoursApi->add_time_tracking_bulk: %s\n" % e)
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
**201** | An array of objects with success as true or false depending on the success of each time tracking object in the request along with the successful IDs or the reason of the error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_time_tracking_hour_record**
> TimeTrackingIdResponseSchema add_time_tracking_hour_record(time_tracking_record)

Create Hour Record

Add an hour record

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
        api_response = api_instance.add_time_tracking_hour_record(time_tracking_record)
        print("The response of HoursApi->add_time_tracking_hour_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HoursApi->add_time_tracking_hour_record: %s\n" % e)
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
**201** | The time tracking ID will be returned in JSON. |  -  |
**400** | If any required field is missing, any of the IDs are invalid, or the posted JSON is not valid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_time_tracking_by_id**
> TimeTrackingDeleteResponseSchema delete_time_tracking_by_id(id)

Delete Hour Record

Delete an hour record

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
        api_response = api_instance.delete_time_tracking_by_id(id)
        print("The response of HoursApi->delete_time_tracking_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HoursApi->delete_time_tracking_by_id: %s\n" % e)
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
**201** | Record removed. |  -  |
**400** | If the time tracking ID cannot be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_time_tracking_record**
> TimeTrackingIdResponseSchema edit_time_tracking_record(adjust_time_tracking_request_schema)

Update Hour Record

Edit an hour record

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
        api_response = api_instance.edit_time_tracking_record(adjust_time_tracking_request_schema)
        print("The response of HoursApi->edit_time_tracking_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HoursApi->edit_time_tracking_record: %s\n" % e)
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
**201** | The time tracking ID will be returned in JSON. |  -  |
**400** | if any required field is missing, any of the IDs are invalid, or the posted JSON is not valid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_tracking_record**
> TimeTrackingRecordSchema get_time_tracking_record(id)

Get Hour Record

Get an hour record

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
    id = 'id_example' # str | {id} is the time tracking ID used to originally create the record.

    try:
        # Get Hour Record
        api_response = api_instance.get_time_tracking_record(id)
        print("The response of HoursApi->get_time_tracking_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HoursApi->get_time_tracking_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| {id} is the time tracking ID used to originally create the record. | 

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
**200** | The response content will be a JSON document with the requested information. |  -  |
**400** | Invalid or missing argument. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

