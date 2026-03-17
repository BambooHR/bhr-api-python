# bamboohr_sdk.WebhooksApi


Please also refer to this link for notes on security and an explanation of global & permissioned webhooks: https://documentation.bamboohr.com/docs/webhooks

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhooksApi.md#create_webhook) | **POST** /api/v1/webhooks | Create Webhook
[**delete_webhook**](WebhooksApi.md#delete_webhook) | **DELETE** /api/v1/webhooks/{id} | Delete Webhook
[**get_monitor_fields**](WebhooksApi.md#get_monitor_fields) | **GET** /api/v1/webhooks/monitor_fields | Get Monitor Fields
[**get_post_fields**](WebhooksApi.md#get_post_fields) | **GET** /api/v1/webhooks/post-fields | Get Post Fields
[**get_webhook**](WebhooksApi.md#get_webhook) | **GET** /api/v1/webhooks/{id} | Get Webhook
[**get_webhook_logs**](WebhooksApi.md#get_webhook_logs) | **GET** /api/v1/webhooks/{id}/log | Get Webhook Logs
[**list_webhooks**](WebhooksApi.md#list_webhooks) | **GET** /api/v1/webhooks | List Webhooks
[**update_webhook**](WebhooksApi.md#update_webhook) | **PUT** /api/v1/webhooks/{id} | Update Webhook


# **create_webhook**
> Webhook create_webhook(new_web_hook)

Create Webhook

Creates a new webhook for the authenticated user's API key. The webhook will fire when the specified events occur or when any of the monitored fields change.

The `monitorFields` array is required when `events` includes `employee.updated` or `employee_with_fields.updated`. If `events` is omitted, it defaults to `['employee_with_fields.updated', 'employee_with_fields.deleted', 'employee_with_fields.created']`, which means `monitorFields` is required by default. The `format` field is required.

The response includes a `privateKey` that can be used to verify the authenticity of incoming webhook payloads via HMAC-SHA256. This key is only returned at creation time and cannot be retrieved again.

For more details refer to the [webhooks documentation](https://documentation.bamboohr.com/docs/webhooks), including guides for [event-based](https://documentation.bamboohr.com/docs/event-based-webhooks) and [field-based](https://documentation.bamboohr.com/docs/field-based-webhooks) webhooks.

For details on the payloads sent by each event, see the event reference:
- [employee.created](https://documentation.bamboohr.com/reference/employee-created-webhook)
- [employee.updated](https://documentation.bamboohr.com/reference/employee-updated-webhook)
- [employee.deleted](https://documentation.bamboohr.com/reference/employee-deleted-webhook)

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.new_web_hook import NewWebHook
from bamboohr_sdk.models.webhook import Webhook
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
    api_instance = bamboohr_sdk.WebhooksApi(api_client)
    new_web_hook = bamboohr_sdk.NewWebHook() # NewWebHook | 

    try:
        # Create Webhook
        api_response = api_instance.create_webhook(new_web_hook)
        print("The response of WebhooksApi->create_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->create_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_web_hook** | [**NewWebHook**](NewWebHook.md)|  | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Webhook created successfully. The &#x60;privateKey&#x60; field is only returned in this response and cannot be retrieved again. |  -  |
**400** | Request body is malformed or missing required fields. Common causes: missing &#x60;format&#x60;, missing &#x60;monitorFields&#x60; when required by the selected events, URL not starting with &#x60;https://&#x60;, or an invalid &#x60;format&#x60; value. |  -  |
**401** | The user API key is invalid. |  -  |
**403** | The authenticated user does not have permission to access one or more of the specified fields. The response lists which &#x60;monitorFields&#x60;, &#x60;postFields&#x60;, and &#x60;unknownFields&#x60; caused the violation. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**
> str delete_webhook(id)

Delete Webhook

Deletes a webhook tied to the authenticated user API key. Returns 403 if the webhook belongs to a different user API key, and 404 if the webhook does not exist. On success, returns a plain text confirmation message.

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
    api_instance = bamboohr_sdk.WebhooksApi(api_client)
    id = 56 # int | The webhook ID to delete.

    try:
        # Delete Webhook
        api_response = api_instance.delete_webhook(id)
        print("The response of WebhooksApi->delete_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->delete_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The webhook ID to delete. | 

### Return type

**str**

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook deleted successfully. Returns a plain text confirmation message. |  -  |
**401** | The user API key is invalid. |  -  |
**403** | The API user key does not have permission to delete the requested webhook. |  -  |
**404** | The webhook to be deleted doesn\\&#39;t exist. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitor_fields**
> FieldList get_monitor_fields()

Get Monitor Fields

Returns the list of employee fields that can be monitored by a webhook. Use these field IDs or aliases in the `monitorFields` array when creating or updating a webhook. Each entry includes a numeric field ID (returned as a string), a human-readable name, and an alias (if one exists; otherwise null).

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.field_list import FieldList
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
    api_instance = bamboohr_sdk.WebhooksApi(api_client)

    try:
        # Get Monitor Fields
        api_response = api_instance.get_monitor_fields()
        print("The response of WebhooksApi->get_monitor_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_monitor_fields: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FieldList**](FieldList.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object with a &#x60;fields&#x60; array containing one entry per monitorable employee field, including the field ID (as a string), human-readable name, and alias (null if no alias is defined). |  -  |
**401** | The user API key is invalid. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_post_fields**
> WebHookPostFieldResponseObject get_post_fields()

Get Post Fields

Returns an object containing the employee fields that can be included in the webhook post body, along with the related table and page records referenced by those fields. Use the field IDs or aliases from this response in the `postFields` map when creating or updating a webhook.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.web_hook_post_field_response_object import WebHookPostFieldResponseObject
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
    api_instance = bamboohr_sdk.WebhooksApi(api_client)

    try:
        # Get Post Fields
        api_response = api_instance.get_post_fields()
        print("The response of WebhooksApi->get_post_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_post_fields: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WebHookPostFieldResponseObject**](WebHookPostFieldResponseObject.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object with &#x60;fields&#x60;, &#x60;tables&#x60;, and &#x60;pages&#x60; arrays. &#x60;fields&#x60; contains the postable employee fields with their IDs, aliases, types, and associated page/table IDs. &#x60;tables&#x60; and &#x60;pages&#x60; contain the referenced metadata for those associations. |  -  |
**403** | Permission denied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**
> WebHookResponse get_webhook(id)

Get Webhook

Returns the full configuration of a single webhook owned by the authenticated user API key, including its name, URL, format, monitored fields, post fields, events, creation datetime, and last-sent datetime. Returns 403 if the webhook exists but belongs to a different user API key, and 404 if the webhook does not exist.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.web_hook_response import WebHookResponse
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
    api_instance = bamboohr_sdk.WebhooksApi(api_client)
    id = 56 # int | The webhook ID to display details about.

    try:
        # Get Webhook
        api_response = api_instance.get_webhook(id)
        print("The response of WebhooksApi->get_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The webhook ID to display details about. | 

### Return type

[**WebHookResponse**](WebHookResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The full configuration of the requested webhook. |  -  |
**401** | The user API key is invalid. |  -  |
**403** | The API user key does not have permission to see the requested webhook. |  -  |
**404** | The webhook does not exist. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_logs**
> WebhookLogListResponse get_webhook_logs(id)

Get Webhook Logs

Returns an array of recent delivery log entries for a webhook. Logs cover the last 14 days and are limited to 200 entries. Each entry includes the webhook URL, the last attempt value, the last success value, the HTTP status code of the last response, the payload format, and the list of employee IDs included in the payload. The `lastAttempted` and `lastSuccess` fields are usually UTC datetimes in `YYYY-MM-DD HH:MM:SS` format, but may instead contain status strings such as `Webhook Not Found`. Returns an empty array if no deliveries have occurred in the lookback window.

**Rate limiting:** This endpoint is rate-limited. When the rate limit is exceeded the server still returns HTTP 200, but the body is `{"error":{"code":429,"message":"Over rate limit, please try again in 60 seconds"}}` instead of the log array. Callers should check for this shape before processing the response as a log list.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.webhook_log_list_response import WebhookLogListResponse
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
    api_instance = bamboohr_sdk.WebhooksApi(api_client)
    id = 56 # int | The webhook ID to get logs about.

    try:
        # Get Webhook Logs
        api_response = api_instance.get_webhook_logs(id)
        print("The response of WebhooksApi->get_webhook_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhook_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The webhook ID to get logs about. | 

### Return type

[**WebhookLogListResponse**](WebhookLogListResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of webhook delivery log entries for the last 14 days (up to 200 entries). Returns an empty array if no deliveries have occurred. |  -  |
**403** | The authenticated user does not have permission to see the requested webhook. |  -  |
**404** | The webhook does not exist. |  -  |
**500** | Internal error |  -  |
**503** | Log search timed out. Returns a plain text error message. Try again later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhooks**
> WebhooksList list_webhooks()

List Webhooks

Returns all webhooks owned by the authenticated user API key. Returns an empty array if no webhooks have been created for this key. Each entry includes the webhook ID, name, URL, creation datetime, and the datetime it was last fired. Use `GET /api/v1/webhooks/{id}` to retrieve the full configuration including monitored fields, post fields, and events for a specific webhook.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.webhooks_list import WebhooksList
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
    api_instance = bamboohr_sdk.WebhooksApi(api_client)

    try:
        # List Webhooks
        api_response = api_instance.list_webhooks()
        print("The response of WebhooksApi->list_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->list_webhooks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WebhooksList**](WebhooksList.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object with a &#x60;webhooks&#x60; array containing one entry per webhook owned by the authenticated user API key. Returns an empty array when no webhooks exist for this key. |  -  |
**401** | The user API key is invalid. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> WebHookResponse update_webhook(id, new_web_hook)

Update Webhook

Performs a full replacement update of a webhook. All fields in the request body replace the existing values. The `format` field is required. The `monitorFields` array is required when `events` includes `employee.updated` or `employee_with_fields.updated`. Returns 403 if the webhook belongs to a different user or if field permission violations are present, and 404 if the webhook does not exist.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.new_web_hook import NewWebHook
from bamboohr_sdk.models.web_hook_response import WebHookResponse
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
    api_instance = bamboohr_sdk.WebhooksApi(api_client)
    id = 56 # int | The webhook ID to update.
    new_web_hook = bamboohr_sdk.NewWebHook() # NewWebHook | 

    try:
        # Update Webhook
        api_response = api_instance.update_webhook(id, new_web_hook)
        print("The response of WebhooksApi->update_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->update_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The webhook ID to update. | 
 **new_web_hook** | [**NewWebHook**](NewWebHook.md)|  | 

### Return type

[**WebHookResponse**](WebHookResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook updated successfully. |  -  |
**400** | Request body is malformed or missing required fields. Common causes: missing &#x60;format&#x60;, missing &#x60;monitorFields&#x60; when required by the selected events, URL not starting with &#x60;https://&#x60;, or an invalid &#x60;format&#x60; value. |  -  |
**401** | The user API key is invalid. |  -  |
**403** | The authenticated user does not have permission to access one or more of the specified fields, or does not have access to the webhook. When caused by field permission violations, &#x60;errors&#x60; is an array and lists which &#x60;monitorFields&#x60;, &#x60;postFields&#x60;, and &#x60;unknownFields&#x60; caused the violation. When caused by webhook ownership denial, &#x60;errors&#x60; is an object with a single &#x60;error&#x60; string (e.g. &#x60;{\&quot;errors\&quot;:{\&quot;error\&quot;:\&quot;You do not have access to webhook ID: 6\&quot;}}&#x60;). |  -  |
**404** | The webhook to be updated doesn\\&#39;t exist. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

