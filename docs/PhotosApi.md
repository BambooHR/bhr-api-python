# bamboohr_sdk.PhotosApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_employee_photo**](PhotosApi.md#get_employee_photo) | **GET** /api/v1/employees/{employeeId}/photo/{size} | Get Employee Photo
[**upload_employee_photo**](PhotosApi.md#upload_employee_photo) | **POST** /api/v1/employees/{employeeId}/photo | Upload Employee Photo


# **get_employee_photo**
> get_employee_photo(employee_id, size)

Get Employee Photo

Get an employee photo

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
    api_instance = bamboohr_sdk.PhotosApi(api_client)
    employee_id = 'employee_id_example' # str | The ID for the employee you are getting the photo for.
    size = 'size_example' # str | Photo size

    try:
        # Get Employee Photo
        api_instance.get_employee_photo(employee_id, size)
    except Exception as e:
        print("Exception when calling PhotosApi->get_employee_photo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| The ID for the employee you are getting the photo for. | 
 **size** | **str**| Photo size | 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_employee_photo**
> upload_employee_photo(employee_id)

Upload Employee Photo

Store a new employee photo

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
    api_instance = bamboohr_sdk.PhotosApi(api_client)
    employee_id = 'employee_id_example' # str | The ID for the employee you are setting the photo for.

    try:
        # Upload Employee Photo
        api_instance.upload_employee_photo(employee_id)
    except Exception as e:
        print("Exception when calling PhotosApi->upload_employee_photo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| The ID for the employee you are setting the photo for. | 

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
**201** | The file was successfully uploaded |  -  |
**404** | if the employee doesn\\&#39;t exist |  -  |
**413** | if the file is too big. |  -  |
**415** | if the file is not in a supported file format or if the width doesn\\&#39;t match the height. |  -  |
**400** | Maximum number of photo uploads exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

