# bamboohr_sdk.WebhooksApi


Please also refer to this link for notes on security and an explanation of global & permissioned webhooks: https://documentation.bamboohr.com/docs/webhooks

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_webhook**](WebhooksApi.md#delete_webhook) | **DELETE** /api/v1/webhooks/{id} | Delete Webhook
[**get_monitor_fields**](WebhooksApi.md#get_monitor_fields) | **GET** /api/v1/webhooks/monitor_fields | Get Monitor Fields
[**get_post_fields**](WebhooksApi.md#get_post_fields) | **GET** /api/v1/webhooks/post-fields | Get Post Fields
[**get_webhook**](WebhooksApi.md#get_webhook) | **GET** /api/v1/webhooks/{id} | Get Webhook
[**get_webhook_list**](WebhooksApi.md#get_webhook_list) | **GET** /api/v1/webhooks | Get Webhooks
[**get_webhook_logs**](WebhooksApi.md#get_webhook_logs) | **GET** /api/v1/webhooks/{id}/log | Get Webhook Logs
[**post_webhook**](WebhooksApi.md#post_webhook) | **POST** /api/v1/webhooks | Create Webhook
[**put_webhook**](WebhooksApi.md#put_webhook) | **PUT** /api/v1/webhooks/{id} | Update Webhook


# **delete_webhook**
> delete_webhook(id)

Delete Webhook

Delete a webhook that is tied to a specific user API Key.

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
        api_instance.delete_webhook(id)
    except Exception as e:
        print("Exception when calling WebhooksApi->delete_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The webhook ID to delete. | 

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
**200** | Webhook was deleted |  -  |
**401** | The user API key is invalid. |  -  |
**403** | The API user key does not have permission to delete the requested webhook. |  -  |
**404** | The webhook to be deleted doesn\\&#39;t exist. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_monitor_fields**
> FieldList get_monitor_fields()

Get Monitor Fields

Get a list fields webhooks can monitor

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
**200** | A list of fields |  -  |
**401** | The user API key is invalid. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_post_fields**
> WebHookPostFieldResponseObject get_post_fields()

Get Post Fields

Get a list fields webhooks can include in the post body

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
**200** | A list of fields accessible via the webhooks, with their tables and pages included in the response. |  -  |
**403** | Permission denied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**
> WebHookResponse get_webhook(id)

Get Webhook

Get webhook data that is tied to a specific user API Key.

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
**200** | A Webhook |  -  |
**401** | The user API key is invalid. |  -  |
**403** | The API user key does not have permission to see the requested webhook. |  -  |
**404** | The webhook does not exist. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_list**
> WebhooksList get_webhook_list()

Get Webhooks

Gets a list of webhooks for the user API key.

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
        # Get Webhooks
        api_response = api_instance.get_webhook_list()
        print("The response of WebhooksApi->get_webhook_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhook_list: %s\n" % e)
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
**200** | List of webhooks |  -  |
**401** | The user API key is invalid. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_logs**
> WebHookLogResponse get_webhook_logs(id)

Get Webhook Logs

Get webhook logs for specific webhook id that is associated with the user API Key.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.web_hook_log_response import WebHookLogResponse
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

[**WebHookLogResponse**](WebHookLogResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook Logs |  -  |
**403** | The API user key is invalid, or does not have permission to see the requested webhook. |  -  |
**404** | The webhook does not exist. |  -  |
**429** | Rate limit exceeded for webhook log requests. |  -  |
**500** | Internal error |  -  |
**503** | Log search timed out. Try again later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_webhook**
> Webhook post_webhook(new_web_hook)

Create Webhook

Add a new Webhook. For more details or instructions you can refer to the [webhooks documentation](https://documentation.bamboohr.com/docs/webhooks-2).

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
        api_response = api_instance.post_webhook(new_web_hook)
        print("The response of WebhooksApi->post_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->post_webhook: %s\n" % e)
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
**201** | Webhook created, JSON output of webhook follows. Private key is included in the create webhook only! |  -  |
**400** | Provided JSON is bad, missing required fields, or mulitple access levels. |  -  |
**401** | The user API key is invalid. |  -  |
**403** | Permission violations in the fields selected. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_webhook**
> WebHookResponse put_webhook(id, new_web_hook)

Update Webhook

Update a webhook, based on webhook ID.

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
        api_response = api_instance.put_webhook(id, new_web_hook)
        print("The response of WebhooksApi->put_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->put_webhook: %s\n" % e)
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
**400** | Provided JSON is bad, missing required fields, or mulitple access levels. |  -  |
**401** | The user API key is invalid. |  -  |
**403** | Permission violations in the fields selected, or the user does not have access to the webhook. |  -  |
**404** | The webhook to be updated doesn\\&#39;t exist. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

