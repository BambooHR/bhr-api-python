# bamboohr_sdk.TimeOffApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adjust_time_off_balance**](TimeOffApi.md#adjust_time_off_balance) | **PUT** /api/v1/employees/{employeeId}/time_off/balance_adjustment | Adjust Time Off Balance
[**assign_time_off_policies**](TimeOffApi.md#assign_time_off_policies) | **PUT** /api/v1/employees/{employeeId}/time_off/policies | Assign Time Off Policies
[**assign_time_off_policies_v1_1**](TimeOffApi.md#assign_time_off_policies_v1_1) | **PUT** /api/v1_1/employees/{employeeId}/time_off/policies | Assign Time Off Policies v1.1
[**create_time_off_history**](TimeOffApi.md#create_time_off_history) | **PUT** /api/v1/employees/{employeeId}/time_off/history | Create Time Off History Item
[**create_time_off_request**](TimeOffApi.md#create_time_off_request) | **PUT** /api/v1/employees/{employeeId}/time_off/request | Create Time Off Request
[**get_time_off_balance**](TimeOffApi.md#get_time_off_balance) | **GET** /api/v1/employees/{employeeId}/time_off/calculator | Get Time Off Balance
[**list_employee_time_off_policies**](TimeOffApi.md#list_employee_time_off_policies) | **GET** /api/v1/employees/{employeeId}/time_off/policies | List Employee Time Off Policies
[**list_employee_time_off_policies_v1_1**](TimeOffApi.md#list_employee_time_off_policies_v1_1) | **GET** /api/v1_1/employees/{employeeId}/time_off/policies | List Employee Time Off Policies v1.1
[**list_time_off_policies**](TimeOffApi.md#list_time_off_policies) | **GET** /api/v1/meta/time_off/policies | List Time Off Policies
[**list_time_off_requests**](TimeOffApi.md#list_time_off_requests) | **GET** /api/v1/time_off/requests | List Time Off Requests
[**list_time_off_types**](TimeOffApi.md#list_time_off_types) | **GET** /api/v1/meta/time_off/types | List Time Off Types
[**list_whos_out**](TimeOffApi.md#list_whos_out) | **GET** /api/v1/time_off/whos_out | List Who’s Out
[**update_time_off_request_status**](TimeOffApi.md#update_time_off_request_status) | **PUT** /api/v1/time_off/requests/{requestId}/status | Update Time Off Request Status


# **adjust_time_off_balance**
> adjust_time_off_balance(employee_id, adjust_time_off_balance)

Adjust Time Off Balance

Creates a balance adjustment for an employee's time off type. The adjustment is recorded as an override history item. Cannot adjust balances for discretionary (unlimited) time off types.

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
        # Adjust Time Off Balance
        api_instance.adjust_time_off_balance(employee_id, adjust_time_off_balance)
    except Exception as e:
        print("Exception when calling TimeOffApi->adjust_time_off_balance: %s\n" % e)
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

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The balance adjustment has been created. |  -  |
**400** | Empty or malformed JSON/XML, an invalid date format, an invalid time off type, an invalid override amount, or an attempt to adjust a discretionary time off type. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient permissions to perform this action. |  -  |
**404** | Employee not found. |  -  |
**503** | Service unavailable due to a database error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_time_off_policies**
> List[AssignedTimeOffPolicy] assign_time_off_policies(employee_id, assign_time_off_policies_request_inner)

Assign Time Off Policies

Assigns time off policies to an employee with accruals starting on the specified date. A null start date removes the existing assignment. On success, returns the current list of assigned policies.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.assign_time_off_policies_request_inner import AssignTimeOffPoliciesRequestInner
from bamboohr_sdk.models.assigned_time_off_policy import AssignedTimeOffPolicy
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
    employee_id = 56 # int | The ID of the employee to assign policies to.
    assign_time_off_policies_request_inner = [bamboohr_sdk.AssignTimeOffPoliciesRequestInner()] # List[AssignTimeOffPoliciesRequestInner] | 

    try:
        # Assign Time Off Policies
        api_response = api_instance.assign_time_off_policies(employee_id, assign_time_off_policies_request_inner)
        print("The response of TimeOffApi->assign_time_off_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeOffApi->assign_time_off_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| The ID of the employee to assign policies to. | 
 **assign_time_off_policies_request_inner** | [**List[AssignTimeOffPoliciesRequestInner]**](AssignTimeOffPoliciesRequestInner.md)|  | 

### Return type

[**List[AssignedTimeOffPolicy]**](AssignedTimeOffPolicy.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current list of assigned policies for the employee. |  -  |
**400** | Invalid request. Possible causes: employee not found, missing hire date, malformed JSON, missing timeOffPolicyId, or a policy is already assigned for the time off type. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient permissions to assign time off policies. |  -  |
**422** | Unprocessable entity. The operation is not allowed for this employee, for example because of EOR restrictions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_time_off_policies_v1_1**
> List[AssignedTimeOffPolicyV11] assign_time_off_policies_v1_1(employee_id, assign_time_off_policies_request_inner)

Assign Time Off Policies v1.1

Assigns time off policies to an employee with accruals starting on the specified date. On success, returns the current list of assigned policies including manual and unlimited policy types.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.assign_time_off_policies_request_inner import AssignTimeOffPoliciesRequestInner
from bamboohr_sdk.models.assigned_time_off_policy_v11 import AssignedTimeOffPolicyV11
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
    employee_id = 56 # int | The ID of the employee to assign policies to.
    assign_time_off_policies_request_inner = [bamboohr_sdk.AssignTimeOffPoliciesRequestInner()] # List[AssignTimeOffPoliciesRequestInner] | 

    try:
        # Assign Time Off Policies v1.1
        api_response = api_instance.assign_time_off_policies_v1_1(employee_id, assign_time_off_policies_request_inner)
        print("The response of TimeOffApi->assign_time_off_policies_v1_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeOffApi->assign_time_off_policies_v1_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| The ID of the employee to assign policies to. | 
 **assign_time_off_policies_request_inner** | [**List[AssignTimeOffPoliciesRequestInner]**](AssignTimeOffPoliciesRequestInner.md)|  | 

### Return type

[**List[AssignedTimeOffPolicyV11]**](AssignedTimeOffPolicyV11.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current list of assigned policies for the employee, including manual and unlimited types. |  -  |
**400** | Invalid request. Possible causes: malformed JSON, missing required fields, missing hire date, or duplicate policy type. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient permissions to assign time off policies. |  -  |
**422** | Unprocessable entity. The operation is not allowed for this employee (e.g., EOR restrictions). |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_time_off_history**
> create_time_off_history(employee_id, time_off_history)

Create Time Off History Item

Creates a time off history item for an employee. For `used` type entries, a `timeOffRequestId` referencing an approved request is required. For `override` (balance adjustment) entries via the /history path, provide the `amount` and `timeOffTypeId` directly. The `eventType` defaults based on the URI path when omitted.

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
        # Create Time Off History Item
        api_instance.create_time_off_history(employee_id, time_off_history)
    except Exception as e:
        print("Exception when calling TimeOffApi->create_time_off_history: %s\n" % e)
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

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The history item has been created. |  -  |
**400** | Empty or malformed JSON/XML, an invalid date format, an invalid event type, an invalid time off request, an invalid time off type, or an invalid override amount. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Invalid permissions to perform this action. |  -  |
**404** | Employee not found. |  -  |
**409** | The time off request already has a history item. |  -  |
**503** | Service unavailable due to a database error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_time_off_request**
> create_time_off_request(employee_id, time_off_request)

Create Time Off Request

Creates a time off request for an employee. The request can be submitted with a status of `approved`, `denied`, or `requested`. Approved and denied requests are recorded directly without triggering approval notifications. A `previousRequest` ID supersedes an existing request, cancelling the original. Accepts both JSON and XML request bodies.

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
    employee_id = 56 # int | The ID of the employee to create the time off request for.
    time_off_request = bamboohr_sdk.TimeOffRequest() # TimeOffRequest | 

    try:
        # Create Time Off Request
        api_instance.create_time_off_request(employee_id, time_off_request)
    except Exception as e:
        print("Exception when calling TimeOffApi->create_time_off_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| The ID of the employee to create the time off request for. | 
 **time_off_request** | [**TimeOffRequest**](TimeOffRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Request created. The &#x60;Location&#x60; header contains the URL of the new request. When &#x60;Accept: application/json&#x60; is set, the response body contains the created request. |  -  |
**400** | Malformed JSON or XML, an invalid time off type, an invalid previous request ID, or other invalid request data. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Forbidden. The caller does not have permission to create or record this request for the employee, time off type, or requested status. |  -  |
**404** | Employee not found. |  -  |
**422** | Unprocessable entity. Returned when a remote/EOR time off request cannot be created for the requested action. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_off_balance**
> List[TimeOffBalanceEntry] get_time_off_balance(employee_id, accept_header_parameter=accept_header_parameter, end=end, precision=precision)

Get Time Off Balance

Returns time off balances for an employee across all assigned categories as of a given date. Each category's balance is calculated by summing all historical balance events (accruals, manual adjustments, used time off, and carry-over events) plus any future accruals and adjustments up to the specified date. To get current balances, pass today's date; to project future balances, pass a future date. Response defaults to XML unless Accept: application/json is provided.

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
    end = '2026-12-31' # date | The date to calculate the time off balance as of, in YYYY-MM-DD format. Defaults to company today if not provided. Example: use a future date to project balance. (optional)
    precision = 2 # int | Number of decimal places for balance and usedYearToDate values. Minimum 0, maximum 4. Defaults to 2. (optional) (default to 2)

    try:
        # Get Time Off Balance
        api_response = api_instance.get_time_off_balance(employee_id, accept_header_parameter=accept_header_parameter, end=end, precision=precision)
        print("The response of TimeOffApi->get_time_off_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeOffApi->get_time_off_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| The ID of the employee to get time off balances for. | 
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 
 **end** | **date**| The date to calculate the time off balance as of, in YYYY-MM-DD format. Defaults to company today if not provided. Example: use a future date to project balance. | [optional] 
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
**401** | Unauthorized. Invalid API credentials. |  -  |
**404** | Employee not found. Some clients may receive an empty HTML response body for this legacy error case. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_employee_time_off_policies**
> List[EmployeeTimeOffPolicyAssignment] list_employee_time_off_policies(employee_id)

List Employee Time Off Policies

Returns the time off policies currently assigned to the specified employee, including policy ID, time off type, and accrual start date.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.employee_time_off_policy_assignment import EmployeeTimeOffPolicyAssignment
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

    try:
        # List Employee Time Off Policies
        api_response = api_instance.list_employee_time_off_policies(employee_id)
        print("The response of TimeOffApi->list_employee_time_off_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeOffApi->list_employee_time_off_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| The ID of the employee. | 

### Return type

[**List[EmployeeTimeOffPolicyAssignment]**](EmployeeTimeOffPolicyAssignment.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of time off policies assigned to the employee. Only includes regular (accruing) policy types. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient permissions to view time off policy assignments. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_employee_time_off_policies_v1_1**
> List[EmployeeTimeOffPolicyAssignmentV11] list_employee_time_off_policies_v1_1(employee_id)

List Employee Time Off Policies v1.1

Returns the time off policies currently assigned to the specified employee, including manual and unlimited policy types that v1 excludes.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.employee_time_off_policy_assignment_v11 import EmployeeTimeOffPolicyAssignmentV11
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

    try:
        # List Employee Time Off Policies v1.1
        api_response = api_instance.list_employee_time_off_policies_v1_1(employee_id)
        print("The response of TimeOffApi->list_employee_time_off_policies_v1_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeOffApi->list_employee_time_off_policies_v1_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| The ID of the employee. | 

### Return type

[**List[EmployeeTimeOffPolicyAssignmentV11]**](EmployeeTimeOffPolicyAssignmentV11.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of time off policies assigned to the employee, including manual and unlimited types. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient permissions to view time off policy assignments. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_time_off_policies**
> List[TimeOffPolicy] list_time_off_policies(accept_header_parameter=accept_header_parameter)

List Time Off Policies

Returns all non-deleted time off policies for the company, sorted alphabetically by name. Only includes policies whose time off type has not been deleted.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_off_policy import TimeOffPolicy
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
        # List Time Off Policies
        api_response = api_instance.list_time_off_policies(accept_header_parameter=accept_header_parameter)
        print("The response of TimeOffApi->list_time_off_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeOffApi->list_time_off_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 

### Return type

[**List[TimeOffPolicy]**](TimeOffPolicy.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of all non-deleted time off policies, sorted alphabetically by name. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient permissions to view time off policies. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_time_off_requests**
> List[TimeOffRequest1] list_time_off_requests(start, end, accept_header_parameter=accept_header_parameter, id=id, action=action, employee_id=employee_id, type=type, status=status, exclude_note=exclude_note)

List Time Off Requests

Returns time off requests within the specified date range. Both `start` and `end` query parameters are required (YYYY-MM-DD). The search is inclusive: requests whose date range overlaps the query window are returned. Results can be filtered by status, employee, time off type, or limited to requests the caller can approve.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_off_request1 import TimeOffRequest1
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
    start = '2013-10-20' # date | Only include requests that end on or after this date. YYYY-MM-DD format.
    end = '2013-10-20' # date | Only include requests that start on or before this date. YYYY-MM-DD format.
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)
    id = 56 # int | A particular request ID to limit the response to. (optional)
    action = view # str | Limit to requests the caller can `view`, requests they can `approve`, or only their own requests via `myRequests`. Defaults to `view`. (optional) (default to view)
    employee_id = 56 # int | A particular employee ID to limit the response to. (optional)
    type = 'type_example' # str | A comma-separated list of time off type IDs to filter by. If omitted, requests of all types are included. (optional)
    status = 'status_example' # str | A comma-separated list of request status values to filter by. Accepted values are approved, denied, superceded, requested, and canceled. If omitted, requests of all statuses are included. (optional)
    exclude_note = 'exclude_note_example' # str | When set to any truthy value, omits the `notes` object from each request in the response. (optional)

    try:
        # List Time Off Requests
        api_response = api_instance.list_time_off_requests(start, end, accept_header_parameter=accept_header_parameter, id=id, action=action, employee_id=employee_id, type=type, status=status, exclude_note=exclude_note)
        print("The response of TimeOffApi->list_time_off_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeOffApi->list_time_off_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| Only include requests that end on or after this date. YYYY-MM-DD format. | 
 **end** | **date**| Only include requests that start on or before this date. YYYY-MM-DD format. | 
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 
 **id** | **int**| A particular request ID to limit the response to. | [optional] 
 **action** | **str**| Limit to requests the caller can &#x60;view&#x60;, requests they can &#x60;approve&#x60;, or only their own requests via &#x60;myRequests&#x60;. Defaults to &#x60;view&#x60;. | [optional] [default to view]
 **employee_id** | **int**| A particular employee ID to limit the response to. | [optional] 
 **type** | **str**| A comma-separated list of time off type IDs to filter by. If omitted, requests of all types are included. | [optional] 
 **status** | **str**| A comma-separated list of request status values to filter by. Accepted values are approved, denied, superceded, requested, and canceled. If omitted, requests of all statuses are included. | [optional] 
 **exclude_note** | **str**| When set to any truthy value, omits the &#x60;notes&#x60; object from each request in the response. | [optional] 

### Return type

[**List[TimeOffRequest1]**](TimeOffRequest1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of time off requests matching the specified filters. |  -  |
**400** | Invalid or missing start/end date. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_time_off_types**
> TimeOffTypesAndDefaultHours list_time_off_types(accept_header_parameter=accept_header_parameter, mode=mode)

List Time Off Types

Returns active time off types for the company along with the company's default hours-per-day schedule. Pass `mode=request` to filter to only types the authenticated employee has permission to request.

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
    mode = 'mode_example' # str | Set to `request` to limit the results to time off types the authenticated employee can request. (optional)

    try:
        # List Time Off Types
        api_response = api_instance.list_time_off_types(accept_header_parameter=accept_header_parameter, mode=mode)
        print("The response of TimeOffApi->list_time_off_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeOffApi->list_time_off_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 
 **mode** | **str**| Set to &#x60;request&#x60; to limit the results to time off types the authenticated employee can request. | [optional] 

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
**200** | Active time off types and the company&#39;s default hours-per-day schedule. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_whos_out**
> List[WhosOutEntry] list_whos_out(accept_header_parameter=accept_header_parameter, start=start, end=end, filter=filter)

List Who’s Out

Returns a date-sorted list of employees who are out and company holidays for the specified period. Defaults to today through 14 days out when dates are omitted. Results include both time off entries and holidays, each identified by type.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.whos_out_entry import WhosOutEntry
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
    start = '2013-10-20' # date | Start date in YYYY-MM-DD format. Defaults to today. (optional)
    end = '2013-10-20' # date | End date in YYYY-MM-DD format. Defaults to 14 days after the start date. (optional)
    filter = 'filter_example' # str | Set to `off` to disable the Who's Out visibility filter and return the unfiltered feed. Any other value leaves filtering enabled. (optional)

    try:
        # List Who’s Out
        api_response = api_instance.list_whos_out(accept_header_parameter=accept_header_parameter, start=start, end=end, filter=filter)
        print("The response of TimeOffApi->list_whos_out:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeOffApi->list_whos_out: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 
 **start** | **date**| Start date in YYYY-MM-DD format. Defaults to today. | [optional] 
 **end** | **date**| End date in YYYY-MM-DD format. Defaults to 14 days after the start date. | [optional] 
 **filter** | **str**| Set to &#x60;off&#x60; to disable the Who&#39;s Out visibility filter and return the unfiltered feed. Any other value leaves filtering enabled. | [optional] 

### Return type

[**List[WhosOutEntry]**](WhosOutEntry.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A date-sorted list of employees who are out and company holidays. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | The Who&#39;s Out feature is disabled for this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_time_off_request_status**
> update_time_off_request_status(request_id, request)

Update Time Off Request Status

Updates the status of an existing time off request. Valid statuses are `approved`, `denied` (or `declined`), and `canceled`. Owner/admins can approve out of turn by completing all workflow steps at once; other approvers complete only their current step.

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
    request_id = 56 # int | The ID of the time off request to update.
    request = bamboohr_sdk.Request() # Request | 

    try:
        # Update Time Off Request Status
        api_instance.update_time_off_request_status(request_id, request)
    except Exception as e:
        print("Exception when calling TimeOffApi->update_time_off_request_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **int**| The ID of the time off request to update. | 
 **request** | [**Request**](Request.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The status has been updated. |  -  |
**400** | If the posted XML is invalid or the status is not \&quot;approved\&quot;, \&quot;denied\&quot;, \&quot;canceled\&quot;, or \&quot;declined\&quot;. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | If the current user doesn\\&#39;t have access to change the status in this way. |  -  |
**404** | If the time off request ID doesn\\&#39;t exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

