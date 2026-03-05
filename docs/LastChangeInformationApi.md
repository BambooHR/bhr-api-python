# bamboohr_sdk.LastChangeInformationApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_changed_employee_ids**](LastChangeInformationApi.md#get_changed_employee_ids) | **GET** /api/v1/employees/changed | Get Updated Employee IDs


# **get_changed_employee_ids**
> get_changed_employee_ids(since, type=type)

Get Updated Employee IDs

This API allows for efficient syncing of employee data. When you use this API you will provide a timestamp and the results will be limited to just the employees that have changed since the time you provided. This API operates on an employee-last-changed-timestamp, which means that a change in ANY individual field in the employee record, as well as any change to the employment status, job info, or compensation tables, will cause that employee to be returned via this API.

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
    api_instance = bamboohr_sdk.LastChangeInformationApi(api_client)
    since = 'since_example' # str | URL encoded iso8601 timestamp
    type = 'type_example' # str | Use one of these in the {type} variable in the URL: \"inserted\", \"updated\", \"deleted\" (optional)

    try:
        # Get Updated Employee IDs
        api_instance.get_changed_employee_ids(since, type=type)
    except Exception as e:
        print("Exception when calling LastChangeInformationApi->get_changed_employee_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **str**| URL encoded iso8601 timestamp | 
 **type** | **str**| Use one of these in the {type} variable in the URL: \&quot;inserted\&quot;, \&quot;updated\&quot;, \&quot;deleted\&quot; | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

