# bamboohr_sdk.TotalRewardsApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_total_rewards_employees**](TotalRewardsApi.md#add_total_rewards_employees) | **POST** /api/v1/compensation/total_rewards/employees | Add Employees to Total Rewards
[**check_total_rewards_profile**](TotalRewardsApi.md#check_total_rewards_profile) | **GET** /api/v1/compensation/total_rewards/{employeeId} | Check Total Rewards Profile Availability
[**get_total_rewards_printable_statement**](TotalRewardsApi.md#get_total_rewards_printable_statement) | **GET** /api/v1/compensation/total_rewards/{employeeId}/printable | Get Printable Total Rewards Statement
[**get_total_rewards_statement**](TotalRewardsApi.md#get_total_rewards_statement) | **GET** /api/v1/compensation/total_rewards/{employeeId}/statement | Get Total Rewards Statement
[**remove_total_rewards_custom_disclaimer**](TotalRewardsApi.md#remove_total_rewards_custom_disclaimer) | **DELETE** /api/v1/compensation/total_rewards/custom_disclaimer | Remove Total Rewards Custom Disclaimer
[**remove_total_rewards_employees**](TotalRewardsApi.md#remove_total_rewards_employees) | **DELETE** /api/v1/compensation/total_rewards/employees | Remove Employees from Total Rewards
[**set_total_rewards_custom_disclaimer**](TotalRewardsApi.md#set_total_rewards_custom_disclaimer) | **PUT** /api/v1/compensation/total_rewards/custom_disclaimer | Set Total Rewards Custom Disclaimer
[**set_total_rewards_onboarding_step**](TotalRewardsApi.md#set_total_rewards_onboarding_step) | **PUT** /api/v1/compensation/total_rewards/onboarding/{stepName} | Set Total Rewards Onboarding Step Status


# **add_total_rewards_employees**
> add_total_rewards_employees(add_total_rewards_employees_request)

Add Employees to Total Rewards

Add employees to Total Rewards. Each employee will have a Total Rewards profile created and will be notified if they are active users.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.add_total_rewards_employees_request import AddTotalRewardsEmployeesRequest
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TotalRewardsApi(api_client)
    add_total_rewards_employees_request = bamboohr_sdk.AddTotalRewardsEmployeesRequest() # AddTotalRewardsEmployeesRequest | 

    try:
        # Add Employees to Total Rewards
        api_instance.add_total_rewards_employees(add_total_rewards_employees_request)
    except Exception as e:
        print("Exception when calling TotalRewardsApi->add_total_rewards_employees: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_total_rewards_employees_request** | [**AddTotalRewardsEmployeesRequest**](AddTotalRewardsEmployeesRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Employees successfully added to Total Rewards. |  -  |
**400** | Invalid request (e.g. missing or empty employeeIds). |  -  |
**403** | The authenticated caller lacks permission to manage Total Rewards employees. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_total_rewards_profile**
> check_total_rewards_profile(employee_id)

Check Total Rewards Profile Availability

Check if the given employee has an active Total Rewards profile and the current user has permission to view it. Returns 204 when the employee has a profile and the user is authorized; 404 if the profile does not exist or the user lacks access.

### Example

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TotalRewardsApi(api_client)
    employee_id = 'employee_id_example' # str | The ID of the employee to check.

    try:
        # Check Total Rewards Profile Availability
        api_instance.check_total_rewards_profile(employee_id)
    except Exception as e:
        print("Exception when calling TotalRewardsApi->check_total_rewards_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| The ID of the employee to check. | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Employee has an active Total Rewards profile and the user can view it. |  -  |
**404** | Employee does not have a Total Rewards profile or the user lacks permission. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_total_rewards_printable_statement**
> get_total_rewards_printable_statement(employee_id, multiplier=multiplier, year=year)

Get Printable Total Rewards Statement

Generate and return a PDF printable version of the employee's Total Rewards statement.

### Example

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TotalRewardsApi(api_client)
    employee_id = 'employee_id_example' # str | The ID of the employee.
    multiplier = 3.4 # float | Hours-per-week multiplier for annualizing hourly pay. (optional)
    year = 56 # int | Statement year. Defaults to the current year when omitted. (optional)

    try:
        # Get Printable Total Rewards Statement
        api_instance.get_total_rewards_printable_statement(employee_id, multiplier=multiplier, year=year)
    except Exception as e:
        print("Exception when calling TotalRewardsApi->get_total_rewards_printable_statement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| The ID of the employee. | 
 **multiplier** | **float**| Hours-per-week multiplier for annualizing hourly pay. | [optional] 
 **year** | **int**| Statement year. Defaults to the current year when omitted. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PDF document streamed with Content-Disposition: attachment. |  -  |
**400** | Invalid argument (e.g. bad year or multiplier). |  -  |
**403** | The authenticated caller lacks permission to view this employee&#39;s Total Rewards statement. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_total_rewards_statement**
> TotalRewardsEmployeeStatement get_total_rewards_statement(employee_id)

Get Total Rewards Statement

Returns the full Total Rewards statement for the given employee, including compensation, benefits, bonuses, equity, reimbursements, and time-off data.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.total_rewards_employee_statement import TotalRewardsEmployeeStatement
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TotalRewardsApi(api_client)
    employee_id = 'employee_id_example' # str | The ID of the employee.

    try:
        # Get Total Rewards Statement
        api_response = api_instance.get_total_rewards_statement(employee_id)
        print("The response of TotalRewardsApi->get_total_rewards_statement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TotalRewardsApi->get_total_rewards_statement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**| The ID of the employee. | 

### Return type

[**TotalRewardsEmployeeStatement**](TotalRewardsEmployeeStatement.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Total Rewards statement for the employee. |  -  |
**403** | The authenticated caller lacks permission to view this employee&#39;s Total Rewards statement. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_total_rewards_custom_disclaimer**
> remove_total_rewards_custom_disclaimer()

Remove Total Rewards Custom Disclaimer

Remove the company-wide Total Rewards custom disclaimer. After removal, the default disclaimer will be shown on employee statements.

### Example

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TotalRewardsApi(api_client)

    try:
        # Remove Total Rewards Custom Disclaimer
        api_instance.remove_total_rewards_custom_disclaimer()
    except Exception as e:
        print("Exception when calling TotalRewardsApi->remove_total_rewards_custom_disclaimer: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom disclaimer removed successfully. |  -  |
**403** | The authenticated caller lacks permission to manage Total Rewards settings. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_total_rewards_employees**
> remove_total_rewards_employees(remove_total_rewards_employees_request)

Remove Employees from Total Rewards

Remove employees from Total Rewards. Their Total Rewards profiles will be deleted.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.remove_total_rewards_employees_request import RemoveTotalRewardsEmployeesRequest
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TotalRewardsApi(api_client)
    remove_total_rewards_employees_request = bamboohr_sdk.RemoveTotalRewardsEmployeesRequest() # RemoveTotalRewardsEmployeesRequest | 

    try:
        # Remove Employees from Total Rewards
        api_instance.remove_total_rewards_employees(remove_total_rewards_employees_request)
    except Exception as e:
        print("Exception when calling TotalRewardsApi->remove_total_rewards_employees: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_total_rewards_employees_request** | [**RemoveTotalRewardsEmployeesRequest**](RemoveTotalRewardsEmployeesRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Employees successfully removed from Total Rewards. |  -  |
**400** | Invalid request (e.g. missing or empty employeeIds). |  -  |
**403** | The authenticated caller lacks permission to manage Total Rewards employees. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_total_rewards_custom_disclaimer**
> set_total_rewards_custom_disclaimer(set_total_rewards_custom_disclaimer_request)

Set Total Rewards Custom Disclaimer

Set the company-wide Total Rewards custom disclaimer text shown on employee statements.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.set_total_rewards_custom_disclaimer_request import SetTotalRewardsCustomDisclaimerRequest
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TotalRewardsApi(api_client)
    set_total_rewards_custom_disclaimer_request = bamboohr_sdk.SetTotalRewardsCustomDisclaimerRequest() # SetTotalRewardsCustomDisclaimerRequest | 

    try:
        # Set Total Rewards Custom Disclaimer
        api_instance.set_total_rewards_custom_disclaimer(set_total_rewards_custom_disclaimer_request)
    except Exception as e:
        print("Exception when calling TotalRewardsApi->set_total_rewards_custom_disclaimer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_total_rewards_custom_disclaimer_request** | [**SetTotalRewardsCustomDisclaimerRequest**](SetTotalRewardsCustomDisclaimerRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom disclaimer updated successfully. |  -  |
**403** | The authenticated caller lacks permission to manage Total Rewards settings. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_total_rewards_onboarding_step**
> TotalRewardsOnboardingStep set_total_rewards_onboarding_step(step_name, set_total_rewards_onboarding_step_request)

Set Total Rewards Onboarding Step Status

Set a Total Rewards onboarding step to completed or incomplete. Valid step names are defined by the Total Rewards onboarding configuration.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.set_total_rewards_onboarding_step_request import SetTotalRewardsOnboardingStepRequest
from bamboohr_sdk.models.total_rewards_onboarding_step import TotalRewardsOnboardingStep
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.TotalRewardsApi(api_client)
    step_name = 'step_name_example' # str | Name of the onboarding step.
    set_total_rewards_onboarding_step_request = bamboohr_sdk.SetTotalRewardsOnboardingStepRequest() # SetTotalRewardsOnboardingStepRequest | 

    try:
        # Set Total Rewards Onboarding Step Status
        api_response = api_instance.set_total_rewards_onboarding_step(step_name, set_total_rewards_onboarding_step_request)
        print("The response of TotalRewardsApi->set_total_rewards_onboarding_step:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TotalRewardsApi->set_total_rewards_onboarding_step: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **step_name** | **str**| Name of the onboarding step. | 
 **set_total_rewards_onboarding_step_request** | [**SetTotalRewardsOnboardingStepRequest**](SetTotalRewardsOnboardingStepRequest.md)|  | 

### Return type

[**TotalRewardsOnboardingStep**](TotalRewardsOnboardingStep.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Onboarding step status updated successfully. |  -  |
**400** | Invalid argument (e.g. invalid step name or non-boolean completed value). |  -  |
**403** | The authenticated caller lacks permission to manage Total Rewards onboarding. |  -  |
**500** | Unexpected server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

