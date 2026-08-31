# bamboohr_sdk.HolidaysApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_insert_company_holidays**](HolidaysApi.md#bulk_insert_company_holidays) | **POST** /api/v1/holidays/bulk-insert | Bulk Create Company Holidays
[**create_company_holiday**](HolidaysApi.md#create_company_holiday) | **POST** /api/v1/holidays | Create Company Holiday
[**delete_company_holiday**](HolidaysApi.md#delete_company_holiday) | **DELETE** /api/v1/holidays/{id} | Delete Company Holiday
[**get_catalog_holiday**](HolidaysApi.md#get_catalog_holiday) | **GET** /api/v1/holidays/catalog/{uuid} | Get Catalog Holiday
[**get_company_holiday**](HolidaysApi.md#get_company_holiday) | **GET** /api/v1/holidays/{id} | Get Company Holiday
[**list_catalog_holidays**](HolidaysApi.md#list_catalog_holidays) | **GET** /api/v1/holidays/catalog | List Catalog Holidays
[**list_company_holidays**](HolidaysApi.md#list_company_holidays) | **GET** /api/v1/holidays | List Company Holidays
[**update_company_holiday**](HolidaysApi.md#update_company_holiday) | **PATCH** /api/v1/holidays/{id} | Update Company Holiday


# **bulk_insert_company_holidays**
> HolidayBulkInsertCompanyHolidaysResponseV1 bulk_insert_company_holidays(holiday_create_company_holiday_request_v1, atomic=atomic, return_records=return_records)

Bulk Create Company Holidays

Creates multiple company holidays in one synchronous call. Each record follows the single-create semantics: it may be fully-specified or carry a globalHolidayUuid that seeds name, dates, and countries from the global catalog entry (mix-and-match within the same request). Records are processed in request order.

OAuth Scopes: holidays.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.holiday_bulk_insert_company_holidays_response_v1 import HolidayBulkInsertCompanyHolidaysResponseV1
from bamboohr_sdk.models.holiday_create_company_holiday_request_v1 import HolidayCreateCompanyHolidayRequestV1
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
    api_instance = bamboohr_sdk.HolidaysApi(api_client)
    holiday_create_company_holiday_request_v1 = [bamboohr_sdk.HolidayCreateCompanyHolidayRequestV1()] # List[HolidayCreateCompanyHolidayRequestV1] | 
    atomic = False # bool | When true, the entire batch is committed in a single transaction and any per-record failure aborts the whole request with a 422 (no records are created). When false, each record commits independently and failures are reported per record in a 207 response. Accepted values: true/false, 1/0, yes/no, on/off. (optional) (default to False)
    return_records = False # bool | When true, each entry in the response records array also includes the full created company holiday under the record key. Accepted values: true/false, 1/0, yes/no, on/off. (optional) (default to False)

    try:
        # Bulk Create Company Holidays
        api_response = api_instance.bulk_insert_company_holidays(holiday_create_company_holiday_request_v1, atomic=atomic, return_records=return_records)
        print("The response of HolidaysApi->bulk_insert_company_holidays:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HolidaysApi->bulk_insert_company_holidays: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **holiday_create_company_holiday_request_v1** | [**List[HolidayCreateCompanyHolidayRequestV1]**](HolidayCreateCompanyHolidayRequestV1.md)|  | 
 **atomic** | **bool**| When true, the entire batch is committed in a single transaction and any per-record failure aborts the whole request with a 422 (no records are created). When false, each record commits independently and failures are reported per record in a 207 response. Accepted values: true/false, 1/0, yes/no, on/off. | [optional] [default to False]
 **return_records** | **bool**| When true, each entry in the response records array also includes the full created company holiday under the record key. Accepted values: true/false, 1/0, yes/no, on/off. | [optional] [default to False]

### Return type

[**HolidayBulkInsertCompanyHolidaysResponseV1**](HolidayBulkInsertCompanyHolidaysResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All records were created successfully. |  -  |
**207** | Partial success (non-atomic mode): some records were created and some failed. Per-record errors carry the recordIndex of the failing record in the request body. |  -  |
**400** | Malformed request body: not a JSON array, or a record is not a JSON object. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**422** | Nothing was created. Request-level validation errors (empty array, more than 100 records, an invalid atomic/returnRecords parameter) return a problem-details body. Full batch failures — an atomic abort or a non-atomic batch in which every record failed — return the bulk envelope with status failed and per-record errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_company_holiday**
> HolidayCompanyHolidayV1 create_company_holiday(holiday_create_company_holiday_request_v1)

Create Company Holiday

Creates a company holiday. The body may be fully-specified or carry a globalHolidayUuid that seeds name, dates, and countries from the global catalog entry; partner-supplied values override the catalog defaults.

OAuth Scopes: holidays.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.holiday_company_holiday_v1 import HolidayCompanyHolidayV1
from bamboohr_sdk.models.holiday_create_company_holiday_request_v1 import HolidayCreateCompanyHolidayRequestV1
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
    api_instance = bamboohr_sdk.HolidaysApi(api_client)
    holiday_create_company_holiday_request_v1 = bamboohr_sdk.HolidayCreateCompanyHolidayRequestV1() # HolidayCreateCompanyHolidayRequestV1 | 

    try:
        # Create Company Holiday
        api_response = api_instance.create_company_holiday(holiday_create_company_holiday_request_v1)
        print("The response of HolidaysApi->create_company_holiday:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HolidaysApi->create_company_holiday: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **holiday_create_company_holiday_request_v1** | [**HolidayCreateCompanyHolidayRequestV1**](HolidayCreateCompanyHolidayRequestV1.md)|  | 

### Return type

[**HolidayCompanyHolidayV1**](HolidayCompanyHolidayV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created company holiday. |  -  |
**400** | Malformed request body. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | The supplied globalHolidayUuid does not exist in the catalog. |  -  |
**409** | The supplied globalHolidayUuid already exists on an active company holiday. |  -  |
**422** | Validation error, or the audience or holidayPay block violates its mode rules. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_company_holiday**
> delete_company_holiday(id)

Delete Company Holiday

Soft-deletes a company holiday and removes its audience, pay, and country sub-rows. Idempotent: deleting a missing or already-deleted holiday also returns 204.

OAuth Scopes: holidays.write

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
    api_instance = bamboohr_sdk.HolidaysApi(api_client)
    id = 56 # int | The company holiday ID.

    try:
        # Delete Company Holiday
        api_instance.delete_company_holiday(id)
    except Exception as e:
        print("Exception when calling HolidaysApi->delete_company_holiday: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The company holiday ID. | 

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
**204** | Holiday deleted. Also returned when the holiday does not exist or was already deleted. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_holiday**
> GlobalHolidayGlobalHolidayV1 get_catalog_holiday(uuid)

Get Catalog Holiday

Gets a global holiday catalog entry by UUID.

OAuth Scopes: holidays

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.global_holiday_global_holiday_v1 import GlobalHolidayGlobalHolidayV1
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
    api_instance = bamboohr_sdk.HolidaysApi(api_client)
    uuid = 'uuid_example' # str | The catalog entry UUID.

    try:
        # Get Catalog Holiday
        api_response = api_instance.get_catalog_holiday(uuid)
        print("The response of HolidaysApi->get_catalog_holiday:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HolidaysApi->get_catalog_holiday: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The catalog entry UUID. | 

### Return type

[**GlobalHolidayGlobalHolidayV1**](GlobalHolidayGlobalHolidayV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The catalog holiday. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | Catalog entry not found. |  -  |
**422** | Malformed UUID. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_holiday**
> HolidayCompanyHolidayV1 get_company_holiday(id)

Get Company Holiday

Gets a company holiday by ID.

OAuth Scopes: holidays

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.holiday_company_holiday_v1 import HolidayCompanyHolidayV1
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
    api_instance = bamboohr_sdk.HolidaysApi(api_client)
    id = 56 # int | The company holiday ID.

    try:
        # Get Company Holiday
        api_response = api_instance.get_company_holiday(id)
        print("The response of HolidaysApi->get_company_holiday:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HolidaysApi->get_company_holiday: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The company holiday ID. | 

### Return type

[**HolidayCompanyHolidayV1**](HolidayCompanyHolidayV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The company holiday. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | Holiday not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_catalog_holidays**
> HolidayCatalogHolidayListResponseV1 list_catalog_holidays(country_code=country_code, year=year, filter=filter, order_by=order_by, page=page, page_size=page_size)

List Catalog Holidays

Lists entries in the global holiday catalog. The catalog is read-only system reference data; use the returned uuid values to seed company holidays.

OAuth Scopes: holidays

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.holiday_catalog_holiday_list_response_v1 import HolidayCatalogHolidayListResponseV1
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
    api_instance = bamboohr_sdk.HolidaysApi(api_client)
    country_code = 'country_code_example' # str | ISO 3166-1 alpha-2 country code. Filters the catalog to entries for the given country. (optional)
    year = 56 # int | Calendar year. Filters the catalog to entries whose startDate falls in the given year. (optional)
    filter = 'filter_example' # str | OData v4 filter expression. Supported fields: name, type, countryCode, startDate. Example: startDate ge '2026-01-01' and type eq 'PUBLIC' (optional)
    order_by = 'startDate asc' # str | Sort expression. Allowed fields: startDate, name, with optional asc/desc direction. (optional) (default to 'startDate asc')
    page = 1 # int | Page number. (optional) (default to 1)
    page_size = 20 # int | Page size. (optional) (default to 20)

    try:
        # List Catalog Holidays
        api_response = api_instance.list_catalog_holidays(country_code=country_code, year=year, filter=filter, order_by=order_by, page=page, page_size=page_size)
        print("The response of HolidaysApi->list_catalog_holidays:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HolidaysApi->list_catalog_holidays: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| ISO 3166-1 alpha-2 country code. Filters the catalog to entries for the given country. | [optional] 
 **year** | **int**| Calendar year. Filters the catalog to entries whose startDate falls in the given year. | [optional] 
 **filter** | **str**| OData v4 filter expression. Supported fields: name, type, countryCode, startDate. Example: startDate ge &#39;2026-01-01&#39; and type eq &#39;PUBLIC&#39; | [optional] 
 **order_by** | **str**| Sort expression. Allowed fields: startDate, name, with optional asc/desc direction. | [optional] [default to &#39;startDate asc&#39;]
 **page** | **int**| Page number. | [optional] [default to 1]
 **page_size** | **int**| Page size. | [optional] [default to 20]

### Return type

[**HolidayCatalogHolidayListResponseV1**](HolidayCatalogHolidayListResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of catalog holidays. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**422** | Invalid query parameter. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_company_holidays**
> HolidayCompanyHolidayListResponseV1 list_company_holidays(filter=filter, order_by=order_by, select=select, page=page, page_size=page_size)

List Company Holidays

Returns a paginated list of active company holidays. Soft-deleted holidays are never returned. Supports OData filtering via `filter`, sorting via `orderBy`, field projection via `select`, and page-based pagination.

OAuth Scopes: holidays

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.holiday_company_holiday_list_response_v1 import HolidayCompanyHolidayListResponseV1
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
    api_instance = bamboohr_sdk.HolidaysApi(api_client)
    filter = 'filter_example' # str | OData filter expression applied to company holidays. Supported operators: `eq` (equals, use `eq null` to match NULL), `ne` (not equals, use `ne null` to match NOT NULL), `lt` (less than), `le` (less than or equal), `gt` (greater than), `ge` (greater than or equal), `in` (value in list), `and` (combine clauses). Not supported: `or`, `not`, parenthesized grouping. Filterable fields: `name`, `startDate`, `endDate`, `isPublic`, `globalHolidayUuid`. Examples: `startDate ge '2026-01-01'`, `isPublic eq true and endDate ne null`. (optional)
    order_by = 'startDate asc' # str | Comma-separated list of sort terms, each a field optionally followed by `asc` or `desc`. Allowed sort fields: `name`, `startDate`, `endDate`, `createdAt`, `updatedAt`. (optional) (default to 'startDate asc')
    select = 'select_example' # str | Comma-separated list of properties to include in each returned holiday. Reduces payload size. Example: `id,name,startDate`. (optional)
    page = 1 # int | The page number to retrieve. (optional) (default to 1)
    page_size = 20 # int | The number of items to return per page. (optional) (default to 20)

    try:
        # List Company Holidays
        api_response = api_instance.list_company_holidays(filter=filter, order_by=order_by, select=select, page=page, page_size=page_size)
        print("The response of HolidaysApi->list_company_holidays:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HolidaysApi->list_company_holidays: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| OData filter expression applied to company holidays. Supported operators: &#x60;eq&#x60; (equals, use &#x60;eq null&#x60; to match NULL), &#x60;ne&#x60; (not equals, use &#x60;ne null&#x60; to match NOT NULL), &#x60;lt&#x60; (less than), &#x60;le&#x60; (less than or equal), &#x60;gt&#x60; (greater than), &#x60;ge&#x60; (greater than or equal), &#x60;in&#x60; (value in list), &#x60;and&#x60; (combine clauses). Not supported: &#x60;or&#x60;, &#x60;not&#x60;, parenthesized grouping. Filterable fields: &#x60;name&#x60;, &#x60;startDate&#x60;, &#x60;endDate&#x60;, &#x60;isPublic&#x60;, &#x60;globalHolidayUuid&#x60;. Examples: &#x60;startDate ge &#39;2026-01-01&#39;&#x60;, &#x60;isPublic eq true and endDate ne null&#x60;. | [optional] 
 **order_by** | **str**| Comma-separated list of sort terms, each a field optionally followed by &#x60;asc&#x60; or &#x60;desc&#x60;. Allowed sort fields: &#x60;name&#x60;, &#x60;startDate&#x60;, &#x60;endDate&#x60;, &#x60;createdAt&#x60;, &#x60;updatedAt&#x60;. | [optional] [default to &#39;startDate asc&#39;]
 **select** | **str**| Comma-separated list of properties to include in each returned holiday. Reduces payload size. Example: &#x60;id,name,startDate&#x60;. | [optional] 
 **page** | **int**| The page number to retrieve. | [optional] [default to 1]
 **page_size** | **int**| The number of items to return per page. | [optional] [default to 20]

### Return type

[**HolidayCompanyHolidayListResponseV1**](HolidayCompanyHolidayListResponseV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of company holidays. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**422** | Invalid query parameter (bad page or pageSize, unsupported filter/sort/select field, or malformed filter expression). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_company_holiday**
> HolidayCompanyHolidayV1 update_company_holiday(id, holiday_update_company_holiday_request_v1)

Update Company Holiday

Updates a company holiday with a JSON Merge Patch (RFC 7396) document. Only the fields present in the patch change; countryCodes, audience, and holidayPay replace their stored blocks wholesale when supplied. Send null for endDate to revert to a single-day holiday and null for holidayPay to clear the pay treatment. globalHolidayUuid is read-only and rejected if present.

OAuth Scopes: holidays.write

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.holiday_company_holiday_v1 import HolidayCompanyHolidayV1
from bamboohr_sdk.models.holiday_update_company_holiday_request_v1 import HolidayUpdateCompanyHolidayRequestV1
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
    api_instance = bamboohr_sdk.HolidaysApi(api_client)
    id = 56 # int | The company holiday ID.
    holiday_update_company_holiday_request_v1 = bamboohr_sdk.HolidayUpdateCompanyHolidayRequestV1() # HolidayUpdateCompanyHolidayRequestV1 | 

    try:
        # Update Company Holiday
        api_response = api_instance.update_company_holiday(id, holiday_update_company_holiday_request_v1)
        print("The response of HolidaysApi->update_company_holiday:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HolidaysApi->update_company_holiday: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The company holiday ID. | 
 **holiday_update_company_holiday_request_v1** | [**HolidayUpdateCompanyHolidayRequestV1**](HolidayUpdateCompanyHolidayRequestV1.md)|  | 

### Return type

[**HolidayCompanyHolidayV1**](HolidayCompanyHolidayV1.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated company holiday. |  -  |
**400** | Malformed request body. |  -  |
**401** | Unauthorized. Missing or invalid authentication. |  -  |
**403** | Forbidden. Insufficient permissions. |  -  |
**404** | Holiday not found. |  -  |
**415** | Unsupported media type. The request Content-Type is not application/merge-patch+json. |  -  |
**422** | Validation error, or the audience or holidayPay block violates its mode rules. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

