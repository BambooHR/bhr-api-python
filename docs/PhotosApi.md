# bamboohr_sdk.PhotosApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_employee_photo**](PhotosApi.md#get_employee_photo) | **GET** /api/v1/employees/{employeeId}/photo/{size} | Get Employee Photo
[**upload_employee_photo**](PhotosApi.md#upload_employee_photo) | **POST** /api/v1/employees/{employeeId}/photo | Upload Employee Photo


# **get_employee_photo**
> get_employee_photo(employee_id, size, width=width, height=height)

Get Employee Photo

Returns an employee photo at the requested size. Available sizes are: `original` (full resolution), `large` (340×340), `medium` (170×170), `small` (150×150), `xs` (50×50), and `tiny` (20×20). The response shape is selected via standard HTTP content negotiation: by default the body is the stored image bytes and the `Content-Type` response header matches the body (`image/jpeg`, `image/png`, `image/bmp`, `image/gif`, or `image/tiff`). When the caller sends `Accept: application/json` (typical MCP/LLM-connector usage), the body is a JSON object `{ mimeType, fileBase64 }` with the same image bytes base64-encoded, and the response `Content-Type` is `application/json`.

A 404 response covers three distinct cases: (1) the employee exists but has no photo on file (a normal, non-error state), (2) the employee ID does not exist, or (3) the size value is not one of the recognized options. The `x-bamboohr-error-message` response header distinguishes them: `Employee photo not found`, `Employee not found`, or `Size: "<value>" is not a valid size option. Valid sizes are: xs, small, tiny, original, medium and large.`. Treat "Employee photo not found" as a normal "no photo on file" result rather than as a bad employee ID, permission failure, or other error to debug.

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
 - **Accept**: image/*, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Employee photo, returned in one of two shapes via standard HTTP content negotiation: binary &#x60;image/*&#x60; bytes by default (matching the stored format), or &#x60;application/json&#x60; with &#x60;{ mimeType, fileBase64 }&#x60; when the caller sends &#x60;Accept: application/json&#x60;. |  -  |
**403** | The authenticated user does not have permission to view this employee&#39;s photo. |  -  |
**404** | Returned in three distinct cases: the employee does not exist, the employee has no photo on file, or the requested size is not a recognized value. The &#x60;x-bamboohr-error-message&#x60; response header reports which case applies (&#x60;Employee not found&#x60;, &#x60;Employee photo not found&#x60;, or &#x60;Size: \&quot;&lt;value&gt;\&quot; is not a valid size option. Valid sizes are: xs, small, tiny, original, medium and large.&#x60;). \&quot;Employee photo not found\&quot; is the expected response for an employee who simply has not uploaded a photo and should not be treated as an error to debug. |  * x-bamboohr-error-message - Human-readable error message describing why the request failed (e.g. &#39;Invalid status&#39;). <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_employee_photo**
> upload_employee_photo(employee_id, file)

Upload Employee Photo

Uploads a new photo for an employee. Accepts either a `multipart/form-data` POST with a `file` field carrying raw binary image bytes (typical browser/SDK usage), or an `application/json` POST with a `fileBase64` property carrying the base64-encoded image bytes (typical MCP/LLM-connector usage). The server selects the path based on the request `Content-Type`. Supported formats: JPEG, PNG, BMP, GIF. Other formats (HEIC, SVG, AVIF, WebP) are rejected with 415; TIFF is accepted by the format gate but some variants may fail downstream. The image must be square (width and height must match within one pixel) and at least 150×150 pixels. Maximum file size is 20MB (applies to the decoded bytes for the JSON variant). The photo replaces the employee's current photo for all size variants. Employees may upload their own photo if the company has self-photo uploads enabled.

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
    file = None # bytearray | The image file to upload as the employee's photo. Supported formats: JPEG, PNG, BMP, GIF (HEIC, SVG, AVIF, and WebP are rejected with 415; TIFF is accepted by the format gate but some variants may fail downstream). Must be square (width and height within 1 pixel), at least 150×150 pixels, and no larger than 20MB.

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
 **file** | **bytearray**| The image file to upload as the employee&#39;s photo. Supported formats: JPEG, PNG, BMP, GIF (HEIC, SVG, AVIF, and WebP are rejected with 415; TIFF is accepted by the format gate but some variants may fail downstream). Must be square (width and height within 1 pixel), at least 150×150 pixels, and no larger than 20MB. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The photo was uploaded and processed successfully. No response body is returned. |  -  |
**400** | The request is invalid: no file provided, zero-byte file, or the maximum number of photo uploads (32767) has been exceeded. |  -  |
**402** | The photo could not be processed: the image crop failed, or the file contents could not be read. |  -  |
**403** | The authenticated user does not have permission to upload photos for this employee. |  -  |
**404** | The employee does not exist. |  -  |
**413** | The uploaded file exceeds the 20MB size limit. |  -  |
**415** | The image does not meet requirements: not square (width and height differ by more than one pixel), smaller than 150×150 pixels, or the file could not be read as a supported image format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

