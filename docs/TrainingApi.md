# bamboohr_sdk.TrainingApi

All URIs are relative to *https://companySubDomain.bamboohr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_employee_training_record**](TrainingApi.md#create_employee_training_record) | **POST** /api/v1/training/record/employee/{employeeId} | Create Employee Training Record
[**create_training_category**](TrainingApi.md#create_training_category) | **POST** /api/v1/training/category | Create Training Category
[**create_training_type**](TrainingApi.md#create_training_type) | **POST** /api/v1/training/type | Create Training Type
[**delete_employee_training_record**](TrainingApi.md#delete_employee_training_record) | **DELETE** /api/v1/training/record/{employeeTrainingRecordId} | Delete Employee Training Record
[**delete_training_category**](TrainingApi.md#delete_training_category) | **DELETE** /api/v1/training/category/{trainingCategoryId} | Delete Training Category
[**delete_training_type**](TrainingApi.md#delete_training_type) | **DELETE** /api/v1/training/type/{trainingTypeId} | Delete Training Type
[**list_employee_trainings**](TrainingApi.md#list_employee_trainings) | **GET** /api/v1/training/record/employee/{employeeId} | List Employee Training Records
[**list_training_categories**](TrainingApi.md#list_training_categories) | **GET** /api/v1/training/category | List Training Categories
[**list_training_types**](TrainingApi.md#list_training_types) | **GET** /api/v1/training/type | List Training Types
[**update_employee_training_record**](TrainingApi.md#update_employee_training_record) | **PUT** /api/v1/training/record/{employeeTrainingRecordId} | Update Employee Training Record
[**update_training_category**](TrainingApi.md#update_training_category) | **PUT** /api/v1/training/category/{trainingCategoryId} | Update Training Category
[**update_training_type**](TrainingApi.md#update_training_type) | **PUT** /api/v1/training/type/{trainingTypeId} | Update Training Type


# **create_employee_training_record**
> TrainingRecord create_employee_training_record(employee_id, create_employee_training_record_request)

Create Employee Training Record

Creates a new training record for the specified employee. The 'completed' date (yyyy-mm-dd) and 'type' (training type ID) are required. Optional fields include instructor, hours, credits, notes, and cost. The owner of the API key must have permission to add trainings for the employee.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.create_employee_training_record_request import CreateEmployeeTrainingRecordRequest
from bamboohr_sdk.models.training_record import TrainingRecord
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
    api_instance = bamboohr_sdk.TrainingApi(api_client)
    employee_id = 56 # int | The ID of the employee to add a training record to.
    create_employee_training_record_request = bamboohr_sdk.CreateEmployeeTrainingRecordRequest() # CreateEmployeeTrainingRecordRequest | Training object to post

    try:
        # Create Employee Training Record
        api_response = api_instance.create_employee_training_record(employee_id, create_employee_training_record_request)
        print("The response of TrainingApi->create_employee_training_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingApi->create_employee_training_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| The ID of the employee to add a training record to. | 
 **create_employee_training_record_request** | [**CreateEmployeeTrainingRecordRequest**](CreateEmployeeTrainingRecordRequest.md)| Training object to post | 

### Return type

[**TrainingRecord**](TrainingRecord.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_training_category**
> TrainingCategory create_training_category(create_training_category_request)

Create Training Category

Creates a new training category. The 'name' field is required. Returns the created TrainingCategory on success. The owner of the API key must have access to training settings.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.create_training_category_request import CreateTrainingCategoryRequest
from bamboohr_sdk.models.training_category import TrainingCategory
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
    api_instance = bamboohr_sdk.TrainingApi(api_client)
    create_training_category_request = bamboohr_sdk.CreateTrainingCategoryRequest() # CreateTrainingCategoryRequest | Training category to post

    try:
        # Create Training Category
        api_response = api_instance.create_training_category(create_training_category_request)
        print("The response of TrainingApi->create_training_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingApi->create_training_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_training_category_request** | [**CreateTrainingCategoryRequest**](CreateTrainingCategoryRequest.md)| Training category to post | 

### Return type

[**TrainingCategory**](TrainingCategory.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_training_type**
> TrainingType create_training_type(create_training_type_request)

Create Training Type

Creates a new training type. Only 'name' is required; all other fields are optional. When 'renewable' is true, 'frequency' (months between renewals) must also be provided. The 'dueFromHireDate' field is only valid when 'required' is true. The owner of the API key must have access to training settings.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.create_training_type_request import CreateTrainingTypeRequest
from bamboohr_sdk.models.training_type import TrainingType
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
    api_instance = bamboohr_sdk.TrainingApi(api_client)
    create_training_type_request = bamboohr_sdk.CreateTrainingTypeRequest() # CreateTrainingTypeRequest | Training object to post

    try:
        # Create Training Type
        api_response = api_instance.create_training_type(create_training_type_request)
        print("The response of TrainingApi->create_training_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingApi->create_training_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_training_type_request** | [**CreateTrainingTypeRequest**](CreateTrainingTypeRequest.md)| Training object to post | 

### Return type

[**TrainingType**](TrainingType.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_employee_training_record**
> delete_employee_training_record(employee_training_record_id)

Delete Employee Training Record

Delete an existing employee training record. The owner of the API key used must have permission to view and edit the employee and training type.

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
    api_instance = bamboohr_sdk.TrainingApi(api_client)
    employee_training_record_id = 56 # int | The ID of the training record to delete.

    try:
        # Delete Employee Training Record
        api_instance.delete_employee_training_record(employee_training_record_id)
    except Exception as e:
        print("Exception when calling TrainingApi->delete_employee_training_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_training_record_id** | **int**| The ID of the training record to delete. | 

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
**200** | Deleted successfully. No response body. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url or training record does not exist. |  -  |
**405** | Unable to delete training record. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_training_category**
> delete_training_category(training_category_id)

Delete Training Category

Delete an existing training category. The owner of the API key used must have access to training settings.

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
    api_instance = bamboohr_sdk.TrainingApi(api_client)
    training_category_id = 56 # int | The ID of the training category to delete.

    try:
        # Delete Training Category
        api_instance.delete_training_category(training_category_id)
    except Exception as e:
        print("Exception when calling TrainingApi->delete_training_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **training_category_id** | **int**| The ID of the training category to delete. | 

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
**200** | Deleted successfully. No response body. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url or training category does not exist. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_training_type**
> delete_training_type(training_type_id)

Delete Training Type

Delete an existing training type. The owner of the API key must have access to training settings. Deleting a training type will only be successful if all employee trainings for this type have been removed prior to this request.

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
    api_instance = bamboohr_sdk.TrainingApi(api_client)
    training_type_id = 56 # int | The ID of the training type to delete.

    try:
        # Delete Training Type
        api_instance.delete_training_type(training_type_id)
    except Exception as e:
        print("Exception when calling TrainingApi->delete_training_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **training_type_id** | **int**| The ID of the training type to delete. | 

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
**200** | Deleted successfully. No response body. |  -  |
**400** | Bad request. This also occurs when the training type still has associated employee records that must be removed first. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url or training type does not exist. |  -  |
**405** | Training type was unable to be deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_employee_trainings**
> TrainingRecordMap list_employee_trainings(employee_id, type=type)

List Employee Training Records

Returns all training records for the specified employee as an object keyed by training record ID. Use the optional 'type' query parameter to filter by training type ID. Fields such as instructor, credits, hours, and cost are only included when enabled in the company's training settings. The owner of the API key must have permission to view the employee.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.training_record_map import TrainingRecordMap
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
    api_instance = bamboohr_sdk.TrainingApi(api_client)
    employee_id = 56 # int | The ID of the employee to get a list of trainings for.
    type = 56 # int | Optional training type ID to filter records. Omitting this parameter returns all training records for the employee. (optional)

    try:
        # List Employee Training Records
        api_response = api_instance.list_employee_trainings(employee_id, type=type)
        print("The response of TrainingApi->list_employee_trainings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingApi->list_employee_trainings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**| The ID of the employee to get a list of trainings for. | 
 **type** | **int**| Optional training type ID to filter records. Omitting this parameter returns all training records for the employee. | [optional] 

### Return type

[**TrainingRecordMap**](TrainingRecordMap.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns training records keyed by record ID, or an empty array when the employee has no records. |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_training_categories**
> Dict[str, TrainingCategory] list_training_categories()

List Training Categories

Returns all training categories for the company as an object keyed by category ID. Each entry contains the category ID and name. The owner of the API key must have access to training settings.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.training_category import TrainingCategory
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
    api_instance = bamboohr_sdk.TrainingApi(api_client)

    try:
        # List Training Categories
        api_response = api_instance.list_training_categories()
        print("The response of TrainingApi->list_training_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingApi->list_training_categories: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dict[str, TrainingCategory]**](TrainingCategory.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all training categories as an object keyed by category ID. |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_training_types**
> Dict[str, TrainingType] list_training_types()

List Training Types

Returns all training types for the company as an object keyed by training type ID. Each entry includes the training name, renewable status, renewal frequency, required status, due-date window for new hires, category, link URL, description, and self-completion permission. The owner of the API key must have access to training settings.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.training_type import TrainingType
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
    api_instance = bamboohr_sdk.TrainingApi(api_client)

    try:
        # List Training Types
        api_response = api_instance.list_training_types()
        print("The response of TrainingApi->list_training_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingApi->list_training_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dict[str, TrainingType]**](TrainingType.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all training types as an object keyed by training type ID. |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_employee_training_record**
> TrainingRecord update_employee_training_record(employee_training_record_id, update_employee_training_record_request)

Update Employee Training Record

Updates an existing employee training record. The 'completed' date (yyyy-mm-dd) is required; all other fields are optional. Returns the updated TrainingRecord with HTTP 201. Returns 405 when the record cannot be updated. The owner of the API key must have permission to edit trainings for the employee.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.training_record import TrainingRecord
from bamboohr_sdk.models.update_employee_training_record_request import UpdateEmployeeTrainingRecordRequest
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
    api_instance = bamboohr_sdk.TrainingApi(api_client)
    employee_training_record_id = 56 # int | The ID of the training record to update.
    update_employee_training_record_request = bamboohr_sdk.UpdateEmployeeTrainingRecordRequest() # UpdateEmployeeTrainingRecordRequest | Training object to update

    try:
        # Update Employee Training Record
        api_response = api_instance.update_employee_training_record(employee_training_record_id, update_employee_training_record_request)
        print("The response of TrainingApi->update_employee_training_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingApi->update_employee_training_record: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_training_record_id** | **int**| The ID of the training record to update. | 
 **update_employee_training_record_request** | [**UpdateEmployeeTrainingRecordRequest**](UpdateEmployeeTrainingRecordRequest.md)| Training object to update | 

### Return type

[**TrainingRecord**](TrainingRecord.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Updated |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |
**405** | Training record could not be updated. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_training_category**
> TrainingCategory update_training_category(training_category_id, update_training_category_request)

Update Training Category

Updates the name of an existing training category. Returns 409 if a category with the same name already exists. The owner of the API key must have access to training settings.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.training_category import TrainingCategory
from bamboohr_sdk.models.update_training_category_request import UpdateTrainingCategoryRequest
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
    api_instance = bamboohr_sdk.TrainingApi(api_client)
    training_category_id = 56 # int | The ID of the training category to update.
    update_training_category_request = bamboohr_sdk.UpdateTrainingCategoryRequest() # UpdateTrainingCategoryRequest | Training category to update

    try:
        # Update Training Category
        api_response = api_instance.update_training_category(training_category_id, update_training_category_request)
        print("The response of TrainingApi->update_training_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingApi->update_training_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **training_category_id** | **int**| The ID of the training category to update. | 
 **update_training_category_request** | [**UpdateTrainingCategoryRequest**](UpdateTrainingCategoryRequest.md)| Training category to update | 

### Return type

[**TrainingCategory**](TrainingCategory.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated training category. |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |
**409** | A training category with the same name already exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_training_type**
> TrainingType update_training_type(training_type_id, update_training_type_request)

Update Training Type

Updates an existing training type. Only provided fields are updated. To remove a category, pass an empty string or null for the category field. Returns 405 when the training type cannot be modified. The owner of the API key must have access to training settings.

### Example

* Basic Authentication (basic):
* OAuth Authentication (oauth):

```python
import bamboohr_sdk
from bamboohr_sdk.models.training_type import TrainingType
from bamboohr_sdk.models.update_training_type_request import UpdateTrainingTypeRequest
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
    api_instance = bamboohr_sdk.TrainingApi(api_client)
    training_type_id = 56 # int | The ID of the training type to update.
    update_training_type_request = bamboohr_sdk.UpdateTrainingTypeRequest() # UpdateTrainingTypeRequest | Training type object to update to

    try:
        # Update Training Type
        api_response = api_instance.update_training_type(training_type_id, update_training_type_request)
        print("The response of TrainingApi->update_training_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrainingApi->update_training_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **training_type_id** | **int**| The ID of the training type to update. | 
 **update_training_type_request** | [**UpdateTrainingTypeRequest**](UpdateTrainingTypeRequest.md)| Training type object to update to | 

### Return type

[**TrainingType**](TrainingType.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated training type. |  -  |
**400** | Bad request parameters. |  -  |
**401** | Unauthorized. Invalid API credentials. |  -  |
**403** | Insufficient user permissions or API access is not turned on. |  -  |
**404** | Bad request url. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

