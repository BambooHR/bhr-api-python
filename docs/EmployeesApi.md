# bamboohr_sdk.EmployeesApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_employee**](EmployeesApi.md#add_employee) | **POST** /api/v1/employees | Create Employee
[**get_company_information**](EmployeesApi.md#get_company_information) | **GET** /api/v1/company_information | Get Company Information
[**get_employee**](EmployeesApi.md#get_employee) | **GET** /api/v1/employees/{id} | Get Employee
[**get_employees_directory**](EmployeesApi.md#get_employees_directory) | **GET** /api/v1/employees/directory | Get Employee Directory
[**get_employees_list**](EmployeesApi.md#get_employees_list) | **GET** /api/v1/employees | Get Employees
[**update_employee**](EmployeesApi.md#update_employee) | **POST** /api/v1/employees/{id} | Update Employee


# **add_employee**
> add_employee(post_new_employee)

Create Employee

Add a new employee. New employees must have at least a first name and a last name. The ID of the newly created employee is included in the Location header of the response. Other fields can be included. Please see the [fields](ref:metadata-get-a-list-of-fields) endpoint. New Employees added to a pay schedule synced with Trax Payroll must have the following required fields (listed by API field name): employeeNumber, firstName, lastName, dateOfBirth, ssn or ein, gender, maritalStatus, hireDate, address1, city, state, country, employmentHistoryStatus, exempt, payType, payRate, payPer, location, department, and division.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.post_new_employee import PostNewEmployee
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
    api_instance = bamboohr_sdk.EmployeesApi(api_client)
    post_new_employee = bamboohr_sdk.PostNewEmployee() # PostNewEmployee | 

    try:
        # Create Employee
        api_instance.add_employee(post_new_employee)
    except Exception as e:
        print("Exception when calling EmployeesApi->add_employee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_new_employee** | [**PostNewEmployee**](PostNewEmployee.md)|  | 

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
**201** | Additionally, an HTTP Location: header that points to the new API URL for the new employee will be returned. |  * Location - The URL to view the employee in the web app. The ID of the employee will be included. <br>  |
**400** | If the posted XML or JSON is invalid or the minimum fields are not provided. |  -  |
**403** | If the API user does not have permission to add an employee. |  -  |
**409** | If an employee field was given an invalid value. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_information**
> CompanyInformation get_company_information()

Get Company Information

Gets Company Information

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.company_information import CompanyInformation
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
    api_instance = bamboohr_sdk.EmployeesApi(api_client)

    try:
        # Get Company Information
        api_response = api_instance.get_company_information()
        print("The response of EmployeesApi->get_company_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->get_company_information: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CompanyInformation**](CompanyInformation.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Company Information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee**
> Employee get_employee(fields, id, only_current=only_current, accept_header_parameter=accept_header_parameter)

Get Employee

Get employee data by specifying a set of fields. This is suitable for getting basic employee information, including current values for fields that are part of a historical table, like job title, or compensation information. See the [fields](ref:metadata-get-a-list-of-fields) endpoint for a list of possible fields.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.employee import Employee
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
    api_instance = bamboohr_sdk.EmployeesApi(api_client)
    fields = 'firstName,lastName' # str | {fields} is a comma separated list of values taken from the official list of field names.  (default to 'firstName,lastName')
    id = '0' # str | {id} is an employee ID. The special employee ID of zero (0) means to use the employee ID associated with the API key (if any). (default to '0')
    only_current = False # bool | Setting to false will return future dated values from history table fields. (optional) (default to False)
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)

    try:
        # Get Employee
        api_response = api_instance.get_employee(fields, id, only_current=only_current, accept_header_parameter=accept_header_parameter)
        print("The response of EmployeesApi->get_employee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->get_employee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| {fields} is a comma separated list of values taken from the official list of field names.  | [default to &#39;firstName,lastName&#39;]
 **id** | **str**| {id} is an employee ID. The special employee ID of zero (0) means to use the employee ID associated with the API key (if any). | [default to &#39;0&#39;]
 **only_current** | **bool**| Setting to false will return future dated values from history table fields. | [optional] [default to False]
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 

### Return type

[**Employee**](Employee.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Employee |  -  |
**403** | if the API user does not have permission to see the requested employee. |  -  |
**404** | if the employee does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employees_directory**
> JsonDirectoryEmployee get_employees_directory(accept_header_parameter=accept_header_parameter)

Get Employee Directory

Gets employee directory.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.json_directory_employee import JsonDirectoryEmployee
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
    api_instance = bamboohr_sdk.EmployeesApi(api_client)
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)

    try:
        # Get Employee Directory
        api_response = api_instance.get_employees_directory(accept_header_parameter=accept_header_parameter)
        print("The response of EmployeesApi->get_employees_directory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->get_employees_directory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 

### Return type

[**JsonDirectoryEmployee**](JsonDirectoryEmployee.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Employee directory with fieldset definitions and employee data |  -  |
**403** | if the directory has not been shared company-wide. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employees_list**
> GetEmployeesResponseObject get_employees_list(filter=filter, sort=sort, page=page, fields=fields)

Get Employees

Retrieve a paginated list of employees with optional filtering and sorting. Returns a fixed set of simple employee fields that support efficient filter and sort operations. For more complex employee data, use the single-employee endpoint or the Datasets API for bulk queries.

### Example

* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.cursor_pagination_query_object import CursorPaginationQueryObject
from bamboohr_sdk.models.get_employees_filter_request_object import GetEmployeesFilterRequestObject
from bamboohr_sdk.models.get_employees_response_object import GetEmployeesResponseObject
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
    api_instance = bamboohr_sdk.EmployeesApi(api_client)
    filter = bamboohr_sdk.GetEmployeesFilterRequestObject() # GetEmployeesFilterRequestObject | Filters used to match employees. Encode filter properties using deepObject style. If the caller does not have access to the filtered field on a matching employee, that employee is excluded from the results to avoid leaking sensitive data. (optional)
    sort = 'sort_example' # str | Comma-separated list of sortable fields. Prefix a field with \"-\" for descending order. Allowed fields: `employeeId`, `firstName`, `lastName`, `preferredName`, `jobTitleName`, `status`. Nulls sort first in ascending order and last in descending order. If the caller does not have access to the sort field for an employee, that employee is excluded from the final result set to avoid leaking sensitive information. (optional)
    page = bamboohr_sdk.CursorPaginationQueryObject() # CursorPaginationQueryObject | Cursor-based pagination parameters (`limit`, `after`, `before`). (optional)
    fields = 'workEmail,hireDate,employeeNumber' # str | Comma-separated list of additional fields to include in the response. Default fields (employeeId, firstName, lastName, preferredName, photoUrl, jobTitleName, status) are always included. Invalid field names are silently ignored. Field values are subject to permission checks - restricted fields will be null or omitted. (optional)

    try:
        # Get Employees
        api_response = api_instance.get_employees_list(filter=filter, sort=sort, page=page, fields=fields)
        print("The response of EmployeesApi->get_employees_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->get_employees_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**GetEmployeesFilterRequestObject**](.md)| Filters used to match employees. Encode filter properties using deepObject style. If the caller does not have access to the filtered field on a matching employee, that employee is excluded from the results to avoid leaking sensitive data. | [optional] 
 **sort** | **str**| Comma-separated list of sortable fields. Prefix a field with \&quot;-\&quot; for descending order. Allowed fields: &#x60;employeeId&#x60;, &#x60;firstName&#x60;, &#x60;lastName&#x60;, &#x60;preferredName&#x60;, &#x60;jobTitleName&#x60;, &#x60;status&#x60;. Nulls sort first in ascending order and last in descending order. If the caller does not have access to the sort field for an employee, that employee is excluded from the final result set to avoid leaking sensitive information. | [optional] 
 **page** | [**CursorPaginationQueryObject**](.md)| Cursor-based pagination parameters (&#x60;limit&#x60;, &#x60;after&#x60;, &#x60;before&#x60;). | [optional] 
 **fields** | **str**| Comma-separated list of additional fields to include in the response. Default fields (employeeId, firstName, lastName, preferredName, photoUrl, jobTitleName, status) are always included. Invalid field names are silently ignored. Field values are subject to permission checks - restricted fields will be null or omitted. | [optional] 

### Return type

[**GetEmployeesResponseObject**](GetEmployeesResponseObject.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Employees retrieved successfully |  -  |
**400** | Bad Request — invalid parameters provided. |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_employee**
> update_employee(id, employee)

Update Employee

Update an employee, based on employee ID. If employee is currently on a pay schedule syncing with Trax Payroll, or being added to one, the API user will need to update the employee with all of the following required fields for the update to be successful (listed by API field name): employeeNumber, firstName, lastName, dateOfBirth, ssn or ein, gender, maritalStatus, hireDate, address1, city, state, country, employmentHistoryStatus, exempt, payType, payRate, payPer, location, department, and division.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.employee import Employee
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
    api_instance = bamboohr_sdk.EmployeesApi(api_client)
    id = 'id_example' # str | {id} is an employee ID.
    employee = bamboohr_sdk.Employee() # Employee | 

    try:
        # Update Employee
        api_instance.update_employee(id, employee)
    except Exception as e:
        print("Exception when calling EmployeesApi->update_employee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| {id} is an employee ID. | 
 **employee** | [**Employee**](Employee.md)|  | 

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
**200** | Employee updated successfully. |  -  |
**400** | Provided JSON is bad or user is missing required fields. |  -  |
**403** | If the user doesn\\&#39;t have perms to see the employee or the user doesn\\&#39;t have perms to update ANY of the requested fields. |  -  |
**404** | If the employee to be updated doesn\\&#39;t exist. |  -  |
**409** | If an employee field was given an invalid value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

