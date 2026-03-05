# bamboohr_sdk.CustomReportsApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_by_report_id**](CustomReportsApi.md#get_by_report_id) | **GET** /api/v1/custom-reports/{reportId} | Get Report by ID
[**list_reports**](CustomReportsApi.md#list_reports) | **GET** /api/v1/custom-reports | Get Reports


# **get_by_report_id**
> EmployeeResponse get_by_report_id(report_id)

Get Report by ID

Use this resource to retrieve data for a specific report.

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
    report_id = 56 # int | 

    try:
        # Get Report by ID
        api_response = api_instance.get_by_report_id(report_id)
        print("The response of CustomReportsApi->get_by_report_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomReportsApi->get_by_report_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **int**|  | 

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
**200** | Report details |  -  |
**400** | Invalid or missing argument(s) |  -  |
**403** | Access denied |  -  |
**404** | Report not found |  -  |
**500** | An unexpected error occurred while getting a report |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_reports**
> ReportsResponse list_reports(page=page, page_size=page_size)

Get Reports

Use this resource to retrieve a list of available reports.

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
    page = 56 # int | The page number to retrieve (optional)
    page_size = 56 # int | The number of records to retrieve per page. Default is 500 and the Max is 1000 (optional)

    try:
        # Get Reports
        api_response = api_instance.list_reports(page=page, page_size=page_size)
        print("The response of CustomReportsApi->list_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomReportsApi->list_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number to retrieve | [optional] 
 **page_size** | **int**| The number of records to retrieve per page. Default is 500 and the Max is 1000 | [optional] 

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
**200** | A list of reports |  -  |
**403** | Access denied |  -  |
**500** | An unexpected error occurred while getting the list of reports |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

