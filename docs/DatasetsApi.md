# bamboohr_sdk.DatasetsApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_from_dataset**](DatasetsApi.md#get_data_from_dataset) | **POST** /api/v1/datasets/{datasetName} | Get Data from Dataset
[**get_datasets**](DatasetsApi.md#get_datasets) | **GET** /api/v1/datasets | Get Datasets
[**get_datasets_v12**](DatasetsApi.md#get_datasets_v12) | **GET** /api/v1_2/datasets | Get Datasets v1.2
[**get_field_options**](DatasetsApi.md#get_field_options) | **POST** /api/v1/datasets/{datasetName}/field-options | Get Field Options
[**get_field_options_v1_2**](DatasetsApi.md#get_field_options_v1_2) | **POST** /api/v1_2/datasets/{datasetName}/field-options | Get Field Options v1.2
[**get_fields_from_dataset**](DatasetsApi.md#get_fields_from_dataset) | **GET** /api/v1/datasets/{datasetName}/fields | Get Fields from Dataset
[**get_fields_from_dataset_v1_2**](DatasetsApi.md#get_fields_from_dataset_v1_2) | **GET** /api/v1_2/datasets/{datasetName}/fields | Get Fields from Dataset v1.2


# **get_data_from_dataset**
> EmployeeResponse get_data_from_dataset(dataset_name, data_request)

Get Data from Dataset

Use this resource to request data from the specified dataset. You must specify a list of fields to show on the report. The list of fields is available here at /api/v1/datasets/{datasetName}/fields.

***Field Settings:***


**Show History**
When any of the fields included in your request are historical table fields, you may include the "showHistory" setting. Example: "showHistory":["entityName"]. Entity Name can be found in the get /api/v1/datasets/{datasetName}/fields endpoint.

**Sort By:**
You can pass multiple fields to sort by as an array of objects {field: "fieldName", sort: "asc,desc"}. The order of the fields in the array will determine the order of the sort.

**Group By:**
Group By is passed as an array of strings but currently grouping by more than one field is not supported.

**Aggregations:**
When using aggregations the following aggregates are available based on field type:
  - **text**
    - count
  - **date**
    - count
    - min
    - max
  - **int**
    - count
    - min
    - max
    - sum
    - avg
  - **bool**
    - count
  - **options**
    - count
  - **ssnText**
    - count

**Filters:**
When using filters, the filtered field does not have to be in the list of fields you want to show on the report.

**Important Filter Notes:**
  - **List filter values** (for "options" field type using "includes" or "does_not_include" operators) must be enclosed in square brackets [ ]. Example: ["value1", "value2"]
  - **Future hires**: Future hires have a status of "Inactive" in the datasets API. To include future hires in your results, you must include "Inactive" in your status filter.

Use the `/api/v1/datasets/{datasetName}/field-options` endpoint to retrieve possible filter values for fields. Use the "id" returned from the field-options endpoint.

**Filter Operators by Field Type:**
  - **text**
    - contains
    - does_not_contain
    - equal
    - not_equal
    - empty
    - not_empty
  - **date**
    - lt (less than)
    - lte (less than or equal)
    - gt (greater than)
    - gte (greater than or equal)
    - last - Uses an object for the value: {"duration": "5", "unit": "years"}. Unit can be "days", "weeks", "months", or "years". Duration is a number as a string.
    - next - Uses an object for the value: {"duration": "5", "unit": "years"}. Unit can be "days", "weeks", "months", or "years". Duration is a number as a string.
    - range - Uses an object for the value: {"start": "2023-01-01", "end": "2023-12-31"}. Dates must be in YYYY-MM-DD format.
    - equal
    - not_equal
    - empty
    - not_empty
  - **int**
    - equal
    - not_equal
    - gte
    - gt
    - lte
    - lt
    - empty
    - not_empty
  - **bool**
    - checked
    - not_checked
  - **options**
    - includes
    - does_not_include
    - empty
    - not_empty
  - **ssnText**:
    - empty
    - not_empty


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

    try:
        # Get Data from Dataset
        api_response = api_instance.get_data_from_dataset(dataset_name, data_request)
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

Use this resource to retrieve the available datasets to query data from.

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

Use this resource to retrieve the available datasets to query data from. Each dataset represents a collection of related data that can be filtered, sorted, and retrieved through other dataset endpoints. Returns a list of dataset names and their human-readable labels. V1.2 endpoint with RFC 7807 compliant error responses.

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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved list of available datasets |  * X-Request-ID - Correlation ID for request tracing <br>  |
**403** | Forbidden - insufficient permissions to access datasets |  -  |
**500** | Internal server error while retrieving datasets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_field_options**
> List[FieldOptionsTransformer] get_field_options(dataset_name, field_options_request_schema)

Get Field Options

Use this resource to retrieve a list of possible values for a field. For RFC 7807 compliant error responses, use the v1.2 endpoint: POST /api/v1_2/datasets/{datasetName}/field-options

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

[**List[FieldOptionsTransformer]**](FieldOptionsTransformer.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Field options response |  -  |
**400** | Bad request - invalid fields, filters, or request format |  -  |
**403** | Permissions error - user does not have access to this dataset |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_field_options_v1_2**
> List[FieldOptionsTransformer] get_field_options_v1_2(dataset_name, field_options_request_schema)

Get Field Options v1.2

Use this resource to retrieve a list of possible values for specified fields. V1.2 endpoint with RFC 7807 compliant error responses.

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
        api_response = api_instance.get_field_options_v1_2(dataset_name, field_options_request_schema)
        print("The response of DatasetsApi->get_field_options_v1_2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_field_options_v1_2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**| The name of the dataset you want to see field options for | 
 **field_options_request_schema** | [**FieldOptionsRequestSchema**](FieldOptionsRequestSchema.md)|  | 

### Return type

[**List[FieldOptionsTransformer]**](FieldOptionsTransformer.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Field options response |  -  |
**400** | Bad request - invalid fields, filters, or request format |  -  |
**403** | Permissions error - user does not have access to this dataset |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fields_from_dataset**
> DatasetFieldsResponse get_fields_from_dataset(dataset_name, page=page, page_size=page_size)

Get Fields from Dataset

Use this resource to request the available fields on a dataset.

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
    page = 56 # int | The page number to retrieve (optional)
    page_size = 56 # int | The number of records to retrieve per page. Default is 500 and the Max is 1000 (optional)

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
 **page** | **int**| The page number to retrieve | [optional] 
 **page_size** | **int**| The number of records to retrieve per page. Default is 500 and the Max is 1000 | [optional] 

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

# **get_fields_from_dataset_v1_2**
> DatasetFieldsResponse get_fields_from_dataset_v1_2(dataset_name, page=page, page_size=page_size)

Get Fields from Dataset v1.2

Use this resource to request the available fields on a dataset. V1.2 endpoint with RFC 7807 compliant error responses.

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
    page = 56 # int | The page number to retrieve (optional)
    page_size = 56 # int | The number of records to retrieve per page. Default is 500 and the Max is 1000 (optional)

    try:
        # Get Fields from Dataset v1.2
        api_response = api_instance.get_fields_from_dataset_v1_2(dataset_name, page=page, page_size=page_size)
        print("The response of DatasetsApi->get_fields_from_dataset_v1_2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_fields_from_dataset_v1_2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**| The name of the dataset you want to see fields for | 
 **page** | **int**| The page number to retrieve | [optional] 
 **page_size** | **int**| The number of records to retrieve per page. Default is 500 and the Max is 1000 | [optional] 

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

