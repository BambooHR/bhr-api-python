# bamboohr_sdk.GoalsApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_goal**](GoalsApi.md#delete_goal) | **DELETE** /api/v1/performance/employees/{employeeId}/goals/{goalId} | Delete Goal
[**delete_goal_comment**](GoalsApi.md#delete_goal_comment) | **DELETE** /api/v1/performance/employees/{employeeId}/goals/{goalId}/comments/{commentId} | Delete Goal Comment
[**get_can_create_goal**](GoalsApi.md#get_can_create_goal) | **GET** /api/v1/performance/employees/{employeeId}/goals/canCreateGoals | Check Goal Creation Permission
[**get_goal_aggregate**](GoalsApi.md#get_goal_aggregate) | **GET** /api/v1/performance/employees/{employeeId}/goals/{goalId}/aggregate | Get Goal Aggregate
[**get_goal_comments**](GoalsApi.md#get_goal_comments) | **GET** /api/v1/performance/employees/{employeeId}/goals/{goalId}/comments | Get Goal Comments
[**get_goals**](GoalsApi.md#get_goals) | **GET** /api/v1/performance/employees/{employeeId}/goals | Get Goals
[**get_goals_aggregate_v1**](GoalsApi.md#get_goals_aggregate_v1) | **GET** /api/v1/performance/employees/{employeeId}/goals/aggregate | Get Goals Aggregate
[**get_goals_aggregate_v1_1**](GoalsApi.md#get_goals_aggregate_v1_1) | **GET** /api/v1_1/performance/employees/{employeeId}/goals/aggregate | Get Goals Aggregate v1.1
[**get_goals_aggregate_v1_2**](GoalsApi.md#get_goals_aggregate_v1_2) | **GET** /api/v1_2/performance/employees/{employeeId}/goals/aggregate | Get Goals Aggregate v1.2
[**get_goals_alignment_options**](GoalsApi.md#get_goals_alignment_options) | **GET** /api/v1/performance/employees/{employeeId}/goals/alignmentOptions | Get Alignable Goal Options
[**get_goals_filters_v1**](GoalsApi.md#get_goals_filters_v1) | **GET** /api/v1/performance/employees/{employeeId}/goals/filters | Get Goal Filters
[**get_goals_filters_v1_1**](GoalsApi.md#get_goals_filters_v1_1) | **GET** /api/v1_1/performance/employees/{employeeId}/goals/filters | Get Goal Filters v1.1
[**get_goals_filters_v1_2**](GoalsApi.md#get_goals_filters_v1_2) | **GET** /api/v1_2/performance/employees/{employeeId}/goals/filters | Get Goal Status Counts v1.2
[**get_goals_share_options**](GoalsApi.md#get_goals_share_options) | **GET** /api/v1/performance/employees/{employeeId}/goals/shareOptions | Get Available Goal Sharing Options
[**post_close_goal**](GoalsApi.md#post_close_goal) | **POST** /api/v1/performance/employees/{employeeId}/goals/{goalId}/close | Close Goal
[**post_goal**](GoalsApi.md#post_goal) | **POST** /api/v1/performance/employees/{employeeId}/goals | Create Goal
[**post_goal_comment**](GoalsApi.md#post_goal_comment) | **POST** /api/v1/performance/employees/{employeeId}/goals/{goalId}/comments | Create Goal Comment
[**post_reopen_goal**](GoalsApi.md#post_reopen_goal) | **POST** /api/v1/performance/employees/{employeeId}/goals/{goalId}/reopen | Reopen Goal
[**put_goal_comment**](GoalsApi.md#put_goal_comment) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId}/comments/{commentId} | Update Goal Comment
[**put_goal_milestone_progress**](GoalsApi.md#put_goal_milestone_progress) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId}/milestones/{milestoneId}/progress | Update Milestone Progress
[**put_goal_progress**](GoalsApi.md#put_goal_progress) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId}/progress | Update Goal Progress
[**put_goal_shared_with**](GoalsApi.md#put_goal_shared_with) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId}/sharedWith | Update Goal Sharing
[**put_goal_v1**](GoalsApi.md#put_goal_v1) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId} | Update Goal
[**put_goal_v1_1**](GoalsApi.md#put_goal_v1_1) | **PUT** /api/v1_1/performance/employees/{employeeId}/goals/{goalId} | Update Goal v1.1


# **delete_goal**
> delete_goal(employee_id, goal_id)

Delete Goal

Delete a goal.

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
    api_instance = bamboohr_sdk.GoalsApi(api_client)
    employee_id = 'employee_id_example' # str | employeeId is the employee ID with whom the goal is associated.
    goal_id = 'goal_id_example' # str | goalId is the goal ID for the specified employee.

    try:
        # Delete Goal
        api_instance.delete_goal(employee_id, goal_id)
    except Exception as e:
        print("Exception when calling GoalsApi->delete_goal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID with whom the goal is associated. | 
 **goal_id** | **str**| goalId is the goal ID for the specified employee. | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The goal was successfully deleted. |  -  |
**403** | The API user does not have permission to delete this goal. |  -  |
**404** | The goalId is zero or non-positive after integer cast, or the goal was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_goal_comment**
> delete_goal_comment(employee_id, goal_id, comment_id)

Delete Goal Comment

Delete a goal comment.

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
    api_instance = bamboohr_sdk.GoalsApi(api_client)
    employee_id = 'employee_id_example' # str | employeeId is the employee ID with whom the goal is associated.
    goal_id = 'goal_id_example' # str | goalId is the goal ID for the specified employee.
    comment_id = 'comment_id_example' # str | commentId is the ID of a specific comment for the specified goal.

    try:
        # Delete Goal Comment
        api_instance.delete_goal_comment(employee_id, goal_id, comment_id)
    except Exception as e:
        print("Exception when calling GoalsApi->delete_goal_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID with whom the goal is associated. | 
 **goal_id** | **str**| goalId is the goal ID for the specified employee. | 
 **comment_id** | **str**| commentId is the ID of a specific comment for the specified goal. | 

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
**204** | The comment was successfully deleted. No response body is returned. |  -  |
**400** | The goal does not belong to the specified employee. |  -  |
**403** | Goal is not editable or insufficient permissions. |  -  |
**404** | The goal specified by the given goalId was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_can_create_goal**
> CanCreateGoalsResponse get_can_create_goal(employee_id)

Check Goal Creation Permission

Determine if the API user has permission to create a goal for this employee.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.can_create_goals_response import CanCreateGoalsResponse
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
    api_instance = bamboohr_sdk.GoalsApi(api_client)
    employee_id = 'employee_id_example' # str | employeeId is the employee ID with whom the goal is associated.

    try:
        # Check Goal Creation Permission
        api_response = api_instance.get_can_create_goal(employee_id)
        print("The response of GoalsApi->get_can_create_goal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->get_can_create_goal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID with whom the goal is associated. | 

### Return type

[**CanCreateGoalsResponse**](CanCreateGoalsResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns whether the API user can create a goal for this employee. |  -  |
**400** | The provided employeeId is invalid. |  -  |
**403** | The API user does not have permission to view goals for this employee. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goal_aggregate**
> GoalAggregate get_goal_aggregate(employee_id, goal_id)

Get Goal Aggregate

Provides goal information, goal comments, and employees shared with goals or who have commented on the given goal.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.goal_aggregate import GoalAggregate
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
    api_instance = bamboohr_sdk.GoalsApi(api_client)
    employee_id = 'employee_id_example' # str | employeeId is the employee ID with whom the goal is associated.
    goal_id = 'goal_id_example' # str | goalId is the Goal ID used to generate the aggregate information.

    try:
        # Get Goal Aggregate
        api_response = api_instance.get_goal_aggregate(employee_id, goal_id)
        print("The response of GoalsApi->get_goal_aggregate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->get_goal_aggregate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID with whom the goal is associated. | 
 **goal_id** | **str**| goalId is the Goal ID used to generate the aggregate information. | 

### Return type

[**GoalAggregate**](GoalAggregate.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response content will be a JSON object with the requested information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goal_comments**
> GoalCommentsResponse get_goal_comments(employee_id, goal_id)

Get Goal Comments

Get comments for a goal.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.goal_comments_response import GoalCommentsResponse
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
    api_instance = bamboohr_sdk.GoalsApi(api_client)
    employee_id = 'employee_id_example' # str | employeeId is the employee ID with whom the goal is associated.
    goal_id = 'goal_id_example' # str | goalId is the goal ID for the specified employee.

    try:
        # Get Goal Comments
        api_response = api_instance.get_goal_comments(employee_id, goal_id)
        print("The response of GoalsApi->get_goal_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->get_goal_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID with whom the goal is associated. | 
 **goal_id** | **str**| goalId is the goal ID for the specified employee. | 

### Return type

[**GoalCommentsResponse**](GoalCommentsResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns up to 50 comments for the specified goal, ordered by creation date. |  -  |
**403** | The API user does not have permission to view comments for this goal, or the goal does not belong to this employee. |  -  |
**404** | The specified goalId is invalid (non-positive integer). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goals**
> GoalsList get_goals(employee_id, filter=filter)

Get Goals

Get goals for an employee.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.goals_list import GoalsList
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
    api_instance = bamboohr_sdk.GoalsApi(api_client)
    employee_id = 'employee_id_example' # str | employeeId is the employee ID to whom the goals are assigned.
    filter = 'filter_example' # str | A filter that can be applied to only show the goals that are in a certain state. (optional)

    try:
        # Get Goals
        api_response = api_instance.get_goals(employee_id, filter=filter)
        print("The response of GoalsApi->get_goals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->get_goals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID to whom the goals are assigned. | 
 **filter** | **str**| A filter that can be applied to only show the goals that are in a certain state. | [optional] 

### Return type

[**GoalsList**](GoalsList.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response content will be a JSON document with the requested information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goals_aggregate_v1**
> GoalsAggregateV1 get_goals_aggregate_v1(employee_id, filter=filter)

Get Goals Aggregate

Provides a list of all goals, type counts, goal comment counts, and employees shared with goals for the given employee. This version of the endpoint will not return any goals with milestones. Milestone functionality for this endpoint begins in version 1.2.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.goals_aggregate_v1 import GoalsAggregateV1
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
    api_instance = bamboohr_sdk.GoalsApi(api_client)
    employee_id = 'employee_id_example' # str | employeeId is the employee ID used to generate the aggregate information.
    filter = 'filter_example' # str | Filter goals by status. Accepts filter IDs returned by the filters endpoint (e.g. status-inProgress). If omitted or invalid, defaults to the first available filter. The API accepts arbitrary strings and returns 200. (optional)

    try:
        # Get Goals Aggregate
        api_response = api_instance.get_goals_aggregate_v1(employee_id, filter=filter)
        print("The response of GoalsApi->get_goals_aggregate_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->get_goals_aggregate_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID used to generate the aggregate information. | 
 **filter** | **str**| Filter goals by status. Accepts filter IDs returned by the filters endpoint (e.g. status-inProgress). If omitted or invalid, defaults to the first available filter. The API accepts arbitrary strings and returns 200. | [optional] 

### Return type

[**GoalsAggregateV1**](GoalsAggregateV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response content will be a JSON object with the requested information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goals_aggregate_v1_1**
> GoalsAggregateV11 get_goals_aggregate_v1_1(employee_id, filter=filter)

Get Goals Aggregate v1.1

Provides a list of all goals, type counts, filter actions, goal comment counts, and employees shared with goals for the given employee. Difference from Version 1: Returns goals in the closed filter and provides filter actions for each filter. This version of the endpoint will not return any goals with milestones. Milestone functionality for this endpoint begins in version 1.2.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.goals_aggregate_v11 import GoalsAggregateV11
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
    api_instance = bamboohr_sdk.GoalsApi(api_client)
    employee_id = 'employee_id_example' # str | employeeId is the employee ID used to generate the aggregate information.
    filter = 'filter_example' # str | Filter goals by status. Accepts filter IDs returned by the filters endpoint (e.g. status-inProgress). If omitted or invalid, defaults to the first available filter. The API accepts arbitrary strings and returns 200. (optional)

    try:
        # Get Goals Aggregate v1.1
        api_response = api_instance.get_goals_aggregate_v1_1(employee_id, filter=filter)
        print("The response of GoalsApi->get_goals_aggregate_v1_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->get_goals_aggregate_v1_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID used to generate the aggregate information. | 
 **filter** | **str**| Filter goals by status. Accepts filter IDs returned by the filters endpoint (e.g. status-inProgress). If omitted or invalid, defaults to the first available filter. The API accepts arbitrary strings and returns 200. | [optional] 

### Return type

[**GoalsAggregateV11**](GoalsAggregateV11.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response content will be a JSON object with the requested information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goals_aggregate_v1_2**
> GoalsAggregateV12 get_goals_aggregate_v1_2(employee_id, filter=filter)

Get Goals Aggregate v1.2

Provides a list of all goals, type counts, filter actions, goal comment counts, and employees shared with goals for the given employee. Difference from Version 1.1: Returns all goals, including goals that contain milestones.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.goals_aggregate_v12 import GoalsAggregateV12
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
    api_instance = bamboohr_sdk.GoalsApi(api_client)
    employee_id = 56 # int | employeeId is the employee ID used to generate the aggregate information.
    filter = 'filter_example' # str | Filter goals by status. Accepts filter IDs returned by the filters endpoint (e.g. status-inProgress). If omitted or invalid, defaults to the first available filter. The API accepts arbitrary strings and returns 200. (optional)

    try:
        # Get Goals Aggregate v1.2
        api_response = api_instance.get_goals_aggregate_v1_2(employee_id, filter=filter)
        print("The response of GoalsApi->get_goals_aggregate_v1_2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->get_goals_aggregate_v1_2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| employeeId is the employee ID used to generate the aggregate information. | 
 **filter** | **str**| Filter goals by status. Accepts filter IDs returned by the filters endpoint (e.g. status-inProgress). If omitted or invalid, defaults to the first available filter. The API accepts arbitrary strings and returns 200. | [optional] 

### Return type

[**GoalsAggregateV12**](GoalsAggregateV12.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response content will be a JSON object with the requested information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goals_alignment_options**
> AlignmentOptionsResponse get_goals_alignment_options(employee_id, goal_id=goal_id)

Get Alignable Goal Options

Get alignable goal options for an employee.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.alignment_options_response import AlignmentOptionsResponse
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
    api_instance = bamboohr_sdk.GoalsApi(api_client)
    employee_id = 'employee_id_example' # str | employeeId is the employee ID to get alignable goal options for.
    goal_id = 56 # int | Optional. When provided, the response includes the option currently aligned with this goal. If omitted, returns alignment options for the API user. (optional)

    try:
        # Get Alignable Goal Options
        api_response = api_instance.get_goals_alignment_options(employee_id, goal_id=goal_id)
        print("The response of GoalsApi->get_goals_alignment_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->get_goals_alignment_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID to get alignable goal options for. | 
 **goal_id** | **int**| Optional. When provided, the response includes the option currently aligned with this goal. If omitted, returns alignment options for the API user. | [optional] 

### Return type

[**AlignmentOptionsResponse**](AlignmentOptionsResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response content will be a JSON document with a list of goals that are available alignment options. |  -  |
**400** | The provided goalId does not belong to the specified employee. |  -  |
**403** | The employeeId resolves to 0 (invalid path segment), or the API user lacks permission to view the specified goal. |  -  |
**404** | The provided goalId is zero or non-positive after integer cast (e.g. goalId&#x3D;0, goalId&#x3D;-1, or a non-numeric value such as goalId&#x3D;abc). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goals_filters_v1**
> GoalFiltersV1 get_goals_filters_v1(employee_id)

Get Goal Filters

Get the number of goals per status for an employee.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.goal_filters_v1 import GoalFiltersV1
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
    api_instance = bamboohr_sdk.GoalsApi(api_client)
    employee_id = 56 # int | employeeId is the employee ID to whom the goals are assigned.

    try:
        # Get Goal Filters
        api_response = api_instance.get_goals_filters_v1(employee_id)
        print("The response of GoalsApi->get_goals_filters_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->get_goals_filters_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| employeeId is the employee ID to whom the goals are assigned. | 

### Return type

[**GoalFiltersV1**](GoalFiltersV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns goal status filter counts. Goals with milestones are excluded in this version. |  -  |
**403** | The API user does not have permission to view goals for this employee. |  -  |
**500** | Something went wrong fetching filters. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goals_filters_v1_1**
> GoalFiltersV11 get_goals_filters_v1_1(employee_id)

Get Goal Filters v1.1

Get the number of goals per status for an employee. Difference from Version 1: Includes actions.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.goal_filters_v11 import GoalFiltersV11
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
    api_instance = bamboohr_sdk.GoalsApi(api_client)
    employee_id = 56 # int | employeeId is the employee ID to whom the goals are assigned.

    try:
        # Get Goal Filters v1.1
        api_response = api_instance.get_goals_filters_v1_1(employee_id)
        print("The response of GoalsApi->get_goals_filters_v1_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->get_goals_filters_v1_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| employeeId is the employee ID to whom the goals are assigned. | 

### Return type

[**GoalFiltersV11**](GoalFiltersV11.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contains the map of goal statuses, their counts, and available actions |  -  |
**403** | Permissions error. |  -  |
**500** | Something went wrong fetching filters. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goals_filters_v1_2**
> GoalFiltersV11 get_goals_filters_v1_2(employee_id)

Get Goal Status Counts v1.2

Get the number of goals per status for an employee. Difference from Version 1_1: Returns goals with milestones.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.goal_filters_v11 import GoalFiltersV11
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
    api_instance = bamboohr_sdk.GoalsApi(api_client)
    employee_id = 56 # int | employeeId is the employee ID to whom the goals are assigned.

    try:
        # Get Goal Status Counts v1.2
        api_response = api_instance.get_goals_filters_v1_2(employee_id)
        print("The response of GoalsApi->get_goals_filters_v1_2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->get_goals_filters_v1_2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| employeeId is the employee ID to whom the goals are assigned. | 

### Return type

[**GoalFiltersV11**](GoalFiltersV11.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contains the map of goal statuses, their counts, and available actions |  -  |
**403** | Permissions error. |  -  |
**500** | Something went wrong fetching filters. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goals_share_options**
> ShareOptionsResponse get_goals_share_options(employee_id, search, limit=limit)

Get Available Goal Sharing Options

Provides a list of employees with whom the specified employee\'s goals may be shared.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.share_options_response import ShareOptionsResponse
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
    api_instance = bamboohr_sdk.GoalsApi(api_client)
    employee_id = 'employee_id_example' # str | employeeId is the employee ID to get sharing options for.
    search = 'search_example' # str | The search term used to filter employees returned. Will search name, employee ID and email.
    limit = 10 # int | Maximum number of employees to return. Defaults to 10, maximum 100. (optional) (default to 10)

    try:
        # Get Available Goal Sharing Options
        api_response = api_instance.get_goals_share_options(employee_id, search, limit=limit)
        print("The response of GoalsApi->get_goals_share_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->get_goals_share_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID to get sharing options for. | 
 **search** | **str**| The search term used to filter employees returned. Will search name, employee ID and email. | 
 **limit** | **int**| Maximum number of employees to return. Defaults to 10, maximum 100. | [optional] [default to 10]

### Return type

[**ShareOptionsResponse**](ShareOptionsResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response content will be a JSON document with a list of available employees with whom the goals can be shared. |  -  |
**400** | The search parameter is invalid or empty. |  -  |
**403** | Goals are not enabled, or the API user does not have permission to view sharing options for this employee. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_close_goal**
> TransformedApiGoal post_close_goal(employee_id, goal_id, body=body)

Close Goal

Close a goal.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.transformed_api_goal import TransformedApiGoal
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
    api_instance = bamboohr_sdk.GoalsApi(api_client)
    employee_id = 'employee_id_example' # str | employeeId is the employee ID with whom the goal is associated.
    goal_id = 'goal_id_example' # str | goalId is the goal ID for the specified employee.
    body = 'body_example' # str | Comment field is optional. (optional)

    try:
        # Close Goal
        api_response = api_instance.post_close_goal(employee_id, goal_id, body=body)
        print("The response of GoalsApi->post_close_goal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->post_close_goal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID with whom the goal is associated. | 
 **goal_id** | **str**| goalId is the goal ID for the specified employee. | 
 **body** | **str**| Comment field is optional. | [optional] 

### Return type

[**TransformedApiGoal**](TransformedApiGoal.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A successful response indicates that all the goal was closed. The content of the response will be the goal response object for the specified goalId. |  -  |
**400** | The posted JSON is invalid. |  -  |
**403** | Goal is not editable or insufficient permissions. |  -  |
**404** | The goal specified by the given goalId was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_goal**
> TransformedApiEmployeeGoalDetails post_goal(employee_id, post_goal_request)

Create Goal

Create a new goal for an employee.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.post_goal_request import PostGoalRequest
from bamboohr_sdk.models.transformed_api_employee_goal_details import TransformedApiEmployeeGoalDetails
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
    api_instance = bamboohr_sdk.GoalsApi(api_client)
    employee_id = 'employee_id_example' # str | employeeId is the employee ID with whom the goal is associated.
    post_goal_request = bamboohr_sdk.PostGoalRequest() # PostGoalRequest | 

    try:
        # Create Goal
        api_response = api_instance.post_goal(employee_id, post_goal_request)
        print("The response of GoalsApi->post_goal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->post_goal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID with whom the goal is associated. | 
 **post_goal_request** | [**PostGoalRequest**](PostGoalRequest.md)|  | 

### Return type

[**TransformedApiEmployeeGoalDetails**](TransformedApiEmployeeGoalDetails.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A goal object that includes the new goal. |  -  |
**400** | If the posted XML or JSON is invalid or the minimum fields are not provided. |  -  |
**403** | If the API user does not have permission to create a goal for this employee. |  -  |
**500** | If there was a problem creating the goal. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_goal_comment**
> GoalCommentResponse post_goal_comment(employee_id, goal_id, post_goal_comment_request)

Create Goal Comment

Create a new goal comment.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.goal_comment_response import GoalCommentResponse
from bamboohr_sdk.models.post_goal_comment_request import PostGoalCommentRequest
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
    api_instance = bamboohr_sdk.GoalsApi(api_client)
    employee_id = 'employee_id_example' # str | employeeId is the employee ID with whom the goal is associated.
    goal_id = 'goal_id_example' # str | goalId is the goal ID for the specified employee.
    post_goal_comment_request = bamboohr_sdk.PostGoalCommentRequest() # PostGoalCommentRequest | 

    try:
        # Create Goal Comment
        api_response = api_instance.post_goal_comment(employee_id, goal_id, post_goal_comment_request)
        print("The response of GoalsApi->post_goal_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->post_goal_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID with whom the goal is associated. | 
 **goal_id** | **str**| goalId is the goal ID for the specified employee. | 
 **post_goal_comment_request** | [**PostGoalCommentRequest**](PostGoalCommentRequest.md)|  | 

### Return type

[**GoalCommentResponse**](GoalCommentResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A goal comment object with the new goal comment ID. |  -  |
**400** | The goal does not belong to the specified employee, or the comment text is blank. |  -  |
**403** | If the API user does not have permission to add a comment to the specified goal. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_reopen_goal**
> TransformedApiGoal post_reopen_goal(employee_id, goal_id)

Reopen Goal

Reopen a goal.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.transformed_api_goal import TransformedApiGoal
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
    api_instance = bamboohr_sdk.GoalsApi(api_client)
    employee_id = 'employee_id_example' # str | employeeId is the employee ID with whom the goal is associated.
    goal_id = 'goal_id_example' # str | goalId is the goal ID for the specified employee.

    try:
        # Reopen Goal
        api_response = api_instance.post_reopen_goal(employee_id, goal_id)
        print("The response of GoalsApi->post_reopen_goal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->post_reopen_goal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID with whom the goal is associated. | 
 **goal_id** | **str**| goalId is the goal ID for the specified employee. | 

### Return type

[**TransformedApiGoal**](TransformedApiGoal.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A successful response indicates that all the goal was reopened. The content of the response will be the goal response object for the specified goalId. |  -  |
**400** | The posted JSON is invalid. |  -  |
**403** | Goal is not editable or insufficient permissions. |  -  |
**404** | The goal specified by the given goalId was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_goal_comment**
> GoalCommentResponse put_goal_comment(employee_id, goal_id, comment_id, put_goal_comment_request)

Update Goal Comment

Update a goal comment.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.goal_comment_response import GoalCommentResponse
from bamboohr_sdk.models.put_goal_comment_request import PutGoalCommentRequest
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
    api_instance = bamboohr_sdk.GoalsApi(api_client)
    employee_id = 'employee_id_example' # str | employeeId is the employee ID with whom the goal is associated.
    goal_id = 'goal_id_example' # str | goalId is the goal ID for the specified employee.
    comment_id = 'comment_id_example' # str | commentId is the comment ID for the specified goal.
    put_goal_comment_request = bamboohr_sdk.PutGoalCommentRequest() # PutGoalCommentRequest | 

    try:
        # Update Goal Comment
        api_response = api_instance.put_goal_comment(employee_id, goal_id, comment_id, put_goal_comment_request)
        print("The response of GoalsApi->put_goal_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->put_goal_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID with whom the goal is associated. | 
 **goal_id** | **str**| goalId is the goal ID for the specified employee. | 
 **comment_id** | **str**| commentId is the comment ID for the specified goal. | 
 **put_goal_comment_request** | [**PutGoalCommentRequest**](PutGoalCommentRequest.md)|  | 

### Return type

[**GoalCommentResponse**](GoalCommentResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response indicates that all the requested changes were made. The content of the response will be the goal comment response object for the specified commentId. |  -  |
**400** | The goal does not belong to the specified employee, or the comment text is blank. |  -  |
**403** | Goal is not editable or insufficient permissions. |  -  |
**404** | The goal specified by the given goalId was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_goal_milestone_progress**
> TransformedApiEmployeeGoalDetails put_goal_milestone_progress(employee_id, goal_id, milestone_id, put_goal_milestone_progress_request)

Update Milestone Progress

Update the progress of a milestone in a goal.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.put_goal_milestone_progress_request import PutGoalMilestoneProgressRequest
from bamboohr_sdk.models.transformed_api_employee_goal_details import TransformedApiEmployeeGoalDetails
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
    api_instance = bamboohr_sdk.GoalsApi(api_client)
    employee_id = 'employee_id_example' # str | employeeId is the employee ID to whom the goals are assigned.
    goal_id = 'goal_id_example' # str | goalId is the goal ID for the specified employee.
    milestone_id = 'milestone_id_example' # str | milestoneId is the milestone ID for the specified goal.
    put_goal_milestone_progress_request = bamboohr_sdk.PutGoalMilestoneProgressRequest() # PutGoalMilestoneProgressRequest | 

    try:
        # Update Milestone Progress
        api_response = api_instance.put_goal_milestone_progress(employee_id, goal_id, milestone_id, put_goal_milestone_progress_request)
        print("The response of GoalsApi->put_goal_milestone_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->put_goal_milestone_progress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID to whom the goals are assigned. | 
 **goal_id** | **str**| goalId is the goal ID for the specified employee. | 
 **milestone_id** | **str**| milestoneId is the milestone ID for the specified goal. | 
 **put_goal_milestone_progress_request** | [**PutGoalMilestoneProgressRequest**](PutGoalMilestoneProgressRequest.md)|  | 

### Return type

[**TransformedApiEmployeeGoalDetails**](TransformedApiEmployeeGoalDetails.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the milestone progress |  -  |
**400** | Invalid request parameters provided |  -  |
**403** | User does not have permission to update this goal |  -  |
**404** | Goal or milestone not found |  -  |
**500** | Something went wrong updating your progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_goal_progress**
> TransformedApiEmployeeGoalDetails put_goal_progress(employee_id, goal_id, put_goal_progress_request)

Update Goal Progress

Update the progress percentage of an individual goal.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.put_goal_progress_request import PutGoalProgressRequest
from bamboohr_sdk.models.transformed_api_employee_goal_details import TransformedApiEmployeeGoalDetails
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
    api_instance = bamboohr_sdk.GoalsApi(api_client)
    employee_id = 56 # int | employeeId is the employee ID with whom the goal is associated.
    goal_id = 56 # int | goalId is the goal ID for the specified employee.
    put_goal_progress_request = bamboohr_sdk.PutGoalProgressRequest() # PutGoalProgressRequest | Employee IDs of employees with whom the goal is shared. All goal owners are considered \"shared with\".

    try:
        # Update Goal Progress
        api_response = api_instance.put_goal_progress(employee_id, goal_id, put_goal_progress_request)
        print("The response of GoalsApi->put_goal_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->put_goal_progress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| employeeId is the employee ID with whom the goal is associated. | 
 **goal_id** | **int**| goalId is the goal ID for the specified employee. | 
 **put_goal_progress_request** | [**PutGoalProgressRequest**](PutGoalProgressRequest.md)| Employee IDs of employees with whom the goal is shared. All goal owners are considered \&quot;shared with\&quot;. | 

### Return type

[**TransformedApiEmployeeGoalDetails**](TransformedApiEmployeeGoalDetails.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response indicates that all the requested changes were made. The content of the response will be the goal response object for the specified goalId. |  -  |
**400** | The posted JSON is invalid. |  -  |
**403** | Goal is not editable or insufficient permissions. |  -  |
**404** | No goal found for the given goalId. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_goal_shared_with**
> TransformedApiGoal put_goal_shared_with(employee_id, goal_id, put_goal_shared_with_request)

Update Goal Sharing

Updates which employees this goal is shared with.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.put_goal_shared_with_request import PutGoalSharedWithRequest
from bamboohr_sdk.models.transformed_api_goal import TransformedApiGoal
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
    api_instance = bamboohr_sdk.GoalsApi(api_client)
    employee_id = 'employee_id_example' # str | employeeId is the employee ID with whom the goal is associated.
    goal_id = 'goal_id_example' # str | goalId is the goal ID for the specified employee.
    put_goal_shared_with_request = bamboohr_sdk.PutGoalSharedWithRequest() # PutGoalSharedWithRequest | Employee IDs of employees with whom the goal is shared. All goal owners are considered \"shared with\".

    try:
        # Update Goal Sharing
        api_response = api_instance.put_goal_shared_with(employee_id, goal_id, put_goal_shared_with_request)
        print("The response of GoalsApi->put_goal_shared_with:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->put_goal_shared_with: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID with whom the goal is associated. | 
 **goal_id** | **str**| goalId is the goal ID for the specified employee. | 
 **put_goal_shared_with_request** | [**PutGoalSharedWithRequest**](PutGoalSharedWithRequest.md)| Employee IDs of employees with whom the goal is shared. All goal owners are considered \&quot;shared with\&quot;. | 

### Return type

[**TransformedApiGoal**](TransformedApiGoal.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response indicates that all the requested changes were made. The content of the response will be the goal response object for the specified goalId. |  -  |
**400** | The posted JSON is invalid. |  -  |
**403** | Goal is not editable or insufficient permissions. |  -  |
**404** | No goal found for the given goalId. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_goal_v1**
> TransformedApiEmployeeGoalDetails put_goal_v1(employee_id, goal_id, goal)

Update Goal

Update a goal. This version will not update a goal to contain milestones, that functionality is added in version 1.1

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.goal import Goal
from bamboohr_sdk.models.transformed_api_employee_goal_details import TransformedApiEmployeeGoalDetails
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
    api_instance = bamboohr_sdk.GoalsApi(api_client)
    employee_id = 'employee_id_example' # str | employeeId is the employee ID with whom the goal is associated.
    goal_id = 'goal_id_example' # str | goalId is the goal ID for the specified employee.
    goal = bamboohr_sdk.Goal() # Goal | Required fields: title, sharedWithEmployeeIds, dueDate. Any non-required field not provided will overwrite existing data with a NULL value.

    try:
        # Update Goal
        api_response = api_instance.put_goal_v1(employee_id, goal_id, goal)
        print("The response of GoalsApi->put_goal_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->put_goal_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID with whom the goal is associated. | 
 **goal_id** | **str**| goalId is the goal ID for the specified employee. | 
 **goal** | [**Goal**](Goal.md)| Required fields: title, sharedWithEmployeeIds, dueDate. Any non-required field not provided will overwrite existing data with a NULL value. | 

### Return type

[**TransformedApiEmployeeGoalDetails**](TransformedApiEmployeeGoalDetails.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response indicates that all the requested changes were made. The content of the response will be the goal response object for the specified goalId. |  -  |
**400** | The posted JSON is invalid. |  -  |
**403** | Goal is not editable or insufficient permissions. |  -  |
**404** | The goal specified by the given goalId was not found. |  -  |
**500** | If there was a problem updating the goal. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_goal_v1_1**
> TransformedApiEmployeeGoalDetails put_goal_v1_1(employee_id, goal_id, put_goal_v11_request)

Update Goal v1.1

Update a goal. Version 1.1 allows the updating of the milestones contained within the goal, unlike Version 1.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.put_goal_v11_request import PutGoalV11Request
from bamboohr_sdk.models.transformed_api_employee_goal_details import TransformedApiEmployeeGoalDetails
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
    api_instance = bamboohr_sdk.GoalsApi(api_client)
    employee_id = 56 # int | employeeId is the employee ID with whom the goal is associated.
    goal_id = 56 # int | goalId is the goal ID for the specified employee.
    put_goal_v11_request = bamboohr_sdk.PutGoalV11Request() # PutGoalV11Request | Required fields: title, sharedWithEmployeeIds, dueDate. Any non-required field not provided will overwrite existing data with a NULL value.

    try:
        # Update Goal v1.1
        api_response = api_instance.put_goal_v1_1(employee_id, goal_id, put_goal_v11_request)
        print("The response of GoalsApi->put_goal_v1_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->put_goal_v1_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| employeeId is the employee ID with whom the goal is associated. | 
 **goal_id** | **int**| goalId is the goal ID for the specified employee. | 
 **put_goal_v11_request** | [**PutGoalV11Request**](PutGoalV11Request.md)| Required fields: title, sharedWithEmployeeIds, dueDate. Any non-required field not provided will overwrite existing data with a NULL value. | 

### Return type

[**TransformedApiEmployeeGoalDetails**](TransformedApiEmployeeGoalDetails.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response indicates that all the requested changes were made. The content of the response will be the goal response object for the specified goalId. |  -  |
**400** | The posted JSON is invalid. |  -  |
**403** | Goal is not editable or insufficient permissions. |  -  |
**404** | The goal specified by the given goalId was not found. |  -  |
**500** | Something went wrong editing your goal. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

