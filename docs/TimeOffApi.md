# bamboohr_sdk.TimeOffApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_a_list_of_who_is_out**](TimeOffApi.md#get_a_list_of_who_is_out) | **GET** /api/v1/time_off/whos_out | Get Who’s Out
[**get_time_off_policies**](TimeOffApi.md#get_time_off_policies) | **GET** /api/v1/meta/time_off/policies | Get Time Off Policies
[**get_time_off_types**](TimeOffApi.md#get_time_off_types) | **GET** /api/v1/meta/time_off/types | Get Time Off Types
[**time_off_add_a_time_off_history_item_for_time_off_request**](TimeOffApi.md#time_off_add_a_time_off_history_item_for_time_off_request) | **PUT** /api/v1/employees/{employeeId}/time_off/history | Create Time Off Request History Item
[**time_off_add_a_time_off_request**](TimeOffApi.md#time_off_add_a_time_off_request) | **PUT** /api/v1/employees/{employeeId}/time_off/request | Create Time Off Request
[**time_off_adjust_time_off_balance**](TimeOffApi.md#time_off_adjust_time_off_balance) | **PUT** /api/v1/employees/{employeeId}/time_off/balance_adjustment | Update Time Off Balance
[**time_off_assign_time_off_policies_for_an_employee**](TimeOffApi.md#time_off_assign_time_off_policies_for_an_employee) | **PUT** /api/v1/employees/{employeeId}/time_off/policies | Assign Time Off Policies
[**time_off_assign_time_off_policies_for_an_employee_v1_1**](TimeOffApi.md#time_off_assign_time_off_policies_for_an_employee_v1_1) | **PUT** /api/v1_1/employees/{employeeId}/time_off/policies | Assign Time Off Policies v1.1
[**time_off_change_a_request_status**](TimeOffApi.md#time_off_change_a_request_status) | **PUT** /api/v1/time_off/requests/{requestId}/status | Update Time Off Request Status
[**time_off_get_time_off_balance**](TimeOffApi.md#time_off_get_time_off_balance) | **GET** /api/v1/employees/{employeeId}/time_off/calculator | Get Time Off Balance
[**time_off_get_time_off_requests**](TimeOffApi.md#time_off_get_time_off_requests) | **GET** /api/v1/time_off/requests | Get Time Off Requests
[**time_off_list_time_off_policies_for_employee**](TimeOffApi.md#time_off_list_time_off_policies_for_employee) | **GET** /api/v1/employees/{employeeId}/time_off/policies | Get Time Off Policies for Employee
[**time_off_list_time_off_policies_for_employee_v1_1**](TimeOffApi.md#time_off_list_time_off_policies_for_employee_v1_1) | **GET** /api/v1_1/employees/{employeeId}/time_off/policies | Get Time Off Policies for Employee v1.1


# **get_a_list_of_who_is_out**
> get_a_list_of_who_is_out(accept_header_parameter=accept_header_parameter, start=start, end=end)

Get Who’s Out

This endpoint will return a list, sorted by date, of employees who will be out, and company holidays, for a period of time.

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
    api_instance = bamboohr_sdk.TimeOffApi(api_client)
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)
    start = 'start_example' # str | A date in the form YYYY-MM-DD - defaults to the current date. (optional)
    end = 'end_example' # str | A date in the form YYYY-MM-DD - defaults to 14 days from the start date. (optional)

    try:
        # Get Who’s Out
        api_instance.get_a_list_of_who_is_out(accept_header_parameter=accept_header_parameter, start=start, end=end)
    except Exception as e:
        print("Exception when calling TimeOffApi->get_a_list_of_who_is_out: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 
 **start** | **str**| A date in the form YYYY-MM-DD - defaults to the current date. | [optional] 
 **end** | **str**| A date in the form YYYY-MM-DD - defaults to 14 days from the start date. | [optional] 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_off_policies**
> get_time_off_policies(accept_header_parameter=accept_header_parameter)

Get Time Off Policies

This endpoint gets a list of time off policies.

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
    api_instance = bamboohr_sdk.TimeOffApi(api_client)
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)

    try:
        # Get Time Off Policies
        api_instance.get_time_off_policies(accept_header_parameter=accept_header_parameter)
    except Exception as e:
        print("Exception when calling TimeOffApi->get_time_off_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_off_types**
> TimeOffTypesAndDefaultHours get_time_off_types(accept_header_parameter=accept_header_parameter, mode=mode)

Get Time Off Types

This endpoint gets a list of time off types.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_off_types_and_default_hours import TimeOffTypesAndDefaultHours
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
    api_instance = bamboohr_sdk.TimeOffApi(api_client)
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)
    mode = 'mode_example' # str | Set to 'request' to filter down to time off types that the user has permission to request (optional)

    try:
        # Get Time Off Types
        api_response = api_instance.get_time_off_types(accept_header_parameter=accept_header_parameter, mode=mode)
        print("The response of TimeOffApi->get_time_off_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeOffApi->get_time_off_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 
 **mode** | **str**| Set to &#39;request&#39; to filter down to time off types that the user has permission to request | [optional] 

### Return type

[**TimeOffTypesAndDefaultHours**](TimeOffTypesAndDefaultHours.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Time off types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_off_add_a_time_off_history_item_for_time_off_request**
> time_off_add_a_time_off_history_item_for_time_off_request(employee_id, time_off_history)

Create Time Off Request History Item

To use this API make an HTTP PUT where the body of the request is the JSON documented below. A new time off history item will be inserted into the database. On success, a 201 Created code is returned and the "Location" header of the response will contain a URL that identifies the new history item.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_off_history import TimeOffHistory
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
    api_instance = bamboohr_sdk.TimeOffApi(api_client)
    employee_id = 56 # int | The ID of the employee.
    time_off_history = bamboohr_sdk.TimeOffHistory() # TimeOffHistory | 

    try:
        # Create Time Off Request History Item
        api_instance.time_off_add_a_time_off_history_item_for_time_off_request(employee_id, time_off_history)
    except Exception as e:
        print("Exception when calling TimeOffApi->time_off_add_a_time_off_history_item_for_time_off_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| The ID of the employee. | 
 **time_off_history** | [**TimeOffHistory**](TimeOffHistory.md)|  | 

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
**201** | The history item has been created. |  -  |
**400** | For empty or malformed JSON, an invalid date format, or an invalid time off request. |  -  |
**403** | Invalid permissions to perform this action. |  -  |
**409** | If the time off request already has a history item. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_off_add_a_time_off_request**
> time_off_add_a_time_off_request(employee_id, time_off_request)

Create Time Off Request

A time off request is an entity that describes the decision making process for approving time off. Once a request has been created, a history entry can be created documenting the actual use of time off.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_off_request import TimeOffRequest
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
    api_instance = bamboohr_sdk.TimeOffApi(api_client)
    employee_id = 'employee_id_example' # str | 
    time_off_request = bamboohr_sdk.TimeOffRequest() # TimeOffRequest | 

    try:
        # Create Time Off Request
        api_instance.time_off_add_a_time_off_request(employee_id, time_off_request)
    except Exception as e:
        print("Exception when calling TimeOffApi->time_off_add_a_time_off_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**|  | 
 **time_off_request** | [**TimeOffRequest**](TimeOffRequest.md)|  | 

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
**201** | Request created. |  -  |
**400** | Malformed request. |  -  |
**403** | Forbidden. Cannot change past approved requests. |  -  |
**404** | Employee not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_off_adjust_time_off_balance**
> time_off_adjust_time_off_balance(employee_id, adjust_time_off_balance)

Update Time Off Balance

To use this API make an HTTP PUT where the body of the request is the JSON documented below. A time off balance adjustment will be inserted into the database. On success, a 201 Created code is returned and the "Location" header of the response will contain a URL that identifies the new history item.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.adjust_time_off_balance import AdjustTimeOffBalance
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
    api_instance = bamboohr_sdk.TimeOffApi(api_client)
    employee_id = 56 # int | The ID of the employee.
    adjust_time_off_balance = bamboohr_sdk.AdjustTimeOffBalance() # AdjustTimeOffBalance | 

    try:
        # Update Time Off Balance
        api_instance.time_off_adjust_time_off_balance(employee_id, adjust_time_off_balance)
    except Exception as e:
        print("Exception when calling TimeOffApi->time_off_adjust_time_off_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| The ID of the employee. | 
 **adjust_time_off_balance** | [**AdjustTimeOffBalance**](AdjustTimeOffBalance.md)|  | 

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
**201** | The balance adjustment has been created. |  -  |
**400** | For empty or malformed JSON, an invalid date format, or an invalid time off type. |  -  |
**403** | Invalid permissions to perform this action. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_off_assign_time_off_policies_for_an_employee**
> time_off_assign_time_off_policies_for_an_employee(employee_id, time_off_assign_time_off_policies_for_an_employee_request_inner)

Assign Time Off Policies

To use this API make an HTTP PUT where the body of the request is the JSON documented below. A time off policy will be assigned to the employee with accruals starting on the date specified. A null start date will remove the assignment. On success, a 200 Success code is returned and the content of the response will be the same as the List Time off Policies API.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_off_assign_time_off_policies_for_an_employee_request_inner import TimeOffAssignTimeOffPoliciesForAnEmployeeRequestInner
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
    api_instance = bamboohr_sdk.TimeOffApi(api_client)
    employee_id = 'employee_id_example' # str | 
    time_off_assign_time_off_policies_for_an_employee_request_inner = [bamboohr_sdk.TimeOffAssignTimeOffPoliciesForAnEmployeeRequestInner()] # List[TimeOffAssignTimeOffPoliciesForAnEmployeeRequestInner] | 

    try:
        # Assign Time Off Policies
        api_instance.time_off_assign_time_off_policies_for_an_employee(employee_id, time_off_assign_time_off_policies_for_an_employee_request_inner)
    except Exception as e:
        print("Exception when calling TimeOffApi->time_off_assign_time_off_policies_for_an_employee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**|  | 
 **time_off_assign_time_off_policies_for_an_employee_request_inner** | [**List[TimeOffAssignTimeOffPoliciesForAnEmployeeRequestInner]**](TimeOffAssignTimeOffPoliciesForAnEmployeeRequestInner.md)|  | 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_off_assign_time_off_policies_for_an_employee_v1_1**
> time_off_assign_time_off_policies_for_an_employee_v1_1(employee_id, time_off_assign_time_off_policies_for_an_employee_request_inner)

Assign Time Off Policies v1.1

To use this API make an HTTP PUT where the body of the request is the JSON documented below. A time off policy will be assigned to the employee with accruals starting on the date specified. On success, a 200 Success code is returned and the content of the response will be the same as the List Time off Policies API.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_off_assign_time_off_policies_for_an_employee_request_inner import TimeOffAssignTimeOffPoliciesForAnEmployeeRequestInner
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
    api_instance = bamboohr_sdk.TimeOffApi(api_client)
    employee_id = 'employee_id_example' # str | 
    time_off_assign_time_off_policies_for_an_employee_request_inner = [bamboohr_sdk.TimeOffAssignTimeOffPoliciesForAnEmployeeRequestInner()] # List[TimeOffAssignTimeOffPoliciesForAnEmployeeRequestInner] | 

    try:
        # Assign Time Off Policies v1.1
        api_instance.time_off_assign_time_off_policies_for_an_employee_v1_1(employee_id, time_off_assign_time_off_policies_for_an_employee_request_inner)
    except Exception as e:
        print("Exception when calling TimeOffApi->time_off_assign_time_off_policies_for_an_employee_v1_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**|  | 
 **time_off_assign_time_off_policies_for_an_employee_request_inner** | [**List[TimeOffAssignTimeOffPoliciesForAnEmployeeRequestInner]**](TimeOffAssignTimeOffPoliciesForAnEmployeeRequestInner.md)|  | 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_off_change_a_request_status**
> time_off_change_a_request_status(request_id, request)

Update Time Off Request Status

This endpoint allows you to change the status of a request in the system. You can use this to approve, deny, or cancel a time off request.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.request import Request
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
    api_instance = bamboohr_sdk.TimeOffApi(api_client)
    request_id = 'request_id_example' # str | 
    request = bamboohr_sdk.Request() # Request | 

    try:
        # Update Time Off Request Status
        api_instance.time_off_change_a_request_status(request_id, request)
    except Exception as e:
        print("Exception when calling TimeOffApi->time_off_change_a_request_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**|  | 
 **request** | [**Request**](Request.md)|  | 

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
**200** | The status has been updated. |  -  |
**400** | If the posted XML is invalid or the status is not \&quot;approved\&quot;, \&quot;denied\&quot;, \&quot;canceled\&quot;, or \&quot;declined\&quot;. |  -  |
**403** | If the current user doesn\\&#39;t have access to change the status in this way. |  -  |
**404** | If the time off request ID doesn\\&#39;t exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_off_get_time_off_balance**
> List[TimeOffBalanceEntry] time_off_get_time_off_balance(employee_id, accept_header_parameter=accept_header_parameter, end=end, precision=precision)

Get Time Off Balance

This endpoint returns time off balances for an employee for assigned categories as of a given date. Each category's balance is calculated by summing all historical balance events (accruals, manual adjustments, used time off, and carry-over events) plus any future accruals and adjustments up to the specified date. To get current balance, pass today's date in the 'end' parameter. To estimate a future balance, pass a future date. If no 'end' parameter is provided, it defaults to today.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_off_balance_entry import TimeOffBalanceEntry
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
    api_instance = bamboohr_sdk.TimeOffApi(api_client)
    employee_id = 56 # int | The ID of the employee to get time off balances for.
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)
    end = '2013-10-20' # date | The date to calculate the time off balance as of, in YYYY-MM-DD format. Defaults to company today if not provided. (optional)
    precision = 2 # int | Number of decimal places for balance and usedYearToDate values. Minimum 0, maximum 4. Defaults to 2. (optional) (default to 2)

    try:
        # Get Time Off Balance
        api_response = api_instance.time_off_get_time_off_balance(employee_id, accept_header_parameter=accept_header_parameter, end=end, precision=precision)
        print("The response of TimeOffApi->time_off_get_time_off_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeOffApi->time_off_get_time_off_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| The ID of the employee to get time off balances for. | 
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 
 **end** | **date**| The date to calculate the time off balance as of, in YYYY-MM-DD format. Defaults to company today if not provided. | [optional] 
 **precision** | **int**| Number of decimal places for balance and usedYearToDate values. Minimum 0, maximum 4. Defaults to 2. | [optional] [default to 2]

### Return type

[**List[TimeOffBalanceEntry]**](TimeOffBalanceEntry.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of time off balance entries, one per assigned time off type. |  -  |
**404** | Employee not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_off_get_time_off_requests**
> time_off_get_time_off_requests(start, end, accept_header_parameter=accept_header_parameter, id=id, action=action, employee_id=employee_id, type=type, status=status)

Get Time Off Requests

Retrieves a list of time off requests based on specified filters. This endpoint allows filtering by date range, status, employee, and time off type. It's useful for generating time off reports or displaying a calendar of time off events.

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
    api_instance = bamboohr_sdk.TimeOffApi(api_client)
    start = 'start_example' # str | YYYY-MM-DD. Only show time off that occurs on/after the specified start date.
    end = 'end_example' # str | YYYY-MM-DD. Only show time off that occurs on/before the specified end date.
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)
    id = 56 # int | A particular request ID to limit the response to. (optional)
    action = 'action_example' # str | Limit to requests that the user has a particular level of access to. Legal values are: \"view\" or \"approve\". Defaults to view. (optional)
    employee_id = 'employee_id_example' # str | A particular employee ID to limit the response to. (optional)
    type = 'type_example' # str | A comma separated list of time off types IDs to include limit the response to. If omitted, requests of all types are included. (optional)
    status = 'status_example' # str | A comma separated list of request status values to include. If omitted, requests of all status values are included. Legal values are \"approved\", \"denied\", \"superceded\", \"requested\", \"canceled\". (optional)

    try:
        # Get Time Off Requests
        api_instance.time_off_get_time_off_requests(start, end, accept_header_parameter=accept_header_parameter, id=id, action=action, employee_id=employee_id, type=type, status=status)
    except Exception as e:
        print("Exception when calling TimeOffApi->time_off_get_time_off_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **str**| YYYY-MM-DD. Only show time off that occurs on/after the specified start date. | 
 **end** | **str**| YYYY-MM-DD. Only show time off that occurs on/before the specified end date. | 
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 
 **id** | **int**| A particular request ID to limit the response to. | [optional] 
 **action** | **str**| Limit to requests that the user has a particular level of access to. Legal values are: \&quot;view\&quot; or \&quot;approve\&quot;. Defaults to view. | [optional] 
 **employee_id** | **str**| A particular employee ID to limit the response to. | [optional] 
 **type** | **str**| A comma separated list of time off types IDs to include limit the response to. If omitted, requests of all types are included. | [optional] 
 **status** | **str**| A comma separated list of request status values to include. If omitted, requests of all status values are included. Legal values are \&quot;approved\&quot;, \&quot;denied\&quot;, \&quot;superceded\&quot;, \&quot;requested\&quot;, \&quot;canceled\&quot;. | [optional] 

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
**200** |  |  -  |
**400** | Malformed request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_off_list_time_off_policies_for_employee**
> time_off_list_time_off_policies_for_employee(employee_id)

Get Time Off Policies for Employee

Retrieves a list of time off policies assigned to a specific employee. This includes policy details such as name, type, and current balance. The response helps in displaying available time off options and balances to employees.

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
    api_instance = bamboohr_sdk.TimeOffApi(api_client)
    employee_id = 'employee_id_example' # str | 

    try:
        # Get Time Off Policies for Employee
        api_instance.time_off_list_time_off_policies_for_employee(employee_id)
    except Exception as e:
        print("Exception when calling TimeOffApi->time_off_list_time_off_policies_for_employee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**|  | 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_off_list_time_off_policies_for_employee_v1_1**
> time_off_list_time_off_policies_for_employee_v1_1(employee_id)

Get Time Off Policies for Employee v1.1

Version 1.1 of the endpoint that retrieves time off policies for a specific employee. This version includes additional policy details and enhanced filtering capabilities compared to v1. It provides comprehensive information about each policy including accrual rates, carryover rules, and policy-specific settings.

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
    api_instance = bamboohr_sdk.TimeOffApi(api_client)
    employee_id = 'employee_id_example' # str | 

    try:
        # Get Time Off Policies for Employee v1.1
        api_instance.time_off_list_time_off_policies_for_employee_v1_1(employee_id)
    except Exception as e:
        print("Exception when calling TimeOffApi->time_off_list_time_off_policies_for_employee_v1_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**|  | 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

