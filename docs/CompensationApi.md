# bamboohr_sdk.CompensationApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**c5880b509783cd9d7fce9ddf5d6af1be**](CompensationApi.md#c5880b509783cd9d7fce9ddf5d6af1be) | **PUT** /api/v1/compensation/equity/settings | Update company equity settings
[**call_9f398e2652ea47a6dc5121ce5184222a**](CompensationApi.md#call_9f398e2652ea47a6dc5121ce5184222a) | **GET** /api/v1/compensation/tools | List available compensation tools
[**db49fb29f9f04d59afad7c01ce860418**](CompensationApi.md#db49fb29f9f04d59afad7c01ce860418) | **GET** /api/v1/compensation/equity/settings | Get company equity settings


# **c5880b509783cd9d7fce9ddf5d6af1be**
> CompensationEquitySettingsResponse c5880b509783cd9d7fce9ddf5d6af1be(compensation_equity_settings_update_request)

Update company equity settings

Updates company-level equity settings including calculation type, valuation, shares, pricing, and vesting-related configuration.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.compensation_equity_settings_response import CompensationEquitySettingsResponse
from bamboohr_sdk.models.compensation_equity_settings_update_request import CompensationEquitySettingsUpdateRequest
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
    api_instance = bamboohr_sdk.CompensationApi(api_client)
    compensation_equity_settings_update_request = bamboohr_sdk.CompensationEquitySettingsUpdateRequest() # CompensationEquitySettingsUpdateRequest | 

    try:
        # Update company equity settings
        api_response = api_instance.c5880b509783cd9d7fce9ddf5d6af1be(compensation_equity_settings_update_request)
        print("The response of CompensationApi->c5880b509783cd9d7fce9ddf5d6af1be:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationApi->c5880b509783cd9d7fce9ddf5d6af1be: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compensation_equity_settings_update_request** | [**CompensationEquitySettingsUpdateRequest**](CompensationEquitySettingsUpdateRequest.md)|  | 

### Return type

[**CompensationEquitySettingsResponse**](CompensationEquitySettingsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Settings updated successfully |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_9f398e2652ea47a6dc5121ce5184222a**
> CompensationToolsResponse call_9f398e2652ea47a6dc5121ce5184222a()

List available compensation tools

Returns the list of available compensation tools/settings for the company, including Levels & Bands, Compensation Benchmarking, Compensation Planning, and Total Rewards. Also returns upsell information if applicable.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.compensation_tools_response import CompensationToolsResponse
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
    api_instance = bamboohr_sdk.CompensationApi(api_client)

    try:
        # List available compensation tools
        api_response = api_instance.call_9f398e2652ea47a6dc5121ce5184222a()
        print("The response of CompensationApi->call_9f398e2652ea47a6dc5121ce5184222a:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationApi->call_9f398e2652ea47a6dc5121ce5184222a: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CompensationToolsResponse**](CompensationToolsResponse.md)

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

# **db49fb29f9f04d59afad7c01ce860418**
> CompensationEquitySettingsResponse db49fb29f9f04d59afad7c01ce860418()

Get company equity settings

Retrieves company-level equity settings including calculation type, valuation, shares, pricing, and vesting-related configuration.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.compensation_equity_settings_response import CompensationEquitySettingsResponse
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
    api_instance = bamboohr_sdk.CompensationApi(api_client)

    try:
        # Get company equity settings
        api_response = api_instance.db49fb29f9f04d59afad7c01ce860418()
        print("The response of CompensationApi->db49fb29f9f04d59afad7c01ce860418:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationApi->db49fb29f9f04d59afad7c01ce860418: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CompensationEquitySettingsResponse**](CompensationEquitySettingsResponse.md)

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

