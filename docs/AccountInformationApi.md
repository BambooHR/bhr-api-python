# bamboohr_sdk.AccountInformationApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**baa7162824294d030115568d1d8e6ca7**](AccountInformationApi.md#baa7162824294d030115568d1d8e6ca7) | **GET** /api/v1/meta/timezones/{id} | Get timezone by ID
[**call_10d66d8561dd7dac50ff9c21ef63d83b**](AccountInformationApi.md#call_10d66d8561dd7dac50ff9c21ef63d83b) | **GET** /api/v1/meta/timezones/by-zip/{zip} | Get timezone by ZIP code
[**call_5c5fb0f1211ae1c9451753f92f1053b6**](AccountInformationApi.md#call_5c5fb0f1211ae1c9451753f92f1053b6) | **GET** /api/v1/meta/timezones | List timezones
[**get_all_currency_types**](AccountInformationApi.md#get_all_currency_types) | **GET** /api/v1/meta/currency/types | Get all currency types
[**get_all_provinces**](AccountInformationApi.md#get_all_provinces) | **GET** /api/v1/meta/provinces | Get All Provinces
[**get_countries_options**](AccountInformationApi.md#get_countries_options) | **GET** /api/v1/meta/countries/options | Get Countries
[**get_meta_company**](AccountInformationApi.md#get_meta_company) | **GET** /api/v1/meta/company | Get company properties
[**get_states_by_country_id**](AccountInformationApi.md#get_states_by_country_id) | **GET** /api/v1/meta/provinces/{countryId} | List states and provinces for a country by Country ID
[**list_fields**](AccountInformationApi.md#list_fields) | **GET** /api/v1/meta/fields | List Fields
[**list_list_fields**](AccountInformationApi.md#list_list_fields) | **GET** /api/v1/meta/lists | List List Fields
[**list_tabular_fields**](AccountInformationApi.md#list_tabular_fields) | **GET** /api/v1/meta/tables | List Tabular Fields
[**list_users**](AccountInformationApi.md#list_users) | **GET** /api/v1/meta/users | List Users
[**update_list_field_values**](AccountInformationApi.md#update_list_field_values) | **PUT** /api/v1/meta/lists/{listFieldId} | Update List Field Values


# **baa7162824294d030115568d1d8e6ca7**
> TimezoneResource baa7162824294d030115568d1d8e6ca7(id)

Get timezone by ID

Retrieves a single timezone by its numeric ID. Returns the same timezone resource shape used by the list endpoint.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.timezone_resource import TimezoneResource
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
    api_instance = bamboohr_sdk.AccountInformationApi(api_client)
    id = 56 # int | The numeric ID of the timezone to retrieve.

    try:
        # Get timezone by ID
        api_response = api_instance.baa7162824294d030115568d1d8e6ca7(id)
        print("The response of AccountInformationApi->baa7162824294d030115568d1d8e6ca7:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountInformationApi->baa7162824294d030115568d1d8e6ca7: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The numeric ID of the timezone to retrieve. | 

### Return type

[**TimezoneResource**](TimezoneResource.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The timezone resource |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Timezone not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_10d66d8561dd7dac50ff9c21ef63d83b**
> TimezoneResource call_10d66d8561dd7dac50ff9c21ef63d83b(zip)

Get timezone by ZIP code

Retrieves the timezone for a US ZIP code. Returns the same timezone resource shape used by the list endpoint. Only US ZIP codes are supported; valid 5-digit ZIPs that are not present in our reference data return a 404.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.timezone_resource import TimezoneResource
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
    api_instance = bamboohr_sdk.AccountInformationApi(api_client)
    zip = '84604' # str | A 5-digit US ZIP code.

    try:
        # Get timezone by ZIP code
        api_response = api_instance.call_10d66d8561dd7dac50ff9c21ef63d83b(zip)
        print("The response of AccountInformationApi->call_10d66d8561dd7dac50ff9c21ef63d83b:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountInformationApi->call_10d66d8561dd7dac50ff9c21ef63d83b: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zip** | **str**| A 5-digit US ZIP code. | 

### Return type

[**TimezoneResource**](TimezoneResource.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The timezone resource |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | No timezone found for the provided ZIP code |  -  |
**422** | Invalid ZIP format |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_5c5fb0f1211ae1c9451753f92f1053b6**
> TimezoneListResponse call_5c5fb0f1211ae1c9451753f92f1053b6(page_size=page_size, page=page, sort=sort, select=select, filter=filter)

List timezones

Retrieves a paginated list of timezones. Supports pagination, filtering, sorting, and field projection via OData query parameters.

### Example


```python
import bamboohr_sdk
from bamboohr_sdk.models.timezone_list_response import TimezoneListResponse
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
    api_instance = bamboohr_sdk.AccountInformationApi(api_client)
    page_size = 500 # int | The number of items to return per page. (optional) (default to 500)
    page = 1 # int | The page number to retrieve. (optional) (default to 1)
    sort = '' # str | Ordering by OData (Open Data Protocol) v4 specification (optional) (default to '')
    select = '' # str | Projection (field selection) by OData specification (optional) (default to '')
    filter = '' # str | Filter by an OData (Open Data Protocol) v4 specification (optional) (default to '')

    try:
        # List timezones
        api_response = api_instance.call_5c5fb0f1211ae1c9451753f92f1053b6(page_size=page_size, page=page, sort=sort, select=select, filter=filter)
        print("The response of AccountInformationApi->call_5c5fb0f1211ae1c9451753f92f1053b6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountInformationApi->call_5c5fb0f1211ae1c9451753f92f1053b6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 500]
 **page** | **int**| The page number to retrieve. | [optional] [default to 1]
 **sort** | **str**| Ordering by OData (Open Data Protocol) v4 specification | [optional] [default to &#39;&#39;]
 **select** | **str**| Projection (field selection) by OData specification | [optional] [default to &#39;&#39;]
 **filter** | **str**| Filter by an OData (Open Data Protocol) v4 specification | [optional] [default to &#39;&#39;]

### Return type

[**TimezoneListResponse**](TimezoneListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of timezones |  -  |
**400** | Invalid query parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_currency_types**
> List[MetaCurrencyTypeItem] get_all_currency_types()

Get all currency types

Returns a JSON array of supported currency catalog entries. Each object includes `id`, `code`, `name`, `symbol` (display symbol), and `symbolPosition`—an integer discriminator: `0` = symbol before the amount (prefix) and `1` = after the amount (postfix), matching the values returned in the JSON body.

### Example

* Basic Authentication (basic):

```python
import bamboohr_sdk
from bamboohr_sdk.models.meta_currency_type_item import MetaCurrencyTypeItem
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

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.AccountInformationApi(api_client)

    try:
        # Get all currency types
        api_response = api_instance.get_all_currency_types()
        print("The response of AccountInformationApi->get_all_currency_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountInformationApi->get_all_currency_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MetaCurrencyTypeItem]**](MetaCurrencyTypeItem.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK with a JSON array of currency objects, each with &#x60;id&#x60;, &#x60;code&#x60;, &#x60;name&#x60;, &#x60;symbol&#x60;, and &#x60;symbolPosition&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_provinces**
> List[ProvinceItem] get_all_provinces()

Get All Provinces

Returns a flat list of all states and provinces across every country. Each entry includes a numeric ID, the countryId it belongs to, an abbreviation label (e.g. "UT"), an ISO 3166-2 code (e.g. "US-UT"), and a full name. Use the countryId field to filter client-side.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.province_item import ProvinceItem
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
    api_instance = bamboohr_sdk.AccountInformationApi(api_client)

    try:
        # Get All Provinces
        api_response = api_instance.get_all_provinces()
        print("The response of AccountInformationApi->get_all_provinces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountInformationApi->get_all_provinces: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ProvinceItem]**](ProvinceItem.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flat array of all states/provinces across all countries. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_countries_options**
> CountriesOptionsResponse get_countries_options(iso_code=iso_code)

Get Countries

Returns a JSON array of every country in the catalog, or a single country object when `isoCode` is supplied. Each element has `id` (Country ID), `name` (Country Name), and `isoCode` (ISO 3166-1 alpha-2 code or null when unset).

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.countries_options_response import CountriesOptionsResponse
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
    api_instance = bamboohr_sdk.AccountInformationApi(api_client)
    iso_code = 'iso_code_example' # str | ISO 3166-1 alpha-2 country code (exactly two letters). When present, returns the matching country as a single object instead of the full array. (optional)

    try:
        # Get Countries
        api_response = api_instance.get_countries_options(iso_code=iso_code)
        print("The response of AccountInformationApi->get_countries_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountInformationApi->get_countries_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iso_code** | **str**| ISO 3166-1 alpha-2 country code (exactly two letters). When present, returns the matching country as a single object instead of the full array. | [optional] 

### Return type

[**CountriesOptionsResponse**](CountriesOptionsResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | When &#x60;isoCode&#x60; is omitted: a JSON array of all country objects. When &#x60;isoCode&#x60; is provided: the matching country as a single object. |  -  |
**404** | No country found for the given &#x60;isoCode&#x60;. |  -  |
**422** | &#x60;isoCode&#x60; is present but malformed (not exactly two alpha characters). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meta_company**
> MetaCompanyPropertiesResponse get_meta_company()

Get company properties

Get company properties including ID, name, domain, and base API URL. Provides essential company metadata for API access.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.meta_company_properties_response import MetaCompanyPropertiesResponse
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
    api_instance = bamboohr_sdk.AccountInformationApi(api_client)

    try:
        # Get company properties
        api_response = api_instance.get_meta_company()
        print("The response of AccountInformationApi->get_meta_company:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountInformationApi->get_meta_company: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MetaCompanyPropertiesResponse**](MetaCompanyPropertiesResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Company id, name, domain, and baseApiUrl gateway URL. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_states_by_country_id**
> StateProvinceResponseSchema get_states_by_country_id(country_id)

List states and provinces for a country by Country ID

Returns the list of states or provinces for the specified country, sorted alphabetically by abbreviation (`options[].label`). Each item follows StateProvinceSchema: `label` is the subdivision abbreviation (e.g. "UT"), not the full name; `name` is the full subdivision name; `iso` is the ISO 3166-2 code (e.g. "US-UT"). Use a `countryId` from `GET /api/v1/meta/countries/options` (the `id` field on the row for the country) so it matches the countries list.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.state_province_response_schema import StateProvinceResponseSchema
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
    api_instance = bamboohr_sdk.AccountInformationApi(api_client)
    country_id = 56 # int | Numeric id of the country, taken from the countries options list. Use the `id` of the target country from `GET /api/v1/meta/countries/options`.

    try:
        # List states and provinces for a country by Country ID
        api_response = api_instance.get_states_by_country_id(country_id)
        print("The response of AccountInformationApi->get_states_by_country_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountInformationApi->get_states_by_country_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_id** | **int**| Numeric id of the country, taken from the countries options list. Use the &#x60;id&#x60; of the target country from &#x60;GET /api/v1/meta/countries/options&#x60;. | 

### Return type

[**StateProvinceResponseSchema**](StateProvinceResponseSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of states/provinces. The &#x60;options&#x60; array items match StateProvinceSchema; &#x60;label&#x60; is always the subdivision abbreviation used for sorting. |  -  |
**400** | The provided country ID is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fields**
> List[Field1] list_fields(accept_header_parameter=accept_header_parameter)

List Fields

Returns a list of all employee fields available in the account, including field ID, display name, data type, and whether the field is deprecated. Use this endpoint to discover which field names are valid for use with the Get Employee, Datasets, and other field-based endpoints. The response includes standard BambooHR fields as well as any custom fields configured in the account.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.field1 import Field1
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
    api_instance = bamboohr_sdk.AccountInformationApi(api_client)
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)

    try:
        # List Fields
        api_response = api_instance.list_fields(accept_header_parameter=accept_header_parameter)
        print("The response of AccountInformationApi->list_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountInformationApi->list_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 

### Return type

[**List[Field1]**](Field1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of all available employee fields in the account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_list_fields**
> List[ListFieldDetail] list_list_fields(format=format, accept_header_parameter=accept_header_parameter)

List List Fields

Returns details for all list fields in the account. Each list includes its field ID, alias, options, and whether it is manageable (editable). Lists with the `manageable` attribute set to `yes` can be modified via the PUT endpoint. Lists with the `multiple` attribute set to `yes` are fields that can have multiple values. Options with the `archived` attribute set to `yes` are soft-deleted and included so that historical data can reference the value — filter by `archived: no` to show only active options to end users.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.list_field_detail import ListFieldDetail
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
    api_instance = bamboohr_sdk.AccountInformationApi(api_client)
    format = 'format_example' # str | Set to \"json\" to receive JSON output as an alternative to using the Accept header. (optional)
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)

    try:
        # List List Fields
        api_response = api_instance.list_list_fields(format=format, accept_header_parameter=accept_header_parameter)
        print("The response of AccountInformationApi->list_list_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountInformationApi->list_list_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Set to \&quot;json\&quot; to receive JSON output as an alternative to using the Accept header. | [optional] 
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 

### Return type

[**List[ListFieldDetail]**](ListFieldDetail.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All list field details, including field IDs, option values, and manageability. |  -  |
**403** | The API user does not have permission to view employee fields. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tabular_fields**
> List[TabularField] list_tabular_fields(accept_header_parameter=accept_header_parameter)

List Tabular Fields

Returns a list of all tabular (table-based) fields available in the account. Each table includes its alias and the fields it contains with their IDs, names, and types. Use this endpoint to discover which table names are valid for the table row endpoints (e.g., jobInfo, compensation, employmentStatus). For fields whose type is `list`, `multilist`, or another option-backed type, the field `id` can be matched to `fieldId` from `list-list-fields` to retrieve the account-level option list.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.tabular_field import TabularField
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
    api_instance = bamboohr_sdk.AccountInformationApi(api_client)
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)

    try:
        # List Tabular Fields
        api_response = api_instance.list_tabular_fields(accept_header_parameter=accept_header_parameter)
        print("The response of AccountInformationApi->list_tabular_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountInformationApi->list_tabular_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 

### Return type

[**List[TabularField]**](TabularField.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of all tabular fields in the account, with each table&#39;s fields and their metadata. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> Dict[str, ListUsersResponseValue] list_users(accept_header_parameter=accept_header_parameter, status=status)

List Users

Returns all users for the company, optionally filtered by status. Each user entry includes a user ID, associated employee ID, name, email address (resolved in priority order: work, home, account), account status, and last login time when available.

Pass a comma-separated list of status values via the `status` query parameter to filter results. Valid values are `enabled` and `disabled`. If the parameter is omitted or contains only unrecognized values, users of all statuses are returned. Support admin accounts are always excluded from the response.

The response format is determined by the `Accept` request header. Send `Accept: application/json` to receive JSON; omit the header or send any other value to receive XML.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.list_users_response_value import ListUsersResponseValue
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
    api_instance = bamboohr_sdk.AccountInformationApi(api_client)
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)
    status = 'enabled' # str | Comma-separated list of statuses to filter by. Valid values: `enabled`, `disabled`. Defaults to returning users of all statuses when omitted or when no recognized value is provided. (optional)

    try:
        # List Users
        api_response = api_instance.list_users(accept_header_parameter=accept_header_parameter, status=status)
        print("The response of AccountInformationApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountInformationApi->list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 
 **status** | **str**| Comma-separated list of statuses to filter by. Valid values: &#x60;enabled&#x60;, &#x60;disabled&#x60;. Defaults to returning users of all statuses when omitted or when no recognized value is provided. | [optional] 

### Return type

[**Dict[str, ListUsersResponseValue]**](ListUsersResponseValue.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object whose keys are user IDs (as strings) and whose values are user objects. When the Accept header requests XML, a &#x60;&lt;users&gt;&#x60; document is returned instead. |  -  |
**401** | Unauthorized. The API key is missing or invalid. |  -  |
**403** | Forbidden. The caller does not have permission to access this endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_list_field_values**
> ListFieldDetail update_list_field_values(list_field_id, list_field_values, format=format)

Update List Field Values

Create, update, or archive options for a list field. To update an existing option, specify its `id`. To create a new option, omit `id`. To archive an option, set `archived` to `yes` — the option is soft-deleted and will continue to appear in GET responses for historical data integrity. To reactivate an archived option, set `archived` to `no`. The `archivedDate` field is server-set when an option is first archived and is not cleared if the option is later reactivated. Options on list fields with `manageable: no` cannot be modified and will return a 405.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.list_field_detail import ListFieldDetail
from bamboohr_sdk.models.list_field_values import ListFieldValues
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
    api_instance = bamboohr_sdk.AccountInformationApi(api_client)
    list_field_id = 'list_field_id_example' # str | The field ID of the list to update. This is the `fieldId` value returned by the GET endpoint, not the list `id`.
    list_field_values = bamboohr_sdk.ListFieldValues() # ListFieldValues | 
    format = 'format_example' # str | Set to \"json\" to receive JSON output as an alternative to using the Accept header. (optional)

    try:
        # Update List Field Values
        api_response = api_instance.update_list_field_values(list_field_id, list_field_values, format=format)
        print("The response of AccountInformationApi->update_list_field_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountInformationApi->update_list_field_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_field_id** | **str**| The field ID of the list to update. This is the &#x60;fieldId&#x60; value returned by the GET endpoint, not the list &#x60;id&#x60;. | 
 **list_field_values** | [**ListFieldValues**](ListFieldValues.md)|  | 
 **format** | **str**| Set to \&quot;json\&quot; to receive JSON output as an alternative to using the Accept header. | [optional] 

### Return type

[**ListFieldDetail**](ListFieldDetail.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All requested changes were applied. Returns the full updated list. |  -  |
**400** | The request body is invalid or malformed. |  -  |
**403** | The list is not editable, or the API user does not have sufficient permissions. |  -  |
**404** | The specified list field or option ID does not exist. |  -  |
**405** | One or more of the specified options belong to a non-manageable list field and cannot be modified. |  -  |
**409** | A duplicate list value conflicted with the value specified. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

