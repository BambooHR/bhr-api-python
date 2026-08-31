# bamboohr_sdk.CustomFieldsApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_custom_field_list_value**](CustomFieldsApi.md#add_custom_field_list_value) | **POST** /api/v1/hris/custom-fields/{customFieldId}/list-values | Add Custom Field List Value
[**archive_public_custom_field**](CustomFieldsApi.md#archive_public_custom_field) | **DELETE** /api/v1/hris/custom-fields/{customFieldId} | Archive Custom Field
[**create_public_custom_field**](CustomFieldsApi.md#create_public_custom_field) | **POST** /api/v1/hris/custom-fields | Create Custom Field
[**delete_custom_field_list_value**](CustomFieldsApi.md#delete_custom_field_list_value) | **DELETE** /api/v1/hris/custom-fields/{customFieldId}/list-values/{listValueId} | Delete Custom Field List Value
[**edit_custom_field_list_value**](CustomFieldsApi.md#edit_custom_field_list_value) | **PATCH** /api/v1/hris/custom-fields/{customFieldId}/list-values/{listValueId} | Edit Custom Field List Value
[**edit_public_custom_field**](CustomFieldsApi.md#edit_public_custom_field) | **PUT** /api/v1/hris/custom-fields/{customFieldId} | Edit Custom Field
[**get_custom_field**](CustomFieldsApi.md#get_custom_field) | **GET** /api/v1/hris/custom-fields/{customFieldId} | Get Custom Field
[**list_archived_custom_fields**](CustomFieldsApi.md#list_archived_custom_fields) | **GET** /api/v1/hris/custom-fields/archived | List Archived Custom Fields
[**list_custom_field_list_values**](CustomFieldsApi.md#list_custom_field_list_values) | **GET** /api/v1/hris/custom-fields/{customFieldId}/list-values | List Custom Field List Values
[**list_custom_field_types**](CustomFieldsApi.md#list_custom_field_types) | **GET** /api/v1/hris/custom-fields/types | List Custom Field Types
[**list_custom_fields**](CustomFieldsApi.md#list_custom_fields) | **GET** /api/v1/hris/custom-fields | List Custom Fields
[**unarchive_public_custom_fields**](CustomFieldsApi.md#unarchive_public_custom_fields) | **POST** /api/v1/hris/custom-fields/unarchive | Unarchive Custom Fields


# **add_custom_field_list_value**
> AddCustomFieldListValueResponse add_custom_field_list_value(custom_field_id, add_custom_field_list_value_request)

Add Custom Field List Value

Adds one or more dropdown options to a list-type custom field.

OAuth Scopes: employee:custom_fields.write

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.add_custom_field_list_value_request import AddCustomFieldListValueRequest
from bamboohr_sdk.models.add_custom_field_list_value_response import AddCustomFieldListValueResponse
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
    api_instance = bamboohr_sdk.CustomFieldsApi(api_client)
    custom_field_id = '123' # str | The ID of the custom field.
    add_custom_field_list_value_request = bamboohr_sdk.AddCustomFieldListValueRequest() # AddCustomFieldListValueRequest | 

    try:
        # Add Custom Field List Value
        api_response = api_instance.add_custom_field_list_value(custom_field_id, add_custom_field_list_value_request)
        print("The response of CustomFieldsApi->add_custom_field_list_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->add_custom_field_list_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_id** | **str**| The ID of the custom field. | 
 **add_custom_field_list_value_request** | [**AddCustomFieldListValueRequest**](AddCustomFieldListValueRequest.md)|  | 

### Return type

[**AddCustomFieldListValueResponse**](AddCustomFieldListValueResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | List value(s) added. A single \&quot;option\&quot; in the request body returns one object; a \&quot;values\&quot; array returns an array of objects. |  -  |
**400** | Invalid argument. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not found. |  -  |
**422** | Validation failed. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_public_custom_field**
> ArchiveCustomFieldResponse archive_public_custom_field(custom_field_id)

Archive Custom Field

Archive a custom field.

OAuth Scopes: employee:custom_fields.write

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.archive_custom_field_response import ArchiveCustomFieldResponse
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
    api_instance = bamboohr_sdk.CustomFieldsApi(api_client)
    custom_field_id = '123' # str | The ID of the custom field to archive.

    try:
        # Archive Custom Field
        api_response = api_instance.archive_public_custom_field(custom_field_id)
        print("The response of CustomFieldsApi->archive_public_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->archive_public_custom_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_id** | **str**| The ID of the custom field to archive. | 

### Return type

[**ArchiveCustomFieldResponse**](ArchiveCustomFieldResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom field archived. |  -  |
**400** | Invalid argument. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not found. |  -  |
**409** | Conflict. |  -  |
**422** | Validation failed. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_public_custom_field**
> CustomFieldViewObject create_public_custom_field(custom_field_request)

Create Custom Field

Create a new custom field.

OAuth Scopes: employee:custom_fields.write

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.custom_field_request import CustomFieldRequest
from bamboohr_sdk.models.custom_field_view_object import CustomFieldViewObject
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
    api_instance = bamboohr_sdk.CustomFieldsApi(api_client)
    custom_field_request = bamboohr_sdk.CustomFieldRequest() # CustomFieldRequest | 

    try:
        # Create Custom Field
        api_response = api_instance.create_public_custom_field(custom_field_request)
        print("The response of CustomFieldsApi->create_public_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->create_public_custom_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_request** | [**CustomFieldRequest**](CustomFieldRequest.md)|  | 

### Return type

[**CustomFieldViewObject**](CustomFieldViewObject.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom field created. |  -  |
**400** | Invalid argument. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not found. |  -  |
**422** | Validation failed. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_field_list_value**
> delete_custom_field_list_value(custom_field_id, list_value_id)

Delete Custom Field List Value

Deletes a dropdown option from a list-type custom field.

OAuth Scopes: employee:custom_fields.write

### Example

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with bamboohr_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bamboohr_sdk.CustomFieldsApi(api_client)
    custom_field_id = '123' # str | The ID of the custom field.
    list_value_id = '456' # str | The ID of the list value to delete.

    try:
        # Delete Custom Field List Value
        api_instance.delete_custom_field_list_value(custom_field_id, list_value_id)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->delete_custom_field_list_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_id** | **str**| The ID of the custom field. | 
 **list_value_id** | **str**| The ID of the list value to delete. | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | List value deleted. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not found. |  -  |
**409** | Conflict — list value is still assigned to employees. |  -  |
**422** | Validation failed. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_custom_field_list_value**
> ListValueViewObject edit_custom_field_list_value(custom_field_id, list_value_id, change_custom_field_list_value_request)

Edit Custom Field List Value

Updates a dropdown option on a list-type custom field.

OAuth Scopes: employee:custom_fields.write

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.change_custom_field_list_value_request import ChangeCustomFieldListValueRequest
from bamboohr_sdk.models.list_value_view_object import ListValueViewObject
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
    api_instance = bamboohr_sdk.CustomFieldsApi(api_client)
    custom_field_id = '123' # str | The ID of the custom field.
    list_value_id = '456' # str | The ID of the list value to edit.
    change_custom_field_list_value_request = bamboohr_sdk.ChangeCustomFieldListValueRequest() # ChangeCustomFieldListValueRequest | 

    try:
        # Edit Custom Field List Value
        api_response = api_instance.edit_custom_field_list_value(custom_field_id, list_value_id, change_custom_field_list_value_request)
        print("The response of CustomFieldsApi->edit_custom_field_list_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->edit_custom_field_list_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_id** | **str**| The ID of the custom field. | 
 **list_value_id** | **str**| The ID of the list value to edit. | 
 **change_custom_field_list_value_request** | [**ChangeCustomFieldListValueRequest**](ChangeCustomFieldListValueRequest.md)|  | 

### Return type

[**ListValueViewObject**](ListValueViewObject.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List value edited. |  -  |
**400** | Invalid argument. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not found. |  -  |
**415** | Unsupported media type. Content-Type must be application/merge-patch+json. |  -  |
**422** | Validation failed. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_public_custom_field**
> CustomFieldViewObject edit_public_custom_field(custom_field_id, custom_field_request)

Edit Custom Field

Edit an existing custom field.

OAuth Scopes: employee:custom_fields.write

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.custom_field_request import CustomFieldRequest
from bamboohr_sdk.models.custom_field_view_object import CustomFieldViewObject
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
    api_instance = bamboohr_sdk.CustomFieldsApi(api_client)
    custom_field_id = '123' # str | The ID of the custom field to edit.
    custom_field_request = bamboohr_sdk.CustomFieldRequest() # CustomFieldRequest | 

    try:
        # Edit Custom Field
        api_response = api_instance.edit_public_custom_field(custom_field_id, custom_field_request)
        print("The response of CustomFieldsApi->edit_public_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->edit_public_custom_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_id** | **str**| The ID of the custom field to edit. | 
 **custom_field_request** | [**CustomFieldRequest**](CustomFieldRequest.md)|  | 

### Return type

[**CustomFieldViewObject**](CustomFieldViewObject.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom field edited. |  -  |
**400** | Invalid argument. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not found. |  -  |
**422** | Validation failed. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_field**
> CustomFieldDefinitionResponseObject get_custom_field(custom_field_id)

Get Custom Field

Returns one custom field definition. IDs are strings and each has a numeric `legacyId` companion for legacy integrations. Use this for a known custom field ID. For browsing active fields, use List Custom Fields (`list-custom-fields`) instead. For archived fields, use List Archived Custom Fields (`list-archived-custom-fields`) instead.

OAuth Scopes: employee:custom_fields

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.custom_field_definition_response_object import CustomFieldDefinitionResponseObject
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
    api_instance = bamboohr_sdk.CustomFieldsApi(api_client)
    custom_field_id = '123' # str | The ID of the custom field to retrieve

    try:
        # Get Custom Field
        api_response = api_instance.get_custom_field(custom_field_id)
        print("The response of CustomFieldsApi->get_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->get_custom_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_id** | **str**| The ID of the custom field to retrieve | 

### Return type

[**CustomFieldDefinitionResponseObject**](CustomFieldDefinitionResponseObject.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom field definition. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not found. |  -  |
**422** | Invalid argument. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_archived_custom_fields**
> ArchivedCustomFieldsListResponse list_archived_custom_fields(page=page, page_size=page_size)

List Archived Custom Fields

Returns a paginated list of archived custom fields. IDs are strings and each has a numeric `legacyId` companion for legacy integrations. Use this for archived custom fields. For active custom fields, use List Custom Fields (`list-custom-fields`) instead.

OAuth Scopes: employee:custom_fields

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.archived_custom_fields_list_response import ArchivedCustomFieldsListResponse
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
    api_instance = bamboohr_sdk.CustomFieldsApi(api_client)
    page = 1 # int | Page number to retrieve. Must be greater than or equal to 1. (optional) (default to 1)
    page_size = 100 # int | Maximum number of archived custom fields to return per page. (optional) (default to 100)

    try:
        # List Archived Custom Fields
        api_response = api_instance.list_archived_custom_fields(page=page, page_size=page_size)
        print("The response of CustomFieldsApi->list_archived_custom_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->list_archived_custom_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number to retrieve. Must be greater than or equal to 1. | [optional] [default to 1]
 **page_size** | **int**| Maximum number of archived custom fields to return per page. | [optional] [default to 100]

### Return type

[**ArchivedCustomFieldsListResponse**](ArchivedCustomFieldsListResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of archived custom fields. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**422** | Invalid pagination. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custom_field_list_values**
> PublicListValuesCustomFieldSettingsResponse list_custom_field_list_values(custom_field_id)

List Custom Field List Values

Returns the dropdown options (and employee counts) for a list-type custom field.

OAuth Scopes: employee:custom_fields

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.public_list_values_custom_field_settings_response import PublicListValuesCustomFieldSettingsResponse
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
    api_instance = bamboohr_sdk.CustomFieldsApi(api_client)
    custom_field_id = '123' # str | The ID of the custom field.

    try:
        # List Custom Field List Values
        api_response = api_instance.list_custom_field_list_values(custom_field_id)
        print("The response of CustomFieldsApi->list_custom_field_list_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->list_custom_field_list_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_id** | **str**| The ID of the custom field. | 

### Return type

[**PublicListValuesCustomFieldSettingsResponse**](PublicListValuesCustomFieldSettingsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom field list values and counts. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not found. |  -  |
**422** | Invalid custom field ID. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custom_field_types**
> PublicCustomFieldTypesResponse list_custom_field_types()

List Custom Field Types

Returns an object containing the custom field types available when creating a custom field.

OAuth Scopes: employee:custom_fields

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.public_custom_field_types_response import PublicCustomFieldTypesResponse
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
    api_instance = bamboohr_sdk.CustomFieldsApi(api_client)

    try:
        # List Custom Field Types
        api_response = api_instance.list_custom_field_types()
        print("The response of CustomFieldsApi->list_custom_field_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->list_custom_field_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PublicCustomFieldTypesResponse**](PublicCustomFieldTypesResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom field types. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custom_fields**
> CustomFieldsListResponse list_custom_fields(page=page, page_size=page_size)

List Custom Fields

Returns a paginated list of active custom fields. IDs are strings and each has a numeric `legacyId` companion for legacy integrations. Use this for active custom fields. For archived custom fields, use List Archived Custom Fields (`list-archived-custom-fields`) instead.

OAuth Scopes: employee:custom_fields

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.custom_fields_list_response import CustomFieldsListResponse
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
    api_instance = bamboohr_sdk.CustomFieldsApi(api_client)
    page = 1 # int | Page number to retrieve. Must be greater than or equal to 1. (optional) (default to 1)
    page_size = 100 # int | Maximum number of custom fields to return per page. (optional) (default to 100)

    try:
        # List Custom Fields
        api_response = api_instance.list_custom_fields(page=page, page_size=page_size)
        print("The response of CustomFieldsApi->list_custom_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->list_custom_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number to retrieve. Must be greater than or equal to 1. | [optional] [default to 1]
 **page_size** | **int**| Maximum number of custom fields to return per page. | [optional] [default to 100]

### Return type

[**CustomFieldsListResponse**](CustomFieldsListResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of active custom fields. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**422** | Invalid pagination. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unarchive_public_custom_fields**
> UnarchiveCustomFieldsResponse unarchive_public_custom_fields(unarchive_custom_fields_request)

Unarchive Custom Fields

Unarchive custom fields.

OAuth Scopes: employee:custom_fields.write

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.unarchive_custom_fields_request import UnarchiveCustomFieldsRequest
from bamboohr_sdk.models.unarchive_custom_fields_response import UnarchiveCustomFieldsResponse
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
    api_instance = bamboohr_sdk.CustomFieldsApi(api_client)
    unarchive_custom_fields_request = bamboohr_sdk.UnarchiveCustomFieldsRequest() # UnarchiveCustomFieldsRequest | 

    try:
        # Unarchive Custom Fields
        api_response = api_instance.unarchive_public_custom_fields(unarchive_custom_fields_request)
        print("The response of CustomFieldsApi->unarchive_public_custom_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldsApi->unarchive_public_custom_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unarchive_custom_fields_request** | [**UnarchiveCustomFieldsRequest**](UnarchiveCustomFieldsRequest.md)|  | 

### Return type

[**UnarchiveCustomFieldsResponse**](UnarchiveCustomFieldsResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Invalid argument. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |
**404** | Not found. |  -  |
**409** | Conflict. |  -  |
**422** | Validation failed. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

