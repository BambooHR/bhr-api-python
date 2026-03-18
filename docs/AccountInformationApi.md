# bamboohr_sdk.AccountInformationApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call_5c5fb0f1211ae1c9451753f92f1053b6**](AccountInformationApi.md#call_5c5fb0f1211ae1c9451753f92f1053b6) | **GET** /api/v1/meta/timezones | List timezones
[**get_countries_options**](AccountInformationApi.md#get_countries_options) | **GET** /api/v1/meta/countries/options | Get Countries
[**get_states_by_country_id**](AccountInformationApi.md#get_states_by_country_id) | **GET** /api/v1/meta/provinces/{countryId} | Get States by Country ID
[**list_fields**](AccountInformationApi.md#list_fields) | **GET** /api/v1/meta/fields | List Fields
[**list_list_fields**](AccountInformationApi.md#list_list_fields) | **GET** /api/v1/meta/lists | List List Fields
[**list_tabular_fields**](AccountInformationApi.md#list_tabular_fields) | **GET** /api/v1/meta/tables | List Tabular Fields
[**list_users**](AccountInformationApi.md#list_users) | **GET** /api/v1/meta/users | List Users
[**update_list_field_values**](AccountInformationApi.md#update_list_field_values) | **PUT** /api/v1/meta/lists/{listFieldId} | Update List Field Values


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

# **get_countries_options**
> List[CountrySchema] get_countries_options()

Get Countries

Returns the full list of countries supported by BambooHR, each with a numeric string ID, full name, and ISO 3166-1 alpha-2 code. The returned IDs can be passed to the Get States by Country ID endpoint to retrieve the corresponding states or provinces.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.country_schema import CountrySchema
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

    try:
        # Get Countries
        api_response = api_instance.get_countries_options()
        print("The response of AccountInformationApi->get_countries_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountInformationApi->get_countries_options: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CountrySchema]**](CountrySchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all supported countries. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_states_by_country_id**
> StateProvinceResponseSchema get_states_by_country_id(country_id)

Get States by Country ID

Returns the list of states or provinces for the specified country, sorted alphabetically by abbreviation. Each entry includes a numeric ID, an abbreviation label (e.g. "UT"), an ISO 3166-2 code (e.g. "US-UT"), and a full name. Pass the country ID from the Get Countries endpoint to retrieve its subdivisions.

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
    country_id = 56 # int | The numeric ID of the country whose states or provinces to retrieve. Use the Get Countries endpoint to look up valid country IDs.

    try:
        # Get States by Country ID
        api_response = api_instance.get_states_by_country_id(country_id)
        print("The response of AccountInformationApi->get_states_by_country_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountInformationApi->get_states_by_country_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_id** | **int**| The numeric ID of the country whose states or provinces to retrieve. Use the Get Countries endpoint to look up valid country IDs. | 

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
**200** | List of states/provinces for the specified country. |  -  |
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

Returns details for all list fields in the account. Each list includes its field ID, alias, options, and whether it is manageable (editable). Lists with the `manageable` attribute set to `yes` can be modified via the PUT endpoint. Lists with the `multiple` attribute set to `yes` are fields that can have multiple values. Options with the `archived` attribute set to `yes` should not appear as current options, but are included so that historical data can reference the value.

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

Returns a list of all tabular (table-based) fields available in the account. Each table includes its alias and the fields it contains with their IDs, names, and types. Use this endpoint to discover which table names are valid for the table row endpoints (e.g., jobInfo, compensation, employmentStatus).

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
> ListFieldDetail update_list_field_values(list_field_id, list_field_values)

Update List Field Values

Create, update, or archive options for a list field. To update an existing option, specify its ID. To create a new option, omit the `id` attribute. To archive an option while preserving it for historical data, set the `archived` attribute to `yes`.

Response format note: A successful response returns the full updated list in XML format.

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
    list_field_id = 'list_field_id_example' # str | The ID of the list field to update.
    list_field_values = bamboohr_sdk.ListFieldValues() # ListFieldValues | 

    try:
        # Update List Field Values
        api_response = api_instance.update_list_field_values(list_field_id, list_field_values)
        print("The response of AccountInformationApi->update_list_field_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountInformationApi->update_list_field_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_field_id** | **str**| The ID of the list field to update. | 
 **list_field_values** | [**ListFieldValues**](ListFieldValues.md)|  | 

### Return type

[**ListFieldDetail**](ListFieldDetail.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All requested changes were applied. Returns the full updated list of options for the specified list field as XML. |  -  |
**400** | The posted JSON is invalid or malformed. |  -  |
**403** | The list is not editable, or the API user does not have sufficient permissions. |  -  |
**404** | The specified list field or option ID does not exist. |  -  |
**409** | A duplicate list value conflicted with the value specified. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

