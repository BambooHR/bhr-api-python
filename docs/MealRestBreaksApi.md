# bamboohr_sdk.MealRestBreaksApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_employees_to_break_policy**](MealRestBreaksApi.md#assign_employees_to_break_policy) | **POST** /api/v1/time-tracking/break-policies/{id}/assign | Assign Employees to Break Policy
[**create_break**](MealRestBreaksApi.md#create_break) | **POST** /api/v1/time-tracking/break-policies/{id}/breaks | Create Break
[**create_break_policy**](MealRestBreaksApi.md#create_break_policy) | **POST** /api/v1/time-tracking/break-policies | Create Break Policy
[**delete_break**](MealRestBreaksApi.md#delete_break) | **DELETE** /api/v1/time-tracking/breaks/{id} | Delete Break
[**delete_break_policy**](MealRestBreaksApi.md#delete_break_policy) | **DELETE** /api/v1/time-tracking/break-policies/{id} | Delete Break Policy
[**get_break**](MealRestBreaksApi.md#get_break) | **GET** /api/v1/time-tracking/breaks/{id} | Get Break
[**get_break_policy**](MealRestBreaksApi.md#get_break_policy) | **GET** /api/v1/time-tracking/break-policies/{id} | Get Break Policy
[**get_break_policy_suggestions**](MealRestBreaksApi.md#get_break_policy_suggestions) | **POST** /api/v1/time-tracking/break-policies/suggestions | Get Break Policy Suggestions
[**list_break_assessments**](MealRestBreaksApi.md#list_break_assessments) | **GET** /api/v1/time-tracking/break-assessments | List Break Assessments
[**list_break_policies**](MealRestBreaksApi.md#list_break_policies) | **GET** /api/v1/time-tracking/break-policies | List Break Policies
[**list_break_policy_breaks**](MealRestBreaksApi.md#list_break_policy_breaks) | **GET** /api/v1/time-tracking/break-policies/{id}/breaks | List Breaks for Break Policy
[**list_break_policy_employees**](MealRestBreaksApi.md#list_break_policy_employees) | **GET** /api/v1/time-tracking/break-policies/{id}/employees | List Break Policy Employees
[**list_employee_break_availabilities**](MealRestBreaksApi.md#list_employee_break_availabilities) | **GET** /api/v1/time-tracking/employees/{id}/break-availabilities | List Employee Break Availabilities
[**list_employee_break_policies**](MealRestBreaksApi.md#list_employee_break_policies) | **GET** /api/v1/time-tracking/employees/{id}/break-policies | List Employee Break Policies
[**replace_breaks_for_break_policy**](MealRestBreaksApi.md#replace_breaks_for_break_policy) | **PUT** /api/v1/time-tracking/break-policies/{id}/breaks | Replace Breaks for Break Policy
[**set_break_policy_employees**](MealRestBreaksApi.md#set_break_policy_employees) | **PUT** /api/v1/time-tracking/break-policies/{id}/assign | Set Employees for Break Policy
[**sync_break_policy**](MealRestBreaksApi.md#sync_break_policy) | **PUT** /api/v1/time-tracking/break-policies/{id}/sync | Sync Break Policy
[**unassign_employees_from_break_policy**](MealRestBreaksApi.md#unassign_employees_from_break_policy) | **POST** /api/v1/time-tracking/break-policies/{id}/unassign | Unassign Employees from Break Policy
[**update_break**](MealRestBreaksApi.md#update_break) | **PATCH** /api/v1/time-tracking/breaks/{id} | Update Break
[**update_break_policy**](MealRestBreaksApi.md#update_break_policy) | **PATCH** /api/v1/time-tracking/break-policies/{id} | Update Break Policy


# **assign_employees_to_break_policy**
> assign_employees_to_break_policy(id, assign_employees_to_break_policy_request)

Assign Employees to Break Policy

Assigns employees to a break policy. Adds the specified employees to the policy without removing existing assignments.

OAuth Scopes: time_tracking:breaks.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.assign_employees_to_break_policy_request import AssignEmployeesToBreakPolicyRequest
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
    api_instance = bamboohr_sdk.MealRestBreaksApi(api_client)
    id = 'id_example' # str | The break policy ID.
    assign_employees_to_break_policy_request = bamboohr_sdk.AssignEmployeesToBreakPolicyRequest() # AssignEmployeesToBreakPolicyRequest | 

    try:
        # Assign Employees to Break Policy
        api_instance.assign_employees_to_break_policy(id, assign_employees_to_break_policy_request)
    except Exception as e:
        print("Exception when calling MealRestBreaksApi->assign_employees_to_break_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 
 **assign_employees_to_break_policy_request** | [**AssignEmployeesToBreakPolicyRequest**](AssignEmployeesToBreakPolicyRequest.md)|  | 

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
**204** | Employees successfully assigned to the break policy |  -  |
**400** | Bad request - invalid data provided (for example: missing &#x60;employeeIds&#x60;, invalid IDs, or policy assignment constraints). |  -  |
**403** | Forbidden - insufficient permissions |  -  |
**404** | Break policy not found |  -  |
**422** | Unprocessable entity - validation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_break**
> TimeTrackingTimeTrackingBreakV1 create_break(id, time_tracking_create_time_tracking_break_v1)

Create Break

Creates a new break and associates it with the specified break policy.

OAuth Scopes: time_tracking:breaks.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_create_time_tracking_break_v1 import TimeTrackingCreateTimeTrackingBreakV1
from bamboohr_sdk.models.time_tracking_time_tracking_break_v1 import TimeTrackingTimeTrackingBreakV1
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
    api_instance = bamboohr_sdk.MealRestBreaksApi(api_client)
    id = 'id_example' # str | The break policy ID.
    time_tracking_create_time_tracking_break_v1 = bamboohr_sdk.TimeTrackingCreateTimeTrackingBreakV1() # TimeTrackingCreateTimeTrackingBreakV1 | 

    try:
        # Create Break
        api_response = api_instance.create_break(id, time_tracking_create_time_tracking_break_v1)
        print("The response of MealRestBreaksApi->create_break:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MealRestBreaksApi->create_break: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 
 **time_tracking_create_time_tracking_break_v1** | [**TimeTrackingCreateTimeTrackingBreakV1**](TimeTrackingCreateTimeTrackingBreakV1.md)|  | 

### Return type

[**TimeTrackingTimeTrackingBreakV1**](TimeTrackingTimeTrackingBreakV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a break |  -  |
**422** | Invalid request data |  -  |
**403** | Forbidden - user does not have permission |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_break_policy**
> TimeTrackingTimeTrackingBreakPolicyWithRelationsV1 create_break_policy(time_tracking_create_time_tracking_break_policy_v1)

Create Break Policy

Create a break policy. Breaks and assignments can be optionally included and created at the same time.

OAuth Scopes: time_tracking:breaks.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_create_time_tracking_break_policy_v1 import TimeTrackingCreateTimeTrackingBreakPolicyV1
from bamboohr_sdk.models.time_tracking_time_tracking_break_policy_with_relations_v1 import TimeTrackingTimeTrackingBreakPolicyWithRelationsV1
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
    api_instance = bamboohr_sdk.MealRestBreaksApi(api_client)
    time_tracking_create_time_tracking_break_policy_v1 = bamboohr_sdk.TimeTrackingCreateTimeTrackingBreakPolicyV1() # TimeTrackingCreateTimeTrackingBreakPolicyV1 | 

    try:
        # Create Break Policy
        api_response = api_instance.create_break_policy(time_tracking_create_time_tracking_break_policy_v1)
        print("The response of MealRestBreaksApi->create_break_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MealRestBreaksApi->create_break_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_tracking_create_time_tracking_break_policy_v1** | [**TimeTrackingCreateTimeTrackingBreakPolicyV1**](TimeTrackingCreateTimeTrackingBreakPolicyV1.md)|  | 

### Return type

[**TimeTrackingTimeTrackingBreakPolicyWithRelationsV1**](TimeTrackingTimeTrackingBreakPolicyWithRelationsV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a break policy |  -  |
**403** | Forbidden |  -  |
**422** | Invalid request data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_break**
> delete_break(id)

Delete Break

Deletes a time tracking break by its UUID. The break is soft-deleted and removed from any break policies it was associated with.

OAuth Scopes: time_tracking:breaks.write

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
    api_instance = bamboohr_sdk.MealRestBreaksApi(api_client)
    id = 'id_example' # str | The break ID.

    try:
        # Delete Break
        api_instance.delete_break(id)
    except Exception as e:
        print("Exception when calling MealRestBreaksApi->delete_break: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break ID. | 

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
**204** | Break deleted successfully |  -  |
**400** | Invalid ID format |  -  |
**403** | Forbidden |  -  |
**404** | Break not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_break_policy**
> delete_break_policy(id)

Delete Break Policy

Deletes a break policy by its UUID. Associated breaks and employee assignments are also removed.

OAuth Scopes: time_tracking:breaks.write

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
    api_instance = bamboohr_sdk.MealRestBreaksApi(api_client)
    id = 'id_example' # str | The break policy ID.

    try:
        # Delete Break Policy
        api_instance.delete_break_policy(id)
    except Exception as e:
        print("Exception when calling MealRestBreaksApi->delete_break_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 

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
**204** | Break policy deleted successfully |  -  |
**400** | Invalid uuid format |  -  |
**403** | Forbidden |  -  |
**404** | Break policy not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_break**
> TimeTrackingTimeTrackingBreakV1 get_break(id)

Get Break

Retrieves a single time tracking break by its UUID. Returns the full break details including name, duration, paid status, and availability configuration.

OAuth Scopes: time_tracking:breaks

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_time_tracking_break_v1 import TimeTrackingTimeTrackingBreakV1
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
    api_instance = bamboohr_sdk.MealRestBreaksApi(api_client)
    id = 'id_example' # str | The break ID.

    try:
        # Get Break
        api_response = api_instance.get_break(id)
        print("The response of MealRestBreaksApi->get_break:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MealRestBreaksApi->get_break: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break ID. | 

### Return type

[**TimeTrackingTimeTrackingBreakV1**](TimeTrackingTimeTrackingBreakV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the break. |  -  |
**403** | Forbidden |  -  |
**404** | Break not found. |  -  |
**422** | The provided &#x60;id&#x60; is not a valid UUID. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_break_policy**
> TimeTrackingTimeTrackingBreakPolicyV1 get_break_policy(id, include_counts=include_counts)

Get Break Policy

Retrieves a single break policy by its UUID. When includeCounts is enabled, the response includes the number of associated employees and breaks.

OAuth Scopes: time_tracking:breaks

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_time_tracking_break_policy_v1 import TimeTrackingTimeTrackingBreakPolicyV1
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
    api_instance = bamboohr_sdk.MealRestBreaksApi(api_client)
    id = 'id_example' # str | The break policy ID.
    include_counts = False # bool | Include employee and break counts (optional) (default to False)

    try:
        # Get Break Policy
        api_response = api_instance.get_break_policy(id, include_counts=include_counts)
        print("The response of MealRestBreaksApi->get_break_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MealRestBreaksApi->get_break_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 
 **include_counts** | **bool**| Include employee and break counts | [optional] [default to False]

### Return type

[**TimeTrackingTimeTrackingBreakPolicyV1**](TimeTrackingTimeTrackingBreakPolicyV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Break policy retrieved successfully |  -  |
**403** | Forbidden |  -  |
**404** | Break policy not found |  -  |
**422** | Invalid input |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_break_policy_suggestions**
> TimeTrackingBreakPolicySuggestionsResponseV1 get_break_policy_suggestions(get_break_policy_suggestions_request)

Get Break Policy Suggestions

Uses an AI agent to analyze existing break policies and company context, then returns structured meal and rest break policy recommendations ready for form pre-fill.

OAuth Scopes: time_tracking:breaks

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.get_break_policy_suggestions_request import GetBreakPolicySuggestionsRequest
from bamboohr_sdk.models.time_tracking_break_policy_suggestions_response_v1 import TimeTrackingBreakPolicySuggestionsResponseV1
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
    api_instance = bamboohr_sdk.MealRestBreaksApi(api_client)
    get_break_policy_suggestions_request = bamboohr_sdk.GetBreakPolicySuggestionsRequest() # GetBreakPolicySuggestionsRequest | 

    try:
        # Get Break Policy Suggestions
        api_response = api_instance.get_break_policy_suggestions(get_break_policy_suggestions_request)
        print("The response of MealRestBreaksApi->get_break_policy_suggestions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MealRestBreaksApi->get_break_policy_suggestions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_break_policy_suggestions_request** | [**GetBreakPolicySuggestionsRequest**](GetBreakPolicySuggestionsRequest.md)|  | 

### Return type

[**TimeTrackingBreakPolicySuggestionsResponseV1**](TimeTrackingBreakPolicySuggestionsResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Suggestions returned successfully |  -  |
**422** | Invalid request — prompt is missing or empty |  -  |
**500** | Internal server error — agent workflow failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_break_assessments**
> TimeTrackingPaginatedBreakAssessmentsResponseV1 list_break_assessments(offset=offset, limit=limit, filter=filter)

List Break Assessments

Returns a paginated list of break assessments. A break assessment records whether an employee complied with their assigned break policy for a given day, along with any violations. Use the `filter` parameter to scope results by employee, date, result, or other fields. Use `offset` and `limit` for pagination; `limit` defaults to 100 and may not exceed 500.

OAuth Scopes: time_tracking:breaks

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_paginated_break_assessments_response_v1 import TimeTrackingPaginatedBreakAssessmentsResponseV1
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
    api_instance = bamboohr_sdk.MealRestBreaksApi(api_client)
    offset = 0 # int | Number of items to skip before returning results. Defaults to 0. (optional) (default to 0)
    limit = 100 # int | Maximum number of items to return. Defaults to 100. Maximum is 500. (optional) (default to 100)
    filter = '' # str | OData filter expression applied to break assessments. Supported operators: `eq` (equals, use `eq null` to match NULL), `ne` (not equals, use `ne null` to match NOT NULL), `lt` (less than), `le` (less than or equal), `gt` (greater than), `ge` (greater than or equal), `in` (value in list), `and` (combine clauses). Not supported: `or`, `not`, parenthesized grouping. Filterable fields: `id`, `breakId`, `employeeId`, `employeeTimesheetId`, `date`, `result`, `availableYmdt`, `unavailableYmdt`, `expectedDuration`, `recordedDuration`, `durationDifference`, `createdAt`, `updatedAt`. Examples: `employeeId eq 614`, `employeeId in (614, 615, 616)`, `breakId eq 'abc-123' and employeeId eq 614`. (optional) (default to '')

    try:
        # List Break Assessments
        api_response = api_instance.list_break_assessments(offset=offset, limit=limit, filter=filter)
        print("The response of MealRestBreaksApi->list_break_assessments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MealRestBreaksApi->list_break_assessments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Number of items to skip before returning results. Defaults to 0. | [optional] [default to 0]
 **limit** | **int**| Maximum number of items to return. Defaults to 100. Maximum is 500. | [optional] [default to 100]
 **filter** | **str**| OData filter expression applied to break assessments. Supported operators: &#x60;eq&#x60; (equals, use &#x60;eq null&#x60; to match NULL), &#x60;ne&#x60; (not equals, use &#x60;ne null&#x60; to match NOT NULL), &#x60;lt&#x60; (less than), &#x60;le&#x60; (less than or equal), &#x60;gt&#x60; (greater than), &#x60;ge&#x60; (greater than or equal), &#x60;in&#x60; (value in list), &#x60;and&#x60; (combine clauses). Not supported: &#x60;or&#x60;, &#x60;not&#x60;, parenthesized grouping. Filterable fields: &#x60;id&#x60;, &#x60;breakId&#x60;, &#x60;employeeId&#x60;, &#x60;employeeTimesheetId&#x60;, &#x60;date&#x60;, &#x60;result&#x60;, &#x60;availableYmdt&#x60;, &#x60;unavailableYmdt&#x60;, &#x60;expectedDuration&#x60;, &#x60;recordedDuration&#x60;, &#x60;durationDifference&#x60;, &#x60;createdAt&#x60;, &#x60;updatedAt&#x60;. Examples: &#x60;employeeId eq 614&#x60;, &#x60;employeeId in (614, 615, 616)&#x60;, &#x60;breakId eq &#39;abc-123&#39; and employeeId eq 614&#x60;. | [optional] [default to &#39;&#39;]

### Return type

[**TimeTrackingPaginatedBreakAssessmentsResponseV1**](TimeTrackingPaginatedBreakAssessmentsResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of paginated break assessments |  -  |
**403** | Forbidden |  -  |
**422** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_break_policies**
> TimeTrackingPaginatedBreakPoliciesResponseV1 list_break_policies(offset=offset, limit=limit, filter=filter, include_counts=include_counts)

List Break Policies

Returns a paginated list of all break policies. Supports OData v4 filtering. Use includeCounts to include employee and break counts per policy.

OAuth Scopes: time_tracking:breaks

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_paginated_break_policies_response_v1 import TimeTrackingPaginatedBreakPoliciesResponseV1
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
    api_instance = bamboohr_sdk.MealRestBreaksApi(api_client)
    offset = 0 # int | The offset of items to retrieve (optional) (default to 0)
    limit = 100 # int | The maximum items to retrieve (optional) (default to 100)
    filter = '' # str | OData filter expression applied to break policies. Supported operators: `eq` (equals, use `eq null` to match NULL), `ne` (not equals, use `ne null` to match NOT NULL), `lt` (less than), `le` (less than or equal), `gt` (greater than), `ge` (greater than or equal), `in` (value in list), `and` (combine clauses). Not supported: `or`, `not`, parenthesized grouping. Filterable fields: `id`, `name`, `description`, `allEmployeesAssigned`, `createdAt`, `updatedAt`, `deletedAt`. Examples: `name eq 'Standard Lunch'`, `description eq null`, `allEmployeesAssigned eq true and name ne 'Legacy'`. (optional) (default to '')
    include_counts = False # bool | Include employee and break counts (optional) (default to False)

    try:
        # List Break Policies
        api_response = api_instance.list_break_policies(offset=offset, limit=limit, filter=filter, include_counts=include_counts)
        print("The response of MealRestBreaksApi->list_break_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MealRestBreaksApi->list_break_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The offset of items to retrieve | [optional] [default to 0]
 **limit** | **int**| The maximum items to retrieve | [optional] [default to 100]
 **filter** | **str**| OData filter expression applied to break policies. Supported operators: &#x60;eq&#x60; (equals, use &#x60;eq null&#x60; to match NULL), &#x60;ne&#x60; (not equals, use &#x60;ne null&#x60; to match NOT NULL), &#x60;lt&#x60; (less than), &#x60;le&#x60; (less than or equal), &#x60;gt&#x60; (greater than), &#x60;ge&#x60; (greater than or equal), &#x60;in&#x60; (value in list), &#x60;and&#x60; (combine clauses). Not supported: &#x60;or&#x60;, &#x60;not&#x60;, parenthesized grouping. Filterable fields: &#x60;id&#x60;, &#x60;name&#x60;, &#x60;description&#x60;, &#x60;allEmployeesAssigned&#x60;, &#x60;createdAt&#x60;, &#x60;updatedAt&#x60;, &#x60;deletedAt&#x60;. Examples: &#x60;name eq &#39;Standard Lunch&#39;&#x60;, &#x60;description eq null&#x60;, &#x60;allEmployeesAssigned eq true and name ne &#39;Legacy&#39;&#x60;. | [optional] [default to &#39;&#39;]
 **include_counts** | **bool**| Include employee and break counts | [optional] [default to False]

### Return type

[**TimeTrackingPaginatedBreakPoliciesResponseV1**](TimeTrackingPaginatedBreakPoliciesResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved break policies |  -  |
**403** | Forbidden |  -  |
**422** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_break_policy_breaks**
> TimeTrackingPaginatedBreaksResponseV1 list_break_policy_breaks(id, offset=offset, limit=limit, filter=filter)

List Breaks for Break Policy

Returns a paginated list of breaks belonging to the specified break policy. Supports OData v4 filtering.

OAuth Scopes: time_tracking:breaks

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_paginated_breaks_response_v1 import TimeTrackingPaginatedBreaksResponseV1
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
    api_instance = bamboohr_sdk.MealRestBreaksApi(api_client)
    id = 'id_example' # str | The break policy ID.
    offset = 0 # int | The offset of items to retrieve (optional) (default to 0)
    limit = 100 # int | The maximum items to retrieve (optional) (default to 100)
    filter = '' # str | OData filter expression applied to breaks within the policy. Supported operators: `eq` (equals, use `eq null` to match NULL), `ne` (not equals, use `ne null` to match NOT NULL), `lt` (less than), `le` (less than or equal), `gt` (greater than), `ge` (greater than or equal), `in` (value in list), `and` (combine clauses). Not supported: `or`, `not`, parenthesized grouping. Filterable fields: `id`, `name`, `paid`, `duration`, `availabilityType`, `availabilityMinHoursWorked`, `availabilityMaxHoursWorked`, `availabilityStartTime`, `availabilityEndTime`, `createdAt`, `updatedAt`, `deletedAt`. Examples: `name eq 'Lunch'`, `paid eq true`, `paid eq false and name ne 'Quick Break'`. (optional) (default to '')

    try:
        # List Breaks for Break Policy
        api_response = api_instance.list_break_policy_breaks(id, offset=offset, limit=limit, filter=filter)
        print("The response of MealRestBreaksApi->list_break_policy_breaks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MealRestBreaksApi->list_break_policy_breaks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 
 **offset** | **int**| The offset of items to retrieve | [optional] [default to 0]
 **limit** | **int**| The maximum items to retrieve | [optional] [default to 100]
 **filter** | **str**| OData filter expression applied to breaks within the policy. Supported operators: &#x60;eq&#x60; (equals, use &#x60;eq null&#x60; to match NULL), &#x60;ne&#x60; (not equals, use &#x60;ne null&#x60; to match NOT NULL), &#x60;lt&#x60; (less than), &#x60;le&#x60; (less than or equal), &#x60;gt&#x60; (greater than), &#x60;ge&#x60; (greater than or equal), &#x60;in&#x60; (value in list), &#x60;and&#x60; (combine clauses). Not supported: &#x60;or&#x60;, &#x60;not&#x60;, parenthesized grouping. Filterable fields: &#x60;id&#x60;, &#x60;name&#x60;, &#x60;paid&#x60;, &#x60;duration&#x60;, &#x60;availabilityType&#x60;, &#x60;availabilityMinHoursWorked&#x60;, &#x60;availabilityMaxHoursWorked&#x60;, &#x60;availabilityStartTime&#x60;, &#x60;availabilityEndTime&#x60;, &#x60;createdAt&#x60;, &#x60;updatedAt&#x60;, &#x60;deletedAt&#x60;. Examples: &#x60;name eq &#39;Lunch&#39;&#x60;, &#x60;paid eq true&#x60;, &#x60;paid eq false and name ne &#39;Quick Break&#39;&#x60;. | [optional] [default to &#39;&#39;]

### Return type

[**TimeTrackingPaginatedBreaksResponseV1**](TimeTrackingPaginatedBreaksResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved breaks for the specified break policy |  -  |
**403** | Forbidden |  -  |
**422** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_break_policy_employees**
> TimeTrackingPaginatedBreakPolicyEmployeesResponseV1 list_break_policy_employees(id, offset=offset, limit=limit)

List Break Policy Employees

Retrieves employees assigned to a specific break policy. If a policy has no assignments, returns HTTP 200 with an empty `data` array.

OAuth Scopes: time_tracking:breaks

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_paginated_break_policy_employees_response_v1 import TimeTrackingPaginatedBreakPolicyEmployeesResponseV1
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
    api_instance = bamboohr_sdk.MealRestBreaksApi(api_client)
    id = 'id_example' # str | The break policy ID.
    offset = 0 # int | The offset of items to retrieve (optional) (default to 0)
    limit = 100 # int | The maximum items to retrieve (optional) (default to 100)

    try:
        # List Break Policy Employees
        api_response = api_instance.list_break_policy_employees(id, offset=offset, limit=limit)
        print("The response of MealRestBreaksApi->list_break_policy_employees:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MealRestBreaksApi->list_break_policy_employees: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 
 **offset** | **int**| The offset of items to retrieve | [optional] [default to 0]
 **limit** | **int**| The maximum items to retrieve | [optional] [default to 100]

### Return type

[**TimeTrackingPaginatedBreakPolicyEmployeesResponseV1**](TimeTrackingPaginatedBreakPolicyEmployeesResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of employees assigned to a break policy |  -  |
**403** | Forbidden |  -  |
**422** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_employee_break_availabilities**
> List[TimeTrackingTimeTrackingBreakAvailabilityV1] list_employee_break_availabilities(id, effective=effective)

List Employee Break Availabilities

Retrieves break availability information for an employee. Requires permission to view the target employee in addition to time-tracking-break access.

OAuth Scopes: time_tracking:breaks

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_time_tracking_break_availability_v1 import TimeTrackingTimeTrackingBreakAvailabilityV1
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
    api_instance = bamboohr_sdk.MealRestBreaksApi(api_client)
    id = 56 # int | The internal employee ID.
    effective = '2025-12-15T14:30:00' # str | The employee's local time that should be used to calculate availability. Defaults to the current time. Must be in Y-m-d\\TH:i:s format (no timezone offset). (optional)

    try:
        # List Employee Break Availabilities
        api_response = api_instance.list_employee_break_availabilities(id, effective=effective)
        print("The response of MealRestBreaksApi->list_employee_break_availabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MealRestBreaksApi->list_employee_break_availabilities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The internal employee ID. | 
 **effective** | **str**| The employee&#39;s local time that should be used to calculate availability. Defaults to the current time. Must be in Y-m-d\\TH:i:s format (no timezone offset). | [optional] 

### Return type

[**List[TimeTrackingTimeTrackingBreakAvailabilityV1]**](TimeTrackingTimeTrackingBreakAvailabilityV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved break availabilities for the specified employee |  -  |
**403** | Forbidden - insufficient permissions to view this employee or break settings. |  -  |
**422** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_employee_break_policies**
> TimeTrackingPaginatedBreakPoliciesResponseV1 list_employee_break_policies(id, offset=offset, limit=limit)

List Employee Break Policies

Retrieves break policies assigned to a specific employee. Requires permission to view the target employee.

OAuth Scopes: time_tracking:breaks

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_paginated_break_policies_response_v1 import TimeTrackingPaginatedBreakPoliciesResponseV1
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
    api_instance = bamboohr_sdk.MealRestBreaksApi(api_client)
    id = 56 # int | The internal employee ID.
    offset = 0 # int | The number of items to skip before starting to collect the result set. Minimum 0. Defaults to 0. (optional) (default to 0)
    limit = 100 # int | The maximum number of items to return. Must be between 0 and 500. Defaults to 100. (optional) (default to 100)

    try:
        # List Employee Break Policies
        api_response = api_instance.list_employee_break_policies(id, offset=offset, limit=limit)
        print("The response of MealRestBreaksApi->list_employee_break_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MealRestBreaksApi->list_employee_break_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The internal employee ID. | 
 **offset** | **int**| The number of items to skip before starting to collect the result set. Minimum 0. Defaults to 0. | [optional] [default to 0]
 **limit** | **int**| The maximum number of items to return. Must be between 0 and 500. Defaults to 100. | [optional] [default to 100]

### Return type

[**TimeTrackingPaginatedBreakPoliciesResponseV1**](TimeTrackingPaginatedBreakPoliciesResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of break policies |  -  |
**403** | Forbidden |  -  |
**422** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_breaks_for_break_policy**
> List[TimeTrackingTimeTrackingBreakV1] replace_breaks_for_break_policy(id, time_tracking_create_or_update_time_tracking_break_without_policy_v1)

Replace Breaks for Break Policy

Replace all breaks for a break policy. Breaks with an ID will be updated, breaks without an ID will be created. Existing breaks not in the request will be soft-deleted.

OAuth Scopes: time_tracking:breaks.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_create_or_update_time_tracking_break_without_policy_v1 import TimeTrackingCreateOrUpdateTimeTrackingBreakWithoutPolicyV1
from bamboohr_sdk.models.time_tracking_time_tracking_break_v1 import TimeTrackingTimeTrackingBreakV1
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
    api_instance = bamboohr_sdk.MealRestBreaksApi(api_client)
    id = 'id_example' # str | The break policy ID.
    time_tracking_create_or_update_time_tracking_break_without_policy_v1 = [bamboohr_sdk.TimeTrackingCreateOrUpdateTimeTrackingBreakWithoutPolicyV1()] # List[TimeTrackingCreateOrUpdateTimeTrackingBreakWithoutPolicyV1] | 

    try:
        # Replace Breaks for Break Policy
        api_response = api_instance.replace_breaks_for_break_policy(id, time_tracking_create_or_update_time_tracking_break_without_policy_v1)
        print("The response of MealRestBreaksApi->replace_breaks_for_break_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MealRestBreaksApi->replace_breaks_for_break_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 
 **time_tracking_create_or_update_time_tracking_break_without_policy_v1** | [**List[TimeTrackingCreateOrUpdateTimeTrackingBreakWithoutPolicyV1]**](TimeTrackingCreateOrUpdateTimeTrackingBreakWithoutPolicyV1.md)|  | 

### Return type

[**List[TimeTrackingTimeTrackingBreakV1]**](TimeTrackingTimeTrackingBreakV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully replaced breaks for the policy |  -  |
**400** | Bad request - validation errors |  -  |
**403** | Insufficient permissions |  -  |
**404** | Break policy not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_break_policy_employees**
> set_break_policy_employees(id, set_break_policy_employees_request)

Set Employees for Break Policy

Sets the employee assignments for a break policy. This replaces all existing assignments with the provided list.

OAuth Scopes: time_tracking:breaks.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.set_break_policy_employees_request import SetBreakPolicyEmployeesRequest
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
    api_instance = bamboohr_sdk.MealRestBreaksApi(api_client)
    id = 'id_example' # str | The break policy ID.
    set_break_policy_employees_request = bamboohr_sdk.SetBreakPolicyEmployeesRequest() # SetBreakPolicyEmployeesRequest | 

    try:
        # Set Employees for Break Policy
        api_instance.set_break_policy_employees(id, set_break_policy_employees_request)
    except Exception as e:
        print("Exception when calling MealRestBreaksApi->set_break_policy_employees: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 
 **set_break_policy_employees_request** | [**SetBreakPolicyEmployeesRequest**](SetBreakPolicyEmployeesRequest.md)|  | 

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
**204** | Employees assigned successfully |  -  |
**400** | Invalid data provided. |  -  |
**403** | Forbidden |  -  |
**404** | Break policy not found |  -  |
**422** | Unprocessable entity. The provided &#x60;id&#x60; is not a valid UUID, or &#x60;employeeIds&#x60; is not an array of positive integers. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_break_policy**
> TimeTrackingTimeTrackingBreakPolicyWithRelationsV1 sync_break_policy(id, time_tracking_sync_time_tracking_break_policy_v1)

Sync Break Policy

Performs a full replacement of a break policy and its related data (breaks and employee assignments). Unlike the partial update endpoint, this replaces the entire policy state with the provided payload, removing any breaks or assignments not included in the request.

OAuth Scopes: time_tracking:breaks.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_sync_time_tracking_break_policy_v1 import TimeTrackingSyncTimeTrackingBreakPolicyV1
from bamboohr_sdk.models.time_tracking_time_tracking_break_policy_with_relations_v1 import TimeTrackingTimeTrackingBreakPolicyWithRelationsV1
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
    api_instance = bamboohr_sdk.MealRestBreaksApi(api_client)
    id = 'id_example' # str | The break policy ID.
    time_tracking_sync_time_tracking_break_policy_v1 = bamboohr_sdk.TimeTrackingSyncTimeTrackingBreakPolicyV1() # TimeTrackingSyncTimeTrackingBreakPolicyV1 | 

    try:
        # Sync Break Policy
        api_response = api_instance.sync_break_policy(id, time_tracking_sync_time_tracking_break_policy_v1)
        print("The response of MealRestBreaksApi->sync_break_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MealRestBreaksApi->sync_break_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 
 **time_tracking_sync_time_tracking_break_policy_v1** | [**TimeTrackingSyncTimeTrackingBreakPolicyV1**](TimeTrackingSyncTimeTrackingBreakPolicyV1.md)|  | 

### Return type

[**TimeTrackingTimeTrackingBreakPolicyWithRelationsV1**](TimeTrackingTimeTrackingBreakPolicyWithRelationsV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Break policy synced successfully |  -  |
**403** | Forbidden |  -  |
**404** | Break policy not found |  -  |
**422** | Invalid data provided |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_employees_from_break_policy**
> unassign_employees_from_break_policy(id, unassign_employees_from_break_policy_request)

Unassign Employees from Break Policy

Unassigns the specified employees from a break policy. Removes employee assignments from the policy without affecting the policy itself or other assigned employees. Employees can only be unassigned from policies that are not assigned to all employees.

OAuth Scopes: time_tracking:breaks.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.unassign_employees_from_break_policy_request import UnassignEmployeesFromBreakPolicyRequest
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
    api_instance = bamboohr_sdk.MealRestBreaksApi(api_client)
    id = 'id_example' # str | The break policy ID.
    unassign_employees_from_break_policy_request = bamboohr_sdk.UnassignEmployeesFromBreakPolicyRequest() # UnassignEmployeesFromBreakPolicyRequest | 

    try:
        # Unassign Employees from Break Policy
        api_instance.unassign_employees_from_break_policy(id, unassign_employees_from_break_policy_request)
    except Exception as e:
        print("Exception when calling MealRestBreaksApi->unassign_employees_from_break_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 
 **unassign_employees_from_break_policy_request** | [**UnassignEmployeesFromBreakPolicyRequest**](UnassignEmployeesFromBreakPolicyRequest.md)|  | 

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
**204** | Employees successfully unassigned from break policy |  -  |
**400** | Bad request - Invalid data or policy is assigned to all employees |  -  |
**403** | Forbidden |  -  |
**404** | Break policy not found |  -  |
**422** | Unprocessable entity - validation failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_break**
> TimeTrackingTimeTrackingBreakV1 update_break(id, time_tracking_update_time_tracking_break_v1)

Update Break

Partially updates a time tracking break identified by its UUID. Only fields provided in the request body are updated. Returns the updated break on success.

OAuth Scopes: time_tracking:breaks.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_time_tracking_break_v1 import TimeTrackingTimeTrackingBreakV1
from bamboohr_sdk.models.time_tracking_update_time_tracking_break_v1 import TimeTrackingUpdateTimeTrackingBreakV1
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
    api_instance = bamboohr_sdk.MealRestBreaksApi(api_client)
    id = 'id_example' # str | The break ID.
    time_tracking_update_time_tracking_break_v1 = bamboohr_sdk.TimeTrackingUpdateTimeTrackingBreakV1() # TimeTrackingUpdateTimeTrackingBreakV1 | 

    try:
        # Update Break
        api_response = api_instance.update_break(id, time_tracking_update_time_tracking_break_v1)
        print("The response of MealRestBreaksApi->update_break:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MealRestBreaksApi->update_break: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break ID. | 
 **time_tracking_update_time_tracking_break_v1** | [**TimeTrackingUpdateTimeTrackingBreakV1**](TimeTrackingUpdateTimeTrackingBreakV1.md)|  | 

### Return type

[**TimeTrackingTimeTrackingBreakV1**](TimeTrackingTimeTrackingBreakV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated break |  -  |
**403** | Forbidden |  -  |
**422** | Invalid request data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_break_policy**
> TimeTrackingTimeTrackingBreakPolicyV1 update_break_policy(id, time_tracking_update_time_tracking_break_policy_v1)

Update Break Policy

Partially updates a break policy identified by its UUID. Only fields provided in the request body are updated. Returns the updated break policy on success.

OAuth Scopes: time_tracking:breaks.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.time_tracking_time_tracking_break_policy_v1 import TimeTrackingTimeTrackingBreakPolicyV1
from bamboohr_sdk.models.time_tracking_update_time_tracking_break_policy_v1 import TimeTrackingUpdateTimeTrackingBreakPolicyV1
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
    api_instance = bamboohr_sdk.MealRestBreaksApi(api_client)
    id = 'id_example' # str | The break policy ID.
    time_tracking_update_time_tracking_break_policy_v1 = bamboohr_sdk.TimeTrackingUpdateTimeTrackingBreakPolicyV1() # TimeTrackingUpdateTimeTrackingBreakPolicyV1 | 

    try:
        # Update Break Policy
        api_response = api_instance.update_break_policy(id, time_tracking_update_time_tracking_break_policy_v1)
        print("The response of MealRestBreaksApi->update_break_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MealRestBreaksApi->update_break_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The break policy ID. | 
 **time_tracking_update_time_tracking_break_policy_v1** | [**TimeTrackingUpdateTimeTrackingBreakPolicyV1**](TimeTrackingUpdateTimeTrackingBreakPolicyV1.md)|  | 

### Return type

[**TimeTrackingTimeTrackingBreakPolicyV1**](TimeTrackingTimeTrackingBreakPolicyV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Break policy updated successfully |  -  |
**403** | Forbidden |  -  |
**404** | Break policy not found |  -  |
**422** | Invalid uuid format |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

