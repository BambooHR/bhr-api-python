# bamboohr_sdk.LastChangeInformationApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_changed_employee_ids**](LastChangeInformationApi.md#get_changed_employee_ids) | **GET** /api/v1/employees/changed | Get Changed Employee IDs


# **get_changed_employee_ids**
> ChangedEmployeeIdsResponse get_changed_employee_ids(since, type=type)

Get Changed Employee IDs

Returns a list of employee IDs that have changed since the given timestamp. This allows for efficient syncing of employee data — rather than downloading all employees, only those that have changed are returned. A change in ANY individual field in the employee record, as well as any change to the employment status, job info, or compensation tables, will cause that employee to be returned. Each entry includes the employee ID, the type of change (Inserted, Updated, or Deleted), and the last-changed timestamp.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.changed_employee_ids_response import ChangedEmployeeIdsResponse
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
    api_instance = bamboohr_sdk.LastChangeInformationApi(api_client)
    since = '2013-10-20T19:20:30+01:00' # datetime | ISO 8601 timestamp (URL-encoded). Only employees changed since this timestamp will be returned.
    type = 'type_example' # str | Filter by change type. If omitted, all change types are returned. (optional)

    try:
        # Get Changed Employee IDs
        api_response = api_instance.get_changed_employee_ids(since, type=type)
        print("The response of LastChangeInformationApi->get_changed_employee_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LastChangeInformationApi->get_changed_employee_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **datetime**| ISO 8601 timestamp (URL-encoded). Only employees changed since this timestamp will be returned. | 
 **type** | **str**| Filter by change type. If omitted, all change types are returned. | [optional] 

### Return type

[**ChangedEmployeeIdsResponse**](ChangedEmployeeIdsResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The latest change timestamp in the result set and a map of employees changed since the given timestamp. |  -  |
**400** | The since parameter is missing, is not a valid ISO 8601 date, or the type parameter is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

