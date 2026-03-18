# bamboohr_sdk.ReportsApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_company_report**](ReportsApi.md#get_company_report) | **GET** /api/v1/reports/{id} | Get Company Report
[**request_custom_report**](ReportsApi.md#request_custom_report) | **POST** /api/v1/reports/custom | Request Custom Report


# **get_company_report**
> GetCompanyReportResponse get_company_report(id, accept_header_parameter=accept_header_parameter, format=format, fd=fd, only_current=only_current)

Get Company Report

**Warning: This endpoint will soon be deprecated and replaced with Custom Reports - Get Report by ID.**

Returns the data from an existing saved custom report. Non-admins can find these reports in My Reports. Admins can find them in Custom Reports under the My Reports and Company Reports tabs. The report ID can be found by hovering over the report name in BambooHR and noting the ID in the URL. Standard Reports are not available via this endpoint, and report IDs are company-specific.

The caller must have permission to view or access the report. The `format` query parameter is case-insensitive (`json`, `JSON`, `Json` are all accepted). If `format` is omitted, the output format is inferred from the `Accept` header, but only these exact values are supported: `application/json`, `text/xml`, `text/csv`, `application/pdf`, `application/vnd.ms-excel`. Any other `Accept` value (including `application/xml` and `*/*`) returns 404.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.get_company_report_response import GetCompanyReportResponse
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
    api_instance = bamboohr_sdk.ReportsApi(api_client)
    id = 56 # int | The integer ID of the saved custom report to run. Find this ID by hovering over the report name in the BambooHR Reports tab and noting the ID in the URL.
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)
    format = 'format_example' # str | The output format for the report. Case-insensitive. If omitted, format is inferred from the `Accept` header — only `application/json`, `text/xml`, `text/csv`, `application/pdf`, and `application/vnd.ms-excel` are accepted; any other value returns 404. (optional)
    fd = 'fd_example' # str | Controls duplicate row filtering. `yes` applies standard deduplication (default for JSON and XML formats). `no` returns raw results without filtering (default for CSV and XLS formats). (optional)
    only_current = True # bool | Whether to restrict results to current (non-future-dated) field values. Set to false to include future-dated history field values. Defaults to true. (optional) (default to True)

    try:
        # Get Company Report
        api_response = api_instance.get_company_report(id, accept_header_parameter=accept_header_parameter, format=format, fd=fd, only_current=only_current)
        print("The response of ReportsApi->get_company_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_company_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The integer ID of the saved custom report to run. Find this ID by hovering over the report name in the BambooHR Reports tab and noting the ID in the URL. | 
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 
 **format** | **str**| The output format for the report. Case-insensitive. If omitted, format is inferred from the &#x60;Accept&#x60; header — only &#x60;application/json&#x60;, &#x60;text/xml&#x60;, &#x60;text/csv&#x60;, &#x60;application/pdf&#x60;, and &#x60;application/vnd.ms-excel&#x60; are accepted; any other value returns 404. | [optional] 
 **fd** | **str**| Controls duplicate row filtering. &#x60;yes&#x60; applies standard deduplication (default for JSON and XML formats). &#x60;no&#x60; returns raw results without filtering (default for CSV and XLS formats). | [optional] 
 **only_current** | **bool**| Whether to restrict results to current (non-future-dated) field values. Set to false to include future-dated history field values. Defaults to true. | [optional] [default to True]

### Return type

[**GetCompanyReportResponse**](GetCompanyReportResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml, text/csv, application/pdf, application/vnd.ms-excel

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report data in the requested format. For JSON, returns an object with a &#x60;title&#x60; string, a &#x60;fields&#x60; array (each element has &#x60;id&#x60;, &#x60;type&#x60;, and &#x60;name&#x60;), and an &#x60;employees&#x60; array (each element has &#x60;id&#x60; plus one key per report field). For XML (&#x60;text/xml&#x60;), returns a &#x60;&lt;report&gt;&#x60; document. For CSV/XLS/PDF, returns file content with the appropriate content-type header. |  -  |
**403** | Access denied. The authenticated user does not have permission to view this report. |  -  |
**404** | Not found. Returned when the report ID does not exist or belongs to a different company, when an unsupported &#x60;format&#x60; value is supplied (e.g. &#x60;?format&#x3D;bogus&#x60;), or when &#x60;format&#x60; is omitted and the &#x60;Accept&#x60; header is not one of the supported exact values (&#x60;application/json&#x60;, &#x60;text/xml&#x60;, &#x60;text/csv&#x60;, &#x60;application/pdf&#x60;, &#x60;application/vnd.ms-excel&#x60;). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_custom_report**
> RequestCustomReportResponse request_custom_report(request_custom_report, format=format, only_current=only_current)

Request Custom Report

**Warning: This endpoint will soon be deprecated and replaced with Datasets - Get Data from Dataset.**

Generates an ad-hoc employee report based on a caller-specified list of fields and optional filters. Returns report data in the requested format (JSON, XML, CSV, XLS, or PDF). The report includes all employees regardless of status (both Active and Inactive), unlike the BambooHR UI which filters to Active employees by default.

The request body may be submitted as JSON or XML. To submit JSON, set `Content-Type: application/json` exactly — any variation such as `application/json; charset=UTF-8` is not recognised as JSON and the body will be parsed as XML instead, which typically results in `400 Malformed XML`. To submit XML, set `Content-Type` to any other value; the body must be a `<report>` document as described in the XML request body schema.

The `format` query parameter is case-insensitive (`json`, `JSON`, `Json` are all accepted). If `format` is omitted, the output format is inferred from the `Accept` header, but only these exact values are supported: `application/json`, `text/xml`, `text/csv`, `application/pdf`, `application/vnd.ms-excel`. Any other `Accept` value (including `application/xml` and `*/*`) will return 404.

Field IDs in the request that are unknown or that the caller does not have permission to view are silently omitted from the report — the endpoint still returns 200. The `filters` object supports `lastChanged` (ISO 8601 date-time to filter by last-modified date) and `employeeIds` (restrict results to specific employee IDs). The maximum number of fields per request is 400.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.request_custom_report import RequestCustomReport
from bamboohr_sdk.models.request_custom_report_response import RequestCustomReportResponse
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
    api_instance = bamboohr_sdk.ReportsApi(api_client)
    request_custom_report = bamboohr_sdk.RequestCustomReport() # RequestCustomReport | 
    format = 'format_example' # str | The output format for the report. Case-insensitive. If omitted, format is inferred from the `Accept` header — only `application/json`, `text/xml`, `text/csv`, `application/pdf`, and `application/vnd.ms-excel` are accepted; any other value returns 404. (optional)
    only_current = True # bool | Limits the report to only current employees. Set to false to include future-dated employees. Defaults to true. (optional) (default to True)

    try:
        # Request Custom Report
        api_response = api_instance.request_custom_report(request_custom_report, format=format, only_current=only_current)
        print("The response of ReportsApi->request_custom_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->request_custom_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_custom_report** | [**RequestCustomReport**](RequestCustomReport.md)|  | 
 **format** | **str**| The output format for the report. Case-insensitive. If omitted, format is inferred from the &#x60;Accept&#x60; header — only &#x60;application/json&#x60;, &#x60;text/xml&#x60;, &#x60;text/csv&#x60;, &#x60;application/pdf&#x60;, and &#x60;application/vnd.ms-excel&#x60; are accepted; any other value returns 404. | [optional] 
 **only_current** | **bool**| Limits the report to only current employees. Set to false to include future-dated employees. Defaults to true. | [optional] [default to True]

### Return type

[**RequestCustomReportResponse**](RequestCustomReportResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, text/xml, text/csv, application/pdf, application/vnd.ms-excel

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report data in the requested format. For JSON, returns an object with a &#x60;title&#x60; string, a &#x60;fields&#x60; array (each with &#x60;id&#x60;, &#x60;type&#x60;, and &#x60;name&#x60;), and an &#x60;employees&#x60; array (each with &#x60;id&#x60; and one key per requested field). For XML, returns a &#x60;&lt;report&gt;&#x60; document. For CSV/XLS/PDF, returns the file content with the appropriate content-type header. |  -  |
**400** | Bad request. Returned when the request body is malformed JSON or XML, or when more than 400 fields are requested. Unknown or inaccessible field IDs are silently omitted and do not cause a 400. |  -  |
**404** | Report format not found. Returned when an unsupported &#x60;format&#x60; value is supplied (e.g. &#x60;?format&#x3D;bogus&#x60;), or when &#x60;format&#x60; is omitted and the &#x60;Accept&#x60; header is not one of the supported exact values (&#x60;application/json&#x60;, &#x60;text/xml&#x60;, &#x60;text/csv&#x60;, &#x60;application/pdf&#x60;, &#x60;application/vnd.ms-excel&#x60;). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

