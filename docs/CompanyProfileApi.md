# bamboohr_sdk.CompanyProfileApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_company_profile_integrations**](CompanyProfileApi.md#get_company_profile_integrations) | **GET** /api/v1/company-profile-integrations | Get Company Profile Integrations
[**patch_company_profile_company_information**](CompanyProfileApi.md#patch_company_profile_company_information) | **PATCH** /api/v1/company-profile-data/company-information | Update company information (phone, address, legal name)
[**put_company_profile_display_name**](CompanyProfileApi.md#put_company_profile_display_name) | **PUT** /api/v1/company-profile-data/display-name | Update company display name


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

# **patch_company_profile_company_information**
> CompanyProfileData patch_company_profile_company_information(patch_company_profile_company_information_request)

Update company information (phone, address, legal name)

Updates legal name, phone, and/or address for the company (application/merge-patch+json). String fields must be JSON strings (not numbers). Response matches GET /api/v1/company-profile-data.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.company_profile_data import CompanyProfileData
from bamboohr_sdk.models.patch_company_profile_company_information_request import PatchCompanyProfileCompanyInformationRequest
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
    api_instance = bamboohr_sdk.CompanyProfileApi(api_client)
    patch_company_profile_company_information_request = bamboohr_sdk.PatchCompanyProfileCompanyInformationRequest() # PatchCompanyProfileCompanyInformationRequest | 

    try:
        # Update company information (phone, address, legal name)
        api_response = api_instance.patch_company_profile_company_information(patch_company_profile_company_information_request)
        print("The response of CompanyProfileApi->patch_company_profile_company_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyProfileApi->patch_company_profile_company_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_company_profile_company_information_request** | [**PatchCompanyProfileCompanyInformationRequest**](PatchCompanyProfileCompanyInformationRequest.md)|  | 

### Return type

[**CompanyProfileData**](CompanyProfileData.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response; same shape as GET company-profile-data |  -  |
**400** | Invalid JSON or Content-Type |  -  |
**403** | Permission denied |  -  |
**422** | Validation failed (invalid field types or incomplete profile after merge) |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_profile_display_name**
> UpdateCompanyNameSuccessResponse put_company_profile_display_name(put_company_profile_display_name_request=put_company_profile_display_name_request)

Update company display name

Updates the company display name. Requires admin permissions and the company:details.write OAuth scope. The display name must be a non-empty string with a maximum length of 255 characters. Upon successful update, the system logs the change and broadcasts an event to notify other services.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.put_company_profile_display_name_request import PutCompanyProfileDisplayNameRequest
from bamboohr_sdk.models.update_company_name_success_response import UpdateCompanyNameSuccessResponse
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
    api_instance = bamboohr_sdk.CompanyProfileApi(api_client)
    put_company_profile_display_name_request = bamboohr_sdk.PutCompanyProfileDisplayNameRequest() # PutCompanyProfileDisplayNameRequest |  (optional)

    try:
        # Update company display name
        api_response = api_instance.put_company_profile_display_name(put_company_profile_display_name_request=put_company_profile_display_name_request)
        print("The response of CompanyProfileApi->put_company_profile_display_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyProfileApi->put_company_profile_display_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **put_company_profile_display_name_request** | [**PutCompanyProfileDisplayNameRequest**](PutCompanyProfileDisplayNameRequest.md)|  | [optional] 

### Return type

[**UpdateCompanyNameSuccessResponse**](UpdateCompanyNameSuccessResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Company name updated successfully |  -  |
**400** | Invalid request body or company name |  -  |
**403** | Permission denied |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

