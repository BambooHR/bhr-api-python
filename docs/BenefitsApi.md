# bamboohr_sdk.BenefitsApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_employee_dependent**](BenefitsApi.md#create_employee_dependent) | **POST** /api/v1/employeedependents | Create Employee Dependent
[**get_employee_dependent**](BenefitsApi.md#get_employee_dependent) | **GET** /api/v1/employeedependents/{id} | Get Employee Dependent
[**list_benefit_coverages**](BenefitsApi.md#list_benefit_coverages) | **GET** /api/v1/benefitcoverages | List Benefit Coverages
[**list_benefit_deduction_types**](BenefitsApi.md#list_benefit_deduction_types) | **GET** /api/v1/benefits/settings/deduction_types/all | List Benefit Deduction Types
[**list_company_benefits**](BenefitsApi.md#list_company_benefits) | **GET** /api/v1/benefit/company_benefit | List Company Benefits
[**list_employee_benefits**](BenefitsApi.md#list_employee_benefits) | **GET** /api/v1/benefit/employee_benefit | List Employee Benefits
[**list_employee_dependents**](BenefitsApi.md#list_employee_dependents) | **GET** /api/v1/employeedependents | List Employee Dependents
[**list_member_benefit_events**](BenefitsApi.md#list_member_benefit_events) | **GET** /api/v1/benefit/member_benefit | List Member Benefit Events
[**list_member_benefits**](BenefitsApi.md#list_member_benefits) | **GET** /api/v1/benefits/member-benefits | List Member Benefits
[**update_employee_dependent**](BenefitsApi.md#update_employee_dependent) | **PUT** /api/v1/employeedependents/{id} | Update Employee Dependent


# **create_employee_dependent**
> EmployeeDependentsResponse create_employee_dependent(employee_dependent)

Create Employee Dependent

Creates a new dependent record for an employee. `employeeId` is required and must reference a valid employee. `relationship` must be a valid relationship type and `gender` must be a valid gender value. `isUsCitizen` and `isStudent` accept "yes" or "no". `state` accepts a state code (e.g. "UT") and `country` accepts an ISO 3166-1 alpha-2 country code (e.g. "US"). `dateOfBirth` must be in YYYY-MM-DD format. SSN and SIN are accepted as plain text and stored encrypted. Accepts both `application/json` and `application/xml` request bodies. The response format mirrors the request `Content-Type` (not the `Accept` header): JSON request bodies receive a JSON response; XML request bodies receive an XML response. A successful creation fires an internal dependent-created event that may trigger downstream benefit enrollment processing.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.employee_dependent import EmployeeDependent
from bamboohr_sdk.models.employee_dependents_response import EmployeeDependentsResponse
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
    api_instance = bamboohr_sdk.BenefitsApi(api_client)
    employee_dependent = bamboohr_sdk.EmployeeDependent() # EmployeeDependent | 

    try:
        # Create Employee Dependent
        api_response = api_instance.create_employee_dependent(employee_dependent)
        print("The response of BenefitsApi->create_employee_dependent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BenefitsApi->create_employee_dependent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_dependent** | [**EmployeeDependent**](EmployeeDependent.md)|  | 

### Return type

[**EmployeeDependentsResponse**](EmployeeDependentsResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly created dependent record. Format matches the request Content-Type (JSON or XML). |  -  |
**400** | The request body is invalid or contains a validation error (e.g. missing employeeId, invalid relationship, gender, state code, country code, or date format). |  -  |
**403** | The authenticated user does not have permission to add a dependent. |  -  |
**409** | A duplicate record conflict was detected. |  -  |
**500** | An unexpected server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_dependent**
> EmployeeDependentsResponse get_employee_dependent(id, accept_header_parameter=accept_header_parameter)

Get Employee Dependent

Returns the details of a single employee dependent by their dependent ID. The response is a JSON object with a top-level key "Employee Dependents" containing a single-element array. SSN and SIN are returned as masked values (e.g. "xxx-xx-1234"). State and country are returned as full names. Supports both JSON and XML response formats via the Accept header. Requires Benefits Administration permissions.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.employee_dependents_response import EmployeeDependentsResponse
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
    api_instance = bamboohr_sdk.BenefitsApi(api_client)
    id = 56 # int | The numeric ID of the employee dependent to retrieve.
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)

    try:
        # Get Employee Dependent
        api_response = api_instance.get_employee_dependent(id, accept_header_parameter=accept_header_parameter)
        print("The response of BenefitsApi->get_employee_dependent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BenefitsApi->get_employee_dependent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The numeric ID of the employee dependent to retrieve. | 
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 

### Return type

[**EmployeeDependentsResponse**](EmployeeDependentsResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested employee dependent. |  -  |
**400** | The specified dependent ID was not found. |  -  |
**403** | The authenticated user does not have Benefits Administration permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_benefit_coverages**
> BenefitCoveragesResponse list_benefit_coverages(accept_header_parameter=accept_header_parameter)

List Benefit Coverages

Returns all benefit coverage levels configured in the company, such as Employee Only, Employee + Spouse, and Employee + Family. The JSON response wraps results under a "Benefit Coverages" key. Each coverage level includes an ID, short name, optional description, sort order, and an associated benefit plan ID (null for company-wide levels). Requires Benefits Administration permissions or owner/admin access.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.benefit_coverages_response import BenefitCoveragesResponse
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
    api_instance = bamboohr_sdk.BenefitsApi(api_client)
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)

    try:
        # List Benefit Coverages
        api_response = api_instance.list_benefit_coverages(accept_header_parameter=accept_header_parameter)
        print("The response of BenefitsApi->list_benefit_coverages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BenefitsApi->list_benefit_coverages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 

### Return type

[**BenefitCoveragesResponse**](BenefitCoveragesResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of benefit coverage levels ordered by sort order. |  -  |
**403** | The authenticated user does not have Benefits Administration permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_benefit_deduction_types**
> List[BenefitDeductionType] list_benefit_deduction_types()

List Benefit Deduction Types

Returns all benefit deduction types available in the system. Each deduction type describes a category of payroll deduction (e.g. 401(k), HSA, Section 125) along with its allowable benefit plan types, default deduction code, and optional sub-types. Some deduction types are grouped under a parent with sub-types (e.g. Pre-Tax groups Health, Dental, etc.); in that case the parent entry has a non-empty `subTypes` array. Requires Benefits Administration permissions.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.benefit_deduction_type import BenefitDeductionType
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
    api_instance = bamboohr_sdk.BenefitsApi(api_client)

    try:
        # List Benefit Deduction Types
        api_response = api_instance.list_benefit_deduction_types()
        print("The response of BenefitsApi->list_benefit_deduction_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BenefitsApi->list_benefit_deduction_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[BenefitDeductionType]**](BenefitDeductionType.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of benefit deduction type objects. |  -  |
**403** | The authenticated user does not have Benefits Administration permissions. |  -  |
**500** | An unexpected server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_company_benefits**
> CompanyBenefitsListResponse list_company_benefits()

List Company Benefits

Returns all active (non-deleted) company benefit plans for the account. Each plan includes summary-level fields such as name, benefit category type, associated vendor and deduction IDs, effective date range, and catch-up eligibility flags. Deleted plans are excluded. To retrieve full detail for a specific plan (including SSO URL, description, and ACA fields), use "Get a company benefit".

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.company_benefits_list_response import CompanyBenefitsListResponse
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
    api_instance = bamboohr_sdk.BenefitsApi(api_client)

    try:
        # List Company Benefits
        api_response = api_instance.list_company_benefits()
        print("The response of BenefitsApi->list_company_benefits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BenefitsApi->list_company_benefits: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CompanyBenefitsListResponse**](CompanyBenefitsListResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object containing a companyBenefits array of benefit plan summaries. |  -  |
**401** | Unauthorized. Invalid or missing authentication credentials. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_employee_benefits**
> EmployeeBenefitsListResponse list_employee_benefits(employee_benefit_filters)

List Employee Benefits

Returns current and scheduled-future benefit enrollment records, grouped by employee. The response is a JSON object with a single `employeeBenefits` array where each entry contains the employee ID, the employee's current pay frequency (null when no pay schedule is set), and an `employeeBenefit` array of per-plan records that includes both the current enrollment record and any scheduled future-change records for that plan. Each record includes enrollment status, deduction date range, currency, occurrences-per-year, and the full employee/employer cost-sharing fields.

A JSON request body with a `filters` object is required, and the `filters` object must contain at least one of `employeeId`, `companyBenefitId`, or `enrollmentStatusEffectiveDate`. Any combination is accepted. Providing no `filters` object or an empty `filters` object returns a 400 validation error. Filtering by `companyBenefitId` or `enrollmentStatusEffectiveDate` returns enrollments for every accessible employee, so the response can contain many entries. Use **List Company Benefits** (`list-company-benefits`) to look up valid `companyBenefitId` values.

Future-enrollment records are silently omitted when the authenticated user lacks permission to view scheduled benefit changes. Current enrollment records continue to be returned. An empty `employeeBenefit` array on a known employee can mean either no enrollments or that the caller cannot view them.

Note: This endpoint accepts filters inside a JSON request body on a `GET` request, which is non-standard. Some HTTP clients, proxies, and gateways may strip request bodies from GET requests, which can produce confusing missing-filter behavior. Callers experiencing validation errors should verify that the request body is being preserved. A query-parameter-based endpoint will be released in the future.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.employee_benefit_filters import EmployeeBenefitFilters
from bamboohr_sdk.models.employee_benefits_list_response import EmployeeBenefitsListResponse
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
    api_instance = bamboohr_sdk.BenefitsApi(api_client)
    employee_benefit_filters = bamboohr_sdk.EmployeeBenefitFilters() # EmployeeBenefitFilters | Filters that scope the results. The `filters` object is required, and at least one of `employeeId`, `companyBenefitId`, or `enrollmentStatusEffectiveDate` must be provided. Any combination of the three is accepted.

    try:
        # List Employee Benefits
        api_response = api_instance.list_employee_benefits(employee_benefit_filters)
        print("The response of BenefitsApi->list_employee_benefits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BenefitsApi->list_employee_benefits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_benefit_filters** | [**EmployeeBenefitFilters**](EmployeeBenefitFilters.md)| Filters that scope the results. The &#x60;filters&#x60; object is required, and at least one of &#x60;employeeId&#x60;, &#x60;companyBenefitId&#x60;, or &#x60;enrollmentStatusEffectiveDate&#x60; must be provided. Any combination of the three is accepted. | 

### Return type

[**EmployeeBenefitsListResponse**](EmployeeBenefitsListResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object containing an employeeBenefits array, each item representing one employee&#39;s benefit enrollments. |  -  |
**400** | Bad request. The request body is missing or not valid JSON, the &#x60;filters&#x60; object is missing, none of &#x60;employeeId&#x60;, &#x60;companyBenefitId&#x60;, or &#x60;enrollmentStatusEffectiveDate&#x60; was provided, or &#x60;enrollmentStatusEffectiveDate&#x60; is not in &#x60;YYYY-MM-DD&#x60; format. |  -  |
**401** | Unauthorized. Invalid or missing authentication credentials. |  -  |
**403** | Forbidden. The authenticated caller does not have permission to view benefit data. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_employee_dependents**
> EmployeeDependentsResponse list_employee_dependents(accept_header_parameter=accept_header_parameter, employeeid=employeeid)

List Employee Dependents

Returns employee dependents for the company. When `employeeid` is provided, only dependents for that employee are returned. When omitted, all dependents across all employees are returned. The response is a JSON object with a top-level key "Employee Dependents" containing an array of dependent objects. SSN and SIN are returned as masked values (e.g. "xxx-xx-1234"). State and country are returned as full names. Supports both JSON and XML response formats via the Accept header. Requires Benefits Administration permissions.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.employee_dependents_response import EmployeeDependentsResponse
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
    api_instance = bamboohr_sdk.BenefitsApi(api_client)
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)
    employeeid = 56 # int | The employee ID to filter dependents by. When provided, only dependents for that employee are returned. When omitted, all company dependents are returned. (optional)

    try:
        # List Employee Dependents
        api_response = api_instance.list_employee_dependents(accept_header_parameter=accept_header_parameter, employeeid=employeeid)
        print("The response of BenefitsApi->list_employee_dependents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BenefitsApi->list_employee_dependents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 
 **employeeid** | **int**| The employee ID to filter dependents by. When provided, only dependents for that employee are returned. When omitted, all company dependents are returned. | [optional] 

### Return type

[**EmployeeDependentsResponse**](EmployeeDependentsResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of employee dependents. |  -  |
**403** | The authenticated user does not have Benefits Administration permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_member_benefit_events**
> MemberBenefitEventsResponse list_member_benefit_events()

List Member Benefit Events

Returns benefit enrollment events for all employees and their dependents over the past year, organized by member. Each entry identifies a member (employee or dependent) and lists their per-plan coverage events (eligibility granted, enrolled, or loss of coverage), sorted chronologically. Requires benefit settings access.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.member_benefit_events_response import MemberBenefitEventsResponse
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
    api_instance = bamboohr_sdk.BenefitsApi(api_client)

    try:
        # List Member Benefit Events
        api_response = api_instance.list_member_benefit_events()
        print("The response of BenefitsApi->list_member_benefit_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BenefitsApi->list_member_benefit_events: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MemberBenefitEventsResponse**](MemberBenefitEventsResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object containing a members array of member benefit event records. |  -  |
**401** | Unauthorized. Invalid or missing authentication credentials. |  -  |
**403** | Forbidden. The authenticated user does not have benefit settings access. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_member_benefits**
> MemberBenefitsGetSuccessResponse list_member_benefits(calendar_year, page=page, page_size=page_size)

List Member Benefits

Returns a paginated list of benefit enrollment records for all members (employees and dependents) in the company for a given calendar year. Each record represents one member and includes the plans they held and the date ranges during which they held each enrollment status. Dependents appear alongside their subscribing employee via subscriberId. Use "List Company Benefits" to get valid planId values.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.member_benefits_get_success_response import MemberBenefitsGetSuccessResponse
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
    api_instance = bamboohr_sdk.BenefitsApi(api_client)
    calendar_year = '2024' # str | The 4-digit calendar year (YYYY) to retrieve benefit enrollment data for.
    page = '1' # str | The 1-based page number for pagination. The value is cast to an integer; values that cast to 0 or below are rejected with a 400. Defaults to 1. (optional) (default to '1')
    page_size = '25' # str | The number of items per page. The value is cast to an integer; values that cast to 0 or below, or to 100 or above, are rejected with a 400. Defaults to 25. (optional) (default to '25')

    try:
        # List Member Benefits
        api_response = api_instance.list_member_benefits(calendar_year, page=page, page_size=page_size)
        print("The response of BenefitsApi->list_member_benefits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BenefitsApi->list_member_benefits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar_year** | **str**| The 4-digit calendar year (YYYY) to retrieve benefit enrollment data for. | 
 **page** | **str**| The 1-based page number for pagination. The value is cast to an integer; values that cast to 0 or below are rejected with a 400. Defaults to 1. | [optional] [default to &#39;1&#39;]
 **page_size** | **str**| The number of items per page. The value is cast to an integer; values that cast to 0 or below, or to 100 or above, are rejected with a 400. Defaults to 25. | [optional] [default to &#39;25&#39;]

### Return type

[**MemberBenefitsGetSuccessResponse**](MemberBenefitsGetSuccessResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of member benefit enrollment records for the requested calendar year. |  -  |
**400** | Validation error. Returned when calendarYear is missing or not a 4-digit year, or when page or pageSize are out of range. |  -  |
**403** | Permission denied. The authenticated user is not a benefit admin. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_employee_dependent**
> EmployeeDependentsResponse update_employee_dependent(id, employee_dependent)

Update Employee Dependent

Replaces all fields on an existing employee dependent record. The request body must contain the full desired state of the dependent — omitted fields are written as empty or null, not preserved. `employeeId` is required and must reference a valid employee. `relationship` must be a valid relationship type and `gender` must be a valid gender value. `isUsCitizen` and `isStudent` accept "yes" or "no". `state` accepts a state code (e.g. "UT") and `country` accepts an ISO 3166-1 alpha-2 country code (e.g. "US"). `dateOfBirth` must be in YYYY-MM-DD format. SSN and SIN are accepted as plain text and stored encrypted. Accepts both `application/json` and `application/xml` request bodies. The response format mirrors the request `Content-Type` (not the `Accept` header): JSON request bodies receive a JSON response; XML request bodies receive an XML response. A successful update fires an internal dependent-updated event that may trigger downstream benefit enrollment processing.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.employee_dependent import EmployeeDependent
from bamboohr_sdk.models.employee_dependents_response import EmployeeDependentsResponse
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
    api_instance = bamboohr_sdk.BenefitsApi(api_client)
    id = 56 # int | The numeric ID of the employee dependent to update.
    employee_dependent = bamboohr_sdk.EmployeeDependent() # EmployeeDependent | 

    try:
        # Update Employee Dependent
        api_response = api_instance.update_employee_dependent(id, employee_dependent)
        print("The response of BenefitsApi->update_employee_dependent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BenefitsApi->update_employee_dependent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The numeric ID of the employee dependent to update. | 
 **employee_dependent** | [**EmployeeDependent**](EmployeeDependent.md)|  | 

### Return type

[**EmployeeDependentsResponse**](EmployeeDependentsResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated dependent record. Format matches the request Content-Type (JSON or XML). |  -  |
**400** | The request body is invalid or contains a validation error (e.g. invalid relationship, gender, state code, country code, or date format). |  -  |
**403** | The authenticated user does not have permission to update this dependent. |  -  |
**409** | A duplicate record conflict was detected. |  -  |
**500** | An unexpected server error occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

