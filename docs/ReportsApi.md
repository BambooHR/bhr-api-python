# bamboohr_sdk.ReportsApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_company_report**](ReportsApi.md#get_company_report) | **GET** /api/v1/reports/{id} | Get Company Report
[**request_custom_report**](ReportsApi.md#request_custom_report) | **POST** /api/v1/reports/custom | Request Custom Report


# **get_company_report**
> get_company_report(id, format, accept_header_parameter=accept_header_parameter, fd=fd, only_current=only_current)

Get Company Report

**Warning: This endpoint will soon be deprecated and replaced with Custom Reports - Get Report by ID.** 

Use this resource to request one of your existing custom company reports from the My Reports or Manage Reports sections in the Reports tab. You can get the report number by hovering over the report name and noting the ID from the URL. At present, only reports from the My Reports or Manage Reports sections are supported. In the future we may implement reports from the Standard Reports section if there is enough demand for it. The report numbers used in this request are different in each company.


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
    api_instance = bamboohr_sdk.ReportsApi(api_client)
    id = 'id_example' # str | {id} is a report ID.
    format = 'format_example' # str | The output format for the report. Supported formats: CSV, PDF, XLS, XML, JSON
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)
    fd = 'fd_example' # str | yes=apply standard duplicate field filtering, no=return the raw results with no duplicate filtering. Default value is \"yes\" (optional)
    only_current = False # bool | Setting to false will return future dated values from history table fields. (optional) (default to False)

    try:
        # Get Company Report
        api_instance.get_company_report(id, format, accept_header_parameter=accept_header_parameter, fd=fd, only_current=only_current)
    except Exception as e:
        print("Exception when calling ReportsApi->get_company_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| {id} is a report ID. | 
 **format** | **str**| The output format for the report. Supported formats: CSV, PDF, XLS, XML, JSON | 
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 
 **fd** | **str**| yes&#x3D;apply standard duplicate field filtering, no&#x3D;return the raw results with no duplicate filtering. Default value is \&quot;yes\&quot; | [optional] 
 **only_current** | **bool**| Setting to false will return future dated values from history table fields. | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All fields available in BambooHR. |  -  |
**404** | if you request a nonexistent report number. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_custom_report**
> request_custom_report(format, request_custom_report, only_current=only_current)

Request Custom Report

**Warning: This endpoint will soon be deprecated and replaced with Datasets - Get Data from Dataset.** 

Use this resource to request BambooHR generate a report. You must specify a type of either "PDF", "XLS", "CSV", "JSON", or "XML". You must specify a list of fields to show on the report. The list of fields is available here. The custom report will return employees regardless of their status, "Active" or "Inactive". This differs from the UI, which by default applies a quick filter to display only "Active" employees.


### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.request_custom_report import RequestCustomReport
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
    format = 'format_example' # str | The output format for the report. Supported formats: CSV, PDF, XLS, XML, JSON
    request_custom_report = bamboohr_sdk.RequestCustomReport() # RequestCustomReport | 
    only_current = False # bool | Limits the report to only current employees. Setting to false will include future-dated employees in the report. (optional) (default to False)

    try:
        # Request Custom Report
        api_instance.request_custom_report(format, request_custom_report, only_current=only_current)
    except Exception as e:
        print("Exception when calling ReportsApi->request_custom_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| The output format for the report. Supported formats: CSV, PDF, XLS, XML, JSON | 
 **request_custom_report** | [**RequestCustomReport**](RequestCustomReport.md)|  | 
 **only_current** | **bool**| Limits the report to only current employees. Setting to false will include future-dated employees in the report. | [optional] [default to False]

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
**200** | Custom report successfully requested |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

