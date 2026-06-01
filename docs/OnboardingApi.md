# bamboohr_sdk.OnboardingApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**caa7fc488bcfaef14125398f2ebb987d**](OnboardingApi.md#caa7fc488bcfaef14125398f2ebb987d) | **DELETE** /api/v1/new-hire-packets/{id} | Delete new hire packet
[**call_0158de7cde2a4c4cf577f0b25070d809**](OnboardingApi.md#call_0158de7cde2a4c4cf577f0b25070d809) | **GET** /api/v1/employees/{employeeId}/onboarding-experiences | List employee onboarding experiences
[**call_044949386f2d655c6a627ef53f9434b7**](OnboardingApi.md#call_044949386f2d655c6a627ef53f9434b7) | **GET** /api/v1/onboarding/new-hire-widget | Get welcome new hires widget
[**call_19c7e26a1347ae7eb22919e9b0595c19**](OnboardingApi.md#call_19c7e26a1347ae7eb22919e9b0595c19) | **POST** /api/v1/new-hire-packets/{id}/cancel | Cancel new hire packet
[**call_1ab0279d46023eb951a434f24df885f1**](OnboardingApi.md#call_1ab0279d46023eb951a434f24df885f1) | **PUT** /api/v1/new-hire-packets/{id} | Update new hire packet
[**call_288aa996aba16d7a495c62321ea999a9**](OnboardingApi.md#call_288aa996aba16d7a495c62321ea999a9) | **POST** /api/v1/employees/{employeeId}/onboarding-experiences | Create employee onboarding experience
[**call_696f0a229cdde60b733568e3c4d043d9**](OnboardingApi.md#call_696f0a229cdde60b733568e3c4d043d9) | **GET** /api/v1/new-hire-packets/{id} | Get new hire packet by id
[**call_847dd061d1d1859e7ce8cb3adfc9faf2**](OnboardingApi.md#call_847dd061d1d1859e7ce8cb3adfc9faf2) | **GET** /api/v1/employees/{employeeId}/onboarding-experiences/{onboardingExperienceId} | Get employee onboarding experience by id
[**ec1ba8e76f33960b018d0d7518fe97b5**](OnboardingApi.md#ec1ba8e76f33960b018d0d7518fe97b5) | **POST** /api/v1/new-hire-packets | Create new hire packet
[**f44b802c30cdea2b9076b3f82f99c74d**](OnboardingApi.md#f44b802c30cdea2b9076b3f82f99c74d) | **GET** /api/v1/new-hire-packets | List new hire packets
[**f49b0f1f2fb1ef2c408ba12916ee9baa**](OnboardingApi.md#f49b0f1f2fb1ef2c408ba12916ee9baa) | **POST** /api/v1/new-hire-packets/{id}/send | Send new hire packet
[**update_new_hire_packet_gtky_answer_visibility**](OnboardingApi.md#update_new_hire_packet_gtky_answer_visibility) | **PUT** /api/v1/new-hire-packets/{id}/question-visibility | Update GTKY answer visibility for a new hire packet


# **caa7fc488bcfaef14125398f2ebb987d**
> caa7fc488bcfaef14125398f2ebb987d(id)

Delete new hire packet

Deletes a new hire packet instance by primary key.

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
    api_instance = bamboohr_sdk.OnboardingApi(api_client)
    id = 56 # int | 

    try:
        # Delete new hire packet
        api_instance.caa7fc488bcfaef14125398f2ebb987d(id)
    except Exception as e:
        print("Exception when calling OnboardingApi->caa7fc488bcfaef14125398f2ebb987d: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_0158de7cde2a4c4cf577f0b25070d809**
> OnboardingExperiencesListResponse call_0158de7cde2a4c4cf577f0b25070d809(employee_id)

List employee onboarding experiences

Returns onboarding experiences for the employee when the onboarding experience phase-1 and workflow framework company toggles are enabled, and at least one OnboardingExperienceWorkflow execution is running for them. Each item is projected from the employee’s new hire packet instance row for the same public id contract (no embedded NHP payload).

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.onboarding_experiences_list_response import OnboardingExperiencesListResponse
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
    api_instance = bamboohr_sdk.OnboardingApi(api_client)
    employee_id = 56 # int | 

    try:
        # List employee onboarding experiences
        api_response = api_instance.call_0158de7cde2a4c4cf577f0b25070d809(employee_id)
        print("The response of OnboardingApi->call_0158de7cde2a4c4cf577f0b25070d809:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnboardingApi->call_0158de7cde2a4c4cf577f0b25070d809: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**|  | 

### Return type

[**OnboardingExperiencesListResponse**](OnboardingExperiencesListResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden — missing OAuth permission, onboarding experience phase-1 / workflow framework feature not enabled for the company, or caller cannot access the employee. |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_044949386f2d655c6a627ef53f9434b7**
> NewHireWidgetResponse call_044949386f2d655c6a627ef53f9434b7()

Get welcome new hires widget

Returns the upcoming-new-hires data that powers the BambooHR home "Welcome New Hires" widget. Items are ordered by most recent hire date first. The list reflects the authenticated user's new-hire-packet and company-directory access — when either is missing the response is an empty list (not 403). Sensitive contact fields (work email, home email) are never returned.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.new_hire_widget_response import NewHireWidgetResponse
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
    api_instance = bamboohr_sdk.OnboardingApi(api_client)

    try:
        # Get welcome new hires widget
        api_response = api_instance.call_044949386f2d655c6a627ef53f9434b7()
        print("The response of OnboardingApi->call_044949386f2d655c6a627ef53f9434b7:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnboardingApi->call_044949386f2d655c6a627ef53f9434b7: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NewHireWidgetResponse**](NewHireWidgetResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_19c7e26a1347ae7eb22919e9b0595c19**
> NewHirePacketPublicApi call_19c7e26a1347ae7eb22919e9b0595c19(id)

Cancel new hire packet

Cancels the new hire packet. Completed packets cannot be cancelled.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.new_hire_packet_public_api import NewHirePacketPublicApi
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
    api_instance = bamboohr_sdk.OnboardingApi(api_client)
    id = 56 # int | 

    try:
        # Cancel new hire packet
        api_response = api_instance.call_19c7e26a1347ae7eb22919e9b0595c19(id)
        print("The response of OnboardingApi->call_19c7e26a1347ae7eb22919e9b0595c19:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnboardingApi->call_19c7e26a1347ae7eb22919e9b0595c19: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**NewHirePacketPublicApi**](NewHirePacketPublicApi.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_1ab0279d46023eb951a434f24df885f1**
> NewHirePacketPublicApi call_1ab0279d46023eb951a434f24df885f1(id, new_hire_packet_public_api_writable_body)

Update new hire packet

Updates an existing new hire packet instance. Sent, viewed, and completed timestamps are not changed through this endpoint.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.new_hire_packet_public_api import NewHirePacketPublicApi
from bamboohr_sdk.models.new_hire_packet_public_api_writable_body import NewHirePacketPublicApiWritableBody
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
    api_instance = bamboohr_sdk.OnboardingApi(api_client)
    id = 56 # int | 
    new_hire_packet_public_api_writable_body = bamboohr_sdk.NewHirePacketPublicApiWritableBody() # NewHirePacketPublicApiWritableBody | 

    try:
        # Update new hire packet
        api_response = api_instance.call_1ab0279d46023eb951a434f24df885f1(id, new_hire_packet_public_api_writable_body)
        print("The response of OnboardingApi->call_1ab0279d46023eb951a434f24df885f1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnboardingApi->call_1ab0279d46023eb951a434f24df885f1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **new_hire_packet_public_api_writable_body** | [**NewHirePacketPublicApiWritableBody**](NewHirePacketPublicApiWritableBody.md)|  | 

### Return type

[**NewHirePacketPublicApi**](NewHirePacketPublicApi.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_288aa996aba16d7a495c62321ea999a9**
> OnboardingExperiencePublicApi call_288aa996aba16d7a495c62321ea999a9(employee_id, model288aa996aba16d7a495c62321ea999a9_request=model288aa996aba16d7a495c62321ea999a9_request)

Create employee onboarding experience

Creates (starts) an onboarding experience workflow for the employee’s existing new hire packet instance. Requires the onboarding experience phase-1 and workflow framework company toggles. Optional sentDateTime may be supplied for workflow idempotency (ISO 8601 or legacy datetime string accepted when non-empty).

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.model288aa996aba16d7a495c62321ea999a9_request import Model288aa996aba16d7a495c62321ea999a9Request
from bamboohr_sdk.models.onboarding_experience_public_api import OnboardingExperiencePublicApi
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
    api_instance = bamboohr_sdk.OnboardingApi(api_client)
    employee_id = 56 # int | 
    model288aa996aba16d7a495c62321ea999a9_request = bamboohr_sdk.Model288aa996aba16d7a495c62321ea999a9Request() # Model288aa996aba16d7a495c62321ea999a9Request |  (optional)

    try:
        # Create employee onboarding experience
        api_response = api_instance.call_288aa996aba16d7a495c62321ea999a9(employee_id, model288aa996aba16d7a495c62321ea999a9_request=model288aa996aba16d7a495c62321ea999a9_request)
        print("The response of OnboardingApi->call_288aa996aba16d7a495c62321ea999a9:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnboardingApi->call_288aa996aba16d7a495c62321ea999a9: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**|  | 
 **model288aa996aba16d7a495c62321ea999a9_request** | [**Model288aa996aba16d7a495c62321ea999a9Request**](Model288aa996aba16d7a495c62321ea999a9Request.md)|  | [optional] 

### Return type

[**OnboardingExperiencePublicApi**](OnboardingExperiencePublicApi.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request |  -  |
**403** | Forbidden — missing OAuth permission, or onboarding experience phase-1 / workflow framework feature not enabled for the company. |  -  |
**409** | Conflict — an onboarding experience workflow already exists for this employee. |  -  |
**422** | Workflow instance could not be started or is not running. |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_696f0a229cdde60b733568e3c4d043d9**
> NewHirePacketPublicApi call_696f0a229cdde60b733568e3c4d043d9(id)

Get new hire packet by id

Returns a single new hire packet instance with a derived status. Sub-resources (sections, tasks, questions, GTKY) are not included.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.new_hire_packet_public_api import NewHirePacketPublicApi
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
    api_instance = bamboohr_sdk.OnboardingApi(api_client)
    id = 56 # int | 

    try:
        # Get new hire packet by id
        api_response = api_instance.call_696f0a229cdde60b733568e3c4d043d9(id)
        print("The response of OnboardingApi->call_696f0a229cdde60b733568e3c4d043d9:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnboardingApi->call_696f0a229cdde60b733568e3c4d043d9: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**NewHirePacketPublicApi**](NewHirePacketPublicApi.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_847dd061d1d1859e7ce8cb3adfc9faf2**
> OnboardingExperiencePublicApi call_847dd061d1d1859e7ce8cb3adfc9faf2(employee_id, onboarding_experience_id)

Get employee onboarding experience by id

Returns a single onboarding experience when the onboarding experience phase-1 and workflow framework company toggles are enabled, the employee has at least one running OnboardingExperienceWorkflow (execution status RUNNING), the path id matches their current new hire packet instance id, and the row belongs to the employee. NHP fields are referenced by id only.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.onboarding_experience_public_api import OnboardingExperiencePublicApi
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
    api_instance = bamboohr_sdk.OnboardingApi(api_client)
    employee_id = 56 # int | 
    onboarding_experience_id = 56 # int | 

    try:
        # Get employee onboarding experience by id
        api_response = api_instance.call_847dd061d1d1859e7ce8cb3adfc9faf2(employee_id, onboarding_experience_id)
        print("The response of OnboardingApi->call_847dd061d1d1859e7ce8cb3adfc9faf2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnboardingApi->call_847dd061d1d1859e7ce8cb3adfc9faf2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**|  | 
 **onboarding_experience_id** | **int**|  | 

### Return type

[**OnboardingExperiencePublicApi**](OnboardingExperiencePublicApi.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden — missing OAuth permission, onboarding experience phase-1 / workflow framework feature not enabled for the company, or caller cannot access the employee. |  -  |
**404** | Not found — no matching running workflow, id does not match the employee’s current packet instance, or no such row. |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ec1ba8e76f33960b018d0d7518fe97b5**
> NewHirePacketPublicApi ec1ba8e76f33960b018d0d7518fe97b5(ec1ba8e76f33960b018d0d7518fe97b5_request)

Create new hire packet

Creates a new hire packet instance (draft) for an employee. Company configuration is applied for default inclusion flags.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.ec1ba8e76f33960b018d0d7518fe97b5_request import Ec1ba8e76f33960b018d0d7518fe97b5Request
from bamboohr_sdk.models.new_hire_packet_public_api import NewHirePacketPublicApi
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
    api_instance = bamboohr_sdk.OnboardingApi(api_client)
    ec1ba8e76f33960b018d0d7518fe97b5_request = bamboohr_sdk.Ec1ba8e76f33960b018d0d7518fe97b5Request() # Ec1ba8e76f33960b018d0d7518fe97b5Request | 

    try:
        # Create new hire packet
        api_response = api_instance.ec1ba8e76f33960b018d0d7518fe97b5(ec1ba8e76f33960b018d0d7518fe97b5_request)
        print("The response of OnboardingApi->ec1ba8e76f33960b018d0d7518fe97b5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnboardingApi->ec1ba8e76f33960b018d0d7518fe97b5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ec1ba8e76f33960b018d0d7518fe97b5_request** | [**Ec1ba8e76f33960b018d0d7518fe97b5Request**](Ec1ba8e76f33960b018d0d7518fe97b5Request.md)|  | 

### Return type

[**NewHirePacketPublicApi**](NewHirePacketPublicApi.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **f44b802c30cdea2b9076b3f82f99c74d**
> NewHirePacketsListResponse f44b802c30cdea2b9076b3f82f99c74d(page=page, page_size=page_size)

List new hire packets

Returns a paginated list of new hire packet instances for the company. Each item is a flat summary (no sections, tasks, questions, or GTKY recipients).

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.new_hire_packets_list_response import NewHirePacketsListResponse
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
    api_instance = bamboohr_sdk.OnboardingApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)

    try:
        # List new hire packets
        api_response = api_instance.f44b802c30cdea2b9076b3f82f99c74d(page=page, page_size=page_size)
        print("The response of OnboardingApi->f44b802c30cdea2b9076b3f82f99c74d:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnboardingApi->f44b802c30cdea2b9076b3f82f99c74d: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**NewHirePacketsListResponse**](NewHirePacketsListResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **f49b0f1f2fb1ef2c408ba12916ee9baa**
> NewHirePacketPublicApi f49b0f1f2fb1ef2c408ba12916ee9baa(id)

Send new hire packet

Sends the new hire packet for that packet's employee (email or onboarding experience workflow, depending on company configuration). The packet must be in draft state.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.new_hire_packet_public_api import NewHirePacketPublicApi
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
    api_instance = bamboohr_sdk.OnboardingApi(api_client)
    id = 56 # int | 

    try:
        # Send new hire packet
        api_response = api_instance.f49b0f1f2fb1ef2c408ba12916ee9baa(id)
        print("The response of OnboardingApi->f49b0f1f2fb1ef2c408ba12916ee9baa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnboardingApi->f49b0f1f2fb1ef2c408ba12916ee9baa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**NewHirePacketPublicApi**](NewHirePacketPublicApi.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_new_hire_packet_gtky_answer_visibility**
> NewHirePacketGtkyAnswerVisibilityResponse update_new_hire_packet_gtky_answer_visibility(id, new_hire_packet_gtky_answer_visibility_request)

Update GTKY answer visibility for a new hire packet

Shows or hides get-to-know-you (GTKY) question answers for the packet. Omit questionIds to toggle all answers (same as the legacy BFF POST /onboarding/questions/visibility/{newHirePacketId} with a visible query flag). Send questionIds to toggle only specific personal questions linked to this new hire packet. Requires the same edit access as other NHP writes. When the employee has a hire date set, updates are rejected once the company-local calendar date is on or after that date (same rule as GET /onboarding/questions/{newHirePacketId}, which redirects to expired in that case). Draft employees without a hire date are not blocked.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.new_hire_packet_gtky_answer_visibility_request import NewHirePacketGtkyAnswerVisibilityRequest
from bamboohr_sdk.models.new_hire_packet_gtky_answer_visibility_response import NewHirePacketGtkyAnswerVisibilityResponse
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
    api_instance = bamboohr_sdk.OnboardingApi(api_client)
    id = 56 # int | 
    new_hire_packet_gtky_answer_visibility_request = bamboohr_sdk.NewHirePacketGtkyAnswerVisibilityRequest() # NewHirePacketGtkyAnswerVisibilityRequest | 

    try:
        # Update GTKY answer visibility for a new hire packet
        api_response = api_instance.update_new_hire_packet_gtky_answer_visibility(id, new_hire_packet_gtky_answer_visibility_request)
        print("The response of OnboardingApi->update_new_hire_packet_gtky_answer_visibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnboardingApi->update_new_hire_packet_gtky_answer_visibility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **new_hire_packet_gtky_answer_visibility_request** | [**NewHirePacketGtkyAnswerVisibilityRequest**](NewHirePacketGtkyAnswerVisibilityRequest.md)|  | 

### Return type

[**NewHirePacketGtkyAnswerVisibilityResponse**](NewHirePacketGtkyAnswerVisibilityResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success — returns the current visibility for each GTKY answer row on the packet. |  -  |
**400** | Bad request — invalid body (e.g. hidden type, questionIds shape, ids not linked to this packet), or visibility change not allowed on or after the employee hire date when a hire date is set |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

