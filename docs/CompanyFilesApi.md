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

Creates one or more company file categories. Accepts a JSON array of category name strings or an equivalent XML document. An empty payload returns 200 without creating anything. Returns 400 if a name is empty or already exists, 403 if the caller lacks permission or the name is reserved, and 500 on an internal error.

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

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was processed but no categories were created (empty payload). |  -  |
**201** | All specified categories were created successfully. |  -  |
**400** | The request body contains malformed JSON or XML, an empty category name, or a category name that already exists. |  -  |
**403** | The API user does not have permission to create company file categories, or the category name is reserved. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_company_file**
> delete_company_file(file_id)

Delete Company File

Deletes the specified company file. Requires the caller to have company file write access. Returns 404 if the file does not exist, 403 if the caller lacks permission, and 500 on an internal error.

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
    file_id = 56 # int | The ID of the company file to delete.

    try:
        # Delete Company File
        api_instance.delete_company_file(file_id)
    except Exception as e:
        print("Exception when calling CompanyFilesApi->delete_company_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The ID of the company file to delete. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The company file was deleted successfully. |  -  |
**403** | The API user does not have permission to delete the requested file. |  -  |
**404** | The requested file was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_file**
> get_company_file(file_id)

Get Company File

Downloads a company file by its ID. The response body is the raw file content. The `Content-Type` header reflects the file's MIME type and `Content-Disposition` is set to `attachment` with the original filename. Access is permitted if the file or its category is shared with employees, shared directly with the requesting user, or the user has view permission on the file section.

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
    file_id = 56 # int | The ID of the company file to download.

    try:
        # Get Company File
        api_instance.get_company_file(file_id)
    except Exception as e:
        print("Exception when calling CompanyFilesApi->get_company_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The ID of the company file to download. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The raw file content. The Content-Type header reflects the file&#39;s MIME type. |  -  |
**403** | The API user does not have permission to access this file. |  -  |
**404** | No file exists with the given ID. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_company_files**
> CompanyFilesResponse list_company_files()

Get Company Files and Categories

Returns all company file categories and the files within each category that the requesting user is permitted to see. The response format is determined by the `Accept` request header: send `application/json` for JSON or omit it (or send `application/xml`) for XML.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.company_files_response import CompanyFilesResponse
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
        api_response = api_instance.list_company_files()
        print("The response of CompanyFilesApi->list_company_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyFilesApi->list_company_files: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CompanyFilesResponse**](CompanyFilesResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of company file categories and their visible files. |  -  |
**403** | The API user does not have permission to access company files. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_company_file**
> update_company_file(file_id, company_file_update)

Update Company File

Updates metadata for an existing company file. Supports renaming the file, moving it to a different category, and toggling employee visibility. Accepts JSON or XML. Only fields included in the request body are updated.

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
    file_id = 56 # int | The ID of the company file to update.
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
 **file_id** | **int**| The ID of the company file to update. | 
 **company_file_update** | [**CompanyFileUpdate**](CompanyFileUpdate.md)|  | 

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
**200** | The company file was updated successfully. |  -  |
**400** | The request body contains malformed JSON or XML. |  -  |
**403** | The API user does not have permission to modify this file or its category. |  -  |
**404** | The file or the target category was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_company_file**
> upload_company_file(file_name, category, file, share=share)

Upload Company File

Uploads a file to a company file category. The request must be a `multipart/form-data` POST. On success, a `Location` header is returned with the URL of the newly created file resource. The file must be under 20MB and use a supported extension. Uploading to read-only categories is not permitted. Uploading to implementation categories is not permitted on companies that have completed implementation.

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
    file_name = 'file_name_example' # str | The display name for the uploaded file.
    category = 56 # int | The ID of the file category (section) to upload the file into.
    file = None # bytearray | The file to upload.
    share = 'share_example' # str | Whether to share the file with all employees. Accepted values: `yes` or `no`. Defaults to `no`. (optional)

    try:
        # Upload Company File
        api_instance.upload_company_file(file_name, category, file, share=share)
    except Exception as e:
        print("Exception when calling CompanyFilesApi->upload_company_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| The display name for the uploaded file. | 
 **category** | **int**| The ID of the file category (section) to upload the file into. | 
 **file** | **bytearray**| The file to upload. | 
 **share** | **str**| Whether to share the file with all employees. Accepted values: &#x60;yes&#x60; or &#x60;no&#x60;. Defaults to &#x60;no&#x60;. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The file was uploaded successfully. The &#x60;Location&#x60; header contains the URL of the new file resource. |  -  |
**400** | The request is invalid: missing file name, missing file, zero-byte file, or unsupported file extension. |  -  |
**403** | The API user does not have permission to upload files, or the target category is read-only. |  -  |
**404** | The specified category ID was not found. |  -  |
**413** | The file exceeds the 20MB limit or the company&#39;s storage limit. |  -  |
**503** | The file storage API is temporarily unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

