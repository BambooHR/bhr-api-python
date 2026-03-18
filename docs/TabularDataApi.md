# bamboohr_sdk.TabularDataApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_table_row**](TabularDataApi.md#create_table_row) | **POST** /api/v1/employees/{id}/tables/{table} | Create Table Row
[**create_table_row_v11**](TabularDataApi.md#create_table_row_v11) | **POST** /api/v1_1/employees/{id}/tables/{table} | Create Table Row v1.1
[**delete_employee_table_row**](TabularDataApi.md#delete_employee_table_row) | **DELETE** /api/v1/employees/{id}/tables/{table}/{rowId} | Delete Employee Table Row
[**get_changed_employee_table_data**](TabularDataApi.md#get_changed_employee_table_data) | **GET** /api/v1/employees/changed/tables/{table} | Get Changed Employee Table Data
[**get_employee_table_data**](TabularDataApi.md#get_employee_table_data) | **GET** /api/v1/employees/{id}/tables/{table} | Get Employee Table Data
[**update_table_row**](TabularDataApi.md#update_table_row) | **POST** /api/v1/employees/{id}/tables/{table}/{rowId} | Update Table Row
[**update_table_row_v11**](TabularDataApi.md#update_table_row_v11) | **POST** /api/v1_1/employees/{id}/tables/{table}/{rowId} | Update Table Row v1.1


# **create_table_row**
> create_table_row(id, table, table_row_update)

Create Table Row

Add a new row to the specified employee table by submitting field name/value pairs in JSON or XML. Use this endpoint to append records to tabular employee data such as job information or compensation history.

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
    id = 'id_example' # str | The employee ID.
    table = 'table_example' # str | The name of the table to add a row to (e.g., jobInfo, compensation).
    table_row_update = bamboohr_sdk.TableRowUpdate() # TableRowUpdate | 

    try:
        # Create Table Row
        api_instance.create_table_row(id, table, table_row_update)
    except Exception as e:
        print("Exception when calling TabularDataApi->create_table_row: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The employee ID. | 
 **table** | **str**| The name of the table to add a row to (e.g., jobInfo, compensation). | 
 **table_row_update** | [**TableRowUpdate**](TableRowUpdate.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, text/xml
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Row added successfully. No response body is returned. |  -  |
**400** | The posted JSON or XML is malformed, or required fields are missing. |  -  |
**403** | Permission denied. |  -  |
**404** | The employee or table does not exist. |  -  |
**406** | One or more field values are invalid. |  -  |
**409** | Conflict. The provided field values conflict with business rules or payroll constraints. |  -  |
**412** | Precondition failed. The update requires an active pay schedule or other required prerequisite data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_table_row_v11**
> create_table_row_v11(id, table, table_row_update)

Create Table Row v1.1

Add a new row to the specified employee table using the v1.1 table-row creation endpoint. Submit the new row in JSON or XML. This version is largely compatible with v1 and supports the same tabular employee data use cases.

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
    id = 'id_example' # str | The employee ID.
    table = 'table_example' # str | The name of the table to add a row to (e.g., jobInfo, compensation).
    table_row_update = bamboohr_sdk.TableRowUpdate() # TableRowUpdate | 

    try:
        # Create Table Row v1.1
        api_instance.create_table_row_v11(id, table, table_row_update)
    except Exception as e:
        print("Exception when calling TabularDataApi->create_table_row_v11: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The employee ID. | 
 **table** | **str**| The name of the table to add a row to (e.g., jobInfo, compensation). | 
 **table_row_update** | [**TableRowUpdate**](TableRowUpdate.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, text/xml
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Row added successfully. No response body is returned. |  -  |
**400** | The posted JSON or XML is malformed, or required fields are missing. |  -  |
**403** | Permission denied. |  -  |
**404** | The employee or table does not exist. |  -  |
**406** | One or more field values are invalid. |  -  |
**409** | Conflict. The provided field values conflict with business rules or payroll constraints. |  -  |
**412** | Precondition failed. The update requires an active pay schedule or other required prerequisite data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_employee_table_row**
> TableRowDeleteResponse delete_employee_table_row(id, table, row_id)

Delete Employee Table Row

Deletes a specific row from an employee's tabular data. The table name identifies which tabular dataset to target (e.g., jobInfo, compensation, customTabularField). Returns `success: true` if the row was deleted, or `success: false` with an error message if the row was not found or could not be deleted. Deletion will fail with a 409 if the row has pending approval changes, or a 412 if the row is tied to an active pay schedule.

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
    id = 'id_example' # str | The employee ID.
    table = 'table_example' # str | The name of the table containing the row to delete (e.g., jobInfo, compensation, customTabularField).
    row_id = 'row_id_example' # str | The ID of the specific row to delete.

    try:
        # Delete Employee Table Row
        api_response = api_instance.delete_employee_table_row(id, table, row_id)
        print("The response of TabularDataApi->delete_employee_table_row:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TabularDataApi->delete_employee_table_row: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The employee ID. | 
 **table** | **str**| The name of the table containing the row to delete (e.g., jobInfo, compensation, customTabularField). | 
 **row_id** | **str**| The ID of the specific row to delete. | 

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
**200** | Returns &#x60;success: true&#x60; if the row was deleted. Returns &#x60;success: false&#x60; with an error message if the row was not found or could not be deleted. |  -  |
**400** | Bad request. Invalid employee ID or table name. |  -  |
**401** | Unauthorized. |  -  |
**403** | Permission denied. The caller lacks write access to this table for the specified employee. |  -  |
**409** | Conflict. The row has pending approval changes and cannot be deleted until they are resolved. |  -  |
**412** | Precondition failed. The row cannot be deleted because it is tied to an active pay schedule. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_changed_employee_table_data**
> ChangedEmployeeTableDataResponse get_changed_employee_table_data(table, since)

Get Changed Employee Table Data

Returns table data for employees that have changed since the given timestamp. This is an optimization to avoid downloading all table data for all employees. It operates on an employee-last-changed-timestamp, which means that a change in ANY field in the employee record will cause ALL of that employee's table rows to show up via this API. The response includes the table rows grouped by employee ID with their last-changed timestamps.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.changed_employee_table_data_response import ChangedEmployeeTableDataResponse
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
    table = 'table_example' # str | The name of the table to retrieve changed data for (e.g., jobInfo, compensation).
    since = '2013-10-20T19:20:30+01:00' # datetime | ISO 8601 timestamp (URL-encoded). Only employees changed since this timestamp will be returned.

    try:
        # Get Changed Employee Table Data
        api_response = api_instance.get_changed_employee_table_data(table, since)
        print("The response of TabularDataApi->get_changed_employee_table_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TabularDataApi->get_changed_employee_table_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table** | **str**| The name of the table to retrieve changed data for (e.g., jobInfo, compensation). | 
 **since** | **datetime**| ISO 8601 timestamp (URL-encoded). Only employees changed since this timestamp will be returned. | 

### Return type

[**ChangedEmployeeTableDataResponse**](ChangedEmployeeTableDataResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Changed table data for the specified table, grouped by employee ID. |  -  |
**400** | The since parameter is missing or is not a valid ISO 8601 date. |  -  |
**404** | The specified table does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_table_data**
> List[EmployeeTableRow] get_employee_table_data(id, table, accept_header_parameter=accept_header_parameter)

Get Employee Table Data

Returns all rows for a given employee and table combination. The result is not sorted in any particular order. Each row contains the fields defined for that table, subject to field-level permission checks. Fields the caller does not have access to are omitted from the response.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.employee_table_row import EmployeeTableRow
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
    id = 'id_example' # str | The employee ID. Use the special value \"all\" to retrieve table data for all employees the API user has access to.
    table = 'table_example' # str | The name of the table to retrieve (e.g., jobInfo, compensation, employmentStatus).
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)

    try:
        # Get Employee Table Data
        api_response = api_instance.get_employee_table_data(id, table, accept_header_parameter=accept_header_parameter)
        print("The response of TabularDataApi->get_employee_table_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TabularDataApi->get_employee_table_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The employee ID. Use the special value \&quot;all\&quot; to retrieve table data for all employees the API user has access to. | 
 **table** | **str**| The name of the table to retrieve (e.g., jobInfo, compensation, employmentStatus). | 
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 

### Return type

[**List[EmployeeTableRow]**](EmployeeTableRow.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All rows for the specified employee and table. |  -  |
**404** | The employee or table does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_table_row**
> update_table_row(id, table, row_id, table_row_update)

Update Table Row

Update an existing row in the specified employee table by submitting field name/value pairs for the fields to change in JSON or XML.

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
    id = 'id_example' # str | The employee ID.
    table = 'table_example' # str | The name of the table containing the row to update (e.g., jobInfo, compensation).
    row_id = 'row_id_example' # str | The ID of the row to update.
    table_row_update = bamboohr_sdk.TableRowUpdate() # TableRowUpdate | 

    try:
        # Update Table Row
        api_instance.update_table_row(id, table, row_id, table_row_update)
    except Exception as e:
        print("Exception when calling TabularDataApi->update_table_row: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The employee ID. | 
 **table** | **str**| The name of the table containing the row to update (e.g., jobInfo, compensation). | 
 **row_id** | **str**| The ID of the row to update. | 
 **table_row_update** | [**TableRowUpdate**](TableRowUpdate.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, text/xml
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Row updated successfully. A 200 response is returned as long as at least one field was updated, even if some fields were skipped due to permissions. No response body is returned. |  -  |
**400** | The posted JSON or XML is malformed, or required fields are missing. |  -  |
**403** | Permission denied. |  -  |
**404** | The employee, table, or row does not exist. |  -  |
**406** | One or more field values are invalid. |  -  |
**409** | Conflict. The provided field values conflict with business rules or payroll constraints. |  -  |
**412** | Precondition failed. The update requires an active pay schedule or other required prerequisite data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_table_row_v11**
> update_table_row_v11(id, table, row_id, table_row_update)

Update Table Row v1.1

Update an existing row in the specified employee table using the v1.1 table-row update endpoint. Submit the field changes in JSON or XML. This version is largely compatible with v1 and is intended for the same tabular employee data use cases.

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
    id = 'id_example' # str | The employee ID.
    table = 'table_example' # str | The name of the table containing the row to update (e.g., jobInfo, compensation).
    row_id = 'row_id_example' # str | The ID of the row to update.
    table_row_update = bamboohr_sdk.TableRowUpdate() # TableRowUpdate | 

    try:
        # Update Table Row v1.1
        api_instance.update_table_row_v11(id, table, row_id, table_row_update)
    except Exception as e:
        print("Exception when calling TabularDataApi->update_table_row_v11: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The employee ID. | 
 **table** | **str**| The name of the table containing the row to update (e.g., jobInfo, compensation). | 
 **row_id** | **str**| The ID of the row to update. | 
 **table_row_update** | [**TableRowUpdate**](TableRowUpdate.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, text/xml
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Row updated successfully. A 200 response is returned as long as at least one field was updated, even if some fields were skipped due to permissions. No response body is returned. |  -  |
**400** | The posted JSON or XML is malformed, or required fields are missing. |  -  |
**403** | Permission denied. |  -  |
**404** | The employee, table, or row does not exist. |  -  |
**406** | One or more field values are invalid. |  -  |
**409** | Conflict. The provided field values conflict with business rules or payroll constraints. |  -  |
**412** | Precondition failed. The update requires an active pay schedule or other required prerequisite data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

