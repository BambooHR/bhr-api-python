# bamboohr_sdk.AccountInformationApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_countries_options**](AccountInformationApi.md#get_countries_options) | **GET** /api/v1/meta/countries/options | Get Countries
[**get_list_of_users**](AccountInformationApi.md#get_list_of_users) | **GET** /api/v1/meta/users | Get Users
[**get_states_by_country_id**](AccountInformationApi.md#get_states_by_country_id) | **GET** /api/v1/meta/provinces/{countryId} | Get States by Country ID
[**metadata_add_or_update_values_for_list_fields**](AccountInformationApi.md#metadata_add_or_update_values_for_list_fields) | **PUT** /api/v1/meta/lists/{listFieldId} | Create or Update List Field Values
[**metadata_get_a_list_of_fields**](AccountInformationApi.md#metadata_get_a_list_of_fields) | **GET** /api/v1/meta/fields | Get Fields
[**metadata_get_a_list_of_tabular_fields**](AccountInformationApi.md#metadata_get_a_list_of_tabular_fields) | **GET** /api/v1/meta/tables | Get Tabular Fields
[**metadata_get_details_for_list_fields**](AccountInformationApi.md#metadata_get_details_for_list_fields) | **GET** /api/v1/meta/lists | Get List Field Details


# **get_countries_options**
> List[CountrySchema] get_countries_options()

Get Countries

Get all available countries as options. Returns a list of countries with ID and name for use in forms and dropdowns.

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
**200** | Countries retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_of_users**
> get_list_of_users()

Get Users

Retrieves a list of all active users in the system with their basic information. This includes user IDs, names, and email addresses. The list can be used to map user IDs to user information throughout the API.

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
    api_instance = bamboohr_sdk.AccountInformationApi(api_client)

    try:
        # Get Users
        api_instance.get_list_of_users()
    except Exception as e:
        print("Exception when calling AccountInformationApi->get_list_of_users: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_states_by_country_id**
> StateProvinceResponseSchema get_states_by_country_id(country_id)

Get States by Country ID

Get states/provinces for a specific country. Returns a list of state/province options with ID, label, ISO code, and name.

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
    country_id = 56 # int | ID of the country to get states/provinces for

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
 **country_id** | **int**| ID of the country to get states/provinces for | 

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
**200** | States/provinces retrieved successfully |  -  |
**400** | Invalid country ID provided |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_add_or_update_values_for_list_fields**
> metadata_add_or_update_values_for_list_fields(list_field_id, list_field_values)

Create or Update List Field Values

This resource accepts one or more options. To update an option, specify an ID. You may also remove an option from the list of current values by archiving the value. To create a new option, do not specify an "id" attribute.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
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
    list_field_id = 'list_field_id_example' # str | 
    list_field_values = bamboohr_sdk.ListFieldValues() # ListFieldValues | 

    try:
        # Create or Update List Field Values
        api_instance.metadata_add_or_update_values_for_list_fields(list_field_id, list_field_values)
    except Exception as e:
        print("Exception when calling AccountInformationApi->metadata_add_or_update_values_for_list_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_field_id** | **str**|  | 
 **list_field_values** | [**ListFieldValues**](ListFieldValues.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/xml, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response indicates that all the requested changes were made. The content of the response will be the full list of options for the specified listId. |  -  |
**400** | The posted JSON is invalid. |  -  |
**403** | List is not editable or insufficient permissions. |  -  |
**404** | A non-existant list value or option ID is specified. |  -  |
**409** | A duplicate list value conflicted with the value specified. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_get_a_list_of_fields**
> metadata_get_a_list_of_fields(accept_header_parameter=accept_header_parameter)

Get Fields

This endpoint can help with discovery of fields that are available in an account.

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
    api_instance = bamboohr_sdk.AccountInformationApi(api_client)
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)

    try:
        # Get Fields
        api_instance.metadata_get_a_list_of_fields(accept_header_parameter=accept_header_parameter)
    except Exception as e:
        print("Exception when calling AccountInformationApi->metadata_get_a_list_of_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All fields available in BambooHR. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_get_a_list_of_tabular_fields**
> metadata_get_a_list_of_tabular_fields(accept_header_parameter=accept_header_parameter)

Get Tabular Fields

This endpoint can help discover table fields available in your BambooHR account.

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
    api_instance = bamboohr_sdk.AccountInformationApi(api_client)
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)

    try:
        # Get Tabular Fields
        api_instance.metadata_get_a_list_of_tabular_fields(accept_header_parameter=accept_header_parameter)
    except Exception as e:
        print("Exception when calling AccountInformationApi->metadata_get_a_list_of_tabular_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All table fields available in BambooHR |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_get_details_for_list_fields**
> metadata_get_details_for_list_fields(accept_header_parameter=accept_header_parameter)

Get List Field Details

This endpoint will return details for all list fields. Lists that can be edited will have the "manageable" attribute set to yes. Lists with the "multiple" attribute set to yes are fields that can have multiple values. Options with the "archived" attribute set to yes should not appear as current options, but are included so that historical data can reference the value.

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
    api_instance = bamboohr_sdk.AccountInformationApi(api_client)
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)

    try:
        # Get List Field Details
        api_instance.metadata_get_details_for_list_fields(accept_header_parameter=accept_header_parameter)
    except Exception as e:
        print("Exception when calling AccountInformationApi->metadata_get_details_for_list_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All details for list fields available in BambooHR |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

