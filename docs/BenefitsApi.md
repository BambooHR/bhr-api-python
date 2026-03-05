# bamboohr_sdk.BenefitsApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_employee_dependent**](BenefitsApi.md#add_employee_dependent) | **POST** /api/v1/employeedependents | Create Employee Dependent
[**get_benefit_coverages**](BenefitsApi.md#get_benefit_coverages) | **GET** /api/v1/benefitcoverages | Get Benefit Coverages
[**get_benefit_deduction_types**](BenefitsApi.md#get_benefit_deduction_types) | **GET** /api/v1/benefits/settings/deduction_types/all | Get Benefit Deduction Types
[**get_company_benefits**](BenefitsApi.md#get_company_benefits) | **GET** /api/v1/benefit/company_benefit | Get Company Benefits
[**get_employee_benefit**](BenefitsApi.md#get_employee_benefit) | **GET** /api/v1/benefit/employee_benefit | Get Employee Benefits
[**get_employee_dependent**](BenefitsApi.md#get_employee_dependent) | **GET** /api/v1/employeedependents/{id} | Get Employee Dependent
[**get_employee_dependents**](BenefitsApi.md#get_employee_dependents) | **GET** /api/v1/employeedependents | Get Employee Dependents
[**get_member_benefit**](BenefitsApi.md#get_member_benefit) | **GET** /api/v1/benefit/member_benefit | Get Member Benefit Events
[**get_member_benefits**](BenefitsApi.md#get_member_benefits) | **GET** /api/v1/benefits/member-benefits | Get Member Benefits
[**update_employee_dependent**](BenefitsApi.md#update_employee_dependent) | **PUT** /api/v1/employeedependents/{id} | Update Employee Dependent


# **add_employee_dependent**
> add_employee_dependent(employee_dependent)

Create Employee Dependent

Adds an employee dependent

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.employee_dependent import EmployeeDependent
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
        api_instance.add_employee_dependent(employee_dependent)
    except Exception as e:
        print("Exception when calling BenefitsApi->add_employee_dependent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_dependent** | [**EmployeeDependent**](EmployeeDependent.md)|  | 

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
**200** | Dependent added |  -  |
**400** | if the posted JSON is invalid |  -  |
**403** | if the current user doesn\\&#39;t have access to add the dependent. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_benefit_coverages**
> get_benefit_coverages(accept_header_parameter=accept_header_parameter)

Get Benefit Coverages

Get benefit coverages

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
    api_instance = bamboohr_sdk.BenefitsApi(api_client)
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)

    try:
        # Get Benefit Coverages
        api_instance.get_benefit_coverages(accept_header_parameter=accept_header_parameter)
    except Exception as e:
        print("Exception when calling BenefitsApi->get_benefit_coverages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_benefit_deduction_types**
> get_benefit_deduction_types()

Get Benefit Deduction Types

Get benefit deduction types

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
    api_instance = bamboohr_sdk.BenefitsApi(api_client)

    try:
        # Get Benefit Deduction Types
        api_instance.get_benefit_deduction_types()
    except Exception as e:
        print("Exception when calling BenefitsApi->get_benefit_deduction_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_benefits**
> List[CompanyBenefitResponse] get_company_benefits()

Get Company Benefits

Get a list of company benefits

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.company_benefit_response import CompanyBenefitResponse
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
        # Get Company Benefits
        api_response = api_instance.get_company_benefits()
        print("The response of BenefitsApi->get_company_benefits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BenefitsApi->get_company_benefits: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CompanyBenefitResponse]**](CompanyBenefitResponse.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of company benefits |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_benefit**
> List[EmployeeBenefit] get_employee_benefit(accept_header_parameter=accept_header_parameter, employee_benefit_filters=employee_benefit_filters)

Get Employee Benefits

Get a list of employee benefits

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.employee_benefit import EmployeeBenefit
from bamboohr_sdk.models.employee_benefit_filters import EmployeeBenefitFilters
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
    employee_benefit_filters = bamboohr_sdk.EmployeeBenefitFilters() # EmployeeBenefitFilters | Employee Benefit Filters (optional)

    try:
        # Get Employee Benefits
        api_response = api_instance.get_employee_benefit(accept_header_parameter=accept_header_parameter, employee_benefit_filters=employee_benefit_filters)
        print("The response of BenefitsApi->get_employee_benefit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BenefitsApi->get_employee_benefit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 
 **employee_benefit_filters** | [**EmployeeBenefitFilters**](EmployeeBenefitFilters.md)| Employee Benefit Filters | [optional] 

### Return type

[**List[EmployeeBenefit]**](EmployeeBenefit.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a list of employee benefits |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_dependent**
> get_employee_dependent(id, accept_header_parameter=accept_header_parameter)

Get Employee Dependent

Get employee dependent

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
    api_instance = bamboohr_sdk.BenefitsApi(api_client)
    id = 'id_example' # str | {id} is the employee dependent ID.
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)

    try:
        # Get Employee Dependent
        api_instance.get_employee_dependent(id, accept_header_parameter=accept_header_parameter)
    except Exception as e:
        print("Exception when calling BenefitsApi->get_employee_dependent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| {id} is the employee dependent ID. | 
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee_dependents**
> get_employee_dependents(employeeid, accept_header_parameter=accept_header_parameter)

Get Employee Dependents

Get all employee dependents

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
    api_instance = bamboohr_sdk.BenefitsApi(api_client)
    employeeid = 'employeeid_example' # str | {employeeid} is the employee ID. Supplying this ID limits the response to the specific employee.
    accept_header_parameter = 'accept_header_parameter_example' # str | This endpoint can produce either JSON or XML. (optional)

    try:
        # Get Employee Dependents
        api_instance.get_employee_dependents(employeeid, accept_header_parameter=accept_header_parameter)
    except Exception as e:
        print("Exception when calling BenefitsApi->get_employee_dependents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employeeid** | **str**| {employeeid} is the employee ID. Supplying this ID limits the response to the specific employee. | 
 **accept_header_parameter** | **str**| This endpoint can produce either JSON or XML. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_member_benefit**
> List[MemberBenefitEvent] get_member_benefit()

Get Member Benefit Events

Get a list of member benefit events

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.member_benefit_event import MemberBenefitEvent
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
        # Get Member Benefit Events
        api_response = api_instance.get_member_benefit()
        print("The response of BenefitsApi->get_member_benefit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BenefitsApi->get_member_benefit: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MemberBenefitEvent]**](MemberBenefitEvent.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of member benefit events. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_member_benefits**
> MemberBenefitsGetSuccessResponse get_member_benefits(calendar_year, page=page, page_size=page_size)

Get Member Benefits

Retrieves a paginated list of member benefits for a specified calendar year. Returns benefit enrollment data including member IDs, subscriber IDs, plan IDs, and date ranges with enrollment status. Requires benefit admin permissions.

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
    calendar_year = '2024' # str | The 4-digit calendar year to retrieve benefits for
    page = '1' # str | The page number for pagination (optional) (default to '1')
    page_size = '25' # str | The number of items per page (must be less than 100) (optional) (default to '25')

    try:
        # Get Member Benefits
        api_response = api_instance.get_member_benefits(calendar_year, page=page, page_size=page_size)
        print("The response of BenefitsApi->get_member_benefits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BenefitsApi->get_member_benefits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar_year** | **str**| The 4-digit calendar year to retrieve benefits for | 
 **page** | **str**| The page number for pagination | [optional] [default to &#39;1&#39;]
 **page_size** | **str**| The number of items per page (must be less than 100) | [optional] [default to &#39;25&#39;]

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
**200** | Successfully retrieved member benefits |  -  |
**400** | Validation error |  -  |
**403** | Permission denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_employee_dependent**
> update_employee_dependent(id, employee_dependent)

Update Employee Dependent

This API allows you to change the information for a given dependent ID.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.employee_dependent import EmployeeDependent
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
    id = 'id_example' # str | {id} is the employee dependent ID.
    employee_dependent = bamboohr_sdk.EmployeeDependent() # EmployeeDependent | 

    try:
        # Update Employee Dependent
        api_instance.update_employee_dependent(id, employee_dependent)
    except Exception as e:
        print("Exception when calling BenefitsApi->update_employee_dependent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| {id} is the employee dependent ID. | 
 **employee_dependent** | [**EmployeeDependent**](EmployeeDependent.md)|  | 

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
**201** | Dependent updated |  -  |
**400** | if the posted JSON is invalid |  -  |
**403** | if the current user doesn\\&#39;t have access to change the dependent in this way. |  -  |
**500** | Server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

