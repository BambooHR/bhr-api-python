# bamboohr_sdk.DatasetsApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_from_dataset**](DatasetsApi.md#get_data_from_dataset) | **POST** /api/v1/datasets/{datasetName} | Get Data from Dataset
[**get_datasets**](DatasetsApi.md#get_datasets) | **GET** /api/v1/datasets | Get Datasets
[**get_datasets_v12**](DatasetsApi.md#get_datasets_v12) | **GET** /api/v1_2/datasets | Get Datasets v1.2
[**get_field_options**](DatasetsApi.md#get_field_options) | **POST** /api/v1/datasets/{datasetName}/field-options | Get Field Options
[**get_field_options_v12**](DatasetsApi.md#get_field_options_v12) | **POST** /api/v1_2/datasets/{datasetName}/field-options | Get Field Options v1.2
[**get_fields_from_dataset**](DatasetsApi.md#get_fields_from_dataset) | **GET** /api/v1/datasets/{datasetName}/fields | Get Fields from Dataset
[**get_fields_from_dataset_v12**](DatasetsApi.md#get_fields_from_dataset_v12) | **GET** /api/v1_2/datasets/{datasetName}/fields | Get Fields from Dataset v1.2


# **get_data_from_dataset**
> EmployeeResponse get_data_from_dataset(dataset_name, data_request, page=page, page_size=page_size)

Get Data from Dataset

Retrieve data from the specified dataset. You must provide a list of fields to return; use GET /api/v1/datasets/{datasetName}/fields to discover available field names. Returns a paginated list of records under the `data` key, along with optional `aggregations` and a `pagination` block.

Results default to 500 records per page. Use the `page` and `page_size` query parameters to paginate through large result sets.

**Deprecation notice:** This endpoint is deprecated. Use POST /api/v2/datasets/{datasetName}/data instead.

***Field Settings:***

**Show History**
When any of the fields included in your request are historical table fields, you may include the `showHistory` setting. Example: `"showHistory":["entityName"]`. Entity Name can be found in the GET /api/v1/datasets/{datasetName}/fields endpoint.

**Sort By:**
Pass multiple fields to sort by as an array of objects `{field: "fieldName", sort: "asc"}`. The order of the fields in the array determines the sort priority.

**Group By:**
Passed as an array of strings. Currently grouping by more than one field is not supported.

**Aggregations:**
When using aggregations the following aggregates are available based on field type:
  - **text**: count
  - **date**: count, min, max
  - **int**: count, min, max, sum, avg
  - **bool**: count
  - **options**: count
  - **govIdText**: count

**Filters:**
When using filters, the filtered field does not have to be in the list of fields you want to show on the report.

**Important Filter Notes:**
  - **List filter values** (for `options` field type using `includes` or `does_not_include` operators) must be enclosed in square brackets [ ]. Example: `["value1", "value2"]`
  - **Future hires**: Future hires have a status of `Inactive` in the datasets API. To include future hires in your results, you must include `Inactive` in your status filter.

Use GET /api/v1/datasets/{datasetName}/field-options to retrieve possible filter values for fields. Use the `id` returned from the field-options endpoint.

**Filter Operators by Field Type:**
  - **text**: contains, does_not_contain, equal, not_equal, empty, not_empty
  - **date**: lt, lte, gt, gte, equal, not_equal, empty, not_empty, last (value: `{"duration": "5", "unit": "years"}`), next, range (value: `{"start": "2023-01-01", "end": "2023-12-31"}`)
  - **int**: equal, not_equal, gte, gt, lte, lt, empty, not_empty
  - **bool**: checked, not_checked
  - **options**: includes, does_not_include, empty, not_empty
  - **govIdText**: empty, not_empty


### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.data_request import DataRequest
from bamboohr_sdk.models.employee_response import EmployeeResponse
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
    api_instance = bamboohr_sdk.DatasetsApi(api_client)
    dataset_name = 'dataset_name_example' # str | The name of the dataset you want data from
    data_request = bamboohr_sdk.DataRequest() # DataRequest | 
    page = 1 # int | The page number to retrieve. Defaults to 1. (optional) (default to 1)
    page_size = 500 # int | The number of records to retrieve per page. Defaults to 500. Maximum is 1000. (optional) (default to 500)

    try:
        # Get Data from Dataset
        api_response = api_instance.get_data_from_dataset(dataset_name, data_request, page=page, page_size=page_size)
        print("The response of DatasetsApi->get_data_from_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_data_from_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**| The name of the dataset you want data from | 
 **data_request** | [**DataRequest**](DataRequest.md)|  | 
 **page** | **int**| The page number to retrieve. Defaults to 1. | [optional] [default to 1]
 **page_size** | **int**| The number of records to retrieve per page. Defaults to 500. Maximum is 1000. | [optional] [default to 500]

### Return type

[**EmployeeResponse**](EmployeeResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data from the dataset successfully requested |  -  |
**400** | Invalid or missing argument(s) |  -  |
**403** | You do not have permissions to hit this endpoint |  -  |
**500** | An unexpected error occurred while getting the data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasets**
> DatasetResponse get_datasets()

Get Datasets

Retrieve the list of available datasets that can be queried. Returns each dataset's machine-readable name (used in subsequent dataset API calls) and its human-readable label. Use the returned `name` values with POST /api/v1/datasets/{datasetName} to query data, and GET /api/v1/datasets/{datasetName}/fields to discover available fields.

**Deprecation notice:** This endpoint is deprecated. Use GET /api/v1_2/datasets instead.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.dataset_response import DatasetResponse
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
    api_instance = bamboohr_sdk.DatasetsApi(api_client)

    try:
        # Get Datasets
        api_response = api_instance.get_datasets()
        print("The response of DatasetsApi->get_datasets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_datasets: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DatasetResponse**](DatasetResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of datasets |  -  |
**403** | You do not have permissions to hit this endpoint |  -  |
**500** | Internal error getting the datasets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasets_v12**
> DatasetsResponse get_datasets_v12()

Get Datasets v1.2

Retrieve the list of available datasets that can be queried. Returns each dataset's machine-readable name (used in subsequent dataset API calls) and its human-readable label. Use the returned `name` values with POST /api/v1/datasets/{datasetName} to query data, and GET /api/v1_2/datasets/{datasetName}/fields to discover available fields. V1.2 endpoint: error responses use RFC 7807 `application/problem+json`.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.datasets_response import DatasetsResponse
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
    api_instance = bamboohr_sdk.DatasetsApi(api_client)

    try:
        # Get Datasets v1.2
        api_response = api_instance.get_datasets_v12()
        print("The response of DatasetsApi->get_datasets_v12:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_datasets_v12: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DatasetsResponse**](DatasetsResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved list of available datasets |  * X-Request-ID - Correlation ID for request tracing <br>  |
**403** | Forbidden - insufficient permissions to access datasets |  -  |
**500** | Internal server error while retrieving datasets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_field_options**
> Dict[str, List[FieldOptionsTransformer]] get_field_options(dataset_name, field_options_request_schema)

Get Field Options

Retrieve the possible values for one or more dataset fields, for use as filter values in dataset queries. Pass the field names you want options for in the `fields` array. The response is an object keyed by field name, where each value is an array of `{id, value}` objects. Use the `id` values as filter values when querying POST /api/v1/datasets/{datasetName}. Optionally supply `filters` to scope the returned options (e.g., returning only option values that exist for active employees).

**Deprecation notice:** For RFC 7807 compliant error responses, use POST /api/v1_2/datasets/{datasetName}/field-options instead.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.field_options_request_schema import FieldOptionsRequestSchema
from bamboohr_sdk.models.field_options_transformer import FieldOptionsTransformer
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
    api_instance = bamboohr_sdk.DatasetsApi(api_client)
    dataset_name = 'dataset_name_example' # str | The name of the dataset you want to see field options for
    field_options_request_schema = bamboohr_sdk.FieldOptionsRequestSchema() # FieldOptionsRequestSchema | 

    try:
        # Get Field Options
        api_response = api_instance.get_field_options(dataset_name, field_options_request_schema)
        print("The response of DatasetsApi->get_field_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_field_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**| The name of the dataset you want to see field options for | 
 **field_options_request_schema** | [**FieldOptionsRequestSchema**](FieldOptionsRequestSchema.md)|  | 

### Return type

**Dict[str, List[FieldOptionsTransformer]]**

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object keyed by field name, where each value is an array of available option objects for that field. |  -  |
**400** | Bad request - missing or invalid fields/filters |  -  |
**403** | Permissions error - user does not have access to this dataset |  -  |
**500** | Internal server error. The response body may be plain text rather than a structured JSON payload. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_field_options_v12**
> Dict[str, List[FieldOptionsTransformer]] get_field_options_v12(dataset_name, field_options_request_schema)

Get Field Options v1.2

Retrieve the possible values for one or more dataset fields, for use as filter values in dataset queries. Pass the field names you want options for in the `fields` array. The response is an object keyed by field name, where each value is an array of `{id, value}` objects. Use the `id` values as filter values when querying dataset endpoints. Optionally supply `filters` to scope the returned options. V1.2 endpoint: `400` and `403` error responses use RFC 7807 `application/problem+json`. Note: unrecognised field names may result in a `500` response with a plain-text body rather than a structured error payload.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.field_options_request_schema import FieldOptionsRequestSchema
from bamboohr_sdk.models.field_options_transformer import FieldOptionsTransformer
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
    api_instance = bamboohr_sdk.DatasetsApi(api_client)
    dataset_name = 'dataset_name_example' # str | The name of the dataset you want to see field options for
    field_options_request_schema = bamboohr_sdk.FieldOptionsRequestSchema() # FieldOptionsRequestSchema | 

    try:
        # Get Field Options v1.2
        api_response = api_instance.get_field_options_v12(dataset_name, field_options_request_schema)
        print("The response of DatasetsApi->get_field_options_v12:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_field_options_v12: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**| The name of the dataset you want to see field options for | 
 **field_options_request_schema** | [**FieldOptionsRequestSchema**](FieldOptionsRequestSchema.md)|  | 

### Return type

**Dict[str, List[FieldOptionsTransformer]]**

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object keyed by field name, where each value is an array of available option objects for that field. |  -  |
**400** | Bad request - invalid fields, filters, or request format |  -  |
**403** | Permissions error - user does not have access to this dataset |  -  |
**500** | Internal server error. The response body may be plain text rather than a structured payload. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fields_from_dataset**
> DatasetFieldsResponse get_fields_from_dataset(dataset_name, page=page, page_size=page_size)

Get Fields from Dataset

Retrieve the available fields for a given dataset. Returns a paginated list of field descriptors, each including the field's machine-readable name, human-readable label, parent section type and name, and the entity name. Use the returned field `name` values in the `fields` array when querying data from POST /api/v1/datasets/{datasetName}.

**Deprecation notice:** This endpoint is deprecated. Use GET /api/v1_2/datasets/{datasetName}/fields instead.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.dataset_fields_response import DatasetFieldsResponse
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
    api_instance = bamboohr_sdk.DatasetsApi(api_client)
    dataset_name = 'dataset_name_example' # str | The name of the dataset you want to see fields for
    page = 1 # int | The page number to retrieve. Defaults to 1. (optional) (default to 1)
    page_size = 500 # int | The number of records to retrieve per page. Defaults to 500. Maximum is 1000. (optional) (default to 500)

    try:
        # Get Fields from Dataset
        api_response = api_instance.get_fields_from_dataset(dataset_name, page=page, page_size=page_size)
        print("The response of DatasetsApi->get_fields_from_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_fields_from_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**| The name of the dataset you want to see fields for | 
 **page** | **int**| The page number to retrieve. Defaults to 1. | [optional] [default to 1]
 **page_size** | **int**| The number of records to retrieve per page. Defaults to 500. Maximum is 1000. | [optional] [default to 500]

### Return type

[**DatasetFieldsResponse**](DatasetFieldsResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fields of the dataset |  -  |
**400** | Dataset label not found for dataset |  -  |
**403** | You do not have permissions to hit this endpoint |  -  |
**500** | Something went wrong while fetching the dataset configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fields_from_dataset_v12**
> DatasetFieldsResponse get_fields_from_dataset_v12(dataset_name, page=page, page_size=page_size)

Get Fields from Dataset v1.2

Retrieve the available fields for a given dataset. Returns a paginated list of field descriptors, each including the field's machine-readable name, human-readable label, parent section type and name, and the entity name. Use the returned field `name` values in the `fields` array when querying data via POST /api/v1/datasets/{datasetName}. V1.2 endpoint: error responses use RFC 7807 `application/problem+json`.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.dataset_fields_response import DatasetFieldsResponse
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
    api_instance = bamboohr_sdk.DatasetsApi(api_client)
    dataset_name = 'dataset_name_example' # str | The name of the dataset you want to see fields for
    page = 1 # int | The page number to retrieve. Defaults to 1. (optional) (default to 1)
    page_size = 500 # int | The number of records to retrieve per page. Defaults to 500. Maximum is 1000. (optional) (default to 500)

    try:
        # Get Fields from Dataset v1.2
        api_response = api_instance.get_fields_from_dataset_v12(dataset_name, page=page, page_size=page_size)
        print("The response of DatasetsApi->get_fields_from_dataset_v12:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_fields_from_dataset_v12: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**| The name of the dataset you want to see fields for | 
 **page** | **int**| The page number to retrieve. Defaults to 1. | [optional] [default to 1]
 **page_size** | **int**| The number of records to retrieve per page. Defaults to 500. Maximum is 1000. | [optional] [default to 500]

### Return type

[**DatasetFieldsResponse**](DatasetFieldsResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fields of the dataset |  -  |
**403** | You do not have permissions to hit this endpoint |  -  |
**422** | Dataset not found |  -  |
**500** | Something went wrong while fetching the dataset configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

