# bamboohr_sdk.AlertApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call_0f0dcb585e5883175b6557c16cf6755a**](AlertApi.md#call_0f0dcb585e5883175b6557c16cf6755a) | **GET** /api/v1/alerts | List alert templates


# **call_0f0dcb585e5883175b6557c16cf6755a**
> AlertTemplateListResponse call_0f0dcb585e5883175b6557c16cf6755a()

List alert templates

Returns all available alert templates with their IDs, names, and group names. Use the returned IDs when creating or updating company alert configurations.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.alert_template_list_response import AlertTemplateListResponse
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
    api_instance = bamboohr_sdk.AlertApi(api_client)

    try:
        # List alert templates
        api_response = api_instance.call_0f0dcb585e5883175b6557c16cf6755a()
        print("The response of AlertApi->call_0f0dcb585e5883175b6557c16cf6755a:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertApi->call_0f0dcb585e5883175b6557c16cf6755a: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AlertTemplateListResponse**](AlertTemplateListResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of alert templates |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

