# bamboohr_sdk.CompensationBenchmarkingApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_compensation_benchmark**](CompensationBenchmarkingApi.md#create_compensation_benchmark) | **POST** /api/v1/compensation/benchmarks | Create Compensation Benchmark
[**create_compensation_benchmark_source**](CompensationBenchmarkingApi.md#create_compensation_benchmark_source) | **POST** /api/v1/compensation/benchmarks/sources | Create Compensation Benchmark Source
[**delete_compensation_benchmark**](CompensationBenchmarkingApi.md#delete_compensation_benchmark) | **DELETE** /api/v1/compensation/benchmarks/{id} | Delete Compensation Benchmark
[**delete_compensation_benchmark_source**](CompensationBenchmarkingApi.md#delete_compensation_benchmark_source) | **DELETE** /api/v1/compensation/benchmarks/sources | Delete Compensation Benchmark Source
[**export_compensation_benchmark_details**](CompensationBenchmarkingApi.md#export_compensation_benchmark_details) | **GET** /api/v1/compensation/benchmarks/details/export | Export Compensation Benchmark Details
[**get_compensation_benchmark_details**](CompensationBenchmarkingApi.md#get_compensation_benchmark_details) | **GET** /api/v1/compensation/benchmarks/details | Get Compensation Benchmark Details
[**import_compensation_benchmarks**](CompensationBenchmarkingApi.md#import_compensation_benchmarks) | **POST** /api/v1/compensation/benchmarks/import | Import Compensation Benchmarks From CSV
[**list_compensation_benchmark_sources**](CompensationBenchmarkingApi.md#list_compensation_benchmark_sources) | **GET** /api/v1/compensation/benchmarks/sources | List Compensation Benchmark Sources
[**list_compensation_benchmarks**](CompensationBenchmarkingApi.md#list_compensation_benchmarks) | **GET** /api/v1/compensation/benchmarks | List Compensation Benchmarks
[**update_compensation_benchmark**](CompensationBenchmarkingApi.md#update_compensation_benchmark) | **PUT** /api/v1/compensation/benchmarks | Update Compensation Benchmark
[**update_compensation_benchmark_sources**](CompensationBenchmarkingApi.md#update_compensation_benchmark_sources) | **PUT** /api/v1/compensation/benchmarks/sources | Update Compensation Benchmark Sources


# **create_compensation_benchmark**
> CreatedCompensationBenchmark create_compensation_benchmark(create_compensation_benchmark_request=create_compensation_benchmark_request)

Create Compensation Benchmark

Creates a new compensation benchmark for a specific company job title (and optionally a specific job location). The `jobTitleId` value comes from `GET /api/v1/compensation/benchmarks` (`jobDetails.id`) or the company's job-title list. When `jobLocationId` is omitted, the benchmark applies to the job title at any location. Returns the saved benchmark wrapped in `savedBenchmark` along with a status `message`.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.create_compensation_benchmark_request import CreateCompensationBenchmarkRequest
from bamboohr_sdk.models.created_compensation_benchmark import CreatedCompensationBenchmark
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
    api_instance = bamboohr_sdk.CompensationBenchmarkingApi(api_client)
    create_compensation_benchmark_request = bamboohr_sdk.CreateCompensationBenchmarkRequest() # CreateCompensationBenchmarkRequest |  (optional)

    try:
        # Create Compensation Benchmark
        api_response = api_instance.create_compensation_benchmark(create_compensation_benchmark_request=create_compensation_benchmark_request)
        print("The response of CompensationBenchmarkingApi->create_compensation_benchmark:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationBenchmarkingApi->create_compensation_benchmark: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_compensation_benchmark_request** | [**CreateCompensationBenchmarkRequest**](CreateCompensationBenchmarkRequest.md)|  | [optional] 

### Return type

[**CreatedCompensationBenchmark**](CreatedCompensationBenchmark.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object containing the newly created benchmark row and a status message. |  -  |
**403** | The authenticated caller lacks permission to create compensation benchmarks. |  -  |
**500** | Unexpected server error while creating the benchmark. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_compensation_benchmark_source**
> CreatedCompensationBenchmarkSource create_compensation_benchmark_source(create_compensation_benchmark_source_request=create_compensation_benchmark_source_request)

Create Compensation Benchmark Source

Creates a new benchmark source the company can attach to its benchmarks. The `name` must be non-empty; the reserved name `mercer` (case-insensitive) is rejected because Mercer sources are managed separately. Returns the new source's ID and the trimmed name.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.create_compensation_benchmark_source_request import CreateCompensationBenchmarkSourceRequest
from bamboohr_sdk.models.created_compensation_benchmark_source import CreatedCompensationBenchmarkSource
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
    api_instance = bamboohr_sdk.CompensationBenchmarkingApi(api_client)
    create_compensation_benchmark_source_request = bamboohr_sdk.CreateCompensationBenchmarkSourceRequest() # CreateCompensationBenchmarkSourceRequest |  (optional)

    try:
        # Create Compensation Benchmark Source
        api_response = api_instance.create_compensation_benchmark_source(create_compensation_benchmark_source_request=create_compensation_benchmark_source_request)
        print("The response of CompensationBenchmarkingApi->create_compensation_benchmark_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationBenchmarkingApi->create_compensation_benchmark_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_compensation_benchmark_source_request** | [**CreateCompensationBenchmarkSourceRequest**](CreateCompensationBenchmarkSourceRequest.md)|  | [optional] 

### Return type

[**CreatedCompensationBenchmarkSource**](CreatedCompensationBenchmarkSource.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object with the newly created source&#39;s ID and name. |  -  |
**400** | The &#x60;name&#x60; is missing, empty, or the reserved value &#x60;mercer&#x60;. |  -  |
**403** | The authenticated caller lacks permission to modify compensation benchmarks. |  -  |
**500** | Unexpected server error while creating the benchmark source. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_compensation_benchmark**
> str delete_compensation_benchmark(id)

Delete Compensation Benchmark

Permanently removes the compensation benchmark identified by `id`. The `id` is a numeric benchmark row identifier; non-numeric values are rejected by the handler. Valid values are returned by `GET /api/v1/compensation/benchmarks/details` under `benchmarkValues[].id` and by the create/update endpoints as `savedBenchmark.id`.

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
    api_instance = bamboohr_sdk.CompensationBenchmarkingApi(api_client)
    id = 56 # int | Integer ID of the compensation benchmark to delete.

    try:
        # Delete Compensation Benchmark
        api_response = api_instance.delete_compensation_benchmark(id)
        print("The response of CompensationBenchmarkingApi->delete_compensation_benchmark:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationBenchmarkingApi->delete_compensation_benchmark: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Integer ID of the compensation benchmark to delete. | 

### Return type

**str**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Literal string &#x60;\&quot;Success\&quot;&#x60; indicating the benchmark was deleted. |  -  |
**403** | The authenticated caller lacks permission to delete compensation benchmarks. |  -  |
**500** | Unexpected server error while deleting the benchmark. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_compensation_benchmark_source**
> DeleteCompensationBenchmarkSourceResponse delete_compensation_benchmark_source(delete_compensation_benchmark_source_request=delete_compensation_benchmark_source_request)

Delete Compensation Benchmark Source

Deletes a benchmark source together with all benchmarks currently attached to it. The source `id` is taken from the request body. Use `GET /api/v1/compensation/benchmarks/sources` to look up the `id` of the source to delete. Returns `{ "result": "success" }` when the source is removed.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.delete_compensation_benchmark_source_request import DeleteCompensationBenchmarkSourceRequest
from bamboohr_sdk.models.delete_compensation_benchmark_source_response import DeleteCompensationBenchmarkSourceResponse
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
    api_instance = bamboohr_sdk.CompensationBenchmarkingApi(api_client)
    delete_compensation_benchmark_source_request = bamboohr_sdk.DeleteCompensationBenchmarkSourceRequest() # DeleteCompensationBenchmarkSourceRequest |  (optional)

    try:
        # Delete Compensation Benchmark Source
        api_response = api_instance.delete_compensation_benchmark_source(delete_compensation_benchmark_source_request=delete_compensation_benchmark_source_request)
        print("The response of CompensationBenchmarkingApi->delete_compensation_benchmark_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationBenchmarkingApi->delete_compensation_benchmark_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_compensation_benchmark_source_request** | [**DeleteCompensationBenchmarkSourceRequest**](DeleteCompensationBenchmarkSourceRequest.md)|  | [optional] 

### Return type

[**DeleteCompensationBenchmarkSourceResponse**](DeleteCompensationBenchmarkSourceResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object containing &#x60;{ \&quot;result\&quot;: \&quot;success\&quot; }&#x60; when the source is deleted. |  -  |
**400** | The id is missing, empty, or not a valid non-zero numeric identifier. |  -  |
**403** | The authenticated caller lacks permission to modify compensation benchmarks. |  -  |
**500** | Unexpected server error while deleting the benchmark source. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_compensation_benchmark_details**
> str export_compensation_benchmark_details(job_id, location_id=location_id)

Export Compensation Benchmark Details

Returns a CSV export of the compensation benchmark detail view for a single job, optionally scoped to a specific location. Rows include employee-level data (name, location, annualized pay, compa-ratio, range penetration, years of experience) alongside the company's internal pay band for the job. Use `GET /api/v1/compensation/benchmarks` to find valid `jobId` and `locationId` values. When `locationId` is omitted, the export aggregates across all locations for the job.

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
    api_instance = bamboohr_sdk.CompensationBenchmarkingApi(api_client)
    job_id = 'job_id_example' # str | ID of the company job title to export benchmark details for.
    location_id = 'location_id_example' # str | Optional job location ID to restrict the export to one location. (optional)

    try:
        # Export Compensation Benchmark Details
        api_response = api_instance.export_compensation_benchmark_details(job_id, location_id=location_id)
        print("The response of CompensationBenchmarkingApi->export_compensation_benchmark_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationBenchmarkingApi->export_compensation_benchmark_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| ID of the company job title to export benchmark details for. | 
 **location_id** | **str**| Optional job location ID to restrict the export to one location. | [optional] 

### Return type

**str**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CSV payload streamed with a &#x60;Content-Disposition: attachment&#x60; header. The filename is derived from the job title and location. |  -  |
**403** | The authenticated caller lacks permission to read compensation benchmarks. |  -  |
**500** | Unexpected server error while generating the CSV export. Also returned when &#x60;jobId&#x60; is missing. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compensation_benchmark_details**
> CompensationBenchmarkDetails get_compensation_benchmark_details(job_id, location_id=location_id)

Get Compensation Benchmark Details

Returns detailed benchmark data for a single company job title, optionally scoped to a specific location. The response includes the company pay range derived from current employees, the internal pay band configured for the job (if any), Mercer benchmark details when a Mercer benchmark is linked, every saved benchmark for the job/location (empty when none exist), and per-employee salary and compensation stats. Use `GET /api/v1/compensation/benchmarks` to find valid `jobId` and `locationId` values.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.compensation_benchmark_details import CompensationBenchmarkDetails
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
    api_instance = bamboohr_sdk.CompensationBenchmarkingApi(api_client)
    job_id = 'job_id_example' # str | ID of the company job title to fetch benchmark details for.
    location_id = 'location_id_example' # str | Optional job location ID. When omitted, results aggregate across all locations for the job. (optional)

    try:
        # Get Compensation Benchmark Details
        api_response = api_instance.get_compensation_benchmark_details(job_id, location_id=location_id)
        print("The response of CompensationBenchmarkingApi->get_compensation_benchmark_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationBenchmarkingApi->get_compensation_benchmark_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| ID of the company job title to fetch benchmark details for. | 
 **location_id** | **str**| Optional job location ID. When omitted, results aggregate across all locations for the job. | [optional] 

### Return type

[**CompensationBenchmarkDetails**](CompensationBenchmarkDetails.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Benchmark detail object for the requested job (and optional location). |  -  |
**403** | The authenticated caller lacks permission to read compensation benchmarks. |  -  |
**500** | Unexpected server error while loading benchmark details. Also returned when &#x60;jobId&#x60; is missing. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_compensation_benchmarks**
> ImportCompensationBenchmarksResponse import_compensation_benchmarks(file)

Import Compensation Benchmarks From CSV

Parses a CSV of compensation benchmarks uploaded as multipart/form-data and returns the parsed rows together with a suggested column-to-field mapping. The response is a preview payload — callers must follow up with the publish step in the UI/API to persist benchmarks. Returns `400` when no `file` part is provided and `422` when the CSV is malformed.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.import_compensation_benchmarks_response import ImportCompensationBenchmarksResponse
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
    api_instance = bamboohr_sdk.CompensationBenchmarkingApi(api_client)
    file = None # bytearray | CSV file to import.

    try:
        # Import Compensation Benchmarks From CSV
        api_response = api_instance.import_compensation_benchmarks(file)
        print("The response of CompensationBenchmarkingApi->import_compensation_benchmarks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationBenchmarkingApi->import_compensation_benchmarks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| CSV file to import. | 

### Return type

[**ImportCompensationBenchmarksResponse**](ImportCompensationBenchmarksResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Parsed CSV preview containing the raw rows and a suggested column map. |  -  |
**400** | The multipart request is missing the &#x60;file&#x60; part. |  -  |
**403** | The authenticated caller lacks permission to import compensation benchmarks. |  -  |
**422** | The uploaded CSV could not be parsed (missing columns, invalid data, etc.). |  -  |
**500** | Unexpected server error while parsing the CSV upload. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_compensation_benchmark_sources**
> List[CompensationBenchmarkSource] list_compensation_benchmark_sources()

List Compensation Benchmark Sources

Returns every enabled benchmark source configured for the company. Each source identifies where a benchmark value came from (for example, a specific survey provider) and includes a display color and the count of benchmarks currently attached to that source. Use the returned `id` as the `sourceId` input when creating or updating a benchmark.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.compensation_benchmark_source import CompensationBenchmarkSource
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
    api_instance = bamboohr_sdk.CompensationBenchmarkingApi(api_client)

    try:
        # List Compensation Benchmark Sources
        api_response = api_instance.list_compensation_benchmark_sources()
        print("The response of CompensationBenchmarkingApi->list_compensation_benchmark_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationBenchmarkingApi->list_compensation_benchmark_sources: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CompensationBenchmarkSource]**](CompensationBenchmarkSource.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of benchmark sources. Empty when no sources are configured. |  -  |
**403** | The authenticated caller lacks permission to read compensation benchmarks. |  -  |
**500** | Unexpected server error while loading benchmark sources. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_compensation_benchmarks**
> CompensationBenchmarksList list_compensation_benchmarks()

List Compensation Benchmarks

Returns every job/location pair the company tracks for compensation benchmarking. Each entry includes job and location identifiers, the benchmarks attached to that pair, the employees currently assigned to that job and location, and the company's configured internal pay band if one exists. Use the returned `jobDetails.id` and `locationDetails.id` values as the `jobId` and `locationId` inputs for `GET /api/v1/compensation/benchmarks/details`. Top-level `dismiss*Banner` fields reflect UI banner state and are not part of the benchmark data contract.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.compensation_benchmarks_list import CompensationBenchmarksList
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
    api_instance = bamboohr_sdk.CompensationBenchmarkingApi(api_client)

    try:
        # List Compensation Benchmarks
        api_response = api_instance.list_compensation_benchmarks()
        print("The response of CompensationBenchmarkingApi->list_compensation_benchmarks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationBenchmarkingApi->list_compensation_benchmarks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CompensationBenchmarksList**](CompensationBenchmarksList.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object with a &#x60;jobLocationPairs&#x60; array and banner-dismissal flags. |  -  |
**403** | The authenticated caller lacks permission to read compensation benchmarks. |  -  |
**500** | Unexpected server error while loading compensation benchmarks. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_compensation_benchmark**
> UpdatedCompensationBenchmark update_compensation_benchmark(update_compensation_benchmark_request=update_compensation_benchmark_request)

Update Compensation Benchmark

Updates an existing compensation benchmark identified by `id`. The `id` of an existing benchmark can be obtained from `GET /api/v1/compensation/benchmarks/details`. Request fields that are omitted or `null` are cleared on the stored benchmark; callers should send the full benchmark payload to preserve values. On success, returns the saved benchmark row wrapped in `savedBenchmark` together with a status `message`.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.update_compensation_benchmark_request import UpdateCompensationBenchmarkRequest
from bamboohr_sdk.models.updated_compensation_benchmark import UpdatedCompensationBenchmark
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
    api_instance = bamboohr_sdk.CompensationBenchmarkingApi(api_client)
    update_compensation_benchmark_request = bamboohr_sdk.UpdateCompensationBenchmarkRequest() # UpdateCompensationBenchmarkRequest |  (optional)

    try:
        # Update Compensation Benchmark
        api_response = api_instance.update_compensation_benchmark(update_compensation_benchmark_request=update_compensation_benchmark_request)
        print("The response of CompensationBenchmarkingApi->update_compensation_benchmark:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationBenchmarkingApi->update_compensation_benchmark: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_compensation_benchmark_request** | [**UpdateCompensationBenchmarkRequest**](UpdateCompensationBenchmarkRequest.md)|  | [optional] 

### Return type

[**UpdatedCompensationBenchmark**](UpdatedCompensationBenchmark.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object containing the saved benchmark row and a status message. |  -  |
**403** | The authenticated caller lacks permission to modify compensation benchmarks. |  -  |
**500** | Unexpected server error while saving the benchmark. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_compensation_benchmark_sources**
> UpdateCompensationBenchmarkSourcesResponse update_compensation_benchmark_sources(update_compensation_benchmark_sources_request=update_compensation_benchmark_sources_request)

Update Compensation Benchmark Sources

Updates the name and sort order of one or more existing benchmark sources in a single call. Every item in `benchmarkSources` must include a non-empty `id` and `name`; any item with the reserved name `mercer` (case-insensitive) is rejected because Mercer sources are managed separately. Use `GET /api/v1/compensation/benchmarks/sources` to obtain the current `id` values. Returns `{ "result": "success" }` when all updates are applied.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.update_compensation_benchmark_sources_request import UpdateCompensationBenchmarkSourcesRequest
from bamboohr_sdk.models.update_compensation_benchmark_sources_response import UpdateCompensationBenchmarkSourcesResponse
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
    api_instance = bamboohr_sdk.CompensationBenchmarkingApi(api_client)
    update_compensation_benchmark_sources_request = bamboohr_sdk.UpdateCompensationBenchmarkSourcesRequest() # UpdateCompensationBenchmarkSourcesRequest |  (optional)

    try:
        # Update Compensation Benchmark Sources
        api_response = api_instance.update_compensation_benchmark_sources(update_compensation_benchmark_sources_request=update_compensation_benchmark_sources_request)
        print("The response of CompensationBenchmarkingApi->update_compensation_benchmark_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompensationBenchmarkingApi->update_compensation_benchmark_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_compensation_benchmark_sources_request** | [**UpdateCompensationBenchmarkSourcesRequest**](UpdateCompensationBenchmarkSourcesRequest.md)|  | [optional] 

### Return type

[**UpdateCompensationBenchmarkSourcesResponse**](UpdateCompensationBenchmarkSourcesResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object containing &#x60;{ \&quot;result\&quot;: \&quot;success\&quot; }&#x60; when all source updates succeed. |  -  |
**400** | The &#x60;benchmarkSources&#x60; array is missing, empty, contains items without &#x60;id&#x60; or &#x60;name&#x60;, or contains the reserved &#x60;mercer&#x60; name. |  -  |
**403** | The authenticated caller lacks permission to modify compensation benchmarks. |  -  |
**500** | Unexpected server error while updating benchmark sources. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

