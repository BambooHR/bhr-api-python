# bamboohr_sdk.EmployeeFilesApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_employee_file_category**](EmployeeFilesApi.md#add_employee_file_category) | **POST** /api/v1/employees/files/categories | Create Employee File Category
[**delete_employee_file**](EmployeeFilesApi.md#delete_employee_file) | **DELETE** /api/v1/employees/{id}/files/{fileId} | Delete Employee File
[**get_employee_file**](EmployeeFilesApi.md#get_employee_file) | **GET** /api/v1/employees/{id}/files/{fileId} | Get Employee File
[**list_employee_files**](EmployeeFilesApi.md#list_employee_files) | **GET** /api/v1/employees/{id}/files/view | Get Employee Files and Categories
[**update_employee_file**](EmployeeFilesApi.md#update_employee_file) | **POST** /api/v1/employees/{id}/files/{fileId} | Update Employee File
[**upload_employee_file**](EmployeeFilesApi.md#upload_employee_file) | **POST** /api/v1/employees/{id}/files | Upload Employee File


# **add_employee_file_category**
> add_employee_file_category(request_body)

Create Employee File Category

Add an employee file category.

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
    api_instance = bamboohr_sdk.EmployeeFilesApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Create Employee File Category
        api_instance.add_employee_file_category(request_body)
    except Exception as e:
        print("Exception when calling EmployeeFilesApi->add_employee_file_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

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
**201** | The category was created |  -  |
**400** | if the posted XML is invalid or there was no category name given. |  -  |
**403** | if the API user does not have permission to create employee categories. |  -  |
**500** | there was an unknown server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_employee_file**
> delete_employee_file(id, file_id)

Delete Employee File

Delete an employee file

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
    api_instance = bamboohr_sdk.EmployeeFilesApi(api_client)
    id = '0' # str | {id} is an employee ID. The special employee ID of zero (0) means to use the employee ID associated with the API key (if any). (default to '0')
    file_id = 'file_id_example' # str | {fileId} is the ID of the employee file being deleted.

    try:
        # Delete Employee File
        api_instance.delete_employee_file(id, file_id)
    except Exception as e:
        print("Exception when calling EmployeeFilesApi->delete_employee_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| {id} is an employee ID. The special employee ID of zero (0) means to use the employee ID associated with the API key (if any). | [default to &#39;0&#39;]
 **file_id** | **str**| {fileId} is the ID of the employee file being deleted. | 

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
**200** | Employee file was deleted |  -  |
**403** | if the API user does not have permission to see the requested employee or the employee\\&#39;s files. |  -  |
**404** | if the employee file was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_file**
> get_employee_file(id, file_id)

Get Employee File

Gets an employee file

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
    api_instance = bamboohr_sdk.EmployeeFilesApi(api_client)
    id = '0' # str | {id} is an employee ID. The special employee ID of zero (0) means to use the employee ID associated with the API key (if any). (default to '0')
    file_id = 'file_id_example' # str | {fileId} is the ID of the employee file being retrieved.

    try:
        # Get Employee File
        api_instance.get_employee_file(id, file_id)
    except Exception as e:
        print("Exception when calling EmployeeFilesApi->get_employee_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| {id} is an employee ID. The special employee ID of zero (0) means to use the employee ID associated with the API key (if any). | [default to &#39;0&#39;]
 **file_id** | **str**| {fileId} is the ID of the employee file being retrieved. | 

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
**200** | Employee file was successfully retrieved |  -  |
**403** | if the API user does not have permission to see the requested employee or the employee\\&#39;s files. |  -  |
**404** | if the employee file was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_employee_files**
> list_employee_files(id)

Get Employee Files and Categories

Lists employee files and categories

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
    api_instance = bamboohr_sdk.EmployeeFilesApi(api_client)
    id = '1501' # str | Employee ID is required and needs to be a valid employee ID.

    try:
        # Get Employee Files and Categories
        api_instance.list_employee_files(id)
    except Exception as e:
        print("Exception when calling EmployeeFilesApi->list_employee_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Employee ID is required and needs to be a valid employee ID. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Employee file and category list |  -  |
**403** | if the API user does not have permission to see the requested employee or the employee\\&#39;s files. |  -  |
**404** | if no files or employees are found for this employee. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_employee_file**
> update_employee_file(id, file_id, employee_file_update)

Update Employee File

Update an employee file

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.employee_file_update import EmployeeFileUpdate
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
    api_instance = bamboohr_sdk.EmployeeFilesApi(api_client)
    id = '0' # str | {id} is an employee ID. The special employee ID of zero (0) means to use the employee ID associated with the API key (if any). (default to '0')
    file_id = 'file_id_example' # str | {fileId} is the ID of the employee file being updated.
    employee_file_update = bamboohr_sdk.EmployeeFileUpdate() # EmployeeFileUpdate | 

    try:
        # Update Employee File
        api_instance.update_employee_file(id, file_id, employee_file_update)
    except Exception as e:
        print("Exception when calling EmployeeFilesApi->update_employee_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| {id} is an employee ID. The special employee ID of zero (0) means to use the employee ID associated with the API key (if any). | [default to &#39;0&#39;]
 **file_id** | **str**| {fileId} is the ID of the employee file being updated. | 
 **employee_file_update** | [**EmployeeFileUpdate**](EmployeeFileUpdate.md)|  | 

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
**200** | The employee file was updated |  -  |
**400** | Invalid JSON |  -  |
**403** | if the API user does not have permission to see the requested employee or the employee\\&#39;s files. |  -  |
**404** | if the employee file or category was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_employee_file**
> upload_employee_file(id)

Upload Employee File

Upload an employee file

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
    api_instance = bamboohr_sdk.EmployeeFilesApi(api_client)
    id = '0' # str | {id} is an employee ID. The special employee ID of zero (0) means to use the employee ID associated with the API key (if any). (default to '0')

    try:
        # Upload Employee File
        api_instance.upload_employee_file(id)
    except Exception as e:
        print("Exception when calling EmployeeFilesApi->upload_employee_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| {id} is an employee ID. The special employee ID of zero (0) means to use the employee ID associated with the API key (if any). | [default to &#39;0&#39;]

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
**201** | The employee file was successfully uploaded |  -  |
**403** | if the API user does not have permission to see the requested employee or the employee\\&#39;s files. |  -  |
**404** | if the category ID was not found. |  -  |
**413** | if the file size exceeds 20MB or the storage limit for the company. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

