# bamboohr_sdk.AlertsApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_alert_configuration**](AlertsApi.md#create_alert_configuration) | **POST** /api/v1/alert-configurations | Create Alert Configuration
[**get_alert_configuration**](AlertsApi.md#get_alert_configuration) | **GET** /api/v1/alert-configurations/{id} | Get Alert Configuration
[**list_alert_configurations**](AlertsApi.md#list_alert_configurations) | **GET** /api/v1/alert-configurations | List Alert Configurations
[**list_alert_templates**](AlertsApi.md#list_alert_templates) | **GET** /api/v1/alerts | List Alert Templates
[**replace_alert_configuration**](AlertsApi.md#replace_alert_configuration) | **PUT** /api/v1/alert-configurations/{id} | Replace Alert Configuration


# **create_alert_configuration**
> AlertConfigurationV1 create_alert_configuration(alert_configuration_write_v1)

Create Alert Configuration

Creates an alert configuration for the authenticated company from one of BambooHR's alert templates, and returns the stored configuration, including its server-assigned `id`, as a single JSON object.

Use this to add a configuration the company does not have yet. To overwrite one that already exists, use **Replace Alert Configuration** (`replace-alert-configuration`) instead; to see what is already configured, use **List Alert Configurations** (`list-alert-configurations`). `bambooAlertId` names the alert template the configuration is built on and comes from **List Alert Templates** (`list-alert-templates`). An alert configuration sends scheduled email to people; to receive a programmatic HTTP callback when employee data changes instead, use **Webhooks > Create Webhook** (`create-webhook`).

The configuration is live as soon as it is created and begins sending on the schedule it defines. Nothing limits a template to one configuration, so repeating this call with the same `bambooAlertId` adds a second configuration rather than replacing the first, and no endpoint deletes an alert configuration once it exists. The returned object also carries `additionalRecipientEmails`, `employeeIds`, `listValueIds`, and `userIds`; this API never stores those, so scope an alert's audience with `filterListValueIds` and the `sendTo*` properties instead.

Access is all-or-nothing rather than per-record. An authenticated caller without view access to the company's Email Alerts settings receives `403` instead of a partial success.

OAuth Scopes: alerts.write

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.alert_configuration_v1 import AlertConfigurationV1
from bamboohr_sdk.models.alert_configuration_write_v1 import AlertConfigurationWriteV1
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
    api_instance = bamboohr_sdk.AlertsApi(api_client)
    alert_configuration_write_v1 = bamboohr_sdk.AlertConfigurationWriteV1() # AlertConfigurationWriteV1 | 

    try:
        # Create Alert Configuration
        api_response = api_instance.create_alert_configuration(alert_configuration_write_v1)
        print("The response of AlertsApi->create_alert_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->create_alert_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_configuration_write_v1** | [**AlertConfigurationWriteV1**](AlertConfigurationWriteV1.md)|  | 

### Return type

[**AlertConfigurationV1**](AlertConfigurationV1.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created alert configuration, as a single JSON object. |  -  |
**400** | Bad request. The request body failed validation; the &#x60;fields.body&#x60; entry names the property at fault. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. The authenticated user does not have view access to the company&#39;s Email Alerts settings. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_configuration**
> AlertConfigurationV1 get_alert_configuration(id)

Get Alert Configuration

Returns one alert configuration the company has set up: which alert template it uses, when it runs, who receives it, and any custom subject, message, or list-value filters. The response is a single JSON object with no wrapper.

Use this when the configuration's `id` is already known, either from **List Alert Configurations** (`list-alert-configurations`) or from the body **Create Alert Configuration** (`create-alert-configuration`) and **Replace Alert Configuration** (`replace-alert-configuration`) return. To enumerate or search a company's configured alerts, use `list-alert-configurations` instead. For the catalog of alert types that *can* be configured, rather than what this company has configured, use **List Alert Templates** (`list-alert-templates`). The `bambooAlertId` on the returned object identifies the underlying template, not this configuration, so the two identifiers are not interchangeable.

Access is all-or-nothing rather than per-record. An authenticated caller without view access to the company's Email Alerts settings receives `403` rather than a partially redacted object. Only configurations belonging to the authenticated company are reachable, and an `id` from any other company is indistinguishable from one that never existed.

OAuth Scopes: alerts

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.alert_configuration_v1 import AlertConfigurationV1
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
    api_instance = bamboohr_sdk.AlertsApi(api_client)
    id = 56 # int | Identifier of the alert configuration to return, as emitted in the `id` field of **List Alert Configurations** (`list-alert-configurations`). This is the configuration's own identifier, not the `bambooAlertId` of the alert template it is based on. No wildcard or `0` sentinel is supported; enumerate configurations with `list-alert-configurations` instead.

    try:
        # Get Alert Configuration
        api_response = api_instance.get_alert_configuration(id)
        print("The response of AlertsApi->get_alert_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->get_alert_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identifier of the alert configuration to return, as emitted in the &#x60;id&#x60; field of **List Alert Configurations** (&#x60;list-alert-configurations&#x60;). This is the configuration&#39;s own identifier, not the &#x60;bambooAlertId&#x60; of the alert template it is based on. No wildcard or &#x60;0&#x60; sentinel is supported; enumerate configurations with &#x60;list-alert-configurations&#x60; instead. | 

### Return type

[**AlertConfigurationV1**](AlertConfigurationV1.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested alert configuration, as a single JSON object. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. The authenticated user does not have view access to the company&#39;s Email Alerts settings. |  -  |
**404** | Not found. No alert configuration with the given &#x60;id&#x60; exists for the authenticated company. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alert_configurations**
> List[AlertConfigurationV1] list_alert_configurations()

List Alert Configurations

Returns every alert configuration the company has set up: which alert template each one uses, when it runs, who receives it, and any custom subject, message, or list-value filters. The response is a top-level JSON array with no wrapper, empty when the company has no configured alerts, and in no guaranteed order.

Use this to enumerate or search a company's own configured alerts. To read a single configuration whose `id` is already known, use **Get Alert Configuration** (`get-alert-configuration`) instead. For the catalog of alert types that *can* be configured, rather than what this company has configured, use **List Alert Templates** (`list-alert-templates`). The `bambooAlertId` on each entry returned here is the same identifier that `list-alert-templates` returns as `id`.

Access is all-or-nothing rather than per-record. An authenticated caller without view access to the company's Email Alerts settings receives `403` instead of a filtered list, so a successful response always contains the company's complete set.

OAuth Scopes: alerts

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.alert_configuration_v1 import AlertConfigurationV1
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
    api_instance = bamboohr_sdk.AlertsApi(api_client)

    try:
        # List Alert Configurations
        api_response = api_instance.list_alert_configurations()
        print("The response of AlertsApi->list_alert_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->list_alert_configurations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AlertConfigurationV1]**](AlertConfigurationV1.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of the company&#39;s alert configurations. Empty array when none are configured. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. The authenticated user does not have view access to the company&#39;s Email Alerts settings. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alert_templates**
> AlertTemplateListResponseV1 list_alert_templates()

List Alert Templates

Returns the catalog of alert templates that company alert configurations are built from. These are the built-in alert types BambooHR supports (for example New Hire, Birthdays, Time Off Approved), each paired with the settings group it is filed under.

The response is an object with a single `alerts` array, ordered by `groupName` and then `name`. The alert-configuration endpoints represent the same identifier as `bambooAlertId`. The catalog is global: it lists every alert BambooHR offers and is not narrowed to the features the authenticated company has enabled, so a template appearing here does not guarantee that the company can configure it.

Use this to discover the `bambooAlertId` required by **Create Alert Configuration** (`create-alert-configuration`). For the alerts a company has already configured, use **List Alert Configurations** (`list-alert-configurations`) instead. Callers without view access to the company's Email Alerts settings receive `403` rather than a filtered result.

OAuth Scopes: alerts

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.alert_template_list_response_v1 import AlertTemplateListResponseV1
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
    api_instance = bamboohr_sdk.AlertsApi(api_client)

    try:
        # List Alert Templates
        api_response = api_instance.list_alert_templates()
        print("The response of AlertsApi->list_alert_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->list_alert_templates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AlertTemplateListResponseV1**](AlertTemplateListResponseV1.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object containing the alert template catalog. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. The authenticated user does not have view access to the company&#39;s Email Alerts settings. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_alert_configuration**
> AlertConfigurationV1 replace_alert_configuration(id, alert_configuration_write_v1)

Replace Alert Configuration

Overwrites the alert configuration identified by `{id}` and returns the stored configuration as a single JSON object. Each call replaces the whole configuration: a property left out of the request body is reset to its default rather than kept at its current value, so send the full desired state and not only the properties that changed. Read the current state with **Get Alert Configuration** (`get-alert-configuration`) first when only part of a configuration should change. The response echoes the values submitted rather than re-reading the saved row, so read the configuration back with `get-alert-configuration` when the persisted state needs to be confirmed.

Use this to change a configuration the company already has. To add one, use **Create Alert Configuration** (`create-alert-configuration`) instead; to find out what is already configured, use **List Alert Configurations** (`list-alert-configurations`). `bambooAlertId` names the alert template the configuration is built on, comes from **List Alert Templates** (`list-alert-templates`), and is required on every call even when the template is not changing.

The configuration stays live throughout and sends on whatever schedule the call leaves it with, so an update that omits the `sendTo*` properties can re-enable delivery to recipients the previous state excluded. Changing `bambooAlertId` re-points this configuration at a different alert template rather than adding a second one, and no endpoint deletes an alert configuration once it exists. The returned object also carries `additionalRecipientEmails`, `employeeIds`, `listValueIds`, and `userIds`; this API never stores those, so scope an alert's audience with `filterListValueIds` and the `sendTo*` properties instead.

Access is all-or-nothing rather than per-record. An authenticated caller without view access to the company's Email Alerts settings receives `403` instead of a partial success.

OAuth Scopes: alerts.write

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.alert_configuration_v1 import AlertConfigurationV1
from bamboohr_sdk.models.alert_configuration_write_v1 import AlertConfigurationWriteV1
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
    api_instance = bamboohr_sdk.AlertsApi(api_client)
    id = 56 # int | Identifier of the alert configuration to overwrite, as emitted in the `id` field of **List Alert Configurations** (`list-alert-configurations`). This is the configuration's own identifier, not the `bambooAlertId` of the alert template it is based on. The path value is authoritative; no wildcard or `0` sentinel is supported.
    alert_configuration_write_v1 = bamboohr_sdk.AlertConfigurationWriteV1() # AlertConfigurationWriteV1 | 

    try:
        # Replace Alert Configuration
        api_response = api_instance.replace_alert_configuration(id, alert_configuration_write_v1)
        print("The response of AlertsApi->replace_alert_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertsApi->replace_alert_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identifier of the alert configuration to overwrite, as emitted in the &#x60;id&#x60; field of **List Alert Configurations** (&#x60;list-alert-configurations&#x60;). This is the configuration&#39;s own identifier, not the &#x60;bambooAlertId&#x60; of the alert template it is based on. The path value is authoritative; no wildcard or &#x60;0&#x60; sentinel is supported. | 
 **alert_configuration_write_v1** | [**AlertConfigurationWriteV1**](AlertConfigurationWriteV1.md)|  | 

### Return type

[**AlertConfigurationV1**](AlertConfigurationV1.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The replaced alert configuration, as a single JSON object. |  -  |
**400** | Bad request. The request body failed validation; the &#x60;fields.body&#x60; entry names the property at fault. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. The authenticated user does not have view access to the company&#39;s Email Alerts settings. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

