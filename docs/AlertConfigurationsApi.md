# bamboohr_sdk.AlertConfigurationsApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**a05e93bc2eb9c39a40fbd71e6e07f3c6**](AlertConfigurationsApi.md#a05e93bc2eb9c39a40fbd71e6e07f3c6) | **POST** /api/v1/alert-configurations | Create an alert configuration
[**call_14e66bfb5f075043221ce1e843c97493**](AlertConfigurationsApi.md#call_14e66bfb5f075043221ce1e843c97493) | **GET** /api/v1/alert-configurations/{id} | Get an alert configuration
[**call_6d0a073cbf3e97fe0409de42c68fe779**](AlertConfigurationsApi.md#call_6d0a073cbf3e97fe0409de42c68fe779) | **GET** /api/v1/alert-configurations | List alert configurations
[**eb42aa2fa339ba5c08b147fc13c6a79e**](AlertConfigurationsApi.md#eb42aa2fa339ba5c08b147fc13c6a79e) | **PUT** /api/v1/alert-configurations/{id} | Update an alert configuration


# **a05e93bc2eb9c39a40fbd71e6e07f3c6**
> CompanyAlertDataObject a05e93bc2eb9c39a40fbd71e6e07f3c6(company_alert_data_object)

Create an alert configuration

Creates a new company alert configuration.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.company_alert_data_object import CompanyAlertDataObject
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
    api_instance = bamboohr_sdk.AlertConfigurationsApi(api_client)
    company_alert_data_object = bamboohr_sdk.CompanyAlertDataObject() # CompanyAlertDataObject | 

    try:
        # Create an alert configuration
        api_response = api_instance.a05e93bc2eb9c39a40fbd71e6e07f3c6(company_alert_data_object)
        print("The response of AlertConfigurationsApi->a05e93bc2eb9c39a40fbd71e6e07f3c6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertConfigurationsApi->a05e93bc2eb9c39a40fbd71e6e07f3c6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_alert_data_object** | [**CompanyAlertDataObject**](CompanyAlertDataObject.md)|  | 

### Return type

[**CompanyAlertDataObject**](CompanyAlertDataObject.md)

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

# **call_14e66bfb5f075043221ce1e843c97493**
> CompanyAlertDataObject call_14e66bfb5f075043221ce1e843c97493(id)

Get an alert configuration

Returns a single company alert configuration by ID.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.company_alert_data_object import CompanyAlertDataObject
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
    api_instance = bamboohr_sdk.AlertConfigurationsApi(api_client)
    id = 56 # int | 

    try:
        # Get an alert configuration
        api_response = api_instance.call_14e66bfb5f075043221ce1e843c97493(id)
        print("The response of AlertConfigurationsApi->call_14e66bfb5f075043221ce1e843c97493:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertConfigurationsApi->call_14e66bfb5f075043221ce1e843c97493: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CompanyAlertDataObject**](CompanyAlertDataObject.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Alert configuration |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_6d0a073cbf3e97fe0409de42c68fe779**
> List[CompanyAlertDataObject] call_6d0a073cbf3e97fe0409de42c68fe779()

List alert configurations

Returns all company alert configurations for the authenticated company.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.company_alert_data_object import CompanyAlertDataObject
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
    api_instance = bamboohr_sdk.AlertConfigurationsApi(api_client)

    try:
        # List alert configurations
        api_response = api_instance.call_6d0a073cbf3e97fe0409de42c68fe779()
        print("The response of AlertConfigurationsApi->call_6d0a073cbf3e97fe0409de42c68fe779:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertConfigurationsApi->call_6d0a073cbf3e97fe0409de42c68fe779: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CompanyAlertDataObject]**](CompanyAlertDataObject.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of alert configurations |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **eb42aa2fa339ba5c08b147fc13c6a79e**
> CompanyAlertDataObject eb42aa2fa339ba5c08b147fc13c6a79e(id, company_alert_data_object)

Update an alert configuration

Updates an existing company alert configuration.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.company_alert_data_object import CompanyAlertDataObject
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
    api_instance = bamboohr_sdk.AlertConfigurationsApi(api_client)
    id = 56 # int | 
    company_alert_data_object = bamboohr_sdk.CompanyAlertDataObject() # CompanyAlertDataObject | 

    try:
        # Update an alert configuration
        api_response = api_instance.eb42aa2fa339ba5c08b147fc13c6a79e(id, company_alert_data_object)
        print("The response of AlertConfigurationsApi->eb42aa2fa339ba5c08b147fc13c6a79e:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertConfigurationsApi->eb42aa2fa339ba5c08b147fc13c6a79e: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **company_alert_data_object** | [**CompanyAlertDataObject**](CompanyAlertDataObject.md)|  | 

### Return type

[**CompanyAlertDataObject**](CompanyAlertDataObject.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

