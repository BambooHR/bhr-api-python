# bamboohr_sdk.CompanyFilesApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_company_file_category**](CompanyFilesApi.md#add_company_file_category) | **POST** /api/v1/files/categories | Create Company File Category
[**delete_company_file**](CompanyFilesApi.md#delete_company_file) | **DELETE** /api/v1/files/{fileId} | Delete Company File
[**get_company_file**](CompanyFilesApi.md#get_company_file) | **GET** /api/v1/files/{fileId} | Get Company File
[**list_company_files**](CompanyFilesApi.md#list_company_files) | **GET** /api/v1/files/view | Get Company Files and Categories
[**update_company_file**](CompanyFilesApi.md#update_company_file) | **POST** /api/v1/files/{fileId} | Update Company File
[**upload_company_file**](CompanyFilesApi.md#upload_company_file) | **POST** /api/v1/files | Upload Company File


# **add_company_file_category**
> add_company_file_category(request_body)

Create Company File Category

Add a company file category.

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
    api_instance = bamboohr_sdk.CompanyFilesApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Create Company File Category
        api_instance.add_company_file_category(request_body)
    except Exception as e:
        print("Exception when calling CompanyFilesApi->add_company_file_category: %s\n" % e)
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
**400** | if the posted JSON is invalid or there was no category name given. |  -  |
**403** | if the API user does not have permission to see the company files. |  -  |
**500** | there was an unknown server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_company_file**
> delete_company_file(file_id)

Delete Company File

Delete a company file

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
    api_instance = bamboohr_sdk.CompanyFilesApi(api_client)
    file_id = 'file_id_example' # str | {fileId} is the ID of the company file being deleted.

    try:
        # Delete Company File
        api_instance.delete_company_file(file_id)
    except Exception as e:
        print("Exception when calling CompanyFilesApi->delete_company_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| {fileId} is the ID of the company file being deleted. | 

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
**200** | Company file was deleted |  -  |
**403** | if the API user does not have permission to see the requested file. |  -  |
**404** | if the file was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_file**
> get_company_file(file_id)

Get Company File

Gets an company file

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
    api_instance = bamboohr_sdk.CompanyFilesApi(api_client)
    file_id = 'file_id_example' # str | {fileId} is the ID of the company file being retrieved.

    try:
        # Get Company File
        api_instance.get_company_file(file_id)
    except Exception as e:
        print("Exception when calling CompanyFilesApi->get_company_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| {fileId} is the ID of the company file being retrieved. | 

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
**200** | Company file was successfully retrieved |  -  |
**403** | if the API user does not have permission to see the company files. |  -  |
**404** | if the file was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_company_files**
> list_company_files()

Get Company Files and Categories

Lists company files and categories

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
    api_instance = bamboohr_sdk.CompanyFilesApi(api_client)

    try:
        # Get Company Files and Categories
        api_instance.list_company_files()
    except Exception as e:
        print("Exception when calling CompanyFilesApi->list_company_files: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | Company files and category list |  -  |
**403** | if the API user does not have permission to see the company files. |  -  |
**404** | if no files or categories are found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_company_file**
> update_company_file(file_id, company_file_update)

Update Company File

Update a company file

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.company_file_update import CompanyFileUpdate
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
    api_instance = bamboohr_sdk.CompanyFilesApi(api_client)
    file_id = 'file_id_example' # str | {fileId} is the ID of the employee file being updated.
    company_file_update = bamboohr_sdk.CompanyFileUpdate() # CompanyFileUpdate | 

    try:
        # Update Company File
        api_instance.update_company_file(file_id, company_file_update)
    except Exception as e:
        print("Exception when calling CompanyFilesApi->update_company_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| {fileId} is the ID of the employee file being updated. | 
 **company_file_update** | [**CompanyFileUpdate**](CompanyFileUpdate.md)|  | 

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
**400** | if the posted JSON is invalid. |  -  |
**403** | if the API user does not have permission to see the company files. |  -  |
**404** | if the file or category was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_company_file**
> upload_company_file()

Upload Company File

Upload a company file

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
    api_instance = bamboohr_sdk.CompanyFilesApi(api_client)

    try:
        # Upload Company File
        api_instance.upload_company_file()
    except Exception as e:
        print("Exception when calling CompanyFilesApi->upload_company_file: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**201** | The company file was successfully uploaded |  -  |
**403** | if the API user does not have permission to see the company files. |  -  |
**404** | if the category ID was not found. |  -  |
**413** | if the file size exceeds 20MB or the storage limit for the company. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

