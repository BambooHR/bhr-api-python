# bamboohr_sdk.TabularDataApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_employee_table_row**](TabularDataApi.md#add_employee_table_row) | **POST** /api/v1/employees/{id}/tables/{table} | Create Table Row
[**add_employee_table_row_v1**](TabularDataApi.md#add_employee_table_row_v1) | **POST** /api/v1_1/employees/{id}/tables/{table} | Create Table Row v1.1
[**delete_employee_table_row_v1**](TabularDataApi.md#delete_employee_table_row_v1) | **DELETE** /api/v1/employees/{id}/tables/{table}/{rowId} | Delete Table Row
[**get_changed_employee_table_data**](TabularDataApi.md#get_changed_employee_table_data) | **GET** /api/v1/employees/changed/tables/{table} | Get Changed Employee Table Data
[**get_employee_table_row**](TabularDataApi.md#get_employee_table_row) | **GET** /api/v1/employees/{id}/tables/{table} | Get Employee Table Rows
[**update_employee_table_row**](TabularDataApi.md#update_employee_table_row) | **POST** /api/v1/employees/{id}/tables/{table}/{rowId} | Update Table Row
[**update_employee_table_row_v**](TabularDataApi.md#update_employee_table_row_v) | **POST** /api/v1_1/employees/{id}/tables/{table}/{rowId} | Update Table Row v1.1


# **add_employee_table_row**
> add_employee_table_row(id, table, table_row_update)

Create Table Row

Adds a table row. If employee is currently on a pay schedule syncing with Trax Payroll, or being added to one, the row cannot be added if they are missing any required fields for that table. If the API user is adding a row on the compensation table, the row cannot be added if they are missing any of the required employee fields (including fields not on that table).

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.table_row_update import TableRowUpdate
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
    api_instance = bamboohr_sdk.TabularDataApi(api_client)
    id = 'id_example' # str | {id} is the employee ID.
    table = 'table_example' # str | Table name
    table_row_update = bamboohr_sdk.TableRowUpdate() # TableRowUpdate | 

    try:
        # Create Table Row
        api_instance.add_employee_table_row(id, table, table_row_update)
    except Exception as e:
        print("Exception when calling TabularDataApi->add_employee_table_row: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| {id} is the employee ID. | 
 **table** | **str**| Table name | 
 **table_row_update** | [**TableRowUpdate**](TableRowUpdate.md)|  | 

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
**200** | Row added successfully. |  -  |
**400** | Invalid or missing required fields. |  -  |
**406** | An error with one or more of the fields. |  -  |
**403** | Permission denied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_employee_table_row_v1**
> add_employee_table_row_v1(id, table, table_row_update)

Create Table Row v1.1

Adds a table row. Fundamentally the same as version 1 so choose a version and stay with it unless other changes occur. Changes from version 1 are now minor with a few variations limited to ACA, payroll, terminated rehire, gusto, benetrac, and final pay date.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.table_row_update import TableRowUpdate
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
    api_instance = bamboohr_sdk.TabularDataApi(api_client)
    id = 'id_example' # str | {id} is the employee ID.
    table = 'table_example' # str | Table name
    table_row_update = bamboohr_sdk.TableRowUpdate() # TableRowUpdate | 

    try:
        # Create Table Row v1.1
        api_instance.add_employee_table_row_v1(id, table, table_row_update)
    except Exception as e:
        print("Exception when calling TabularDataApi->add_employee_table_row_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| {id} is the employee ID. | 
 **table** | **str**| Table name | 
 **table_row_update** | [**TableRowUpdate**](TableRowUpdate.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_employee_table_row_v1**
> TableRowDeleteResponse delete_employee_table_row_v1(id, table, row_id)

Delete Table Row

Deletes a table row

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.table_row_delete_response import TableRowDeleteResponse
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
    api_instance = bamboohr_sdk.TabularDataApi(api_client)
    id = 'id_example' # str | {id} is the employee ID.
    table = 'table_example' # str | Table name
    row_id = 'row_id_example' # str | Row ID

    try:
        # Delete Table Row
        api_response = api_instance.delete_employee_table_row_v1(id, table, row_id)
        print("The response of TabularDataApi->delete_employee_table_row_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TabularDataApi->delete_employee_table_row_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| {id} is the employee ID. | 
 **table** | **str**| Table name | 
 **row_id** | **str**| Row ID | 

### Return type

[**TableRowDeleteResponse**](TableRowDeleteResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Respond true if the row was deleted, false if the row was not found. |  -  |
**400** | Bad request. Invalid employee ID or table name. |  -  |
**401** | Unauthorized. |  -  |
**403** | Permission denied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_changed_employee_table_data**
> get_changed_employee_table_data(table, since)

Get Changed Employee Table Data

This API is merely an optimization to avoid downloading all table data for all employees. When you use this API you will provide a timestamp and the results will be limited to just the employees that have changed since the time you provided. This API operates on an employee-last-changed-timestamp, which means that a change in ANY field in the employee record will cause ALL of that employees table rows to show up via this API.

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
    api_instance = bamboohr_sdk.TabularDataApi(api_client)
    table = 'table_example' # str | Table name
    since = 'since_example' # str | URL encoded iso8601 timestamp

    try:
        # Get Changed Employee Table Data
        api_instance.get_changed_employee_table_data(table, since)
    except Exception as e:
        print("Exception when calling TabularDataApi->get_changed_employee_table_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table** | **str**| Table name | 
 **since** | **str**| URL encoded iso8601 timestamp | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_table_row**
> get_employee_table_row(id, table)

Get Employee Table Rows

Returns a data structure representing all the table rows for a given employee and table combination. The result is not sorted in any particular order.

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
    api_instance = bamboohr_sdk.TabularDataApi(api_client)
    id = 'id_example' # str | {id} is the employee ID.
    table = 'table_example' # str | Table name

    try:
        # Get Employee Table Rows
        api_instance.get_employee_table_row(id, table)
    except Exception as e:
        print("Exception when calling TabularDataApi->get_employee_table_row: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| {id} is the employee ID. | 
 **table** | **str**| Table name | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_employee_table_row**
> update_employee_table_row(id, table, row_id, table_row_update)

Update Table Row

Updates a table row. If employee is currently on a pay schedule syncing with Trax Payroll, or being added to one, the row cannot be added if they are missing any required fields for that table. If the API user is updating a row on the compensation table, the row cannot be updated if they are missing any of the required employee fields (including fields not on that table).

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.table_row_update import TableRowUpdate
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
    api_instance = bamboohr_sdk.TabularDataApi(api_client)
    id = 'id_example' # str | {id} is the employee ID.
    table = 'table_example' # str | Table name
    row_id = 'row_id_example' # str | Row ID
    table_row_update = bamboohr_sdk.TableRowUpdate() # TableRowUpdate | 

    try:
        # Update Table Row
        api_instance.update_employee_table_row(id, table, row_id, table_row_update)
    except Exception as e:
        print("Exception when calling TabularDataApi->update_employee_table_row: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| {id} is the employee ID. | 
 **table** | **str**| Table name | 
 **row_id** | **str**| Row ID | 
 **table_row_update** | [**TableRowUpdate**](TableRowUpdate.md)|  | 

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
**200** | A successful response is possible even if one or more updates were dis-allowed because of permissions. As long as a single field is updated a 200 response will be returned. |  -  |
**400** | Invalid or missing required fields. |  -  |
**406** | An error with one or more of the fields. |  -  |
**403** | Permission denied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_employee_table_row_v**
> update_employee_table_row_v(id, table, row_id, table_row_update)

Update Table Row v1.1

Updates a table row. Fundamentally the same as version 1 so choose a version and stay with it unless other changes occur. Changes from version 1 are now minor with a few variations limited to ACA, payroll, terminated rehire, gusto, benetrac, and final pay date.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.table_row_update import TableRowUpdate
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
    api_instance = bamboohr_sdk.TabularDataApi(api_client)
    id = 'id_example' # str | {id} is the employee ID.
    table = 'table_example' # str | Table name
    row_id = 'row_id_example' # str | Row ID
    table_row_update = bamboohr_sdk.TableRowUpdate() # TableRowUpdate | 

    try:
        # Update Table Row v1.1
        api_instance.update_employee_table_row_v(id, table, row_id, table_row_update)
    except Exception as e:
        print("Exception when calling TabularDataApi->update_employee_table_row_v: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| {id} is the employee ID. | 
 **table** | **str**| Table name | 
 **row_id** | **str**| Row ID | 
 **table_row_update** | [**TableRowUpdate**](TableRowUpdate.md)|  | 

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
**200** | A successful response is possible even if one or more updates were dis-allowed because of permissions. As long as a single field is updated a 200 response will be returned. |  -  |
**400** | Invalid or missing required fields. |  -  |
**406** | An error with one or more of the fields. |  -  |
**403** | Permission denied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

