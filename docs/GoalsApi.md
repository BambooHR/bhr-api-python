# bamboohr_sdk.GoalsApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_goal**](GoalsApi.md#close_goal) | **POST** /api/v1/performance/employees/{employeeId}/goals/{goalId}/close | Close Goal
[**create_goal**](GoalsApi.md#create_goal) | **POST** /api/v1/performance/employees/{employeeId}/goals | Create Goal
[**create_goal_comment**](GoalsApi.md#create_goal_comment) | **POST** /api/v1/performance/employees/{employeeId}/goals/{goalId}/comments | Create Goal Comment
[**delete_goal**](GoalsApi.md#delete_goal) | **DELETE** /api/v1/performance/employees/{employeeId}/goals/{goalId} | Delete Goal
[**delete_goal_comment**](GoalsApi.md#delete_goal_comment) | **DELETE** /api/v1/performance/employees/{employeeId}/goals/{goalId}/comments/{commentId} | Delete Goal Comment
[**get_alignable_goal_options**](GoalsApi.md#get_alignable_goal_options) | **GET** /api/v1/performance/employees/{employeeId}/goals/alignmentOptions | Get Alignable Goal Options
[**get_goal_aggregate**](GoalsApi.md#get_goal_aggregate) | **GET** /api/v1/performance/employees/{employeeId}/goals/{goalId}/aggregate | Get Goal Aggregate
[**get_goal_creation_permission**](GoalsApi.md#get_goal_creation_permission) | **GET** /api/v1/performance/employees/{employeeId}/goals/canCreateGoals | Get Goal Creation Permission
[**get_goals_aggregate_v1**](GoalsApi.md#get_goals_aggregate_v1) | **GET** /api/v1/performance/employees/{employeeId}/goals/aggregate | Get Goals Aggregate (v1)
[**get_goals_aggregate_v1_1**](GoalsApi.md#get_goals_aggregate_v1_1) | **GET** /api/v1_1/performance/employees/{employeeId}/goals/aggregate | Get Goals Aggregate (v1.1)
[**get_goals_aggregate_v1_2**](GoalsApi.md#get_goals_aggregate_v1_2) | **GET** /api/v1_2/performance/employees/{employeeId}/goals/aggregate | Get Goals Aggregate (v1.2)
[**get_goals_filters_v1**](GoalsApi.md#get_goals_filters_v1) | **GET** /api/v1/performance/employees/{employeeId}/goals/filters | Get Goal Filters (v1)
[**get_goals_filters_v1_1**](GoalsApi.md#get_goals_filters_v1_1) | **GET** /api/v1_1/performance/employees/{employeeId}/goals/filters | Get Goal Filters (v1.1)
[**get_goals_filters_v1_2**](GoalsApi.md#get_goals_filters_v1_2) | **GET** /api/v1_2/performance/employees/{employeeId}/goals/filters | Get Goal Filters (v1.2)
[**list_goal_comments**](GoalsApi.md#list_goal_comments) | **GET** /api/v1/performance/employees/{employeeId}/goals/{goalId}/comments | List Goal Comments
[**list_goal_share_options**](GoalsApi.md#list_goal_share_options) | **GET** /api/v1/performance/employees/{employeeId}/goals/shareOptions | List Goal Sharing Options
[**list_goals**](GoalsApi.md#list_goals) | **GET** /api/v1/performance/employees/{employeeId}/goals | List Goals
[**reopen_goal**](GoalsApi.md#reopen_goal) | **POST** /api/v1/performance/employees/{employeeId}/goals/{goalId}/reopen | Reopen Goal
[**update_goal_comment**](GoalsApi.md#update_goal_comment) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId}/comments/{commentId} | Update Goal Comment
[**update_goal_milestone_progress**](GoalsApi.md#update_goal_milestone_progress) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId}/milestones/{milestoneId}/progress | Update Milestone Progress
[**update_goal_progress**](GoalsApi.md#update_goal_progress) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId}/progress | Update Goal Progress
[**update_goal_sharing**](GoalsApi.md#update_goal_sharing) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId}/sharedWith | Update Goal Sharing
[**update_goal_v1**](GoalsApi.md#update_goal_v1) | **PUT** /api/v1/performance/employees/{employeeId}/goals/{goalId} | Update Goal (v1)
[**update_goal_v1_1**](GoalsApi.md#update_goal_v1_1) | **PUT** /api/v1_1/performance/employees/{employeeId}/goals/{goalId} | Update Goal (v1.1)


# **close_goal**
> GoalResponse close_goal(employee_id, goal_id, close_goal_request=close_goal_request)

Close Goal

Closes a goal, moving it to the closed status. An optional comment may be included in the request body to record a note at closing time. Returns the updated goal object. Validate the result using the returned `status`, `percentComplete`, and `completionDate` fields; do not rely solely on `lastChangedDateTime` as the confirmation timestamp, because it may not match the HTTP response time or may reflect BambooHR's internal timezone/update semantics. Note: Cascading goals with visible children cannot be closed.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.close_goal_request import CloseGoalRequest
from bamboohr_sdk.models.goal_response import GoalResponse
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
    close_goal_request = bamboohr_sdk.CloseGoalRequest() # CloseGoalRequest | An optional comment to record when closing the goal. (optional)

    try:
        # Close Goal
        api_response = api_instance.close_goal(employee_id, goal_id, close_goal_request=close_goal_request)
        print("The response of GoalsApi->close_goal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->close_goal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID with whom the goal is associated. | 
 **goal_id** | **str**| goalId is the goal ID for the specified employee. | 
 **close_goal_request** | [**CloseGoalRequest**](CloseGoalRequest.md)| An optional comment to record when closing the goal. | [optional] 

### Return type

[**GoalResponse**](GoalResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The goal was successfully closed. The response body contains the updated goal object. |  -  |
**400** | The request is invalid. Possible causes: the specified employee is not associated with this goal, or the goal is a cascading goal with visible children and cannot be closed. |  -  |
**403** | Goal is not editable or insufficient permissions. |  -  |
**404** | The goal specified by the given goalId was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_goal**
> TransformedApiEmployeeGoalDetails create_goal(employee_id, create_goal_request)

Create Goal

Create a new goal for an employee. To create a simple goal without milestones, omit the `milestones` field; the goal's progress can then be changed with `update-goal-progress`. To create a milestone-based goal, provide `milestones` as a non-empty array of `{ "title": string }` objects; the goal's percent complete is then derived from milestone completion and should be changed via `update-goal-milestone-progress`. Sending `milestones: null` is treated as omitted (creates a simple goal).

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.create_goal_request import CreateGoalRequest
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
    create_goal_request = bamboohr_sdk.CreateGoalRequest() # CreateGoalRequest | 

    try:
        # Create Goal
        api_response = api_instance.create_goal(employee_id, create_goal_request)
        print("The response of GoalsApi->create_goal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->create_goal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID with whom the goal is associated. | 
 **create_goal_request** | [**CreateGoalRequest**](CreateGoalRequest.md)|  | 

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
**400** | The request body is invalid or required fields are missing or malformed (e.g. invalid dueDate, percentComplete out of range, completionDate provided with a non-100 percentComplete, sharedWithEmployeeIds not an array or missing the goal owner). |  -  |
**403** | If the API user does not have permission to create a goal for this employee. |  -  |
**500** | If there was a problem creating the goal. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_goal_comment**
> GoalCommentResponse create_goal_comment(employee_id, goal_id, create_goal_comment_request)

Create Goal Comment

Creates a new comment on a goal. The goal must belong to the specified employee. Returns the newly created comment object including its assigned ID.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.create_goal_comment_request import CreateGoalCommentRequest
from bamboohr_sdk.models.goal_comment_response import GoalCommentResponse
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
    create_goal_comment_request = bamboohr_sdk.CreateGoalCommentRequest() # CreateGoalCommentRequest | 

    try:
        # Create Goal Comment
        api_response = api_instance.create_goal_comment(employee_id, goal_id, create_goal_comment_request)
        print("The response of GoalsApi->create_goal_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->create_goal_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID with whom the goal is associated. | 
 **goal_id** | **str**| goalId is the goal ID for the specified employee. | 
 **create_goal_comment_request** | [**CreateGoalCommentRequest**](CreateGoalCommentRequest.md)|  | 

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
**404** | The specified goalId was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_goal**
> delete_goal(employee_id, goal_id)

Delete Goal

Permanently deletes a goal for an employee. The goal must belong to the specified employee. Returns 204 with no response body on success. For natural-language requests that identify a goal by title or partial title, first call `list-goals` with `filter=status-all` and resolve exactly one matching goal. Do not delete if there are multiple matches or no match; ask for clarification or report that the goal was not found.

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
    goal_id = 'goal_id_example' # str | The exact goal ID for the specified employee. Do not infer this from a partial title unless you have resolved a single matching goal via `list-goals`.

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
 **goal_id** | **str**| The exact goal ID for the specified employee. Do not infer this from a partial title unless you have resolved a single matching goal via &#x60;list-goals&#x60;. | 

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

Deletes a goal comment. The comment must belong to the specified goal, and the goal must belong to the specified employee. Returns 204 with no response body on success. If the user does not provide a comment ID, first call `list-goal-comments` and select a single deletable comment (`canDelete` is true) matching the user's description. If multiple comments match or none are deletable, do not delete; ask for clarification.

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

# **get_alignable_goal_options**
> AlignmentOptionsResponse get_alignable_goal_options(employee_id, goal_id=goal_id)

Get Alignable Goal Options

Returns goals that can be used as alignment targets. When a `goalId` query parameter is provided, the currently aligned goal is included in the results even if it would otherwise be excluded. When `goalId` is omitted, returns alignment options for the API user. This endpoint is permission-sensitive: the caller may be able to view a goal through `list-goals` or `get-goal-aggregate` but still receive 403 here if they lack permission to view alignment options for the selected goal. Treat 403 as "alignment options are permission-restricted," not as proof that the goal ID is invalid.

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
    goal_id = 56 # int | Optional goal ID whose current alignment should be included in the results. Only pass a goal ID that belongs to the specified employee. If this endpoint returns 403 for an otherwise visible goal, report that alignment options are restricted by permissions rather than treating the goal ID as invalid. (optional)

    try:
        # Get Alignable Goal Options
        api_response = api_instance.get_alignable_goal_options(employee_id, goal_id=goal_id)
        print("The response of GoalsApi->get_alignable_goal_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->get_alignable_goal_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID to get alignable goal options for. | 
 **goal_id** | **int**| Optional goal ID whose current alignment should be included in the results. Only pass a goal ID that belongs to the specified employee. If this endpoint returns 403 for an otherwise visible goal, report that alignment options are restricted by permissions rather than treating the goal ID as invalid. | [optional] 

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

# **get_goal_aggregate**
> GoalAggregate get_goal_aggregate(employee_id, goal_id)

Get Goal Aggregate

Returns a single goal with its comments, alignment options, and a list of all persons who are either shared on the goal or have commented on it. Useful for rendering a full goal detail view in a single request.

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
**403** | The API user does not have permission to view this goal. |  -  |
**404** | The specified goalId was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goal_creation_permission**
> CanCreateGoalsResponse get_goal_creation_permission(employee_id)

Get Goal Creation Permission

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
        # Get Goal Creation Permission
        api_response = api_instance.get_goal_creation_permission(employee_id)
        print("The response of GoalsApi->get_goal_creation_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->get_goal_creation_permission: %s\n" % e)
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

# **get_goals_aggregate_v1**
> GoalsAggregateV1 get_goals_aggregate_v1(employee_id, filter=filter)

Get Goals Aggregate (v1)

Deprecated. Use "Get Goals Aggregate (v1.1)" instead. Provides a list of all goals, type counts, goal comment counts, and employees shared with goals for the given employee. This version of the endpoint will not return any goals with milestones. Milestone functionality for this endpoint begins in version 1.2.

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
        # Get Goals Aggregate (v1)
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
**403** | The API user does not have permission to view goals for this employee. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goals_aggregate_v1_1**
> GoalsAggregateV11 get_goals_aggregate_v1_1(employee_id, filter=filter)

Get Goals Aggregate (v1.1)

Deprecated. Use "Get Goals Aggregate (v1.2)" instead. Provides a list of all goals, type counts, filter actions, goal comment counts, and employees shared with goals for the given employee. Note: Compared to "Get Goals Aggregate (v1)", this version returns goals in the closed filter and provides filter actions for each filter. This version of the endpoint will not return any goals with milestones. Milestone functionality for this endpoint begins in version 1.2.

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
        # Get Goals Aggregate (v1.1)
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
**403** | The API user does not have permission to view goals for this employee. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goals_aggregate_v1_2**
> GoalsAggregateV12 get_goals_aggregate_v1_2(employee_id, filter=filter)

Get Goals Aggregate (v1.2)

Provides a goals dashboard for an employee: goals matching the selected filter, status filter counts/actions, comment counts, and people shared with or commenting on those goals. This v1.2 endpoint includes milestone-based goals in the returned goal list. Use the optional `filter` query parameter to control which statuses are included; use `status-all` when the user asks for a complete dashboard across active, completed, and closed goals. Note: Compared to "Get Goals Aggregate (v1.1)", this version returns goals that contain milestones.

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
    filter = 'filter_example' # str | Optional status filter for the goals collection in the aggregate response. Use `status-all` for a full dashboard across statuses; otherwise pass `status-inProgress`, `status-completed`, or `status-closed`. If omitted or invalid, defaults to the first available filter. The response's `filters` counts may include statuses beyond the selected goal list. (optional)

    try:
        # Get Goals Aggregate (v1.2)
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
 **filter** | **str**| Optional status filter for the goals collection in the aggregate response. Use &#x60;status-all&#x60; for a full dashboard across statuses; otherwise pass &#x60;status-inProgress&#x60;, &#x60;status-completed&#x60;, or &#x60;status-closed&#x60;. If omitted or invalid, defaults to the first available filter. The response&#39;s &#x60;filters&#x60; counts may include statuses beyond the selected goal list. | [optional] 

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
**403** | The API user does not have permission to view goals for this employee. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goals_filters_v1**
> GoalFiltersV1 get_goals_filters_v1(employee_id)

Get Goal Filters (v1)

Deprecated. Use "Get Goal Filters (v1.1)" instead. Get the number of goals per status for an employee. Returns a count of goals in each status (In Progress, Completed) for the specified employee. Goals with milestones are excluded from counts in this version.

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
        # Get Goal Filters (v1)
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

Get Goal Filters (v1.1)

Deprecated. Use "Get Goal Filters (v1.2)" instead. Get the number of goals per status for an employee. Note: Compared to "Get Goal Filters (v1)", this version includes actions.

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
        # Get Goal Filters (v1.1)
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
**403** | The API user does not have permission to view goals for this employee. |  -  |
**500** | Something went wrong fetching filters. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goals_filters_v1_2**
> GoalFiltersV11 get_goals_filters_v1_2(employee_id)

Get Goal Filters (v1.2)

Get the number of goals per status for an employee, including goals with milestones. Note: Compared to "Get Goal Filters (v1.1)", this version returns goals with milestones.

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
        # Get Goal Filters (v1.2)
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
**403** | The API user does not have permission to view goals for this employee. |  -  |
**500** | Something went wrong fetching filters. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_goal_comments**
> GoalCommentsResponse list_goal_comments(employee_id, goal_id)

List Goal Comments

Returns comments for a goal, including each comment's ID, author, text, creation time, and edit/delete permissions. Use this endpoint before updating or deleting a comment when the user identifies a comment by text or says "my comment" rather than providing a comment ID.

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
        # List Goal Comments
        api_response = api_instance.list_goal_comments(employee_id, goal_id)
        print("The response of GoalsApi->list_goal_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->list_goal_comments: %s\n" % e)
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

# **list_goal_share_options**
> ShareOptionsResponse list_goal_share_options(employee_id, search, limit=limit)

List Goal Sharing Options

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
        # List Goal Sharing Options
        api_response = api_instance.list_goal_share_options(employee_id, search, limit=limit)
        print("The response of GoalsApi->list_goal_share_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->list_goal_share_options: %s\n" % e)
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

# **list_goals**
> GoalsList list_goals(employee_id, filter=filter)

List Goals

Returns goals for an employee. Use this endpoint to locate goals by title before updating, commenting on, closing, reopening, or deleting them. Use `filter=status-inProgress` when the user asks for current/active goals, `filter=status-completed` for completed goals, `filter=status-closed` for closed goals, and `filter=status-all` when the user says "all goals", "including closed", or you are resolving a goal by title for a write operation where the status is unknown. If no filter is provided, closed goals are excluded. Results are capped at 50 goals; if a title lookup is ambiguous or absent, do not update or delete a different goal.

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
    filter = 'filter_example' # str | Goal status filter. Use `status-inProgress` for current active goals, `status-completed` for completed goals, `status-closed` for closed goals, and `status-all` when locating a goal by title for update/delete/reopen or when the user asks for all goals. If omitted, closed goals are excluded. Unrecognized values behave like omission. (optional)

    try:
        # List Goals
        api_response = api_instance.list_goals(employee_id, filter=filter)
        print("The response of GoalsApi->list_goals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->list_goals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID to whom the goals are assigned. | 
 **filter** | **str**| Goal status filter. Use &#x60;status-inProgress&#x60; for current active goals, &#x60;status-completed&#x60; for completed goals, &#x60;status-closed&#x60; for closed goals, and &#x60;status-all&#x60; when locating a goal by title for update/delete/reopen or when the user asks for all goals. If omitted, closed goals are excluded. Unrecognized values behave like omission. | [optional] 

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
**403** | The API user does not have permission to view goals for this employee. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reopen_goal**
> GoalResponse reopen_goal(employee_id, goal_id)

Reopen Goal

Reopens a closed goal, returning it to the in-progress status. Returns the updated goal object. Validate the result using the returned `status` and `percentComplete` fields; do not rely solely on `lastChangedDateTime` as the confirmation timestamp, because it may not match the HTTP response time or may reflect BambooHR's internal timezone/update semantics.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.goal_response import GoalResponse
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
        api_response = api_instance.reopen_goal(employee_id, goal_id)
        print("The response of GoalsApi->reopen_goal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->reopen_goal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID with whom the goal is associated. | 
 **goal_id** | **str**| goalId is the goal ID for the specified employee. | 

### Return type

[**GoalResponse**](GoalResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The goal was successfully reopened. The response body contains the updated goal object. |  -  |
**400** | The request is invalid. The specified employee is not associated with this goal. |  -  |
**403** | Goal is not editable or insufficient permissions. |  -  |
**404** | The goal specified by the given goalId was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_goal_comment**
> GoalCommentResponse update_goal_comment(employee_id, goal_id, comment_id, update_goal_comment_request)

Update Goal Comment

Updates the text of an existing goal comment. The comment must belong to the specified goal, and the goal must belong to the specified employee. Returns the updated comment object. If the user does not provide a comment ID, first call `list-goal-comments` and select a single editable comment (`canEdit` is true) matching the user's description. If multiple comments match or none are editable, do not update; ask for clarification.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.goal_comment_response import GoalCommentResponse
from bamboohr_sdk.models.update_goal_comment_request import UpdateGoalCommentRequest
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
    update_goal_comment_request = bamboohr_sdk.UpdateGoalCommentRequest() # UpdateGoalCommentRequest | 

    try:
        # Update Goal Comment
        api_response = api_instance.update_goal_comment(employee_id, goal_id, comment_id, update_goal_comment_request)
        print("The response of GoalsApi->update_goal_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->update_goal_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID with whom the goal is associated. | 
 **goal_id** | **str**| goalId is the goal ID for the specified employee. | 
 **comment_id** | **str**| commentId is the comment ID for the specified goal. | 
 **update_goal_comment_request** | [**UpdateGoalCommentRequest**](UpdateGoalCommentRequest.md)|  | 

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

# **update_goal_milestone_progress**
> TransformedApiEmployeeGoalDetails update_goal_milestone_progress(employee_id, goal_id, milestone_id, update_goal_milestone_progress_request)

Update Milestone Progress

Update the progress of a milestone in a goal. Validate the result using returned domain fields such as the milestone's `completedDateTime`, plus the goal's `status` and `percentComplete`; do not rely solely on `lastChangedDateTime` as the confirmation timestamp, because it may not match the HTTP response time or may reflect BambooHR's internal timezone/update semantics.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.transformed_api_employee_goal_details import TransformedApiEmployeeGoalDetails
from bamboohr_sdk.models.update_goal_milestone_progress_request import UpdateGoalMilestoneProgressRequest
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
    update_goal_milestone_progress_request = bamboohr_sdk.UpdateGoalMilestoneProgressRequest() # UpdateGoalMilestoneProgressRequest | 

    try:
        # Update Milestone Progress
        api_response = api_instance.update_goal_milestone_progress(employee_id, goal_id, milestone_id, update_goal_milestone_progress_request)
        print("The response of GoalsApi->update_goal_milestone_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->update_goal_milestone_progress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID to whom the goals are assigned. | 
 **goal_id** | **str**| goalId is the goal ID for the specified employee. | 
 **milestone_id** | **str**| milestoneId is the milestone ID for the specified goal. | 
 **update_goal_milestone_progress_request** | [**UpdateGoalMilestoneProgressRequest**](UpdateGoalMilestoneProgressRequest.md)|  | 

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
**200** | The milestone progress was successfully updated. The response contains the updated goal details. |  -  |
**400** | The request was invalid. Please check the request parameters and try again. |  -  |
**403** | User does not have permission to update this goal |  -  |
**404** | Goal or milestone not found |  -  |
**500** | Something went wrong updating your progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_goal_progress**
> TransformedApiEmployeeGoalDetails update_goal_progress(employee_id, goal_id, update_goal_progress_request)

Update Goal Progress

Update the progress percentage of a simple, non-milestone goal. Do not use this endpoint for goals that contain milestones; BambooHR derives percent complete for milestone-based goals from milestone completion and will reject manual percent updates with a 400 response (`UPDATE_GOAL_WITH_MILESTONE_PROGRESS_ERROR`). For milestone-based goals, use `update-goal-milestone-progress` to mark individual milestones complete or incomplete.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.transformed_api_employee_goal_details import TransformedApiEmployeeGoalDetails
from bamboohr_sdk.models.update_goal_progress_request import UpdateGoalProgressRequest
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
    update_goal_progress_request = bamboohr_sdk.UpdateGoalProgressRequest() # UpdateGoalProgressRequest | The updated progress for a simple goal. Provide `percentComplete` from 0–100. When `percentComplete` is 100, provide `completionDate`; when less than 100, omit `completionDate` or set it to null. This endpoint is rejected for goals with milestones — use `update-goal-milestone-progress` instead.

    try:
        # Update Goal Progress
        api_response = api_instance.update_goal_progress(employee_id, goal_id, update_goal_progress_request)
        print("The response of GoalsApi->update_goal_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->update_goal_progress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| employeeId is the employee ID with whom the goal is associated. | 
 **goal_id** | **int**| goalId is the goal ID for the specified employee. | 
 **update_goal_progress_request** | [**UpdateGoalProgressRequest**](UpdateGoalProgressRequest.md)| The updated progress for a simple goal. Provide &#x60;percentComplete&#x60; from 0–100. When &#x60;percentComplete&#x60; is 100, provide &#x60;completionDate&#x60;; when less than 100, omit &#x60;completionDate&#x60; or set it to null. This endpoint is rejected for goals with milestones — use &#x60;update-goal-milestone-progress&#x60; instead. | 

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
**400** | The request is invalid. Possible causes: percentComplete is out of range (0–100), the goal has milestones (use the milestone progress endpoint instead), or the specified employee is not associated with this goal. |  -  |
**403** | Goal is not editable or insufficient permissions. |  -  |
**404** | No goal found for the given goalId. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_goal_sharing**
> GoalResponse update_goal_sharing(employee_id, goal_id, update_goal_sharing_request)

Update Goal Sharing

Replaces the full list of employees this goal is shared with. The provided `sharedWithEmployeeIds` array must include the goal owner's employee ID. Returns the updated goal object.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.goal_response import GoalResponse
from bamboohr_sdk.models.update_goal_sharing_request import UpdateGoalSharingRequest
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
    update_goal_sharing_request = bamboohr_sdk.UpdateGoalSharingRequest() # UpdateGoalSharingRequest | Employee IDs of employees with whom the goal is shared. All goal owners are considered \"shared with\".

    try:
        # Update Goal Sharing
        api_response = api_instance.update_goal_sharing(employee_id, goal_id, update_goal_sharing_request)
        print("The response of GoalsApi->update_goal_sharing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->update_goal_sharing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID with whom the goal is associated. | 
 **goal_id** | **str**| goalId is the goal ID for the specified employee. | 
 **update_goal_sharing_request** | [**UpdateGoalSharingRequest**](UpdateGoalSharingRequest.md)| Employee IDs of employees with whom the goal is shared. All goal owners are considered \&quot;shared with\&quot;. | 

### Return type

[**GoalResponse**](GoalResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response indicates that all the requested changes were made. The content of the response will be the goal response object for the specified goalId. |  -  |
**400** | The request is invalid. Possible causes: sharedWithEmployeeIds is not an array, sharedWithEmployeeIds is empty, or the specified employee is not associated with this goal. |  -  |
**403** | Goal is not editable or insufficient permissions. |  -  |
**404** | No goal found for the given goalId. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_goal_v1**
> TransformedApiEmployeeGoalDetails update_goal_v1(employee_id, goal_id, update_goal_v1)

Update Goal (v1)

Deprecated. Use "Update Goal (v1.1)" instead. Update a goal. This version will not update a goal to contain milestones, that functionality is added in version 1.1.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.transformed_api_employee_goal_details import TransformedApiEmployeeGoalDetails
from bamboohr_sdk.models.update_goal_v1 import UpdateGoalV1
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
    update_goal_v1 = bamboohr_sdk.UpdateGoalV1() # UpdateGoalV1 | Required fields: title, sharedWithEmployeeIds, dueDate. Omitted optional fields overwrite existing values using the endpoint's default behavior; see individual field descriptions for details.

    try:
        # Update Goal (v1)
        api_response = api_instance.update_goal_v1(employee_id, goal_id, update_goal_v1)
        print("The response of GoalsApi->update_goal_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->update_goal_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| employeeId is the employee ID with whom the goal is associated. | 
 **goal_id** | **str**| goalId is the goal ID for the specified employee. | 
 **update_goal_v1** | [**UpdateGoalV1**](UpdateGoalV1.md)| Required fields: title, sharedWithEmployeeIds, dueDate. Omitted optional fields overwrite existing values using the endpoint&#39;s default behavior; see individual field descriptions for details. | 

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

# **update_goal_v1_1**
> TransformedApiEmployeeGoalDetails update_goal_v1_1(employee_id, goal_id, update_goal_v11_request)

Update Goal (v1.1)

Update a goal's top-level fields and optionally add or delete milestones. Milestone handling is not a full replace or upsert: objects passed in `milestones` are always added as new milestones, even if their titles match existing milestones. To keep existing milestones unchanged while editing title, description, due date, sharing, or alignment, omit the `milestones` field. To remove milestones, pass their IDs in `deletedMilestoneIds`. There is no field for editing an existing milestone title in place. Note: Compared to "Update Goal (v1)", this version adds milestone updates.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.transformed_api_employee_goal_details import TransformedApiEmployeeGoalDetails
from bamboohr_sdk.models.update_goal_v11_request import UpdateGoalV11Request
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
    update_goal_v11_request = bamboohr_sdk.UpdateGoalV11Request() # UpdateGoalV11Request | Required fields: `title`, `sharedWithEmployeeIds`, and `dueDate`. Omit optional fields that should remain unchanged. In particular, omit `milestones` unless adding new milestones; included milestones are appended, not reconciled or replaced.

    try:
        # Update Goal (v1.1)
        api_response = api_instance.update_goal_v1_1(employee_id, goal_id, update_goal_v11_request)
        print("The response of GoalsApi->update_goal_v1_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->update_goal_v1_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| employeeId is the employee ID with whom the goal is associated. | 
 **goal_id** | **int**| goalId is the goal ID for the specified employee. | 
 **update_goal_v11_request** | [**UpdateGoalV11Request**](UpdateGoalV11Request.md)| Required fields: &#x60;title&#x60;, &#x60;sharedWithEmployeeIds&#x60;, and &#x60;dueDate&#x60;. Omit optional fields that should remain unchanged. In particular, omit &#x60;milestones&#x60; unless adding new milestones; included milestones are appended, not reconciled or replaced. | 

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
**400** | The request is invalid. Possible causes: sharedWithEmployeeIds is not an array or missing the goal owner, percentComplete is out of range (0–100), the goal has milestones and percentComplete cannot be manually updated, or the goal is a cascading goal (not supported by this endpoint). |  -  |
**403** | Goal is not editable or insufficient permissions. |  -  |
**404** | The goal specified by the given goalId was not found. |  -  |
**500** | Something went wrong editing your goal. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

