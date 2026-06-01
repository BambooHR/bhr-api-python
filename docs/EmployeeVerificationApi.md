# bamboohr_sdk.EmployeeVerificationApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_employee_verification_integration**](EmployeeVerificationApi.md#get_employee_verification_integration) | **GET** /api/v1/employee-verifications/integration | Get employee verification integration status
[**list_employee_verifications_by_employee**](EmployeeVerificationApi.md#list_employee_verifications_by_employee) | **GET** /api/v1/employee-verifications/employees/{employeeId} | List employee verification records for an employee
[**send_employee_verification_lifecycle_email_by_user**](EmployeeVerificationApi.md#send_employee_verification_lifecycle_email_by_user) | **POST** /api/v1/employee-verifications/users/{userId}/send-email | Send employee verification lifecycle email by user and email type
[**update_employee_verification**](EmployeeVerificationApi.md#update_employee_verification) | **PUT** /api/v1/employee-verifications/employees/{employeeId}/{verificationId} | Update an employee verification record
[**update_employee_verification_integration**](EmployeeVerificationApi.md#update_employee_verification_integration) | **PUT** /api/v1/employee-verifications/integration | Enable or disable the employee verification integration


# **get_employee_verification_integration**
> EmployeeVerificationIntegrationResponse get_employee_verification_integration()

Get employee verification integration status

Returns the install state and partner metadata for the company's employee verification integration. Scoped to the authenticated OAuth company context. The `enabled` flag reflects whether the partner app is installed and usable; `integrationType` identifies the configured verification partner.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.employee_verification_integration_response import EmployeeVerificationIntegrationResponse
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
    api_instance = bamboohr_sdk.EmployeeVerificationApi(api_client)

    try:
        # Get employee verification integration status
        api_response = api_instance.get_employee_verification_integration()
        print("The response of EmployeeVerificationApi->get_employee_verification_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeVerificationApi->get_employee_verification_integration: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**EmployeeVerificationIntegrationResponse**](EmployeeVerificationIntegrationResponse.md)

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

# **list_employee_verifications_by_employee**
> EmployeeVerificationsListResponse list_employee_verifications_by_employee(employee_id)

List employee verification records for an employee

Returns every employee verification row for the given employee (including archived), newest first. Intended for admin-level API consumers with the employee verifications OAuth scope; callers must have onboarding access and permission to view the employee (same rules as the active-verification employee verification API), except when the OAuth context is the employee themselves.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.employee_verifications_list_response import EmployeeVerificationsListResponse
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
    api_instance = bamboohr_sdk.EmployeeVerificationApi(api_client)
    employee_id = 56 # int | Company employee id whose verification history is returned.

    try:
        # List employee verification records for an employee
        api_response = api_instance.list_employee_verifications_by_employee(employee_id)
        print("The response of EmployeeVerificationApi->list_employee_verifications_by_employee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeVerificationApi->list_employee_verifications_by_employee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| Company employee id whose verification history is returned. | 

### Return type

[**EmployeeVerificationsListResponse**](EmployeeVerificationsListResponse.md)

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

# **send_employee_verification_lifecycle_email_by_user**
> EmployeeVerificationLifecycleEmailAcceptedResponse send_employee_verification_lifecycle_email_by_user(user_id, send_employee_verification_lifecycle_email_by_user_request)

Send employee verification lifecycle email by user and email type

Accepts a Bamboo `userId` (path) and an `emailType` (body) and queues the corresponding employee verification lifecycle email—the same templates as the in-app auth listener (`signup_survey` after signup, `app_installed` after the integration app is installed). Delivered to the company owner contact with template context for that user id. Not an employee I-9 reminder. Requires the employee verification integration enabled, onboarding edit access, and `employee_verifications.write`.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.employee_verification_lifecycle_email_accepted_response import EmployeeVerificationLifecycleEmailAcceptedResponse
from bamboohr_sdk.models.send_employee_verification_lifecycle_email_by_user_request import SendEmployeeVerificationLifecycleEmailByUserRequest
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
    api_instance = bamboohr_sdk.EmployeeVerificationApi(api_client)
    user_id = 56 # int | Bamboo user id for the requesting user in the email template (same role as the listener’s event user id). Together with body `emailType`, selects which verification email to send.
    send_employee_verification_lifecycle_email_by_user_request = bamboohr_sdk.SendEmployeeVerificationLifecycleEmailByUserRequest() # SendEmployeeVerificationLifecycleEmailByUserRequest | 

    try:
        # Send employee verification lifecycle email by user and email type
        api_response = api_instance.send_employee_verification_lifecycle_email_by_user(user_id, send_employee_verification_lifecycle_email_by_user_request)
        print("The response of EmployeeVerificationApi->send_employee_verification_lifecycle_email_by_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeVerificationApi->send_employee_verification_lifecycle_email_by_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Bamboo user id for the requesting user in the email template (same role as the listener’s event user id). Together with body &#x60;emailType&#x60;, selects which verification email to send. | 
 **send_employee_verification_lifecycle_email_by_user_request** | [**SendEmployeeVerificationLifecycleEmailByUserRequest**](SendEmployeeVerificationLifecycleEmailByUserRequest.md)|  | 

### Return type

[**EmployeeVerificationLifecycleEmailAcceptedResponse**](EmployeeVerificationLifecycleEmailAcceptedResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request accepted; email has been queued for delivery. |  -  |
**400** | Bad request (invalid body, unknown user id, or integration disabled) |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_employee_verification**
> EmployeeVerificationUpdateResponse update_employee_verification(employee_id, verification_id, update_employee_verification_request)

Update an employee verification record

Partial update of a single employee verification row. Any field omitted from the request body is left unchanged. Returns 404 when the verification id does not exist or does not belong to {employeeId}. Most verification updates flow in via partner webhooks; this endpoint exists for admin-level integrations that need to correct or annotate a record out-of-band, and requires onboarding view-and-edit permission on the employee.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.employee_verification_update_response import EmployeeVerificationUpdateResponse
from bamboohr_sdk.models.update_employee_verification_request import UpdateEmployeeVerificationRequest
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
    api_instance = bamboohr_sdk.EmployeeVerificationApi(api_client)
    employee_id = 56 # int | Company employee id that owns the verification row.
    verification_id = 56 # int | Identifier of the verification record to update.
    update_employee_verification_request = bamboohr_sdk.UpdateEmployeeVerificationRequest() # UpdateEmployeeVerificationRequest | Fields to update on the verification record. At least one field must be supplied.

    try:
        # Update an employee verification record
        api_response = api_instance.update_employee_verification(employee_id, verification_id, update_employee_verification_request)
        print("The response of EmployeeVerificationApi->update_employee_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeVerificationApi->update_employee_verification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| Company employee id that owns the verification row. | 
 **verification_id** | **int**| Identifier of the verification record to update. | 
 **update_employee_verification_request** | [**UpdateEmployeeVerificationRequest**](UpdateEmployeeVerificationRequest.md)| Fields to update on the verification record. At least one field must be supplied. | 

### Return type

[**EmployeeVerificationUpdateResponse**](EmployeeVerificationUpdateResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success — returns the updated verification record. |  -  |
**400** | Invalid request body (unknown enum value or no updatable fields supplied). |  -  |
**403** | Forbidden |  -  |
**404** | Verification id not found for the supplied employee. |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_employee_verification_integration**
> EmployeeVerificationIntegrationResponse update_employee_verification_integration(update_employee_verification_integration_request)

Enable or disable the employee verification integration

Enables or disables the company's employee verification integration. Enabling installs the configured partner app and schedules the daily sync; the company must have a valid US work location before enabling, otherwise a 400 is returned. Disabling tears down the partner app. The call is idempotent: a request to enable when already enabled (or disable when already disabled) returns 200 with the current state. Requires the employee_verifications.write OAuth scope, intended for admin-level API consumers.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.employee_verification_integration_response import EmployeeVerificationIntegrationResponse
from bamboohr_sdk.models.update_employee_verification_integration_request import UpdateEmployeeVerificationIntegrationRequest
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
    api_instance = bamboohr_sdk.EmployeeVerificationApi(api_client)
    update_employee_verification_integration_request = bamboohr_sdk.UpdateEmployeeVerificationIntegrationRequest() # UpdateEmployeeVerificationIntegrationRequest | 

    try:
        # Enable or disable the employee verification integration
        api_response = api_instance.update_employee_verification_integration(update_employee_verification_integration_request)
        print("The response of EmployeeVerificationApi->update_employee_verification_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeeVerificationApi->update_employee_verification_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_employee_verification_integration_request** | [**UpdateEmployeeVerificationIntegrationRequest**](UpdateEmployeeVerificationIntegrationRequest.md)|  | 

### Return type

[**EmployeeVerificationIntegrationResponse**](EmployeeVerificationIntegrationResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request body or partner configuration prevented the change. |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

