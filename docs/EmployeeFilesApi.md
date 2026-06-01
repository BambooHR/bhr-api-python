# bamboohr_sdk.EmployeeFilesApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_employee_file_category**](EmployeeFilesApi.md#create_employee_file_category) | **POST** /api/v1/employees/files/categories | Create Employee File Category
[**delete_employee_file**](EmployeeFilesApi.md#delete_employee_file) | **DELETE** /api/v1/employees/{id}/files/{fileId} | Delete Employee File
[**get_employee_file**](EmployeeFilesApi.md#get_employee_file) | **GET** /api/v1/employees/{id}/files/{fileId} | Get Employee File
[**list_employee_files**](EmployeeFilesApi.md#list_employee_files) | **GET** /api/v1/employees/{id}/files/view | List Employee Files
[**update_employee_file**](EmployeeFilesApi.md#update_employee_file) | **POST** /api/v1/employees/{id}/files/{fileId} | Update Employee File
[**upload_employee_file**](EmployeeFilesApi.md#upload_employee_file) | **POST** /api/v1/employees/{id}/files | Upload Employee File


# **create_employee_file_category**
> create_employee_file_category(request_body)

Create Employee File Category

Creates one or more employee file categories (not company file categories). The request body is a JSON array of category name strings or an equivalent XML document with `<category>` elements. Each name must be non-empty and unique among existing employee file categories. An empty array returns 200 without creating anything. On success, returns 201 with no body. The admin user group is automatically granted edit permission on each new category.

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
        api_instance.create_employee_file_category(request_body)
    except Exception as e:
        print("Exception when calling EmployeeFilesApi->create_employee_file_category: %s\n" % e)
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
**201** | All specified categories were created successfully. No response body is returned. |  -  |
**400** | The request body contains malformed JSON or XML, an empty category name, or a category name that already exists. |  -  |
**403** | The API user does not have permission to create employee file categories. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_employee_file**
> delete_employee_file(id, file_id)

Delete Employee File

Permanently deletes an employee file. This action cannot be undone and removes the file from storage. The special employee ID of 0 resolves to the employee associated with the API key. Returns 200 even if the file was already deleted (idempotent). Returns 403 if the caller lacks permission or the file belongs to a BambooPayroll-managed section. Returns 404 if the file does not exist for the specified employee or the Files tool is not enabled for the company. Use 'List Employee Files' to obtain file IDs.

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
    id = 56 # int | The ID of the employee whose file is being deleted. Use 0 to default to the employee associated with the API key.
    file_id = 56 # int | The ID of the employee file to delete.

    try:
        # Delete Employee File
        api_instance.delete_employee_file(id, file_id)
    except Exception as e:
        print("Exception when calling EmployeeFilesApi->delete_employee_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the employee whose file is being deleted. Use 0 to default to the employee associated with the API key. | 
 **file_id** | **int**| The ID of the employee file to delete. | 

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
**200** | The employee file was deleted successfully, or had already been deleted for this employee. |  -  |
**403** | The caller does not have permission to delete this employee&#39;s file, or the file belongs to a BambooPayroll-managed section and the caller is not a payroll admin. |  -  |
**404** | The file was not found for the specified employee, or the Files tool is not enabled for this company. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_file**
> bytearray get_employee_file(id, file_id)

Get Employee File

Downloads the binary content of an employee file as an attachment. The response Content-Type header reflects the file's stored MIME type (e.g. application/pdf) and includes a Content-Disposition header with the original filename. The special employee ID of 0 resolves to the employee associated with the API key.

Use "List Employee Files" to discover file IDs and their categories for a given employee. Archived or soft-deleted files are excluded and return 404.

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
    id = 56 # int | The ID of the employee whose file is being retrieved. Use 0 to resolve to the employee associated with the API key.
    file_id = 56 # int | The ID of the employee file to download.

    try:
        # Get Employee File
        api_response = api_instance.get_employee_file(id, file_id)
        print("The response of EmployeeFilesApi->get_employee_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeFilesApi->get_employee_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the employee whose file is being retrieved. Use 0 to resolve to the employee associated with the API key. | 
 **file_id** | **int**| The ID of the employee file to download. | 

### Return type

**bytearray**

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The employee file content streamed as a binary download. The Content-Type matches the file&#39;s stored MIME type and a Content-Disposition header provides the original filename. |  -  |
**403** | The API user does not have permission to access the requested employee or the file&#39;s section. |  -  |
**404** | The requested employee file was not found, or it has been archived or soft-deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_employee_files**
> JsonEmployeeFiles list_employee_files(id, accept=accept)

List Employee Files

Lists the file categories and files visible to the caller for the specified employee. This is a metadata listing (names, sizes, permissions); to download a file's content use `get-employee-file`. The response format is controlled by the Accept header: send `application/json` for JSON or omit/send anything else for XML. Only categories and files the caller is permitted to see are included; employees viewing their own profile also see files shared with them. Returns 404 when the employee has no accessible categories.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.json_employee_files import JsonEmployeeFiles
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
    id = 56 # int | The ID of the employee whose files are being listed.
    accept = 'application/xml' # str | Set to `application/json` to receive a JSON response. Any other value (or omitted) returns XML. (optional) (default to 'application/xml')

    try:
        # List Employee Files
        api_response = api_instance.list_employee_files(id, accept=accept)
        print("The response of EmployeeFilesApi->list_employee_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeFilesApi->list_employee_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the employee whose files are being listed. | 
 **accept** | **str**| Set to &#x60;application/json&#x60; to receive a JSON response. Any other value (or omitted) returns XML. | [optional] [default to &#39;application/xml&#39;]

### Return type

[**JsonEmployeeFiles**](JsonEmployeeFiles.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The employee&#39;s file categories and files. Each category contains permission flags and an array of file metadata. |  -  |
**403** | The API user does not have permission to access the requested employee&#39;s files. |  -  |
**404** | The requested employee was not found, or the employee has no accessible file categories. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_employee_file**
> update_employee_file(id, file_id, employee_file_update)

Update Employee File

Updates metadata for an existing employee file. Supports renaming the file, moving it to a different category, and toggling employee visibility. Accepts JSON or XML; only fields present in the request body are updated. An empty XML document no-ops successfully, while an empty JSON body returns 400. The `categoryId` field is silently ignored when the caller authenticated as the file creator but lacks full file permissions. Moving a file to a new category requires view/edit access to both the current and target category. Returns 403 if the file belongs to a read-only file section. Use 'List Employee Files' to obtain file IDs and category IDs.

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
    id = 56 # int | The ID of the employee whose file is being updated.
    file_id = 56 # int | The ID of the employee file to update.
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
 **id** | **int**| The ID of the employee whose file is being updated. | 
 **file_id** | **int**| The ID of the employee file to update. | 
 **employee_file_update** | [**EmployeeFileUpdate**](EmployeeFileUpdate.md)|  | 

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
**200** | The employee file metadata was updated successfully. No response body is returned. |  -  |
**400** | The request body contains malformed JSON or XML. |  -  |
**403** | The API user does not have permission to modify the requested employee&#39;s file, its category, or the file belongs to a read-only section. |  -  |
**404** | The requested employee file or target category was not found. |  -  |
**500** | An internal server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_employee_file**
> upload_employee_file(id, file_name, category, file, share=share)

Upload Employee File

Uploads a file to an employee's file section. The request must be a `multipart/form-data` POST. On success, a `Location` header is returned with the URL of the newly created file resource. The file must be under 20MB and use a supported extension. Pass `0` as the employee ID to use the employee associated with the API key. Employees may upload to their own folder if the company has employee document uploads enabled.

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
    file_name = 'file_name_example' # str | The display name for the uploaded file.
    category = 56 # int | The ID of the employee file section to upload the file into.
    file = None # bytearray | The file to upload.
    share = 'share_example' # str | Whether to share the file with the employee. Accepted values: `yes` or `no`. Defaults to `no`. (optional)

    try:
        # Upload Employee File
        api_instance.upload_employee_file(id, file_name, category, file, share=share)
    except Exception as e:
        print("Exception when calling EmployeeFilesApi->upload_employee_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| {id} is an employee ID. The special employee ID of zero (0) means to use the employee ID associated with the API key (if any). | [default to &#39;0&#39;]
 **file_name** | **str**| The display name for the uploaded file. | 
 **category** | **int**| The ID of the employee file section to upload the file into. | 
 **file** | **bytearray**| The file to upload. | 
 **share** | **str**| Whether to share the file with the employee. Accepted values: &#x60;yes&#x60; or &#x60;no&#x60;. Defaults to &#x60;no&#x60;. | [optional] 

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
**403** | The API user does not have permission to access the requested employee or their file section. |  -  |
**404** | The employee or the specified file category was not found. |  -  |
**413** | The file exceeds the 20MB limit or the company&#39;s storage limit. |  -  |
**503** | The file storage API is temporarily unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

