# bamboohr_sdk.CustomReportsApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_report_by_id**](CustomReportsApi.md#get_report_by_id) | **GET** /api/v1/custom-reports/{reportId} | Get Report by ID
[**list_reports**](CustomReportsApi.md#list_reports) | **GET** /api/v1/custom-reports | List Reports


# **get_report_by_id**
> EmployeeResponse get_report_by_id(report_id, page=page, page_size=page_size)

Get Report by ID

Executes a saved custom report and returns its data using the report's configured fields and filters. The `data` array contains employee record objects whose keys are determined by the fields selected when the report was created — each object is a flat key-value map where keys are field names (e.g. `firstName`, `status`, `hireDate`) and values are strings or `null`. The `aggregations` array is empty unless the report's underlying dataset configuration includes aggregation rules. Use "List Reports" to discover available report IDs.

Response shape: Each element of `data` is a flat key-value object — field values are top-level keys (e.g. `row["firstName"]`). This differs from `get-data-from-dataset-v2`, where field values are nested under a `fields` key (e.g. `row["fields"]["firstName"]`).

There is no schema-only response from this endpoint.

The `pagination.total_records` value is the number of rows produced by the saved report after applying the report's configured filters, not necessarily the total number of employees in the account. Validate output before using in automated pipelines.

Results default to page 1 with 500 records per page (maximum 1000). Out-of-range page numbers are clamped to the nearest valid page. Invalid or zero values for `page` and `page_size` fall back to their defaults.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.employee_response import EmployeeResponse
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
    api_instance = bamboohr_sdk.CustomReportsApi(api_client)
    report_id = 56 # int | The numeric ID of the saved custom report to execute.
    page = 1 # int | The page number to retrieve. Defaults to 1. (optional) (default to 1)
    page_size = 500 # int | The number of records per page. Defaults to 500. Maximum is 1000. (optional) (default to 500)

    try:
        # Get Report by ID
        api_response = api_instance.get_report_by_id(report_id, page=page, page_size=page_size)
        print("The response of CustomReportsApi->get_report_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomReportsApi->get_report_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **int**| The numeric ID of the saved custom report to execute. | 
 **page** | **int**| The page number to retrieve. Defaults to 1. | [optional] [default to 1]
 **page_size** | **int**| The number of records per page. Defaults to 500. Maximum is 1000. | [optional] [default to 500]

### Return type

[**EmployeeResponse**](EmployeeResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated report data with dynamic employee fields based on the report&#39;s configuration. |  -  |
**400** | Invalid or missing argument(s). Returned when the request fails validation or contains a type error. |  -  |
**403** | Access denied. The caller does not have permission to view this report. |  -  |
**404** | Report not found. No saved custom report exists with the given ID. |  -  |
**500** | An unexpected error occurred while retrieving the report. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_reports**
> ReportsResponse list_reports(page=page, page_size=page_size)

List Reports

Returns a paginated list of saved custom reports available in the account. Each report entry contains an `id` (integer) and a `name` (string). Pass a report's `id` to "Get Report by ID" to execute it and retrieve its data.

Results default to page 1 with 500 records per page (maximum 1000). Out-of-range page numbers are clamped to the nearest valid page rather than returning an error. Invalid or zero values for `page` and `page_size` fall back to their defaults.

The `pagination` object includes `total_records`, `current_page`, `total_pages`, and nullable `next_page`/`prev_page` links. When there is no next or previous page the corresponding value is `null`.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.reports_response import ReportsResponse
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
    api_instance = bamboohr_sdk.CustomReportsApi(api_client)
    page = 1 # int | The page number to retrieve. Out-of-range values are clamped to the nearest valid page. Defaults to 1. (optional) (default to 1)
    page_size = 500 # int | The number of records to retrieve per page. Defaults to 500. Maximum is 1000. (optional) (default to 500)

    try:
        # List Reports
        api_response = api_instance.list_reports(page=page, page_size=page_size)
        print("The response of CustomReportsApi->list_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomReportsApi->list_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number to retrieve. Out-of-range values are clamped to the nearest valid page. Defaults to 1. | [optional] [default to 1]
 **page_size** | **int**| The number of records to retrieve per page. Defaults to 500. Maximum is 1000. | [optional] [default to 500]

### Return type

[**ReportsResponse**](ReportsResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an object containing a &#x60;reports&#x60; array of report objects and a &#x60;pagination&#x60; object with page navigation metadata. |  -  |
**403** | The required feature toggle is not enabled for this account. |  -  |
**500** | An unexpected error occurred while retrieving the list of reports. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

