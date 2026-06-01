# bamboohr_sdk.CompanyApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**put_company_industry_codes**](CompanyApi.md#put_company_industry_codes) | **PUT** /api/v1/company-profile-data/industry-codes | Update Company Industry Codes


# **put_company_industry_codes**
> UpdateCompanyIndustryCodesResponse put_company_industry_codes(put_company_industry_codes_request)

Update Company Industry Codes

Updates the industry codes associated with a company.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.put_company_industry_codes_request import PutCompanyIndustryCodesRequest
from bamboohr_sdk.models.update_company_industry_codes_response import UpdateCompanyIndustryCodesResponse
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
    api_instance = bamboohr_sdk.CompanyApi(api_client)
    put_company_industry_codes_request = {"industryIds":[1]} # PutCompanyIndustryCodesRequest | 

    try:
        # Update Company Industry Codes
        api_response = api_instance.put_company_industry_codes(put_company_industry_codes_request)
        print("The response of CompanyApi->put_company_industry_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyApi->put_company_industry_codes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **put_company_industry_codes_request** | [**PutCompanyIndustryCodesRequest**](PutCompanyIndustryCodesRequest.md)|  | 

### Return type

[**UpdateCompanyIndustryCodesResponse**](UpdateCompanyIndustryCodesResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated list of enabled industries for the company |  -  |
**400** | Bad request due to invalid request structure or multiple industry IDs provided |  -  |
**401** | Missing or invalid authentication |  -  |
**403** | Insufficient permissions or release toggle not enabled |  -  |
**404** | Industry ID not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

