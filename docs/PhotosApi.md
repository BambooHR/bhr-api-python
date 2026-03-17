# bamboohr_sdk.PhotosApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_employee_photo**](PhotosApi.md#get_employee_photo) | **GET** /api/v1/employees/{employeeId}/photo/{size} | Get Employee Photo
[**upload_employee_photo**](PhotosApi.md#upload_employee_photo) | **POST** /api/v1/employees/{employeeId}/photo | Upload Employee Photo


# **get_employee_photo**
> get_employee_photo(employee_id, size, width=width, height=height)

Get Employee Photo

Returns an employee photo at the requested size. Available sizes are: `original` (full resolution), `large` (340×340), `medium` (170×170), `small` (150×150), `xs` (50×50), and `tiny` (20×20). The server always sets `Content-Type: image/jpeg`, but the underlying byte payload may reflect the original upload format.

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
    employee_id = 56 # int | The ID of the employee whose photo to retrieve.
    size = 'size_example' # str | The desired photo size. One of: `original`, `large`, `medium`, `small`, `xs`, `tiny`.
    width = 56 # int | Optional. Scales the returned image to the specified pixel width, capped at the natural width of the requested size. Only applies to `small` and `tiny` sizes. (optional)
    height = 56 # int | Optional. Scales the returned image to the specified pixel height, capped at the natural height of the requested size. Only applies to `small` and `tiny` sizes. (optional)

    try:
        # Get Employee Photo
        api_instance.get_employee_photo(employee_id, size, width=width, height=height)
    except Exception as e:
        print("Exception when calling PhotosApi->get_employee_photo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| The ID of the employee whose photo to retrieve. | 
 **size** | **str**| The desired photo size. One of: &#x60;original&#x60;, &#x60;large&#x60;, &#x60;medium&#x60;, &#x60;small&#x60;, &#x60;xs&#x60;, &#x60;tiny&#x60;. | 
 **width** | **int**| Optional. Scales the returned image to the specified pixel width, capped at the natural width of the requested size. Only applies to &#x60;small&#x60; and &#x60;tiny&#x60; sizes. | [optional] 
 **height** | **int**| Optional. Scales the returned image to the specified pixel height, capped at the natural height of the requested size. Only applies to &#x60;small&#x60; and &#x60;tiny&#x60; sizes. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image bytes returned with Content-Type: image/jpeg. The payload may reflect the original upload format and is not guaranteed to be JPEG-encoded. |  -  |
**403** | The API user does not have permission to view this employee&#39;s photo. |  -  |
**404** | The employee does not exist, no photo is on file, or an unrecognized size was specified. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_employee_photo**
> upload_employee_photo(employee_id, file)

Upload Employee Photo

Uploads a new photo for an employee. The request must be a `multipart/form-data` POST with a `file` field. Confirmed supported formats: JPEG, PNG, BMP. Other formats (e.g. HEIC, SVG, AVIF, TIFF) are not reliably supported and may return 415, 500, or 502. The image must be square (width and height must match within one pixel) and at least 150×150 pixels. Maximum file size is 20MB. The photo replaces the employee's current photo for all size variants. Employees may upload their own photo if the company has self-photo uploads enabled.

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
    employee_id = 56 # int | The ID of the employee whose photo is being uploaded.
    file = None # bytearray | The image file to upload as the employee's photo.

    try:
        # Upload Employee Photo
        api_instance.upload_employee_photo(employee_id, file)
    except Exception as e:
        print("Exception when calling PhotosApi->upload_employee_photo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| The ID of the employee whose photo is being uploaded. | 
 **file** | **bytearray**| The image file to upload as the employee&#39;s photo. | 

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
**201** | The photo was uploaded and processed successfully. |  -  |
**400** | The request is invalid: no file provided, zero-byte file, or the maximum number of photo uploads (32767) has been exceeded. |  -  |
**403** | The API user does not have permission to upload photos for this employee. |  -  |
**404** | The employee does not exist. |  -  |
**413** | The uploaded file exceeds the 20MB size limit. |  -  |
**415** | The image does not meet requirements: not square (width and height differ by more than one pixel), smaller than 150×150 pixels, or the file could not be read as a supported image format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

