# bamboohr_sdk.DatasetsApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_from_dataset_v1**](DatasetsApi.md#get_data_from_dataset_v1) | **POST** /api/v1/datasets/{datasetName} | Get Data from Dataset (v1)
[**get_data_from_dataset_v2**](DatasetsApi.md#get_data_from_dataset_v2) | **POST** /api/v2/datasets/{datasetName}/data | Get Data from Dataset (v2)
[**get_field_options_v1**](DatasetsApi.md#get_field_options_v1) | **POST** /api/v1/datasets/{datasetName}/field-options | Get Field Options (v1)
[**get_field_options_v12**](DatasetsApi.md#get_field_options_v12) | **POST** /api/v1_2/datasets/{datasetName}/field-options | Get Field Options (v1.2)
[**get_fields_from_dataset_v1**](DatasetsApi.md#get_fields_from_dataset_v1) | **GET** /api/v1/datasets/{datasetName}/fields | Get Fields from Dataset (v1)
[**get_fields_from_dataset_v12**](DatasetsApi.md#get_fields_from_dataset_v12) | **GET** /api/v1_2/datasets/{datasetName}/fields | Get Fields from Dataset (v1.2)
[**list_datasets_v1**](DatasetsApi.md#list_datasets_v1) | **GET** /api/v1/datasets | List Datasets (v1)
[**list_datasets_v12**](DatasetsApi.md#list_datasets_v12) | **GET** /api/v1_2/datasets | List Datasets (v1.2)


# **get_data_from_dataset_v1**
> EmployeeResponse get_data_from_dataset_v1(dataset_name, data_request, page=page, page_size=page_size)

Get Data from Dataset (v1)

Deprecated. Use "Get Data from Dataset (v2)" instead.

Retrieves records from the specified dataset using the fields, filters, sorting, grouping, and aggregations supplied in the request body. Provide field names in the `fields` array; use "Get Fields from Dataset (v1.2)" to discover available names. The response contains paginated rows under `data`, an `aggregations` array (empty when none requested), and a `pagination` block with page navigation links. Results default to page 1 with 500 records per page (maximum 1000).

Use "Get Field Options (v1.2)" to retrieve valid filter values. Filter fields do not need to appear in the `fields` list. Future hires have a status of `Inactive`; include it in your status filter to retrieve them. For `options`-type fields using `includes`/`does_not_include`, pass the filter value as an array enclosed in square brackets, for example `["Full-Time", "Part-Time"]`.

When any requested fields are historical table fields, pass their entity names in `showHistory`; entity names are returned by "Get Fields from Dataset (v1.2)". Grouping (`groupBy`) currently supports only one field; when active, `data` becomes an object keyed by group value instead of an array. Sort priority follows the order of objects in `sortBy`. Aggregations accept a `defaultAggregation` applied to every field and/or per-field `overridingAggregations`.

**Aggregations by field type:** text: count; date: count, min, max; int: count, min, max, sum, avg; bool: count; options: count; govIdText: count.

**Filter operators by field type:** text: contains, does_not_contain, equal, not_equal, empty, not_empty; date: lt, lte, gt, gte (each accepts a YYYY-MM-DD date string or a relative object `{"duration": "N", "unit": "days|weeks|months|years"}` where duration is a number as a string — lt/lte are measured backward from today, gt/gte forward), equal, not_equal, empty, not_empty, last, next (relative object `{"duration": "N", "unit": "days|weeks|months|years"}`), range (object `{"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"}`); int: equal, not_equal, gte, gt, lte, lt, empty, not_empty; bool: checked, not_checked; options: includes, does_not_include, empty, not_empty; govIdText: empty, not_empty.

OAuth Scopes: report

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
    dataset_name = 'dataset_name_example' # str | The machine-readable name of the dataset to query. Use \"List Datasets (v1.2)\" to discover available names.
    data_request = bamboohr_sdk.DataRequest() # DataRequest | 
    page = 1 # int | The page number to retrieve. Defaults to 1. (optional) (default to 1)
    page_size = 500 # int | The number of records to retrieve per page. Defaults to 500. Maximum is 1000. (optional) (default to 500)

    try:
        # Get Data from Dataset (v1)
        api_response = api_instance.get_data_from_dataset_v1(dataset_name, data_request, page=page, page_size=page_size)
        print("The response of DatasetsApi->get_data_from_dataset_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_data_from_dataset_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**| The machine-readable name of the dataset to query. Use \&quot;List Datasets (v1.2)\&quot; to discover available names. | 
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
**200** | Returns an object with &#x60;data&#x60; (array of record objects, or an object keyed by group value when &#x60;groupBy&#x60; is used), &#x60;aggregations&#x60; (array, empty when none requested), and &#x60;pagination&#x60;. |  -  |
**400** | Invalid or missing argument(s), such as an unrecognised operator, malformed filter, invalid dataset name, or empty request body. |  -  |
**403** | Insufficient permissions to access this dataset. |  -  |
**500** | An unexpected internal error occurred while retrieving data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_from_dataset_v2**
> DatasetDataResponseV2 get_data_from_dataset_v2(dataset_name, get_data_from_dataset_v2_request)

Get Data from Dataset (v2)

Queries the named dataset and returns the matching rows. The response is a JSON object with `data` (an array of row objects, each wrapping its values under a `fields` object whose keys match the requested field names), `links` (pagination navigation URLs; `prev` and/or `next`, omitted at boundaries), and `meta` (with `page`, `pageSize`, `totalPages`, `totalItems`).

Use this for tabular reporting, custom field selection across many employees, and OData-style filtering against the full dataset field catalog. For multiple employees, use List Employees (`list-employees`). For the full set of fields on a single employee, use Get Employee (`get-employee`). Dataset access itself requires elevated permissions, so a caller without them receives `403` here regardless of which fields are requested. For information published in a coworker's company directory entry, such as job title, department, location, work contact details, or who they report to, use Get Employees Directory (`get-employees-directory`), which is governed by directory sharing settings rather than by per-employee record permissions and is available when directory or org-chart access is shared with the caller's access level.

Discover valid `datasetName` values via List Datasets (v1.2) (`list-datasets-v1_2`). Discover valid field names for a dataset via Get Fields from Dataset (v1.2) (`get-fields-from-dataset-v1_2`); the field set is dataset-specific.

Field-name vocabulary differs from the dedicated employee endpoints. The `employee` dataset uses fully qualified names such as `jobInformationJobTitle`, `jobInformationDepartment`, `jobInformationReportsTo`, and `employmentStatus`, where the employee endpoints use endpoint-specific shorter names — for example `jobTitleName` on List Employees (`list-employees`), and `jobTitle`, `department`, `supervisor`, and `workEmail` on Get Employee (`get-employee`). Identifier and contact fields also differ: the dataset's internal employee identifier is `eeid` (`get-employee` returns the same value as `id`, and `list-employees` as `employeeId`); the dataset's work-email field is `email` (`get-employee` uses `workEmail`). The dataset also exposes `employeeNumber` — the editable Employee # value, not the internal employee ID. Do not pass `employeeNumber` to employee ID inputs such as `filter[ids]` or `{id}` path parameters; it may fail with `404` or resolve to a different employee whose internal employee ID happens to match. Always source field names from Get Fields from Dataset (v1.2) (`get-fields-from-dataset-v1_2`) — names from the employee endpoints will not necessarily resolve here.

For routine `employee` dataset lookups, a useful starter field set is: `firstName`, `lastName`, `eeid` (internal employee ID), `employeeNumber` (Employee # / editable employee number), `email` (work email), `mobilePhone`, `hireDate`, `employmentStatus`, `jobInformationJobTitle`, `jobInformationDepartment`, `jobInformationLocation`, `jobInformationReportsTo` (supervisor's name), and `supervisorEid` (supervisor's `eeid`). The full catalog (over 450 fields) is discoverable via Get Fields from Dataset (v1.2) (`get-fields-from-dataset-v1_2`) — use it when you need anything beyond this starter set.

Filter expressions use OData-style syntax with comparison operators `eq`, `ne`, `lt`, `le`, `gt`, `ge`, the list-membership operator `in (...)`, and logical operators `and` / `or`. The parser does not support `not in`; use `ne` for the inverse of `eq`, and on options-type fields `ne` already applies set-membership negation under the hood. A single filter expression may use `and` or `or`, but not both; mixed logical expressions return `422` with code `INVALID_FILTER`. Operator support varies by field type: `eq` / `ne` work on text, numeric, date, and options-type (single-select enum) fields like `status`, `employmentStatus`, and `jobInformationDepartment`; ordering operators `lt`, `le`, `gt`, `ge` are supported on numeric and date fields. The list operator `in` is the natural fit on options-type fields (e.g. `status in ('Active','Inactive')`), and is also accepted on text, numeric, and date fields when used with a single value (e.g. `firstName in ('Ashley')`, equivalent to `firstName eq 'Ashley'`); multi-value `in` on non-options fields returns `422`. To check a field's type, see the `type` value returned by Get Fields from Dataset (v1.2). Filter fields do not need to appear in the `fields` array; rows are filtered server-side. String literals in filter expressions are wrapped in single quotes, e.g. `firstName eq 'Ashley'` or `status in ('Active','Inactive')`.

On date fields, the ordering operators also accept a relative-date duration literal in OData v4 / ISO 8601 form, e.g. `hireDate ge duration'P30D'`. The literal resolves against today at query time: with `lt` / `le` it resolves to today minus the duration, with `gt` / `ge` to today plus the duration (so `terminationDate lt duration'P6M'` matches dates before six months ago, and `hireDate ge duration'P30D'` matches dates from 30 days in the future onward). A negative duration reverses the direction — `hireDate ge duration'-P30D'` matches hire dates from 30 days ago onward (i.e. anyone hired in the last 30 days), including any future-dated hires. Exactly one date component is required — `P<n>Y` (years), `P<n>M` (months), `P<n>W` (weeks), or `P<n>D` (days). Combined components (`P1Y6M`), time components (`PT12H`), and duration literals with `eq` / `ne` / `in` return `422` with code `INVALID_FILTER`.

`orderBy` is a comma-separated list of `<field> <asc|desc>` rules. Every field used in `orderBy` must also appear in the `fields` array; omitting it returns a `400` with code `UE-1001`. `orderBy` is optional; with no `orderBy` the row order is unspecified.

Field-level access is enforced server-side based on the authenticated caller's permissions and OAuth scopes. When a caller lacks permission to read a requested field, the field is still returned in each row with an empty value, and its canonical name is listed in that row's `_restrictedFields` array (e.g., `_restrictedFields: ["employee_employeeNumber"]`) — the request is not rejected, and other requested fields still come back. This differs from Get Employee (`get-employee`), which silently omits unauthorized fields with no marker, leaving an absent field ambiguous between "not requested" and "not permitted". Callers without dataset-level access receive `403`, and a dataset the caller cannot see at all returns `404` ("not accessible" rather than disclosing existence).

Bad field names in `fields` or `filter` return `400` with `code: INVALID_ARGUMENT` and the offending name in the `detail` field (e.g., `"Invalid field name: employee_workEmail"`). The reported name carries the internal `<dataset>_` prefix; the actual misspelling is the unprefixed form. Confirm spelling against Get Fields from Dataset (v1.2) (`get-fields-from-dataset-v1_2`). Note: the field name appears in `detail` (singular); the `details` field (plural) remains empty in this error class. (Bad names in `orderBy` hit the must-be-in-`fields` check above first and return `UE-1001` rather than `INVALID_ARGUMENT`.)

Pagination: `page` defaults to `1` and `pageSize` defaults to `100` (maximum `1000`). `meta.totalItems` is the count of rows matching the query across all pages, `meta.totalPages` is `ceil(totalItems / pageSize)`, and `data` contains at most `pageSize` rows for the requested page. `links.next` is present when more pages exist; `links.prev` is present when not on the first page. Errors follow RFC 7807 (`application/problem+json`).

Note: Compared to Get Data from Dataset (v1) (`get-data-from-dataset-v1`), this version uses `filter` and `orderBy` request fields instead of the legacy `filters` and `sortBy` structures, moves pagination inputs to body fields (`page`, `pageSize`) instead of query parameters, returns pagination in `links` / `meta` objects instead of a legacy `pagination` object, and returns RFC 7807 compliant error responses with an `X-Request-ID` correlation header.

OAuth Scopes: report

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.dataset_data_response_v2 import DatasetDataResponseV2
from bamboohr_sdk.models.get_data_from_dataset_v2_request import GetDataFromDatasetV2Request
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
    dataset_name = 'employee' # str | Machine-readable name of the dataset to query. Discover valid values via List Datasets (v1.2) (`list-datasets-v1_2`); examples include `employee`, `benefit`, and `applicants`. Unknown or inaccessible names return `404`.
    get_data_from_dataset_v2_request = bamboohr_sdk.GetDataFromDatasetV2Request() # GetDataFromDatasetV2Request | Request parameters for dataset data retrieval

    try:
        # Get Data from Dataset (v2)
        api_response = api_instance.get_data_from_dataset_v2(dataset_name, get_data_from_dataset_v2_request)
        print("The response of DatasetsApi->get_data_from_dataset_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_data_from_dataset_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**| Machine-readable name of the dataset to query. Discover valid values via List Datasets (v1.2) (&#x60;list-datasets-v1_2&#x60;); examples include &#x60;employee&#x60;, &#x60;benefit&#x60;, and &#x60;applicants&#x60;. Unknown or inaccessible names return &#x60;404&#x60;. | 
 **get_data_from_dataset_v2_request** | [**GetDataFromDatasetV2Request**](GetDataFromDatasetV2Request.md)| Request parameters for dataset data retrieval | 

### Return type

[**DatasetDataResponseV2**](DatasetDataResponseV2.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object containing &#x60;data&#x60; (array of record objects each wrapping requested values under a &#x60;fields&#x60; object), &#x60;links&#x60; (pagination URLs; &#x60;prev&#x60; and/or &#x60;next&#x60;, omitted at boundaries), and &#x60;meta&#x60; (&#x60;page&#x60;, &#x60;pageSize&#x60;, &#x60;totalPages&#x60;, &#x60;totalItems&#x60;). |  * X-Request-ID - Correlation ID for request tracing. Echoes the client-provided value or a generated identifier. <br>  |
**400** | Missing or invalid parameters. |  -  |
**401** | Unauthorized. |  -  |
**403** | Insufficient permissions to access the requested dataset. |  -  |
**404** | The specified dataset does not exist or is not accessible. |  -  |
**413** | The request produced too much data. |  -  |
**422** | Validation failed, such as an invalid filter expression or pagination value. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_field_options_v1**
> Dict[str, List[FieldOptionsTransformer]] get_field_options_v1(dataset_name, field_options_request_schema)

Get Field Options (v1)

Deprecated. Use "Get Field Options (v1.2)" instead.

Returns the allowed values for one or more fields in a dataset, for use as filter values when querying data via "Get Data from Dataset". Pass field names in the `fields` array of the request body; the response is an object keyed by field name, where each value is an array of `{id, value}` option objects. Optionally supply `filters` to narrow the returned options (e.g. only options that exist for active employees) and `dependentFields` when one field's options depend on another field's selected value.

Unrecognised field names may produce a `500` response with a plain-text body rather than structured JSON.

OAuth Scopes: field

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
    dataset_name = 'dataset_name_example' # str | The name of the dataset to retrieve field options for.
    field_options_request_schema = bamboohr_sdk.FieldOptionsRequestSchema() # FieldOptionsRequestSchema | 

    try:
        # Get Field Options (v1)
        api_response = api_instance.get_field_options_v1(dataset_name, field_options_request_schema)
        print("The response of DatasetsApi->get_field_options_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_field_options_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**| The name of the dataset to retrieve field options for. | 
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
**400** | Bad request - missing or invalid fields, filters, or request format. |  -  |
**403** | Forbidden - insufficient permissions to access this dataset. |  -  |
**500** | Internal server error. The response body may be plain text rather than a structured JSON payload. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_field_options_v12**
> Dict[str, List[FieldOptionsTransformer]] get_field_options_v12(dataset_name, field_options_request_schema)

Get Field Options (v1.2)

Returns the allowed values for one or more fields in a dataset, for use as filter values when querying data via "Get Data from Dataset (v2)". Pass field names in the `fields` array of the request body; the response is an object keyed by field name, where each value is an array of `{id, value}` option objects. Optionally supply `filters` to narrow the returned options (e.g. only options that exist for active employees) and `dependentFields` when one field's options depend on another field's selected value. Use "Get Fields from Dataset (v1.2)" to discover valid field names for a dataset.

Use this endpoint when you already have dataset field names from `get-fields-from-dataset-v1_2` and need valid filter/display options for those specific dataset fields. It is dataset-scoped: field names must be dataset field name values such as `jobInformationDepartment`, not account list aliases such as `department`. 

Note: Compared to "Get Field Options (v1)", error responses (`400`, `403`) use RFC 7807 `application/problem+json` format. Unrecognised field names may produce a `500` response with a plain-text body rather than structured JSON.

OAuth Scopes: field

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
    dataset_name = 'dataset_name_example' # str | The name of the dataset you want to see field options for. Use \"List Datasets (v1.2)\" to discover available dataset names.
    field_options_request_schema = bamboohr_sdk.FieldOptionsRequestSchema() # FieldOptionsRequestSchema | 

    try:
        # Get Field Options (v1.2)
        api_response = api_instance.get_field_options_v12(dataset_name, field_options_request_schema)
        print("The response of DatasetsApi->get_field_options_v12:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_field_options_v12: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**| The name of the dataset you want to see field options for. Use \&quot;List Datasets (v1.2)\&quot; to discover available dataset names. | 
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
**400** | Bad request - invalid fields, filters, or request format. Uses RFC 7807 problem+json. |  -  |
**403** | Forbidden - insufficient permissions to access this dataset. Uses RFC 7807 problem+json. |  -  |
**500** | Internal server error. The response body may be plain text rather than a structured payload. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fields_from_dataset_v1**
> DatasetFieldsResponse get_fields_from_dataset_v1(dataset_name, page=page, page_size=page_size)

Get Fields from Dataset (v1)

Deprecated. Use "Get Fields from Dataset (v1.2)" instead.

Returns a paginated list of field descriptors for the specified dataset. Each field includes its machine-readable `name`, human-readable `label`, `parentType`, `parentName`, and `entityName`. Use the returned field `name` values in the `fields` array when querying data via "Get Data from Dataset". Use "List Datasets (v1.2)" to discover valid dataset names.

Pagination defaults to page 1 with 500 fields per page (maximum 1000). Out-of-range page numbers are clamped to the nearest valid page. The `next_page` and `prev_page` links in the pagination object are absolute URLs.

Error responses (400, 403, 500) return plain-text bodies, not JSON.

OAuth Scopes: report

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
    dataset_name = 'dataset_name_example' # str | The machine-readable name of the dataset to retrieve fields for. Use \"List Datasets (v1.2)\" to discover valid names.
    page = 1 # int | The page number to retrieve. Out-of-range values are clamped to the nearest valid page. Defaults to 1. (optional) (default to 1)
    page_size = 500 # int | The number of field records to retrieve per page. Defaults to 500. Maximum is 1000. (optional) (default to 500)

    try:
        # Get Fields from Dataset (v1)
        api_response = api_instance.get_fields_from_dataset_v1(dataset_name, page=page, page_size=page_size)
        print("The response of DatasetsApi->get_fields_from_dataset_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_fields_from_dataset_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**| The machine-readable name of the dataset to retrieve fields for. Use \&quot;List Datasets (v1.2)\&quot; to discover valid names. | 
 **page** | **int**| The page number to retrieve. Out-of-range values are clamped to the nearest valid page. Defaults to 1. | [optional] [default to 1]
 **page_size** | **int**| The number of field records to retrieve per page. Defaults to 500. Maximum is 1000. | [optional] [default to 500]

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
**200** | Returns an object containing pagination metadata, the dataset name and label, and a &#x60;fields&#x60; array of field descriptors. |  -  |
**400** | The specified dataset name was not found. The body is a plain-text message. |  -  |
**403** | Insufficient permissions to access dataset fields. The body is a plain-text message. |  -  |
**500** | Internal server error while fetching the dataset configuration. The body is a plain-text message. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fields_from_dataset_v12**
> DatasetFieldsResponse get_fields_from_dataset_v12(dataset_name, page=page, page_size=page_size)

Get Fields from Dataset (v1.2)

Returns a paginated list of field descriptors for the specified dataset. Each field includes its machine-readable `name`, human-readable `label`, parent section type and name, and `entityName`. Use the returned field `name` values in the `fields` array when querying data via "Get Data from Dataset (v2)". Use "List Datasets (v1.2)" to discover valid `datasetName` values. Pagination defaults to page 1 with 500 fields per page (maximum 1000). Out-of-range page numbers are clamped to the nearest valid page. Some datasets, especially `employee`, may return hundreds of fields. This endpoint does not support filtering by parent/entity/type; retrieve all pages and group client-side.

The `employee` dataset field names are fully qualified with their section prefix and differ from the field names used by `list-employees` and `get-employee`. Do not assume a field name from one endpoint works in the other.

For fields whose type is `list`, `multilist`, or another option-backed type, the field `id` can be matched to `fieldId` from `list-list-fields` to retrieve the account-level option list.

Note: Compared to "Get Fields from Dataset (v1)", this version returns RFC 7807 `application/problem+json` error responses and includes an `X-Request-ID` correlation header.

OAuth Scopes: report

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
    dataset_name = 'dataset_name_example' # str | The name of the dataset to retrieve fields for. Use \"List Datasets (v1.2)\" to discover valid names.
    page = 1 # int | The page number to retrieve. Defaults to 1. (optional) (default to 1)
    page_size = 500 # int | The number of records to retrieve per page. Defaults to 500. Maximum is 1000. (optional) (default to 500)

    try:
        # Get Fields from Dataset (v1.2)
        api_response = api_instance.get_fields_from_dataset_v12(dataset_name, page=page, page_size=page_size)
        print("The response of DatasetsApi->get_fields_from_dataset_v12:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_fields_from_dataset_v12: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_name** | **str**| The name of the dataset to retrieve fields for. Use \&quot;List Datasets (v1.2)\&quot; to discover valid names. | 
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
**200** | Returns an object containing pagination metadata, the dataset name and label, and a &#x60;fields&#x60; array of field descriptors. |  * X-Request-ID - Correlation ID for request tracing. Echoes the client-provided value or a generated identifier. <br>  |
**403** | Insufficient permissions to access dataset fields. Uses RFC 7807 problem+json. |  * X-Request-ID - Correlation ID for request tracing. Echoes the client-provided value or a generated identifier. <br>  |
**422** | The specified dataset name was not found. The &#x60;code&#x60; field is &#x60;DATASET_NOT_FOUND&#x60;. |  * X-Request-ID - Correlation ID for request tracing. <br>  |
**500** | Internal server error while fetching the dataset configuration. |  * X-Request-ID - Correlation ID for request tracing. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_datasets_v1**
> DatasetResponseV1 list_datasets_v1()

List Datasets (v1)

Deprecated. Use "List Datasets (v1.2)" instead.

Returns the catalog of datasets available for querying via the Datasets API. Each entry includes a machine-readable `name` (used as the `datasetName` path parameter in "Get Fields from Dataset (v1.2)" and "Get Data from Dataset") and a human-readable `label`. Use this endpoint to discover which datasets the current account has access to before building queries.

The response includes `Deprecation` and `Link` headers pointing to the v1.2 successor endpoint.

OAuth Scopes: report

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.dataset_response_v1 import DatasetResponseV1
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
        # List Datasets (v1)
        api_response = api_instance.list_datasets_v1()
        print("The response of DatasetsApi->list_datasets_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->list_datasets_v1: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DatasetResponseV1**](DatasetResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an object containing a &#x60;datasets&#x60; array of available datasets. |  -  |
**403** | Forbidden - insufficient permissions to access datasets. |  -  |
**500** | Internal server error while retrieving datasets. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_datasets_v12**
> DatasetsResponseV12 list_datasets_v12()

List Datasets (v1.2)

Returns the catalog of datasets available for querying via the Datasets API. Each entry includes a machine-readable `name` (used as the `datasetName` path parameter in "Get Fields from Dataset (v1.2)" and "Get Data from Dataset (v2)") and a human-readable `label`. Use this endpoint to discover which datasets the current account has access to before building queries.

Datasets are queryable reporting datasets for the Datasets API. They are not the same as saved custom reports (`list-reports`), employee tabular table aliases (`list-tabular-fields`), or account list-field definitions (`list-list-fields`).

Note: Compared to "List Datasets (v1)", this version returns RFC 7807 `application/problem+json` error responses and includes an `X-Request-ID` correlation header.

OAuth Scopes: report

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.datasets_response_v12 import DatasetsResponseV12
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
        # List Datasets (v1.2)
        api_response = api_instance.list_datasets_v12()
        print("The response of DatasetsApi->list_datasets_v12:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->list_datasets_v12: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DatasetsResponseV12**](DatasetsResponseV12.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an object containing a &#x60;datasets&#x60; array of available datasets. |  * X-Request-ID - Correlation ID for request tracing. Echoes the client-provided value or a generated identifier. <br>  |
**403** | Forbidden - insufficient permissions to access datasets. |  -  |
**500** | Internal server error while retrieving datasets. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

