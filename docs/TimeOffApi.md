# bamboohr_sdk.TimeOffApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adjust_time_off_balance**](TimeOffApi.md#adjust_time_off_balance) | **PUT** /api/v1/employees/{employeeId}/time_off/balance_adjustment | Adjust Time Off Balance
[**assign_time_off_policies_v1**](TimeOffApi.md#assign_time_off_policies_v1) | **PUT** /api/v1/employees/{employeeId}/time_off/policies | Assign Time Off Policies (v1)
[**assign_time_off_policies_v11**](TimeOffApi.md#assign_time_off_policies_v11) | **PUT** /api/v1_1/employees/{employeeId}/time_off/policies | Assign Time Off Policies (v1.1)
[**create_time_off_history**](TimeOffApi.md#create_time_off_history) | **PUT** /api/v1/employees/{employeeId}/time_off/history | Create Time Off History Item
[**create_time_off_request**](TimeOffApi.md#create_time_off_request) | **PUT** /api/v1/employees/{employeeId}/time_off/request | Create Time Off Request
[**get_time_off_balance**](TimeOffApi.md#get_time_off_balance) | **GET** /api/v1/employees/{employeeId}/time_off/calculator | Get Time Off Balance
[**list_employee_time_off_policies_v1**](TimeOffApi.md#list_employee_time_off_policies_v1) | **GET** /api/v1/employees/{employeeId}/time_off/policies | List Employee Time Off Policies (v1)
[**list_employee_time_off_policies_v11**](TimeOffApi.md#list_employee_time_off_policies_v11) | **GET** /api/v1_1/employees/{employeeId}/time_off/policies | List Employee Time Off Policies (v1.1)
[**list_time_off_policies**](TimeOffApi.md#list_time_off_policies) | **GET** /api/v1/meta/time_off/policies | List Time Off Policies
[**list_time_off_requests**](TimeOffApi.md#list_time_off_requests) | **GET** /api/v1/time_off/requests | List Time Off Requests
[**list_time_off_types**](TimeOffApi.md#list_time_off_types) | **GET** /api/v1/meta/time_off/types | List Time Off Types
[**list_whos_out**](TimeOffApi.md#list_whos_out) | **GET** /api/v1/time_off/whos_out | List Who’s Out
[**list_whos_out_v1**](TimeOffApi.md#list_whos_out_v1) | **GET** /api/v1/whos-out | List Who&#39;s Out
[**update_time_off_request_status**](TimeOffApi.md#update_time_off_request_status) | **PUT** /api/v1/time_off/requests/{requestId}/status | Update Time Off Request Status


# **adjust_time_off_balance**
> adjust_time_off_balance(employee_id, adjust_time_off_balance)

Adjust Time Off Balance

Creates a balance adjustment for an employee's time off type. The adjustment is recorded as an override history item. Cannot adjust balances for discretionary (unlimited) time off types.

OAuth Scopes: time_off.write

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
    employee_id = 56 # int | The internal employee ID.
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
 **employee_id** | **int**| The internal employee ID. | 
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

# **assign_time_off_policies_v1**
> List[AssignedTimeOffPolicy] assign_time_off_policies_v1(employee_id, assign_time_off_policies_v1_request_inner)

Assign Time Off Policies (v1)

Deprecated. Use **Assign Time Off Policies (v1.1)** instead (`assign-time-off-policies-v1_1`). Assigns time off policies to an employee with accruals starting on the specified date. A null start date removes the existing assignment. On success, returns the current list of assigned policies.

OAuth Scopes: time_off.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.assign_time_off_policies_v1_request_inner import AssignTimeOffPoliciesV1RequestInner
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
    employee_id = 56 # int | The internal employee ID of the employee whose time off policies are being assigned.
    assign_time_off_policies_v1_request_inner = [bamboohr_sdk.AssignTimeOffPoliciesV1RequestInner()] # List[AssignTimeOffPoliciesV1RequestInner] | 

    try:
        # Assign Time Off Policies (v1)
        api_response = api_instance.assign_time_off_policies_v1(employee_id, assign_time_off_policies_v1_request_inner)
        print("The response of TimeOffApi->assign_time_off_policies_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeOffApi->assign_time_off_policies_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| The internal employee ID of the employee whose time off policies are being assigned. | 
 **assign_time_off_policies_v1_request_inner** | [**List[AssignTimeOffPoliciesV1RequestInner]**](AssignTimeOffPoliciesV1RequestInner.md)|  | 

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

# **assign_time_off_policies_v11**
> List[AssignedTimeOffPolicyV11] assign_time_off_policies_v11(employee_id, assign_time_off_policies_v1_request_inner)

Assign Time Off Policies (v1.1)

Assigns time off policies to an employee with accruals starting on the specified date. On success, returns the current list of assigned policies including manual and unlimited policy types.

OAuth Scopes: time_off.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.assign_time_off_policies_v1_request_inner import AssignTimeOffPoliciesV1RequestInner
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
    employee_id = 56 # int | The internal employee ID of the employee whose time off policies are being assigned.
    assign_time_off_policies_v1_request_inner = [bamboohr_sdk.AssignTimeOffPoliciesV1RequestInner()] # List[AssignTimeOffPoliciesV1RequestInner] | 

    try:
        # Assign Time Off Policies (v1.1)
        api_response = api_instance.assign_time_off_policies_v11(employee_id, assign_time_off_policies_v1_request_inner)
        print("The response of TimeOffApi->assign_time_off_policies_v11:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeOffApi->assign_time_off_policies_v11: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| The internal employee ID of the employee whose time off policies are being assigned. | 
 **assign_time_off_policies_v1_request_inner** | [**List[AssignTimeOffPoliciesV1RequestInner]**](AssignTimeOffPoliciesV1RequestInner.md)|  | 

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

OAuth Scopes: time_off.write

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
    employee_id = 56 # int | The internal employee ID.
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
 **employee_id** | **int**| The internal employee ID. | 
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
> CreatedTimeOffRequest create_time_off_request(employee_id, time_off_request)

Create Time Off Request

Creates a time off request for an employee. The request can be submitted with a status of `approved`, `denied`, or `requested`. Submitting `approved` or `denied` is only honored when the caller is an owner/admin or has view/edit access to the time off type field for the target employee; other callers receive 403. When honored, these statuses record the request directly and suppress approval notifications. Supplying a `previousRequest` ID performs a destructive supersede: the prior request's status is set to `superceded`, all approvals on its workflow are removed and the workflow is marked deleted, and any home-page notifications tied to that workflow are deleted. Accepts both JSON and XML request bodies.

OAuth Scopes: time_off.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.created_time_off_request import CreatedTimeOffRequest
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
    employee_id = 'employee_id_example' # str | The internal employee ID of the employee for whom to create the time off request.
    time_off_request = bamboohr_sdk.TimeOffRequest() # TimeOffRequest | 

    try:
        # Create Time Off Request
        api_response = api_instance.create_time_off_request(employee_id, time_off_request)
        print("The response of TimeOffApi->create_time_off_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeOffApi->create_time_off_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| The internal employee ID of the employee for whom to create the time off request. | 
 **time_off_request** | [**TimeOffRequest**](TimeOffRequest.md)|  | 

### Return type

[**CreatedTimeOffRequest**](CreatedTimeOffRequest.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Request created. The &#x60;Location&#x60; header contains the URL of the new request. When &#x60;Accept: application/json&#x60; is set, the response body contains the full created request — use the &#x60;id&#x60; field to chain follow-up operations (e.g. approve, cancel, supersede) without a separate lookup. |  -  |
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

**This endpoint does not accept the `0` self sentinel.** Unlike Get Employee (`get-employee`), passing `0` as `employeeId` returns `404` with an empty body and the header `x-bamboohr-error-message: Employee not found`. To read the authenticated caller's own balances, first resolve their internal employee ID with `get-employee` using the id `0`, then call this endpoint with that ID.

**Permissions.** Access is gated on the same Time Off tab view permission the web application uses. That permission is configured per access level and is **not** implied by the reporting structure: being an employee's manager does not by itself grant it, and a manager may receive `403` for their own direct reports. A caller without permission for the target employee receives an explicit `403` rather than an empty success, so the two cases are distinguishable: a `403` means access was denied, while an empty array with `200` means the employee has no assigned policies among the time off types this caller can view. Do not read a `403` as the employee having no time off, and do not read an empty array as a permission problem.

Because the categories returned are limited to the time off types the caller can view for that employee, two callers can legitimately receive different subsets for the same person. Treat the returned set as what this caller may see, not as the employee's complete policy list. `list-employee-time-off-policies-v1_1` is the companion endpoint for the underlying assignments and is gated on the same permission.

A category returning `0.00` is not an error and does not necessarily mean the time cannot be requested. Discretionary policies (for example Bereavement or FMLA) are granted as needed rather than accrued, so they normally report a zero balance while still being available to request. Use `policyType` to distinguish `accruing` from `discretionary` before characterizing a zero.

OAuth Scopes: time_off

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
    employee_id = 'employee_id_example' # str | The internal employee ID of the employee whose time off balances are returned.
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
 **employee_id** | **str**| The internal employee ID of the employee whose time off balances are returned. | 
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
**403** | Insufficient permissions to view this employee&#39;s time off. |  -  |
**404** | Employee not found. Some clients may receive an empty HTML response body for this legacy error case. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_employee_time_off_policies_v1**
> List[EmployeeTimeOffPolicyAssignment] list_employee_time_off_policies_v1(employee_id)

List Employee Time Off Policies (v1)

Deprecated. Use **List Employee Time Off Policies (v1.1)** instead (`list-employee-time-off-policies-v1_1`). Returns the time off policies currently assigned to the specified employee, including policy ID, time off type, and accrual start date.

OAuth Scopes: time_off

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
    employee_id = 'employee_id_example' # str | The internal employee ID.

    try:
        # List Employee Time Off Policies (v1)
        api_response = api_instance.list_employee_time_off_policies_v1(employee_id)
        print("The response of TimeOffApi->list_employee_time_off_policies_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeOffApi->list_employee_time_off_policies_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| The internal employee ID. | 

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

# **list_employee_time_off_policies_v11**
> List[EmployeeTimeOffPolicyAssignmentV11] list_employee_time_off_policies_v11(employee_id)

List Employee Time Off Policies (v1.1)

Returns the time off policies currently assigned to a specific employee, as a list of `{timeOffPolicyId, timeOffTypeId, accrualStartDate}` records. Use this to find which policy governs each time off type for this employee and when their accruals began. This is the per-employee assignment view; use `list-time-off-policies` for the company-wide policy catalog. Includes all policy types (accruing, manual, and unlimited); the v1 form of this endpoint excluded manual and unlimited types — v1.1 includes them.

OAuth Scopes: time_off

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
    employee_id = 'employee_id_example' # str | The internal employee ID.

    try:
        # List Employee Time Off Policies (v1.1)
        api_response = api_instance.list_employee_time_off_policies_v11(employee_id)
        print("The response of TimeOffApi->list_employee_time_off_policies_v11:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeOffApi->list_employee_time_off_policies_v11: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| The internal employee ID. | 

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

OAuth Scopes: time_off

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

**Do not pass `employeeId=0` expecting the caller's own requests.** Unlike Get Employee (`get-employee`), the `0` self sentinel is not supported here and returns an empty array with HTTP `200` rather than an error, which is easily misread as the caller having no requests. Use `action=myRequests` for the authenticated caller's own requests, or resolve their internal employee ID with `get-employee` using the id `0` and pass that value.

**An empty result does not mean the employee has no requests.** A caller who lacks permission to view another employee's time off receives an empty array with HTTP `200`, indistinguishable from an employee with no requests in the window. Before concluding that someone has no time off requests, confirm that the window is wide enough and that the caller can actually view that employee. This endpoint and Get Time Off Balance (`get-time-off-balance`) are gated independently, so neither one's outcome predicts the other's. A caller can receive `403` from the balance endpoint for an employee while still receiving that same employee's requests here, which has been observed for a manager viewing a direct report. Do not infer access to one endpoint from access to the other, and do not treat a result from one as evidence about the other.

OAuth Scopes: time_off

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
    start = '2013-10-20' # date | The left boundary of the search window, in YYYY-MM-DD format. Returns any request whose end date falls on or after this date — i.e., requests that are still active at the start of your window. To find all requests overlapping a date range, pass your range start here. Note: this parameter filters on each request's *end* date, not its start date.
    end = '2013-10-20' # date | The right boundary of the search window, in YYYY-MM-DD format. Returns any request whose start date falls on or before this date — i.e., requests that have begun by the end of your window. To find all requests overlapping a date range, pass your range end here. Note: this parameter filters on each request's *start* date, not its end date.
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)
    id = 'id_example' # str | A particular request ID to limit the response to. (optional)
    action = view # str | Limit to requests the caller can `view`, requests they can `approve`, or only their own requests via `myRequests`. Defaults to `view`. (optional) (default to view)
    employee_id = 'employee_id_example' # str | A particular internal employee ID to limit the response to. (optional)
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
 **start** | **date**| The left boundary of the search window, in YYYY-MM-DD format. Returns any request whose end date falls on or after this date — i.e., requests that are still active at the start of your window. To find all requests overlapping a date range, pass your range start here. Note: this parameter filters on each request&#39;s *end* date, not its start date. | 
 **end** | **date**| The right boundary of the search window, in YYYY-MM-DD format. Returns any request whose start date falls on or before this date — i.e., requests that have begun by the end of your window. To find all requests overlapping a date range, pass your range end here. Note: this parameter filters on each request&#39;s *start* date, not its end date. | 
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 
 **id** | **str**| A particular request ID to limit the response to. | [optional] 
 **action** | **str**| Limit to requests the caller can &#x60;view&#x60;, requests they can &#x60;approve&#x60;, or only their own requests via &#x60;myRequests&#x60;. Defaults to &#x60;view&#x60;. | [optional] [default to view]
 **employee_id** | **str**| A particular internal employee ID to limit the response to. | [optional] 
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

Lists the company's active time off types — PTO options, vacation, sick leave, and other time off categories — along with the company's default hours-per-day schedule. Pass `mode=request` to filter to only types the authenticated employee has permission to request. Time off type names are company-configured labels; common terms like "PTO" may not appear verbatim and may be expressed as "Vacation" or another company-specific name. The returned list is also permission-filtered: an admin caller may see types (e.g., "Sick") that a non-admin caller does not, so the set available for a given user depends on the caller's role. If a user's term does not exactly match a returned type name, present the available types as options rather than choosing one heuristically.

OAuth Scopes: time_off

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

Returns a date-sorted list of employees who are out and company holidays for the specified period. Defaults to today through 14 days out when dates are omitted. Results include both `timeOff` entries (employee requests) and `holiday` entries, each identified by `type`. An empty array may mean no one is out, or that no holidays have been configured in the BambooHR company calendar — holidays must be set up there before they appear here. The `filter: off` parameter applies only to employee time-off entries; holidays are independently filtered per-employee based on holiday visibility settings, and that filter is not disabled by `filter: off`.

OAuth Scopes: time_off

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
    filter = 'filter_example' # str | Controls the Who's Out calendar filter. By default (parameter omitted), results are limited to the set of employees defined by the authenticated user's saved Who's Out calendar filter (the same filter applied to their in-app Who's Out view). A user with no filter configured sees all employees; a user with a saved filter (e.g. by department, location, division) sees only the configured subset. Set to `off` to ignore the saved filter and return employee time-off entries for everyone — useful for admins or integrations that need the complete company-wide view, or to diagnose whether incomplete results are caused by the saved filter. Note: this parameter applies to employee `timeOff` entries only. `holiday` entries are filtered separately on a per-employee basis (holidays can be configured as visible to specific employees) and that filter is not affected by `filter: off`. (optional)

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
 **filter** | **str**| Controls the Who&#39;s Out calendar filter. By default (parameter omitted), results are limited to the set of employees defined by the authenticated user&#39;s saved Who&#39;s Out calendar filter (the same filter applied to their in-app Who&#39;s Out view). A user with no filter configured sees all employees; a user with a saved filter (e.g. by department, location, division) sees only the configured subset. Set to &#x60;off&#x60; to ignore the saved filter and return employee time-off entries for everyone — useful for admins or integrations that need the complete company-wide view, or to diagnose whether incomplete results are caused by the saved filter. Note: this parameter applies to employee &#x60;timeOff&#x60; entries only. &#x60;holiday&#x60; entries are filtered separately on a per-employee basis (holidays can be configured as visible to specific employees) and that filter is not affected by &#x60;filter: off&#x60;. | [optional] 

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

# **list_whos_out_v1**
> WhosOutListResponseV1 list_whos_out_v1(start, end, filter=filter, direct_reports_only=direct_reports_only, include_persons=include_persons, page=page, page_size=page_size)

List Who's Out

Lists approved time off occurrences overlapping the requested date range, scoped to employees the caller can see. Results the caller lacks permission to view are silently excluded. Dates are interpreted in the company timezone. Results are sorted by start date ascending, then id ascending.

OAuth Scopes: time_off

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.whos_out_list_response_v1 import WhosOutListResponseV1
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
    start = '2013-10-20' # date | Inclusive start date (YYYY-MM-DD). Interpreted in the company timezone.
    end = '2013-10-20' # date | Inclusive end date (YYYY-MM-DD). Must be on or after start; the range may not exceed 366 days.
    filter = 'filter_example' # str | OData filter expression applied to who's out results. Supported operators: `eq` (equals), `in` (value in list), `and` (combine clauses). Filterable fields: `employeeId` (int), `department` (int), `division` (int), `location` (int). Examples: `employeeId eq 42`, `department in (10, 20) and location eq 5`. (optional)
    direct_reports_only = False # bool | When true, restrict to time off for the caller's direct reports. Callers with no direct reports receive an empty result. (optional) (default to False)
    include_persons = False # bool | When true, embed a persons map of employee display data alongside results. (optional) (default to False)
    page = 1 # int | The page number to retrieve. (optional) (default to 1)
    page_size = 100 # int | The number of items to return per page. (optional) (default to 100)

    try:
        # List Who's Out
        api_response = api_instance.list_whos_out_v1(start, end, filter=filter, direct_reports_only=direct_reports_only, include_persons=include_persons, page=page, page_size=page_size)
        print("The response of TimeOffApi->list_whos_out_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeOffApi->list_whos_out_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**| Inclusive start date (YYYY-MM-DD). Interpreted in the company timezone. | 
 **end** | **date**| Inclusive end date (YYYY-MM-DD). Must be on or after start; the range may not exceed 366 days. | 
 **filter** | **str**| OData filter expression applied to who&#39;s out results. Supported operators: &#x60;eq&#x60; (equals), &#x60;in&#x60; (value in list), &#x60;and&#x60; (combine clauses). Filterable fields: &#x60;employeeId&#x60; (int), &#x60;department&#x60; (int), &#x60;division&#x60; (int), &#x60;location&#x60; (int). Examples: &#x60;employeeId eq 42&#x60;, &#x60;department in (10, 20) and location eq 5&#x60;. | [optional] 
 **direct_reports_only** | **bool**| When true, restrict to time off for the caller&#39;s direct reports. Callers with no direct reports receive an empty result. | [optional] [default to False]
 **include_persons** | **bool**| When true, embed a persons map of employee display data alongside results. | [optional] [default to False]
 **page** | **int**| The page number to retrieve. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**WhosOutListResponseV1**](WhosOutListResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of approved time off occurrences. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Missing the time_off scope. |  -  |
**422** | Invalid query parameters (e.g. missing or malformed start/end, end before start, range over 366 days, pageSize outside 10-100, or an unsupported filter field). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_time_off_request_status**
> object update_time_off_request_status(request_id, request)

Update Time Off Request Status

Updates the status of an existing time off request. Valid statuses are `approved`, `denied` (or `declined`), and `canceled`. Owner/admins can approve out of turn by completing all workflow steps at once; other approvers complete only their current step. Deprecated: use the approvals, denials, or cancellations process resources under /api/v1/time-off/requests/{id} instead.

OAuth Scopes: time_off.write

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
    request_id = 'request_id_example' # str | The ID of the time off request to update.
    request = bamboohr_sdk.Request() # Request | 

    try:
        # Update Time Off Request Status
        api_response = api_instance.update_time_off_request_status(request_id, request)
        print("The response of TimeOffApi->update_time_off_request_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeOffApi->update_time_off_request_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| The ID of the time off request to update. | 
 **request** | [**Request**](Request.md)|  | 

### Return type

**object**

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The status has been updated successfully. The response body is an empty JSON object (&#x60;{}&#x60;) with &#x60;Content-Type: application/json&#x60;. |  -  |
**400** | If the posted XML is invalid or the status is not \&quot;approved\&quot;, \&quot;denied\&quot;, \&quot;canceled\&quot;, or \&quot;declined\&quot;. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | If the current user doesn\\&#39;t have access to change the status in this way. |  -  |
**404** | If the time off request ID doesn\\&#39;t exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

