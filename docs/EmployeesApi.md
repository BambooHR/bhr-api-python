# bamboohr_sdk.EmployeesApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_employee**](EmployeesApi.md#create_employee) | **POST** /api/v1/employees | Create Employee
[**get_company_information**](EmployeesApi.md#get_company_information) | **GET** /api/v1/company_information | Get Company Information
[**get_employee**](EmployeesApi.md#get_employee) | **GET** /api/v1/employees/{id} | Get Employee
[**get_employees_directory**](EmployeesApi.md#get_employees_directory) | **GET** /api/v1/employees/directory | Get Employee Directory
[**list_employees**](EmployeesApi.md#list_employees) | **GET** /api/v1/employees | List Employees
[**update_employee**](EmployeesApi.md#update_employee) | **POST** /api/v1/employees/{id} | Update Employee


# **create_employee**
> create_employee(post_new_employee)

Create Employee

Create a new employee. At minimum, provide a first name and last name in a JSON object or XML document. The request body schema lists commonly used fields, but any valid employee field name may be included as a key. To discover available field names, call the list-fields endpoint (operationId: list-fields, GET /api/v1/meta/fields).

Trax Payroll note: Employees added to a pay schedule synced with Trax Payroll must include the required payroll-related employee fields: employeeNumber, firstName, lastName, dateOfBirth, ssn or ein, gender, maritalStatus, hireDate, address1, city, state, country, employmentHistoryStatus, exempt, payType, payRate, payPer, location, department, and division.

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
        api_instance.create_employee(post_new_employee)
    except Exception as e:
        print("Exception when calling EmployeesApi->create_employee: %s\n" % e)
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

 - **Content-Type**: application/json, application/xml, text/xml
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Employee created successfully. No response body is returned. The Location header points to the new employee resource. |  * Location - The URL to view the employee in the web app. The ID of the employee will be included. <br>  |
**400** | If the posted XML or JSON is invalid or the minimum fields are not provided. |  -  |
**403** | If the API user does not have permission to add an employee. |  -  |
**409** | If an employee field was given an invalid value. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_information**
> CompanyInformation get_company_information()

Get Company Information

Returns basic profile information for the company, including its legal name, display name, primary address, and contact phone number. For companies using BambooHR Payroll, the legal name and address are sourced from the active payroll client metadata; for all other companies, the data comes from the company's account settings.

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
**200** | Company information retrieved successfully. |  -  |
**403** | The API user does not have permission to access company information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee**
> Dict[str, EmployeeValue] get_employee(id, fields=fields, only_current=only_current, accept_header_parameter=accept_header_parameter)

Get Employee

Returns employee data for the specified employee ID. Specify which fields to return using the `fields` query parameter (comma-separated list of field names). See the List Fields endpoint (operationId: list-fields, GET /api/v1/meta/fields) for available field names. This endpoint is suitable for retrieving basic employee information, including current values from historical tables such as job title or compensation. By default only current values are returned; set `onlyCurrent` to false to include future-dated values from historical table fields.

Usage note: The maximum number of fields per request is 400.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.employee_value import EmployeeValue
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
    id = 'id_example' # str | The employee ID. The special employee ID of zero (0) means to use the employee ID associated with the API key (if any).
    fields = 'firstName,lastName' # str | Comma-separated list of field names to include in the response. See the List Fields endpoint for valid field names. (optional) (default to 'firstName,lastName')
    only_current = True # bool | Setting to false will return future-dated values from history table fields. Defaults to true. (optional) (default to True)
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)

    try:
        # Get Employee
        api_response = api_instance.get_employee(id, fields=fields, only_current=only_current, accept_header_parameter=accept_header_parameter)
        print("The response of EmployeesApi->get_employee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->get_employee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The employee ID. The special employee ID of zero (0) means to use the employee ID associated with the API key (if any). | 
 **fields** | **str**| Comma-separated list of field names to include in the response. See the List Fields endpoint for valid field names. | [optional] [default to &#39;firstName,lastName&#39;]
 **only_current** | **bool**| Setting to false will return future-dated values from history table fields. Defaults to true. | [optional] [default to True]
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 

### Return type

[**Dict[str, EmployeeValue]**](EmployeeValue.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A dictionary of the requested employee fields and their values. Fields the caller does not have permission to view are omitted. |  -  |
**400** | The request exceeded the maximum number of allowed fields (400). |  -  |
**403** | The API user does not have permission to see the requested employee. |  -  |
**404** | The employee does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employees_directory**
> JsonDirectoryEmployee get_employees_directory(accept_header_parameter=accept_header_parameter, only_current=only_current)

Get Employee Directory

Returns the company employee directory, including a fieldset definition and an array of employee records. By default only current (active) employees are returned; pass onlyCurrent=false to include terminated employees. If the caller has org-chart access but not full directory access, a reduced fieldset is returned. Returns 403 if neither directory nor org-chart sharing is enabled for the company. Returns 404 if the directory is empty. The response format is controlled by the Accept header.

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
    only_current = True # bool | When true (the default), only active employees are returned. Set to false to include terminated employees. (optional) (default to True)

    try:
        # Get Employee Directory
        api_response = api_instance.get_employees_directory(accept_header_parameter=accept_header_parameter, only_current=only_current)
        print("The response of EmployeesApi->get_employees_directory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->get_employees_directory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 
 **only_current** | **bool**| When true (the default), only active employees are returned. Set to false to include terminated employees. | [optional] [default to True]

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
**200** | Employee directory with fieldset definitions and employee data. |  -  |
**403** | The company directory is not shared company-wide and the caller does not have org-chart access. |  -  |
**404** | The directory is empty. |  -  |
**500** | An internal server error occurred while generating the directory report. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_employees**
> GetEmployeesResponseObject list_employees(filter=filter, sort=sort, fields=fields, page=page)

List Employees

Returns a paginated list of employees with optional filtering and sorting. Each employee record always includes: `employeeId`, `firstName`, `lastName`, `preferredName`, `photoUrl`, `jobTitleName`, and `status`. The `_restrictedFields` property is only present when at least one requested field is restricted by permissions — it is omitted entirely on unrestricted records. Use the `fields` parameter to request up to 14 additional contact/social fields. The `status` field is returned as title-case (e.g., `Active`, `Inactive`). For richer employee field data, use the Get Employee endpoint or the Datasets API.

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
    fields = 'workEmail,mobilePhone' # str | Comma-separated list of additional fields to include in the response beyond the default set. Supported values: `workEmail`, `homeEmail`, `bestEmail`, `middleName`, `workPhone`, `workPhoneExtension`, `mobilePhone`, `homePhone`, `skypeUsername`, `linkedinUrl`, `facebookUrl`, `instagramUrl`, `twitterUrl`, `pinterestUrl`. Unrecognized field names are silently ignored. Field values are subject to permission checks — restricted fields will be null or omitted and the field name will appear in `_restrictedFields`. (optional)
    page = bamboohr_sdk.CursorPaginationQueryObject() # CursorPaginationQueryObject | Cursor-based pagination parameters (`limit`, `after`, `before`). (optional)

    try:
        # List Employees
        api_response = api_instance.list_employees(filter=filter, sort=sort, fields=fields, page=page)
        print("The response of EmployeesApi->list_employees:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->list_employees: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**GetEmployeesFilterRequestObject**](.md)| Filters used to match employees. Encode filter properties using deepObject style. If the caller does not have access to the filtered field on a matching employee, that employee is excluded from the results to avoid leaking sensitive data. | [optional] 
 **sort** | **str**| Comma-separated list of sortable fields. Prefix a field with \&quot;-\&quot; for descending order. Allowed fields: &#x60;employeeId&#x60;, &#x60;firstName&#x60;, &#x60;lastName&#x60;, &#x60;preferredName&#x60;, &#x60;jobTitleName&#x60;, &#x60;status&#x60;. Nulls sort first in ascending order and last in descending order. If the caller does not have access to the sort field for an employee, that employee is excluded from the final result set to avoid leaking sensitive information. | [optional] 
 **fields** | **str**| Comma-separated list of additional fields to include in the response beyond the default set. Supported values: &#x60;workEmail&#x60;, &#x60;homeEmail&#x60;, &#x60;bestEmail&#x60;, &#x60;middleName&#x60;, &#x60;workPhone&#x60;, &#x60;workPhoneExtension&#x60;, &#x60;mobilePhone&#x60;, &#x60;homePhone&#x60;, &#x60;skypeUsername&#x60;, &#x60;linkedinUrl&#x60;, &#x60;facebookUrl&#x60;, &#x60;instagramUrl&#x60;, &#x60;twitterUrl&#x60;, &#x60;pinterestUrl&#x60;. Unrecognized field names are silently ignored. Field values are subject to permission checks — restricted fields will be null or omitted and the field name will appear in &#x60;_restrictedFields&#x60;. | [optional] 
 **page** | [**CursorPaginationQueryObject**](.md)| Cursor-based pagination parameters (&#x60;limit&#x60;, &#x60;after&#x60;, &#x60;before&#x60;). | [optional] 

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

Update an employee's fields by submitting a JSON object or XML document containing field name/value pairs. The request body schema lists commonly used fields, but any valid employee field name may be used as a key. To discover available field names, call the list-fields endpoint (operationId: list-fields, GET /api/v1/meta/fields).

Trax Payroll note: If the employee is currently on a pay schedule syncing with Trax Payroll, or is being added to one, the request must include the required payroll-related employee fields: employeeNumber, firstName, lastName, dateOfBirth, ssn or ein, gender, maritalStatus, hireDate, address1, city, state, country, employmentHistoryStatus, exempt, payType, payRate, payPer, location, department, and division.

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
    id = 'id_example' # str | The employee ID.
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
 **id** | **str**| The employee ID. | 
 **employee** | [**Employee**](Employee.md)|  | 

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
**200** | Employee updated successfully. No response body is returned. |  -  |
**400** | Provided JSON is malformed, or required fields are missing. |  -  |
**403** | The API user does not have permission to see the employee or to update any of the requested fields. |  -  |
**404** | The employee does not exist. |  -  |
**409** | A field was given an invalid value (e.g., duplicate email, invalid state/country, incompatible pay type). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

