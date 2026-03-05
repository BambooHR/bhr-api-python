# bamboohr_sdk.WebhookEventsApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**employee_created_webhook**](WebhookEventsApi.md#employee_created_webhook) | **POST** /employee.created | Employee Created
[**employee_deleted_webhook**](WebhookEventsApi.md#employee_deleted_webhook) | **POST** /employee.deleted | Employee Deleted
[**employee_updated_webhook**](WebhookEventsApi.md#employee_updated_webhook) | **POST** /employee.updated | Employee Updated


# **employee_created_webhook**
> employee_created_webhook(employee_created_webhook_payload=employee_created_webhook_payload)

Employee Created


Triggered when a new employee is created.

### Behavior & Constraints
- **Creation Sequence**: When an employee is created, both `employee.created` and `employee.updated` events fire sequentially due to the create-then-initialize pattern.
- **Data Availability**: The `data` object contains the `companyId` and `employeeId` of the newly created employee.
- **Permission Checking**: This event does **not** enforce permission checking. The webhook will fire for all subscribers regardless of the API token's field-level permissions.

### Deprecation Notice
**Note:** This event is the modern replacement for the legacy `employee_with_fields.created` event. While the legacy event is deprecated, it will remain available for the foreseeable future to support existing integrations. We encourage using this new event for all new development.

**Important:** You cannot subscribe to both this new event and the legacy `employee_with_fields` events on the same webhook. Webhooks created without specifying any events will default to the legacy behavior, effectively subscribing to the `employee_with_fields` events automatically.


### Example


```python
import bamboohr_sdk
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)


# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.WebhookEventsApi(api_client)
    employee_created_webhook_payload = bamboohr_sdk.EmployeeCreatedWebhookPayload() # EmployeeCreatedWebhookPayload | Webhook payload containing information about the employee creation (optional)

    try:
        # Employee Created
        api_instance.employee_created_webhook(employee_created_webhook_payload=employee_created_webhook_payload)
    except Exception as e:
        print("Exception when calling WebhookEventsApi->employee_created_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_created_webhook_payload** | [**EmployeeCreatedWebhookPayload**](EmployeeCreatedWebhookPayload.md)| Webhook payload containing information about the employee creation | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook received successfully (200-299 status code). |  -  |
**400** | Client error (400-499 status code) - the webhook endpoint intentionally rejected the request. BambooHR will not retry webhooks that return 4xx status codes. |  -  |
**500** | Server error (500+ status code). BambooHR will automatically retry this webhook up to 5 times using exponential backoff (5min, 10min, 20min, 40min, 80min intervals). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employee_deleted_webhook**
> employee_deleted_webhook(employee_deleted_webhook_payload=employee_deleted_webhook_payload)

Employee Deleted


Triggered when an employee is deleted.

### Behavior & Constraints
- **Permission Checking**: This event does **not** enforce permission checking. The webhook will fire for all subscribers regardless of the API token's field-level permissions.

### Deprecation Notice
**Note:** This event is the modern replacement for the legacy `employee_with_fields.deleted` event. While the legacy event is deprecated, it will remain available for the foreseeable future to support existing integrations. We encourage using this new event for all new development.

**Important:** You cannot subscribe to both this new event and the legacy `employee_with_fields` events on the same webhook. Webhooks created without specifying any events will default to the legacy behavior, effectively subscribing to the `employee_with_fields` events automatically.


### Example


```python
import bamboohr_sdk
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)


# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.WebhookEventsApi(api_client)
    employee_deleted_webhook_payload = bamboohr_sdk.EmployeeDeletedWebhookPayload() # EmployeeDeletedWebhookPayload | Webhook payload containing information about the employee deletion (optional)

    try:
        # Employee Deleted
        api_instance.employee_deleted_webhook(employee_deleted_webhook_payload=employee_deleted_webhook_payload)
    except Exception as e:
        print("Exception when calling WebhookEventsApi->employee_deleted_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_deleted_webhook_payload** | [**EmployeeDeletedWebhookPayload**](EmployeeDeletedWebhookPayload.md)| Webhook payload containing information about the employee deletion | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook received successfully (200-299 status code). |  -  |
**400** | Client error (400-499 status code) - the webhook endpoint intentionally rejected the request. BambooHR will not retry webhooks that return 4xx status codes. |  -  |
**500** | Server error (500+ status code). BambooHR will automatically retry this webhook up to 5 times using exponential backoff (5min, 10min, 20min, 40min, 80min intervals). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employee_updated_webhook**
> employee_updated_webhook(employee_updated_webhook_payload=employee_updated_webhook_payload)

Employee Updated


Triggered when an employee record is updated and at least one of the monitored fields has changed.

### Behavior & Constraints
- **Monitoring**: At least one `monitorField` is required when subscribing to this event via `POST /api/v1/webhooks`.
- **Permissions**: For API-created webhooks, this event will not fire if the webhook creator lacks access to all monitored fields being changed.

### Detailed Description
- **Creation Sequence**: When an employee is created, both `employee.created` and `employee.updated` events fire sequentially due to the create-then-initialize pattern.
- **Field Consolidation**: When multiple fields change simultaneously, they may be consolidated into a single event. Currently, custom field updates and standard field updates are grouped separately and may fire as two events.
- **Effective Dates**: For history-tracked fields (e.g., `jobTitle`, `payRate`), events fire only when changes take effect, not when future-dated changes are created.
- **Changed Fields**: The `changedFields` array contains the API aliases for fields that changed and are monitored by this webhook. Aliases match those returned by `GET /api/v1/webhooks/monitor_fields`.

### Deprecation Notice
**Note:** This event is the modern replacement for the legacy `employee_with_fields.updated` event. While the legacy event is deprecated, it will remain available for the foreseeable future to support existing integrations. We encourage using this new event for all new development.

**Important:** You cannot subscribe to both this new event and the legacy `employee_with_fields` events on the same webhook. Webhooks created without specifying any events will default to the legacy behavior, effectively subscribing to the `employee_with_fields` events automatically.


### Example


```python
import bamboohr_sdk
from bamboohr_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://companySubDomain.bamboohr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = bamboohr_sdk.Configuration(
    host = "https://companySubDomain.bamboohr.com"
)


# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.WebhookEventsApi(api_client)
    employee_updated_webhook_payload = bamboohr_sdk.EmployeeUpdatedWebhookPayload() # EmployeeUpdatedWebhookPayload | Webhook payload containing information about the employee update (optional)

    try:
        # Employee Updated
        api_instance.employee_updated_webhook(employee_updated_webhook_payload=employee_updated_webhook_payload)
    except Exception as e:
        print("Exception when calling WebhookEventsApi->employee_updated_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_updated_webhook_payload** | [**EmployeeUpdatedWebhookPayload**](EmployeeUpdatedWebhookPayload.md)| Webhook payload containing information about the employee update | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook received successfully (200-299 status code). |  -  |
**400** | Client error (400-499 status code) - the webhook endpoint intentionally rejected the request. BambooHR will not retry webhooks that return 4xx status codes. |  -  |
**500** | Server error (500+ status code). BambooHR will automatically retry this webhook up to 5 times using exponential backoff (5min, 10min, 20min, 40min, 80min intervals). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

