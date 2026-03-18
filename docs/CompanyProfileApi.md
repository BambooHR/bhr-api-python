# bamboohr_sdk.CompanyProfileApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_company_profile_integrations**](CompanyProfileApi.md#get_company_profile_integrations) | **GET** /api/v1/company-profile-integrations | Get Company Profile Integrations


# **get_company_profile_integrations**
> CompanyProfileIntegrations get_company_profile_integrations()

Get Company Profile Integrations

Returns the list of integration feature identifiers currently enabled for the company. Each identifier is an uppercase string key (e.g. `BAMBOOHR_PAYROLL`, `TIME_TRACKING`, `E_SIGNATURES`) representing a product feature or integration that has been activated on the account. The list reflects the company's current subscription and configuration.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.company_profile_integrations import CompanyProfileIntegrations
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
    api_instance = bamboohr_sdk.CompanyProfileApi(api_client)

    try:
        # Get Company Profile Integrations
        api_response = api_instance.get_company_profile_integrations()
        print("The response of CompanyProfileApi->get_company_profile_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyProfileApi->get_company_profile_integrations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CompanyProfileIntegrations**](CompanyProfileIntegrations.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of enabled integration identifiers for the company. |  -  |
**403** | The API user does not have permission to access company profile integrations. |  -  |
**500** | An unexpected error occurred while retrieving company profile integrations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

